"""Fetch citation counts from the Semantic Scholar Graph API.

Runs in CI (see .github/workflows/semantic_scholar_crawler.yaml) and writes the
results to ./results, which the workflow force-pushes to the
`semantic-scholar-stats` branch. The page reads that JSON from jsDelivr.

Why build time and not the browser: the anonymous Semantic Scholar pool is
rate limited hard (frequent HTTP 429), so a visitor's fetch would often come
back empty. Here we can retry with backoff.
"""

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

API = 'https://api.semanticscholar.org/graph/v1'
AUTHOR_ID = os.environ.get('SEMANTIC_SCHOLAR_AUTHOR_ID', '').strip()
API_KEY = os.environ.get('SEMANTIC_SCHOLAR_API_KEY', '').strip()
ABOUT_MD = os.path.join(os.path.dirname(__file__), '..', '_pages', 'about.md')

AUTHOR_FIELDS = 'name,citationCount,hIndex,paperCount,papers.paperId,papers.title,papers.year,papers.citationCount,papers.influentialCitationCount,papers.externalIds'
PAPER_FIELDS = 'paperId,title,year,citationCount,influentialCitationCount,externalIds'


def get(url, payload=None, tries=8):
    """GET/POST with backoff. Returns parsed JSON, or None if we never got a 200."""
    headers = {'User-Agent': 'Curry09.github.io citation crawler'}
    if API_KEY:
        headers['x-api-key'] = API_KEY
    data = None
    if payload is not None:
        data = json.dumps(payload).encode()
        headers['Content-Type'] = 'application/json'

    for attempt in range(tries):
        if attempt:
            time.sleep(min(2 ** attempt, 30))
        try:
            req = urllib.request.Request(url, data=data, headers=headers)
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as err:
            print(f'  attempt {attempt + 1}: HTTP {err.code}', file=sys.stderr)
            if err.code not in (429, 500, 502, 503, 504):
                return None
        except Exception as err:  # network hiccup
            print(f'  attempt {attempt + 1}: {err}', file=sys.stderr)
    return None


def arxiv_ids_on_page():
    """Every arXiv id linked from a publication box in _pages/about.md."""
    try:
        with open(ABOUT_MD, encoding='utf-8') as handle:
            text = handle.read()
    except OSError:
        return []
    # Only the Publications section, so News/Internships links don't leak in.
    body = text.split('# 📝', 1)[-1]
    seen = []
    for match in re.finditer(r'arxiv\.org/abs/([0-9]{4}\.[0-9]{4,5})', body, re.I):
        if match.group(1) not in seen:
            seen.append(match.group(1))
    return seen


def entry(paper):
    ext = paper.get('externalIds') or {}
    return {
        'paperId': paper.get('paperId'),
        'title': paper.get('title'),
        'year': paper.get('year'),
        'citationCount': paper.get('citationCount') or 0,
        'influentialCitationCount': paper.get('influentialCitationCount') or 0,
        'arxivId': ext.get('ArXiv'),
        'doi': ext.get('DOI'),
        'url': f"https://www.semanticscholar.org/paper/{paper.get('paperId')}",
    }


def shields(label, message):
    return {'schemaVersion': 1, 'label': label, 'message': str(message), 'color': 'fff'}


def main():
    papers = {}       # arXiv id -> entry
    extra = []        # entries without an arXiv id
    author = None

    if AUTHOR_ID:
        print(f'Fetching author {AUTHOR_ID}')
        author = get(f'{API}/author/{AUTHOR_ID}?fields={AUTHOR_FIELDS}')
        if author is None:
            print('Author lookup failed', file=sys.stderr)
        else:
            for paper in author.get('papers') or []:
                record = entry(paper)
                if record['arxivId']:
                    papers[record['arxivId']] = record
                else:
                    extra.append(record)

    # Anything linked on the page that the author profile missed (co-author
    # disambiguation slips) gets looked up directly.
    wanted = arxiv_ids_on_page()
    missing = [i for i in wanted if i not in papers]
    if missing:
        print(f'Looking up {len(missing)} paper(s) not on the author profile: {missing}')
        found = get(f'{API}/paper/batch?fields={PAPER_FIELDS}',
                    payload={'ids': [f'arXiv:{i}' for i in missing]})
        for arxiv_id, paper in zip(missing, found or []):
            if paper:
                papers[arxiv_id] = entry(paper)

    if not papers:
        print('No citation data retrieved; refusing to write empty results.', file=sys.stderr)
        return 1

    total = (author or {}).get('citationCount')
    if total is None:
        total = sum(p['citationCount'] for p in papers.values()) + sum(p['citationCount'] for p in extra)

    out = {
        'source': 'Semantic Scholar Graph API',
        'author_id': AUTHOR_ID or None,
        'name': (author or {}).get('name'),
        'citedby': total,
        'h_index': (author or {}).get('hIndex'),
        'paper_count': (author or {}).get('paperCount'),
        'updated': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'publications': papers,
        'publications_without_arxiv_id': extra,
    }

    os.makedirs('results', exist_ok=True)
    with open('results/s2_data.json', 'w', encoding='utf-8') as handle:
        json.dump(out, handle, ensure_ascii=False, indent=1)

    # shields.io endpoint badges, in case we ever want badges instead of text.
    with open('results/s2_data_shieldsio.json', 'w', encoding='utf-8') as handle:
        json.dump(shields('citations', total), handle, ensure_ascii=False)
    for arxiv_id, paper in papers.items():
        name = f'results/s2_{arxiv_id}_shieldsio.json'
        with open(name, 'w', encoding='utf-8') as handle:
            json.dump(shields('citations', paper['citationCount']), handle, ensure_ascii=False)

    print(f"\n{out['name']} -- {total} citations, h-index {out['h_index']}")
    for arxiv_id in wanted:
        paper = papers.get(arxiv_id)
        status = f"{paper['citationCount']:>5}" if paper else '    ?'
        print(f'  {status}  arXiv:{arxiv_id}  {(paper or {}).get("title", "NOT FOUND")}')
    return 0


if __name__ == '__main__':
    sys.exit(main())

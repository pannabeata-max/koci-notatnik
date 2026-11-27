"""Generate sitemap.xml from the canonical URLs of public article pages."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://koci-notatnik.pages.dev'
NS = 'http://www.sitemaps.org/schemas/sitemap/0.9'

class CanonicalParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonicals = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonicals.append(attrs.get('href', ''))

ET.register_namespace('', NS)
root = ET.Element(f'{{{NS}}}urlset')
seen = set()
for page in [ROOT / 'index.html', *sorted((ROOT / 'artykuly').glob('*.html'))]:
    parser = CanonicalParser()
    parser.feed(page.read_text(encoding='utf-8'))
    expected = BASE + ('/' if page.name == 'index.html' else '/artykuly/' + page.stem)
    if parser.canonicals != [expected]:
        raise ValueError(f'{page.name}: canonical must be {expected}')
    parts = urlsplit(expected)
    if parts.query or parts.fragment or expected in seen:
        raise ValueError(f'Duplicate or invalid canonical: {expected}')
    seen.add(expected)
    entry = ET.SubElement(root, f'{{{NS}}}url')
    ET.SubElement(entry, f'{{{NS}}}loc').text = expected
ET.indent(root, space='  ')
ET.ElementTree(root).write(ROOT / 'sitemap.xml', encoding='utf-8', xml_declaration=True)
print(f'Generated sitemap.xml: {len(seen)} canonical URLs')

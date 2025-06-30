from urllib.parse import urljoin, urlparse, parse_qs, urlencode
import requests
from bs4 import BeautifulSoup

visited = set()
testable_urls = set()

def strip_params_for_payload(url):
    parsed = urlparse(url)
    if not parsed.query:
        return None
    qs = parse_qs(parsed.query)
    clean_qs = {k: '' for k in qs}
    return parsed._replace(query=urlencode(clean_qs)).geturl()

def crawl(url):
    try:
        r = requests.get(url)
        visited.add(url)
        soup = BeautifulSoup(r.text, "html.parser")
        for a_tag in soup.find_all("a", href=True):
            link = urljoin(url, a_tag['href'])
            if urlparse(link).netloc == urlparse(url).netloc and link not in visited:
                clean_link = strip_params_for_payload(link)
                if clean_link:
                    testable_urls.add(clean_link)
                crawl(link)
    except:
        pass


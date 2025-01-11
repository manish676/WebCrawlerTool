import requests
import re
from urllib.parse import urljoin, urlparse

class Scanner:
    def __init__(self, url):
        # Ensure the URL has a scheme (http/https)
        if not urlparse(url).scheme:
            url = f"http://{url}"
        self.target_url = url
        self.target_links = []

    def extract_links(self, url):
        try:
            # Request the URL and extract href links
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return re.findall(r'href="(.*?)"', response.text)
        except requests.RequestException as e:
            print(f"❌ Failed to fetch {url}: {e}")
            return []

    def crawl(self, url):
        href_links = self.extract_links(url)

        for link in href_links:
            target_link = urljoin(url, link)
            target_link = target_link.split('#')[0]

            # Avoid crawling the same link again and ensure it's within the same domain
            if target_link not in self.target_links and self.target_url in target_link:
                self.target_links.append(target_link)
                print(f"🔗 Discovered: {target_link}")
                
                self.crawl(target_link)

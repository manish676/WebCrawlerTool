import requests
import re
from urllib.parse import urljoin  

class Scanner:
    
    def __init__(self, url):
        self.target_url = url
        self.target_links = []
    
    def extract_links(self, url):
        # Request the URL and extract href links
        response = requests.get(url)
        # Corrected regex pattern for extracting href attributes
        return re.findall(r'href="(.*?)"', str(response.content))

    def crawl(self, url):
        # Extract links from the current URL
        href_links = self.extract_links(url)
        
        # Loop through each link
        for link in href_links:
            # Join relative URLs to absolute URLs
            target_link = urljoin(url, link)
            
            # Avoid crawling the same link again
            if target_link not in self.target_links:
                self.target_links.append(target_link)
                print(target_link)  # Print the discovered link
                
                # Recursively crawl the new target link
                self.crawl(target_link)  # Pass target_link instead of url

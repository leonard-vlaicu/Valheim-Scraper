import requests

class Scraper:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def fetch_html(self, url: str):
        try:
            response: response = requests.get(url)
            response.raise_for_status()  # Raise an exception for 4xx and 5xx errors
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL: {e}")
            return None

    def scrape_page(self, page_url: str):
        url: str = self.base_url + page_url
        html_content: str = self.fetch_html(url)
        if html_content:
            return html_content
        else:
            return None

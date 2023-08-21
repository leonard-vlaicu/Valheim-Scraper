"""Module providing request functionality """
import requests

class Scraper:
    """Scraper class that fetches the html content from a given url"""

    def __init__(self, base_url: str):
        self.base_url = base_url

    def fetch_html(self):
        """tries to get the html content from the base url"""
        try:
            response: response = requests.get(self.base_url, timeout=5)
            response.raise_for_status()  # Raise an exception for 4xx and 5xx errors

            return response.text
        except requests.exceptions.RequestException as request_error:
            print(f"Error fetching URL: {request_error}")

            return None

    def scrape_page(self):
        """fetches the html content from the base_url and returns it as a string"""
        html_content: str = self.fetch_html()
        if html_content:
            return html_content
        else:
            return None

"""Module providing request functionality """
import requests

class Scraper:
    """Scraper class that fetches the html content from a given url"""

    def __init__(self, base_url: str):
        self.base_url = base_url

    def fetch_html(self):
        """tries to get the html content from the base url"""
        try:
            request_response: requests.Response = requests.get(self.base_url, timeout=5)
            request_response.raise_for_status()  # Raise an exception for 4xx and 5xx errors

            return request_response.text
        
        except requests.exceptions.RequestException as request_error:
            print(f"ERROR: {request_error}")

            return None

    def scrape_page(self):
        """fetches the html content from the base_url and returns it as a string"""
        html_content: str|None = self.fetch_html()

        if html_content:
            return html_content
        else:
            raise(TypeError("ERROR: No HTML content found!"))

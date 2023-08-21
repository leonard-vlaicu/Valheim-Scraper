"""Module for parsing html content"""
from bs4 import BeautifulSoup

class Parser:
    """Parser class that parses the html content"""
    def __init__(self, html_content: str):
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def get_soup(self):
        """returns the soup object"""
        return self.soup

    def get_soup_prettyfied(self):
        """returns the soup object prettyfied"""
        return self.soup.prettify()

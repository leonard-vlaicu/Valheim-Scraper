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

class TableParser:
    """Parser class that parses the html content for tables"""
    def __init__(self, html_content: str):
        self.soup = BeautifulSoup(html_content, 'html.parser')
        self.tables = self.soup.find_all('table')

    def get_table_by_index(self, index: int):
        """returns the table by index"""
        return self.tables[index]

    def get_tr_by_index(self, index: int):
        """returns the tr by table index"""
        return self.tables[index].find_all('tr')

    def get_tables(self):
        """returns the tables"""
        return self.tables
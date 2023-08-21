
from bs4 import BeautifulSoup

class Parser:
    def __init__(self, html_content: str):
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def getSoup(self):
        return self.soup
    
    def getSoupPrettyfied(self):
        return self.soup.prettify()
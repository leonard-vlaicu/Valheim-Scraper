from core.parser import Parser

class ArmourParser(Parser):
    """Parser class that parses the html content for armour"""
    def __init__(self, html_content: str):
        super().__init__(html_content)

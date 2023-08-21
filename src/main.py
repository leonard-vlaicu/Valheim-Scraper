from core.scraper import Scraper
from core.parser import Parser

def main():
    """Main function of the program."""
    main_scraper: Scraper = Scraper("https://www.google.com")
    html = main_scraper.scrape_page()

    main_parser: Parser = Parser(html)
    print(main_parser.get_soup_prettyfied())

if __name__ == "__main__":
    main()

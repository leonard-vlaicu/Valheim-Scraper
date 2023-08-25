from core.scraper import Scraper
from core.armour.armour_parser import ArmourParser
from core.parser import TableParser

def main():
    """Main function of the program."""
    main_scraper: Scraper = Scraper("https://valheim.fandom.com/wiki/Armor")

    try :
        html: str = main_scraper.scrape_page()

        armour_tables: list = []
        
        capes_table: list = []
        helmets_table: list = []
        chest_table: list = []
        legs_table: list = []

        table_parser: TableParser = TableParser(html)

        armour_parser: ArmourParser = ArmourParser(table_parser, capes_table, helmets_table, chest_table, legs_table)

        print(armour_parser.parse_capes())

    except TypeError as type_error:
        print(type_error)


if __name__ == "__main__":
    main()

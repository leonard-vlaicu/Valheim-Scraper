from core.parser import Parser, TableParser

class ArmourParser(Parser):
    """Parser class that parses the html content for armour"""
    def __init__(self, table_parser: TableParser, capes_table: list, helmets_table: list, chest_table: list, legs_table: list):
        self.table_parser = table_parser
        self.capes_table = capes_table
        self.helmets_table = helmets_table
        self.chest_table = chest_table
        self.legs_table = legs_table

    def get_capes_table(self):
        """returns the capes table"""
        return self.capes_table
    
    def get_helmets_table(self):
        """returns the helmets table"""
        return self.helmets_table
    
    def get_chest_table(self):
        """returns the chest table"""
        return self.chest_table
    
    def get_legs_table(self):
        """returns the legs table"""
        return self.legs_table
    
    def get_table_parser(self):
        """returns the table parser"""
        return self.table_parser
    


    def parse_armour_tables(self, armour_type: str):
        """parse the tables"""
        match armour_type:
            case "capes":
                self.parse_capes()
                

    def extract_data(self, row: list):
        for td in row:
            print(td)

    def extract_armour_piece(self):
        """extracts the armour piece"""
        pass

    def extract_armour_quality(self):
        """extracts the armour quality"""
        pass

    def extract_armour_weight(self):
        """extracts the armour weight"""
        pass

    def extract_materials_needed(self):
        """extracts the materials needed"""
        pass

    def extract_location_obtained(self):
        """extracts the location obtained"""
        pass
    
    def parse_capes(self):
        """parse the capes table"""
        capes_table = self.table_parser.get_table_by_index(0)
        capes_table_rows = capes_table.find_all('tr')

        capes_table_rows_with_td = [row for row in capes_table_rows if row.find('td') is not None and row.find('th') is None]


        for row in capes_table_rows_with_td:
            self.extract_data(row)
            break
        
        

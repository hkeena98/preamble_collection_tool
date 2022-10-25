"""
"""
class SourceIndentifier:
    """
    """
    def __init__(self, file_line):
        try:
            parsed = self.parse_grabid_file(file_line)
            self.id_varType = parsed[0] 
            if len(parsed) == 5:
                self.id_name = "UNDEFINED"
                self.id_useCase = parsed[1]
                self.id_lang = parsed[2]
                self.id_num = parsed[3]
                self.id_loc = parsed[4]               
            else:
                self.id_name = parsed[1]
                self.id_useCase = parsed[2]
                self.id_lang = parsed[3]
                self.id_num = parsed[4]
                self.id_loc = parsed[5]
        except:
            print("IDENTIFIER PARSE ERROR")
    
    """
    """   
    def parse_grabid_file(self, file_line):
        parsed_lines = file_line.split()
        print("Parsed Line:", parsed_lines)
        return parsed_lines
    
    """
    """
    def print_identifier(self):
        print("\nIDENTIFIER DETAILS\n")
        print("Identifier Variable Type:", self.id_varType)
        print("Identifier Name:", self.id_name)
        print("Identifier Use Case:", self.id_useCase)
        print("Identifier Language", self.id_lang)
        print("Identifier Number:", self.id_num)
        print("Identifier File Location", self.id_loc)
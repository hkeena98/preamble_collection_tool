"""
Author: Henry Keena
File: identifier.py
Description: Source file for SourceIdentifier object class.
"""

"""
Class: SourceIdentifier
Description: Object class that represents a variable, function, or class identifier in a given code base.
"""
class SourceIdentifier:
    """
    Function: __init__(self, file_line, project)
    Description: Initialization Function for SourceIdentifier instances.
    Arguments:
        - self : the instance of the class object.
        - file_line : the line of the report file that the identifier is located in.
        - project : the name of the parent project that the identifier is in. 
    """
    def __init__(self, file_line, project):
        try:
            parsed = file_line
            if isinstance(file_line, str):
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
            self.project = project
            self.spiral_analyzed = ""
        except:
            print("IDENTIFIER PARSE ERROR")
    
    """
    Function: parse_grabid_file(self, file_line)
    Description: Function that grabs and parses the file line the identifier is located in.
    Arguments:
        - self : the instance of the class object.
        - file_line : the line of the report file that the identifier is located in.
    """  
    def parse_grabid_file(self, file_line):
        parsed_lines = file_line.split()
        print("Parsed Line:", parsed_lines)
        return parsed_lines
    
    """
    Function: set_spiral(self, spiral_parts)
    Description: Function that sets the 'spiral_analyzed' property of the class instance. 
    Arguments:
        - self : the instance of the class object.
        - spiral_parts : the resulting list of strings created from analyzing the identifier name with the Spiral ronin library.
    """
    def set_spiral(self, spiral_parts):
        self.spiral_analyzed = spiral_parts

    """
    Function: print_identifier_details(self)
    Description: Funtion that prints the attribute details of the class instance.
    Arguments:
        - self : the instance of the class object.
    """
    def print_identifier_details(self):
        print("\nIDENTIFIER DETAILS\n")
        print("Identifier Variable Type:", self.id_varType)
        print("Identifier Name:", self.id_name)
        print("Identifier Use Case:", self.id_useCase)
        print("Identifier Language:", self.id_lang)
        print("Identifier Number:", self.id_num)
        print("Identifier File Location:", self.id_loc)
        print("Identifier Home Project:", self.project)
        print("Idnetifier Spiral Split:", self.spiral_analyzed)

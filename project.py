"""
Author: Henry Keena
File: project.py
Description: Source file for SourceProject object class.
"""

# Declares Imports
import csv
from identifier import SourceIdentifier

"""
"""
class SourceProject:
    """
    Function: __init__(self, project_name, filename)
    Description: Initialization Function for SourceProject instances.
    Arguments:
        - self : the instance of the class object.
        - project_name : name of the source project.
        - filename : name of the source file used to gain metadata about source project.
    """
    def __init__(self, project_name, filename):
        print("Building New Project -", project_name)        
        try:
            self.project_name = project_name
            self.identifiers = []
            self.attribute_bucket = []
            self.function_bucket = []
            self.declaration_bucket = []
            self.class_bucket = []
            self.parameter_bucket = []
            self.populate_buckets(filename, project_name)
        except:
            print("PROJECT OBJECT ERROR - CONSTRUCTOR ERROR")
            
    """
    Function: populate_buckets(self, filename, project_name)
    Description: 
    Arguments:
        - self : the instance of the class object.
        - filename : name of the source file used to gain metadata about source project.
        - project_name : name of the source project.
    """
    def populate_buckets(self, filename, project_name):
        print("Populating Project Buckets")
        try:
            csv_file = open(filename)
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                new_identifier = SourceIdentifier(row, project_name)
                self.identifiers.append(new_identifier)
            for ident in self.identifiers:
                if ident.id_useCase == "ATTRIBUTE":
                    self.attribute_bucket.append(ident)
                elif ident.id_useCase == "FUNCTION":
                    self.function_bucket.append(ident)
                elif ident.id_useCase == "DECLARATION":
                    self.declaration_bucket.append(ident)
                elif ident.id_useCase == "CLASS":
                    self.class_bucket.append(ident)
                elif ident.id_useCase == "PARAMETER":
                    self.parameter_bucket.append(ident)
        except:
            print("PROJECT OBJECT ERROR - POPULATE BUCKETS ERROR")
                         
    """
    Function: print_project_details(self)
    Description: Funtion that prints the attribute details of the class instance.
    Arguments:
        - self : the instance of the class object.
    """
    def print_project_details(self):
        print("\nPROJECT DETAILS\n")
        print("Project Name:", self.project_name)
        print("Total Identifiers:", len(self.identifiers))
        print("Number of Attribute Identifiers:", len(self.attribute_bucket))
        print("Number of Function Identifiers:", len(self.function_bucket))
        print("Number of Declaration Identifiers:", len(self.declaration_bucket))
        print("Number of Class Identifiers:", len(self.class_bucket))
        print("Number of Parameter Identifiers:", len(self.parameter_bucket))

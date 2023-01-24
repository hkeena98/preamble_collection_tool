"""
BASIC ANALYSIS REQUIREMENTS:
- Split data into raw buckets by Attribute, Function, Declaration, Class, and Parameter
- Remove single term identifiers

"""

# Declares Imports
import sys
import os
import subprocess
import time
import csv
from project import SourceProject
from spiral import ronin


# DECLARES PROJECT IDENTIFIER DICTIONARY
DATASET_PROJECTS = {}

"""
"""
def seperate_identifiers_all():
    root = "reports/"
    path = os.path.join(root, "")
    for file in os.listdir(root):
        dir = os.path.join(root, file)
        if os.path.isdir(dir):
            #print(d)
            project = dir.split("/")[1]
            #print(project)
            csv_file_name = "reports/"+project+"/"+project+"-identifiers.csv"
            new_project = SourceProject(project, csv_file_name)
            proj_dict = {    
                project : new_project
            }
            print(proj_dict)
            DATASET_PROJECTS.update(proj_dict)
    
    
"""
"""
def get_all_identifiers():
    working_identifiers = []
    for i in DATASET_PROJECTS:
        #working_identifiers.append(DATASET_PROJECTS[i].identifiers)
        for ident in DATASET_PROJECTS[i].identifiers:
            working_identifiers.append(ident)
    return working_identifiers

"""
"""
def remove_single_term_identifiers(identifiers):
    filtered_identifiers = []
    for identifier in identifiers:
        print("Filtering Single Term Identifiers:", identifier.id_name)
        if len(ronin.split(identifier.id_name)) > 1:
            filtered_identifiers.append(identifier)
            print("Filtered In")
        else: 
            print("Filtered Out")
    return filtered_identifiers 
    

"""
"""
def analyze_dataset():
    pass

"""
"""    
def main():
    print("Beginning Dataset Analysis...\n")
    seperate_identifiers_all()
    print(DATASET_PROJECTS)
    working_identifiers = get_all_identifiers()
    start_num = len(working_identifiers)
    working_identifiers = remove_single_term_identifiers(working_identifiers)
    filtered_num = len(working_identifiers)
    print("Original Number of Identifiers:", start_num)
    print("Removed Single Term Identifiers Total Num:", filtered_num)
    #print(working_identifiers)


# Calls Main
if __name__=='__main__':
    main()


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
def remove_single_letter_identifiers(identifiers):
    filtered_identifiers = []
    for identifier in identifiers:
        print("\nFiltering Single Term Identifier:", identifier.id_name)
        print("Identifier Length:", len(identifier.id_name))
        if len(identifier.id_name) > 1:
            filtered_identifiers.append(identifier)
            print("Filtered In")
        else: 
            print("Filtered Out")
        #print("\nRonin Split Identifier:", ronin.split(identifier.id_name))
        #print("\n")
        #if len(ronin.split(identifier.id_name)) > 1:
        #    filtered_identifiers.append(identifier)
        #    print("Filtered In")
        #else: 
        #    print("Filtered Out")
    return filtered_identifiers 
    

"""
"""
def ronin_filter(identifiers):
    filtered_identifiers = []
    for identifier in identifiers:
        split = ronin.split(identifier.id_name)
        identifier.set_spiral(split)
        print(identifier.spiral_analyzed)
        if len(identifier.spiral_analyzed) > 1:
            if '_' in identifier.spiral_analyzed[0]:
                filtered_identifiers.append(identifier)
            elif identifier.spiral_analyzed[0][0].isupper():
                filtered_identifiers.append(identifier)
            elif identifier.spiral_analyzed[0].islower() and identifier.spiral_analyzed[1][0].isupper():
                filtered_identifiers.append(identifier)
            #elif identifier.spiral_analyzed[0]
    return filtered_identifiers
    #for identifier in identifiers:
    #    identifier_names.append(identifier.id_name)
    #print("Identifier Names:", identifier_names)
    #for identifier in identifier_names:
    #    print(ronin.split(identifier))

"""
"""
def keyword_filter(identifiers):
    filtered_identifiers = []
    #keywords = ['get', 'fetch', 'default']
    keyword_set = set()
    for identifier in identifiers:
        keyword_set.add(identifier.spiral_analyzed[0])
    
    print("\n\nKeyword Set:", keyword_set)
    #for identifier in identifiers:
        


"""
"""    
def main():
    print("Beginning Dataset Analysis...\n")
    seperate_identifiers_all()
    print(DATASET_PROJECTS)
    
    working_identifiers = get_all_identifiers()

    start_num = len(working_identifiers)
    
    working_identifiers = remove_single_letter_identifiers(working_identifiers)

    working_identifiers = ronin_filter(working_identifiers)

    #working_identifiers = keyword_filter(working_identifiers)

    for identifier in working_identifiers:
        identifier.print_identifier_details()

    print("\nOriginal Number of Identifiers:", start_num)    
    filtered_num = len(working_identifiers)
    print("Total Number of Removed/Filtered Identifiers :", filtered_num)
    print("Remaining Identifiers:", (start_num-filtered_num))

    keyword_filter(working_identifiers)
    
    
    #print(working_identifiers)


# Calls Main
if __name__=='__main__':
    main()


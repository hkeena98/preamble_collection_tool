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
from operator import itemgetter
import enchant


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
        #print("\nFiltering Single Term Identifier:", identifier.id_name)
        #print("Identifier Length:", len(identifier.id_name))
        if len(identifier.id_name) > 1:
            filtered_identifiers.append(identifier)
            #print("Filtered In")
        #else: 
            #print("Filtered Out")
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
        #print(identifier.spiral_analyzed)
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
    dic = enchant.Dict("en_US")
    

    filtered_identifiers = []
    keywords = {}
    for identifier in identifiers:
        if identifier.spiral_analyzed[0] in keywords:
            keywords.update({identifier.spiral_analyzed[0] : keywords[identifier.spiral_analyzed[0]]+1})
        else:
            keywords[identifier.spiral_analyzed[0]] = 1

    # Initialize N
    N = len(identifiers)
    
    # printing original dictionary
    #print("The original dictionary is : " + str(keywords))
    
    # N largest values in dictionary
    # Using sorted() + itemgetter() + items()
    highest_frequency = dict(sorted(keywords.items(), key = itemgetter(1), reverse = True)[:N])
    #print("Number of Identifiers:", len(identifiers))
    print("\nTotal Number of Identifier First Terms:", len(keywords))
    print("\nHighest", N ,"Identifier First Term Frequencies:\n")
    for key, value in highest_frequency.items():
        #print(key, value)
        if (dic.check(key) is False) or (len(key) == 1):
            ident_ex = None
            for ident in identifiers:
                if ident.spiral_analyzed[0] == key:
                    ident_ex = ident
                    break
            #print("Not In Dictionary")
            with open('other_terms.csv', 'a', encoding='UTF8', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([key, value, ident_ex.id_name, ident_ex.id_loc])
            
            #with open('other_terms.txt', 'a') as file:
            #    file.write("TERM: "+str(key)+"\t,\tUSES: "+str(value)+"\t,\tEXAMPLE IDENTIFIER: "+ident_ex.id_name+"\t,\tEXAMPLE LOCATION: "+ident_ex.id_loc+"\n\n")
        else:
            ident_ex = None
            for ident in identifiers:
                if ident.spiral_analyzed[0] == key:
                    ident_ex = ident
                    break
            #print("In Dictionary")
            with open('dictionary_terms.csv', 'a', encoding='UTF8', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([key, value, ident_ex.id_name, ident_ex.id_loc])
                
            #with open('dictionary_terms.txt', 'a') as file:
            #    file.write("TERM: "+str(key)+"\t,\tUSES: "+str(value)+"\t,\tEXAMPLE IDENTIFIER: "+ident_ex.id_name+"\t,\tEXAMPLE LOCATION: "+ident_ex.id_loc+"\n\n")
    
    print("")

    #{key: value for key, value in sorted(keywords.items(), key=lambda item: item[1])}

    #for key, value in keywords.items():
    #    print(key, value)
    
    #print("Keyword/Frequency Dictionary:", keywords)
    
    #keywords = ['get', 'fetch', 'default']
    #keyword_set = set()
    #for identifier in identifiers:
    #    keyword_set.add(identifier.spiral_analyzed[0])
    
    #print("\n\nKeyword Set:", keyword_set)
    #for identifier in identifiers:
        
"""
"""
def heuristics_filter(identifiers):
    filtered_identifiers = []
    with open('first_terms.txt', 'r') as file:
        first_terms = file.read().splitlines()
        #print(first_terms)
        for term in first_terms:
            print("Checking for Term:", term)
            for identifier in identifiers:
                if identifier.spiral_analyzed[0] == term:
                    print("Filtered IN:", identifier.id_name)
                    filtered_identifiers.append(identifier)
    return filtered_identifiers








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

    #for identifier in working_identifiers:
    #    identifier.print_identifier_details()
        
    #keyword_filter(working_identifiers)
    
    working_identifiers = heuristics_filter(working_identifiers)
    
    print("\nOriginal Number of Identifiers:", start_num)    
    filtered_num = len(working_identifiers)
    print("Total Number of Removed/Filtered Identifiers :", (start_num-filtered_num))
    print("Remaining Identifiers:", filtered_num)
    
    #print(working_identifiers)


# Calls Main
if __name__=='__main__':
    main()


"""
Author: Henry Keena
File: analyzer.py
Description: Source file for all functions related to analyzing and processing source code identifiers.
"""

# Declares Imports
import os
import csv
from project import SourceProject
from spiral import ronin
from operator import itemgetter
import enchant

# DECLARES PROJECT IDENTIFIER DICTIONARY
DATASET_PROJECTS = {}

"""
Function: seperate_identifiers_all()
Description: Function that seperates all source code identifiers in all reports into appropriate, easy to reference, dictionary lists.
"""
def seperate_identifiers_all():
    root = "reports/"
    path = os.path.join(root, "")
    for file in os.listdir(root):
        dir = os.path.join(root, file)
        if os.path.isdir(dir):
            project = dir.split("/")[1]
            csv_file_name = "reports/"+project+"/"+project+"-identifiers.csv"
            new_project = SourceProject(project, csv_file_name)
            proj_dict = {    
                project : new_project
            }
            print(proj_dict)
            DATASET_PROJECTS.update(proj_dict)
 
"""
Function: get_all_identifiers()
Description: Function that collects all identifiers from collection dictionary.
"""
def get_all_identifiers():
    working_identifiers = []
    for i in DATASET_PROJECTS:
        for ident in DATASET_PROJECTS[i].identifiers:
            working_identifiers.append(ident)
    return working_identifiers

"""
Function: remove_single_letter_identifiers(identifiers)
Description: Function that removes identifiers that are a single character.
Arguments:
    - identifiers : the working list of identifiers to filter.
"""
def remove_single_letter_identifiers(identifiers):
    filtered_identifiers = []
    for identifier in identifiers:
        if len(identifier.id_name) > 1:
            filtered_identifiers.append(identifier)
    return filtered_identifiers 
    
"""
Function: ronin_filter(identifiers)
Description: Function that filters identifiers using the Ronin split functionality of the Spiral library.
Arguments:
    - identifiers : the working list of identifiers to filter.
"""
def ronin_filter(identifiers):
    filtered_identifiers = []
    for identifier in identifiers:
        split = ronin.split(identifier.id_name)
        identifier.set_spiral(split)
        if len(identifier.spiral_analyzed) > 1:
            if '_' in identifier.spiral_analyzed[0]:
                filtered_identifiers.append(identifier)
            elif identifier.spiral_analyzed[0][0].isupper():
                filtered_identifiers.append(identifier)
            elif identifier.spiral_analyzed[0].islower() and identifier.spiral_analyzed[1][0].isupper():
                filtered_identifiers.append(identifier)
    return filtered_identifiers

"""
Function: first_term_fetcher(identifiers)
Description: Function that analyzes working/filtered identifiers for their first terms, and returns a csv file with every first term, and their frequencies.
Arguments:
    - identifiers : the working list of identifiers to fetch first terms from.
"""
def first_term_fetcher(identifiers):
    dic = enchant.Dict("en_US")
    filtered_identifiers = []
    first_term = {}
    for identifier in identifiers:
        if identifier.spiral_analyzed[0] in first_term:
            first_term.update({identifier.spiral_analyzed[0] : first_term[identifier.spiral_analyzed[0]]+1})
        else:
            first_term[identifier.spiral_analyzed[0]] = 1
    N = len(identifiers)
    highest_frequency = dict(sorted(first_term.items(), key = itemgetter(1), reverse = True)[:N])
    print("\nTotal Number of Identifier First Terms:", len(first_term))
    print("\nHighest", N ,"Identifier First Term Frequencies:\n")
    for key, value in highest_frequency.items():
        if (dic.check(key) is False) or (len(key) == 1):
            ident_ex = None
            for ident in identifiers:
                if ident.spiral_analyzed[0] == key:
                    ident_ex = ident
                    break
            with open('analysis/other_first_terms.csv', 'a', encoding='UTF8', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([key, value, ident_ex.id_name, ident_ex.id_loc])
        else:
            ident_ex = None
            for ident in identifiers:
                if ident.spiral_analyzed[0] == key:
                    ident_ex = ident
                    break
            with open('analysis/dictionary_first_terms.csv', 'a', encoding='UTF8', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([key, value, ident_ex.id_name, ident_ex.id_loc])
    print("")
  
"""
Function: heuristics_filter(identifiers)
Description: Function that filters identifiers by preamble detection heuristics as defined in the 'heuristics_terms.txt' file.
Arguments:
    - identifiers : the working list of identifiers to filter.
"""
def heuristics_filter(identifiers):
    filtered_identifiers = []
    with open('heuristics_terms.txt', 'r') as file:
        first_terms = file.read().splitlines()
        for term in first_terms:
            for identifier in identifiers:
                if identifier.spiral_analyzed[0] == term:
                    filtered_identifiers.append(identifier)
    return filtered_identifiers

"""
Function: generate_identifier_preamble_list(identifiers)
Description: Function that generates final list of analyzed source code identifiers, and writes analysis information to an output csv file.
Arguments:
    - identifiers : finalized list of filtered source identifiers.
"""
def generate_identifier_preamble_list(identifiers):
    try:
        print("Generating List of Detected Identifiers with Preambles...\n")
        with open('analysis/preamble_identifiers.csv', 'a', encoding='UTF8', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(['IDENTIFIER', 'USE_CASE', 'LANGUAGE', 'PREAMBLE_FIRST_TERM', 'PREAMBLE_TYPE' 'PROJECT', 'FILE_LOCATION'])
            for identifier in identifiers:
                preamble_type = ""
                if identifier.spiral_analyzed[0]+'_' in identifier.id_name: 
                    preamble_type = "Underscore"
                elif identifier.spiral_analyzed[0].isupper():
                    preamble_type = "UpperCase"
                elif identifier.spiral_analyzed[0].islower(): 
                    preamble_type = "LowerCase" 
                    if identifier.spiral_analyzed[1][0].isupper():
                        preamble_type = "HungarianNotation"
                else:
                    preamble_type = "MixedCase"

                csv_writer.writerow([identifier.id_name, identifier.id_useCase, identifier.id_lang, identifier.spiral_analyzed[0], preamble_type, identifier.project, identifier.id_loc])
        print("\nCSV Preamble Identifier File Written...\n")
    except:
        print("CSV PREAMBLE LIST GENERATION EXCEPTION")

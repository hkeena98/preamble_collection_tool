"""
Author: Henry Keena
File: preamble_tool.py
Description: Primary file for running the tool.
"""

#Declares Imports
import sys
import traceback
import collector as Collector
import analyzer as Analyzer

"""
Function: help()
Description: Print function to display help options for tool operations.
"""
def help():
    print("\nUSAGE:\tpython3 preamble_tool.py [OPTION]")
    print("\nOPTIONS:\n")
    print("Display Help/Options\t\t--help\t-h")
    print("Collect Project Data\t\t--collect-project-data\t-cpd")
    print("Collect First Term Data\t\t--collect-first-terms\t-cft")
    print("Analyze Project Data\t\t--analyze-project-data\t-apd")
    print("")

"""
Function: main()
Description: Main function for handling operation/calls of the tool.
"""
def main():
    try:
        args = sys.argv[1:]
        # Checks for valid number of arguments
        if len(args) != 1:
            print("\nINCORRECT NUMBER OF ARGUMENTS\n")
            help()
            exit()
        # Display Help/Options
        if args[0] == '--help' or args[0] == '-h':
            help()
        # Collect Project Data collector.py
        elif args[0] == '--collect-project-data' or args[0] == '-cpd':
            print("Beginning Preamble Collection...\n")
            Collector.project_identifier_collector()
        # Collect First Term Data analyzer.py
        elif args[0] == '--collect-first-terms' or args[0] == '-cft':
            print("Collecting Project Identifier First Terms...\n")
            Analyzer.seperate_identifiers_all()
            working_identifiers = Analyzer.get_all_identifiers()
            working_identifiers = Analyzer.remove_single_letter_identifiers(working_identifiers)
            working_identifiers = Analyzer.ronin_filter(working_identifiers)
            Analyzer.first_term_fetcher(working_identifiers)
        # Analyze Project Data analyzer.py
        elif args[0] == '--analyze-project-data' or args[0] == '-apd':
            print("Beginning Dataset Analysis...\n")
            Analyzer.seperate_identifiers_all()
            working_identifiers = Analyzer.get_all_identifiers()
            start_num = len(working_identifiers)
            working_identifiers = Analyzer.remove_single_letter_identifiers(working_identifiers)
            working_identifiers = Analyzer.ronin_filter(working_identifiers)
            working_identifiers = Analyzer.heuristics_filter(working_identifiers)
            print("\nOriginal Number of Identifiers:", start_num)    
            filtered_num = len(working_identifiers)
            print("Total Number of Removed/Filtered Identifiers :", (start_num-filtered_num))
            print("Remaining Identifiers:", filtered_num)                
            Analyzer.generate_identifier_preamble_list(working_identifiers)
        # Display Help if invalid argument
        else:
            print("\nINCORRECT ARGUMENT\n")
            help()
            exit()
    except Exception:
        print("RUNTIME EXCEPTION:", traceback.format_exc()) 

# Calls Main
if __name__=='__main__':
    main()
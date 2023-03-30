"""
"""

# Declares Imports
import sys
import os
import subprocess
import time
import csv

from identifier import SourceIdentifier


"""
"""
def project_identifier_collector():
    print("Collection...")
    root = "projects/"
    path = os.path.join(root, "")
    for path, subdirs, files in os.walk(root):
        for name in files:
            file_path = os.path.join(path, name)
            project = file_path.split("/")[1]
            if name.lower().endswith(('.c', '.cpp', '.cc', '.java', '.cs', '.h')):
                print("\nProject Name:", project, "\n")
                print("File Name:", name, "\n")
                print("File Path:", file_path, "\n")
                if os.path.exists("reports/"+project) == False:
                    subprocess.run(["mkdir", "reports/"+project])
                    subprocess.run(["mkdir", "reports/"+project+"/srcml/"])
                    subprocess.run(["mkdir", "reports/"+project+"/grabidentifiers/"])
                if os.path.exists("reports/"+project):
                    print("Generating srcML .xml File...\n")
                    subprocess.run(["srcml", file_path, "-o", "reports/"+project+"/srcml/"+name+".xml"])
                    print("Grabbing Identifiers from srcML .xml File...\n")
                    gi_log_file = open("reports/"+project+"/grabidentifiers/"+name+".xml.log.txt", "w")
                    subprocess.run(["grabidentifiers", "-s", "10000", "reports/"+project+"/srcml/"+name+".xml"], stdout=gi_log_file)
                    gi_log_file.close()
                    gi_log_file = open("reports/"+project+"/grabidentifiers/"+name+".xml.log.txt", "r")
                    for i in gi_log_file.readlines()[:-1]:
                        identifier = SourceIdentifier(i, project)
                        identifier.print_identifier_details()
                        append_project_csv(project, identifier)
                    gi_log_file.close()
                time.sleep(.05)

"""
"""
def append_project_csv(project, identifier):
    try: 
        csv_file_name = "reports/"+project+"/"+project+"-identifiers.csv"
        if os.path.exists(csv_file_name) == False:
            header = ['VARIABLE_TYPE', 'IDENTIFIER_NAME', 'IDENTIFIER_USE_CASE', 'LANGUAGE', 'NUM', 'FILE_LOCATION', 'PROJECT']
            with open(csv_file_name, 'w', encoding='UTF8', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(header)
        else:
            id_tuple = (identifier.id_varType, identifier.id_name, identifier.id_useCase, identifier.id_lang, identifier.id_num, identifier.id_loc, identifier.project)
            with open(csv_file_name, 'a', encoding='UTF8', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(id_tuple)
    except:
        print("CSV FILE ERROR")

"""
"""
def generate_dataset():
    pass
          
"""
"""    
def main():
    print("Beginning Preamble Collection...\n")
    project_identifier_collector()


# Calls Main
if __name__=='__main__':
    main()
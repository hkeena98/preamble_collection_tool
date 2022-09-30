import sys
import os
import subprocess
import time

def collector():
    print("Collection...")
    root = "projects/"
    path = os.path.join(root, "")
    for path, subdirs, files in os.walk(root):
        for name in files:
            if ".java" in name:
                file_path = os.path.join(path, name)
                project = file_path.split("/")[1]
                print("\nProject Name:", project, "\n")
                print("File Name:", name, "\n")
                print("File Path:", file_path, "\n")
                if os.path.exists("reports/"+project):
                    print("Generating srcML .xml File...\n")
                    subprocess.run(["srcml", file_path, "-o", "reports/"+project+"/"+name+".xml"])
                    print("Grabbing Identifiers from srcML .xml File...\n")
                    subprocess.run(["grabidentifiers", "-s", "10000", "reports/"+project+"/"+name+".xml", ">", "reports/"+project+"/"+name+".xml.log.txt"])
                else:
                    subprocess.run(["mkdir", "reports/"+project])
                    print("Generating srcML .xml File...\n")
                    subprocess.run(["srcml", file_path, "-o", "reports/"+project+"/"+name+".xml"])
                    print("Grabbing Identifiers from srcML .xml File...\n")
                    subprocess.run(["grabidentifiers", "-s", "10000", "reports/"+project+"/"+name+".xml", ">", "reports/"+project+"/"+name+".xml.log.txt"])
                    #, ">", "reports/"+project+"/"+name+".xml.log.txt"
                time.sleep(.5)
                
    



def main():
    print("Beginning Preamble Collection...\n")
    collector()
    

if __name__=='__main__':
    main()
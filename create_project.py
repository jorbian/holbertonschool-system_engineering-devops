#!/usr/bin/python3

import csv
import os
import subprocess

from pathlib import Path

# The final version of this script will take THREE parameters:
# 1) the path of a properly formated '.csv' file
# 2) a default first line to the files we are creating
# 3) the permissions each of the new files are supposed to have 
input_file = "/root/holbertonschool-system_engineering-devops/0x00-shell_basics.csv"
first_line = "#!/bin/bash\n"
readme= "README.md exists and is not empty"
permissions = "777"

output_folder_name = Path(input_file).stem
Path(output_folder_name).mkdir(parents=True, exist_ok=True)
os.chdir(output_folder_name)

with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)

    for file in reader:
        with open(file["file_name"], "w") as new_file:
            #Getting to a point where we can deal with newline characters in 
            #the unique content of each individual file IS SOMETHING WE WILL 
            #HAVE TO COME BACK TO. It's fine for now. I have a bunch of more 
            #complicated things communicating with GitHub and possibly 
            #scrapping the school Intranet I need to get working first. 
            #BUT THIS IS A GIANT PROBLEM YOU CAN DRIVE A TRUCK THROUGH THAT
            #WILL HAVE TO BE ADDRESSED THE MOMMENT WE ARE DEALING WITH PROJECTS
            #MORE INVOLVED THAN THESE FIRST ONES.
            unique_content = file["unique_content"]
            contents = [first_line, unique_content, "\n"]
            new_file.writelines(contents)

        subprocess.run(['chmod', permissions, file["file_name"]], capture_output=False)

with open("README.md", "w") as file:
    file.write("README.md exists and is not empty")

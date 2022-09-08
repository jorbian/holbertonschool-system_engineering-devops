#!/usr/bin/python
#coding:utf-8
#

import os
import glob 

host_directory = os.getcwd()

project_folder = (glob.glob("%s/*/" % (host_directory)))

project_data = [
    {
        "project_path": x, 
        "project_name": x.rsplit("/")[-2],
        "file_names": os.listdir(x)
    }
    for x in project_folder
]

for project in project_data:

    csv_name = ("%s.%s" % (project["project_name"], "txt"))
    files = [("%s%s" % (project["project_path"], x)) for x in project["file_names"]]

    with open(csv_name, "w") as out_file:
        out_file.writelines(files)
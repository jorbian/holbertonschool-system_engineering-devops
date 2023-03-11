#!/usr/bin/python3

import sys
import subprocess

command_string = sys.argv[1:]

if command_string < 4:
    print("Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY")
else:
    subprocess.run(command_string)

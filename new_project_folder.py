# REMEMBER THIS SITE:
# https://regexkit.com/python-regex
# It's even more useful than you thought for trying to find regexes like this
# one we needed today to validate the folder name.

import re 

default_README = "This file exists and is not empty."
name_validator = re.compile("(\b(([\d])x(\d{2})-(.*))\b)")

example_names = [
    "0x03-shell_variables_expansions",
    "0x01-emacs",
    "0x02-vi"
] 


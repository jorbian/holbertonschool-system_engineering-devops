# REMEMBER THIS SITE:
# https://regexkit.com/python-regex
# It's even more useful than you thought for trying to find regexes like this
# one we needed today to validate the folder name.

import re 

default_README = "This file exists and is not empty."
name_validator = re.compile("(\b(([\d])x(\d{2})-(.*))\b)")

example_name = [
    "0x03-shell_variables_expansions",
    "0x01-emacs",
    "0x02-vi",
    "asdfdfsaf adf",
    "",
    "12233s"
] 

test = [re.search(name_validator, x) for x in example_name]

if (name_validator.match(example_name[0])):
    print("puppies")

#test = [name_validator.match(x) for x in example_name]

import re

p = re.compile(ur'(\b[\d])x(\d{2})-(.*)')
test_str = u"0x03-shell_variables_expansions\n0x01-emacs\n0x02-vi"
    
matches = re.findall(p, test_str)

print(matches[0][0])
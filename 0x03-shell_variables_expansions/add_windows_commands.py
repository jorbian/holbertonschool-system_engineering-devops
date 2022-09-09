# Figuring all this stuff out about the alias command was the first thing I
# learned at the Holberton School that raelly blew my mind and opened up an
# entirely new universe to me. This is definitely something I need to come 
# back too! Finding out the exact mechanics of how this works and seeing if 
# adding my favourite aliases is something that will have to get parked in a 
# login script that has to be run EVERY single time. But maybe that's not a 
# big a deal!! Figuring out how to work login scripts is a useful sys admin 
# task to know anyway. 
#
# BUT I need to make sure I have the actual homework down first, so this is 
# something I will definitely have to come back too --

import sys 
import subprocess 

arguments = ['dir="ls"','copy="cp"','rename="mv"','md="mkdir"','rd="rmdir"','del="rm -i"']
commands = [("alias %s" % (x))  for x in arguments]

for command in commands:
    job = subprocess.Popen(commands, shell=True, stderr=subprocess.PIPE)

    while True:
        output = job.stderr.read(1)
        if job == '' and job.poll() != None:
            break
        if output != '':
            sys.stdout.write(output)
            sys.stdout.flush()

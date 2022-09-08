#!/bin/bash

string="hello"
filename="10-mirror_permissions"
(head -n 1 $0) > $filename
echo "cp $string $(./reverse_string.sh $string)" >> $filename
chmod 777 $filename 

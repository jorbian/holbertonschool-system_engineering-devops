#!/bin/bash

if [ "$#" -eq 0 ]
then 
	(>&2 echo "NO STRING WAS PROVIDED"; exit 1)
else 
	echo $(echo "$1" | rev)
fi 

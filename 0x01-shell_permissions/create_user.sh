#!/bin/bash

temp_username="NEW_USER_$RANDOM"
default_password="password1."

username=$temp_username 
password=$default_password 

useradd -m $username
printf "$password\n$password" | passwd $username

echo "USER: $username was successfully created"

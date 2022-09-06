#!/bin/bash

thisfile=$0
newfile="${thisfile%%.*}_$RANDOM.sh"
head $0 > $newfile


#!/usr/bin/env python3

import sys

#for loop to iterate through each line in the file from standard input
for line in sys.stdin:
  #strip and split each line in the file
  words=line.strip().split()
  #using list comprehension, capitalize 1st letter each word in words above
  print(" ".join([word.capitalize() for word in words]))

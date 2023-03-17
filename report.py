#!/usr/bin/env python3

#Import modules
import re
import sys
import operator

#Define logfile
log_file = sys.argv[1]

#1.Errors Ranking
#Search through logfile for amount of each errors
#def errors_rank(log_file):
with open(log_file, "r") as file:
  pattern = r"\w* ERROR ([\w ]*).*"
  re.findall(pattern, file)
#print(errors)

#Sort results from most common to least common


#2.User usage stats
#Search through logfile for users


#Search through logfile for how many info and errors corresponds to which users


#Sort results alphabetically


#3.Generate report as CSV file


#4.Convert CSV file to HTML file

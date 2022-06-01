# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re

f = open("Sarah/sarah001.txt")
text = f.read()

text = re.sub("[:\.,+\&%()><\/\\@\?\[\]]", "", text)


text_lines = text.split("\n")


utterances = []
for line in text_lines:
   if line.startswith("*MOT"):
       utterances.append(line[4:])

       

   #get out words and count them    
ut_length = []
for i in utterances: 
    words = i.split()
 
    #count how many words we got? = length
    
    ut_length.append(len(words))

mlu = sum (ut_length)/float(len(ut_length))

print mlu
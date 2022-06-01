# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 13:33:06 2016

@author: Dana
"""

import re
import glob

#define speaker
speakers=["MOT","CHI"]

#define file
files = glob.glob("Sarah/*.txt")

#define what "outfile" you creat will be called/headers
out_file = "MLU_data.csv"
header="filename, speaker, mlu\n"

#writing into the file
f=open(out_file, "w")
f.write(header)
f.close()

#function to get mlu
def get_mlu(sarahfile, speaker):#arguments
   f = open(sarahfile)#open file
   text = f.read()#read file
   text = re.sub("[:\.,+\&%()><\/\\@?\*]","",text)#clean up text
   text = re.sub("\[.*[\],\S*]", "", text)
   text_lines = text.split("\n")
   utterances = []#define utterances as a list
   for line in text_lines:#loop through lines
        if line.startswith(speaker):#if the line starts with MOT eller CHI
            utterances.append(line[4:])#append the utterance 
   ut_length = [] #define utterance length
   for i in utterances:
        words = i.split()
        ut_length.append(len(words))#append length of utterances
        
   return sum(ut_length)/float(len(ut_length))#return the sum of the utterance length idk what float is

for sarahfile in files:
    for speaker in speakers:
        mlu=get_mlu(sarahfile, speaker)
        row="{},{},{}\n".format(sarahfile,speaker,mlu)
        f=open(out_file, "a")
        f.write(row)
        f.close()
        
        
        
        
        
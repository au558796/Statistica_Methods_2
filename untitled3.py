# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 17:05:14 2016

@author: Dana
"""
import re
import os

SAVE_FOLDER = "log"
if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

filename = "log_data.csv"


    
def cleantext(filename):
     f = open(filename)
     text = f.read()
     text = re.sub("[:\+\&%()><\/\\@\?\[\]]", "", text)
     return text
        
def comma(filename):
    text = cleantext(filename)
    text = text.replace(" ", ",")
    return text  

log_data=cleantext("logdata.txt")
log_data=comma("logdata.txt")
    
    
print log_data
    
with open(filename, "w") as f:
    f.write(log_data)
    
f.close
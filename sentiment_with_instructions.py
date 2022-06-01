# -*- coding: utf-8 -*-
"""
Student script for sentiment analysis

Created on Thu Nov 03 16:37:44 2016

@author: Marlene/Kristian
"""

import pandas as pd
import re

"""The first part of the code, we will give you. We actually also just stole it
from http://neuro.imm.dtu.dk/wiki/LabMT ;) """

#This part retrieves the sentiment scores from the url below
url = 'http://www.plosone.org/article/fetchSingleRepresentation.action?uri=info:doi/10.1371/journal.pone.0026752.s001'
labmt = pd.read_csv(url, skiprows=2, sep='\t', index_col=0)

#This will calculate an average (mean) that is subtracted from each score, so the score become "normalized"/centred around 0
average = labmt.happiness_average.mean()
happiness = (labmt.happiness_average - average).to_dict()

#A function that will give an average score for any string (text, sentence or word)
def score(text):
    words = text.split()
    return sum([happiness.get(word.lower(), 0.0) for word in words]) / len(words)


"""Here, you come in. Let's use the above knowledge/function to analyse some recent
text material!!!"""

#First, open the textfile "presidential_debate.txt" and read in all the lines as string
#(which you retrieved from bb and stored in the same folder as this script)
#see MLU script for help
#debate= glob.glob("C:\Users\Dana\Desktop\SEMESTER 1\COGNITION AND COMMUNICATION\Everything Python\debate.txt")

f = open("debate.txt")
    
text = f.read()



#Let's also open a (.csv) file to write the results to, and maybe add some headers
#(I do not know how Malte did this with you, but again, look in the MLU script for help)

out_file= "debate_sentiment.csv"
header= "filename, speaker, sentence, score\n"

f_out=open(out_file, "a")
f_out.write(header)
 
#Clean up the text; here's a little handy code we found online for you (just un-outcomment the next line)

text = re.sub("[:\.,+\&%()><\/\\@\?\[\]]", "", text)


text_lines=text.split("\n")


#Extract individual lines (each line contains: SPEAKER + "\t" + sentence)
turn=0

for line in text_lines:
    split_line=line.split("\t")
    speaker = split_line[0]
    sentence= split_line[1]
    score1=score(sentence)
    turn+=1
    row="{},{},{},{}\n".format(turn,speaker,sentence, score1)
    f_out.write(row)

    print turn
    
f_out.close()
        
        

#for turn, line in enumerate (text_lines):
#Loop through the lines; for each line
#keep a variable that tells you which line you are on (counting 1,2,3,... through the lines)
#separate the line into speaker = "..." and sentence = "..."
#get the sentiment score for the sentence
#write the data to the output file (sentence_nr; speaker; sentence; sentiment_score)
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 19:09:02 2016

Classification of intentionality in videos

Uses words produced in one condition to predict the condition that other sentences were produced in

@author: Marlene
"""
#import modules
import re


"""Based on training data, make a score() function that can be used to classify
words/lines of text as intentional/unintentional"""

"""First of all, we need to read in the training data. In this script, we will read in and clean a total of 
4 textfiles. So don't copy and paste the stuff from the MLU script over and over again.
Any alternatives that come to mind? YES! Let's write a function! This will also be handy to reuse
fur your other scripts."""


#(Step 1:) function that reads in and cleans text (we will need this a lot)

#define a new function which takes a filename as an input and returns a textstring as an output
# open the file

#f = open("trainset_intentional.txt")
# read the text 
#text = f.read()
# use re to remove special characters and numbers
#text = re.sub("[:\.,+\&%()><\/\\@\?\[\]]", "", text)
# use text.lower() to convert all the words to lowercase. 
#text = text.lower()
 


def cleantext(filename):
    f = open(filename)
    text = f.read()
    text = re.sub("[:\.,+\&%()><\/\\@\?\[\]]", "", text)
    text = text.lower()
    return text
    


#(This way, we will find more words that are the same, even if one happens to be capitalized in the text.)
#now test the function: use it to read in and clean the texts from the intentional and the random videos 
#(filenames: "trainset_intentional.txt" and "trainset_random.txt")
# print the texts to see if it works

"""let me know when you are done with step 1!"""


#(Setp 2:) figure out the words that are unique in each corpus 
#That means that in the end of this step, we need to have a list of intentional_words and a list of unintentional_words
#The intentional_words are words that appear in the intentional.txt file, but not the random.txt file, and vice versa with the unintentional_words


#Start by making a list of all the words in each corpus/condition
#(here we do not care about individual lines, so we can directly use the .slpit() method to get a list of all the words)
intentional_words=cleantext("trainset_intentional.txt")#make list from words in file
intentional_words=text.split()#split by individual words in file

print intentional_words

unintentional_words=cleantext("trainset_random.txt")
unintentional_words=text.split()

print unintentional_words
#Next, also make a set list of all (unique) words, so we can iterate over them in a loop
#so first, add the two lists from the two textfiles
unique_words= intentional_words + unintentional_words#combine two lists to one list

#then, use set() to create a unique list (in which each word only appears once)
unique_words=set(unique_words)


only_intentional=[]
only_unintentional=[]

for word in unique_words:
    if word in intentional_words:
        if word not in unintentional_words:
            only_intentional.append(word)
            
    elif word in unintentional_words:
        if word not in intentional_words:
            only_unintentional.append(word)
        
     

#Last but not least, we want to go through that list (what method comes to mind?) and check for each word...
#...if it appears in the list of words from the random condition, but not in the lust from the intentional condition
#...or vice versa
#and append that word to the list it belongs to

#maybe try printing the two lists to see if it works, and check what comes out

"""let me know when you are done with step 2!"""


#(Step 3:) Make a score() function that gives any string of words an intentionality score
# the score should be 1) positive for intentional descriptions 2) negative for unintentional descriptions 3) zero if it's undecided
#define the function (what does it take as input?)
# split the string it gets into a list of individual words
# go through that list of words and
# check for each word if it is intentional (in the intentional_words list) or unintentional (or nothing, but you don't need to check for that)
# keep a "intentionality_score" variable to which you add 1 for every intentional word and subtract 1 for every unintentional word
# think about where you need to define that intentionality_score variable!
# remember to return something  

"""let me know when you are done with step 3!"""


"""Now we use the score() function on our test data and see how it works out!"""
#(Step 4:) use read_text() to read in both test data sets ("testset_intentional.txt" and "testset_random.txt")
#here, we are interested in lines - so proceed like with the sentiment analysis
# iterate over each line in the text
# feed that line to the score function
# print out a score for each description
# do this for each testset
# what comes out? does our classification system work? 

"""let me know when you are done with step 4!"""


#(Bonus:) instead of printing out each indvidual score and then manually looking through the score,
#we want to make a summary of how many sentences we classified correctly/incorrectly and how many our classification could not classify
#for this, when going through the lines and getting a score for each line, instead of printing, store that score in a variable
# for descriptions in the intentional_testset, check if the score is > 0 - count them as correct classifications/successes
# if it is == 0 - count them as unclassified
# else, count them as fails/wrongly classified
# same in the random_testset, except now scores < 0 will be correctly classified/successes
#print out the results in this format:
#success: xx    fail: xx    unclassified: xx
#what numbers do you get?


#(Bonus 2:) for incorrectly classified descriptions, add another line to print them out and have a look
# is there something odd about them? might they be different from the rest (e.g., actually contain less intentional
#descriptions, even if they are in the intentional condition?)
# or is this rather a problem with our automated classification? i.e., would you as humans classify them differently?
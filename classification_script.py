# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 19:09:02 2016

Classification of intentionality in videos

Uses words produced in one condition to predict the condition that other sentences were produced in

@author: Marlene
"""
#import modules
import re


"""Part 1: Based on training data, make a score() function that can be used to classify
words/lines of text as intentional/unintentional"""

#function that reads in and cleans text (we will need this a lot)
def read_text(filename):
    f = open(filename)
    text = f.read()
    text = re.sub(ur'[^\w\d\s]+', '', text)
    text = text.lower()
    return text

#read in and clean the intentional and the random words
int_text = read_text("trainset_intentional.txt")
rand_text = read_text("trainset_random.txt")

#make a list of all the words in each corpus (here we do not care about individual lines)
int_wordlist = int_text.split()
rand_wordlist = rand_text.split()

#a set list of all (unique) words
all_words = set(int_wordlist+rand_wordlist)

#figure out the words that are unique in each corpus
intentional_words = []
unintentional_words = []
for word in all_words:
    if word in int_wordlist and not word in rand_wordlist:
        intentional_words.append(word)
    elif word not in int_wordlist and word in rand_wordlist:
        unintentional_words.append(word)
#print intentional_words
#print unintentional_words

#make a function that gives any string of words an intentionality score
def score(string):
    words = string.split()
    int_score = 0
    for word in words:
        if word in intentional_words:
            int_score +=1
        elif word in unintentional_words:
            int_score -=1
    return int_score


"""Part 2: give a score to each sentence in the test data and see how it works out"""

int_test = read_text("testset_intentional.txt")

print "Intentional movement video descriptions:"
success = 0
fail = 0
unclassified = 0

for line in int_test.split('\n'):
    
    x = score(line)
    print x
    if x > 0:
        success += 1
    elif x == 0:
        unclassified +=1
    else:
        fail += 1
        print line   
print "success: " , success, "\nfail:" , fail, "\nunclassified:", unclassified
    

rand_test = read_text("testset_random.txt")

print "Random movement video descriptions:"
success = 0
fail = 0
unclassified = 0

for line in rand_test.split('\n'):
    x = score(line)
    print x
    if x < 0:
        success += 1
    elif x == 0:
        unclassified +=1
    else:
        fail += 1
        print line
        
print "success: " , success, "\nfail:" , fail, "\nunclassified:", unclassified
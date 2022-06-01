# -*- coding: utf-8 -*-
"""
Created on Wed Oct 05 09:38:55 2016

@author: Dana
"""


from psychopy import core

text = """once upon a time there was a moose

the next line is here.
"""



text_lines = text.split()
stopwatch = core.Clock()


for word in text_lines:
    stopwatch.reset()
    print word
    raw_input() 
    print stopwatch.getTime()
    
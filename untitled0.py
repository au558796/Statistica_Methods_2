
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 15:50:20 2016

@author: Dana
"""

from psychopy import visual, event, core 

#make instruction texts 

win=visual.Window()

#define function to make visual text
def show_info(text):
    msg =visual.TextStim(win,text=text)
    msg.draw()
    win.flip()
    event.waitKeys()
    fullscr = True
    #try:
        #raw_input("Press enter to continue")
    #except SyntaxError:
       # pass
    #else: 
    core.quit()
    
    
    
show_info("""These are two colour categories, Sinji and Gouloboy. 
You will now be asked to do a training task to distinguish between these two colour categories.
A series of colours will appear and you will be asked to make the distinction which category they belong.
Press the Left arrow key for Sinji, and Right arrow key for Gouloboy.
Press Enter when you are ready to start.""")


    
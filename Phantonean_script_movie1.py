# -*- coding: utf-8 -*-
"""
LEARNING PHANTONEAN SCRIPT

This is a script for an experiment in which participants implicitly learn a 
mini "Alien" Language.

The pyttsx module (for reading out the sentences in speech) may throw an error
if not running this as an administrator in windows (win32com folder needs to be
writeable).

Created on Sun Sep 18 12:38:46 2016

@author: Marlene Staib
"""

#import
from psychopy import visual, core, sound, event, gui, monitors
import pandas as pd
import numpy as np
from sentence_list_maker import *
import random, re, os

#Variables
# Monitor parameters
MON_DISTANCE = 60  # Distance between subject's eyes and monitor
MON_WIDTH = 50  # Width of monitor in cm
MON_SIZE = [1280, 720]  # Pixel-dimensions of monitor
MON_RATIO = MON_SIZE[0]/MON_SIZE[1]

#Folder for writing the trials/create folder if it does not exist
SAVE_FOLDER = 'Phantonean_Data'
if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

# create empty panda matrix 
columns = ['subject_ID', 'age', 'gender', 'L1', 'nr_of_L2', 'condition', 'phase', 'trial_nr', 'block_nr', 'mode', 'target', 'answer', 'accuracy', 'rt', 'error', 'flanker_diff']
index = np.arange(0) # array of numbers for the number of samples
DATA = pd.DataFrame(columns=columns, index = index)


# Intro-dialogue, save input variables 
V = {'subject_ID':'', 'age': '', 'gender':['m', 'f', 'o'], 'L1': '', 'nr_of_L2': ''}
if not gui.DlgFromDict(V, order=['subject_ID', 'age', 'gender']).OK:
    core.quit()

#Pick the condition from subject_ID
V['condition'] = "base" if int(V['subject_ID'])%2 == 0 else "anx" #put all even subjects in baseline, odd ones in anxiety condition


#window and stuff
my_monitor = monitors.Monitor('testMonitor', width=MON_WIDTH)
my_monitor.setSizePix((MON_SIZE)) #change this, dpending on monitor
win = visual.Window(monitor='testMonitor', size=MON_SIZE, units='norm', fullscr=True, allowGUI=False, color='black')
mouse = event.Mouse(visible=True, win=win)
win.mouseVisible = False
clock = core.Clock()  
V['trial_nr'] = 0    #will get incremented on every trial


#Stimuli
#instructions
text = visual.TextStim(win, units='norm', height = .07, pos= [0,0.1], wrapWidth=999)
#for presentation trials
text_below = visual.TextStim(win, units='norm', height = .08, pos= [0,-0.5], wrapWidth=999)
text_above = visual.TextStim(win, units='norm', height = .07, pos= [0,0.9], wrapWidth=999)
text_above2 = visual.TextStim(win, units='norm', height = .09, pos= [0,0.7], wrapWidth=999, color=(-1,0.5,1))
#for multiple choice trials
MOV_POSITIONS = [[-0.4,0.2], [0.4, 0.2], [-0.4, -0.6], [0.4,-0.6]]
TXT_POSITIONS = [[-0.4,-0.4],[0.4,-0.4], [-0.4,-0.75], [0.4,-0.75]]
#sounds & vids & shapes for feedback
fail_sound = sound.Sound('sounds/feedback/fail.wav')
#fail_sound = sound.SoundPyo(value='E', secs=.5)
fail_face = visual.ImageStim(win, image="images/neg_face.png", units = 'norm')
#rectangles (all conditions)
fail_rect_mov = visual.Rect(win, units = 'norm', width = .55, height = .7, fillColor="red", lineColor="red")
correct_rect_mov = visual.Rect(win, units = 'norm', width = .55, height = .7, fillColor="green", lineColor="green")
fail_rect_txt = visual.Rect(win, units = 'norm', width = .6, height = .12, lineWidth = 2, lineColor="red")
correct_rect_txt = visual.Rect(win, units = 'norm', width = .6, height = .12, lineWidth = 2, lineColor="green")


#Lists for trials etc.
word_dict = make_phantonean()
trials_dict = make_sentence_dict(folders, word_dict)
blocks = block_set()


#texts
welcome = unicode("""
Welcome to the experiment! And thank you for being here. In this experiment, you
will learn an alien language called "Phantonean".

Hit "Enter" when you are ready to get started.
""", "utf-8")

instructions1 = unicode("""
Over the next ~20 minutes, you will be presented with 8 little learning blocks. 
In the beginning of each learning block, you will either hear or read some new 
(and some familiar) sentences in Phantonean. You will also be shown a video clip
which demonstrates the meaning of that sentence. You will have limited time to
study each sentence.

Hit "Enter" when you are ready to move on.
""", "utf-8")

instructions2 = unicode("""
After every learning block, you will be able to practice your Phantonean with
some practice questions. You will be asked to choose the sentence that best 
describes a video in Phantonean, or vice versa.
Once you get through all of the learning blocks, there will be a little test.
The test questions will be similar to the practice questions.
""", "utf-8")

anx_instructions = unicode("""
If your answer to one of the questions is correct, it will turn green.
If it is incorrect, you will hear a sound and see a negative emoji, that will 
indicate to you that you were wrong, like this:

(Hit "Enter".)
""", "utf-8")

ready = unicode("""Ready to start learning? Hit "Enter".""", "utf-8")

pick_vid = unicode("""
Use the mouse to pick out the video that correctly matches the sentence.
""", "utf-8")

pick_txt = unicode("""
Use the mouse to pick out the sentence that correctly matches the video.
""", "utf-8")

intermediate = unicode("""
Hit "Enter" to continue.
""", "utf-8")

correct = unicode("""
That's correct!
""", "utf-8")

incorrect = unicode("""
That's incorrect.
""", "utf-8")

practice_trial = unicode("""
Quite a few new sentences you have heard! Let's see if you can remember them...
Hit "Enter" to start practicing.
""", "utf-8")

practice_end = unicode("""
Now, let's learn some more sentences...
Hit "Enter" to hear more Phantonean!
""", "utf-8")

test_start = unicode("""
This is the end of the learning part. Now, it's time to test what you have learned!
On the upcoming test trials, you will (like before) be asked to choose the correct
video/sentence. This time, while still trying to be as accurate as possible, try
also to be as fast as possible!

Hit "Enter" when you are ready to test your skills.
""", "utf-8")

test_block_end = unicode(""" (out of 4). Feel free to take a short break.
Hit "Enter" when you are ready to continue.
""", "utf-8")

flanker_txt = unicode("""
Before you go, there is one final, small task. In the next ~2 minutes, you will
see displays like this\n\n\t\t\t\t\t\t\t\t<<<<<\n\n or like this\n\n\t\t\t\t\t\t\t\t<<><<\n
Pay attention only to the MIDDLE ARROW. Press "right" if it points right, "left"
if it points left. So the correct answer for the top example would be left, and 
in the one below it would be right. Keep your eyes on the little "+" in the centre
of the screen between trials. Got it? Feel free to ask if anything seems unclear.

Hit "Enter" when you are ready to start the trial.
""", "utf-8")

end = unicode("""
This is the end of the Experiment.
Thank you very much for your participation.
""", "utf-8")


"""FUNCTIONS"""

#write data and get out
def escape():
    DATA.to_csv(SAVE_FOLDER + "/logfile_" + V['subject_ID'] + '.csv') #always write df to csv file before escaping the program
    core.quit()


#display info text and wait for key press
def info(string, end = False):
    text.text = string
    text.draw()
    win.flip()
    if end == True:
        keys = ['escape', 'p']
    else:
        keys = ['return', 'escape']
    key=event.waitKeys(keyList=keys)[0]
    if key == 'escape':
        escape()

#record the position of a mouseclick
def mouseclick_pos():
    win.mouseVisible = True
    mouseIsDown, times = mouse.getPressed(getTime=True)#checks if mouse keys [0,1,2] are currently pressed
    if mouseIsDown[0]:
        mouse_pos = mouse.getPos()
        t = times[0]
        m = [mouse_pos, t]
        win.mouseVisible = False
        mouse.clickReset()
    else:
        m = None
    return m


#display options on a practice/test trial, according to options and positions (movies vs. txt)
def make_displayed_set(options, positions_list):
    displayed_set = []
    for nr, stim in enumerate(options):
        pos = positions_list[nr] #pick out the right position from the list
        # make a visual stim, with pos and stim as parameters, add to a list of all_visual_stim 
        if positions_list == MOV_POSITIONS:
            moviefile = trials_dict[stim]["video"]
            displayed_set.append(visual.MovieStim(win, moviefile, units='norm', size=(0.5,0.625), pos=pos, loop=True))
        if positions_list == TXT_POSITIONS:
            try:
                sentence = trials_dict[stim]["sentence"]
            except:
                sentence = re.sub("_", " ", stim) #first, space bar instead of "_"
                for word in sentence.split(): # then replace every word in the dictionary by the phantonean word it has been assigned to
                    sentence = re.sub(word, word_dict[word], sentence)
                sentence = sentence[0].upper() + sentence[1:]
                sentence = "\"" + sentence + ".\"" 
            text = visual.TextStim(win, sentence, units='norm', height = .09, pos=pos, wrapWidth=.8, color=(-1,0.5,1))
            text._pygletTextObj
            displayed_set.append(text)
    return displayed_set


#Chose distractors
# for practice
def choose_practice_distractors(target, block):
    reduced_block = []
    target_length = len(target.split("_")) #split by "_" to get the individual words out
    for item in block:
        if item != target and len(item.split("_")) == target_length: #make sure not to sample the target itself as distractor; and to use distractors of the same length/construction
            reduced_block.append(item)
    while len(reduced_block) < 3: #make sure there are enough items to sample
        add = random.choice(seen)
        if len(add.split("_")) == target_length:
            reduced_block.append(add)
    distractors = random.sample(reduced_block, 3)
    return distractors
    
#for testing
#error function that takes 2 arguments: the target (original) and kind of error
def make_error(target, error, movie=False):
    words = target.split("_")
    
    if error == "morphology":
        for word_id, word in enumerate(words):
            if word.endswith("m"):
                words[word_id] = re.sub("m", "f", word)
            elif word.endswith("f"):
                words[word_id] = re.sub("f", "m", word)

    elif error == "semantics":
        sample_objs = ["bunny", "ball", "gift"]
        sample_verbs = ["throw", "hug", "kick", "give"]
        #one-agent transitives: replace the subject on even trials (and on movie trials)
        if len(words) == 3 and words[1] in sample_objs and (V['trial_nr']%2 == 0 or movie==True): 
            new_subj = "b" if words[0][0] == "r" else "r" 
            new_subj += words[0][1]
            words[0] = new_subj
        #1-agent transitives: replace the object on odd trials
        elif len(words) == 3 and words[1] in sample_objs: 
            sample_objs.remove(words[1])            
            words[1] = random.choice(sample_objs)
        #2-agent trans: replace the verb
        elif len(words) == 3:
            if movie==True: #avoid impossible movies
                sample_verbs = ["hug", "kick"]
            sample_verbs.remove(words[2])#exclude the original verb
            words[2] = random.choice(sample_verbs)#chose another random verb, that is not the original verb
        #ditrans (on even trials): replace the verb
        elif V['trial_nr']%2 == 0: #and len(words) == 4 (can be left out at this point)
            if movie==True:
                sample_verbs.remove("hug") #don't use "hug" on ditransitive trials with movies
                if words[3]=="bunny":
                    sample_verbs.remove("kick") #also don't use "kick" with the bunny
            sample_verbs.remove(words[2])
            words[2] = random.choice(sample_verbs)
        #in ditransitives (odd trials): change the object (in the end)
        else: 
            sample_objs.remove(words[3])
            if movie==True and "bunny" in sample_objs: 
                sample_objs.remove("bunny")
            words[3] = random.choice(sample_objs)
        
    elif error == "syntax":
        #for transitives, switch the verb and object (2nd and 3rd word)
        if len(words)== 3:
            temp = words[1]
            words[1] = words[2]
            words[2] = temp
        #for ditransitives, switch the 2 agents/objects
        else: 
            if V['trial_nr']%2 == 0 and words[0][0] != words[1][0]: # on even trials, switch the agents, if they are of a different colour
                temp = words[0]
                words[0] = words[1]
                words[1] = temp      
            else: #otherwise switch objects       
                temp = words[1]
                words[1] = words[3]
                words[3] = temp
    dist = "_".join(words)
    return dist

        
#make 3 distractors with 2 kinds of errors, and a 3rd distractor that has both
def choose_test_distractors(target, movie=False):
    test_list = [['semantics','morphology'],['semantics', 'syntax'], ['morphology', 'syntax']] #make sure semantics is always first, syntax last (otherwise it will be wrong later) 
    errors = random.choice(test_list) if movie==False else ['semantics', 'morphology'] #don't use syntactic errors on movies
    distractors = []
    for error in errors:
        dist = make_error(target, error, movie=movie)
        distractors.append(dist)   
    dist = make_error(distractors[0], errors[1], movie=movie) #pass the second kind of error to the result of the first kind of error, to get a combination of both error types   
    distractors.append(dist)
    errors.append("+".join(errors))
    return distractors, errors
        

#present parts of Phantonean sentence by sentence
def present_trial(trial, mode): #takes a dictionary as input which stores the trial info
    movie = visual.MovieStim(win, filename=trial["video"], units='norm', size=(0.8,1), pos=(0,0.3), volume=0, loop=True)
    if mode == "written": 
        text_below._pygletTextObj.text = trial["sentence"]
    #read out the sentence, using speech synthesis
    elif mode == "oral":
        oral_lang = sound.Sound(trial["sound"])
        oral_lang.play()
    #display video and written sentence
    for frame in range(270):    
        movie.draw()
        if mode == "written":
            text_below.draw()
        win.flip()
        if event.getKeys(keyList=["escape"]):
            escape()
    info(intermediate)  
      

#A multiple choice trial where a senetence needs to be matched to a video or vice versa 
def test_trial(target, block, mode, testing=False): 
    V["trial_nr"] += 1
    V["target"] = target
    V["mode"] = mode
    positions_list = MOV_POSITIONS if mode == "oral" else TXT_POSITIONS
    #set up all the options (&target)
    if testing == False:
        options = [target] + choose_practice_distractors(target, block)
    else:
        movie = True if positions_list == MOV_POSITIONS else False
        distractors, errors = choose_test_distractors(target, movie=movie)
        options = [target] + distractors                  
    random.shuffle(options)    
    correct_index = options.index(target) #keep track of the index of the target sentence, for later
    trial = trials_dict[target]
    #make them into stim
    choices = make_displayed_set(options, positions_list) #make them into visual stimuli    
    
    #make a stim that is the correct sentence/video as sound/movie
    if positions_list == MOV_POSITIONS:
        text_above._pygletTextObj.text = pick_vid
        #text_above2._pygletTextObj.text = trial["sentence"]
        oral_lang = sound.Sound(trial["sound"])
        oral_lang.play()
    elif positions_list == TXT_POSITIONS:
        text_above._pygletTextObj.text = pick_txt
        moviefile = trial["video"]
        movie = visual.MovieStim(win, moviefile, units='norm', size=(0.6,0.75), pos=(0,0.2), volume=0, loop=True)

    #record a mouseclick    
    answer_pos = None
    mouse.clickReset() #this will set the time of the mouse to 0 (will give the exact RT when mouse is pressed)
    t = 90
    mouseclick = None
    while t > 0:
        if answer_pos != None: #if an answer is given, give feedback (on top of the other stuff - do this in the beginning of the loop in order to have the visual rectangles behind the other stuff)           
            #check if the correct choice was made, depending on position
            z = -.2 if positions_list == MOV_POSITIONS else -.575
            x = 0 if answer_pos[0] < 0 else 1
            y = 0 if answer_pos[1] > z else 2
            answer_index = x+y
            # record answer and accuracy
            V["answer"] = options[answer_index]
            V["accuracy"] = 1 if answer_index == correct_index else 0
            if testing == True:
                V["error"] = "None" if V["accuracy"] == 1 else errors[distractors.index(V["answer"])] #pick up the index of the answer they gave in the distractors, go to that index in the errors to see what kind of error they made
            V["rt"] = rt
            
            #give feedback; this will also give time to clear the mouse
            green = correct_rect_mov if positions_list == MOV_POSITIONS else correct_rect_txt
            green.pos = positions_list[correct_index]
            green.draw() #draw the green rectangle to indicate the correct answer, no matter whether the answer given was correct
            if V["accuracy"] == 0: #if they are wrong, also give them a red rectangle for their own response (& sound, according to condition?) 
                red = fail_rect_mov if positions_list == MOV_POSITIONS else fail_rect_txt
                red.pos = positions_list[answer_index]                
                red.draw()
                if V['condition'] == "anx" and t == 90: #play a failure sound if the condition is anx (start the sound only on the first frame)
                    fail_sound.play()
            t -= 1 #start counting down on every frame, once the answer has been given
            
        #here comes the actual trial
        if positions_list == TXT_POSITIONS:
            movie.draw()

        for stim in choices:
            stim.draw()
        text_above.draw()
        win.flip()
        #record an answer + time
        if mouseclick == None:
            mouseclick = mouseclick_pos()
        if mouseclick != None:
            answer_pos, rt = mouseclick
        #make it possible to get out
        keys = event.getKeys()
        if "escape" in keys:
            escape()
    global DATA
    DATA = DATA.append(V, ignore_index=True)

    #for the "anx" condition, ad around 90 frames of head-shaking
    if V['condition'] == "anx" and V['accuracy']==0:
        for frame in range(90):
            fail_face.draw()
            win.flip()
            
    
#running a block with 10 presentation trials and 4 practice questions     
def run_practice_block(block_nr):
    V["block_nr"] = block_nr+1
    V["phase"] = "training"
    V["error"] = "None"
    #present all (10) stim in a block
    modelist = ["oral", "written"] * (len(blocks[block_nr])/2) #make a list with the same number of oral/written trials, same length as block
    random.shuffle(modelist) #shuffle the mode list, to get random order
    for i,trial in enumerate(blocks[block_nr]):
        present_trial(trials_dict[trial], modelist[i])
    #give them 4 practice trials
    info(practice_trial)
    modelist = ["oral", "written"] * 2
    random.shuffle(modelist)
    for i, target in enumerate(random.sample(blocks[block_nr], 4)):
        test_trial(target, blocks[block_nr], modelist[i])
    if block_nr != 7:
        info(practice_end) # don't give this info on the last block


#running a test block with 10 test questions
def run_test_block(block_nr):
    V["block_nr"] = block_nr+1
    V["phase"] = "testing"
    modelist = ["oral", "written"] * (len(blocks[block_nr])/2) #make a list with the same number of oral/written trials, same length as block
    random.shuffle(modelist) #shuffle the mode list, to get random order
    for i, target in enumerate(blocks[block_nr]):
        test_trial(target, blocks[block_nr], modelist[i], testing=True)
    txt = "This is the end of test round " + str(block_nr-7) + test_block_end
    info(txt)


#running a multiple choice stroop test
def flanker():
    #prepare a pd matrix for the data
    #flanker_columns = ['subject_ID', 'condition', 'arrow', 'accuracy', 'rt']
    #FL_DATA = pd.DataFrame(columns=flanker_columns, index = index)
    #prepare lists to measure mean rts directly
    congruent_mean = []
    incong_mean = []
    #prepare trials
    conditions = ["congruent", "incongruent"]
    arrows = ["left", "right"]
    trials = []
    for condition in conditions:
        for arrow in arrows:
            trials.append([condition, arrow])
    trials=trials*5
    #fixation cross stim
    fix_cross = visual.TextStim(win, "+")
    
    #run trials. each iteration gives 20 trials
    for i in range(5):  #set the number of trials in multiples of 20  
        random.shuffle(trials)    
        for trial in trials:
            target = "<" if trial[1]=="left" else ">"
            if trial[0] == "congruent":
                stimtext = 5*target
            else:
                opposite = ">" if target=="<" else ">"
                stimtext = 2*opposite + target + 2*opposite
            target_stim = visual.TextStim(win, stimtext)
            for frame in range(30):
                fix_cross._pygletTextObj
                fix_cross.draw()
                win.flip()
            target_stim.draw()
            t1 = win.flip()
            key, t2 = event.waitKeys(keyList=["left","right","escape"], timeStamped=True)[0]
            if key == "escape":
                escape() 
            rt = (t2 - t1)*1000 #record rt in ms
            accuracy = 1 if key == trial[1] else 0
            if accuracy == 1 and trial[0] == "congruent":
                congruent_mean.append(rt)
            elif accuracy == 1 and trial[0] == "incongruent":
                incong_mean.append(rt)
    mean_rt_in = sum(incong_mean)/float(len(incong_mean))
    mean_rt_con = sum(congruent_mean)/float(len(congruent_mean))
    flanker_diff = mean_rt_in - mean_rt_con
            #FL_DATA = FL_DATA.append({'subject_ID': V['subject_ID'], 'condition': trial[0], 'arrow': trial[1], 'accuracy': accuracy, 'rt': rt}, ignore_index=True)
    #FL_DATA.to_csv(SAVE_FOLDER + "/flankertask_" + V['subject_ID'] + '.csv')
    return flanker_diff
    

"""Run the experiment"""

#hello&instructions
for txt in [welcome, instructions1, instructions2]:
    info(txt)

#instructions for anx condition
if V['condition'] == "anx":
    info(anx_instructions)
    fail_sound.play()
    for frame in range(90):
        fail_face.draw()
        win.flip()

info(ready)

#learning phase
for block in range(8):
    run_practice_block(block)

#test phase
info(test_start)
for block in range(4):
    run_test_block(block+8) #add 8, to get blocks 9-12 aka 8-11 from the list

#do the flanker test
info(flanker_txt)
DATA['flanker_diff'] = flanker()

#write df to csv file
DATA.to_csv(SAVE_FOLDER + "/logfile_" + V['subject_ID'] + '.csv')

#Bye bye
info(end)



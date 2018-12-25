#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.4),
    on December 23, 2018, at 14:51
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
from datetime import datetime
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'starteExp'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'order': '', 'withRating': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'],expInfo['order'],
                                                         expInfo['withRating'])
trialsLoop = "";

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath=None,
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename + '.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1280, 720), fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructionsGeneral1"
instructionsGeneral1Clock = core.Clock()
imageInstructions1 = visual.ImageStim(
    win=win, name='imageInstructions1',
    image='instructions\\instruction1.png', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "instructionsGeneral2"
instructionsGeneral2Clock = core.Clock()
imageInstructions2 = visual.ImageStim(
    win=win, name='imageInstructions2',
    image='instructions\\instruction2.png', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "instructionsGeneral3"
instructionsGeneral3Clock = core.Clock()
imageInstructions3 = visual.ImageStim(
    win=win, name='imageInstructions3',
    image='instructions\\instruction3.png', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "testFixation"
testFixationClock = core.Clock()
testFixationText = visual.TextStim(win=win, name='testFixationText',
                                   text='+',
                                   font='Arial',
                                   pos=(0, 0), height=0.6, wrapWidth=None, ori=0,
                                   color='white', colorSpace='rgb', opacity=1,
                                   depth=0.0);

# Initialize components for Routine "trialInstructions"
trialInstructionsClock = core.Clock()
conditionInstructionImage = visual.ImageStim(
    win=win, name='conditionInstructionImage',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "trialImageRoutine"
trialImageRoutineClock = core.Clock()
trialImage = visual.ImageStim(
    win=win, name='trialImage',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
probeTest = sound.Sound('A', secs=-1)
probeTest.setVolume(1)
cue_leftSide = visual.ImageStim(
    win=win, name='cue_leftSide',
    image='sin', mask=None,
    ori=0, pos=(-0.87, 0), size=None,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
cue_rightSide = visual.ImageStim(
    win=win, name='cue_rightSide',
    image='sin', mask=None,
    ori=0, pos=(0.87, 0), size=None,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "ratingRoutineValence"
ratingRoutineValenceClock = core.Clock()
valenceRating = visual.RatingScale(win=win, name='valenceRating', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1,
                                   high=9, labels=[''], scale='', showAccept=False)
valenceRatingImage = visual.ImageStim(
    win=win, name='valenceRatingImage',
    image=u'rating\\Sam_valence.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
imageValenceText = visual.ImageStim(
    win=win, name='imageValenceText',
    image=u'rating\\valenceText.png', mask=None,
    ori=0, pos=(0, 0.5), size=None,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ratingRoutineArousal"
ratingRoutineArousalClock = core.Clock()
arousalRating = visual.RatingScale(win=win, name='arousalRating', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1,
                                   high=9, labels=[''], scale='')
arousalRatingImage = visual.ImageStim(
    win=win, name='arousalRatingImage',
    image=u'rating\\Sam_arousal.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
imageArousalText = visual.ImageStim(
    win=win, name='imageArousalText',
    image=u'rating\\arousalText.png', mask=None,
    ori=0, pos=(0, 0.5), size=None,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "instructionsHabituationRoutine"
instructionsHabituationRoutineClock = core.Clock()
imageInstructionsHabituation = visual.ImageStim(
    win=win, name='imageInstructionsHabituation',
    image='instructions\\instruction_hab.png', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "getPreparedForHabituation"
getPreparedForHabituationClock = core.Clock()
imagePrepareForHab = visual.ImageStim(
    win=win, name='imagePrepareForHab',
    image='instructions/instruction_getprepared.png', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "habituationTrial"
habituationTrialClock = core.Clock()
probeSoundHabituation = sound.Sound(u'probe\\Startle_48kHz.wav', secs=-1)
probeSoundHabituation.setVolume(1)
fixationHabituation = visual.TextStim(win=win, name='fixationHabituation',
                                      text='+',
                                      font='Arial',
                                      pos=(0, 0), height=0.6, wrapWidth=None, ori=0,
                                      color='white', colorSpace='rgb', opacity=1,
                                      depth=-1.0);

# Initialize components for Routine "taskStartsSoonRoutine"
taskStartsSoonRoutineClock = core.Clock()
taskStartsSoonImage = visual.ImageStim(
    win=win, name='taskStartsSoonImage',
    image='instructions\\instruction_begin.png', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "testFixation"
testFixationClock = core.Clock()
testFixationText = visual.TextStim(win=win, name='testFixationText',
                                   text='+',
                                   font='Arial',
                                   pos=(0, 0), height=0.6, wrapWidth=None, ori=0,
                                   color='white', colorSpace='rgb', opacity=1,
                                   depth=0.0);

# Initialize components for Routine "trialInstructions"
trialInstructionsClock = core.Clock()
conditionInstructionImage = visual.ImageStim(
    win=win, name='conditionInstructionImage',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "trialImageRoutine"
trialImageRoutineClock = core.Clock()
trialImage = visual.ImageStim(
    win=win, name='trialImage',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
probeTest = sound.Sound('A', secs=-1)
probeTest.setVolume(1)
cue_leftSide = visual.ImageStim(
    win=win, name='cue_leftSide',
    image='sin', mask=None,
    ori=0, pos=(-0.87, 0), size=None,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
cue_rightSide = visual.ImageStim(
    win=win, name='cue_rightSide',
    image='sin', mask=None,
    ori=0, pos=(0.87, 0), size=None,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "ratingRoutineValence"
ratingRoutineValenceClock = core.Clock()
valenceRating = visual.RatingScale(win=win, markerColor='white', name='rating', marker=u'triangle', size=1.30, pos=[0.01, -0.04], low=1, high=5,
                        precision=1, showValue=False, markerExpansion=0, scale=u'',  markerStart=u'3',
                        tickHeight=u'0', showAccept=False, lineColor='Black',textSize=0.0, leftKeys='left',
                        rightKeys='right')
valenceRatingImage = visual.ImageStim(
    win=win, name='valenceRatingImage',
    image=u'rating\\Sam_valence.png', mask=None,
    ori=0, pos=(0, -0.28), size=(0.98, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

imageValenceText = visual.ImageStim(
    win=win, name='imageValenceText',
    image=u'rating\\valenceText.png', mask=None,
    ori=0, pos=(0, 0.5), size=None,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ratingRoutineArousal"
ratingRoutineArousalClock = core.Clock()

arousalRating = visual.RatingScale(win=win, markerColor='white', name='rating', marker=u'triangle', size=1.30, pos=[0.01, -0.04], low=1, high=5,
                            precision=1, showValue=False, markerExpansion=0, scale=u'',  markerStart=u'3',
                            tickHeight=u'0', showAccept=False, lineColor='Black',textSize=0.0, leftKeys='left',
                            rightKeys='right')
arousalRatingImage = visual.ImageStim(
    win=win, name='arousalRatingImage',
    image=u'rating\\Sam_arousal.png', mask=None,
    ori=0, pos=(0, -0.28), size=(0.98, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
imageArousalText = visual.ImageStim(
    win=win, name='imageArousalText',
    image=u'rating\\arousalText.png', mask=None,
    ori=0, pos=(0, 0.5), size=None,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "endExp"
endExpClock = core.Clock()
endImage = visual.ImageStim(
    win=win, name='endImage',
    image=u'instructions/finish.png', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# ------Prepare to start Routine "instructionsGeneral1"-------
t = 0
instructionsGeneral1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsGeneral1Components = [imageInstructions1, key_resp_2]
for thisComponent in instructionsGeneral1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructionsGeneral1"-------
while continueRoutine:
    # get current time
    t = instructionsGeneral1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *imageInstructions1* updates
    if t >= 0.0 and imageInstructions1.status == NOT_STARTED:
        # keep track of start time/frame for later
        imageInstructions1.tStart = t
        imageInstructions1.frameNStart = frameN  # exact frame index
        imageInstructions1.setAutoDraw(True)

    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsGeneral1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructionsGeneral1"-------
for thisComponent in instructionsGeneral1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys', key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "instructionsGeneral1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructionsGeneral2"-------
t = 0
instructionsGeneral2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
spaceContinue = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsGeneral2Components = [imageInstructions2, spaceContinue]
for thisComponent in instructionsGeneral2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructionsGeneral2"-------
while continueRoutine:
    # get current time
    t = instructionsGeneral2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *imageInstructions2* updates
    if t >= 0.0 and imageInstructions2.status == NOT_STARTED:
        # keep track of start time/frame for later
        imageInstructions2.tStart = t
        imageInstructions2.frameNStart = frameN  # exact frame index
        imageInstructions2.setAutoDraw(True)

    # *spaceContinue* updates
    if t >= 0.0 and spaceContinue.status == NOT_STARTED:
        # keep track of start time/frame for later
        spaceContinue.tStart = t
        spaceContinue.frameNStart = frameN  # exact frame index
        spaceContinue.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(spaceContinue.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if spaceContinue.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            spaceContinue.keys = theseKeys[-1]  # just the last key pressed
            spaceContinue.rt = spaceContinue.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsGeneral2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructionsGeneral2"-------
for thisComponent in instructionsGeneral2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if spaceContinue.keys in ['', [], None]:  # No response was made
    spaceContinue.keys = None
thisExp.addData('spaceContinue.keys', spaceContinue.keys)
if spaceContinue.keys != None:  # we had a response
    thisExp.addData('spaceContinue.rt', spaceContinue.rt)
thisExp.nextEntry()
# the Routine "instructionsGeneral2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructionsGeneral3"-------
t = 0
instructionsGeneral3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsGeneral3Components = [imageInstructions3, key_resp_3]
for thisComponent in instructionsGeneral3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructionsGeneral3"-------
while continueRoutine:
    # get current time
    t = instructionsGeneral3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *imageInstructions3* updates
    if t >= 0.0 and imageInstructions3.status == NOT_STARTED:
        # keep track of start time/frame for later
        imageInstructions3.tStart = t
        imageInstructions3.frameNStart = frameN  # exact frame index
        imageInstructions3.setAutoDraw(True)

    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsGeneral3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructionsGeneral3"-------
for thisComponent in instructionsGeneral3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys', key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "instructionsGeneral3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practiceTrials = data.TrialHandler(nReps=1, method='random',
                                   extraInfo=expInfo, originPath=-1,
                                   trialList=data.importConditions(u'practiceTrials.xlsx'),
                                   seed=None, name='practiceTrials')
thisExp.addLoop(practiceTrials)  # add the loop to the experiment
thisPracticeTrial = practiceTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
if thisPracticeTrial != None:
    for paramName in thisPracticeTrial.keys():
        exec (paramName + '= thisPracticeTrial.' + paramName)

for thisPracticeTrial in practiceTrials:
    currentLoop = practiceTrials
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
    if thisPracticeTrial != None:
        for paramName in thisPracticeTrial.keys():
            exec (paramName + '= thisPracticeTrial.' + paramName)

    # ------Prepare to start Routine "testFixation"-------
    t = 0
    testFixationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    testFixationComponents = [testFixationText]
    for thisComponent in testFixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "testFixation"-------
    while continueRoutine:
        # get current time
        t = testFixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *testFixationText* updates
        if t >= 0.0 and testFixationText.status == NOT_STARTED:
            # keep track of start time/frame for later
            testFixationText.tStart = t
            testFixationText.frameNStart = frameN  # exact frame index
            testFixationText.setAutoDraw(True)
        frameRemains = 0.0 + fixationLength - win.monitorFramePeriod * 0.75  # most of one frame period left
        if testFixationText.status == STARTED and t >= frameRemains:
            testFixationText.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testFixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "testFixation"-------
    for thisComponent in testFixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "testFixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "trialInstructions"-------
    t = 0
    trialInstructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    conditionInstructionImage.setImage(conditionInst)
    # keep track of which components have finished
    trialInstructionsComponents = [conditionInstructionImage]
    for thisComponent in trialInstructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trialInstructions"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialInstructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *conditionInstructionImage* updates
        if t >= 0.0 and conditionInstructionImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            conditionInstructionImage.tStart = t
            conditionInstructionImage.frameNStart = frameN  # exact frame index
            conditionInstructionImage.setAutoDraw(True)
        frameRemains = 0.0 + 2 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if conditionInstructionImage.status == STARTED and t >= frameRemains:
            conditionInstructionImage.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialInstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trialInstructions"-------
    for thisComponent in trialInstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # ------Prepare to start Routine "trialImageRoutine"-------
    t = 0
    trialImageRoutineClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    trialImage.setImage(picture)
    probeTest.setSound(showProbe, secs=-1)
    cue_leftSide.setImage(conditionCue)
    cue_rightSide.setImage(conditionCue)
    # keep track of which components have finished
    trialImageRoutineComponents = [trialImage, probeTest, cue_leftSide, cue_rightSide]
    for thisComponent in trialImageRoutineComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trialImageRoutine"-------
    while continueRoutine:
        # get current time
        t = trialImageRoutineClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *trialImage* updates
        if t >= 0.0 and trialImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            trialImage.tStart = t
            trialImage.frameNStart = frameN  # exact frame index
            trialImage.setAutoDraw(True)
        frameRemains = 0.0 + 10 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if trialImage.status == STARTED and t >= frameRemains:
            trialImage.setAutoDraw(False)
        # start/stop probeTest
        if t >= probeTime and probeTest.status == NOT_STARTED:
            # keep track of start time/frame for later
            probeTest.tStart = t
            probeTest.frameNStart = frameN  # exact frame index
            probeTest.play()  # start the sound (it finishes automatically)


        # *cue_leftSide* updates
        if t >= 0.0 and cue_leftSide.status == NOT_STARTED:
            # keep track of start time/frame for later
            cue_leftSide.tStart = t
            cue_leftSide.frameNStart = frameN  # exact frame index
            cue_leftSide.setAutoDraw(True)
        frameRemains = 0.0 + 10 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if cue_leftSide.status == STARTED and t >= frameRemains:
            cue_leftSide.setAutoDraw(False)

        # *cue_rightSide* updates
        if t >= 0.0 and cue_rightSide.status == NOT_STARTED:
            # keep track of start time/frame for later
            cue_rightSide.tStart = t
            cue_rightSide.frameNStart = frameN  # exact frame index
            cue_rightSide.setAutoDraw(True)
        frameRemains = 0.0 + 10 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if cue_rightSide.status == STARTED and t >= frameRemains:
            cue_rightSide.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialImageRoutineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trialImageRoutine"-------
    for thisComponent in trialImageRoutineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    probeTest.stop()  # ensure sound has stopped at end of routine
    # the Routine "trialImageRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "ratingRoutineValence"-------
    t = 0
    ratingRoutineValenceClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    valenceRating.reset()
    # keep track of which components have finished
    ratingRoutineValenceComponents = [valenceRating, valenceRatingImage, imageValenceText]
    for thisComponent in ratingRoutineValenceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "ratingRoutineValence"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ratingRoutineValenceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *valenceRating* updates
        if t >= 0.0 and valenceRating.status == NOT_STARTED:
            # keep track of start time/frame for later
            valenceRating.tStart = t
            valenceRating.frameNStart = frameN  # exact frame index
            valenceRating.setAutoDraw(True)
        continueRoutine &= valenceRating.noResponse  # a response ends the trial

        # *valenceRatingImage* updates
        if t >= 0.0 and valenceRatingImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            valenceRatingImage.tStart = t
            valenceRatingImage.frameNStart = frameN  # exact frame index
            valenceRatingImage.setAutoDraw(True)
        frameRemains = 0.0 + 5 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if valenceRatingImage.status == STARTED and t >= frameRemains:
            valenceRatingImage.setAutoDraw(False)

        # *imageValenceText* updates
        if t >= 0.0 and imageValenceText.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageValenceText.tStart = t
            imageValenceText.frameNStart = frameN  # exact frame index
            imageValenceText.setAutoDraw(True)
        frameRemains = 0.0 + 5 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if imageValenceText.status == STARTED and t >= frameRemains:
            imageValenceText.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ratingRoutineValenceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "ratingRoutineValence"-------
    for thisComponent in ratingRoutineValenceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for practiceTrials (TrialHandler)
    practiceTrials.addData('valenceRating.response', valenceRating.getRating())
    practiceTrials.addData('valenceRating.rt', valenceRating.getRT())
    practiceTrials.addData('valenceRating.history', valenceRating.getHistory())

    # ------Prepare to start Routine "ratingRoutineArousal"-------
    t = 0
    ratingRoutineArousalClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    arousalRating.reset()
    # keep track of which components have finished
    ratingRoutineArousalComponents = [arousalRating, arousalRatingImage, imageArousalText]
    for thisComponent in ratingRoutineArousalComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "ratingRoutineArousal"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ratingRoutineArousalClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *arousalRating* updates
        if t >= 0.0 and arousalRating.status == NOT_STARTED:
            # keep track of start time/frame for later
            arousalRating.tStart = t
            arousalRating.frameNStart = frameN  # exact frame index
            arousalRating.setAutoDraw(True)
        continueRoutine &= arousalRating.noResponse  # a response ends the trial

        # *arousalRatingImage* updates
        if t >= 0.0 and arousalRatingImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            arousalRatingImage.tStart = t
            arousalRatingImage.frameNStart = frameN  # exact frame index
            arousalRatingImage.setAutoDraw(True)
        frameRemains = 0.0 + 5 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if arousalRatingImage.status == STARTED and t >= frameRemains:
            arousalRatingImage.setAutoDraw(False)

        # *imageArousalText* updates
        if t >= 0.0 and imageArousalText.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageArousalText.tStart = t
            imageArousalText.frameNStart = frameN  # exact frame index
            imageArousalText.setAutoDraw(True)
        frameRemains = 0.0 + 5 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if imageArousalText.status == STARTED and t >= frameRemains:
            imageArousalText.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ratingRoutineArousalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "ratingRoutineArousal"-------
    for thisComponent in ratingRoutineArousalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for practiceTrials (TrialHandler)
    practiceTrials.addData('arousalRating.response', arousalRating.getRating())
    practiceTrials.addData('arousalRating.rt', arousalRating.getRT())
    practiceTrials.addData('arousalRating.history', arousalRating.getHistory())
    thisExp.nextEntry()

# completed 1 repeats of 'practiceTrials'


# ------Prepare to start Routine "instructionsHabituationRoutine"-------
t = 0
instructionsHabituationRoutineClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
spaceContinue2 = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsHabituationRoutineComponents = [imageInstructionsHabituation, spaceContinue2]
for thisComponent in instructionsHabituationRoutineComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructionsHabituationRoutine"-------
while continueRoutine:
    # get current time
    t = instructionsHabituationRoutineClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *imageInstructionsHabituation* updates
    if t >= 0.0 and imageInstructionsHabituation.status == NOT_STARTED:
        # keep track of start time/frame for later
        imageInstructionsHabituation.tStart = t
        imageInstructionsHabituation.frameNStart = frameN  # exact frame index
        imageInstructionsHabituation.setAutoDraw(True)

    # *spaceContinue2* updates
    if t >= 0.0 and spaceContinue2.status == NOT_STARTED:
        # keep track of start time/frame for later
        spaceContinue2.tStart = t
        spaceContinue2.frameNStart = frameN  # exact frame index
        spaceContinue2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(spaceContinue2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if spaceContinue2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            spaceContinue2.keys = theseKeys[-1]  # just the last key pressed
            spaceContinue2.rt = spaceContinue2.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsHabituationRoutineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructionsHabituationRoutine"-------
for thisComponent in instructionsHabituationRoutineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if spaceContinue2.keys in ['', [], None]:  # No response was made
    spaceContinue2.keys = None
thisExp.addData('spaceContinue2.keys', spaceContinue2.keys)
if spaceContinue2.keys != None:  # we had a response
    thisExp.addData('spaceContinue2.rt', spaceContinue2.rt)
thisExp.nextEntry()
# the Routine "instructionsHabituationRoutine" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "getPreparedForHabituation"-------
t = 0
getPreparedForHabituationClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
getPreparedForHabituationComponents = [imagePrepareForHab]
for thisComponent in getPreparedForHabituationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "getPreparedForHabituation"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = getPreparedForHabituationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *imagePrepareForHab* updates
    if t >= 0.0 and imagePrepareForHab.status == NOT_STARTED:
        # keep track of start time/frame for later
        imagePrepareForHab.tStart = t
        imagePrepareForHab.frameNStart = frameN  # exact frame index
        imagePrepareForHab.setAutoDraw(True)
    frameRemains = 0.0 + 2 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if imagePrepareForHab.status == STARTED and t >= frameRemains:
        imagePrepareForHab.setAutoDraw(False)

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in getPreparedForHabituationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "getPreparedForHabituation"-------
for thisComponent in getPreparedForHabituationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
habituationLoop = data.TrialHandler(nReps=10, method='random',
                                    extraInfo=expInfo, originPath=-1,
                                    trialList=[None],
                                    seed=None, name='habituationLoop')
thisExp.addLoop(habituationLoop)  # add the loop to the experiment
thisHabituationLoop = habituationLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisHabituationLoop.rgb)
if thisHabituationLoop != None:
    for paramName in thisHabituationLoop.keys():
        exec (paramName + '= thisHabituationLoop.' + paramName)

for thisHabituationLoop in habituationLoop:
    currentLoop = habituationLoop
    # abbreviate parameter names if possible (e.g. rgb = thisHabituationLoop.rgb)
    if thisHabituationLoop != None:
        for paramName in thisHabituationLoop.keys():
            exec (paramName + '= thisHabituationLoop.' + paramName)

    # ------Prepare to start Routine "habituationTrial"-------
    t = 0
    habituationTrialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    habituationTrialComponents = [probeSoundHabituation, fixationHabituation]
    for thisComponent in habituationTrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "habituationTrial"-------
    while continueRoutine:
        # get current time
        t = habituationTrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop probeSoundHabituation
        if t >= 0.0 and probeSoundHabituation.status == NOT_STARTED:
            # keep track of start time/frame for later
            probeSoundHabituation.tStart = t
            probeSoundHabituation.frameNStart = frameN  # exact frame index
            probeSoundHabituation.play()  # start the sound (it finishes automatically)

        # *fixationHabituation* updates
        if t >= 0.0 and fixationHabituation.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixationHabituation.tStart = t
            fixationHabituation.frameNStart = frameN  # exact frame index
            fixationHabituation.setAutoDraw(True)
        frameRemains = 0.0 + 1.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixationHabituation.status == STARTED and t >= frameRemains:
            fixationHabituation.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in habituationTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "habituationTrial"-------
    for thisComponent in habituationTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    probeSoundHabituation.stop()  # ensure sound has stopped at end of routine
    # the Routine "habituationTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# completed 10 repeats of 'habituationLoop'


# ------Prepare to start Routine "taskStartsSoonRoutine"-------
t = 0
taskStartsSoonRoutineClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
taskStartsSoonRoutineComponents = [taskStartsSoonImage]
for thisComponent in taskStartsSoonRoutineComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "taskStartsSoonRoutine"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = taskStartsSoonRoutineClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *taskStartsSoonImage* updates
    if t >= 0.0 and taskStartsSoonImage.status == NOT_STARTED:
        # keep track of start time/frame for later
        taskStartsSoonImage.tStart = t
        taskStartsSoonImage.frameNStart = frameN  # exact frame index
        taskStartsSoonImage.setAutoDraw(True)
    frameRemains = 0.0 + 2 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if taskStartsSoonImage.status == STARTED and t >= frameRemains:
        taskStartsSoonImage.setAutoDraw(False)

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in taskStartsSoonRoutineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "taskStartsSoonRoutine"-------
for thisComponent in taskStartsSoonRoutineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trialsList = "";
if expInfo['order'] == '1':
    trialsList = u'trials1.xlsx'
else:
    trialsList = u'trials2.xlsx'

# set up handler to look after randomisation of conditions etc
trialsLoop = data.TrialHandler(nReps=1, method='sequential',
                               extraInfo=expInfo, originPath=-1,
                               trialList=data.importConditions(
                                   trialsList),
                               seed=None, name='trialsLoop')
thisExp.addLoop(trialsLoop)  # add the loop to the experiment
thisTrialsLoop = trialsLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsLoop.rgb)
if thisTrialsLoop != None:
    for paramName in thisTrialsLoop.keys():
        exec (paramName + '= thisTrialsLoop.' + paramName)

for thisTrialsLoop in trialsLoop:
    currentLoop = trialsLoop
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsLoop.rgb)
    if thisTrialsLoop != None:
        for paramName in thisTrialsLoop.keys():
            exec (paramName + '= thisTrialsLoop.' + paramName)

    # ------Prepare to start Routine "testFixation"-------
    t = 0
    testFixationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    testFixationComponents = [testFixationText]
    for thisComponent in testFixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "testFixation"-------
    while continueRoutine:
        # get current time
        t = testFixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *testFixationText* updates
        if t >= 0.0 and testFixationText.status == NOT_STARTED:
            # keep track of start time/frame for later
            testFixationText.tStart = t
            testFixationText.frameNStart = frameN  # exact frame index
            testFixationText.setAutoDraw(True)
        frameRemains = 0.0 + fixationLength - win.monitorFramePeriod * 0.75  # most of one frame period left
        if testFixationText.status == STARTED and t >= frameRemains:
            testFixationText.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testFixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "testFixation"-------
    for thisComponent in testFixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "testFixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "trialInstructions"-------
    t = 0
    trialInstructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    conditionInstructionImage.setImage(conditionInst)
    # keep track of which components have finished
    trialInstructionsComponents = [conditionInstructionImage]
    for thisComponent in trialInstructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trialInstructions"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialInstructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *conditionInstructionImage* updates
        if t >= 0.0 and conditionInstructionImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            conditionInstructionImage.tStart = t
            conditionInstructionImage.frameNStart = frameN  # exact frame index
            conditionInstructionImage.setAutoDraw(True)
        frameRemains = 0.0 + 2 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if conditionInstructionImage.status == STARTED and t >= frameRemains:
            conditionInstructionImage.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialInstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trialInstructions"-------
    for thisComponent in trialInstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # ------Prepare to start Routine "trialImageRoutine"-------
    t = 0
    trialImageRoutineClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    trialImage.setImage(picture)
    probeTest.setSound(showProbe, secs=-1)
    cue_leftSide.setImage(conditionCue)
    cue_rightSide.setImage(conditionCue)
    # keep track of which components have finished
    trialImageRoutineComponents = [trialImage, probeTest, cue_leftSide, cue_rightSide]
    for thisComponent in trialImageRoutineComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trialImageRoutine"-------
    while continueRoutine:
        # get current time
        t = trialImageRoutineClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *trialImage* updates
        if t >= 0.0 and trialImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            trialImage.tStart = t
            trialImage.frameNStart = frameN  # exact frame index
            trialImage.setAutoDraw(True)
        frameRemains = 0.0 + 10 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if trialImage.status == STARTED and t >= frameRemains:
            trialImage.setAutoDraw(False)
        # start/stop probeTest
        if t >= probeTime and probeTest.status == NOT_STARTED:
            # keep track of start time/frame for later
            probeTest.tStart = t
            probeTest.frameNStart = frameN  # exact frame index
            probeTest.play()  # start the sound (it finishes automatically)
            time=datetime.now();
            trialsLoop.addData('probeTimeSeconds', time);
            trialsLoop.addData('probeTimeMicroSeconds', time.microsecond);

        # *cue_leftSide* updates
        if t >= 0.0 and cue_leftSide.status == NOT_STARTED:
            # keep track of start time/frame for later
            cue_leftSide.tStart = t
            cue_leftSide.frameNStart = frameN  # exact frame index
            cue_leftSide.setAutoDraw(True)
        frameRemains = 0.0 + 10 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if cue_leftSide.status == STARTED and t >= frameRemains:
            cue_leftSide.setAutoDraw(False)

        # *cue_rightSide* updates
        if t >= 0.0 and cue_rightSide.status == NOT_STARTED:
            # keep track of start time/frame for later
            cue_rightSide.tStart = t
            cue_rightSide.frameNStart = frameN  # exact frame index
            cue_rightSide.setAutoDraw(True)
        frameRemains = 0.0 + 10 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if cue_rightSide.status == STARTED and t >= frameRemains:
            cue_rightSide.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialImageRoutineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trialImageRoutine"-------
    for thisComponent in trialImageRoutineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    probeTest.stop()  # ensure sound has stopped at end of routine
    # the Routine "trialImageRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "ratingRoutineValence"-------

    if expInfo['withRating'] == 'no':
        continue;
    t = 0
    ratingRoutineValenceClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    valenceRating.reset()
    # keep track of which components have finished
    ratingRoutineValenceComponents = [valenceRating, valenceRatingImage, imageValenceText]
    for thisComponent in ratingRoutineValenceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "ratingRoutineValence"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ratingRoutineValenceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *valenceRating* updates
        if t >= 0.0 and valenceRating.status == NOT_STARTED:
            # keep track of start time/frame for later
            valenceRating.tStart = t
            valenceRating.frameNStart = frameN  # exact frame index
            valenceRating.setAutoDraw(True)
        continueRoutine &= valenceRating.noResponse  # a response ends the trial

        # *valenceRatingImage* updates
        if t >= 0.0 and valenceRatingImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            valenceRatingImage.tStart = t
            valenceRatingImage.frameNStart = frameN  # exact frame index
            valenceRatingImage.setAutoDraw(True)
        frameRemains = 0.0 + 5 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if valenceRatingImage.status == STARTED and t >= frameRemains:
            valenceRatingImage.setAutoDraw(False)

        # *imageValenceText* updates
        if t >= 0.0 and imageValenceText.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageValenceText.tStart = t
            imageValenceText.frameNStart = frameN  # exact frame index
            imageValenceText.setAutoDraw(True)
        frameRemains = 0.0 + 5 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if imageValenceText.status == STARTED and t >= frameRemains:
            imageValenceText.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ratingRoutineValenceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "ratingRoutineValence"-------
    for thisComponent in ratingRoutineValenceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trialsLoop (TrialHandler)
    rate = valenceRating.getHistory()[len(valenceRating.getHistory()) - 1][0]
    rt = valenceRating.getHistory()[len(valenceRating.getHistory()) - 1][1]
    trialsLoop.addData('valenceRating.response', valenceRating.getRating())
    trialsLoop.addData('valenceRating.rt', valenceRating.getRT())
    trialsLoop.addData('valenceRating.history', valenceRating.getHistory())

    # ------Prepare to start Routine "ratingRoutineArousal"-------
    t = 0
    ratingRoutineArousalClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    arousalRating.reset()
    # keep track of which components have finished
    ratingRoutineArousalComponents = [arousalRating, arousalRatingImage, imageArousalText]
    for thisComponent in ratingRoutineArousalComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "ratingRoutineArousal"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ratingRoutineArousalClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *arousalRating* updates
        if t >= 0.0 and arousalRating.status == NOT_STARTED:
            # keep track of start time/frame for later
            arousalRating.tStart = t
            arousalRating.frameNStart = frameN  # exact frame index
            arousalRating.setAutoDraw(True)
        continueRoutine &= arousalRating.noResponse  # a response ends the trial

        # *arousalRatingImage* updates
        if t >= 0.0 and arousalRatingImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            arousalRatingImage.tStart = t
            arousalRatingImage.frameNStart = frameN  # exact frame index
            arousalRatingImage.setAutoDraw(True)
        frameRemains = 0.0 + 5 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if arousalRatingImage.status == STARTED and t >= frameRemains:
            arousalRatingImage.setAutoDraw(False)

        # *imageArousalText* updates
        if t >= 0.0 and imageArousalText.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageArousalText.tStart = t
            imageArousalText.frameNStart = frameN  # exact frame index
            imageArousalText.setAutoDraw(True)
        frameRemains = 0.0 + 5 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if imageArousalText.status == STARTED and t >= frameRemains:
            imageArousalText.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ratingRoutineArousalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "ratingRoutineArousal"-------
    for thisComponent in ratingRoutineArousalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trialsLoop (TrialHandler)
    rate = arousalRating.getHistory()[len(arousalRating.getHistory()) - 1][0]
    rt = arousalRating.getHistory()[len(arousalRating.getHistory()) - 1][1]
    trialsLoop.addData('arousalRating.response', arousalRating.getRating())
    trialsLoop.addData('arousalRating.rt', arousalRating.getRT())
    trialsLoop.addData('arousalRating.history', arousalRating.getHistory())
    thisExp.nextEntry()

# completed 1 repeats of 'trialsLoop'


# ------Prepare to start Routine "endExp"-------
t = 0
endExpClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
endExpComponents = [endImage, key_resp_4]
for thisComponent in endExpComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "endExp"-------
while continueRoutine:
    # get current time
    t = endExpClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *endImage* updates
    if t >= 0.0 and endImage.status == NOT_STARTED:
        # keep track of start time/frame for later
        endImage.tStart = t
        endImage.frameNStart = frameN  # exact frame index
        endImage.setAutoDraw(True)

    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endExpComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "endExp"-------
for thisComponent in endExpComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys', key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "endExp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename + '.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

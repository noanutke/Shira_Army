#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.4),
    on December 12, 2018, at 11:15
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

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'starteExp'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'order': '', 'withRating': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'],expInfo['order'],
                                                         expInfo['withRating'])

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

# Initialize components for Routine "instructionsGeneralRoutine"
instructionsGeneralRoutineClock = core.Clock()
instructionsGeneralImage = visual.ImageStim(
    win=win, name='instructionsGeneralImage',
    image=u'C:\\Users\\NOA\\Shira_Army\\startle\\newVersion\\instructions\\general.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "instructionsHabituationRoutine"
instructionsHabituationRoutineClock = core.Clock()
instructionsHabituationImage = visual.ImageStim(
    win=win, name='instructionsHabituationImage',
    image=u'C:\\Users\\NOA\\Shira_Army\\startle\\newVersion\\instructions\\habituation.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "habituationTrial"
habituationTrialClock = core.Clock()
probeSoundHabituation = sound.Sound(u'C:\\Users\\NOA\\Shira_Army\\startle\\newVersion\\probe\\Startle_48kHz.wav',
                                    secs=-1)
probeSoundHabituation.setVolume(1)
fixationHabituation = visual.TextStim(win=win, name='fixationHabituation',
                                      text=u'+',
                                      font=u'Arial',
                                      pos=(0, 0), height=0.6, wrapWidth=None, ori=0,
                                      color=u'white', colorSpace='rgb', opacity=1,
                                      depth=-1.0);

# Initialize components for Routine "taskStartsSoonRoutine"
taskStartsSoonRoutineClock = core.Clock()
taskStartsSoonImage = visual.ImageStim(
    win=win, name='taskStartsSoonImage',
    image=u'C:\\Users\\NOA\\Shira_Army\\startle\\newVersion\\instructions\\taskStartsSoon.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "testFixation"
testFixationClock = core.Clock()
testFixationText = visual.TextStim(win=win, name='testFixationText',
                                   text=u'+',
                                   font=u'Arial',
                                   pos=(0, 0), height=0.6, wrapWidth=None, ori=0,
                                   color=u'white', colorSpace='rgb', opacity=1,
                                   depth=0.0);

# Initialize components for Routine "trialInstructionsRoutine"
trialInstructionsRoutineClock = core.Clock()
trialInsturctionsImage = visual.ImageStim(
    win=win, name='trialInsturctionsImage',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "trialImageRoutine"
trialImageRoutineClock = core.Clock()
trialImage = visual.ImageStim(
    win=win, name='trialImage',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
probeTest = sound.Sound('A', secs=-1)
probeTest.setVolume(1)

# Initialize components for Routine "ratingRoutineValence"
ratingRoutineValenceClock = core.Clock()
valenceRating = visual.RatingScale(win=win, name='rating', marker=u'triangle', size=1.53, pos=[0.01, -0.04], low=0, high=10,
                            precision=1, showValue=False, markerExpansion=0, scale=u'',  markerStart=u'5',
                            tickHeight=u'0', showAccept=False, lineColor='Black',textSize=0.0, leftKeys='left',
                            rightKeys='right')
valenceRatingImage = visual.ImageStim(
    win=win, name='valenceRatingImage',
    image=u'C:\\Users\\NOA\\Shira_Army\\startle\\newVersion\\rating\\Sam_valence.png', mask=None,
    ori=0, pos=(0, -0.3), size=(0.95, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "ratingRoutineArousal"
ratingRoutineArousalClock = core.Clock()
arousalRating =  visual.RatingScale(win=win, name='rating', marker=u'triangle', size=1.53, pos=[0.01, -0.04], low=0, high=10,
                            precision=1, showValue=False, markerExpansion=0, scale=u'',  markerStart=u'5',
                            tickHeight=u'0', showAccept=False, lineColor='Black',textSize=0.0, leftKeys='left',
                            rightKeys='right')
arousalRatingImage = visual.ImageStim(
    win=win, name='arousalRatingImage',
    image=u'C:\\Users\\NOA\\Shira_Army\\startle\\newVersion\\rating\\Sam_arousal.png', mask=None,
    ori=0, pos=(0, -1), size=(1, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# ------Prepare to start Routine "instructionsGeneralRoutine"-------
t = 0
instructionsGeneralRoutineClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
spaceContinue = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsGeneralRoutineComponents = [instructionsGeneralImage, spaceContinue]
for thisComponent in instructionsGeneralRoutineComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructionsGeneralRoutine"-------
while continueRoutine:
    # get current time
    t = instructionsGeneralRoutineClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instructionsGeneralImage* updates
    if t >= 0.0 and instructionsGeneralImage.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructionsGeneralImage.tStart = t
        instructionsGeneralImage.frameNStart = frameN  # exact frame index
        instructionsGeneralImage.setAutoDraw(True)

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
    for thisComponent in instructionsGeneralRoutineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        thisExp.saveAsWideText(filename + '.csv')
        thisExp.saveAsPickle(filename)
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructionsGeneralRoutine"-------
for thisComponent in instructionsGeneralRoutineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if spaceContinue.keys in ['', [], None]:  # No response was made
    spaceContinue.keys = None
thisExp.addData('spaceContinue.keys', spaceContinue.keys)
if spaceContinue.keys != None:  # we had a response
    thisExp.addData('spaceContinue.rt', spaceContinue.rt)
thisExp.nextEntry()
# the Routine "instructionsGeneralRoutine" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructionsHabituationRoutine"-------
t = 0
instructionsHabituationRoutineClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
spaceContinue2 = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsHabituationRoutineComponents = [instructionsHabituationImage, spaceContinue2]
for thisComponent in instructionsHabituationRoutineComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructionsHabituationRoutine"-------
while continueRoutine:
    # get current time
    t = instructionsHabituationRoutineClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instructionsHabituationImage* updates
    if t >= 0.0 and instructionsHabituationImage.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructionsHabituationImage.tStart = t
        instructionsHabituationImage.frameNStart = frameN  # exact frame index
        instructionsHabituationImage.setAutoDraw(True)

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
        thisExp.saveAsWideText(filename + '.csv')
        thisExp.saveAsPickle(filename)
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
            thisExp.saveAsWideText(filename + '.csv')
            thisExp.saveAsPickle(filename)
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
        thisExp.saveAsWideText(filename + '.csv')
        thisExp.saveAsPickle(filename)
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "taskStartsSoonRoutine"-------
for thisComponent in taskStartsSoonRoutineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

trialsList = "";
if expInfo['order'] == '1':
    trialsList = u'C:\\Users\\NOA\\Shira_Army\\startle\\newVersion\\trials1.xlsx'
else:
    trialsList = u'C:\\Users\\NOA\\Shira_Army\\startle\\newVersion\\trials2.xlsx'

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
            thisExp.saveAsWideText(filename + '.csv')
            thisExp.saveAsPickle(filename)
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

    # ------Prepare to start Routine "trialInstructionsRoutine"-------
    t = 0
    trialInstructionsRoutineClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    trialInsturctionsImage.setImage(condition)
    # keep track of which components have finished
    trialInstructionsRoutineComponents = [trialInsturctionsImage]
    for thisComponent in trialInstructionsRoutineComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trialInstructionsRoutine"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialInstructionsRoutineClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *trialInsturctionsImage* updates
        if t >= 0.0 and trialInsturctionsImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            trialInsturctionsImage.tStart = t
            trialInsturctionsImage.frameNStart = frameN  # exact frame index
            trialInsturctionsImage.setAutoDraw(True)
        frameRemains = 0.0 + 2 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if trialInsturctionsImage.status == STARTED and t >= frameRemains:
            trialInsturctionsImage.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialInstructionsRoutineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            thisExp.saveAsWideText(filename + '.csv')
            thisExp.saveAsPickle(filename)
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trialInstructionsRoutine"-------
    for thisComponent in trialInstructionsRoutineComponents:
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
    # keep track of which components have finished
    trialImageRoutineComponents = [trialImage, probeTest]
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
            thisExp.saveAsWideText(filename + '.csv')
            thisExp.saveAsPickle(filename)
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

    if expInfo['withRating'] == 'no':
        continue;

    # ------Prepare to start Routine "ratingRoutineValence"-------
    t = 0
    ratingRoutineValenceClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    valenceRating.reset()
    # keep track of which components have finished
    ratingRoutineValenceComponents = [valenceRating, valenceRatingImage]
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
            thisExp.saveAsWideText(filename + '.csv')
            thisExp.saveAsPickle(filename)
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "ratingRoutineValence"-------
    for thisComponent in ratingRoutineValenceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trialsLoop (TrialHandler)
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
    ratingRoutineArousalComponents = [arousalRating, arousalRatingImage]
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
            thisExp.saveAsWideText(filename + '.csv')
            thisExp.saveAsPickle(filename)
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "ratingRoutineArousal"-------
    for thisComponent in ratingRoutineArousalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trialsLoop (TrialHandler)
    trialsLoop.addData('arousalRating.response', arousalRating.getRating())
    trialsLoop.addData('arousalRating.rt', arousalRating.getRT())
    trialsLoop.addData('arousalRating.history', arousalRating.getHistory())
    thisExp.nextEntry()

# completed 10 repeats of 'trialsLoop'

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename + '.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

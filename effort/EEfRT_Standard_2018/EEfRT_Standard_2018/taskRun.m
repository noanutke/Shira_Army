function [completionStatus numberOfPresses goalReachedCount completionTime] = taskRun(window, dexterity, difficulty, resX, resY)
load('hebrewStrings')
% Setup progress bar
progressBarMatrix = ones(400,100);
progressBarMatrix = progressBarMatrix*256;
progressBarMatrix(1:2,:) = 0;
progressBarMatrix(399:400,:) = 0;
progressBarMatrix(:,1:2) = 0;
progressBarMatrix(:,99:100) = 0;

Screen(window,'PutImage',progressBarMatrix); %Display to window pointer
Screen(window, 'Flip'); %Sync


% button setup
KbName('UnifyKeyNames');

if dexterity == 'r'  
    HARD  = KbName('s');
    EASY = KbName('l');
elseif dexterity == 'l'
    HARD  = KbName('k');
    EASY = KbName('s');
    showKey = 'k';
end


%This section takes difficulty into account and assigns the required key
%based on the selected dexterity. 
if (difficulty == 'h')
    if dexterity == 'r'
        requiredKeyPosition = HARD;
        showKey = 's';
    else
        requiredKeyPosition = HARD;
        showKey = 'k';
    end
else
    if dexterity == 'r'
        requiredKeyPosition = EASY;
        showKey = 'k';
    else
        requiredKeyPosition = EASY;
        showKey = 's';
    end
end
    
    
%Set the time and number of presses here
if (difficulty == 'e') %Easy task
    numberOfPresses = 30;
    timeDelta = 7;
else
    %Hard task
    numberOfPresses = 98;
    timeDelta = 21;
end

displayRows = floor(399/numberOfPresses); %This is the number of pixel rows to "fill" dependent on the difficulty of the task.
goalReachedCount = 0;

acceptingInput = 1;

%The following code starts a timer. Keyboard input is expected. The timer
%continues its countdown, and progress is shown via a screen refresh.
%Pressing a key increments the "goalReachedCount" variable."
startTime = GetSecs;
currentTime = GetSecs;

while (currentTime < startTime+timeDelta) && (goalReachedCount < numberOfPresses) %While the time has not yet expired...
    [pressed, secs, kbData] = KbCheck;
    if (pressed == 1) && (kbData(requiredKeyPosition) == 1) && (acceptingInput==1)
        progressBarMatrix(399-goalReachedCount*displayRows:end,:) = 100; %"Fills" the progress bar based on the task difficulty
        goalReachedCount = goalReachedCount + 1; %Increment the number of key presses logged.
        pause(0.1);
        %FlushEvents;]
        acceptingInput=0;
    end
    currentTime = GetSecs;
    Screen('DrawText', window, uint8(timeLeft), ceil(resX/2)+100, ceil(resY/2)-300, 255); %Show remaining time
    Screen('DrawText', window, num2str((startTime+timeDelta)-currentTime), ceil(resX/2), ceil(resY/2)-300, 255); %Show remaining time
    if showKey == 'k' 
        Screen('DrawText', window, uint8(pressLamed),ceil(resX/2)-180, ceil(resY/2)+300, 255); %Show reminder.
    else
        Screen('DrawText', window, uint8(pressDaled),ceil(resX/2)-180, ceil(resY/2)+300, 255); %Show reminder.
    end

    Screen(window,'PutImage',progressBarMatrix); %Display to window pointer
    Screen(window, 'Flip'); %Write framebuffer to display
    
    if pressed~=1
        acceptingInput=1;
    end
end

completionTime = currentTime - startTime;

if goalReachedCount == numberOfPresses
    disp(uint8(taskCompletedSuccessfuly));
    completionStatus = 1;
else
    disp(uint8(timeOut));
    completionStatus = 0;
end
clc
ListenChar(0);







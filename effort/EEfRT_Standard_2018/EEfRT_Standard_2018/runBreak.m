function runBreak(window, resX, resY)
load('hebrewStrings');
Screen(window,'FillRect',0);
Screen(window, 'Flip');
Screen('DrawText', window, uint8(practiceComplete),floor(resX/2)-70,floor(resY/2), 255); %Show reminder.
Screen('DrawText', window, uint8(pressSpaceToStartTest), floor(resX/2)-70,floor(resY/2)+100, 255);
Screen(window, 'Flip');
KbWait;
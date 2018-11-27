whichScreen = 0;
Screen('Preference','SkipSynctests',1); %WARNING: REMOVE FOR PRODUCTION SYSTEM!
window = Screen(whichScreen, 'OpenWindow');
Screen(window,'FillRect',0);
Screen(window, 'Flip');
pause(2.5);
Screen(window, 'DrawText', 'You completed the task!', (1024/2)-150, (768/2)-10, 255);
Screen(window, 'Flip');
pause(2.5);

clear screen
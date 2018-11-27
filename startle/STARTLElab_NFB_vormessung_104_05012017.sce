scenario = "STARTLElab_NFB_vormessung_104_05012017.sce"; ### einstellen
pcl_file = "STARTLElab_NFB_vormessung_104_05012017.pcl";


default_background_color = 125,125,125;
default_text_color = 0,0,0;
default_text_align = align_center;
default_font_size = 52;
default_font = "Arial";

#rating
active_buttons = 3;   
button_codes = 1,2,3;
default_all_responses = true;

response_logging = log_all;
response_matching = simple_matching;

# write_codes = false;
write_codes = true;
response_port_output = false;
pulse_width = 20;



begin;

###########################################
###             Stimulation             ###
###########################################

$nr_pics = 36 ; 

array {
LOOP $pic_nr '$nr_pics';
	$pic = '$pic_nr + 1';
	bitmap { filename = "pic$pic.jpg"; preload = true;};
ENDLOOP;
} pics;

array {
LOOP $value_nr 9;
	$value = '$value_nr + 1';
	bitmap { filename = "rating$value.png"; preload = true; };
ENDLOOP;
} rating;

bitmap { filename = "Sam_valence.png"; preload = true; } sam_valence;
bitmap { filename = "Sam_arousal.png"; preload = true; } sam_arousal;
bitmap { filename = "rating1.png"; preload = true; } rating_scale;
bitmap { filename = "pic1.jpg"; preload = true;} placeholder;

text { caption = "+"; description = "5"; } plus;


picture { text plus; x=0; y=0; } fixcross;
picture { bitmap { filename = "ende_run.png";} ende_run_bmp; x=0;y=0;}ende;

wavefile { filename = "Startle_48kHz.wav"; } white_noise;


sound { wavefile white_noise;} startle; ### Achtung!!! Einstellen!!! (attenuation=.201)


text { caption = "Betrachten"; preload = true;} betrachten_inst ;
text { caption = "Regulieren"; preload = true;} regulieren_inst;

array {
	bitmap { filename = "arrow_down_small.png"; alpha = -1; preload = true;} arrow_down_small;
	bitmap { filename = "dot_small.png"; alpha = -1; preload = true;} dot_small;
} small_arrows;


array {
	text { caption = "Pause"; preload = true;} relax;
} relax_array;


# DissoRating:

array {
LOOP $pic 10;
	bitmap { filename = "Rating\\scale$pic.jpg"; preload = true;};
ENDLOOP;
} scale;

bitmap{filename="Rating\\scale0.jpg";preload=true;}scale_default_pic;
bitmap{filename="Rating\\range.jpg";preload=true;}range_pic;
bitmap{filename="Rating\\range_reg.jpg";preload=true;}range_reg_pic;


trial {
   trial_duration = forever;
	trial_type = specific_response;   
	terminator_button= 3;
	picture { bitmap { filename = "Rating\\DissoRating_Instruktion.png";}disso_instruction; x = 0; y = 0;}; 
} dissoinstruction_trial;  

trial {
   trial_duration = forever;
	trial_type = specific_response;   
	terminator_button= 2;
	picture { bitmap { filename = "Rating\\DissoRating_Instruktion_post.png";}disso_instruction_post; x = 0; y = 0;}; 
} dissoinstructionpost_trial;    

bitmap { filename = "Rating\\dissoziation_depersonalisation.jpg"; preload = true; }dissoziation_depersonalisation_bm;
bitmap { filename = "Rating\\dissoziation_derealisation.jpg"; preload = true; }dissoziation_derealisation_bm;
bitmap { filename = "Rating\\dissoziation_hoeren.jpg"; preload = true; }dissoziation_hoeren_bm;
bitmap { filename = "Rating\\dissoziation_analgesie.jpg"; preload = true; }dissoziation_analgesie_bm;
bitmap { filename = "Rating\\entspannt.jpg"; preload = true; }entspannt_bm;
bitmap { filename = "Rating\\reg_erfolg.jpg"; preload = true; }reg_erfolg_bm;

picture {bitmap dissoziation_depersonalisation_bm; x= 0; y = 20;} dissorating_pic;

trial {                                  
    trial_type = first_response;     
		picture { bitmap reg_erfolg_bm; x=0; y=0; bitmap scale_default_pic; x=0; y=-20; bitmap range_reg_pic; x = 0; y = -90;}scale_default;
		time = 0;
		duration = response;
} dissorating_trial; 




#Habituationsinstruktion


trial {
	picture { bitmap { filename = "instruction_hab.png"; preload = true;}; x = 0; y = 0; };
	time = 0;
	code = "habinsr";
	duration = response;
} hab_instruction_trial;

trial {
	picture { bitmap { filename = "instruction_getprepared.png"; preload = true;}; x = 0; y = 0; };
	duration = 4000;
} getprepared_instruction_trial;


### Beginn 


trial {
	picture { bitmap { filename = "instruction_begin.png"; preload = true;}; x = 0; y = 0; };
	duration = 2000;
} begin_instruction_trial;

#Habituation trials

trial {
	trial_type = fixed;
	stimulus_event {
		picture fixcross;
		code = "fixcross";
	} hab_fixcross_event;
	stimulus_event {
      sound startle;
		code = "hab_sound";
		port_code = 10;
   } hab_startle_event;
} hab_startle_trial;

trial {
	trial_type = fixed;
	picture { text { caption = "Gleich geht's los"; description = "prepare";}; x = 0; y = 0; };
	code = "t0";
	duration = 2000;
} start_trial;

# blank trial
trial {
	stimulus_event {
		picture { text { caption = "+"; font_color = 125,125,125;}; x = 0; y = 0; };
		code = "blank";
	} blank_event;
} blank_trial;

# fixcross trial
trial {
	stimulus_event {
		picture fixcross;
		code = "fixcross";
		duration = 2000;
	}fixcross_event;
} fixcross_trial;



# ER trial 

trial {
	stimulus_event {
		picture { text plus; x = 0; y = 0; } instruction_object;
	} instr_event;
	stimulus_event {
      picture { background_color = 125,125,125; bitmap placeholder; x = 0; y = 0; bitmap arrow_down_small; x = -596; y = 0; bitmap arrow_down_small; x = 596; y = 0; } er_pic;
		code = "pic_onset";
		deltat = 2000;
		duration = 10000;
	 } er_event;
	stimulus_event {
      sound startle;
   } er_startle_event;
} er_trial;



# rating trials
trial {
	trial_type = first_response;
	stimulus_event {
		picture { bitmap sam_valence; x=0; y=100; bitmap {filename = "rating1.png";}; x=0; y=-100; } rating_sam;     
		code = "rating";
	} rating_event;
} rating_trial;


# ende
trial {
	trial_duration = 8000;
	trial_type = fixed;    	
	picture ende;
	code = "ende"; 
} trial_ende; 


###########################################
###      Eye-Tracker Kalibrierung       ###
###########################################

calibration bitmap
trial {
	trial_duration=forever ;
	trial_type=correct_response; 
	picture {bitmap { filename = "cal1360_2.bmp"; height = 1024; scale_factor = scale_to_height;}pic_calib; x = 0; y = 0;};
	target_button = 2;
} calib;

picture
{
   bitmap 
	{
		filename = "black circle.bmp"; # schwarzer kreis
		trans_src_color = 255,255,255; 
	};
   x = 0; 
	y = 0;
} et_calibration;


 #show error message if connection could not be established 
picture{
	text{	
		caption = "Could not establish connection to Eye Tracker \n\n\n Check if the Eye Tracker \n is running and the \n Network Settings are set correctly"; 
		font_size = 20; 
		font_color = 20, 20, 20;
		transparent_color = 0,0,0;
	};
	x = 0;
	y = 0;
}connect_error;


# show accuracy message after the calibration has been validated 
picture { 
   text { 
			caption = "Validation Results: \n\n Accuracy X: - \n Accuracy Y: -";
			font_size = 20; 
			font_color = 20, 20, 20;
			transparent_color = 0,0,0;
			preload = false;
   }accuracy_text;   
   x = 0; 
	y = 0;
}accuracy_picture;

 
# show error message if resolution is wrong 
picture{
	text{	
		caption = "Please change \n the screen resolution \n of your computer \n to 1280 x 1024 or 1680 x 1050"; 
		font_size = 20; 
		font_color = 20, 20, 20;
		transparent_color = 0,0,0;
	};
	x = 0;
	y = 0;}resolution_error;


# show end message if experiment has been finished 
picture{
	text{	
		caption = "End of Experiment"; 
		font_size = 20; 
		font_color = 20, 20, 20;
		transparent_color = 0,0,0;
	};
	x = 0;
	y = 0;
}end_experiment;


picture{
	text{	
		caption = "Try to acquire data..."; 
		font_size = 20; 
		font_color = 20, 20, 20;
		transparent_color = 0,0,0;
	};
	x = 0;
	y = 0;
}data_acquisition;

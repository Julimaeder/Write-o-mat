# -*- coding: utf-8 -*-

from Writeomat import Geschichte_4, Geschichte_3, Geschichte_2
import random
#if Geschlecht == "M":    
#Name_Held = input("Wähle den Namen deines Protagonisten \n-->")
#Name_Held = input("a")

liste_Geschichte_2 = ["Dreirad", "schwebenden Besen", "schnell hüpfenden Frosch", "Papierflieger", "Panzer"]
liste_Geschichte_3 = ["Werwolf", "Riese", "Vampir", "Lavahund", "Babydragon"]


#if Geschlecht == "M":
Name_Held = input("Wähle den Namen deines Protagonisten \n-->").capitalize()
#elif Geschlecht == "W":
 #   Name_Held = input("Wähle den Namen deiner Protagonistin \n-->")
#else:
  #  print(Geschlecht)

Fantasy_Geschichte_1 = Geschichte_4("Wähle den Helden deiner Geschichte ",
           "Eine gute Fee","Ein Oger","Ein Magier","Ein Zwerg",
           f"Es war einmal eine gute Fee namens {Name_Held}. Diese ",
           f"Es war einmal ein Oger namens {Name_Held}. Dieser ",
           f"Es war einmal ein Magier namens {Name_Held}. Dieser ",
           f"Es war einmal ein kleiner Zwerg namens {Name_Held}. Dieser ")

Fantasy_Geschichte_2 = Geschichte_4("Welches Gefährt hat dein Held",
           "Ein Pferd","Ein Riese","Eine Kutsche","Zu Fuß",
           "reitet voller Hochmut ein starkes Ross. ",
           "sitzt auf dem Rücken eines stolzen Riesen. ",
           "fährt in einer Kutsche dem Horizont entgegen. ",
           "schreitet tapfer zu fuße voran. ",
           f"bewegt sich auf einem {random.choice(liste_Geschichte_2)} fort. ")

Fantasy_Geschichte_3 = Geschichte_4("Wähle den Antagonisten deiner Geschichte",
           "Ein dunkler Magier","Ein Drache","Eine Truppe Orks","kein Antagonist",
           "text dunkler Magier",
           "Text Drache",
           "Text Ork",
           "Antagonist Text",
           f"Text {random.choice(liste_Geschichte_3)}. Dieser")  

Fantasy_Geschichte_4 = Geschichte_3("Test für 3 Auswahlmöglichkeiten und zum testen kommt hier noch ein längerer Text rein.",
           "Nummero uno","Option 2","Drei",
           "Nummero uno",
           "Option 2",
           "Drei")

Fantasy_Geschichte_5 = Geschichte_2("Test für zwei Auswahlmöglichkeiten Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magn",
           "Nummero uno","Option 2",
           "Nummero uno",
           "Option 2")

            # Vorerst nicht appenden, soll am Anfang ausgewählt, und später genutzt werden
if Fantasy_Geschichte_3 != "d":
    Name_Gegner = input("\nWähle den Namen deines Antagonisten \n-->").capitalize()
else: 
    Name_Gegner = ("")
    
            
Fantasy_Geschichte_Text_1 = ""

def Titelblatt(Fanatsy_Geschichte_1):
    if "Fee" in Fantasy_Geschichte_1:
        return(
        """                                                                                                      
                                                                                                              
                        #(&              ,@@@@@@@@@@@@@                                                       
                            .@@@@*      @@@@@@@@@@@@@@@@&          .(                                         
                           (    *@@,    @@@@@@@@@@%,@@@@@          @@#                                        
                                  @@@    @@@@@@@@@@   (@@        %@@@@                                        
                                    @@@  ,@@@@@@@@#    (@,   .@@@@@@@@@                                       
                       &@@    #@@@@%, @@@#  @,  #@@@@*   @&@@@@@@@@@@@@.                                      
                      &            *@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@                                       
                   .(                      .,(@@@@@@@@@(@@@@@@@@@@@@@@#                                       
               (@@@#                         @@@@@@@@@@@@@@@@@@@@@@@@                                         
                    (                        .@@@@@@@@@@@@@@@@@@@#                                            
         @@*                                  *@@@@@@@@@@@@&(%#/.                                             
            , /,     /@@#                       @@@@@@@@@@@@@@@@@@@@                                          
            #@@(            &                    *@@@@@@@@@@@@@@@@@@@.                                        
  .@@@&   &%       ,*      @@&                   .%@@@@@@@@@@@@@@@@@@@@                                       
   .       .       (/% ,%.                   @@@@@@@@@@@@@@@@@@@@@@@@@,                                       
        &     /.                           @@@@@@@@@@@@@@@@@@@@@@@@                                           
#@@    #.&   ,,*   *@@#   &@@#            @@@@@@@@@@@@@@@@@@@@&&%                                             
 .            @@@   /      .                  (@#@@@@@@@@@@@@@(                                               
   ,&,   @@@  ..@                                    @@@@@@@@@@                                               
          /.                                          @@@@*@@@@&                                              
                                                       @@@@ @@@@#                                             
                                                        *@@@& @@@@@                                           
                                                          @@@@  &@@@%                                         
                                                           %@@/   %@@&                                        
                                                            .@@     %@&                                       
                                                              @@      @@                                      
                                                               @@@,     @@@                                   
                                                                .@%       %@.                                 
                                                                  %(        .(                                
                                                                     
        """
               )
    elif "Oger" in Fantasy_Geschichte_1:
        return(
        """
                                                                               
                             ,(#(,,,,,,,,,,,,,,(#(                            
                          (#,,,,,,,,,,,,,,,,,,,,,,,,#(                        
                       /#/,,,,,,,,,,,,,,,,,,,,,,,,,,,,,#*           .(##,(#   
   ((,,,#/.          /#*,,(%####,,,,,,,,,,,,,,,,,###%,,,,#,        (##,#,,,#* 
  #*,,,%,*#/.       (#,#%/#/**,*%%##*,,,,,,,##%%%###%%#%#,#(      (#/,(*,,,*#*
 ((****(*,,/#/    *#/,,,,,,,,,,,,,,,,,,,,,*#*,*****,,,,,,,,(#   (#/,,,**,,,*##
 ##(*******,,*##//#(,,,,,*********,,**,,,,,,*****(((/**,,,,,(,*,,,,*#%%####(((
 (((((######%#*,,,,,,,,,#,*(#(*,,(,,,(,,,,,,,,,*(%%%#*,,,,,,,,,**%###((       
           ####%**,,,*(# /(%&%(, *(,(/,,,,,**#..#%%%(#...%/,,**##(            
              ###*,,,,*%/####%%#(,,,,#(((##(*,,##%##%(*,,,,,,,,*#             
              (#**,,,,,,,,,,,,(#,,,,,,,,,,,,,*,(#/,,,,,,,,,,,,*,(#            
             (#/******,,,,,,*(**********,,***,,*,*/*,,,,,,,*,,*,*#/           
            .(#************(////%%(///////////#%%*((***********,,*#,          
            (##****,*#(*,,,,,,,,,,,,,#%#%##*,,,,,,,,,,#%#(******,*#/          
            (##**,,,,/*********,,,**/,,,,,,*(*,,,*,*,,,,,,,,(*****(#          
            (##*****,,/%##********,,(********,,********/##%*,,,,**/#          
            (#%*****,,,(,//,..*###((///////////(#%.. .,*,/,,,,****/#.         
            #(#******,,,//,/,.  ...(....(....,,..,,/%*,#*,,,******/#          
            ((#/*******,,,(*,.*#((//////(/////((%%,,,#/,,,,*******(#          
             ##%**********,,*%*,,,.,,*##(/*,.,,,,,#/,,,,,*********#(          
             ####/**********,,,,,*#%%#((/((#%%/,,,,,,,***********%#           
              /##%//***********,,,,,,,,,,,,,,,,,,,************/(%(            
                ###%(///**********,*************************//%(*             
                  ###%#////*******************************//%#/               
                     ###%//////************************///%#,                 
                       ###%#////////////////////****//*#%(                    
                          ##%&#//////////////////////&%(                      
                             ####%%%%&&&&&&&&&&&&%%(((     
                             
        """
               )
    elif "Magier" in Fantasy_Geschichte_1:
        return(
        """
                                       /(*                                          
     (,,/*   *%                      *%(/((((/#&&.                                   
    .*,,.,.,,,#,                   &((///******((((%&                                
     /*%*.&,                   ,&##((/************(/(&#                              
  .%,,*#/,/##/               &(((/**/(((/((((/*****(((%                              
.(,./(/*(/*..*(             &#(/*/(/%#    ,%#/,****((&.                              
/*,,(**%****%/                 ...  .(&&%#((*****/*((&                               
 .#,,*%*/%             ,#&&&&/.    &#/(/**///******((%%                              
     %///&          ,#/(/////((((&#%(#%//*/*********/#/&.                            
     ,%/((*         .&##%&&&&&&%((((((((//////*/*//*///(&                            
      ##((#.        &..,,,,,,..,/*&%((////**//********(%,                            
       &(//%       &,..,,,,,,,....,*&#(#/*****/##%#/(&,                              
       .%%@#,*&#   &,,,,,,,,,,,,,...,/&(/((/////((#&&&#.                             
     //.........*&(%&..,,,,,,..,,.@...*%*/&(%&&((/*/*//(/%                           
     /&**#&%@#,,,%,.&#&/,,,.....%(..., #*(&,, *(/&%///(%##&.                         
       @..,.(%%*.,&.*/(/(((##%#..... (&&(/##..    ,,,,,%*   .*#                      
        %/*,,&#,,,&,(#(****(#&,,&. *&..&.. (&&(....      ..,%*.%.                    
         %**,%/@.,@,.&(/**/#@,,(/.,//.../,.%&((/#(########&%,.(*                     
           %/(/(%#&.(/(/*/#&,,,& .*#.,*#**%(#%&#//*****,**/(#@./                     
            &/(#&#&((#(**#&*,.*( .*#.*%./#(&##%##%#%&//****/(@                       
            %((/#%%*/##(/(&,.,#.....*&.%#(&#(#&((/*(#**,*,*//%&*                     
             &/#/#.      .(,.,& .,**&*&(#%#((%%(/**********//&%&((&(                 
             ,(((/#      (*,.,& .*/#/&/&%#(#&%((///*///**///(&%#%%%%##.              
              %#//%.    *&,,.,% .,&%%%#@#((&%@.,#%#(/((/*///(#%(/#%(&                
               &/((%   /%&,,.,(....//&#&%#%&#.(&/....%(/#&(((#%(#&#*                 
               .((#%. %##%(,,.,% ,,   .,,&,,.,.,/(&#/(/(&.((..%%#%                   
                /#%#&%(((((/((((((((/((((//##%(,,,,.,*//#&&#%(&(%                    
                 %%%((////(////(//(///((//////#####&#//%&#%&%(#                      
               %#(((///(////////////////////(//(//////(/##%&&/                       
              &(#/////////////////////////(///////////////*/(##                      
             %((///(#(//***/////*/**/*////////////(//////////(#%(                    
             (%.#..#.%((((#%#((/(((%((/****/(((****/((/*///(####*%                   
                 #%*#.***/%(/,*(.,(/#..*(#*(../%%&/#...%&%#..%(.**                   
                                    .*/(&%&&%*,...,#&&,...%&(                        
       
        """
               )
    elif "Zwerg" in Fantasy_Geschichte_1:
        return(
        """
                                     ,%%.                                       
                         /(*/(,,,,/////////,,*                                  
                    ,,*////////////%///////////,                                
                  ,////(/.....((/////////////////,                              
                 ,/(./.........,....///////////////                             
                */,.*.,.......,.(....,(//(////###//(                            
                * ...  /....#   #...,,* (/#####%#(//    ..,      ,.,            
              /  ...(@#...../&@%....,,*  ######/##//     ..,*  ,.., ..          
             (  ..*   ......,. .....,,,   %####  ##/*     ...,,.,,..,/          
             / ...........,/.........,,.  ###           .,....,.../....*        
            *   .....,.....,/.......,,,  *(##        ./,,.............*         
            ,.    .,,.%&@@@(.......,,.   .(#   /.(,,,,,,,,.......,.             
        ...,,.       .,**/..,///*..      ./,,,,,,,,,,,,,,,,,**                  
     .,,,,,,,...        ..            ....*,,,,,,,,,,,,,**,,,,                  
  /.,,,,,,,,,**                      .,/**,,,,,,,,,****/(                       
 .,,,*,,.****//....       .     ......**/*******#                               
(,,,,,,,,,,,,.,*/((..............*,,,****                                       
 (,,,,,,,,,,/,,,,,,&&&#*,,,,,*,,,,,,,,***/                                      
   ****/,,*..,,,,,,,**,,,,,,,,,,,,,,,,****,                                     
      /*...,.,,,,,,,,,,,,,,,,,,,,,,,,,,***/                                     
        ...,.,,,,,,(&&@,,,,,,,,,,,,,,,,,**%                                     
       *.,,...,,,,,,&&@,,,,,,,,,,,,,,,,%@@@                                     
             .,,,,,,,,,,,,,,,,,,,,,&&&&&*****                                   
             ,#&&&*,*.....*#&&&&&&&%**,,,/****                                  
            .,,,,,*/&.*&&*/&/**,,,,,,,,,******(                                 
           .,,,,,,,,,**##*,,,,,,,,,,,,,/****/                                   
             ,,,,,,/*//((##*,,,,,,,,,/#                                         
                 /***(((((#%  ,,*(((###                                         
                  (###%(#%%%   (((((##                                          
               *(#########%% (######%%%                                         
            ((&##########%(#########%%%*                                        
         ############&(############%%%%                                         
                     %#####%%%%%%,        
                                     
        """
               )
    else:
        return (f"FEHLER! Fantasy_Geschichte_1 = {Fantasy_Geschichte_1}")
'''
Todo:
    - Name_Gegner hinzufügen
Ideen: 
    - Einen Begleiter optional mitnehmen 
    - Zufallsevent
'''

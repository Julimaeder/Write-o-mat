# -*- coding: utf-8 -*-
from Writeomat import Geschichte_2, Geschichte_3, Geschichte_4

Name_Held = input("Wähle den Namen deines Protagonisten \n-->").capitalize()

SciFi_Geschichte_1 = Geschichte_2("Wähle den Helden deiner Geschichte ",
           "a) Super Held \nb) Bösewicht",
           f"Es war einmal in einer fernen Galaxie ein Held {Name_Held}. Dieser ",
           f"Es war einmal in einer fernen Galaxie ein Bösewicht namens {Name_Held} the destroyer. Dieser ")

SciFi_Geschichte_2 = Geschichte_2("An welchem Ort willst du starten",
           "a) Raumschiff \nb) Planet Auria",
           "war in seinem riesen Raumschiff mit dem er durch die Galaxie reiste. ",
           "landete auf dem Planeten Auria, welcher bekannt für seine freundlichen Bewohner ist. ")

def Titelblatt(SciFi_Geschichte_1):
    if "Held" in SciFi_Geschichte_1:
        return(
        """

                                              @@@@                              
                    #@@@@@@@@@@               @@@@                              
            (%        @@@@@@@@@@              @@@@                              
#%%%%%%#*.(%%%%%(.*#%%%%( ,# @@             &%@@@@%%%#%%%%%%/                   
    %%%%%%%%%%%%%%%%%%%%%%%%@@@#          .@@*//,,@@@@@@%%%%%%%%%%%%%%%%%%#     
      #%%%%%%%%%%%%     @@@@@@%@@         @@@@,@@@@@@@@@%%%%%%%%%%%%%%%%%       
                        @@ @@@@@@        @@@ @@@@@@& @@@%%%%%%%%%%%%%%%%        
                       &@#  @@@@@       @@@* @@@@@@  &@@@%%%%%%%%%%%#*          
                        @/ @@@@@@@      @@  &@@@@@@,  @@#.%%%%%%%%%%%           
                        @#@&&&&@@&,     @&  @&@&@&&@ @@@   %%%%%%%%.            
                        (@@@@@@@@@       @ (@@@ @@@@@@@     %%%                 
                        &@@@  @@@@          @@@  @@@@        %(                 
                        @@@   @@@           @@#   *@@                           
                       #@@    @@@           @@@    @@@#                         
                      *@@@    @@@           @@@@   @@@@                         
                      @@@     @@            @@(     (@@                         
                      @@      @@           *@@       @@                         
                     @@       @@@        @@@@@      @@@                         
                     @                               @@                         


        """
               )
    elif "Bösewicht" in SciFi_Geschichte_1:
        return(
        """

         .##.                                                    ,#(              
           .@@@@(.                                          ,(@@@%.               
             ,@@@@@@@(.                                .(@@@@@@@,                 
               (@@@@@@@@@&/.                      .(&@@@@@@@@@/                   
                 #@@@@@@@@@@@@%*             ./&@@@@@@@@@@@@#                     
                                                                                  
                                                                                  
                                                                                  
                        .(@@@@@@@@@@*    (@@@@@@@@@@/                             
                            .#@@@@@@@@.*@@@@@@@@(                                 
                                ,#@@@@@@@@@@(.                                    
                                    ,#@@(.                                        
                                                                                  
                                                                                  
                                                                                  
                                                                                  
.,,       ,,    ,,     ,,         .,.             ,,        ,,    .,,      ,,     
 /@@    ,@@.   ,@@.    @@*        #@(            &@@@      .@@.   (@@@/   .@@     
  *@&  ,@@.    ,@@.    @@*        #@(          .&@,*@&.    .@@.   (@%.&@* .@@     
   *@&,@@.     ,@@.    @@*        #@(         .&@,  *@&.   .@@.   (@%  ,@@,@@     
    ,@@&.      ,@@.    @@@@@@@&   #@@@@@@@,  .&@*    *@&.  .@@.   (@%    /@@@     


        """
               )
   
    else:
        return (f"FEHLER! SciFi_Geschichte_1 = {SciFi_Geschichte_1}")


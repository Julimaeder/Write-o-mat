# -*- coding: utf-8 -*-

import Writeomat
from Writeomat import Geschichte_2, Geschichte_3, Geschichte_4

Name_Held = input("Wähle den Namen deines Protagonisten \n-->")

SciFi_Geschichte_1 = Writeomat.Geschichte_2("Wähle den Helden deiner Geschichte ",
                                " Super Held"," Bösewicht",
                                f"Es war einmal in einer fernen Galaxie ein Held {Name_Held}. Dieser ",
                                f"Es war einmal in einer fernen Galaxie ein Bösewicht namens {Name_Held} the destroyer. Dieser ")

SciFi_Geschichte_2 = Writeomat.Geschichte_2("An welchem Ort willst du starten",
                                "Raumschiff","Planet Auria",
                                "Er war in seinem riesen Raumschiff mit dem er durch die Galaxie reiste. ",
                                "Er landete auf dem Planeten Auria, welcher bekannt für seine freundlichen Bewohner ist. ")


if SciFi_Geschichte_1 == Writeomat.Geschichte:
    print(
f"""
{Name_Held} war ein tapferer Krieger, der sich dazu verpflichtet hatte, die Galaxie vor dem Bösen zu schützen. Er hatte unzählige Abenteuer erlebt und viele Gefahren überstanden, aber nichts konnte ihn auf das vorbereiten, was ihn auf dem Planeten Auria erwartete.\n
Als er mit seinem Raumschiff landete, bemerkte er sofort, dass etwas nicht stimmte. Die Straßen waren leer, die Gebäude zerstört und überall lagen tote Körper. Er wusste, dass er schnell handeln musste, um die Bewohner des Planeten zu retten.\n
{Name_Held} entdeckte bald, dass der böse Wissenschaftler Dr. X den Planeten angegriffen hatte. Er hatte eine Armee von Killer Robotern erschaffen, um die Bewohner des Planeten zu unterwerfen.\n
{Name_Held} kämpfte mutig gegen die Roboter und schaffte es schlussendlich Dr. X zu besiegen und den Planeten zu retten. Die Bewohner dankten ihm für seine Tapferkeit und {Name_Held} reiste zufrieden in sein Raumschiff zurück, wissend, dass er wieder eine Galaxie gerettet hatte.
"""
        )

else:
    print(
f"""
{Name_Held} the destroyer war ein mächtiger Bösewicht, der nur ein Ziel hatte: die Galaxie zu unterwerfen. Er hatte bereits viele Planeten erobert und seine Armee wurde immer größer und stärker.\n
Als er auf dem Planeten Auria landete, war er überrascht von der Freundlichkeit und Hilfsbereitschaft der Bewohner. Sie boten ihm sogar Unterkunft und Nahrung an, obwohl sie wussten, dass er ein Bösewicht war.\n
{Name_Held}'s Herz wurde von dieser Güte berührt und er begann, an seinen Zielen zu zweifeln. Er beschloss, die Bewohner des Planeten zu schonen und sie nicht anzugreifen.\n
Aber seine Armee war anderer Meinung und sie griffen den Planeten an, ohne {Name_Held}'s Wissen. Er war entsetzt von dem Blutvergießen und beschloss, seine Armee zu verlassen und sich der Gerechtigkeit anzuschließen, um sich für seine Fehler zu entschuldigen und das Unrecht, das er angerichtet hatte, wieder gutzumachen.\n
Er reiste zu den anderen Planeten, die er erobert hatte, und half beim Wiederaufbau und der Versöhnung zwischen den ehemaligen Feinden. Er wurde zum Helden, der die Galaxie zusammengeführt hatte und Frieden gebracht hatte.\n
Die Bewohner des Planeten Auria, die er einst bedroht hatte, nahmen ihn auf und betrachteten ihn als einen von ihnen. Er lebte unter ihnen und half beim Wiederaufbau ihrer Welt. Er hatte seinen Frieden gefunden und seine Seele war endlich ruhig.
"""
        )





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



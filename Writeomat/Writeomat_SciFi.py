# -*- coding: utf-8 -*-

import Writeomat


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


Name_Held = input("Wähle den Namen deines Protagonisten \n-->")

SciFi_Geschichte_1 = Writeomat.Geschichte("Wähle den Helden deiner Geschichte ",
                                "a) Super Held \nb) Bösewicht",
                                f"Es war einmal in einer fernen Galaxie ein Held {Name_Held}. Dieser ",
                                f"Es war einmal in einer fernen Galaxie ein Bösewicht namens {Name_Held} the destroyer. Dieser ")

SciFi_Geschichte_2 = Writeomat.Geschichte("An welchem Ort willst du starten",
                                "a) Raumschiff \nb) Planet Auria",
                                "Er war in seinem riesen Raumschiff mit dem er durch die Galaxie reiste. ",
                                "Er landete auf dem Planeten Auria, welcher bekannt für seine freundlichen Bewohner ist. ")

SciFi_Geschichte_3 = Writeomat.Geschichte("Welches Ende soll die Geschichte haben?",
                                "a) Gutes Ende \nb) Schlechtes Ende",
                                f"Nach vielen Abenteuern und Kämpfen hatte {Name_Held} es endlich geschafft, die Galaxie zu retten und Frieden zu bringen. ",
                                f"Nach vielen Abenteuern und Kämpfen hatte {Name_Held} es endlich geschafft, die Galaxie zu unterwerfen und seine Macht zu festigen. ")

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

if SciFi_Geschichte_3:
    print(
f"""
Aber {Name_Held}'s Machtgier war unersättlich und er beschloss, noch mehr Planeten zu erobern und noch mehr Macht zu sammeln.\n
Er begann, seine ehemaligen Verbündeten zu verraten und sie an seine Feinde auszuliefern, um seine eigenen Ziele zu erreichen.\n
Die Bewohner der Galaxie erkannten, dass {Name_Held} sich in einen tyranischen Herrscher verwandelt hatte und beschlossen, gegen ihn zu kämpfen.\n
In einer finalen Schlacht schafften sie es, {Name_Held} zu besiegen und die Galaxie von seiner Tyrannei zu befreien. Aber der Preis war hoch, viele Leben wurden verloren und die Galaxie brauchte lange Zeit um sich von den Wunden zu erholen.\n
Dies ist die Geschichte von {Name_Held}, der es fast geschafft hatte, die Galaxie zu retten, aber letztendlich von seiner Machtgier und Tyrannei zerstört wurde.
"""
        )


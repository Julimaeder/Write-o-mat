# -*- coding: utf-8 -*-
from Writeomat import Geschichte_2, Geschichte_3, Geschichte_4
import random


#if Geschlecht == "M":
Name_Held = input("Wähle den Namen deines Protagonisten \n-->").capitalize()
Name_Gefährte = input("Wähle den Namen deines Gefährten\n-->").capitalize()
Name_Antagonist= input("Wähle den Namen deines Antagonisten\n-->").capitalize()
#elif Geschlecht == "W":
 #   Name_Held = input("Wähle den Namen deiner Protagonistin \n-->")
#else:
  #  print(Geschlecht)
         
  
liste_Geschichte_3 = ["Rentier",  "Frosch", "Nilpferd", "Faultier"]
liste_Geschichte_5 = ["Einem Esel","Einem Skateboard","Ein Fahrrad"]
liste_Geschichte_9 = ["Feuer speienden Drachen", " willkürlichen Riese", "gefährlichen Teufel", "Verzauberte Hexe"]
liste_Geschichte_8 = ["Whisky","Schnaps","Shot","Rum"]


String_Horror_0 =f"{Name_Held} ist in seinem Zimmer im Bett und versuchst zu schlafen. Als {Name_Held} dann eingeschlafen ist beginnt die Reise. {Name_Held} kommt langsam zu sich und merkt dass er wo ganz anders ist und komplett anders aussiehst."

Horror_Geschichte_1 = Geschichte_4("Wähle den Helden deiner Geschichte ",
            "Vampir","Mensch","Magier","edler Ritter",
            f"Er sieht das er starker Vampir ist. ",
            f"Er sieht das er ein anderer Mensch ist",
            f"Er sieht das er ein magischer Magier ist ",
            f"Er sieht das er ein edler Ritter ist")


String_Horror_1 =f" {Name_Held} findet es spannend, er schaut sich langsam um und merkt das er"

Horror_Geschichte_2 = Geschichte_4("An welchem Ort willst du starten",
            "Einem Friedhof", "Ein altes Haus im Wald", "Eine Kirmes", "Ein Schloss",
            f"auf einem gruseligem Friedhof ist.",
            f"in einem altem Haus mitten im Wald ist.",
            f"auf einer riesen verlassenen Kirmes ist.",
            f"in einem spuck Schloss ist.")



String_Horror_2 = f" Plötzlich steht neben {Name_Held} ein Tier namens {Name_Gefährte}, dass behauptet sein Gefährte auf seiner Reise zu sein"


Horror_Geschichte_3 = Geschichte_4("Wähle deinen Gefährten",
           "Schweinchen", "Hamster", "Kellerassel", "Luchs",
            f"Das Tier ist ein Schweinchen",
            f"Das Tier ist ein Hamster",
            f"Das Tier ist eine Kellerassel",
            f"Das Tier ist ein Luchs",
            f"Das Tier ist ein {random.choice(liste_Geschichte_3)}")

String_Horror_3 = f"{Name_Held} und {Name_Gefährte} gehen zusammen los um den Ort zu erkunden. Sie treffen auf einen alten Mann. Der Mann erzählt den beiden das sie"

Horror_Geschichte_4 = Geschichte_4("Was ist seine Mission?",
           "Eine Prinzessin retten","der beste werden","Menschen schützen","den Antagonisten töten",
            f"eine Prinzessin retten müssen.",
            f"die besten im ganzem Lande werden sollen.",
            f"die Menschen in der naheligenden stadt retten müssen.",
            f"den Antagonisten töten sollen um die Welt zu retten.")

String_Horror_4 = f" Er stellt Ihnen auch ein Gefährt, damit sie so schnell wie möglich voran kommen. "

Horror_Geschichte_5 = Geschichte_3("Was ist das Gefährt des Helden?",
            "Ein Ross","Eine Kutsche","Dein Gefährte",
            f"Er schenkt Ihnen ein edles Ross",
            f"Er schenkt Ihnen eine pompöse Kutsche",
            f"Doch dann fällt ihm ein,dass sein Gefährte der schnellste ist und sagt,dass er auf Ihm reiten soll",
            f"Er schenkt Ihnen ein {random.choice(liste_Geschichte_5)}")

String_Horror_5 =f"Sie sind fast am Zielort angekommen. Sie sehen allerdings etwas in einer Ecke hinter einer Kiste schimmern. Sie gehen langsam dorthin und finden"

Horror_Geschichte_6 = Geschichte_3("Wähle deine verzauberte Waffe",
           "Schwert", "Axt", "Speer",
            f"Ein verzaubertes Schwert",
            f"Eine riesige Axt",
            f"Ein langes Speer")
           

String_Horror_6 =f" Plötzlich erinnert er sich, dass er eine Geheimfähigkeit besitzt. Diese  Geheimfähigkeit ist"

Horror_Geschichte_7 = Geschichte_3("Was ist die Geheimfähigkeit",
             "Unsichtbarkeit","Schnelligkeit","Sprungkraft",
             f"sich Unsichtbar zu machen",
             f"sich sehr schnell zu bewegen und zu laufen",
             f"eine sehr hohe Sprungkraft zu haben")
            

String_Horror_7 =f" Neben seiner Waffe ist ein Getränk womit er eine Geheimfähigkeit erlernen kann. Er guckt es sich genauer an und siehst das es ein"

Horror_Geschichte_8 = Geschichte_4("Was soll er trinken um die Geheimfähigkeit zu starten",
             "Bier","Sekt","Wein","Gin",
             f"ein Bier ist",
             f"ein Sekt ist",
             f"ein Wein ist",
             f"einen Gin ist",
             f"ein {random.choice(liste_Geschichte_8)}ist")

String_Horror_8 =f" Er fragt sich aber langsam wer der Antagonist ist den er bekämpfen soll. {Name_Gefährte} erzählt {Name_Held}  das er {Name_Antagonist} heißt und ein"


Horror_Geschichte_9 = Geschichte_4("Wähle den Antagonisten deiner Geschichte",
           "Ein Clown"," Ein Zombie"," Ein Werwolf","Ein Geist",
            f"blutrünstiger Clown ist",
            f"ein flinker Zombie ist",
            f"ein haariger Werwolf ist",
            f"ein lästiger Geist ist",
            f"ein {random.choice(liste_Geschichte_9)}ist")

String_Horror_9 =f" Nach ein paar Tagen trifft er schließlich auf den {Name_Antagonist}.Es ist ein hitziges Duell und beide kämpfen Tapfer."

Horror_Geschichte_10 = Geschichte_2("Wie soll das Ende ausgehen?",
            "Der Held Gewinnt","Der Bösewicht gewinnt",
            f"In einem entscheidenden Moment erinnert er sich jedoch an seine Geheimfähigkeit. Er trinkt das Getränk und aktiviert seine besondere Fähigkeit. Damit bringt er Ihn letztendlich zu Fall. Nach dem Kampf lebten sie fortan glücklich und in Frieden, dank ihrer Tapferkeit und ihres Zusammenhalts.",
            f"Trotz all seiner Kraft und Tapferkeit konnte {Name_Held} den {Name_Antagonist} nicht besiegen. Mit einem letzten, verzweifelten Angriff wurde er von dessen Macht überwältigt und sank zu Boden. Der {Name_Antagonist} lachte hämisch, als er seinen Sieg feierte und das Land weiter unter seiner Tyrannei leiden musste."
            f"")

String_Horror_10 = "Auf einmal wacht er wieder auf und merkt, dass alles nur ein Traum war."                  


def Titelblatt(Horror_Geschichte_1):
    if "Vampir" in Horror_Geschichte_1:
        return(
        """   
\n                                                                                            
                    ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                            
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                       
           ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                    
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(                 
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                
       /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                
       /@@@@@@@@@@@@@@..............%..............@@@@@@@@@@@@@@                
       .@@@@@@@@@@@...................................@@@@@@@@@@@                
        @@@@@@@@@.......................................@@@@@@@@@                
        @@@@@@@@@.......................................@@@@@@@@@                
        @@@@@@@@....@@@@@@@@.................@@@@@@@@....@@@@@@@@                
        @@@@@@@...........................................@@@@@@@                
        .@@@@@@...@@@@.  (@@................*@@*  ,@@@@...@@@@@@                 
     @,.....@@@.%@@ @@@@@@@@@@.............@@@@@@@@@@ @@..@@@.....&*             
      @..***@.&.@@ @@@@@@@@@@@.............@@@@@@@@@@@ @@,#(#**,..@              
     .@@...**@...@ .@@@@@@@@@ .............(@@@@@@@@@  @...@**...@@              
    @%%%#@...*@....@ .@@@@@........&,........(@@@@@  @....@....@%%%%@            
   @%%%%%%%%%%%@..*/*///........../###,&.........////*,.*@%%%%%%%%%%%@           
  @%%%%%%%%%%%%%#@@.,,.............................,..@&#%%%%%%%%%%%%#@          
 @%%%%%%%%%%%%%%#%%%%%@@*.......................#@@%%%%%#%%%%%%%%%%%%%%@         
./               .%@@@@@&%%%%, .,,,,*,,,,. (%%%%&@@@@@(.              .(         
                             @@@ %%..,%% @@@         

\n\n
"""
               )
    elif "Mensch" in Horror_Geschichte_1 :
        return(
        """
\n
                                                                                
                            .@@@@@@@@@@@@@@@@@@@@@@@@/                           
                       ,@@@                           @@@@                      
                    @@@                                   %@@&                  
                 @@@                                         %@@                
               @@                                               @@.             
             @@                                                   @@            
            @%                                                     @@           
           @&                                                       @@          
          @@                                                        .@@         
          @@                                                         @@         
          @@                                                         @@         
          @@   @                                                 @   @@         
          @@   %     @&%    ,@@@@#@#         @@@@@@@     @@@     #  @@&         
           @@  &   @             .                           @   @  @@          
        @@@@@  .      /,@@@@@&@ @         @  @ @.*@@@&@@ @       &  @@@@        
        @@  @ @     & @  @   @   .            @ @ @    @  @        @&  @@       
        @  & &@                                                   @@ @ @@       
          *#@@.                          %  &                     @ @@ @        
         @@ @@                        @  %  @                     @&  @@        
          @@ @@                    @      & @                     & . #         
           @ #@                   @          ,                    @ &           
            ( @@                  @ #@@@@#@@@ @                  @@@            
             #&@@                     @@@@  *                   @@ /            
              @@@                                              @@.@             
                &@                 @@@@  @@@@                  @@               
                 @             %@&@@@@@  @@@@@@@&@            @@                
                 &@                                          (@                 
                   @                (@&@@@@@                @@                  
                    @@                                    (@@                   
                     @@@(                               @@@@                    
                      @@#&@@                         @@@  @@                    
                      @@   #@@@                  @@@@     #                     
                      @@     @  @@@          @@@   @     *@                     
                      @@                                 @@                     
                      @@(     &                   (      @@                     
                      @&@                                @@                     
                     @& @                                @&@                    
                    @#  @                                   @@                  
                 &@     %                               %    .@@                
             &@@ @                                      @      @&@@             
        ,#@%     @@                                           @@     %@@        
  *@/              @@                                       #@                  
                      &@@                                @@                     
                            @@&@@                 @@@@,   
  

\n\n
"""
               )
    elif "Magier" in Horror_Geschichte_1:
        return(
        """
\n
                                                                                
                                              #&&                               
                                         &&&&%&&&                               
                                      *&&& %&&&                         %&&&&&  
                                     &&%  .&&.                          &//%&&  
                                    %&      &&%                           &%    
                               &&&&&          #%%&&%                     %&&    
                            ,%&&                  (%%%                   &&     
                          %&&&&&&&&#          &&&&&&&&&&                 &&     
                                 &&           &&&                        &&     
     %%&&  &&&&&&&               &&&          &&               *&&&&&&. (&&     
    &&  *&&&%     &&&&&&         *%&&       (&&&&(       *%&&&&%    *&& %&      
   /%&%  &&,            %%&&&%&%/  &&       &&&  .&&&&&&%%          &&& &&      
      &&&&                         &&(      &&                      &&. &%      
      .&&                    %&&    &&     &&%   %%&&               && /&&      
      &&&&&&&&&&&&&&&&&&&&&&%  &&   &/%   ,&%    && #%&&&&&&&&&&&&&&&& &&.      
                              &&.    *## ./#     %&&                   &%       
                              &&      (&&&&      .%%                   &&       
                             &&&                  &&                  *&&       
                             &&                   &&&                 &&,       
                             &&                   (&&                 &&        
                            &&%                    %&                           
                            &&/                    &&/                          
                            &&                     %&&                          
                           #&%                      &&                          
                           %&%                      %&.                         
                           &&                       %&%                         
                          ,&&                        &&                         
                          &&&&&&&&&&&&&&&&&&&&&&&&&&&&&                         
                          %%                         &&&                        
                          &&                          &&                        
                          &&&&&&&&&&&&&&&&&&&&&&&&&&&&&%                        
                                         

\n\n
"""
               )
    elif "edler Ritter" in Horror_Geschichte_1:
        return(
        """
\n
                                                /&@/                            
                              @@@@@@@@@@@@@@@@@@@@@@@@@@@%                      
                                  @@@@@@@@@@@@@@@@@@@@@@@@@@                    
                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                   
                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                  
                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
               @@@@@@@@@@@@@@@@@@@@.     &@@@@@@@@@@@@@@@@@@@@#                 
              @@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@                  
              @@@@@@@@@@@@@&        @@@@@    @@@@@@@@@@@@@@@@                   
              @@@@@@@@@@@              @@               *@@                     
              @@@@@@@@@@@@@@@@@@@@         /@@@@@@@@@                           
              @@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@                   
              @@@@@@@@@@@@@@    .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@               
               @@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@            
               @@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
                @@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,                  
                @@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@(           @   @@@@@       
                @@@@@@/  ,@@@@@@@@@@@@@& @@@@          @@@@  %@@@@   @@@@@      
                @@@@@@   @@@@@@@@@@@@@@  @@@@   @@@@,  @@@@@  @@@@@   @@@@      
                @@@@@@   ,@@@@@@@@@@@@@@@@@@     @@@   @@@@@   @@@@,   @@@@     
      @       .@@@@@@@@   @@@@@@@@@@@@@@@@@@@@@       @@@@@   @@@@@   @@@@@     
      @@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@    @@@@@@@      .   @@@@@   @@@@@      
       @@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@     @@@@@@@@       @@   @@@@@        
        .@@@@@@@@@@@@@@@@    *@@@@@@@@@@@@@@@@     @@@@@@@@@@                   
           @@@@@@@@@@@&        @@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@           
                                @@@@@@@@@@@@@@@@@@@@@      @@@@@@@@             
                                @@@@@@@@@@@@@@@@@@@@@@@@@       &@@             
                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                  
                                @@@@@@@@@@@@@@@@@@@@@@@@@                       
                                 @@@@@@@@@@@@@@@@@@@@@@@                        
                               /             @@@@@@@@@@@@                       
                              @@@@@@@@@@@@@&             @@                     
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@                        
                               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                  
                                               *@@@@@@@@@@@@@@@    
                                               
\n\n
"""
               )
    else:
        return (f"FEHLER! Horror_Geschichte_1 = {Horror_Geschichte_1}")




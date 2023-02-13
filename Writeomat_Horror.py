# -*- coding: utf-8 -*-
from Writeomat import Geschichte_4, Geschichte_3, Geschichte_2
import random


#if Geschlecht == "M":
Name_Held = input("Wähle den Namen deines Protagonisten \n-->").capitalize()
Name_Gefährte = input("Wähle den Namen deines Gefährten\n-->").capitalize()
Name_Antagonist= input("Wähle den Namen deines Antagonisten\n-->").capitalize()
#elif Geschlecht == "W":
 #   Name_Held = input("Wähle den Namen deiner Protagonistin \n-->")
#else:
  #  print(Geschlecht)

liste_Geschichte_2 = ["Kücken ","Frosch", "Nilpferd", "Faultier"]
liste_Geschichte_4 = ["Feuer speienden Drachen", " willkürlichen Riese", "gefährlichen Teufel", "Verzauberte Hexe"]
liste_Geschichte_7 = ["Einem Esel","Einem Skateboard","Ein Fahrrad"]
liste_Geschichte_9 = ["Whisky","Schnaps","Shot","Rum"]


Horror_Geschichte_1 = Geschichte_4("Wähle den Helden deiner Geschichte ",
            "Ein Vampir","Ein Mensch","Ein Magier","Ein edler Ritter",
            f"Eines Tages kam ein Vampir  {Name_Held}. Dieser ",
            f"Eines Tages kan ein Mensch {Name_Held}. Dieser ",
            f"Eines Tages kam ein Magier {Name_Held}. Dieser ",
            f"Eines Tages kam ein edler Ritter {Name_Held}. Dieser ")



Horror_Geschichte_2 = Geschichte_4("Wähle deinen Gefährten",
           "Schweinchen", "Hamster", "Kellerassel", "Luchs",
           f"ist Der Gefährte von {Name_Held} ",
           f"ist Der Gefährte von {Name_Held} ",
           f"ist Der Gefährte von {Name_Held}",
           f"ist Der Gefährte von {Name_Held}",
           f"ist Der Gefährte von {random.choice(liste_Geschichte_2)} sie" )


Horror_Geschichte_3 = Geschichte_3("Wähle deine verzauberte Waffe",
           "Schwert", "Axt", "Speer",
           f"Seine verzauberte Waffe ist das Schwert",
           f"Seine verzauberte Waffe ist die Axt",
           f"Seine verzauberte Waffe ist der Speer")

Horror_Geschichte_4 = Geschichte_3("Was ist die Geheimfähigkeit",
             "Unsichtbarkeit","Schnelligkeit","Sprungkraft",
             f"{Name_Held} kann sich durch seine Geheimfähigkeit Unsichtbar machen",
             f"{Name_Held} kann durch seine Geheimfähigkeit an schnelligkeit gewinnen ",
             f"{Name_Held} kann durch seine Geheimfähigkeit an Sprungkraft gewinnen")

Horror_Geschichte_5 = Geschichte_4("Was soll er trinken um die Geheimfähigkeit zu starten",
             "Bier","Sekt","Wein","Gin",
             f"{Name_Held} trinkt  ein Bier",
             f"{Name_Held} trinkt  ein Sekt",
             f"{Name_Held} trinkt  ein Wein",
             f"{Name_Held} trinkt  ein Gin",
             f"{Name_Held} trinkt  ein {random.choice(liste_Geschichte_9)}" )

Horror_Geschichte_6 = Geschichte_3("Was ist das Gefährt des Helden?",
            "Ein Ross","Eine Kutsche","Dein Gefährte",
            f"{Name_Held} reitet voller Hochmut ein starkes Ross.",
            f"{Name_Held} fährt lässig in einer Kutsche",
            f"{Name_Held} reitet entspannt auf seinem Gefährten",
            f"{Name_Held} bewegt sich chillig auf {random.choice(liste_Geschichte_7)}fort")


Horror_Geschichte_7 = Geschichte_4("Was ist seine Mission?",
           "Eine Prinzessin retten","der beste werden","Menschen schützen","den Antagonisten töten",
           f"Die Mission von {Name_Held} ist eine Prinzessin zu retten",
           f"Die Mission von {Name_Held} ist der beste zu werden",
           f"Die Mission von {Name_Held} ist die Menschen zu schützen",
           f"Die Mission von {Name_Held} ist den Antagonisten zu töten")


Horror_Geschichte_8 = Geschichte_4("Wähle den Antagonisten deiner Geschichte",
           "Ein Clown"," Ein Zombie"," Ein Werwolf","Ein Geist",
           f"begegneten {Name_Held} eines Tages einem bösen Clown. Dieser ",
           f"begegneten {Name_Held} eines Tages einem gefährlichen Zombie. Dieser ",
           f"begegneten {Name_Held} eines Tages einem blutrünstigen Werwolf. Dieser ",
           f"begegneten {Name_Held} eines Tages einem gruseligen Geist. Dieser ",
           f"begegneten {Name_Held} eines Tages einem {random.choice(liste_Geschichte_4)}. Dieser" )



Horror_Geschichte_9 = Geschichte_3("Wie soll das Ende ausgehen?",
            "Der Held besiegt den Antagonisten","Der Antanogist tötet den Held",
             f"{Name_Held} besiegt {Name_Antagonist} ",
             f"{Name_Antagonist}  besiegt {Name_Held}  ",
             f"{Name_Held} und {Name_Antagonist} sterben beide")


Horror_Geschichte_10 = Geschichte_4("An welchem Ort willst du starten",
           "Einem Friedhof", "Ein altes Haus im Wald", "Eine Kirmes", "Ein Schloss",
           "Wacht auf einem Friedhof auf. ",
           "Wacht in einem alten Haus am Waldrand auf. ",
           "Wacht auf einer Kirmes auf. ",
           "Wacht in einem Schloss auf. ")
             
           


# Vorerst nicht appenden, soll am Anfang ausgewählt, und später genutzt werden
if Horror_Geschichte_3 != "d":
    Name_Gegner = input("\nWähle den Namen deines Antagonisten \n-->").capitalize()
else: 
    Name_Gegner = ("")
              
Horror_Geschichte_Text_1 = ""


def Titelblatt(Horror_Geschichte_1):
    if "Vampir" in Horror_Geschichte_1:
        return(
        """     
                                                                                                 
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
                             

        """
               )
    elif "Mensch" in Horror_Geschichte_1:
        return(
        """
                                                                                
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
  
  
        """
               )
    elif "Magier" in Horror_Geschichte_1:
        return(
        """
                                                                                
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
                                         

        """
               )
    elif "Ritter" in Horror_Geschichte_1:
        return(
        """

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
                                               

        """
               )
    else:
        return (f"FEHLER! Horror_Geschichte_1 = {Horror_Geschichte_1}")

   
# -*- coding: utf-8 -*-

from Writeomat import Geschichte_4, Geschichte_3, Geschichte_2
#if Geschlecht == "M":    
#Name_Held = input("Wähle den Namen deines Protagonisten \n-->")
#Name_Held = input("a")

#if Geschlecht == "M":
Name_Held = input("Wähle den Namen deines Protagonisten \n-->").capitalize()
#elif Geschlecht == "W":
 #   Name_Held = input("Wähle den Namen deiner Protagonistin \n-->")
#else:
  #  print(Geschlecht)

Horror_Geschichte_1 = Geschichte_4("Wähle den Helden deiner Geschichte ",
            "Ein Clown","Ein Zombie","Ein Werwolf","Ein Geist",
            f"Eines Tages kam ein Clown  {Name_Held}. Dieser ",
            f"Eines Tages kan ein Zombie {Name_Held}. Dieser ",
            f"Eines Tages kam ein Werwolf {Name_Held}. Dieser ",
            f"Eines Tages kam ein Geist {Name_Held}. Dieser ")

Horror_Geschichte_2 = Geschichte_4("An welchem Ort willst du starten",
           "Einem Friedhof", "Ein altes Haus im Wald", "Eine Kirmes", "Ein Schloss",
           "Wacht auf einem Friedhof auf. ",
           "Wacht in einem alten Haus am Waldrand auf. ",
           "Wacht auf einer Kirmes auf. ",
           "Wacht in einem Schloss auf. ")


Horror_Geschichte_3 = Geschichte_4("Wähle den Antagonisten deiner Geschichte",
          " Ein Clown"," Ein Zombie"," Ein Werwolf","Ein Geist",
           "",
           "",
           "",
           "")    
            # Vorerst nicht appenden, soll am Anfang ausgewählt, und später genutzt werden
Horror_Geschichte_4 = Geschichte_3("Test für 3 Auswahlmöglichkeiten und zum testen kommt hier noch ein längerer Text rein.",
           "Nummero uno","Option 2","Drei",
           "Nummero uno",
           "Option 2",
           "Drei")

Horror_Geschichte_5 = Geschichte_2("Test für zwei Auswahlmöglichkeiten Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magn",
           "Nummero uno","Option 2",
           "Nummero uno",
           "Option 2")

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
            

                  
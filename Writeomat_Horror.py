# -*- coding: utf-8 -*-
from Writeomat import Geschichte_2, Geschichte_3, Geschichte_4

Name_Held = input("Wähle den Namen deines Protagonisten \n-->").capitalize()

Horror_Geschichte_1 = Geschichte_4("Wähle den Helden deiner Geschichte ",
           "a) Ein Vampir \nb) Ein Mensch \nc) Ein Magier \nd) Ein Mächtiger Ritter",
           f"Eines Tages kam ein Clown  {Name_Held}. Dieser ",
           f"Eines Tages kan ein Zombie {Name_Held}. Dieser ",
           f"Eines Tages kam ein Werwolf {Name_Held}. Dieser ",
           f"Eines Tages kam ein Geist {Name_Held}. Dieser ")

Horror_Geschichte_2 = Geschichte_4("An welchem Ort willst du starten",
           "a) Einem Friedhof \nb) Ein altes Haus im Wald \nc) Eine Kirmes \nd) Ein Schloss",
           "Wacht auf einem Friedhof auf. ",
           "Wacht in einem alten Haus am Waldrand auf. ",
           "Wacht auf einer Kirmes auf. ",
           "Wacht in einem Schloss auf. ")

Horror_Geschichte_3 = Geschichte_4("Wähle den Antagonisten deiner Geschichte",
           "a) Ein Clown \nb) Ein Zombie \nc) Ein Werwolf \nd) Ein Geist",
           "",
           "",
           "",
           "")    

if Horror_Geschichte_3 != "d":
    Name_Gegner = input("Wähle den Namen deines Antagonisten \n-->").capitalize()
else: 
    Name_Gegner = ("")
    
def Titelblatt(Horror_Geschichte_1):
    if "Vampir" in Horror_Geschichte_1:
        return(
        """                                                                                                      

        """
               )
    elif "Mensch" in Horror_Geschichte_1:
        return(
        """

        """
               )
    elif "Magier" in Horror_Geschichte_1:
        return(
        """

        """
               )
    elif "Ritter" in Horror_Geschichte_1:
        return(
        """
                     
        """
               )
    else:
        return (f"FEHLER! Horror_Geschichte_1 = {Horror_Geschichte_1}")
    
            

                  
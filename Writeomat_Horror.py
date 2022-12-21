# -*- coding: utf-8 -*-



from Writeomat import Geschichte
Name_Held = input("Wähle den Namen deines Protagonisten \n-->")

Horror_Geschichte_1 = Geschichte("Wähle den Helden deiner Geschichte ",
           "a) Ein Vampir \nb) Ein Mensch \nc) Ein Magier \nd) Ein Mächtiger Ritter",
           f"Eines Tages kam ein Clown  {Name_Held}. Dieser ",
           f"Eines Tages kan ein Zombie {Name_Held}. Dieser ",
           f"Eines Tages kam ein Werwolf {Name_Held}. Dieser ",
           f"Eines Tages kam ein Geist {Name_Held}. Dieser ")

Horror_Geschichte_2 = Geschichte("An welchem Ort willst du starten",
           "a) Einem Friedhof \nb) Ein altes Haus im Wald \nc) Eine Kirmes \nd) Ein Schloss",
           "Wacht auf einem Friedhof auf. ",
           "Wacht in einem alten Haus am Waldrand auf. ",
           "Wacht auf einer Kirmes auf. ",
           "Wacht in einem Schloss auf. ")

Horror_Geschichte_3 = Geschichte("Wähle den Antagonisten deiner Geschichte",
           "a) Ein Clown \nb) Ein Zombie \nc) Ein Werwolf \nd) Ein Geist",
           "",
           "",
           "",
           "")    
            # Vorerst nicht appenden, soll am Anfang ausgewählt, und später genutzt werden
if Horror_Geschichte_3 != "d":
    Name_Gegner = input("Wähle den Namen deines Antagonisten \n-->")
else: 
    Name_Gegner = ("")
    
            

                  
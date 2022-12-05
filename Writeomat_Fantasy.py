from Writeomat import Geschichte
from Writeomat import Liste_Geschichte
Name_Held = input("Wähle den Namen deines Protagonisten \n-->")

Fantasy_Geschichte_1 = Geschichte("Wähle den Helden deiner Geschichte ",
           "a) Eine gute Fee \nb) Ein Oger \nc) Ein Magier \nd) Ein Zwerg",
           f"Es war einmal eine gute Fee namens {Name_Held}. Diese ",
           f"Es war einmal ein Oger namens {Name_Held}. Dieser ",
           f"Es war einmal ein Magier namens {Name_Held}. Dieser ",
           f"Es war einmal ein kleiner Zwerg namens {Name_Held}. Dieser ",
           Liste_Geschichte)    # Ist Liste_Geschichte wirklich notwendig?

Fantasy_Geschichte_2 = Geschichte("Welches Gefährt hat dein Held",
           "a) Ein Pferd \nb) Ein Riese \nc) Eine Kutsche \nd) Zu Fuß",
           "reitet voller Hochmut ein starkes Ross. ",
           "sitzt auf dem Rücken eines stolzen Riesen. ",
           "fährt in einer Kutsche dem Horizont entgegen. ",
           "schreitet tapfer zu fuße voran. ",
           Liste_Geschichte)

Fantasy_Geschichte_3 = Geschichte("Wähle den Antagonisten deiner Geschichte",
           "a) Ein dunkler Magier \nb) Ein Drache \nc) Eine Truppe Orks \nd) kein Antagonist",
           "",
           "",
           "",
           "",
           Liste_Geschichte)    
            # Vorerst nicht appenden, soll am Anfang ausgewählt, und später genutzt werden
            
Fantasy_Geschichte_Text_1 = ""



'''
Todo:
    - Name_Gegner hinzufügen
Ideen: 
    - Einen Begleiter optional mitnehmen 
    - Zufallsevent
'''

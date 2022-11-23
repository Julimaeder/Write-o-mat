    
name = input("Name des Autors -->")
Liste_Geschichte = []
Name_Held = input("Wähle den Namen deines Heldens \n-->")

def Geschichte(intro,opts, opt1, opt2, opt3, opt4):
    print(intro)
    aktion = ""
    while aktion != "a" or aktion != "b" or aktion != "c" or aktion != "d":
        print(opts)
        aktion = input("-->")
        if aktion == "a": 
            Liste_Geschichte.append(opt1)
            return aktion
        elif aktion == "b":
            Liste_Geschichte.append(opt2)
            return aktion
        elif aktion == "c":
            Liste_Geschichte.append(opt3)
            return aktion
        elif aktion == "d":
            Liste_Geschichte.append(opt4)
            return aktion
        else:
            print("a, b, c oder d ?")


Geschichte_1 = Geschichte("Wähle den Helden deiner Geschichte ",
           "a) Eine gute Fee \nb) Ein Oger \nc) Ein Magier \nd) Ein Zwerg",
           f"Es war einmal eine gute Fee namens {Name_Held}. Diese ",
           f"Es war einmal ein Oger namens {Name_Held}. Dieser ",
           f"Es war einmal ein Magier namens {Name_Held}. Dieser ",
           f"Es war einmal ein kleiner Zwerg namens {Name_Held}. Dieser ")

Geschichte_2 = Geschichte("Welches Gefährt hat dein Held",
           "a) Ein Pferd \nb) Ein Riese \nc) Ein Dreirad \nd) Zu Fuß",
           "reitet voller Hochmut ein starkes Ross ",
           "sitzt auf dem Rücken eines stolzen Riesen ",
           "fährt voller Stolz ein Renn-Dreirad  ",
           "schreitet tapfer zu fuße voran ")

#Geschichte in eine txt Datei schreiben
output = open(f"{name}'s Geschichte.txt", "w")
output.write(str(Liste_Geschichte))
output.close()

#Ausgabe in der Konsole:
filename = f"{name}'s Geschichte.txt"
with open(filename, "r") as file: #r für read und utf-8 ist das Format zum auslesen (deswegen kommen manchmal bei äöü komische Zeichen)
    for line in file:               #, encoding="utf-8"
        print(line)


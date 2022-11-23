name = input("Name des Autors -->")
Liste_Geschichte = []

def Geschichte01():
    print("Wähle den Helden deiner Geschichte ")
    aktion = ""
    while aktion != "a" or aktion != "b" or aktion != "c" or aktion != "d":
        print("a) Eine gute Fee \nb) Ein Oger \nc) Ein Magier \nd) Ein Zwerg")
        aktion = input("-->")
        if aktion == "a": 
            Liste_Geschichte.append("Es war einmal eine gute Fee. Diese ")
            return aktion
        elif aktion == "b":
            Liste_Geschichte.append("Es war einmal ein Oger. Dieser ")
            return aktion
        elif aktion == "c":
            Liste_Geschichte.append("Es war einmal ein Magier. Dieser ")
            return aktion
        elif aktion == "d":
            Liste_Geschichte.append("Es war einmal ein kleiner Zwerg. Dieser ")
            return aktion
        else:
            print("a, b, c oder d ?")
def Geschichte02():
    print("Welches Gefährt hat dein Held")
    aktion2 = ""
    while aktion2 != "a" or aktion2 != "b" or aktion2 != "c" or aktion2 != "d":
        print("a) Ein Pferd \nb) Ein Riese \nc) Ein Dreirad \nd) Zu Fuß")
        aktion2 = input("-->")
        if aktion2 == "a": 
            Liste_Geschichte.append("reitet voller Hochmut ein starkes Ross ")
            return aktion2
        elif aktion2 == "b":
            Liste_Geschichte.append("sitzt auf dem Rücken eines stolzen Riesen ")
            return aktion2
        elif aktion2 == "c":
            Liste_Geschichte.append("fährt voller Stolz ein Renn-Dreirad  ")
            return aktion2
        elif aktion2 == "d":
            Liste_Geschichte.append("schreitet tapfer zu fuße voran ")
            return aktion2
        else:       
            print("a, b, c oder d ?")
            
def Geschichte03():
     print("")

     
x = Geschichte01()
Geschichte02()
Geschichte03()
output = open(f"{name}'s Geschichte.txt", "w")
text = (Liste_Geschichte)
output.write(str(text))
output.close()

filename = f"{name}'s Geschichte.txt"

with open(filename, "r") as file:
    while "[" in file:
        print("hallo")

with open(filename, "r") as file: #r für read und utf-8 ist das Format zum auslesen (deswegen kommen manchmal bei äöü komische Zeichen)
    for line in file:               #, encoding="utf-8"
        print(line)

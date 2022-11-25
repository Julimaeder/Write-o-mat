#import Writeomat_Horror
#import Writeomat_Fantasy
#import Writeomat_SciFi

Liste_Geschichte = []
def main():
    name = input("Name des Autors -->")     # Wird in bei der Benennung der Textdatei benutzt 
    Genre = input("Wähle das Genre deiner Geschichte: \na) Horror \nb) Fantasy \nc) Science-Fiction \n-->")
    #while Genre != ("b"):     # Um andere Eingaben zu vermeiden
     #   Genre = input("a, b oder c?\n-->")
    
    
    if Genre == "a":
        import Writeomat_Horror
        Liste_Geschichte.append(Writeomat_Horror.Horror_Geschichte_1)
        Liste_Geschichte.append(Writeomat_Horror.Horror_Geschichte_2)
    elif Genre == "b":
        import Writeomat_Fantasy
        Liste_Geschichte.append(Writeomat_Fantasy.Fantasy_Geschichte_1)
        Liste_Geschichte.append(Writeomat_Fantasy.Fantasy_Geschichte_2)
    else:
        import Writeomat_SciFi
        Liste_Geschichte.append(Writeomat_SciFi.SciFi_Geschichte_1)

    
    #Geschichte in eine txt Datei schreiben
    output = open(f"{name}'s Geschichte.txt", "w", encoding="utf-8")
    output.write(str(Liste_Geschichte))
    output.close()
    
    #Ausgabe in der Konsole:
    filename = f"{name}'s Geschichte.txt"
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line)
    

if __name__ == "__main__":
    main()
else:
    Name_Held = input("Wähle den Namen deines Heldens \n-->")
 
    def Geschichte(intro,opts, opt1, opt2, opt3, opt4, Liste_Geschichte): 
        print(intro)
        aktion = ""
        while aktion != "a" or aktion != "b" or aktion != "c" or aktion != "d":
            print(opts)
            aktion = input("-->")
            if aktion == "a": 
            #    Liste_Geschichte.append(opt1)
                return opt1
            elif aktion == "b":
            #    Liste_Geschichte.append(opt2)
                return opt2
            elif aktion == "c":
            #    Liste_Geschichte.append(opt3)
                return opt3
            elif aktion == "d":
            #    Liste_Geschichte.append(opt4)
                return opt4
            else:
                print("a, b, c oder d ?")
                
"""            
Probleme: 
   Huber fragen  - ist das Reloaded modules wirklich kein Problem? / ist es vermeidbar
                 
    - Name deines Heldens wird teilweise zu Beginn erfragt
    - nach Abbrechen wird direkt nach dem Helden der Geschichte gefragt (bei Fantasy)
    - code unübersichtlich
        - Kann man die Imports auch nach oben schreiben? -geht gerade nicht,
          da die ausgeführt werden bevor Geschichte definiert ist
        - else umgehen bei name = main
     
Notizen:
    Reloaded modules:<module_name> ist nur eine Warnung von Spyder, ist nicht wichtig und kann in den Einstellungen ausgestellt werden
"""
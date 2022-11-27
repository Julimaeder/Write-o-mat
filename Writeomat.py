#import Writeomat_Horror
#import Writeomat_Fantasy
#import Writeomat_SciFi

Liste_Geschichte = []
def main():
    name = input("Name des Autors -->")     # Wird in bei der Benennung der Textdatei benutzt 
    
    #Die Geschichten werden im Maskulinum erzählt und später ggf. mit regex verändert 
    Geschlecht = input("Wähle das Geschleicht deines Protagonisten/ deiner Protagonistin (m/w) \n-->").upper()
    while Geschlecht != "M" and Geschlecht != "W":     # Um andere Eingaben zu vermeiden
        Geschlecht = input("M/W?\n-->").upper()    
        
    Genre = input("Wähle das Genre deiner Geschichte: \na) Horror \nb) Fantasy \nc) Science-Fiction \n-->")
    while Genre != "a" and Genre != "b" and Genre != "c":     # Um andere Eingaben zu vermeiden
        Genre = input("a, b oder c?\n-->")
    
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
    output.write(str("".join(Liste_Geschichte))) # "".join(Liste) ist eien Funktion um die Liste ohne Sonderzeichen zu speichern; in den "" steht wodurch die Elemente getrennt werden
    output.close()
    if Geschlecht == "W":       #!!!
        pass    #Regex zum Verändern des Geschlechts
  
    #Ausgabe in der Konsole:
    filename = f"{name}'s Geschichte.txt"
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line)


if __name__ == "__main__":
    main()
else:
   # if Geschlecht == "M":      #!!!
    Name_Held = input("Wähle den Namen deines Protagonisten \n-->")
    #else:
     #   Name_Held = input("Wähle den Namen deiner Protagonistin \n-->")
 
    def Geschichte(intro,opts, opt1, opt2, opt3, opt4, Liste_Geschichte): 
        print(intro)
        aktion = ""
        while aktion != "a" or aktion != "b" or aktion != "c" or aktion != "d":
            print(opts)
            aktion = input("-->")
            if aktion == "a": 
                return opt1
            elif aktion == "b":
                return opt2
            elif aktion == "c":
                return opt3
            elif aktion == "d":
                return opt4
            else:
                print("a, b, c oder d ?")
                
"""            
Probleme: 
   Nachfragen:  - ist das Reloaded modules wirklich kein Problem? / ist es vermeidbar
                 
    - Name deines Heldens wird teilweise zu Beginn erfragt
  ? - nach Abbrechen wird direkt nach dem Helden der Geschichte gefragt (bei Fantasy)
    - code unübersichtlich
        - Kann man die Imports auch nach oben schreiben? -geht gerade nicht,
          da die ausgeführt werden bevor Geschichte definiert ist
        - else umgehen bei name = main
    - Name_Held je nach Geschlecht anpassen
     
Notizen:
    Wichtige Sachen im Code mit #!!! markieren
    Reloaded modules:<module_name> ist nur eine Warnung von Spyder, ist nicht wichtig und kann in den Einstellungen ausgestellt werden
"""
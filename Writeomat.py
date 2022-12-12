# -*- coding: utf-8 -*-

#import Writeomat_Horror
#import Writeomat_Fantasy
#import Writeomat_SciFi
import pyfiglet


def Geschichte(intro,opts, opt1, opt2, opt3, opt4): 
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
            
Liste_Geschichte = []

def main():  #Alles, was nicht beim Importieren dieser Datei ausgeführt werden soll
    writeomattext = """
__        __         _   _                                                        _   
\ \      / /  _ __  (_) | |_    ___            ___            _ __ ___     __ _  | |_ 
 \ \ /\ / /  | '__| | | | __|  / _ \  _____   / _ \   _____  | '_ ` _ \   / _` | | __|
  \ V  V /   | |    | | | |_  |  __/ |_____| | (_) | |_____| | | | | | | | (_| | | |_ 
   \_/\_/    |_|    |_|  \__|  \___|          \___/          |_| |_| |_|  \__,_|  \__|
                                                                                      
    """
    print(writeomattext)
    name = input("Name des Autors -->")     # Wird in bei der Benennung der Textdatei benutzt 
    Titel = pyfiglet.figlet_format(input("Titel: \n-->"))
    
    #Die Geschichten werden im Maskulinum erzählt und später ggf. mit regex verändert 
    Geschlecht = input("Wähle das Geschleicht deines Protagonisten/ deiner Protagonistin (m/w) \n-->").upper()
    while Geschlecht != "M" and Geschlecht != "W":     # Um andere Eingaben zu vermeiden
        Geschlecht = input("M/W?\n-->").upper()    
        
    Genre = input("Wähle das Genre deiner Geschichte: \na) Horror \nb) Fantasy \nc) Science-Fiction \n-->")
    while Genre != "a" and Genre != "b" and Genre != "c":     # Um andere Eingaben zu vermeiden
        Genre = input("a, b oder c?\n-->")
    
    if Genre == "a":
        import Writeomat_Horror
        Liste_Geschichte.append(Titel)
        Liste_Geschichte.append(Writeomat_Horror.Horror_Geschichte_1)
        Liste_Geschichte.append(Writeomat_Horror.Horror_Geschichte_2)
    elif Genre == "b":
        import Writeomat_Fantasy
        Liste_Geschichte.append(Titel)
        Liste_Geschichte.append(Writeomat_Fantasy.Titelblatt(Writeomat_Fantasy.Fantasy_Geschichte_1))
        Liste_Geschichte.append(Writeomat_Fantasy.Fantasy_Geschichte_1)
        Liste_Geschichte.append(Writeomat_Fantasy.Fantasy_Geschichte_2)
    else:
        import Writeomat_SciFi
        Liste_Geschichte.append(Titel)
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
               
"""            
Probleme: 
    - code unübersichtlich
        - Kann man die Imports auch nach oben schreiben? -geht gerade nicht,
          da die ausgeführt werden bevor Geschichte definiert ist
    - Name_Held je nach Geschlecht anpassen
     
Notizen:
    Wichtige Sachen im Code mit #!!! markieren
    Reloaded modules:<module_name> ist nur eine Warnung von Spyder, ist nicht wichtig und kann in den Einstellungen ausgestellt werden
    pip install pyfiglet
"""
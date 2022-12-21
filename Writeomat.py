# -*- coding: utf-8 -*-
"""
__        __         _   _                                                        _   
\ \      / /  _ __  (_) | |_    ___            ___            _ __ ___     __ _  | |_ 
 \ \ /\ / /  | '__| | | | __|  / _ \  _____   / _ \   _____  | '_ ` _ \   / _` | | __|
  \ V  V /   | |    | | | |_  |  __/ |_____| | (_) | |_____| | | | | | | | (_| | | |_ 
   \_/\_/    |_|    |_|  \__|  \___|          \___/          |_| |_| |_|  \__,_|  \__|
                                                                                      
"""

#Zum Öffnen der Text Datei 
import os 
import pyfiglet # Für die dicke Schrift
import sys #zum Prüfen, welches os man nutzt; anders als "name" aus "os" unterscheidet sys auch zw. Linux und mac
import subprocess #zum öffnen der Datei im Editor für Mac und Linux
#Für Text to speech: 
import pyttsx3

def Geschichte_4(intro,opts, opt1, opt2, opt3, opt4):   # Geschichte mit 4 Auswahlmöglichkeiten
    print(intro)
    aktion = ""
    while aktion != "a" and aktion != "b" and aktion != "c" and aktion != "d":
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
            print("\nUngültige Eingabe. a, b, c oder d ?\n")

def Geschichte_3(intro,opts, opt1, opt2, opt3): # Geschichte mit 3 Auswahlmöglichkeiten
    print(intro)
    aktion = ""
    while aktion != "a" and aktion != "b" and aktion != "c":
        print(opts)
        aktion = input("-->")
        if aktion == "a": 
            return opt1
        elif aktion == "b":
            return opt2
        elif aktion == "c":
            return opt3
        else:
            print("\nUngültige Eingabe. a, b oder c ?\n")
            
def Geschichte_2(intro,opts, opt1, opt2): # Geschichte mit 2 Auswahlmöglichkeiten
    print(intro)
    aktion = ""
    while aktion != "a" and aktion != "b":
        print(opts)
        aktion = input("-->")
        if aktion == "a": 
            return opt1
        elif aktion == "b":
            return opt2
        else:
            print("\nUngültige Eingabe. a oder b ?\n")


Liste_Geschichte = []

def main():  #Alles, was nicht beim Importieren dieser Datei ausgeführt werden soll
    writeomattext = pyfiglet.figlet_format("Write - o - mat") # Write-o-mat in groß zu Beginn ausgeben
    print(writeomattext)
    name = input("Name des Autors -->").capitalize()      # Wird in bei der Benennung der Textdatei benutzt; Erster Buchstabe Groß, Rest klein
    Titel = pyfiglet.figlet_format(input("Titel: \n-->"))
    
    #Für Text to speech  
    engine = pyttsx3.init()   
    schnelligkeit = input("Schnelligkeit: \n -->").upper()
    
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
    if Geschlecht == "W":       
        pass    #Regex zum Verändern des Geschlechts
  
    
#    #Alte Ausgabe in der Konsole:
#    filename = f"{name}'s Geschichte.txt"
#    with open(filename, "r", encoding="utf-8") as file:
#        for line in file:
#            print(line)


    if sys.platform == "win32": # Windows
        os.startfile(f"{name}'s Geschichte.txt")
    elif sys.platform == "darwin": # Mac
        subprocess.call(["open", f"{name}'s Geschichte.txt"])
    else: # Linux
        subprocess.call(["xdg-open", f"{name}'s Geschichte.txt"])
    
    #Sprachausgabe:
    text = " ".join(Liste_Geschichte[2:]) 
    if schnelligkeit == "L":
        engine.setProperty("rate", 150)  
        engine.say(text)  
        engine.runAndWait()
    elif schnelligkeit == "M":
        engine.setProperty("rate", 200)  
        engine.say(text)  
        engine.runAndWait()
    elif schnelligkeit == "S":
        engine.setProperty("rate", 250)  
        engine.say(text)  
        engine.runAndWait()
    else: 
        print("L = Langsam, M= Mittel, S = Schnell")

       
if __name__ == "__main__":
    main()

   

"""                
Probleme: 
    - Name_Held je nach Geschlecht anpassen
    - While schleife um die Geschwindigkeitseingabe bei gtts, damit nur "L", "M" und "S" wählen kann
    - Sprachausgabe optional
     
Notizen:
    Wichtige Sachen im Code mit #!!! markieren
    Reloaded modules:<module_name> ist nur eine Warnung von Spyder, ist nicht wichtig und kann in den Einstellungen ausgestellt werden
"""
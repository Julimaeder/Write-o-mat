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
from gtts import gTTS



def sprachausgabe():
    engine = pyttsx3.init()   
    schnelligkeit = input("Schnelligkeit: \n-->").upper()
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
        
   
def sprachausgabe():
    # Male voice
    tts_male = gTTS("Hallo, ich bin eine deutsche Männerstimme", lang='de', slow=False, voice='m')
    tts_male.save("male_voice.mp3")

    # Female voice
    tts_female = gTTS("Hallo, ich bin eine deutsche weibliche Stimme", lang='de', slow=False, voice='f')
    tts_female.save("female_voice.mp3")        



def clear():
    if sys.platform == "win32" or sys.platform == "darwin": #Windows oder Mac
        clear_command = 'cls'
    else: # Linux
        clear_command = 'clear'
    os.system(clear_command)

def Geschichte_4(intro,opt1, opt2, opt3, opt4, opt1_long, opt2_long, opt3_long, opt4_long):   # Geschichte mit 4 Auswahlmöglichkeiten
#Fragen schoener ausgeben:
#Damit die Fragen einheitlich bleiben wird eine maximale Laenge der Auswahlmoeglichkeiten festgelegt (16) und die Schrift zentriert anstatt, dass die Box erweitert wird.
#Die rechte Border muss ein Zeichen kürzer sein, wenn der Text eine gerade Anzahl an Zeichen hat, daher die Trennung in l und r
    clear()
    print(pyfiglet.figlet_format("Write - o - mat"))
    opt1_borderl = (24 - len(opt1))// 2 * " "
    opt1_borderr = (24 - len(opt1))// 2 * " " if len(opt1) % 2 == 1 else ((24 - len(opt1))// 2 -1) * " "
    opt2_borderl = (24 - len(opt2))// 2 * " "
    opt2_borderr = (24 - len(opt2))// 2 * " " if len(opt2) % 2 == 1 else ((24 - len(opt2))// 2 -1) * " "
    opt3_borderl = (24 - len(opt3))// 2 * " "
    opt3_borderr = (24 - len(opt3))// 2 * " " if len(opt3) % 2 == 1 else ((24 - len(opt3))// 2 -1) * " "
    opt4_borderl = (24 - len(opt4))// 2 * " "
    opt4_borderr = (24 - len(opt4))// 2 * " " if len(opt4) % 2 == 1 else ((24 - len(opt4))// 2 -1) * " "
    if len(intro) < 65:
        introborder = (64 - len(intro))// 2 * " "   #String wird zentriert
        introtext = f"{introborder}{intro}{introborder}"
    elif len(intro) > 64 and len(intro) < 129:
        space_position = intro[60:].find(" ")   #der nächste space character ab Zeichen 60 wird gesucht
        introborder = (64 - len(intro[64:]))// 2 * " "
        intro1 = intro[:60 + space_position]    #der Text bis zum ersten Space nach 60 Zeichen wird in die erste Zeile geschrieben
        intro2 = intro[60 + space_position :]   #der restliche Text wird in die zweite Zeile geschrieben 
        introtext = f"{intro1}\n{introborder}{intro2}{introborder}"
    else:
        space_position1 = intro[60:].find(" ")
        space_position2 = intro[124:].find(" ")
        introborder1 = (space_position1 // 2) * " "
        introborder2 = (64 - len(intro[128:]))// 2 * " "
        intro1 = intro[:60 + space_position1]
        intro2 = intro[60 + space_position1 :124 + space_position2]
        intro3 = intro[124 + space_position2 :]
        introtext = f"{intro1}\n{introborder1}{intro2}{introborder1}\n{introborder2}{intro3}{introborder2}"
    print(
f"""
{introtext}
        
 __________________________          __________________________
(A|{opt1_borderl}{opt1}{opt1_borderr}|          |{opt2_borderl}{opt2}{opt2_borderr}|B)
 ￣￣￣￣￣￣￣￣￣￣￣￣￣          ￣￣￣￣￣￣￣￣￣￣￣￣￣
 __________________________          __________________________
(C|{opt3_borderl}{opt3}{opt3_borderr}|          |{opt4_borderl}{opt4}{opt4_borderr}|D)
 ￣￣￣￣￣￣￣￣￣￣￣￣￣          ￣￣￣￣￣￣￣￣￣￣￣￣￣
"""
    )

    aktion = ""
    while aktion != "a" and aktion != "b" and aktion != "c" and aktion != "d":
        aktion = input("-->")
        if aktion == "a": 
            return opt1_long
        elif aktion == "b":
            return opt2_long
        elif aktion == "c":
            return opt3_long
        elif aktion == "d":
            return opt4_long
        else:
            print("\nUngültige Eingabe. a, b, c oder d ?\n")

def Geschichte_3(intro,opt1, opt2, opt3, opt1_long, opt2_long, opt3_long):   # Geschichte mit 4 Auswahlmöglichkeiten
#Fragen schoener ausgeben:
#Damit die Fragen einheitlich bleiben wird eine maximale Laenge der Auswahlmoeglichkeiten festgelegt (16) und die Schrift zentriert anstatt, dass die Box erweitert wird.
    clear()
    print(pyfiglet.figlet_format("Write - o - mat"))
    opt1_borderl = (24 - len(opt1))// 2 * " "
    opt1_borderr = (24 - len(opt1))// 2 * " " if len(opt1) % 2 == 1 else ((24 - len(opt1))// 2 -1) * " "
    opt2_borderl = (24 - len(opt2))// 2 * " "
    opt2_borderr = (24 - len(opt2))// 2 * " " if len(opt2) % 2 == 1 else ((24 - len(opt2))// 2 -1) * " "
    opt3_borderl = (24 - len(opt3))// 2 * " "
    opt3_borderr = (24 - len(opt3))// 2 * " " if len(opt3) % 2 == 1 else ((24 - len(opt3))// 2 -1) * " "
    if len(intro) < 24:
        introborder = (64 - len(intro))// 2 * " "   #String wird zentriert
        introtext = f"{introborder}{intro}{introborder}"
    elif len(intro) > 64 and len(intro) < 129:
        space_position = intro[60:].find(" ")   #der nächste space character ab Zeichen 60 wird gesucht
        introborder = (64 - len(intro[64:]))// 2 * " "
        intro1 = intro[:60 + space_position]    #der Text bis zum ersten Space nach 60 Zeichen wird in die erste Zeile geschrieben
        intro2 = intro[60 + space_position :]   #der restliche Text wird in die zweite Zeile geschrieben 
        introtext = f"{intro1}\n{introborder}{intro2}{introborder}"
    else:
        space_position1 = intro[60:].find(" ")
        space_position2 = intro[124:].find(" ")
        introborder1 = (space_position1 // 2) * " "
        introborder2 = (64 - len(intro[128:]))// 2 * " "
        intro1 = intro[:60 + space_position1]
        intro2 = intro[60 + space_position1 :124 + space_position2]
        intro3 = intro[124 + space_position2 :]
        introtext = f"{intro1}\n{introborder1}{intro2}{introborder1}\n{introborder2}{intro3}{introborder2}"
    print(
f"""
{introtext}
        
 __________________________          __________________________
(A|{opt1_borderl}{opt1}{opt1_borderr}|          |{opt2_borderl}{opt2}{opt2_borderr}|B)
 ￣￣￣￣￣￣￣￣￣￣￣￣￣          ￣￣￣￣￣￣￣￣￣￣￣￣￣
                   __________________________
                  (C|{opt3_borderl}{opt3}{opt3_borderr}|
                   ￣￣￣￣￣￣￣￣￣￣￣￣￣ 
"""
    )

    aktion = ""
    while aktion != "a" and aktion != "b" and aktion != "c" and aktion != "d":
       # print(opts)
        aktion = input("-->")
        if aktion == "a": 
            return opt1_long
        elif aktion == "b":
            return opt2_long
        elif aktion == "c":
            return opt3_long
        else:
            print("\nUngültige Eingabe. a, b oder c ?\n")

def Geschichte_2(intro,opt1, opt2, opt1_long, opt2_long):   # Geschichte mit 4 Auswahlmöglichkeiten
#Fragen schoener ausgeben:
#Damit die Fragen einheitlich bleiben wird eine maximale Laenge der Auswahlmoeglichkeiten festgelegt (16) und die Schrift zentriert anstatt, dass die Box erweitert wird.
    clear()
    print(pyfiglet.figlet_format("Write - o - mat"))
    opt1_borderl = (24 - len(opt1))// 2 * " "
    opt1_borderr = (24 - len(opt1))// 2 * " " if len(opt1) % 2 == 1 else ((24 - len(opt1))// 2 -1) * " "
    opt2_borderl = (24 - len(opt2))// 2 * " "
    opt2_borderr = (24 - len(opt2))// 2 * " " if len(opt2) % 2 == 1 else ((24 - len(opt2))// 2 -1) * " "
    if len(intro) < 65:
        introborder = (64 - len(intro))// 2 * " "   #String wird zentriert
        introtext = f"{introborder}{intro}{introborder}"
    elif len(intro) > 64 and len(intro) < 129:
        space_position = intro[60:].find(" ")   #der nächste space character ab Zeichen 60 wird gesucht
        introborder = (64 - len(intro[64:]))// 2 * " "
        intro1 = intro[:60 + space_position]    #der Text bis zum ersten Space nach 60 Zeichen wird in die erste Zeile geschrieben
        intro2 = intro[60 + space_position :]   #der restliche Text wird in die zweite Zeile geschrieben 
        introtext = f"{intro1}\n{introborder}{intro2}{introborder}"
    else:
        space_position1 = intro[60:].find(" ")
        space_position2 = intro[124:].find(" ")
        introborder1 = (space_position1 // 2) * " "
        introborder2 = (64 - len(intro[128:]))// 2 * " "
        intro1 = intro[:60 + space_position1]
        intro2 = intro[60 + space_position1 :124 + space_position2]
        intro3 = intro[124 + space_position2 :]
        introtext = f"{intro1}\n{introborder1}{intro2}{introborder1}\n{introborder2}{intro3}{introborder2}"
    print(
f"""
{introtext}
        
 __________________________          __________________________
(A|{opt1_borderl}{opt1}{opt1_borderr}|          |{opt2_borderl}{opt2}{opt2_borderr}|B)
 ￣￣￣￣￣￣￣￣￣￣￣￣￣          ￣￣￣￣￣￣￣￣￣￣￣￣￣
"""
    )

    aktion = ""
    while aktion != "a" and aktion != "b" and aktion != "c" and aktion != "d":
       # print(opts)
        aktion = input("-->")
        if aktion == "a": 
            return opt1_long
        elif aktion == "b":
            return opt2_long
        else:
            print("\nUngültige Eingabe. a oder b ?\n")


Liste_Geschichte = []

def main():  #Alles, was nicht beim Importieren dieser Datei ausgeführt werden soll
    writeomattext = pyfiglet.figlet_format("Write - o - mat") # Write-o-mat in groß zu Beginn ausgeben
    print(writeomattext)
    name = input("Name des Autors -->").capitalize()      # Wird in bei der Benennung der Textdatei benutzt; Erster Buchstabe Groß, Rest klein
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
        Liste_Geschichte.append(Writeomat_Horror.Titelblatt(Writeomat_Horror.Horror_Geschichte_1))
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
        Liste_Geschichte.append(Writeomat_SciFi.Titelblatt(Writeomat_SciFi.SciFi_Geschichte_1))
        Liste_Geschichte.append(Writeomat_SciFi.SciFi_Geschichte_1)
        Liste_Geschichte.append(Writeomat_SciFi.SciFi_Geschichte_2)



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


    

    response = input("Möchten Sie die Geschichte vorgelesen haben wollen?(j/n)").upper()
    while response != "J" and response != "N":  #um falsche eingaben zu vermeiden
     response = input("J/N?\n-->").upper()
    if response == "J":
        print("Hier ist die Stimme")  #gibt die Stimme aus
        sprachausgabe()
    else:
        print("OK, keine Stimme wird abgespielt.") #wird keine Stimme ausgegeben 
    
  


    if sys.platform == "win32": # Windows
        os.startfile(f"{name}'s Geschichte.txt")
    elif sys.platform == "darwin": # Mac
        subprocess.call(["open", f"{name}'s Geschichte.txt"])
    else: # Linux
        subprocess.call(["xdg-open", f"{name}'s Geschichte.txt"])
    
    #Sprachausgabe:

       
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
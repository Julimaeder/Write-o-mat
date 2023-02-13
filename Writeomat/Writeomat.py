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
import time #Für den Anfangstext



def sprachausgabe():
    engine = pyttsx3.init()   
    geschwindigkeit = input("Wählen Sie die Geschwindigkeit der Stimme (S = Schnell, M = Mittel, L = Langsam): \n-->").upper()
    text = " ".join(Liste_Geschichte[2:]) 
    if geschwindigkeit == "L":
        engine.setProperty("rate", 150)  
        engine.say(text)  
        engine.runAndWait()
    elif geschwindigkeit == "M":
        engine.setProperty("rate", 200)  
        engine.say(text)  
        engine.runAndWait()
    elif geschwindigkeit == "S":
        engine.setProperty("rate", 250)  
        engine.say(text)  
        engine.runAndWait()
    else: 
        print("L = Langsam, M= Mittel, S = Schnell")
        

def clear():
    if sys.platform == "win32": #Windows 
        clear_command = 'cls'
    else: # Linux oder Mac
        clear_command = 'clear'
    os.system(clear_command)

def Geschichte_4(intro,opt1, opt2, opt3, opt4, opt1_long, opt2_long, opt3_long, opt4_long, e_choice = ""):   # Geschichte mit 4 Auswahlmöglichkeiten
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
    if e_choice != "":
        estring = """                   __________________________
                  (E|        Zufällig       |
                   ￣￣￣￣￣￣￣￣￣￣￣￣￣ 
        """
    else:
        estring = ""
    print(
f"""
{introtext}
        
 __________________________          __________________________
(A|{opt1_borderl}{opt1}{opt1_borderr}|          |{opt2_borderl}{opt2}{opt2_borderr}|B)
 ￣￣￣￣￣￣￣￣￣￣￣￣￣          ￣￣￣￣￣￣￣￣￣￣￣￣￣
 __________________________          __________________________
(C|{opt3_borderl}{opt3}{opt3_borderr}|          |{opt4_borderl}{opt4}{opt4_borderr}|D)
 ￣￣￣￣￣￣￣￣￣￣￣￣￣          ￣￣￣￣￣￣￣￣￣￣￣￣￣
{estring}
"""
    )

    aktion = ""
    if estring == "":
        while aktion != "A" and aktion != "B" and aktion != "C" and aktion != "D":
            aktion = input("-->").upper()
            if aktion == "A": 
                return opt1_long
            elif aktion == "B":
                return opt2_long
            elif aktion == "C":
                return opt3_long
            elif aktion == "D":
                return opt4_long
            else:
                print("\nUngültige Eingabe. A, B, C oder D ?\n")
    else:
        while aktion != "A" and aktion != "B" and aktion != "C" and aktion != "D" and aktion != "E":
            aktion = input("-->").upper()
            if aktion == "A": 
                return opt1_long
            elif aktion == "B":
                return opt2_long
            elif aktion == "C":
                return opt3_long
            elif aktion == "D":
                return opt4_long
            elif aktion == "E":
                return e_choice
            else:
                print("\nUngültige Eingabe. A, B, C, D oder E ?\n")

def Geschichte_3(intro,opt1, opt2, opt3, opt1_long, opt2_long, opt3_long, e_choice = ""):   # Geschichte mit 4 Auswahlmöglichkeiten
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
    if e_choice != "":
        estring = """                   __________________________
                  (D|        Zufällig       |
                   ￣￣￣￣￣￣￣￣￣￣￣￣￣ 
        """
    else:
        estring = ""
    print(
f"""
{introtext}
        
 __________________________          __________________________
(A|{opt1_borderl}{opt1}{opt1_borderr}|          |{opt2_borderl}{opt2}{opt2_borderr}|B)
 ￣￣￣￣￣￣￣￣￣￣￣￣￣          ￣￣￣￣￣￣￣￣￣￣￣￣￣
                   __________________________
                  (C|{opt3_borderl}{opt3}{opt3_borderr}|
                   ￣￣￣￣￣￣￣￣￣￣￣￣￣ 
{estring}
"""
    )

    aktion = ""
    if estring == "":
        while aktion != "A" and aktion != "B" and aktion != "C":
            aktion = input("-->").upper()
            if aktion == "A": 
                return opt1_long
            elif aktion == "B":
                return opt2_long
            elif aktion == "C":
                return opt3_long
            else:
                print("\nUngültige Eingabe. A, B oder C ?\n")
    else:
        while aktion != "A" and aktion != "B" and aktion != "C" and aktion != "D":
            aktion = input("-->").upper()
            if aktion == "A": 
                return opt1_long
            elif aktion == "B":
                return opt2_long
            elif aktion == "C":
                return opt3_long
            elif aktion == "D":
                return e_choice
            else:
                print("\nUngültige Eingabe. A, B, C oder D ?\n")

def Geschichte_2(intro,opt1, opt2, opt1_long, opt2_long, e_choice = ""):   # Geschichte mit 4 Auswahlmöglichkeiten
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
    if e_choice != "":
        estring = """                   __________________________
                  (C|        Zufällig       |
                   ￣￣￣￣￣￣￣￣￣￣￣￣￣ 
        """
    else:
        estring = ""
    print(
f"""
{introtext}
        
 __________________________          __________________________
(A|{opt1_borderl}{opt1}{opt1_borderr}|          |{opt2_borderl}{opt2}{opt2_borderr}|B)
 ￣￣￣￣￣￣￣￣￣￣￣￣￣          ￣￣￣￣￣￣￣￣￣￣￣￣￣
{estring}
"""
    )

    aktion = ""
    if estring == "":
        while aktion != "A" and aktion != "B":
            aktion = input("-->").upper()
            if aktion == "A": 
                return opt1_long
            elif aktion == "B":
                return opt2_long
            else:
                print("\nUngültige Eingabe. A oder B ?\n")
    else:
        while aktion != "A" and aktion != "B" and aktion != "C":
            aktion = input("-->").upper()
            if aktion == "A": 
                return opt1_long
            elif aktion == "B":
                return opt2_long
            elif aktion == "C":
                return e_choice
            else:
                print("\nUngültige Eingabe. A, B oder C ?\n")
                
                
def Anfangstext_print(Anfangstext, print_speed=0.04):
	for i in Anfangstext:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(print_speed)
        
Liste_Geschichte = []

def main():  #Alles, was nicht beim Importieren dieser Datei ausgeführt werden soll
    #Die Anfangsanimation
    clear()
    writeomattext = pyfiglet.figlet_format("Write - o - mat") # Write-o-mat in groß zu Beginn ausgeben
    print(writeomattext)
    Anfangstext = "Herzlich Willkommen bei Write-o-mat :) \nHier kannst du aus einer Vielzahl an Bausteinen deine Individuelle Geschichte erstellen. \nViel Spaß!"
    Anfangstext_print(Anfangstext)
    clear()
    timer = 3
    space = "\n" * 10
    space2 = " " * 50
    while timer >0:
        print(writeomattext)
        print(Anfangstext)
        print(f"{space}{space2}Start in {timer}")
        timer = timer -1
        time.sleep(1)
        clear()
        
    print(writeomattext)
    name = input("\nName des Autors -->").capitalize()      # Wird in bei der Benennung der Textdatei benutzt; Erster Buchstabe Groß, Rest klein
    Titel = pyfiglet.figlet_format(input("\nTitel: \n-->"))
    
    #Die Geschichten werden im Maskulinum erzählt und später ggf. mit regex verändert 
    Geschlecht = input("\nWähle das Geschleicht deines Protagonisten/ deiner Protagonistin (m/w) \n-->").upper()
    while Geschlecht != "M" and Geschlecht != "W":     # Um andere Eingaben zu vermeiden
        Geschlecht = input("M/W?\n-->").upper()
    
    Genre = input("\nWähle das Genre deiner Geschichte: \nA) Horror \nB) Fantasy \nC) Science-Fiction \n-->").upper()
    while Genre != "A" and Genre != "B" and Genre != "C":     # Um andere Eingaben zu vermeiden
        Genre = input("A, B oder C?\n-->").upper()
    
    if Genre == "A":
        import Writeomat_Horror
        Liste_Geschichte.append(Titel)
        Liste_Geschichte.append(Writeomat_Horror.Titelblatt(Writeomat_Horror.Horror_Geschichte_1))
        Liste_Geschichte.append(Writeomat_Horror.String_Horror_0)
        Liste_Geschichte.append(Writeomat_Horror.Horror_Geschichte_1)
        Liste_Geschichte.append(Writeomat_Horror.String_Horror_1)
        Liste_Geschichte.append(Writeomat_Horror.Horror_Geschichte_2)
        Liste_Geschichte.append(Writeomat_Horror.String_Horror_2)
        Liste_Geschichte.append(Writeomat_Horror.Horror_Geschichte_3)
        Liste_Geschichte.append(Writeomat_Horror.String_Horror_3)
        Liste_Geschichte.append(Writeomat_Horror.Horror_Geschichte_4)
        Liste_Geschichte.append(Writeomat_Horror.String_Horror_4)
        Liste_Geschichte.append(Writeomat_Horror.Horror_Geschichte_5)
        Liste_Geschichte.append(Writeomat_Horror.String_Horror_5)
        Liste_Geschichte.append(Writeomat_Horror.Horror_Geschichte_6)
        Liste_Geschichte.append(Writeomat_Horror.String_Horror_6)
        Liste_Geschichte.append(Writeomat_Horror.Horror_Geschichte_7)
        Liste_Geschichte.append(Writeomat_Horror.String_Horror_7)
        Liste_Geschichte.append(Writeomat_Horror.Horror_Geschichte_8)
        Liste_Geschichte.append(Writeomat_Horror.String_Horror_8)
        Liste_Geschichte.append(Writeomat_Horror.Horror_Geschichte_9)
        Liste_Geschichte.append(Writeomat_Horror.String_Horror_9)
        Liste_Geschichte.append(Writeomat_Horror.Horror_Geschichte_10)
        Liste_Geschichte.append(Writeomat_Horror.String_Horror_10)
        
        
        
    elif Genre == "B":
        import Writeomat_Fantasy
        Liste_Geschichte.append(Titel)
        Liste_Geschichte.append(Writeomat_Fantasy.Titelblatt(Writeomat_Fantasy.Fantasy_Geschichte_1))
        Liste_Geschichte.append(Writeomat_Fantasy.Fantasy_Geschichte_1)
        Liste_Geschichte.append(Writeomat_Fantasy.Fantasy_Geschichte_2)
        Liste_Geschichte.append(Writeomat_Fantasy.Fantasy_Geschichte_3)
        Liste_Geschichte.append(Writeomat_Fantasy.Fantasy_Geschichte_4)
        Liste_Geschichte.append(Writeomat_Fantasy.Fantasy_Geschichte_5)
        Liste_Geschichte.append(Writeomat_Fantasy.Fantasy_Geschichte_6)
        Liste_Geschichte.append(Writeomat_Fantasy.Fantasy_Geschichte_7)
       
        
    else:
        import Writeomat_SciFi
        Liste_Geschichte.append(Titel)
        Liste_Geschichte.append(Writeomat_SciFi.Titelblatt(Writeomat_SciFi.SciFi_Geschichte_1))
        Liste_Geschichte.append(Writeomat_SciFi.SciFi_Geschichte_1)
        Liste_Geschichte.append(Writeomat_SciFi.SciFi_Geschichte_2)



    # Geschichte in eine txt Datei schreiben  
    # Wird in max 5 Zeilen geteilt
    output = open(f"{name}'s Geschichte.txt", "w", encoding="utf-8")
    output.write(str("".join(Liste_Geschichte[:2]))) # "".join(Liste) ist eien Funktion um die Liste ohne Sonderzeichen zu speichern; in den "" steht wodurch die Elemente getrennt werden
    long_text = " ".join(Liste_Geschichte[2:])
    
    space_position1 = long_text[100:].find(" ")+1 # Der nächste space character ab Zeichen 100 wird gesucht // +1 damit das Leerzeichen noch in der alten Zeile steht 
    short_text1 = long_text[:100 + space_position1]
    
    space_position2 = long_text[len(short_text1) + 100:].find(" ")+1
    short_text2 = long_text[len(short_text1) :len(short_text1) + 100 + space_position2]
    
    space_position3 = long_text[len(short_text1) + len(short_text2) + 100:].find(" ")+1
    short_text3 = long_text[len(short_text1) + len(short_text2) :len(short_text1) + len(short_text2) + 100 + space_position3]
    
    space_position4 = long_text[len(short_text1) + len(short_text2) + len(short_text3) + 100:].find(" ")+1
    short_text4 = long_text[len(short_text1) + len(short_text2) + len(short_text3) :len(short_text1) + len(short_text2) + len(short_text3) + 100 + space_position4]

    short_text5 = long_text[len(short_text1) + len(short_text2) + len(short_text3) + len(short_text4):]
    clean_text = f"{short_text1}\n{short_text2}\n{short_text3}\n{short_text4}\n{short_text5}"
    output.write(str(clean_text))
    output.close()
    if Geschlecht == "W":       
        pass    #Regex zum Verändern des Geschlechts


    clear()
    print(pyfiglet.figlet_format("Write - o - mat"))
    response = input("Möchten Sie die Geschichte vorgelesen haben wollen? (J/N)\n-->").upper()
    while response != "J" and response != "N":  #um falsche eingaben zu vermeiden
     response = input("J/N?\n-->").upper()
    if response == "J":
        sprachausgabe()  #gibt die Stimme aus
    else:
        print("OK, keine Stimme wird abgespielt.") #wird keine Stimme ausgegeben 
    
  


    if sys.platform == "win32": # Windows
        os.startfile(f"{name}'s Geschichte.txt")
    elif sys.platform == "darwin": # Mac
        subprocess.call(["open", f"{name}'s Geschichte.txt"])
    else: # Linux
        subprocess.call(["xdg-open", f"{name}'s Geschichte.txt"])
     
       
if __name__ == "__main__":
    main()

"""
Notizen:
    Wichtige Sachen im Code mit #!!! markieren
    Reloaded modules:<module_name> ist nur eine Warnung von Spyder, ist nicht wichtig und kann in den Einstellungen ausgestellt werden
    Im ersten Geschichtsteil bitte kein Random
"""
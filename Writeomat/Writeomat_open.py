# -*- coding: utf-8 -*-
import os
import sys
import subprocess

print("Write-o-mat wird gestartet...")
path = __file__ [:-18] #Dateinamen hinten weggecutten
os.chdir(path)
if sys.platform == "win32": # Windows
    os.system('start cmd /C "python Writeomat.py"') #/K lässt das cmd Fenster geöffnet, /C schließt es danach
elif sys.platform == "darwin":  # Mac
    subprocess.run(['open', '-a', 'Terminal'])
    subprocess.run(['python', 'Writeomat.py'])
else:  # Linux
    subprocess.run(['x-terminal-emulator', '-e', 'python Writeomat.py'])
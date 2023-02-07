import re

def Text_Nach_Geschlecht(self, text):
    if self.Geschlecht == "M":
        text = re.sub(r"er\b", "er", text)
        text = re.sub(r"Er\b", "Er", text)
        text = re.sub(r"ein\b", "ein", text)
        text = re.sub(r"Ein\b", "Ein", text)
        text = re.sub(r"sein\b", "sein", text)
        text = re.sub(r"Sein\b", "Sein", text)
    elif self.Geschlecht == "W":
        text = re.sub(r"er\b", "sie", text)
        text = re.sub(r"Er\b", "Sie", text)
        text = re.sub(r"ein\b", "eine", text)
        text = re.sub(r"Ein\b", "Eine", text)
        text = re.sub(r"sein\b", "ihr", text)
        text = re.sub(r"Sein\b", "Ihr", text)
    else:
        print("Ungültiges Geschlecht.")
        self.Geschlecht = input("-->")
        self.Geschlecht_Text(text)
    return text

#wird noch bearbeitet und ausfegührt gegebenenfalls angepasst, optional mit PyDictionary bzw komplett neu geschrieben

from PyDictionary import PyDictionary
import re

def Geschlecht_Angepasst(text, Geschlecht):
    if Geschlecht == 'M':
        text = re.sub(r'\b(er)\b', 'er', text)
        text = re.sub(r'\b(Ein)\b', 'Ein', text)
    elif Geschlecht == 'W':
        text = re.sub(r'\b(er)\b', 'sie', text)
        text = re.sub(r'\b(Ein)\b', 'Eine', text)
    else:
        raise ValueError("Falsches  Geschlecht.")
        
    # Pronomen wchsel
    text_komplett= text.split()
    for i in range(len(text_komplett)):
        word = text_komplett[i]
        if dictionary.gender(word) == 'male':
            if Geschlecht == 'W':
                word = dictionary.feminine(word)
                text_komplett[i] = word
        elif dictionary.gender(word) == 'female':
            if Geschlecht == 'M':
                word = dictionary.masculine(word)
                text_komplett[i] = word
    neuer_text = ' '.join(text_komplett)
    return neuer_text

from Writeomat_test import Geschichte
from Writeomat_test import Name_Held
from Writeomat_test import Liste_Geschichte

Fantasy_Geschichte_1 = Geschichte("Wähle den Helden deiner Geschichte ",
           "a) Eine gute Fee \nb) Ein Oger \nc) Ein Magier \nd) Ein Zwerg",
           f"Es war einmal eine gute Fee namens {Name_Held}. Diese ",
           f"Es war einmal ein Oger namens {Name_Held}. Dieser ",
           f"Es war einmal ein Magier namens {Name_Held}. Dieser ",
           f"Es war einmal ein kleiner Zwerg namens {Name_Held}. Dieser ",
           Liste_Geschichte)    # Ist Liste_Geschichte wirklich notwendig?

Fantasy_Geschichte_2 = Geschichte("Welches Gefährt hat dein Held",
           "a) Ein Pferd \nb) Ein Riese \nc) Ein Dreirad \nd) Zu Fuß",
           "reitet voller Hochmut ein starkes Ross ",
           "sitzt auf dem Rücken eines stolzen Riesen ",
           "fährt voller Stolz ein Renn-Dreirad  ",
           "schreitet tapfer zu fuße voran ",
           Liste_Geschichte)

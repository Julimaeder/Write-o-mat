# -*- coding: utf-8 -*-

from Writeomat import Geschichte
Name_Held = input("Wähle den Namen deines Protagonisten \n-->")

SciFi_Geschichte_1 = Geschichte("Wähle den Helden deiner Geschichte ",
           "a) Super Held \nb) Bösewicht",
           f"Es war einmal in einer fernen Galaxie ein Held {Name_Held}. Dieser ",
           f"Es war einmal in einer fernen Galaxie ein Bösewicht namens {Name_Held} the destroyer. Dieser ")

SciFi_Geschichte_2 = Geschichte("An welchem Ort willst du starten",
           "a) Raumschiff \nb) Planet Auria",
           "Er war in seinem riesen Raumschiff mit dem er durch die Galaxie reiste. ",
           "Er landete auf dem Planeten Auria, welcher bekannt für seine freundlichen Bewohner ist. ")


zijde = input()

if zijde == "waarde":
    getalKleur = int(input())
else:
    getalKleur = input()

draaien = input()  

if zijde == "waarde":
    nodig = getalKleur % 2 == 0
else:
    nodig = getalKleur != "rood"
if nodig:
    tekst = "moeten gedraaid worden"
else:
    tekst = "moeten niet gedraaid worden"

if (draaien == "ja") == nodig:
    output = "Juist"
else:
    output = "Fout"

print(f"{output}: kaarten met {zijde} {getalKleur} {tekst}.")
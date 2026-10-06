speler1 = input()
speler2 = input()

wint = [
    ("schaar", "blad"),
    ("blad", "steen"),
    ("steen", "hagedis"),
    ("hagedis", "Spock"),
    ("Spock", "schaar"),
    ("schaar", "hagedis"),
    ("hagedis", "blad"),
    ("blad", "Spock"),
    ("Spock", "steen"),
    ("steen", "schaar"),
]

if speler1 == speler2:
    print("gelijkspel")
elif (speler1, speler2) in wint:
    print("speler1 wint")
else:
    print("speler2 wint")
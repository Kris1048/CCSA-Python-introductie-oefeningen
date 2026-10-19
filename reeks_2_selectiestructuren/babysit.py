uurB = int(input())
minuutB = int(input())
uurE = int(input())
minuutE = int(input())

begin = uurB * 60 + minuutB
einde = uurE * 60 + minuutE

if begin < 18 * 60 or einde < begin:
    print("ongeldige invoer")
else:
    grens = 21 * 60 + 30

    goedkoop = max(0, min(einde, grens) - begin)
    duur = max(0, einde - max(begin, grens))

    totaal = goedkoop / 60 * 2 + duur / 60 * 4
    print(totaal)
    
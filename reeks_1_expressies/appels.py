appels = int(input())

pallet = appels // (20 * 35)
over = appels % (20 * 35)
kisten = over // 20
rest = over % 20

print(pallet)
print(kisten)
print(rest)
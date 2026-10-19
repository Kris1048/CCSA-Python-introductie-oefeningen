weging1 = input()
weging2 = input()


if(weging1 == 'rechts'):
    start = 1
elif(weging1 == 'links'):
    start = 4
else:
    start = 7    

if(weging2 == 'rechts'):
    getal = start
elif(weging2 == 'links'):
    getal = start + 1
else:
    getal = start + 2

print(f"muntstuk #{getal} is vervalst")            

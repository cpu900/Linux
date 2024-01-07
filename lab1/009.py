#!/usr/bin/env python3

#ange tal och räknesätt
tal1 = int(input("Ange tal 1\n"))
tal2 = int(input("Ange tal 2\n"))
typ1 = input("Ange räknesättet\n")

# Utför beräkningar
if typ1 == "+":
    resultat = tal1 + tal2
elif typ1 == "-":
    resultat = tal1 - tal2
elif typ1 == "*":
    resultat = tal1 * tal2
elif typ1 == "/":
    resultat = tal1 / tal2
else:
    print("Ogiltigt räknesätt. Vänligen ange +, -, * eller /.")
    resultat = None

# Skriv ut resultatet
if resultat is not None:
    print(f"Resultatet av {tal1} {typ1} {tal2} är {resultat}.")
else:
    print("Fel försök igen tyvärr")

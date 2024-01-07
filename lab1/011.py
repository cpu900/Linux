#!/usr/bin/env python3

#läs in string 
string1 = input("Ange text att vända på\n")

#vänd på string
summan_text = f"\nFör string: {string1}\nString vänd: {string1[::-1]}"

print("------------------", summan_text)


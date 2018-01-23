# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 22:21:00 2018

@author: hecto
Simple workspace to decypher a substitution cypher manually.
Enter the original cyphertext at the beginning.
Alternate between selecting a cypher character and entering
the desired plain character.
"""

c=' '
plaintext=[]

# Input the ciphertext to solve
ciphertext = input("Enter cyphertext:")

# Initialize plaintext list with as many positions as the ciphertext
for i in range(0,len(ciphertext)):
    plaintext.append(' ')
    
# Repeat until user decides to quit.
# Accept a pair of characters.
# The first character is looked up in the ciphertext.
# If found, the corresponding plaintext character is
# replaced with the second character
# and the current state is displayed
while c != "quit":
    for i in range(0, len(plaintext)):
        print(plaintext[i], end='')
    print(' ')
    print(ciphertext)    
    c = input("enter cypher character followed by plain character ('quit' to exit):")
    print(' ')
    for i in range(0,len(ciphertext)):
        if ciphertext[i]==c[0]:
            plaintext[i]=c[1]

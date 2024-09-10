#from hangman_art import logo
import hangman_art
from hangman_word import word_list
from hangman_art import stages
import random
import os

#Las vidas del juevo esta en esta variable
lifes=6
#Se imprme el logo del archivo hangman_art y la variable logo
print(hangman_art.logo)
# se gurda en la variable randum la palabra al azar de la lsta word_list que tiene las palabras del archivo hangman_word
randum=random.choice(word_list)

print(f"Here your word --> {randum} <--, but shhh because is top secret ")
print(f"You have {lifes} to start the game")

#La lista vacia donde se guardara la palabra
display=[]
lon=len(randum)
#se imprime la misma cantidad de caracteres de la palabra seleccionada y se sustituyen por guines bajos en la lista display
for _ in range(lon):
	display+="_"

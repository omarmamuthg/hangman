#from hangman_art import logo
import hangman_art
from hangman_word import word_list
from hangman_art import stages
import random
import os


lifes=6
print(hangman_art.logo)
randum=random.choice(word_list)

print(f"Here your word --> {randum} <--, but shhh because is top secret ")
print(f"You have {lifes} to start the game")

display=[]
lon=len(randum)
for _ in range(lon):
	display+="_"

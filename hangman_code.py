#from hangman_art import logo
import hangman_art
from hangman_word import word_list
from hangman_art import stages
import random
import os


def play_hangman(randum, display, stages, lifes):
    # Calcula la longitud de la palabra seleccionada aleatoriamente
    lon = len(randum)
    
    # Bucle infinito que mantiene el juego en ejecución hasta que se gana o se pierden todas las vidas
    while True:
        # Solicita al usuario que adivine una letra
        guess = input("\nGuess a letter please: ")
        
        # Limpia la pantalla para una mejor experiencia visual
        os.system('cls')
        
        # Verifica si la letra ya ha sido adivinada previamente
        if guess in display:
            print(f"\nThis letter was already guessed {guess}")
        
        # Recorre cada letra de la palabra para ver si coincide con la adivinada
        for letter in range(lon):
            if randum[letter] == guess:
                # Si hay coincidencia, la letra se revela en la lista display
                display[letter] = guess
        
        # Muestra el progreso actual de la palabra adivinada
        print()
        print(f"{' '.join(display)}")

        # Si la letra adivinada no está en la palabra
        if guess not in randum:
            # Se pierde una vida
            lifes -= 1
            print("\nThis letter isn't in the chosen word, please try again with another letter :3")
            print(f"You lose a life, you have {lifes} left")
            # Muestra la etapa actual del ahorcado según las vidas restantes
            print(stages[lifes])
            # Si se han perdido todas las vidas, el juego termina y el jugador pierde
            if lifes == 0:
                print("You have 0 lives, you're a fucking loser .|.")
                break

        # Si no quedan guiones bajos en display, significa que el jugador ha adivinado toda la palabra
        if "_" not in display:
            print("\nYou are a fucking winner <3")
            break
        else:
            # Continúa el juego si no se ha ganado o perdido
            continue


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


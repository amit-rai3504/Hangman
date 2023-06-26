import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

display = []
for ch in chosen_word:
  display.append("_")

print(display)
while not end_of_game:
  guess = input("Please guess a letter:").lower()
  
  #If the user has entered a letter they've already guessed
  if guess in display:
        print(f"You've already guessed {guess}")

  #Check guessed letter
  for i in range(word_length):
      letter = chosen_word[i]
      if letter == guess:
          display[i] = letter
          found = True

  if guess not in chosen_word:
    print(f"You chosen letter : {guess}, which is not in word , you lose a life")
    lives = lives - 1
    #If lives goes down to 0 then the game should stop
    if lives == 0:
      end_of_game = True
      print("You Lose, Better luck next time")
    
  print(f"{' '.join(display)}")
  #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
  if "_" not in display:
    end_of_game = True
    print("Congrats You won!!")

  print(stages[lives])

  
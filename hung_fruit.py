from hung_fruits_word import word_list
#about calling module
#import hung_fruits_word.py - and to use call as below
#chosen_word = random.choice(hung_fruits_word.word_list)
#just like in-built random we use
# but our code is more simpler. 
import random

from hung_art import stages, logo
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#logo comes here from our import hung_art
print(logo)

display = []
for _ in range(word_length):
  display += "_"



while not end_of_game:
  guess = input("Guess a letter: ").lower()

  if guess in display:
    print(f"You have already guessed {guess}")

  for position in range(word_length):
    letter =  chosen_word[position]
    #print(f"Current position:{position}\n Current letter: {letter} \n Guessed letter {guess}")
    if letter == guess:
        display[position]  = letter

  if guess not in chosen_word:
    lives -= 1
    print(f"You gusssed {guess}, that's not int the word. You lossed a life. Remaining lives: {lives}")
    if lives == 0:
        end_of_game == True
        print("YOU LOSE!")
  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  if "_" not in display:
        end_of_game = True
        print("You win.")
  print(stages[lives])

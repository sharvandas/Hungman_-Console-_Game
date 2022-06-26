
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


import random
word_list = ["apple", "banana", "carrot","grapes","cherry", "mango","papaya","gauva","cucumber"]
chosen_word = random.choice(word_list)
#print(chosen_word)
display = []
for i in range(0,len(chosen_word)):
  display += "_"
print("HINTS:",display,"length is -->", len(display))
print("Ofcourse no need to guess same letter twice")

size = len(chosen_word)
guess_correct = False
lives = 6
index = 0

while size>0 and lives+1>0 and display != list(chosen_word):
  guess = input("Here you go:  guess a letter, it will assigned to guess: ")
  guess = guess.lower()
  for i in range(0,len(chosen_word)):
    if chosen_word[i] == guess:
      display[i] = guess
      guess_correct = True    

    else:
      display[i]=display[i]
  if guess_correct == True:
    size -= 1
    print("You guess is wild... Good work.")
    if display == list(chosen_word):
      print("Bro you Won...Won...Won...Won.")
  else:
    print(stages[lives])
    lives -=1
    if lives == -1:
      print("'YOU LOOSE' want to play again.")
    #print("lives remaining:",lives+1)
    print("Better luck next time.")
  
  guess_correct = False
    
  #print("Guess correct:", guess_correct)
  print("lives remaining:",lives+1)
  print("display","".join(display))
  #print("chosen_word", chosen_word)
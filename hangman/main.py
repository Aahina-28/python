import random

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


word_list = ["apple","camel","balloon","squirel","cat"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

display = []
for _ in range(word_length):
  display += "-"
print(display)

end_of_game = False
while not end_of_game :
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position]= letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game =True
            print("you loose")
       
    print (f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("you win")
    
    print(stages[lives])
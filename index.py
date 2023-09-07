import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors= """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [Rock , Paper , Scissors]

user_choose = int(input("what do you choose ? Type 0 for ROCK , 1 for PAPER or 2 for SCISSORS."))

if user_choose>=3 or user_choose<0 :
     print("you entered an invalid number")
else:
    print(game_images[user_choose])

    computer_choose = random.randint(0,2)
    print("computer chose:")
    print(game_images[computer_choose])

    if user_choose == 0 and computer_choose == 2:
        print("you wins")
    elif(computer_choose==0 and user_choose ==2):
        print("you loose")
    elif user_choose == 1 and computer_choose== 0 :
        print("you loose")
    elif user_choose == 0 and computer_choose == 1 :
        print("you win")
    elif user_choose == computer_choose :
        print("draw")

    elif(computer_choose > user_choose):
        print("you loose")
    elif(user_choose > computer_choose):
        print("you loose")

    




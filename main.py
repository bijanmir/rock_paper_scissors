import random

def show_winner():
    print(f"You chose {choices[choice1]} \n{display_choice[choice1]}")
    print(f"The computer chose {computer_choice} \n{display_choice[random_number]}")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = ['rock', 'paper', 'scissors']
display_choice = [rock, paper, scissors]

while True:
    #chosing random input from computer (Rock, paper, or scissors) by chosing an index from the choices list
    random_number = random.randint(0, len(choices) -1)
    computer_choice = choices[random_number]

    #grabbing input from user
    choice1 = int(input("Rock, Paper, or Scissors? \nUse 0 for Rock"
                        "\nUse 1 for Paper \nUse 2 For Scissors\n:"))

    if choice1 == 0:
        if computer_choice == 'rock':
            print("You Tied")
            show_winner()
        elif computer_choice == 'paper':
            print("You Lose")
            show_winner()
        elif computer_choice == 'scissors':
            print("You Win")
            show_winner()
    elif choice1 == 1:
        if computer_choice == 'paper':
            print("You Tied")
            show_winner()
        elif computer_choice == 'rock':
            print("You Win")
            show_winner()
        elif computer_choice == 'scissors':
            print("You Lose")
            show_winner()
    elif choice1 == 2:
        if computer_choice == 'scissors':
            print("You Tied")
            show_winner()
        elif computer_choice == 'rock':
            print("You Lose")
            show_winner()
        elif computer_choice == 'paper':
            print("You Win")
            show_winner()
    else:
        print("You chose something weird")

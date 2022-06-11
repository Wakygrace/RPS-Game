import random

user_wins = 0
computer_wins = 0

choices = ("r", "p", "s")


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in choices:
        continue

    computer_pick = random.choice(choices)
  
    print(f"User({user_input}): Computer({computer_pick})")
  
    if user_input == computer_pick: print("You and The Computer picked the same thing!\n It's a Tie")
  
    if user_input == "r" and computer_pick == "s":
        print("You won!")
        user_wins += 1

    elif user_input == "p" and computer_pick == "r":
        print("You won!")
        user_wins += 1

    elif user_input == "s" and computer_pick == "p":
        print("You won!")
        user_wins += 1
    elif user_input == "r" and computer_pick == "p":
        print("You lose!")
        computer_wins += 1

    elif user_input == "s" and computer_pick == "r":
        print("You lose!")
        computer_wins += 1

    elif user_input == "p" and computer_pick == "s":
        print("You lose!")
        computer_wins += 1

print("Thankyou! Goodbye!")
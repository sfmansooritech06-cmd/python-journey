import random

print("Welcome to Rock Paper & Sessior Game!")



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
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''
sessior =''' 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
 
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors  :"))
computer_choice = random.randint(0, 2)
print(f"Computer choice :{computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print(rock)
    print(sessior)
    
    print("You Win")

elif user_choice == 2 and computer_choice == 0:
    
    print(sessior)
    print(rock)
    
    print("Computer Wins!")
elif user_choice == 1 and computer_choice == 2:
    
    print(paper)
    print(sessior)
    print("Computer Wins!")

elif user_choice == 2 and computer_choice == 1:
    print(sessior)
    print(paper)
    print("You Wins!")

elif user_choice == 0 and computer_choice == 1:
    user_choice=print(rock)
    computer_choice = print(sessior)
    print("Computer Wins!")

elif user_choice == 1 and computer_choice == 0:
    print(rock)
    print(sessior)
    print("You Wins")

elif user_choice == 0 and computer_choice ==0:
    print(rock)
    print(rock)
    print("Draw")
    
elif user_choice == 1 and computer_choice == 1:
    print(paper)
    print(paper)
    print("Draw")

elif user_choice == 2 and computer_choice == 2:
    print(sessior)
    print(sessior)
    
    print("Draw")
else:
    print("Invalid number!")
    

import random

print("🎮 Number Guessing Game")
print("I have chosen a number between 1 and 100.")
print("You have 7 attempts to guess it!")

random_number = random.randint(1, 100)
count = 1
won = False

while count <= 7:
    print(f"\nAttempt {count}/7")
    num = int(input("Enter your guess: "))

    if num == random_number:
        won = True
        print("🎉 Congratulations! You guessed the correct number.")
        break
    elif num < random_number:
        print("📉 Your guess is too low.")
    else:
        print("📈 Your guess is too high.")

    count += 1

if not won:
    print(f"\n❌ Game Over! The number was {random_number}.")

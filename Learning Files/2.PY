import random


the_number = random.randint(1, 4)
guess = 0

print(the_number)
while guess != the_number:
    guess = int(input("Please enter a number: "))
    if guess > the_number:
        print("Player guess lower...\n")
    elif guess < the_number:
        print("Player guess higher...\n")
    else:
        print("Game Over! The number was", the_number,"The Player wins!")
        break


    guess = random.randint(1, 100)

    if guess > the_number:
        print("Computer guess lower...\n")
    elif guess < the_number:
        print("Computer guess higher...\n")
    else:
        print("Game Over! The number was", the_number,"The Computer wins!")
    break


print("Thank you for playing")

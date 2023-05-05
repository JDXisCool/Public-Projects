import random
print (" You have to guess from the number 1 to 10! Good Luck!")

the_number = random.randint(1, 4)
guess = 0

minPossible = 0
maxPossible = 10

while guess != the_number:
    guess = int(input("Please enter a number: "))
    if guess > the_number:
        print("Player, guess lower...\n")
        if guess < maxPossible:
            maxPossible = guess - 1
    elif guess < the_number:
        print("Player, guess higher...\n")
        if guess > minPossible:
            minPossible = guess + 1
    else:
        print("Game Over! The number was", the_number, "The Player wins!")
        break

    guess = random.randint(minPossible, maxPossible)

    if guess > the_number:
        print("Computer, guess lower...\n")
        maxPossible = guess - 1
    elif guess < the_number:
        print("Computer, guess higher...\n")
        minPossible = guess + 1
    else:
        print("Game Over! The number was", the_number,"The Computer wins!")


print("Thank you for playing")
import random
num = random.randint (1, 10)
print (" The random numbers are generated from 1 to 10")
input ("What is the number that you choose?")
if input == num:
    print (" You are A good guesser!")

if input != num:
    print ("The Number that you guessed is wrong. Better luck next time!")    

print ("Thanks for playing!") 
ans = input (" Do you want to play again? Type 1 or 2")
print (" 1 means yes and 2 means no")
if ans == 2:
         num = random.randint (1, 10)
input ("What is the number?")
if input == num:
    print (" You are A good guesser!")

if input != num:
    print ("The Number that you guessed is wrong. Better luck next time!")    

print ("Thanks for playing!")
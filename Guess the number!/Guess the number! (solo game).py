import random
num = random.randint (1, 10)
print (" The random numbers are generated from 1 to 10")
While True
input ("What is the number that you choose?")
if input == num:
    print (" You are A good guesser!")

if input != num:
    print ("The Number that you guessed is wrong. Better luck next time!")    

print ("Thanks for playing!") 

import random
num = random.randint (1, 10)
print (" The random numbers are generated from 1 to 10")
input ("What is the number that you choose?")
if input == num:
    print (" You are A good guesser!")

else:
    print ("The Number that you guessed is wrong. Better luck next time!")    

print ("Thanks for playing!") 
repeat = input ("Would you like to play again? Type y or n : ")
if repeat == "y":
     while True:
         num = random.randint (1, 10)
         input ("What is the number that you choose?")
         if input == num:
             print (" You are A good guesser!")

         else:
             print ("The Number that you guessed is wrong. Better luck next time!")    
    
print ("Thanks for playing!") 
repeat = input ("Would you like to play again? Type y or n : ")
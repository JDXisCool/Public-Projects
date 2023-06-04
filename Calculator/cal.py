import random
Operation = input ("Select one : + , - X , Divison : ")
if Operation == "+":
    number1 = input (" What is Number One? Please type here :")
    number2 = input (" What is Number Two? Please type here :")
    Answer = number1 + number2
    print ("Your answer is"+ Answer)
 
if Operation == "-":
    number1 = input (" What is Number One? Please type here :")
    number2 = input (" What is Number Two? Please type here :")
    Answer = number1 - number2
    print ("Your answer is"+ Answer)

if Operation == "X":
    number1 = input (" What is Number One? Please type here :")
    number2 = input (" What is Number Two? Please type here :")
    Answer = number1 * number2
    print ("Your answer is"+ Answer) 

if Operation == "Division":
    number1 = input (" What is Number One? Please type here :")
    number2 = input (" What is Number Two? Please type here :")
    Answer = number1 / number2
    print ("Your answer is"+ Answer)       
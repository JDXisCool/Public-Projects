import random
Operation = input ("Select one : + , - X , Divison : ")
if Operation == "+":
    number1 = float(input (" What is Number One? Please type here :"))
    number2 = float(input (" What is Number Two? Please type here :"))
    Answer = number1 + number2
    print ("Your answer is " + str(Answer))

elif Operation == "-":
    number1 = float(input (" What is Number One? Please type here :"))
    number2 = float(input (" What is Number Two? Please type here :"))
    Answer = number1 - number2
    print ("Your answer is " + str(Answer))
      
elif Operation == "*":
    number1 = float(input (" What is Number One? Please type here :"))
    number2 = float(input (" What is Number Two? Please type here :"))
    Answer = number1 * number2
    print ("Your answer is " + str(Answer)) 
    
elif Operation == "/": 
    number1 = float(input (" What is Number One? Please type here :"))
    number2 = float(input (" What is Number Two? Please type here :"))
    if number2 != 0:
        Answer = number1 / number2
        print ("Your answer is " + str(Answer))
    else:
        print("Error: Division by zero is not allowed.")

import random
while True:
    Operation = input("Select one : + , - X , Divison : ")
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
        try:
            Answer = number1 / number2
            print ("Your answer is " + str(Answer))
        except:
            print("Error: Division by zero is not allowed.")
            response = input("Please type y or n to use the program again : ")
            if response == "n":
                break
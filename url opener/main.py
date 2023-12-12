from webbrowser import open as show_me

while True:
    url = input("Enter an URL: ")
    show_me(url)

    response = input("Do you want to Repeat your request? Type y or n: ")
    if response.lower() == "n":
        break
    elif response.lower() != "y":
        print("Invalid input. Please enter 'y' or 'n'.")

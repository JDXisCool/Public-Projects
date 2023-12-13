import random
from webbrowser import open as show_me
players = ["Ayyan", "Aditya","Ansh", "Shriram"]
print("Welcome to Team/Player Allocator!")

while True:
    random.shuffle(players)
    response = input("Is it a team or individual sport? Enter 'team' or 'individual': ")
    if response == "team":
        team1 = players[:len(players)//2]
        print("Team 1 captain: " + random.choice(team1))
        print("Team 1:")
        for player in team1:
            print(player)
        
        team2 = players[len(players)//2:]
        print("\nTeam 2 captain: " + random.choice(team2))
        print("Team 2:")
        for player in team2:
            print(player)
    else:
        for i in range(0 , len(players) , 2):
            print(players[i] + " VS " + players[i+1])
            start = random.randrange(i, i+2)
            print(players[start] + " starts")
    
    response = input("Pick teams again? Type y or n: ")
    if response == "n":
        break

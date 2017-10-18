import random
#Decide what type of game you will be playing. For now there is just Gladiator
while True:
    try:
        GameType = input("What type of game do you want to play? For now there is only Gladiator.\n>").lower().split()
    except ValueError:
        print("Sorry, I didn't understand that!")
        continue
    if GameType[0] == "gladiator":
        from Gladiator import GladiatorMain


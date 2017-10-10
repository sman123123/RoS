import random
#The Player
class CurrentCharacter:
    def __init__(self, name, brawn, daring, tenacity, heart, sagacity, cunning, reflex, aim, knockdown, knockout):
        self.name = name
        self.brawn = brawn
        self.daring = daring
        self.tenacity = tenacity
        self.heart = heart
        self.sagacity = sagacity
        self.cunning = cunning
        self.reflex = reflex
        self.aim = aim
        self.knockdown = knockdown
        self.knockout = knockout

#Have player create their character.
#Set number of Attribute Points to start the game with.
StartingPoints = 34
print("You have 34 Attribute Points to disperse among the 6 Main Attributes, Brawn, Daring, Tenacity, Heart, Sagacity, and Cunning. ")
while True:
    try:
        Brawn = int(input("How many points will you assign to Brawn? You can assign between 1 and 8 Points. "))
    except ValueError:
        print("Sorry, I didn't understand that!")
        continue
    if Brawn < 0 or Brawn > 8:
        print("You can assign between 1 and 8 Points.")
        continue
    else:
        break
StartingPoints = StartingPoints - Brawn
print("You have " + str(StartingPoints) + " Points left.")

while True:
    try:
        Daring = int(input("How many points will you assign to Daring? You can assign between 1 and 8 Points. "))
    except ValueError:
        print("Sorry, I didn't understand that!")
        continue
    if Daring < 0 or Daring > 8:
        print("You can assign between 1 and 8 Points.")
        continue
    else:
        break
StartingPoints = StartingPoints - Daring
print("You have " + str(StartingPoints) + " Points left.")

while True:
    try:
        Tenacity = int(input("How many points will you assign to Tenacity? You can assign between 1 and 8 Points. "))
    except ValueError:
        print("Sorry, I didn't understand that!")
        continue
    if Tenacity < 0 or Tenacity > 8:
        print("You can assign between 1 and 8 Points.")
        continue
    else:
        break
StartingPoints = StartingPoints - Tenacity
print("You have " + str(StartingPoints) + " Points left.")

while True:
    try:
        Heart = int(input("How many points will you assign to Heart? You can assign between 1 and 8 Points. "))
    except ValueError:
        print("Sorry, I didn't understand that!")
        continue
    if Heart < 0 or Heart > 8:
        print("You can assign between 1 and 8 Points.")
        continue
    else:
        break
StartingPoints = StartingPoints - Heart
print("You have " + str(StartingPoints) + " Points left.")

Player = CurrentCharacter("Stuart", "brawn", "daring", "tenacity", "heart", "sagacity", "cunning", "reflex", "aim", "knockdown", "knockout")

#Loop Infinitely
Dead = False
while Dead == False:

    #get the player's next 'command'
    command = input("o==[=========>").lower().split()

import random
from Gladiator import Character
from Gladiator import Enemies
from Equipment import MeleeWeapons
from Equipment import Armor
print("You find yourself in the preparation room beneath the Arena. You hear the roar of the crowd above you.")
print("o==[=========> <=========]==o")
#Loop until player selects character.
while True:
    try:
        Player = input("Which character do you want to play? For now there is only the Soldier\n>").lower().split()
    except ValueError:
        print("Sorry, I didn't understand that!")
        continue
    if Player[0] == "soldier":
        Player = Character.Soldier
        #Loop until player selects his weapon.
        while True:
            try:
                CurrentWeapon = input("Which weapon do you take? The Soldier is proficient with the Arming Sword, the Longsword, and the Mace.\n>").lower().split()
            except ValueError:
                print("Sorry, I didn't understand that!")
                continue
            if CurrentWeapon[0] == "arming":
                CurrentWeapon = MeleeWeapons.ArmingSword
                #Loop until player says 'yes' or 'no' to using a Shield.
                while True:
                    try:
                        CurrentShield = input("Will you use a shield? You can take a buckler, a small shield, or a large shield. Type 'No' to choose no shield.\n>").lower().split()
                    except ValueError:
                        print("Sorry, I didn't understand that!")
                        continue
                    if CurrentShield[0] == "buckler":
                        CurrentShield = Armor.Buckler
                        break
                    elif CurrentShield[0] == "small":
                        CurrentShield = Armor.SmallShield
                        break
                    elif CurrentShield[0] == "large":
                        CurrentShield = Armor.LargeShield
                        break
                    elif CurrentShield[0] == "no":
                        break
                break
            elif CurrentWeapon[0] == "longsword":
                CurrentWeapon = MeleeWeapons.HandandaHalf1h
                break
            elif CurrentWeapon[0] == "mace":
                CurrentWeapon = MeleeWeapons.Mace
                #Loop until player says 'yes' or 'no' to using a Shield.
                while True:
                    try:
                        CurrentShield = input("Will you use a shield? You can take a buckler, a small shield, or a large shield. Type 'No' to choose no shield.\n>").lower().split()
                    except ValueError:
                        print("Sorry, I didn't understand that!")
                        continue
                    if CurrentShield[0] == "buckler":
                        CurrentShield = Armor.Buckler
                        break
                    elif CurrentShield[0] == "small":
                        CurrentShield = Armor.SmallShield
                        break
                    elif CurrentShield[0] == "large":
                        CurrentShield = Armor.LargeShield
                        break
                    elif CurrentShield[0] == "no":
                        break
                break
            
        #Loop until player selects his armor.
        while True:
            try:
                CurrentArmor = input("What kind of armor will you wear? For now you can only choose Leather.\n>").lower().split()
            except ValueError:
                print("Sorry, I didn't understand that!")
                continue
            if CurrentArmor[0] == "leather":
                CurrentArmor = Armor.Leather
                break
        break

#Loop until player selects enemy.
while True:
    try:
        Enemy = input("Which enemy would you like to fight? For now there is only the Slave.\n>").lower().split()
    except ValueError:
        print("Sorry, I didn't understand that!")
        continue
    if Enemy[0] == "slave":
        Enemy = Enemies.Slave
        #Loop until the player selects a weapon for the enemy.
        while True:
            try:
                EnemyWeapon = input("Which weapon will the Slave use? A Gladius, a Spatha, or a Club?\n>").lower().split()
            except ValueError:
                print("Sorry, I didn't understand that!")
                continue
            if EnemyWeapon[0] == "gladius":
                EnemyWeapon = MeleeWeapons.Gladius
                #Loop until player says 'yes' or 'no' to using a Shield.
                while True:
                    try:
                        EnemyShield = input("Will the Slave use a shield? You can take a buckler, a small shield, or a large shield. Type 'No' to choose no shield.\n>").lower().split()
                    except ValueError:
                        print("Sorry, I didn't understand that!")
                        continue
                    if EnemyShield[0] == "buckler":
                        EnemyShield = Armor.Buckler
                        break
                    elif EnemyShield[0] == "small":
                        EnemyShield = Armor.SmallShield
                        break
                    elif EnemyShield[0] == "large":
                        EnemyShield = Armor.LargeShield
                        break
                    elif EnemyShield[0] == "no":
                        break
                break
            elif EnemyWeapon[0] == "spatha":
                EnemyWeapon = MeleeWeapons.Spatha
                #Loop until player says 'yes' or 'no' to using a Shield.
                while True:
                    try:
                        EnemyShield = input("Will the Slave use a shield? You can take a buckler, a small shield, or a large shield. Type 'No' to choose no shield.\n>").lower().split()
                    except ValueError:
                        print("Sorry, I didn't understand that!")
                        continue
                    if EnemyShield[0] == "buckler":
                        EnemyShield = Armor.Buckler
                        break
                    elif EnemyShield[0] == "small":
                        EnemyShield = Armor.SmallShield
                        break
                    elif EnemyShield[0] == "large":
                        EnemyShield = Armor.LargeShield
                        break
                    elif EnemyShield[0] == "no":
                        break
                break
            elif EnemyWeapon[0] == "club":
                EnemyWeapon = MeleeWeapons.Club
                #Loop until player says 'yes' or 'no' to using a Shield.
                while True:
                    try:
                        EnemyShield = input("Will the Slave use a shield? You can take a buckler, a small shield, or a large shield. Type 'No' to choose no shield.\n>").lower().split()
                    except ValueError:
                        print("Sorry, I didn't understand that!")
                        continue
                    if EnemyShield[0] == "buckler":
                        EnemyShield = Armor.Buckler
                        break
                    elif EnemyShield[0] == "small":
                        EnemyShield = Armor.SmallShield
                        break
                    elif EnemyShield[0] == "large":
                        EnemyShield = Armor.LargeShield
                        break
                    elif EnemyShield[0] == "no":
                        break
                break
        #Loop until the player selects armor for the enemy.
        break
        
#Loop until dead.
Dead = False
while Dead == False:
    try:
        #Get the player's next 'command'
        command = input("o==[=========>").lower().split()
    except ValueError:
        print("Sorry, I didn't understand that!")
        continue
    if command[0] == "fight":
        from Mechanics import Combat

    #If player dies, game ends.
    if Dead == True:
        print("You died!")
        break

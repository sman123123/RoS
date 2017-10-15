#Define the Player Class.
class CurrentCharacter:
    def __init__(self, name, brawn, daring, tenacity, heart, sagacity, cunning, reflex, aim, knockdown, knockout, brawling, cut, dagger, greatsword, longsword, mass, pole, spear, sword, wrestling):
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
        self.brawling = brawling
        self.cut = cut
        self.dagger = dagger
        self.greatsword = greatsword
        self.longsword = longsword
        self.mass = mass
        self.pole = pole
        self.spear = spear
        self.sword = sword
        self.wrestling = wrestling
        
        #Have player create their character.      
        #Set number of Attribute Points to start the game with.
        StartingPoints = 29
        print("You have 29 Attribute Points to disperse among the 6 Main Attributes, Brawn, Daring, Tenacity, Heart, Sagacity, and Cunning. ")
        print("o==[=========> <=========]==o")
        #Loop until chosen Attributes are <= 29
        while True:
            try:
                #Have player set their character's Brawn, loop until get a number from 1 - 8.
                while True:
                    try:
                        Brawn = int(input("How many points will you assign to Brawn? You can assign between 1 and 8 Points.\n>"))
                    except ValueError:
                        print("Sorry, I didn't understand that!")
                        continue
                    if Brawn < 1 or Brawn > 8:
                        print("You can assign between 1 and 8 Points.")
                        continue
                    elif StartingPoints - Brawn < 5:
                        print("You have " + str(StartingPoints) + " Points left and 5 more Attributes!")
                        continue
                    else:
                        break
                StartingPoints = StartingPoints - Brawn
                print("You have " + str(StartingPoints) + " Points left.")
                print("o==[=========> <=========]==o")
                
                #Have player set their character's Daring, loop until get a number from 1 - 8.
                while True:
                    try:
                        Daring = int(input("How many points will you assign to Daring? You can assign between 1 and 8 Points.\n>"))
                    except ValueError:
                        print("Sorry, I didn't understand that!")
                        continue
                    if Daring < 1 or Daring > 8:
                        print("You can assign between 1 and 8 Points.")
                        continue
                    elif StartingPoints - Daring < 4:
                        print("You have " + str(StartingPoints) + " Points left and 4 more Attributes!")
                        continue
                    else:
                        break
                StartingPoints = StartingPoints - Daring
                print("You have " + str(StartingPoints) + " Points left.")
                print("o==[=========> <=========]==o")
                
                #Have player set their character's Tenacity, loop until get a number from 1 - 8.
                while True:
                    try:
                        Tenacity = int(input("How many points will you assign to Tenacity? You can assign between 1 and 8 Points.\n>"))
                    except ValueError:
                        print("Sorry, I didn't understand that!")
                        continue
                    if Tenacity < 1 or Tenacity > 8:
                        print("You can assign between 1 and 8 Points.")
                        continue
                    elif StartingPoints - Tenacity < 3:
                        print("You have " + str(StartingPoints) + " Points left and 3 more Attributes!")
                        continue
                    else:
                        break
                StartingPoints = StartingPoints - Tenacity
                print("You have " + str(StartingPoints) + " Points left.")
                print("o==[=========> <=========]==o")
                
                #Have player set their character's Heart, loop until get a number from 1 - 8.
                while True:
                    try:
                        Heart = int(input("How many points will you assign to Heart? You can assign between 1 and 8 Points.\n>"))
                    except ValueError:
                        print("Sorry, I didn't understand that!")
                        continue
                    if Heart < 1 or Heart > 8:
                        print("You can assign between 1 and 8 Points.")
                        continue
                    elif StartingPoints - Heart < 2:
                        print("You have " + str(StartingPoints) + " Points left and 2 more Attributes!")
                        continue
                    else:
                        break
                StartingPoints = StartingPoints - Heart
                print("You have " + str(StartingPoints) + " Points left.")
                print("o==[=========> <=========]==o")
                
                #Have player set their character's Sagacity, loop until get a number from 1 - 8.
                while True:
                    try:
                        Sagacity = int(input("How many points will you assign to Sagacity? You can assign between 1 and 8 Points.\n>"))
                    except ValueError:
                        print("Sorry, I didn't understand that!")
                        continue
                    if Sagacity < 1 or Sagacity > 8:
                        print("You can assign between 1 and 8 Points.")
                        continue
                    elif StartingPoints - Sagacity < 1:
                        print("You only have " + str(StartingPoints) + " Points left and 1 more Attribute!")
                        continue
                    else:
                        break
                StartingPoints = StartingPoints - Sagacity
                print("You have " + str(StartingPoints) + " Points left.")
                print("o==[=========> <=========]==o")
                
                #Have player set their character's Cunning, loop until get a number from 1 - 8.
                while True:
                    try:
                        Cunning = int(input("How many points will you assign to Cunning? You can assign between 1 and 8 Points.\n>"))
                    except ValueError:
                        print("Sorry, I didn't understand that!")
                        continue
                    if Cunning < 1 or Cunning > 8:
                        print("You can assign between 1 and 8 Points.")
                        continue
                    elif StartingPoints - Cunning < 0:
                        print("You only have " + str(StartingPoints) + " Points left!")
                        continue
                    else:
                        break
                StartingPoints = StartingPoints - Cunning

            except ValueError:
                print("Sorry, I didn't understand that!")
                continue
            if StartingPoints < 0:
                print("You only have 29 points!")
                continue
            else:
                break
            
        #Set Combination Attributes based on choices for Basic Attributes.
        Reflex = round((Cunning + Daring)/2, 0)
        Aim = round((Sagacity + Cunning)/2, 0)
        Knockdown = round((Brawn + Daring)/2, 0)
        Knockout = round((Brawn + Tenacity)/2, 0)

        #Set Proficiencies
        StartingProficiencies = 11
        print("You have 11 Proficiency Points to disperse among the main Proficiencies.")
        print("o==[=========> <=========]==o")
        #Loop until chosen Proficiencies are <= 11
        while True:
            try:
                #Have player set their character's Brawling, loop until get a number from 0 - 12.
                while True:
                    try:
                        print("Brawling - This proficiency consists first and foremost of punching and kicking, derived by means of the Bash Maneuver, but also of grappling and plenty of dirty tricks.")
                        Brawling = int(input("How many points will you assign to Brawling? You can assign between 0 and 12 Points.\n>"))
                    except ValueError:
                        print("Sorry, I didn't understand that!")
                        continue
                    if Brawling < 0 or Brawling > 12:
                        print("You can assign between 0 and 12 Points.")
                        continue
                    elif StartingProficiencies - Brawling < 0:
                        print("You only have 11 Points!")
                        continue
                    else:
                        break
                StartingProficiencies = StartingProficiencies - Brawling
                print("You have " + str(StartingProficiencies) + " Points left.")
                print("o==[=========> <=========]==o")
                
                #Have player set their character's Cut & Thrust, loop until get a number from 0 - 12.
                while True:
                    try:
                        print("Cut and Thrust - This proficiency refers to swords that are usually not wielded in conjuction with a larger shield, but rather in quick fencing style.")
                        Cut = int(input("How many points will you assign to Cut & Thrust? You can assign between 0 and 12 Points.\n>"))
                    except ValueError:
                        print("Sorry, I didn't understand that!")
                        continue
                    if Cut < 0 or Cut > 12:
                        print("You can assign between 0 and 12 Points.")
                        continue
                    elif StartingProficiencies - Cut < 0:
                        print("You only have 11 Points!")
                        continue
                    else:
                        break
                StartingProficiencies = StartingProficiencies - Cut
                print("You have " + str(StartingProficiencies) + " Points left.")
                print("o==[=========> <=========]==o")
                
                #Have player set their character's Dagger, loop until get a number from 0 - 12.
                while True:
                    try:
                        print("Dagger - Found in every place in the world, daggers and knives are used as both tools and instruments of death.")
                        Dagger = int(input("How many points will you assign to Dagger? You can assign between 0 and 12 Points.\n>"))
                    except ValueError:
                        print("Sorry, I didn't understand that!")
                        continue
                    if Dagger < 0 or Dagger > 12:
                        print("You can assign between 0 and 12 Points.")
                        continue
                    elif StartingProficiencies - Dagger < 0:
                        print("You only have 11 Points!")
                        continue
                    else:
                        break
                StartingProficiencies = StartingProficiencies - Dagger
                print("You have " + str(StartingProficiencies) + " Points left.")
                print("o==[=========> <=========]==o")
                
                #Have player set their character's Greatsword, loop until get a number from 0 - 12.
                while True:
                    try:
                        print("Greatsword - Frequently wielded with a wide, half-swording grip. Greatswords are fearsome weapons with great range, but easily overcome by any fighter agile enough to get close.")
                        Greatsword = int(input("How many points will you assign to Greatsword? You can assign between 0 and 12 Points.\n>"))
                    except ValueError:
                        print("Sorry, I didn't understand that!")
                        continue
                    if Greatsword < 0 or Greatsword > 12:
                        print("You can assign between 0 and 12 Points.")
                        continue
                    elif StartingProficiencies - Greatsword < 0:
                        print("You only have 11 Points!")
                        continue
                    else:
                        break
                StartingProficiencies = StartingProficiencies - Greatsword
                print("You have " + str(StartingProficiencies) + " Points left.")
                print("o==[=========> <=========]==o")
                
                #Have player set their character's Longsword, loop until get a number from 0 - 12.
                while True:
                    try:
                        print("Longsword - For those warriors that prefer not to use shields, longswords are very polular. They are a fierce weapon, capable of heavy damage when either cleaving or thrusting, as well as complex maneuvering and countering.")
                        Longsword = int(input("How many points will you assign to Longsword? You can assign between 0 and 12 Points.\n>"))
                    except ValueError:
                        print("Sorry, I didn't understand that!")
                        continue
                    if Longsword < 0 or Longsword > 12:
                        print("You can assign between 0 and 12 Points.")
                        continue
                    elif StartingProficiencies - Longsword < 0:
                        print("You only have 11 Points!")
                        continue
                    else:
                        break
                StartingProficiencies = StartingProficiencies - Longsword
                print("You have " + str(StartingProficiencies) + " Points left.")
                print("o==[=========> <=========]==o")
                
                #Have player set their character's Mass Weapon & Shield, loop until get a number from 0 - 12.
                while True:
                    try:
                        print("Mass Weapon & Shield - Mass weapons include any single-handed (and occasionally two-handed) weapon that is particularly heavy on the end. These weapon's balance makes them slow on the parry and commends the use of constant evasion or - more commonly - shields.")
                        Mass = int(input("How many points will you assign to Mass Weapon & Shield? You can assign between 0 and 12 Points.\n>"))
                    except ValueError:
                        print("Sorry, I didn't understand that!")
                        continue
                    if Mass < 0 or Mass > 12:
                        print("You can assign between 0 and 12 Points.")
                        continue
                    elif StartingProficiencies - Mass < 0:
                        print("You only have 11 Points!")
                        continue
                    else:
                        break
                StartingProficiencies = StartingProficiencies - Mass
                print("You have " + str(StartingProficiencies) + " Points left.")
                print("o==[=========> <=========]==o")

                #Have player set their character's Pole-arm, loop until get a number from 0 - 12.
                while True:
                    try:
                        print("Pole-Arms - A wide range of weapons from the Spear to the Halberd.")
                        Pole = int(input("How many points will you assign to Pole-arms? You can assign between 0 and 12 Points.\n>"))
                    except ValueError:
                        print("Sorry, I didn't understand that!")
                        continue
                    if Pole < 0 or Pole > 12:
                        print("You can assign between 0 and 12 Points.")
                        continue
                    elif StartingProficiencies - Pole < 0:
                        print("You only have 11 Points!")
                        continue
                    else:
                        break
                StartingProficiencies = StartingProficiencies - Pole
                print("You have " + str(StartingProficiencies) + " Points left.")
                print("o==[=========> <=========]==o")

                        #Have player set their character's Spear & Shield, loop until get a number from 0 - 12.
                while True:
                    try:
                        print("Spear and Shield - Covers the use of one-handed spears and shields.")
                        Spear = int(input("How many points will you assign to Spear & Shield? You can assign between 0 and 12 Points.\n>"))
                    except ValueError:
                        print("Sorry, I didn't understand that!")
                        continue
                    if Spear < 0 or Spear > 12:
                        print("You can assign between 0 and 12 Points.")
                        continue
                    elif StartingProficiencies - Spear < 0:
                        print("You only have 11 Points!")
                        continue
                    else:
                        break
                StartingProficiencies = StartingProficiencies - Spear
                print("You have " + str(StartingProficiencies) + " Points left.")
                print("o==[=========> <=========]==o")

                        #Have player set their character's Sword & Shield, loop until get a number from 0 - 12.
                while True:
                    try:
                        print("Sword and Shield - This Proficiency involves any one-handed sword and a shield. Although this proficiency could be used without a shield at no penalty.")
                        Sword = int(input("How many points will you assign to Sword & Shield? You can assign between 0 and 12 Points.\n>"))
                    except ValueError:
                        print("Sorry, I didn't understand that!")
                        continue
                    if Sword < 0 or Sword > 12:
                        print("You can assign between 0 and 12 Points.")
                        continue
                    elif StartingProficiencies - Sword < 0:
                        print("You only have 11 Points!")
                        continue
                    else:
                        break
                StartingProficiencies = StartingProficiencies - Sword
                print("You have " + str(StartingProficiencies) + " Points left.")
                print("o==[=========> <=========]==o")

                        #Have player set their character's Wrestling, loop until get a number from 0 - 12.
                while True:
                    try:
                        print("Wrestling - As with Brawling, Wrestling is always an option for the unarmed character.")
                        Wrestling = int(input("How many points will you assign to Wrestling? You can assign between 0 and 12 Points.\n>"))
                    except ValueError:
                        print("Sorry, I didn't understand that!")
                        continue
                    if Wrestling < 0 or Wrestling > 12:
                        print("You can assign between 0 and 12 Points.")
                        continue
                    elif StartingProficiencies - Wrestling < 0:
                        print("You only have 11 Points!")
                        continue
                    else:
                        break
                StartingProficiencies = StartingProficiencies - Wrestling
                
            except ValueError:
                print("Sorry, I didn't understand that!")
                continue
            if StartingProficiencies < 0:
                print("You only have 11 points!")
                continue
            else:
                break

        #Define the Player, based on Basic Attributes, Combined Attributes, Proficiencies, and Pools.
        Player = CurrentCharacter("Stuart", Brawn, Daring, Tenacity, Heart, Sagacity, Cunning, Reflex, Aim, Knockdown, Knockout, Brawling, Cut, Dagger, Greatsword, Longsword, Mass, Pole, Spear, Sword, Wrestling)

        #Print Character Sheet.
        print("o==[=========> <=========]==o")
        print("Primary Attributes")
        print("o==[=========> <=========]==o")
        print("Brawn = " + str(Player.brawn))
        print("Daring = " + str(Player.daring))
        print("Tenacity = " + str(Player.tenacity))
        print("Heart = " + str(Player.heart))
        print("Sagacity = " + str(Player.sagacity))
        print("Cunning = " + str(Player.cunning))
        print("o==[=========> <=========]==o")
        print("Combined Attributes")
        print("o==[=========> <=========]==o")
        print("Reflex = " + str(int(Player.reflex)))
        print("Aim = " + str(int(Player.aim)))
        print("Knockdown = " + str(int(Player.knockdown)))
        print("Knockout = " + str(int(Player.knockout)))
        print("o==[=========> <=========]==o")
        print("Weapon Proficiencies")
        print("o==[=========> <=========]==o")
        print("Brawling = " + str(int(Player.brawling)))
        print("Cut & Thrust = " + str(int(Player.cut)))
        print("Dagger = " + str(int(Player.dagger)))
        print("Greatsword = " + str(int(Player.greatsword)))
        print("Longsword = " + str(int(Player.longsword)))
        print("Mass Weapon & Shield = " + str(int(Player.mass)))
        print("Pole-arm = " + str(int(Player.pole)))
        print("Spear & Shield = " + str(int(Player.spear)))
        print("Sword & Shield = " + str(int(Player.sword)))
        print("Wrestling = " + str(int(Player.wrestling)))

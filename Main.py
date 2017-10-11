import random
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

#Create the Melee Weapons Table
Hand = 1
Short = 2
Medium = 3
Long = 4
VeryLong = 5
ExtremelyLong = 6

MeleeWeapons = {
                1 : { "name" : "Short Sword" ,
                      "description" : "A sword with a short, two-edged blade." ,
                      "reach" : Short,
                      "sATN" : 6,
                      "sDR" : 0,
                      "tATN" : 6,
                      "tDR" : 1,
                      "DTN" : 7,
                      "bDR" : -2,
                      "Proficiency" : [Cut, Sword]} ,

                2 : { "name" : "Arming Sword" ,
                      "description" : "The basic, run-of-the-mill one-handed sword." ,
                      "reach" : Medium,
                      "sATN" : 7,
                      "sDR" : 1,
                      "tATN" : 7,
                      "tDR" : 1,
                      "DTN" : 7,
                      "bDR" : -1} ,

                3 : { "name" : "Hand-and-a-Half, Two-Handed" ,
                      "description" : "An arming sword with a slightly longer blade and hilt long enough to accomodate both hands." ,
                      "reach" : Medium,
                      "sATN" : 7,
                      "sDR" : 2,
                      "tATN" : 7,
                      "tDR" : 1,
                      "DTN" : 6,
                      "bDR" : 0} ,
                
                3.5 : { "name" : "Hand-and-a-Half, One-Handed" ,
                        "description" : "An arming sword with a slightly longer blade and hilt long enough to accomodate both hands." ,
                        "reach" : Long,
                        "sATN" : 8,
                        "sDR" : 2,
                        "tATN" : 8,
                        "tDR" : 1,
                        "DTN" : 8,
                        "bDR" : 0} ,

                4 : { "name" : "Greatsword" ,
                      "description" : "A hand-and-a-half sword with a longer blade, intended soley for use with both hands." ,
                      "reach" : VeryLong,
                      "sATN" : 8,
                      "sDR" : 3,
                      "tATN" : 8,
                      "tDR" : 1,
                      "DTN" : 8,
                      "bDR" : 1} ,

                5 : { "name" : "Falchion, One-Handed" ,
                      "description" : "An arming sword with a slightly longer hilt and a heavy, broad blade, it's back straight and blunt and its one edge curved." ,
                      "reach" : Medium,
                      "sATN" : 8,
                      "sDR" : 2,
                      "tATN" : 10,
                      "tDR" : 0,
                      "DTN" : 9,
                      "bDR" : -1,
                      "armorsDR" : 1} ,

                5.5 : { "name" : "Falchion, Two-Handed" ,
                        "description" : "An arming sword with a slightly longer hilt and a heavy, broad blade, it's back straight and blunt and its one edge curved." ,
                        "reach" : Short,
                        "sATN" : 7,
                        "sDR" : 2,
                        "tATN" : 9,
                        "tDR" : 0,
                        "DTN" : 7,
                        "bDR" : -1,
                        "armorsDR" : 1} ,

                6 : { "name" : "Sidesword" ,
                      "description" : "An arming sword with a slender blade of stiff diamond cross-section tapering to an acute point." ,
                      "reach" : Medium,
                      "sATN" : 6,
                      "sDR" : -1,
                      "tATN" : 7,
                      "tDR" : 1,
                      "DTN" : 6,
                      "bDR" : -2,
                      "AC" : -1,
                      "metalsDR" : -1,
                      "metaltDR" : -1,
                      "notes" : "DTN is increased by +1 against two-handed and heavy one-handed swords, by +2 against light pole-arms and one-handed mass weapons, and by +3 against heavy pole-arms and two-handed mass weapons."} ,

                7 : { "name" : "Rapier" ,
                      "description" : "A sidesword with a somewhat longer but even more slender blade, tapering for much of its length to a very acute point." ,
                      "reach" : Long,
                      "sATN" : 6,
                      "sDR" : -3,
                      "tATN" : 8,
                      "tDR" : 1,
                      "DTN" : 6,
                      "bDR" : -3,
                      "metalsDR" : -2,
                      "metaltDR" : -2,
                      "leathersDR" : -1,
                      "leathertDR" : -1,
                      "notes" : "DTN is increased by +1 against daggers and sideswords, by +2 against one-handed swords, by +3 against two-handed and heavy one-handed swords, by +4 against light pole-arms and one-handed mass weapons, and by +5 against heavy pole-arms and two-handed mass weapons. The point will break on any connecting swing against armor better than gambeson or pliable leather unreinforced by metal, reducing Reach to Medium and Thrust DR to 0."} ,

                8 : { "name" : "Saber" ,
                      "description" : "A one edged arming sword with a slight to moderate back-curve." ,
                      "reach" : Medium,
                      "sATN" : 7,
                      "sDR" : 1,
                      "tATN" : 8,
                      "tDR" : 1,
                      "DTN" : 7,
                      "bDR" : -1,
                      "swingAC" : -1,
                      "armorsDR" : -1} ,

                9 : { "name" : "Scimitar" ,
                      "description" : "A saber with a more pronounced back-curve." ,
                      "reach" : Medium,
                      "sATN" : 7,
                      "sDR" : 1,
                      "tATN" : 9,
                      "tDR" : 1,
                      "DTN" : 7,
                      "bDR" : -1,
                      "swingAC" : -1,
                      "armorsDR" : -1} ,

                10 : { "name" : "Dao" ,
                       "description" : "A far Eastern type of saber with a slight flare towards the - rather blunt - point of the blade." ,
                       "reach" : Medium,
                       "sATN" : 8,
                       "sDR" : 2,
                       "tATN" : 9,
                       "tDR" : 0,
                       "DTN" : 7,
                       "bDR" : 0,
                       "DefAC" : 1} ,

                11 : { "name" : "Katana, Two-Handed" ,
                       "description" : "A far Eastern hand-and-a-half sword with a long hilt and a one-edged, back-curved blade." ,
                       "reach" : Medium,
                       "sATN" : 7,
                       "sDR" : 2,
                       "tATN" : 8,
                       "tDR" : 1,
                       "DTN" : 6,
                       "bDR" : -1,
                       "swingAC" : -1,
                       "armorsDR" : -1} ,

                11.5 : { "name" : "Katana, One-Handed" ,
                         "description" : "A far Eastern hand-and-a-half sword with a long hilt and a one-edged, back-curved blade." ,
                         "reach" : Long,
                         "sATN" : 8,
                         "sDR" : 2,
                         "tATN" : 9,
                         "tDR" : 1,
                         "DTN" : 8,
                         "bDR" : -1,
                         "swingAC" : -1,
                         "armorsDR" : -1} ,

                12 : { "name" : "Wakizashi" ,
                       "description" : "A short sword with a blade of the Katana type." ,
                       "reach" : Short,
                       "sATN" : 6,
                       "sDR" : 1,
                       "tATN" : 7,
                       "tDR" : 1,
                       "DTN" : 7,
                       "bDR" : -2,
                       "swingAC" : -1,
                       "armorsDR" : -1} ,

                13 : { "name" : "Kopis" ,
                       "description" : "An ancient Greek one-edged short sword with a forward curve and a slight flare to the blade before it tapers to a point." ,
                       "reach" : Short,
                       "sATN" : 7,
                       "sDR" : 1,
                       "tATN" : 6,
                       "tDR" : 1,
                       "DTN" : 7,
                       "bDR" : -1,
                       "DefAC" : 1,
                       "tOffAC" : 1} ,

                14 : { "name" : "Gladius" ,
                       "description" : "An ancient Roman short sword with a stiff diamond cross-section and edges either parallel for most of its length before tapering to an acute point, or else of more slightly flaring xiphos-type." ,
                       "reach" : Short,
                       "sATN" : 6,
                       "sDR" : 0,
                       "tATN" : 6,
                       "tDR" : 1,
                       "DTN" : 7,
                       "bDR" : -2,
                       "armortDR" : 1} ,

                15 : { "name" : "Spatha" ,
                       "description" : "The ancient Roman version of the arming sword, tapering slightly along most of its length before suddenly tapering to an acute point." ,
                       "reach" : Medium,
                       "sATN" : 7,
                       "sDR" : 1,
                       "tATN" : 7,
                       "tDR" : 1,
                       "DTN" : 7,
                       "bDR" : -1,
                       "tOffAC" : 1} ,

                16 : { "name" : "Viking Sword" ,
                       "description" : "The Viking version of the Roman spatha, with a less acute point." ,
                       "reach" : Medium,
                       "sATN" : 7,
                       "sDR" : 1,
                       "tATN" : 7,
                       "tDR" : 1,
                       "DTN" : 7,
                       "bDR" : -1} ,

                17 : { "name" : "Dagger" ,
                       "description" : "A straight fighting knife with a substantial blade, usually two-edged." ,
                       "reach" : Hand,
                       "sATN" : 6,
                       "sDR" : -1,
                       "tATN" : 5,
                       "tDR" : 0,
                       "DTN" : 9,
                       "bDR" : -3} ,

                18 : { "name" : "Stiletto" ,
                       "description" : "A dagger with a slender blade of very stiff diamond cross-section, tapering to a very acute point." ,
                       "reach" : Hand,
                       "sATN" : 6,
                       "sDR" : -2,
                       "tATN" : 5,
                       "tDR" : 0,
                       "DTN" : 9,
                       "bDR" : -4,
                       "armortDR" : 1} ,

                19 : { "name" : "Parrying Dagger" ,
                       "description" : "A dagger, usually with a slightly more slender blade, but a very broad and sturdy cross-guard." ,
                       "reach" : Hand,
                       "sATN" : 6,
                       "sDR" : -1,
                       "tATN" : 5,
                       "tDR" : 0,
                       "DTN" : 6,
                       "bDR" : -4,
                       "OffAC" : 1,
                       "notes" : "The DTN is increased by +1 against one-handed swords, by +2 against two-handed and heavy one-handed swords, by +3 against light pole-arms and one-handed mass weapons, and by +4 against heavy pole-arms and two-handed mass weapons."} ,


                20 : { "name" : "Club" ,
                       "description" : "A stout stick, thicker at the business end." ,
                       "reach" : Short,
                       "sATN" : 6,
                       "sDR" : 1,
                       "tATN" : 7,
                       "tDR" : -1,
                       "DTN" : 9,
                       "bDR" : 1,
                       "shock" : 1} ,

                21 : { "name" : "Mace" ,
                       "description" : "A stout stick with a head bound in metal or wholly made of metal or sometimes stone." ,
                       "reach" : Short,
                       "sATN" : 6,
                       "sDR" : 1,
                       "tATN" : 7,
                       "tDR" : -1,
                       "DTN" : 9,
                       "bDR" : 1,
                       "shock" : 1,
                       "OffAC" : 1} ,

                22 : { "name" : "Flanged Mace" ,
                       "description" : "A mace with flanges to the sides of the head, optimized to transfer damage through armor." ,
                       "reach" : Short,
                       "sATN" : 6,
                       "sDR" : 1,
                       "tATN" : 7,
                       "tDR" : -1,
                       "DTN" : 9,
                       "bDR" : 1,
                       "shock" : 1,
                       "OffAC" : 1,
                       "armorsDR" : 1} ,

                23 : { "name" : "Spiked Mace" ,
                       "description" : "A mace with spikes for tearing grisly wounds." ,
                       "reach" : Short,
                       "sATN" : 6,
                       "sDR" : 1,
                       "tATN" : 7,
                       "tDR" : -1,
                       "DTN" : 9,
                       "bDR" : 1,
                       "shock" : 1,
                       "pain" : 1,
                       "BL" : 1,
                       "OffAC" : 1,
                       "armorsDR" : -1} ,

                24 : { "name" : "War-Flail" ,
                       "description" : "A long staff with a much shorter, metal-shod stick with spikes all around affixed to its end by a very short length of chain; wielded with two hands." ,
                       "reach" : VeryLong,
                       "sATN" : 7,
                       "sDR" : 2,
                       "DTN" : 8,
                       "bDR" : 2,
                       "sOffAC" : 1,
                       "shock" : 1,
                       "pain" : 1,
                       "BL" : 1,
                       "parry" : -1} ,

                25 : { "name" : "Hatchet" ,
                       "description" : "An axe with a short haft." ,
                       "reach" : Hand,
                       "sATN" : 6,
                       "sDR" : 0,
                       "DTN" : 8,
                       "bDR" : -1} ,

                26 : { "name" : "Hand-Axe" ,
                       "description" : "A hatchet with a longer haft an slightly larger head." ,
                       "reach" : Short,
                       "sATN" : 7,
                       "sDR" : 1,
                       "DTN" : 9,
                       "bDR" : 0,
                       "armorsDR" : 1} ,

                27 : { "name" : "Long-Hafted Axe, One-Handed" ,
                       "description" : "An axe with a much longer handle and maybe a slightly larger head." ,
                       "reach" : Medium,
                       "sATN" : 7,
                       "sDR" : 1,
                       "DTN" : 9,
                       "bDR" : 0,
                       "armorsDR" : 1,
                       "shock" : 1,
                       "switch" : 1} ,

                27.3 : { "name" : "Long-Hafted Axe, Two-Handed" ,
                         "description" : "An axe with a much longer handle and maybe a slightly larger head." ,
                         "reach" : Medium,
                         "sATN" : 7,
                         "sDR" : 2,
                         "DTN" : 7,
                         "bDR" : 1,
                         "armorsDR" : 1,
                         "shock" : 1,
                         "switch" : 1} ,

                27.6 : { "name" : "Long-Hafted Axe, Two-Handed" ,
                         "description" : "An axe with a much longer handle and maybe a slightly larger head." ,
                         "reach" : Long,
                         "sATN" : 8,
                         "sDR" : 3,
                         "DTN" : 8,
                         "bDR" : 2,
                         "armorsDR" : 1,
                         "shock" : 1,
                         "switch" : 1} ,

                28 : { "name" : "Great Axe" ,
                       "description" : "A long-hafted axe with perhaps a slightly longer haft and a bigger head, to be wielded with both hands." ,
                       "reach" : Medium,
                       "sATN" : 7,
                       "sDR" : 2,
                       "DTN" : 7,
                       "bDR" : 1} ,
                
                28.5 : { "name" : "Great Axe" ,
                         "description" : "A long-hafted axe with perhaps a slightly longer haft and a bigger head, to be wielded with both hands." ,
                         "reach" : Long,
                         "sATN" : 8,
                         "sDR" : 4,
                         "DTN" : 9,
                         "bDR" : 2} ,

                29 : { "name" : "War-Hammer, Hammerhead" ,
                       "description" : "A warhammer with a rather small, but powerful head, often with a beak opposite it." ,
                       "reach" : Short,
                       "sATN" : 6,
                       "sDR" : 1,
                       "tATN" : 8,
                       "tDR" : -1,
                       "DTN" : 9,
                       "bDR" : 1,
                       "switch" : 1,
                       "armorsDR" : 1,
                       "shock" : 1} ,
                
                29.5 : { "name" : "War-Hammer, Beak" ,
                         "description" : "A warhammer with a rather small, but powerful head, often with a beak opposite it." ,
                         "reach" : Short,
                         "sATN" : 7,
                         "sDR" : 1,
                         "tATN" : 8,
                         "tDR" : -1,
                         "DTN" : 9,
                         "bDR" : 1,
                         "switch" : 1,
                         "armorsDR" : 1} ,

                30 : { "name" : "Quarterstaff" ,
                       "description" : "A stout staff, as tall as its wielder or slightly taller." ,
                       "reach" : [Medium, Long],
                       "sATN" : 6,
                       "sDR" : 0,
                       "tATN" : 6,
                       "tDR" : 0,
                       "DTN" : 5,
                       "bDR" : 0,
                       "tOffAC" : 1,
                       "notes" : "Can equally be used at Medium and Long Reach at the same time."} ,

                31 : { "name" : "Short Spear, One-Handed" ,
                       "description" : "A spear, as tall as its wielder or slightly shorter." ,
                       "reach" : Medium,
                       "sATN" : 8,
                       "sDR" : 0,
                       "tATN" : 7,
                       "tDR" : 1,
                       "DTN" : 7,
                       "bDR" : 0,
                       "switch" : 1} ,

                31.5 : { "name" : "Short Spear, Two-Handed" ,
                         "description" : "A spear, as tall as its wielder or slightly shorter." ,
                         "reach" : Medium,
                         "sATN" : 0,
                         "sDR" : 0,
                         "tATN" : 6,
                         "tDR" : 1,
                         "DTN" : 6,
                         "bDR" : 0,
                         "switch" : 1} ,

                32 : { "name" : "Long Spear, One-Handed" ,
                       "description" : "A spear, significantly taller than its wielder." ,
                       "reach" : Long,
                       "sATN" : 9,
                       "sDR" : 0,
                       "tATN" : 8,
                       "tDR" : 1,
                       "DTN" : 8,
                       "bDR" : 0,
                       "switch" : 1} ,

                32.5 : { "name" : "Long Spear, Two-Handed" ,
                         "description" : "A spear, significantly taller than its wielder." ,
                         "reach" : [Medium, Long],
                         "sATN" : 0,
                         "sDR" : 0,
                         "tATN" : 6,
                         "tDR" : 1,
                         "DTN" : 6,
                         "bDR" : 0,
                         "switch" : 1} ,

                33 : { "name" : "Halberd, Axe-Blade" ,
                       "description" : "A long spear with an axe-blade and a spike opposite that." ,
                       "reach" : VeryLong,
                       "sATN" : 8,
                       "sDR" : 4,
                       "tATN" : 7,
                       "tDR" : 1,
                       "DTN" : 7,
                       "bDR" : 2,
                       "OffAC" : 1,
                       "DefAC" : 1,
                       "switch" : 1,
                       "armorsDR" : 1} ,

                33.5 : { "name" : "Halberd, Back-Spike" ,
                         "description" : "A long spear with an axe-blade and a spike opposite that." ,
                         "reach" : VeryLong,
                         "sATN" : 8,
                         "sDR" : 4,
                         "tATN" : 7,
                         "tDR" : 1,
                         "DTN" : 7,
                         "bDR" : 0,
                         "OffAC" : 1,
                         "DefAC" : 1,
                         "switch" : 1,
                         "armorsDR" : 1} ,

                34 : { "name" : "Naginata" ,
                       "description" : "A long spear with a long, one-edged, slightly curved blade, used with two hands for mostly slashing attacks." ,
                       "reach" : [Long, VeryLong],
                       "sATN" : 8,
                       "sDR" : 3,
                       "tATN" : 6,
                       "tDR" : 1,
                       "DTN" : 6,
                       "bDR" : 0,
                       "tOffAC" : 1,
                       "armortDR" : -1} ,
               }

#Decide what type of game you will be playing. For now there is just Gladiator
GameType = input("What type of game do you want to play? For now there is only Gladiator.\n>")
if GameType == "Gladiator":
    #Create a dictionary of rooms.
    Rooms = {
                1 : { "name" : "the Preparation Room"},

                2 : { "name" : "the Arena"}
            }
    #Set the player in the first room.
    currentRoom = 1
    print("You find yourself in the preparation room beneath the Arena. You hear the roar of the crowd above you.")
    print("o==[=========> <=========]==o")

    #Create an Inventory, which is initailly empty.
    Weapon = []
    

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

    #Loop until dead.
    Dead = False
    while Dead == False:

        #Get the player's next 'command'
        command = input("o==[=========>").lower().split()

        #If player dies, game ends.
        if Dead == True:
            print("You died!")
            break

class MeleeWeapon:
    def __init__(self, name, description, reach, sATN, sDR, tATN, tDR, DTN, bDR, armorsDR, armortDR, metalsDR, metaltDR, leathersDR, leathertDR, AC, OffAC, sOffAC, tOffAC, DefAC, shock, pain, BL, parry, switch1, switch2):
        self.name = name
        self.description = description
        self.reach = reach
        self.sATN = sATN
        self.tDR = sDR
        self.tATN = tATN
        self.tDR = tDR
        self.DTN = DTN
        self.bDR = bDR
        self.armorsDR = armorsDR
        self.armortDR = armortDR
        self.metalsDR = metalsDR
        self.metaltDR = metaltDR
        self.leathersDR = leathersDR
        self.leathertDR = leathertDR
        self.AC
        self.OffAC = OffAC
        self.sOffAC = sOffAC
        self.tOffAC = tOffAC
        self.DefAC = DefAC
        self.shock = shock
        self.pain = pain
        self.BL = BL
        self.parry = parry
        self.switch1 = switch1
        self.switch2 = switch2

x = print("The weapon doesn't have that stat.")

ShortSword = MeleeWeapon("Short Sword", "A sword with a short, two-edged blade.", 2, 6, 0, 6, 1, 7, -2, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x)
ArmingSword = MeleeWeapon("Arming Sword", "The basic, run-of-the-mill one-handed sword.", 3, 7, 1, 7, 1, 7, -1, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x)
HandandaHalf2h = MeleeWeapon("Hand-and-a-Half, Two-Handed", "An arming sword with a slightly longer blade and hilt long enough to accomodate both hands.", 3, 7, 2, 7, 1, 6, 0, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1, x)
HandandaHalf1h = MeleeWeapon("Hand-and-a-Half, One-Handed", "An arming sword with a slightly longer blade and hilt long enough to accomodate both hands.", 4, 8, 2, 8, 1, 8, 0, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1, x)
Greatsword = MeleeWeapon("Greatsword", "A hand-and-a-half sword with a longer blade, intended soley for use with both hands.", 5, 8, 3, 8, 1, 8, 1, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x)
Falchion1h = MeleeWeapon("Falchion, One-Handed", "An arming sword with a slightly longer hilt and a heavy, broad blade, it's back straight and blunt and its one edge curved.", 3, 8, 2, 10, 0, 9, -1, 1, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1, x)
Falchion2h = MeleeWeapon("Falchion, Two-Handed", "An arming sword with a slightly longer hilt and a heavy, broad blade, it's back straight and blunt and its one edge curved.", 2, 7, 2, 9, 0, 7, -1, 1, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1, x)
Sidesword = MeleeWeapon("Sidesword", "An arming sword with a slender blade of stiff diamond cross-section tapering to an acute point.", 3, 6, -1, 7, 1, 6, -2, x, x, -1, -1, x, x, -1, x, x, x, x, x, x, x, x, x, x)
Rapier = MeleeWeapon("Rapier", "A sidesword with a somewhat longer but even more slender blade, tapering for much of its length to a very acute point.", 4, 6, -3, 8, 1, 6, -3, x, x, -2, -2, -1, -1, x, x, x, x, x, x, x, x, x, x, x)
Saber = MeleeWeapon("Saber", "A one edged arming sword with a slight to moderate back-curve.", 3, 7, 1, 8, 1, 7, -1, -1, x, x, x, x, x, x, x, -1, x, x, x, x, x, x, x, x)
Scimitar = MeleeWeapon("Scimitar", "A saber with a more pronounced back-curve.", 3, 7, 1, 9, 1, 7, -1, -1, x, x, x, x, x, x, x, -1, x, x, x, x, x, x, x, x)
Dao = MeleeWeapon("Dao", "A far Eastern type of saber with a slight flare towards the - rather blunt - point of the blade.", 3, 8, 2, 9, 0, 7, 0, x, x, x, x, x, x, x, x, x, x, 1, x, x, x, x, x, x)
Katana2h = MeleeWeapon("Katana, Two-Handed", "A far Eastern hand-and-a-half sword with a long hilt and a one-edged, back-curved blade.", 3, 7, 2, 8, 1, 6, -1, -1, x, x, x, x, x, x, x, -1, x, x, x, x, x, x, 1, x)
Katana1h = MeleeWeapon("Katana, One-Handed", "A far Eastern hand-and-a-half sword with a long hilt and a one-edged, back-curved blade.", 4, 8, 2, 9, 1, 8, -1, -1, x, x, x, x, x, x, x, -1, x, x, x, x, x, x, 1, x)
MeleeWeapon(name, description, reach, sATN, sDR, tATN, tDR, DTN, bDR, armorsDR, armortDR, metalsDR, metaltDR, leathersDR, leathertDR, AC, OffAC, sOffAC, tOffAC, DefAC, shock, pain, BL, parry, switch1, switch2)
MeleeWeapon(name, description, reach, sATN, sDR, tATN, tDR, DTN, bDR, armorsDR, armortDR, metalsDR, metaltDR, leathersDR, leathertDR, AC, OffAC, sOffAC, tOffAC, DefAC, shock, pain, BL, parry, switch1, switch2)
MeleeWeapon(name, description, reach, sATN, sDR, tATN, tDR, DTN, bDR, armorsDR, armortDR, metalsDR, metaltDR, leathersDR, leathertDR, AC, OffAC, sOffAC, tOffAC, DefAC, shock, pain, BL, parry, switch1, switch2)
MeleeWeapon(name, description, reach, sATN, sDR, tATN, tDR, DTN, bDR, armorsDR, armortDR, metalsDR, metaltDR, leathersDR, leathertDR, AC, OffAC, sOffAC, tOffAC, DefAC, shock, pain, BL, parry, switch1, switch2)
MeleeWeapon(name, description, reach, sATN, sDR, tATN, tDR, DTN, bDR, armorsDR, armortDR, metalsDR, metaltDR, leathersDR, leathertDR, AC, OffAC, sOffAC, tOffAC, DefAC, shock, pain, BL, parry, switch1, switch2)
MeleeWeapon(name, description, reach, sATN, sDR, tATN, tDR, DTN, bDR, armorsDR, armortDR, metalsDR, metaltDR, leathersDR, leathertDR, AC, OffAC, sOffAC, tOffAC, DefAC, shock, pain, BL, parry, switch1, switch2)
MeleeWeapon(name, description, reach, sATN, sDR, tATN, tDR, DTN, bDR, armorsDR, armortDR, metalsDR, metaltDR, leathersDR, leathertDR, AC, OffAC, sOffAC, tOffAC, DefAC, shock, pain, BL, parry, switch1, switch2)

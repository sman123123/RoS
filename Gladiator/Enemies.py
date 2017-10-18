import random
class Enemy:
    def __init__(self, name, brawn, daring, tenacity, heart, sagacity, cunning, reflex, aim, knockdown, knockout, proficiency, MP):
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
        self.proficiency = proficiency
        self.MP = MP
        
#Reflex = (Cunning + Daring)/2
#Aim = (Sagacity + Cunning)/2
#Knockdown = (Brawn + Daring)/2
#Knockout = (Brawn + Tenacity)/2
        
RandBN = random.randint(4, 5)
if RandBN == 4:
    RandDG = 5
    RandKD = 5
    RandKO = 4
elif RandBN == 5:
    RandDG = 4
    RandKD = 5
    RandKO = 5
RandHT = random.randint(3, 4)
if RandHT == 3:
    RandSY = 4
elif RandHT == 4:
    RandSY = 3
if RandDG == 4:
    RandRef = 4
elif RandDG == 5:
    RandRef = 5
RandProf = random.randint(4, 5)
RandMP = RandProf + RandRef

Slave = Enemy("Slave", RandBN, RandDG, 4, RandHT, RandSY, 4, RandRef, 4, RandKD, RandKO, RandProf, RandMP)

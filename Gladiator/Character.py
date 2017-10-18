class CurrentCharacter:
    def __init__(self, name, brawn, daring, tenacity, heart, sagacity, cunning, reflex, aim, knockdown, knockout, proficiency):
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
#Reflex = (Cunning + Daring)/2
#Aim = (Sagacity + Cunning)/2
#Knockdown = (Brawn + Daring)/2
#Knockout = (Brawn + Tenacity)/2

Soldier = CurrentCharacter("Soldier", 5, 5, 4, 4, 3, 4, 5, 4, 5, 5, 5)

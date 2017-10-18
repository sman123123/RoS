class Armor:
    def __init__(self, name, description, pAV, bAV, cAV):
        self.name = name
        self.description = description
        self.pAV = pAV
        self.bV = bAV
        self.cAV = cAV

Gambeson = Armor("Gambeson", "Pliable textile armor made of a number of layers of quilted cloth and stuffed with cotton, animal hair, or other padding.", 1, 2, 2)
Leather = Armor("Leather", "Tough, yet pliable, cured hide.", 2, 1, 2)
LeatherMetal = Armor("Leather with Metal", "Pliable leather with short metal strips or rings sewn in strategic places to guard against cuts.", 2, 1, 3)
HardenedLeather = Armor("Hardened Leather", "Cured hide boiled and then dried to make it harder, at the cost of pliability. It can be fashioned into segments large enough to serve as helmets and greaves, but not for workable breastplates.", 3, 2, 2)
LeatherLamellar = Armor("Leather Lamellar", "Strips of leather with holes fashioned into its edges and that are bound together and overlapped by neighboring pieces. Leather Lamellar is quite rigid and cannot be used to protect a joint. Requires wearing a gambeson underneath.", 3, 3, 3)

class MetalArmor:
    def __init__(self, name, description, pAV, bAV):
        self.name = name
        self.description = description
        self.pAV = pAV
        self.bV = bAV

MetalLamellar = MetalArmor("Metal Lamellar", "Much like Leather Lamellar but with metal plates instead of leather.", 4, 4)
Brigandine = MetalArmor("Brigandine", "Armor made of palm- to hand-sized metal plates, each sandwiched between two layers of heavy canvas or soft leather and riveted together. Brigandine is quite rigid and cannot be used to protect a joint. Requires wearing a gambeson underneath.", 4, 4)
Mail = MetalArmor("Mail", "This armor consists of a mesh of small metal rings, each interlinked with neighboring rings. It is supremely pliable and can therefore be used to protect joints, but it too requires a gambeson to be worn underneath", 4, 3)
BrigandineMail = MetalArmor("Brigandine over Mail", "A special blend of layering armors, this was common during the transitional period from maille to plate, and consists of maille with additional brigandine worn over it to protect the torso from shoulder to hip.", 5, 3)
PlatePieces = MetalArmor("Plate Pieces", "Thinner plate pieces used to protect the limbs.", 6, 4)
ArticulatedPlate = MetalArmor("Articulated Plate", "Thicker plate pieces used for helmets and breastplates.", 7, 5)

class Shield:
    def __init__(self, name, description, mDTN, tDTN, pDTN):
        self.name = name
        self.description = description
        self.mDTN = mDTN
        self.tDTN = tDTN
        self.pDTN = pDTN

Buckler = Shield("Buckler", "A very small round shield strapped to the forearm so that the hand is still usable.", 7, 8, 11)
SmallShield = Shield("Small Shield", "A small shield held in the hand.", 6, 7, 9)
LargeShield = Shield("Large Shield", "A large shield that can cover from shoulder to knee.", 5, 6, 7)

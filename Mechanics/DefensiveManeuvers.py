class DefensiveManeuver:
    def __init__(self, name, proficiency, minproficiency, brawling, cut, dagger, greatsword, longsword, mass, pole, spear, sword, wrestling):
        self.name = name
        self.proficiency = proficiency
        self.minproficiency = minproficiency
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

x = False
y = True

Block = DefensiveManeuver("Block", 0, 0, x, x, x, x, x, 0, x, x, 0, x)
Parry = DefensiveManeuver("Parry", 0, 0, x, x, x, x, 0, 1, x, x, 1, x)

#Maneuvers
    #Characters can use Maneuvers up to 2 Proficiency levels beyond their own Proficiency, with a flat +1 Activation cost. Proficiencies more than 2 levels beyond a character's Proficiency are entirely unusable.
        #Defensive Maneuvers Described

            #Block: This is the most basic of defenses, halting or deflecting incoming attacks.
                #Where game mechanics are concerned, Blocking works essentially the same as any Parry, except that it uses the shield's DTN.
                #Block is the one exception to the rule that a character may only execute one Maneuver per Exchange, as it may be combined with a Parry if both weapon and shield are being wielded. In this case the DTN for Blocking is increased by +1 for using the off hand, whereas blocking with just a shield in the off hand does not increase DTN.
                #This Maneuver is available at all proficiency levels.

            #Block Open & Strike: This Maneuver consists of Blocking or Parrying an incoming attack wide open, then using a second (usually primary) weapon to attack the new opening.
                #During one Exchange defend with either a normal Block or Parry, but declare this Maneuver alongside this defense and pay its Activation Cost.
                    #Assuming a successful defense, the follow-up attack in the subsequent Exchange may be executed with bonus dice equal to this Maneuver's Quality of Success.
                #This Maneuver is available at Proficiency level 4.

            #Counter: Though primarily an offensive action, Counters are initiated by the defender. Sometimes called a Riposte, a Counter relies on recieving an opponent's attack, then using it against him.
                #When a defender declares Counter as his chosen defense he spends this Maneuver's Activation Cost and then allocates dice as in any standard Parry.
                    #If the defender fails the Parry, his Counter also fails and he is hit.
                    #If the Parry is successful with a QoS of at least 1, so is the Counter, and the defender assumes the role of aggressor as normal, but recieves bonus dice on his counterattack equal to the number of successes that were rolled in the attack that was successfully defended against with the Counter.
                #Additionally, due to they myriad nature of Counters, the countering party should roll on the Counter table to find out the exact effect of his Counter (note that Counters with light, fencing-style blades use the Half-sword column of the table).
                #No Activation Cost for countering Maneuvers derived from this table need be paid, but Activation Costs for Reach differences and those singular for the weapon used have to be paid.
                #If the countering attack would change the engagement range of the combatants, the countering party may decide whether to return to the previous engagement range once the Counter is concluded or to remain at this new engagement range.
                #This Maneuver is available at all Proficiency levels.

            #Evasion: This is the Maneuver of avoiding an attack by moving out of its way.
                #If Evasion is chosen as the Defensive Maneuver, any number of Evasions are possible during the Exchange, provided that dice from the MP are set aside for each individual Evasion.
                #This Maneuver is available at all Proficiency levels.

            #Expulsion: This Maneuver is not dissimilar to the offensive Beat, but is initiated from the defender's side.
                #This Maneuver is only effective against Thrusts and Thrust-based attacks, or against Slash-based attacks made with 4 dice or less.
                #To execute an Expulsion, simply declare "Expulsion" alongside the standard Parry, pay this Maneuver's Activation Cost, and allocate dice to the Parry as usual.
                    #The effects are nearly identical to those of an offensive Beat.
                    #If the Parry fails, then the round is resolved normally.
                    #If the Parry is effective, then all Maneuvers utilizing the weapon that was successfully expulsed receive a penalty equal to the defender's Quality of Success, applicable in the Exchange immediately following the Expulsion.
                #This Maneuver is available at Proficiency level 3.

            #Half-Sword: This technique has fine defensive properties as well.
                #See Half-Sword as an offensive Maneuver above and Counters, also above.

            #Overrun: An Overrun is a highly specialized and demanding Maneuver, similar in concept to a Master-Strike, but more limited than the latter. It combines a defense and an attack in the same action, in the same Exchange, and involves evading an opponent's blow while at the same time launching an attack of your own.
                #After paying the Activation Cost for the Maneuver, the player assigns dice to the defensive and the offensive action in the Maneuver.
                #The defensive action is an Evasion, rolled against TN 8 like a Partial Evasion. Any additional Activation Cost from Encumberance, if these optional rules are being used, must be paid as well, out of dice assigned to the defense.
                    #If the Evasion is successful (QoS 0+), the dice assigned to the offensive part of the Overrun are now used to launch an immediate Bash, Cut or Thrust against the opponent.
                #Any positive QoS from the Evasion carries over into the offensive part of the Maneuver as bonus dice.
                #If the Evasion was not successful, the offensive part of the Overrun goes ahead anyway, but any damage is determined before the Overruning character's attack roll and its consequences are pplied in full, including Shock penalties and any possible Knockdown.
                #A combatant carrying out a successful Overrun as his defense may assume the role of aggressor, unless the attacker inflicted a higher wound level upon the defender than the defender upon him.
                    #In this case the previous aggressor retains this role.
                #In any case the Overrun leaves the combatants at the engagement range of the Reach of the weapon of the combatant who emerges as the aggressor.
                #This maneuver is available at Proficiency level 8.

            #Parry: This Maneuver is the basis for all non-shield non-dodging defenses. It consists primarily of using one's own weapon to deflect - not halt - an incoming attack. Parries are performed by simply rolling defense with the DTN of the weapon at hand as the normal Opposed check of a combat Exchange.
                #If a combatant is wielding two weapons, one in each hand, this Maneuver allows him to deflect two attacks, one with each weapon. To do so, he assigns dice from his MP in any proportion to either Parry. Remember that actions with a weapon in the off hand are at +1 TN.
                #This Maneuver is available at all Proficiency levels.

            #Rota: The Rota is a riposte maneuver. The back edge of the blade is used to deflect an opposing attack, after which an immediate cut with the forward edge is performed.
                #The weapon is not moved far, and as such, the location of the counter attack is fixed. This maneuver is only available against swinging (Cleaving or Blunt) attacks, and the counter attack must be a Cleaving or Blunt swinging attack, not a thrust.
                #The Rota is similar to the Counter Maneuver with the same benefit for success (the attacker's successes as bonus dice for the counter attack the following exchange).
                #However, instead of the random location of the counter attack, the Rota counter attacks the same Target Zone on the opponent that this opponent had originally attacked on the character.
                #This Maneuver is available at Proficiency level 2.

            #Winding & Binding: 
                #Winding & Binding is a deadly game that results from the clash of two weapons "sticking" together for a time. While declared as a standard Parry, the Activation Cost of both Maneuvers must be paid.
                #If the Parry fails, the defender is struck as normal, but if successful, the Winding & Binding now comes into play, with an opponent's weapon not so much deflected, but instead collected on the defender's sword, with both weapons now "stuck" together.
                #Even if the defender merely ties the attacker, intitiate still passes to him, and he receives the Quality of Success of his Winding & Binding defense as bonus dice for his counterattack from the bind to the subsequent Exchange.
                #The nature of this follow-up attack, which has no Activation Cost, is somewhat random, the result of the shoving and winding match of the two combatants locked together, each trying to either disengage or strike past his foe's defending weapon.
                #While a Thrust past an opponent's guard is the most likely outcome, it is by no means the only one possible.
                #To determine the actual form of the follow-up attack, the intiator of the Winding & Binding rolls 1D6 on the Winding table.
                #Winding & Binding actually changes the engagement range. All attacks from the Winding & Binding table happen at optimum Reach for the attacker, this now being the new engagement range.
                #The defender has the choice of three defenses against the Winding & Binding attack determined on the table.
                    #1) If he knows the Winding & Binding Maneuver himself, he may declare it alongside a standard Parry, paying the Activation Cost for both.
                        #If he at least ties his opponent, the bind is maintained, but he becomes the new aggressor, carrying his QoS in the defense over as bonus dice into his follow-up attack, as determined by a roll on some table, check page 87.
                    #2) He may try to disengage his weapon. This is handled like a normal Parry with an additional Activation Cost of +1.
                        #In addition, initiative only switches to the defender if he was unsuccessful by a Quality of Success of at least 3.
                    #3) He may try to run off completely. This is handled like an Evasion with an additional Activation Cost of +3.
                        #On the first Exchange of the Winding & Binding, only Partial Evasion is possible, as the defender may now also try a Full Evasion, which if successful ends the bout as usual.
                    #No matter how the Winding & Binding ultimately ends, the loser is now at a optimum engagement range for the combatant who emerges from Winding & Binding as the aggressor, provided the bout is not broken up by a successful Full Evasion.
                #This Maneuver is available at Proficiency level 5.

        #Defensive Maneuver Activation Costs

            #Brawling:
                #Block: (1)
                #Block Open & Strike: (2)
                #Counter: (2)
                #Disarm: 5
                #Expulsion: (3)
                #Grapple: 1
                #Master Strike: (5)
                #Overrun: 3
                #Parry: 0
                #Rota: (2)
                #Winding & Binding: (4)

            #Cut & Thrust:
                #Block: 0
                #Block Open & Strike: 1
                #Counter: 1
                #Disarm: 3
                #Expulsion: 2
                #Grapple: 1
                #Master Strike: 4
                #Overrun: 2
                #Parry: 0
                #Rota: 1
                #Winding & Binding: 1

            #Dagger:
                #Block: (1)
                #Block Open & Strike: (2)
                #Counter: 2
                #Disarm: 4
                #Expulsion: (3)
                #Grapple: 1
                #Master Strike: (6)
                #Overrun: 2
                #Parry: 0
                #Rota: (2)
                #Winding & Binding: (2)

            #Greatsword:
                #Block: (2)
                #Block Open & Strike: (3)
                #Counter: 3
                #Disarm: 3
                #Expulsion: 2
                #Grapple: 2
                #Master Strike: 3
                #Overrun: 2
                #Parry: 0
                #Rota: 2
                #Winding & Binding: 1

            #Lance:
                #Block: 0
                #Block Open & Strike: -
                #Counter: -
                #Disarm: -
                #Expulsion: -
                #Grapple: -
                #Master Strike: -
                #Overrun: -
                #Parry: -
                #Rota: -
                #Winding & Binding: -

            #Longsword:
                #Block: (1)
                #Block Open & Strike: (2)
                #Counter: 2
                #Disarm: 3
                #Expulsion: 2
                #Grapple: 2
                #Master Strike: 3
                #Overrun: 2
                #Parry: 0
                #Rota: 2
                #Winding & Binding: 1

            #Mass Weapon & Shield:
                #Block: 0
                #Block Open & Strike: 1
                #Counter: (3)
                #Disarm: 3
                #Expulsion: 2
                #Grapple: (2)
                #Master Strike: (6)
                #Overrun: 3 / 2
                #Parry: 1
                #Rota: 2
                #Winding & Binding: (3)

            #Pole-arms:
                #Block: (2)
                #Block Open & Strike: (3)
                #Counter: (3)
                #Disarm: 4
                #Expulsion: 2
                #Grapple: (3)
                #Master Strike: (6)
                #Overrun: 3
                #Parry: 0
                #Rota: 3
                #Winding & Binding: (3)

            #Spear & Shield:
                #Block: 0
                #Block Open & Strike: 1
                #Counter: (3)
                #Disarm: (5)
                #Expulsion: (2)
                #Grapple: (3)
                #Master Strike: (6)
                #Overrun: 3
                #Parry: 1
                #Rota: (3)
                #Winding & Binding: (3)

            #Sword & Shield:
                #Block: 0
                #Block Open & Strike: 1
                #Counter: 3 / 2
                #Disarm: 3
                #Expulsion: 2
                #Grapple: (2)
                #Master Strike: 4
                #Overrun: 2
                #Parry: 1 / 0
                #Rota: 2
                #Winding & Binding: 2

            #Wrestling:
                #Block: (1)
                #Block Open & Strike: (2)
                #Counter: (3)
                #Disarm: 4
                #Expulsion: (4)
                #Grapple: 0
                #Master Strike: (6)
                #Overrun: (4)
                #Parry: (1)
                #Rota: (3)
                #Winding & Binding: (3)

#Evasion and Half-Sword are available for all Proficiencies at identical, variable Activation Costs explained in the Maneuver descriptions.
#Activation Costs in parentheses are those not normally taught with a certain Proficiency, but that might come up for use in unusual situation.
#* Mass Weapon & Shield: Lower of two given Activation Costs is for use without shield.
#** Sword & Shield: Lower of two given Activation Costs is for use without shield.

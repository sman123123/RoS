#Dice required (D6 and D12)

#Successes Needed
    #One - Average
    #Two - Challenging
    #Three - Difficult
    #Four - Amazing
    #Five - Legendary

#Major checks made against TN7.

#Quality of Success may also denote an action's degree of success.
    #Zero - Failure
    #(Ties) - Result Varies
    #One - Basic Success
    #Two - Good
    #Three - Well Done
    #Four - Expertly Done
    #Five - Perfect

#Attribute Checks
#Skill Checks
#Proficiency Checks
#Opposed Checks
#Timed Checks

#Skill Levels
    #Zero - Default
    #One - Beginner or Student
    #Two - Apprentice
    #Three:Four - Journeyman
    #Five:Seven - Adept
    #Eight:Nine - Master

#Complications
    #Unopposed Check that fails to meet its required number of successes by more than 1
    #Any Opposed Check made with 5 or more dice and failing to achieve even a single success.

#Attribute Descriptions
    #Basic Attributes
        #Brawn - (BN) is a measure of your muscle, your vitality, or your frame. It indicates how much damage you can do unaided, and how easily you resist punishment, disease, and poison.
        #Daring - (DG) is a measure of your courage and ability to take decisive action. It affects how well you can strike and parry, as well as how skilled you are with actions like climbing, acrobatics and all kinds of athletics.
        #Tenacity - (TY) is a measure of your ability to focus on a task or goal, a meter of the strength of your persona. It affects how easily influenced you are, your inner discipline, and your sanity.
        #Heart - (HT) is a measure of your social aptitude. It affects both how charismatic you appear to others (people and animals) and how easily you can get them to do your bidding. It governs your ability for empathy, and the understanding of human and animal nature.
        #Sagacity - (SY) is a measure of your mental agility. It indicates how logical, intuitive, and smart you are. It affects situations that require reasoning, sharpness of the senses, as well as any judgment relating to them.
        #Cunning - (CG) is a measure of your raw instincts, agility, reaction time, and balance. It affects how skilled you are with actions like lock picking, pick pocketing, hiding, and sneaking.

    #Combined Attributes (all numbers >= .50 are rounded up.)
        #Reflex is a combination of Daring and Cunning. It determines how quickly a character may physically react to external stimulus.
            #Reflex = (Cunning + Daring)/2
        #Aim is a combination of Sagacity and Cunning. It quantifies one's natural ability to hit a target over distances.
            #Aim = (Sagacity + Cunning)/2
        #Knockdown is a combination of Brawn and Daring. It measures how solid and balanced one remains after taking a blow.
            #Knockdown = (Brawn + Daring)/2
        #Knockout is a combination of Brawn and Tanacity. It measure how hard it is to knock a character unconscious.
            #Knockout = (Brawn + Tenacity)/2
        #Move is a combination of Brawn, Cunning, and Daring. It is a measure of how much distance one can cover on foot in a hurry.
            #Move = (Brawn + Cunning + Daring)/3

#Assigning Attributes
    #Must assign a Focus stat, no other stat may exceed the Focus.
    #Must be <= 8

#Assigning Skills
    #Must be <= 8

#Assigning Proficiencies
    #Must be <= 12

#Pools
    #Melee Pool: Reflex + Weapon Proficiency
    #Archery Pool: Aim + Missile Proficiency

#Proficiencies
    #Brawling - Brawling consists first and foremost of punching and kicking, derived by means of the Bash Maneuver, but also of grappling and plenty of dirty tricks.
    #Cut and Thrust - This proficiency refers to swords that are usually not weilded in conjuction with a larger shield, but rather in quick fencing style.
    #Dagger - Found in every place in the world, daggers and knives are used as both tools and instruments of death.
    #Greatsword - Frequently wielded with a wide, half-swording grip. Greatswords are fearsome weapons with great range, but easily overcome by any fighter agile enough to get close.
    #Longsword - For those warriors that prefer not to use shields, longswords are very polular. They are a fierce weapon, capable of heavy damage when either cleaving or thrusting, as well as complex maneuvering and countering.
    #Mass Weapon and Shield - Mass weapons include any single-handed (and occasionally two-handed) weapon that is particularly heavy on the end. These weapon's balance makes them slow on the parry and commends the use of constant evasion or - more commonly - shields.
    #Missile Weapon Proficiencies
    #Pole-Arms - A wide range of weapons from the Spear to the Halberd.
    #Spear and Shield - Covers the use of one-handed spears and shields.
    #Sword and Shield - This Proficiency involves any one-handed sword and a shield. Although this proficiency could be used without a shield and no penalty.
    #Wrestling - As with Brawling, Wrestling is always an option for the unarmed character.

#Maneuvers
    #Characters can use Maneuvers up to 2 Proficiency levels beyond their own Proficiency, with a flat +1 Activation cost. Proficiencies more than 2 levels beyond a character's Proficiency are entirely unusable.

        #Offensive Maneuvers Described

            #Bash: This is the standard attack for all swung blunt weapons.
                #Extra power may be added to a Bash by expending 1 (and only 1) extra MP die prior to rolling, and adding 1 damage in the event of a successful hit.
                #If a bash successfully strikes the head, the Shock rating of such a hit is increased by half that hits Impact Rating before the defender's AV and half BN are subtracted. This Shock even applies if no actual wound is caused.
                #This maneuver is available at all Proficiency levels.

            #Beat: This is an attack upon the opponent's weapon or shield in attempt to temporarily remove it from the equation.
                #Beats may only be performed at the start of a bout or following a "pause".
                #Every success in the attacker's QoS costs the defender 2 MP (this functions similarly to Shock)
                #If the defender wins, the round resolves normally and initiative changes over.
                #All reach penalties are cut in half when Beating.
                #The Beat maneuver is available at Proficiency level 3.

            #Bind & Strike: This Maneuver uses off-hand weapons to bind or pin down an opponent's weapon or shield, opening up a clean follow-up attack.
                #On one Exchange roll attack as normal with the shield or off-hand weapon, taking into account the normal +1 TN for attacking with the off hand.
                    #If using a shield to Bind the opponent's weapon ATN is 6 for both bucklers and large shields and 5 for small shields, without penalty for using the off hand.
                #The defender can either Evade or use the weapon or shield that is being "Bound" to Parry or Block, but may not use another weapon or shield to defend against the Bind.
                #If this attack is successful your opponent cannot use the "Bound" weapon or shield on the next Exchange and loses 1 MP per point of QoS, also good on the next Exchange.
                #This Maneuver is available at all Proficiency levels.

            #Cut: This is the standard attack for all edged weapons, learned immediately.
                #Extra power may be added to a Cut by expending 1 (and only 1) extra MP die prior to rolling and adding 1 to damage in the evnent of a successful hit.
                #This Maneuver is available at all Proficiency levels.

            #Disarm: Disarms may be performed as an attack or defense.
                #As an attack, it is performed in a similar manner to the Beat Manuever, except that it is not necessary to perform the Disarm after a break in the combat like a Beat.
                    #As with a Beat all reach modifiers are halved.
                    #If the Disarm is successful, the defender must make a Knockdown Check with a Difficulty equal to the attacker's Quality of Success.
                        #If this check is failed then the weapon has been dropped.
                        #If the Knockdown Check is successful, then the defender has managed to retain his grip on his weapon but the attacker retains the role of aggressor.
                #As a defense, the Disarm Maneuver is performed in a similar manne rto a Parry.
                    #Unlike other defenses, Disarm incurs a Reach penalty of 1/2 the usual reach penalty for an attack.
                    #After the Activation Cost has been paid, dice are assigned as if for a Parry.
                    #If the defense was successful, then the attacker must make a Knockdown Check with a Difficulty equal to the defender's QoS.
                        #Failure in the Knockdown Check means that the attacker has instead been disarmed.
                        #Whether the attacker drops his weapon or not, the defender now takes initiative.
                    #Of course, if the attacker wins, then the Disarm attempt has failed and the attack goes through (minus the defender's QoS as usual).
                #This Maneuver is available at Proficiency level 3.

            #Double Attack: Attacking with two weapons at once is a tricky thing.
                #Divide your dice on this attack in any proportion between both weapons (remember weapon Reach penalties) and attack. Note that any weapon wielded in the off-hand adds a penalty of +1 to ATN for that weapon's use.
                #Your opponent will have a difficult time defending against both of your attacks, viable defenses being only Evasion, Parry (if he has two weapons), or Block and Parry (if he has both a weapon and a shield).
                #This Maneuver is available at Proficiency level 4.

            #Evasive Attack: This is a defensive measure that takes place during an attack (thus it counts as an offensive Maneuver). In principle the attacker cuts wit hhis weapon while simultaneously leaping backward so as to evade an opponent's attack.
                #To execute this Maneuver one attacks as normal with a slashing-type attack, spending this Maneuver's Activation Cost in addition to the normal Activation Cost of the attack.
                #If the optional Encumberance rules are being used, a further Activation Cost equal to the Encumberance score must be paid, as per Evasion.
                    #Once the Maneuver is activated any number of additional dice may be spent to raise your opponent's ATN by one per additional die spent.
                        #On the downside, your own ATN also rises, though only by one for every two additional dice spent (rounded up).
                #This Maneuver is impossible to use in conjunction with any Thrust-based Maneuver.
                #This Maneuver is available at Proficiency level 4.

            #Feint & Strike: This as a relatively difficult to perform trick, with a higher Activation Cost than the Feint & Thrust. It consists of swinging at one region of the body, then changing direction mid-swing in an effort to bypass the defender's defenses entirely.
                #Once the Activation Cost is paid, any number of dice may be added to the attacker's hand, at a cost of 1 MP for every additional dice rolled in the attack.
                #A Feint is always declared after the defender declares defense but before dice are rolled.
                    #It's important to note that a Feinted attack lands in a different spot than originally declared. The attacker must also state the new location of attack (within no more than two Target Zones of the original attack).
                #Activation cost is equal to the "distance" from the orignal to the ultimate Target Zone, i.e. either 1 or 2.
                #Feints have a tendency to lose their novel effect after a while when used against the same opponent. Each repeated identical Feint against a single opponent, in the same location costs an extra MP die to execute.
                #The Feint & Strike is available at Proficiency level 3.

            #Feint & Thrust: This is among the first "tricks" that most swordsmen know. Like the Feint & Strike it begins with a false swing, in this case always either over-hand or across, but finishes with a Thrust to the head, neck, or torso.
                #This Maneuver is executed almost identically to the Feint & Strike. When attempting a Feint & Thrust the attacker declares a Slashing attack aimed at Target Zones 3, 4, or 5, complete with MP dice expenditure.
                    #The defender then declares his own defense - if this defense isn't based on the Parry Maneuver, Feint & Thrust cannot be executed and the aggressor either has to stick with his originally declared Swing-type offense.
                #If this Maneuver can proceed, the attacker now states that he is performing a Feint & Thrust and adds any number of MP dice to his pool at a cost of one MP for every one added to the attacking hand (as per Feint & Strike).
                    #He also declares a new Target Zone for his Thrust which must be either zones 11, 12, or 13.
                #Feints have a tendency to lose their novel effect after a while when used against the same opponent. Each repeated identical Feint against a single opponent, in the same location costs an extra MP die to execute.
                #The Feint & Thrust is available at Proficiency level 2.

            #Grapple: The basics of this Maneuver are imparted by many Proficiencies. It consists of grabbing the opponent, removing any weapon currently wielded by him from the equation, and changing the bout from free-flowing combat into a wrestling match, with the purpose of immobilizing the opponent, throwing him to the ground or breaking his limb.
                #The Activation Costs listed for the Grapple Maneuver presume that it is launched against the limb of an opponent, specifically the primary attacking limb if used defensively.
                    #If used offensively (and only then), it may be targeted against other parts of the body, for instance the torso or the head, but its Activation Cost in this case increases by +1.
                    #Also if used defensively against any attack other than an unarmed one, the Activation Cost is increased by a further +1.
                #Finally, Reach modifiers apply to both offensive and defensive use of the Maneuver, which of course has a Reach of Hand.
                #The Grapple's TN, both for offensive and defensive use is invariably 7.
                #If the Maneuver is successfully used defensively, a hit is not only avoided, but a hold on the opponent's weapon arm is also established.
                #If used successfully as an offense, a hold on whatever part of the body that was targeted is established.
                #In either case the successful grappler is now the aggressor, even if he was previously the defender and merely tied the opponent's attack (unless Grapple was used as a defense against another Grapple, in which case a tie establishes no clinch and the roles of aggressor and defender remain unchanged).
                #After a successful Grapple both combatants are now in a clinch at the Reach range of Hand, and until the clinch is broken both must use MP dice from their Wrestling Proficiency.
                #Should the clinch be entered mid-Round when another Proficiency other than Wrestling was being used in the first Exchange, the MP is recalculated for the second Exchange based on Wrestling Proficiency, with dice spent oin the first Exchange subtracted from the Wrestling MP.
                #Once the clinch is established, the aggressor, receiving his QoS in executing the intial Grapple Maneuver as bonus dice for his subsequent MP. now has three options:
                    #1) Immobilize: The aggressor tries to improve his initial hold in such a way as to completely immobilize his opponent. Achieving this can require several Exchanges of wrestling.
                        #The aggressor assigns MP dice and, without paying any Activation Cost, checks against TN 7.
                            #If he is beaten by the opponent's defense, the hold is broken and combat returns to a normal melee at engagement range Hand, with the former defender now being the aggressor.
                            #If the defense is however tied or overcome, the victor's QoS is subtracted from the opponent's MP for the next Exchange. If this does at any time lead to one combatant beginning a Combat Round with an MP of 0 or less dice, he is completely immobilized and unable to break free until circumstances change significantly.
                    #2) Throw: The aggressor tries to throw his opponent to the ground.
                        #To do so he assigns MP dice and rolls his Opposed Check.
                            #The TN is 6 if the initial hold was on a leg, and 8 if on torso, head, or arm.
                                #If the defense against the throw was successful, the hold is broken and the previous defender becomes the new aggressor, at a current engagement Reach range of Hand.
                                #In the case of a tie, the clinch is also broken and the combat also continues at Reach range Hand, but without a change of aggressor.
                                #If the aggressor is vicorious, the clinch is also broken and he remains the aggressor, but the opponent is thrown to the ground, with all the attendant penalties of being prone.
                    #3) Break: The aggressor attempts to break the limb he has grabbed.
                        #To do so, he assigns MP dice and rolls them in an Opposed Check.
                            #His TN for this roll is 7 if an arm is grabbed, 8 for a leg, and 9 for the neck, and is opposed by the defender's assigned MP dice.
                                #If the defender is victorious, the clinch is broken, and he becomes next Exchange's aggressor, at an engagement range of Hand.
                                #If the roll is tied, the outcome is identical to a tied attempt to immobilize.
                                #If the aggressor is vicorious, aggressor and defender immediately make an Opposed BN Check, with the aggressor receiving his QoS as bonus dice.
                                    #If the aggressor wins his Opposed Check with a QoS of at least 2, the limb in question is broken - which in the case of the neck is quite fatal.
                                    #If any limb other than the neck is affected, refer to the Blunt Swing Damage Tables, Zone 1 for broken legs and Zone 7 for broken arms. Roll D6 on the table for Zone 1 or 7 and apply the result of a level 4 wound to the exact location determined by the die.
                                    #Any other outcome is treated like a tied attempt to immobilize.
                #Break Out: The defense against attempts to immobilize, throw, or break limb is always by trying to break out of the opponent's hold.
                    #This is a defensive use of the Maneuver free of any Activation Cost; the defender simply assigns dice from his MP and checks them against TN 7.
                        #Victory on this roll usually signifies the breaking of the clinch and a switch of the role of aggressor and defender, but this may vary with the actual wrestling attack defended against.
                #Alternatively, a grabbed opponent may choose to forego any attempt to break the enemy's hold on him and simply attack him instead.
                    #He cannot use the held limb for such an attack, and the MP for attacks with another part of the body are modified by -1/2 MP due to tehe awkwardness of having one's freedom of movement restricted by the hold.
                        #Engagement Reach range for this attack is Hand, and it is only conducted after the enemy has carried out his - now unopposed - offensive Grapple Maneuver.
                #This Maneuver is available at all Proficiency levels.

            #Half-Sword: This is one of the few practical ways to kill an armored opponent in full harness (full plate) with a sword.
                #Used with long swords, bastard swords, and other longer weapons, the Half-Sword technique is performed by grasping the blade of the sword with the off hand in order to use the sword as a short spear or pole-weapon.
                #This technique is particularly useful in close-quarters as well, when swinging a long weapon may be impractical.
                #Half-Swording reduces a sword's effective Reach by one or two steps from Long to Medium or Short, at the player's discretion, note that the Half-Sword may be released into a one-handed attack at any time, nullifying any Half-Sword bonuses, but gaining Reach.
                #Half-Swording precludes the sword being used for slashing but increases control over the weapon and thus lowers both DTN and Thrust ATN by 1.
                    #The latter does effectively also increase damage dealt, but against any type of armor half-swording also increases the Thrust DR by +1.
                #One can shift from normal grip to the Half-Sword at any time, though doing so during an Exchange (shifting suddenly into our out of the Half-Sword in order to execute a particular counter, for example) costs 1 MP.
                #This Maneuver is available at all Proficiency levels.

            #Hook: Many pole-arms and axes are capable of hooking an opponent's limb or head. This Maneuver is executed like a Thrust that intentionally misses, and then the shaft is pressed against the target and pulled.
                #This Maneuver is particularly effective on the legs, causing one's opponent to fall and become prone. After spending the Activation Cost (usually 1) allot dice for a regular Thrust-like attack.
                #The hooked party checks Knockdown with a Challenge Level equal to the aggressor's QoS. Failure drops him to the ground, with the usual attendant penalty of half total MP for lying prone.
                #This Maneuver is available at all Proficiency levels.

            #Master-Strike: The jewel of the art of fighting is the Master-Strike, a type of attack that both defends and offends in one motion.
                #The technique, as it applies to the game, can be used either as an offensive or defensive Maneuver, and in many ways resembles the Simultaneous Block/Strike Maneuver, but only uses one weapon.
                #As an Offense, declare a Master-Strike alongside any Cleaving attack and pay the Activation Cost.
                    #Divide the attacking dice into offense and defense, in any proportion. This is clearly most useful in a situation where both opponents are attacking simultaneously.
                #As a Defense, declare a Master-Strike as your defense or alongside a Parry and pay the Activation Cost.
                    #Split this Exchange's dice into offense and defense.
                    #Roll the defense first, as your opponent attacks. If your defense is successful, carry the dice in your Quality of Success over into the offensive roll!
                    #Should your defense fail, regardless of offensive or defensive role, the attack also fails, and all dice assigned to it are lost.
                #This Maneuver is available at Proficiency level 10.

            #Murder Stroke: The murder stroke is an unusual Maneuver, used to take down a foe in heavy armor when you're having trouble getting through the armor with your blade.
                #The Murder Stroke can only be performed when using heavier one- or two-handed blades, and involves reversing the entire weapon, gripping the blade with the hands and beating the opponent in the head with the pommel of the sword.
                #Obviously, this requires gauntlets or some form of hand protection! The Murder Stroke reduces the effective Reach of the weapon by one step and the attack must be a swing aimed at area, or 4 (either side).
                #If successful, and if the head is struck, the DR is +1 Blunt, but the attendant Shock rating is increased by +X, wehre X is half the attacker's total of QoS + half BN + DR before the defender's BN and AV are subtracted, exactly as with any other Bash to the head.
                    #This Shock even applies if no actual wound is caused, also as usual for Bashes to the head. This Maneuver is not available to bashing weapons, which hit the head for additional Shock in any case.
                #This Maneuver is available at Proficiency level 3.

            #Simultaneous Block/Strike: This gutsy Maneuver is not unlike the Bind & Strike Maneuver, except that it all happens in the course of one Exchange.
                #To perform this Maneuver, divide your MP between attack and defense (remember that you still need dice for the next Exchange).
                #The defense is then rolled against your opponent's attack, and your offense against his defense (if any).
                #This Maneuver is obviously only useful in situations where both you and your opponent are attacking at once. All attacks are resolved normally.
                #This Maneuver can also be performed with a parrying weapon instead of a shield in the off hand, in which case it should more properly be called "Simultaneous Parry/Strike".
                    #Don't forget that, unlike shields, parrying weapons wielded in the off-hand have their DTN increased by +1, though.
                #This Maneuver is available at all Proficiency levels.

            #Thrust: All Thrusting-capable weapons have an ATN for Thrusting. Some weapons are better suited to this form of attack, as reflected in the ATN.
                #Thrusts are also notoriously fast - in cases when two combatants attack at the same time, if one of them Thrusts as his Offensive Maneuver, he receives a +1 die on his Opposed Reflex Check to determine who goes first.
                    #Should two parties with equal Reflex Thrust at the same time both parties receive the +1 bonus to their Reflex Check.
                #This Maneuver is available at all Proficiency levels.


        #Offensive Maneuver Activation Costs
            #Brawling
                #Bash: 0/1
                #Beat: (3)
                #Bind & Strike: (3)
                #Cut: (3)
                #Disarm: 3
                #Double Attack: (2)
                #Evasive Attack: (2)
                #Grapple: 1
                #Hook: (3)
                #Master Strike: (5)
                #Murder Stroke: (4)
                #Simultaneous Block/Strike: 1
                #Thrust: (3)

            #Cut & Thrust
                #Bash: (2)
                #Beat: 0
                #Bind & Strike: 0
                #Cut: 0
                #Disarm: 1
                #Double Attack: 1
                #Evasive Attack: 1
                #Grapple: (2)
                #Hook: (2)
                #Master Strike: 4
                #Murder Stroke: (2)
                #Simultaneous Block/Strike: 0
                #Thrust: 0

            #Dagger
                #Bash: 1 (2)
                #Beat: (3)
                #Bind & Strike: (2)
                #Cut: 0
                #Disarm: 2
                #Double Attack: 1
                #Evasive Attack: 1
                #Grapple: 1
                #Hook: (3)
                #Master Strike: (5)
                #Murder Stroke: (4)
                #Simultaneous Block/Strike: 1
                #Thrust: 0

            #Greatsword
                #Bash: (1)
                #Beat: 0
                #Bind & Strike: (2)
                #Cut: 1
                #Disarm: 1
                #Double Attack: (3)
                #Evasive Attack: 1
                #Grapple: (3)
                #Hook: (2)
                #Master Strike: 3
                #Murder Stroke: 1
                #Simultaneous Block/Strike: (3)
                #Thrust: 0

            #Lance
                #Bash: -
                #Beat: -
                #Bind & Strike: -
                #Cut: -
                #Disarm: -
                #Double Attack: -
                #Evasive Attack: -
                #Grapple: -
                #Hook: -
                #Master Strike: -
                #Murder Stroke: -
                #Simultaneous Block/Strike: 0
                #Thrust: 1

            #Longsword
                #Bash: (1)
                #Beat: 0
                #Bind & Strike: (1)
                #Cut: 0
                #Disarm: 1
                #Double Attack: (2)
                #Evasive Attack: 1
                #Grapple: (2)
                #Hook: (2)
                #Master Strike: 3
                #Murder Stroke: 1
                #Simultaneous Block/Strike: (2)
                #Thrust: 0

            #Mass Weapon & Shield
                #Bash: 0
                #Beat: 1
                #Bind & Strike: 0
                #Cut: 0
                #Disarm: 1
                #Double Attack: (3)
                #Evasive Attack: 2
                #Grapple: (3)
                #Hook: 1
                #Master Strike: (5)
                #Murder Stroke: (2)
                #Simultaneous Block/Strike: 0
                #Thrust: 1

            #Pole-arms
                #Bash: 0
                #Beat: 0
                #Bind & Strike: (3)
                #Cut: 0
                #Disarm: 2
                #Double Attack: (4)
                #Evasive Attack: 1
                #Grapple: (3)
                #Hook: 1
                #Master Strike: (6)
                #Murder Stroke: (2)
                #Simultaneous Block/Strike: (3)
                #Thrust: 0

            #Spear & Shield
                #Bash: (1)
                #Beat: 1
                #Bind & Strike: 0
                #Cut: (1)
                #Disarm: (3)
                #Double Attack: (4)
                #Evasive Attack: 2
                #Grapple: (4)
                #Hook: 1
                #Master Strike: (6)
                #Murder Stroke: (3)
                #Simultaneous Block/Strike: 0
                #Thrust: 0

            #Sword & Shield
                #Bash: (1)
                #Beat: 0
                #Bind & Strike: 0
                #Cut: 0
                #Disarm: 1
                #Double Attack: (3)
                #Evasive Attack: 2
                #Grapple: (3)
                #Hook: (2)
                #Master Strike: 4
                #Murder Stroke: 1
                #Simultaneous Block/Strike: 0
                #Thrust: 0

            #Wrestling
                #Bash: 1 / 2
                #Beat: (3)
                #Bind & Strike: (3)
                #Cut: (3)
                #Disarm: 2
                #Double Attack: (3)
                #Evasive Attack: (4)
                #Grapple: 0
                #Hook: (2)
                #Master Strike: (6)
                #Murder Stroke: (4)
                #Simultaneous Block/Strike: 2
                #Thrust: (3)

            #Feint & Swing, Feint & Thrust, and Half-Sword are available for all Proficiencies at identical variable Activation Costs explained in the Maneuver descriptions.
            #Activation Costs in parentheses are those not normally taught with a certain Proficiency, but that might come up for use in an unusual situation.
            #*Brawling: Bash Activation Cost 0 is for punches, 1 for kicks and any other Bashes that might come up.
            #**Dagger: Bash Activation Cost 1 is for punches, 2 for any other Bashes that might come up.
            #***Wrestling: Bash Activation Cost 1 is for punches, 2 for kicks and any other Bashes that might come up.

#Page 80

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

#1. LIMELIGHT AND THE COMBAT ROUND
#The basic temporal unit any Combat Scene in Blade is the Combat Round. During the Combat Round, every combatant has dice to spend on action equal to his Melee Pool. 
#Players will have to be judicious about what activities they spend their MP dice on, and all associated costs to their MP pool. A subdivision of the Combat Round is the Exchange, with every Combat Round consisting of two. 
#The Exchange is thus the shortest temporal division of a Combat Scene, which ultimately consists of any number of Combat Rounds, each made up of a pair of Exchanges.

#2. THE ORDER OF A COMBAT ROUND
#A Combat Round is fought in the following sequence:
#1) All stances are declared.
#2) Aggressor and defender is established (initiative). Melee Pool fills/refreshes, with all Modifiers.
#3) During the first half of the Combat Round, the first Exchange, the aggressor attacks and defender defends.
#4) Damage is resolved and/or new attitude determined (aggressor or defender).
#5) During the second half of the Combat Round, the second Exchange, the aggressor attacks and defender defends. These roles may have been reversed since the first Exchange.
#6) All damage is resolved and/or new attitude determined (aggressor or defender).
#Steps 2-6 continue to repeat until the resolution of the combat, or until the flow of combat is interrupted otherwise (a pause). At the beginning of each new melee conflict (or following a pause) begin at step 1, then repeat 2-6 as normal.

#3. STEPS 1 & 2: STANCES, INITIATIVE, AND SURPRISE
#Unless taken by surprise, combatants will usually have time and opportunity to declare a stance – these should be clearly announced at the table. 
#Stances potentially provide for a stronger attack or defence, though perhaps adding some rigidity to a combatant’s action.
#Though every school speaks with confidence on the superiority of its teaching, three stances are universal; Aggressive, Defensive, and Neutral stances.

#Aggressive stances provide an attack bonus at the cost of making one’s defense more difficult. Such stances add 2 MP dice for an attack but increase activation costs for any Defensive Maneuver by 2 MP.
#Defensive stances grant a defensive bonus while making attack execution more difficult. Such stances add 2 MP dice when Defending but increase the activation costs for any Offensive Maneuver by 2 MP.
#Neutral stances are the favorite of many. In a Neutral stance one’s weapon is positioned to allow for either quick attack or defensive response. Neutral stances provide no bonus to either attack or defense.
#Note: Stances are only in effect until the first blow or movement — once a character’s weapon moves, the stance is gone. Once melee is joined the stances of both attacker and defender are treated as neutral, with no bonus conveyed to either. A stance cannot be taken (or regained) until the combatants separate for a full pause.
#Initiative is determined after any stances are declared, when each combatant announces their intent to either attack or defend.
#The intent of the combatants will usually be very clear from the circumstances under which they enter combat – more often than not, one or even both will charge the other. Apart from of course counting as an aggressive stance, such a charge automatically suggests the intent to attack, leaving the other party to decide whether to receive the charge with a defence or to himself attack.
#Some rare combat encounters, for example formal duels or gladiatorial bouts, may however start out less unambiguous, with both combatants gauging each other, shifting from stance to stance and waiting for an opening in their opponent’s defence to attack. In these cases it is advisable to demand that both parties declare intent to attack or defend simultaneously, maybe by lifting one finger for attack and two for defence. Until at least one party declares attack, the bout does not actually commence.
#If a party fails to declare intent while the other declares attack, then this character is considered to have hesitated and may only defend for one full Combat Round – if even that (see Surprise).
#The attacker, now having the initiative, declares how many dice from his Melee Pool are being spent on the attack, where the attack is aimed, and what Maneuver, if any, is being used. 
#The defender in response to the attacker declares how many dice from his Melee Pool are going towards defense, what defense is being used, and what Maneuver, if any, is being executed. If both combatants declare as aggressors, Offensive Maneuvers and assigned dice are announced before the Reflex Check to see who goes fractionally first. The combatant with the higher Reflex may choose whether to declare first or second; tied Reflex scores are broken by the higher CG score, and tied CG scores by the higher Proficiency.
#An Opposed Reflex Check (with the combatants’ own ATNs for Target Numbers— see the Appendix for weapon ATNs) then determines whose strike lands first. For every step of Reach difference of the weapons used, the wielder of the longer weapon receives 1 bonus dice to this Check, and the wielder of the shorter weapon is penalized 1 die. In the rare cases where the combat begins at the optimum engagement range of the shorter Reach weapon, these modifiers are reversed.
#Note that no defense is possible in the middle of an attack, so the loser of this Check will likely be killed. In the Exchange that follows, the winner of this Exchange now assumes the role of aggressor and his opponent that of defender. Should the Opposed Reflex Check be tied, both combatants strike at exactly the same time.
#Stealing Initiative is only and exclusively possible immediately before the first blows of any bout are traded and is usually done in one of two circumstances: 
#The first is when two combatants declare as aggressors and attack simultaneously.
#If one combatant turns out to be fractionally slower than the other, he may attempt to Steal Initiative, but if both combatants attack at exactly the same time, the combatant with the higher Reflex score is the one first entitled to attempt to Steal Initiative; tied Reflex scores are broken by the higher CG score, and tied CG scores by the higher Proficiency. Should he decline to try Stealing Initiative, the other combatant may then opt to attempt to.
#The party attempting to Steal Initiative pays an Actiation Cost equal to half his opponent’s SY (0.50 rounds up).
#The attempt itself is an Opposed Check between the initiator’s CG and his opponent’s DG.
#This contest is modified by differences in the Reach of the weapons used; if there is any difference, the wielder of the longer weapon receives a flat +1 die bonus on his Check while the wielder of the shorter weapon must incur a flat -1 die penalty.
#When the combatants begin the bout already at the Reach of the shorter of the weapons involved, the above modifiers are reversed: Shorter weapons garner a flat +1 die bonus, and longer weapons a flat -1 die penalty.
#Finally, the initiator of the attempt, and only he, may buy bonus dice for his Check by spending dice from his MP on a one-to-one basis, up to the value of his DG rating.
#PAs do not modify to this check, as PAs are added to one’s MP pool at the beginning of the combat scene, and are thus already accounted.
#The winner of the Opposed Check strikes first, and the loser, should he still be able to continue after his opponent’s attack, second. In a tie, both combatants strike simultaneously, which might well result in the death of both. In any case, a combatant who had the Initiative stolen from him may immediately try to steal it back. Such attempts to Steal Initiative or steal it back may theoretically continue until one party depletes his MP.
#The second situation where one may wish to Steal Initiative can occur when a character who has previously declared defense wishes to switch over and instead attack. The process is identical to that described above.
#Surprise can occur at any time, even when you suspect that danger is near. When a Surprise Check is called for, the player checks Reflex against TN7, with the difficulty based on how alert the character or NPC was. Table 4.1, Surprise Difficulties, provides guidelines. Failure indicates no action can be taken until the next Combat Round. 
#Meeting the required number of successes means that the target may defend themselves (or attempt to Steal Initiative).

#4. STEPS 3 & 5: THE EXCHANGE 
#Again, each Combat Round consists of two Exchanges. During an Exchange each of the participants may perform but one action, usually attacking or defending by use of a single one of either the Offensive or Defensive Maneuvers. 
#Someone who is one in the role of aggressor may utilize both Offensive and Defensive Maneuvers, though will of course usually not choose one of the latter. Someone who is in the role of defender may freely utilize nothing but Defensive Maneuvers, but may choose to execute an Offensive Maneuver instead if he pays a special Activation Cost (see below).
#All attacks must be aimed at a specific locale; those numbered 1-14 (see Table 4.1). Arrows indicate swing target zones, while circles mark zones for thrusting or missile attacks. 
#While a player need not declare a specific number, he must describe the attack in terms that may be easily understood, i.e., Thrust to the face, Slash to the right foot, etc.), as random attacks are not a part of Blade melee. Maneuvers and chosen target zones may increase or decrease TNs for both attacker and defender alike, and may also require an additional Activation Cost: Optionally, all melee thrusts to head and limbs (target zones 8, 9, 13, and 14) require an additional 1 point Activation Cost to execute. 
#Both participants now roll the allotted Dice from their Melee Pool (See Step 2), with all modifiers totaled from all Maneuvers, stances, or other situations factors. 
#This is a normal Opposed Check, where one party’s Victories are subtracted from the other’s, leaving the winner with a net Quality of Success. An attack is successfully executed if the attacker achieves a QoS of 1 or more. Ties in the Opposed Check or an outright QoS in the defender’s favor denote a successful defence.
#All Target Numbers for this Check come from the ATN (Attack Target Number, used when attacking) or DTN (Defense Target Number, used when defending) listed with each weapon (see the Appendix) or defence.
#After all damage is resolved, a winning aggressor maintains his role as aggressor, unless he declines it, or cannot continue because of depleted MP, while conversely his opponent still retains uncommitted MP dice. If either is the case, the defender may choose to take on the role of aggressor.
#With a successful defence, the defender may now take on the role of aggressor, unless he merely tied the aggressor, in which case the latter retains his role.
#Some Defensive Maneuvers may on a case-by-case basis allow a successful defender to either assume the role of aggressor upon a tie, or upon paying an additional Activation Cost, or perhaps under no circumstances at all. Any such special mechanics are explained within their respective Maneuvers.
#Finally, should a defender enter a new Exchange and wishes to execute an Offensive Maneuver and attack, regardless of the consequences, he may declare an Offensive Maneuver like the aggressor, announcing both his Maneuver for the Exchange and the number of dice allocated to it. 
#This declaration of an Offensive Maneuver carries an Activation Cost equal to half the aggressor’s DG (0.50 rounds up, as always), above and beyond any normal Activation Cost for the Offensive Maneuver.
#In such circumstances, the aggressor resolves his Maneuver first and only then does the defender resolve his Offensive Maneuver, should he still have the required dice in his MP to do so.
#Sneaking in an attack does not in itself turn the previous defender into the aggressor; he still begins the next Exchange as the defender, and his opponent the aggressor. However, should the defender manage to inflict a higher wound level upon the aggressor than he received himself, he now assumes the role of aggressor.
#Visibility has a profound effect on combat. In dim lighting (for example, dusk) deduct 1 die from all Melee Pools. During hours of darkness (moonlight) reduce all MPs to ¾. In pitch black conditions drop all MPs to half value.
#Archery Pools are effected twice as severly as MPs. Deduct 2 dice from all APs for dim lighting and drop it to half value for darkness. In pitch black conditions, all APs are at 0 dice.
#Weapon Reach plays an enormous role in any combat. Weapon Reach is in six distinct Steps:
#1. Hand: Fists, daggers, knee-strikes, grappling, etc.
#2. Short: Long daggers, shortswords, maces, etc.
#3. Medium: Arming swords, ball-and-chains, sabers, short spears, etc.
#4. Long: Hand-and-a-half swords, rapiers, spears, short pole-arms, etc.
#5. Very Long: Greatswords, long pole-arms, etc.
#6. Extremely Long: Lances, pikes, etc.
#Attacks against a longer weapon are made at -1 MP for each “Step” (i.e.: Short to Medium, or Medium to Long) the attacker wishes to close; attacking a pikeman with a dagger would cost 5MP! 
#This penalty holds until the shorter weapon makes a damaging strike, after which the penalty transfers to the longer weapon until he scores a damaging blow, when again the penalty goes to the shorter weapon. When the shorter weapon is out orange this penalty applies only to attacks; when the longer weapon is penalized, it applies to both offense and defense. 
#Often the best course of action for long weapons is to use a full evasion in the event of sudden close combat, or to drop weapons and wrestle!
#Certain maneuvers (such as the Half-sword) are particularly effective in such situations. 
#Likewise, many weapons—such as spears and other two-handed weapons—may shorten their reach.
#Botching in combat is left for the referee to introduce as Complications at dra-matic moments, to spice up events, increase tension, and put pressure on the PCs. Still, if a group absolutely feels it has to have a mechanic for random botches, this optional rule can be used:
#When an attack or defence comes up with 0 successes, a botch results. No Com-plication arises from this botch, but the character’s MP for the remainder of the Combat Round, or the following Combat Round if the botch occurs on the second Exchange, is reduced by the number of dice rolled on the botched Check.
#In addition, if the botched roll was made with 5+ dice, something else detrimental also happens. The exact nature of this fumble is up to the referee, but most likely occurrences are the weapon breaking or slipping from the character’s hand, or the character slipping and falling.

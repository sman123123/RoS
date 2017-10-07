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
            





















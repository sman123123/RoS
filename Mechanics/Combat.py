import random
#put from Mechanics to play from Main file.
from Mechanics import HitZones
from Mechanics import OffensiveManeuvers
from Mechanics import DefensiveManeuvers
from Gladiator import GladiatorMain
CurrentExchange = 1
CurrentMeleePool = GladiatorMain.Player.reflex + GladiatorMain.Player.proficiency
CurrentAggressiveAC = 0
CurrentDefensiveAC = 0
#Pools
    #Melee Pool: Reflex + Weapon Proficiency
    #Archery Pool: Aim + Missile Proficiency

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
while True:
    try:
        Stance = input("Which stance will you take? Aggressive, Neutral, or Defensive?\n>").lower().split()
    except ValueError:
        print("Sorry, I didn't understand that!")
        continue
    #Aggressive stances provide an attack bonus at the cost of making one’s defense more difficult. Such stances add 2 MP dice for an attack but increase activation costs for any Defensive Maneuver by 2 MP.
    if Stance[0] == "aggressive":
        CurrentMeleePool = CurrentMeleePool + 2
        CurrentDefensiveAC = CurrentDefensiveAC + 4
        print("You assume an aggressive stance.")
        break
    #Neutral stances are the favorite of many. In a Neutral stance one’s weapon is positioned to allow for either quick attack or defensive response. Neutral stances provide no bonus to either attack or defense.
    elif Stance[0] == "neutral":
        print("You assume a neutral stance.")
        break
    #Defensive stances grant a defensive bonus while making attack execution more difficult. Such stances add 2 MP dice when Defending but increase the activation costs for any Offensive Maneuver by 2 MP.
    elif Stance[0] == "defensive":
        CurrentMeleePool = CurrentMeleePool + 2
        CurrentAggressiveAC = CurrentAggressiveAC + 4
        print("You assume a defensive stance.")
        break
#Note: Stances are only in effect until the first blow or movement — once a character’s weapon moves, the stance is gone. Once melee is joined the stances of both attacker and defender are treated as neutral, with no bonus conveyed to either. A stance cannot be taken (or regained) until the combatants separate for a full pause.

#Initiative is determined after any stances are declared, when each combatant announces their intent to either attack or defend.
while True:
    while True:
        try:
            PlayerInitiative = input("Will you attack or defend?\n>").lower().split()
        except ValueError:
            print("Sorry, I didn't understand that!")
            continue
        
        if PlayerInitiative[0] == "attack":
            Aggressor = True
            break
        
        elif PlayerInitiative[0] == "defend":
            Aggressor = False
            break

    EnemyAggressor = random.randint(1, 2)
    if EnemyAggressor == 1:
        EnemyAggressor = True
    elif EnemyAggressor == 2:
        EnemyAggressor = False

    if Aggressor == True and EnemyAggressor == True:
        print("You both attack!")
        Attacker = True
        EnemyAttacker = True
        Defender = False
        EnemyDefender = False
        break
    elif Aggressor == True and EnemyAggressor == False:
        print("The enemy defends against your attack!")
        Attacker = True
        EnemyAttacker = False
        Defender = False
        EnemyDefender = True
        break
    elif Aggressor == False and EnemyAggressor == True:
        print("You defend against the enemy's attack!")
        Attacker = False
        EnemyAttacker = True
        Defender = True
        EnemyDefender = False
        break
    elif Aggressor == False and EnemyAggressor == False:
        print("You circle around each other.")
        continue

#The intent of the combatants will usually be very clear from the circumstances under which they enter combat – more often than not, one or even both will charge the other. Apart from of course counting as an aggressive stance, such a charge automatically suggests the intent to attack, leaving the other party to decide whether to receive the charge with a defence or to himself attack.
#Some rare combat encounters, for example formal duels or gladiatorial bouts, may however start out less unambiguous, with both combatants gauging each other, shifting from stance to stance and waiting for an opening in their opponent’s defence to attack. In these cases it is advisable to demand that both parties declare intent to attack or defend simultaneously, maybe by lifting one finger for attack and two for defence. Until at least one party declares attack, the bout does not actually commence.
#If a party fails to declare intent while the other declares attack, then this character is considered to have hesitated and may only defend for one full Combat Round – if even that (see Surprise).

#The attacker, now having the initiative, declares how many dice from his Melee Pool are being spent on the attack, where the attack is aimed, and what Maneuver is being used.
if Attacker == True:
    while True:
        try:
            SpentMP = int(input("You have " + str(CurrentMeleePool) + " MP left, how many points will you assign to the attack?\n>"))
        except ValueError:
            print("Sorry, I didn't understand that!")
            continue
        if CurrentMeleePool - SpentMP < 0:
            print("You cannot spend more MP than you have!")
            continue
        else:
            break
    CurrentMeleePool = CurrentMeleePool - SpentMP
    #The defender in response to the attacker declares how many dice from his Melee Pool are going towards defense, what defense is being used, and what Maneuver is being executed. 
elif Defender == True:
    while True:
        try:
            SpentMP = int(input("You have " + str(CurrentMeleePool) + " MP left, how many points will you assign to the defense?\n>"))
        except ValueError:
            print("Sorry, I didn't understand that!")
            continue
        if CurrentMeleePool - SpentMP < 0:
            print("You cannot spend more MP than you have!")
            continue
        else:
            break

#If both combatants declare as aggressors, Offensive Maneuvers and assigned dice are announced before the Reflex Check to see who goes fractionally first. The combatant with the higher Reflex may choose whether to declare first or second; tied Reflex scores are broken by the higher CG score, and tied CG scores by the higher Proficiency.
if Attacker == True and EnemyAttacker == True:
    #Enemy must announce maneuver type and spent MP.
    pass
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
#This penalty holds until the shorter weapon makes a damaging strike, after which the penalty transfers to the longer weapon until he scores a damaging blow, when again the penalty goes to the shorter weapon. When the shorter weapon is out of

#6. TERRAIN CHECKS
#Terrain Checks in Blade take place within the abstracted combat environment. 
#During a melee, it is not only common but actually necessary that combatantstwist and turn about, advance and step back, so that once a combat begins, all fight-ers will by default move significantly from the spot they occupied at its outset. 
#Even a single Combat Round might easily shift the combatants as much as five meters in an unforeseen direction, and frequently more; that’s the nature of footwork.
#Once a combat with multiple fighters has been underway for even one Round, it is nigh impossible to determine where anyone is in respect to anyone else – except as it relates to one’s own immediate opponents. 
#Their own footwork, the press of enemies, and wheeling manoeuvres will have carried every pair of fighters in a largely random direction, where allies who started out fighting side by side will by necessity find themselves separated very quickly. 
#In short, as long a Limelight is underway, it is impossible to tell where anyone is in respect to anyone else.
#Locations are roughly re-established once a Limelight ends, and with certainty when a Round of Limelights completes. Positions are determined by the ref ’s common sense, based on what has happened during the previous Round of Limelights. 
#As a player vividly describes his combat actions, the ref is encouraged to take note and visualize the PCs end location within the combat environment. It can thus happen that a player finds his PC in a location where he doesn’t want him to be, which is only a concern if the PC is desperately needed elsewhere. 
#If the character wants to engage somebody who is quite distance away, or get to any other location in the combat environment, this is not handled by measuring movement, but by a Terrain Check.
#A Terrain Check is made with dice from the character’s MP – any number of dice, player’s choice. The ref sets the Difficulty of the Check by how far and over what dif-ficult terrain the character will have to move, but it will rarely, if ever, be greater than a Difficult Challenge Rating. 
#If the optional Encumbrance rules are being used, every Terrain Check other than one for bad footing or refusing to be dislodged from a fixed location carries an Activation Cost that can be found in Table 5.3. If several such Terrain Checks should be made during the same Combat Round, this Activation Cost must be paid separately for every Check.
#If the Check is passed, the character arrives at the point he wanted to reach “in time”, whatever that may mean (usually to engage somebody in melee with the dice remaining in his MP), and if not, he arrives there “late”.
#Example: Returning to where we abandoned Otho in the previous example, right after spending a point of Drama to have his Limelight out of the usual order to rush to Rufo’s aid, the ref tells Otho’s player that 2 Successes on the Terrain Check are necessary to get to Rufo’s side in time. 
#Playing it safe, Otho’s player opts to spend 6 dice, and achieves 3 successes. Rushing at Rufo’s enemy, Otho attacks with the remaining dice in his MP, just in time to save his companion.
#Failing this kind of Terrain Check should only rarely, if at all, be interpreted as the player having wasted his Limelight on a failed attempt. Instead, the ref should give him something else to do, or a new unexpected challenge. 
#A failure might for example be interpreted as the character being intercepted by new enemy, if applicable.
#The use of Terrain Checks are not limited to simply getting somewhere on time. A Terrain Check may also be needed to navigate an area with poor footing. 
#Normal footing like broken ground, light snow, mud, or deep sand do not necessitate a Check, but truly poor areas such as steep, slippery slopes, scree fields, stairs, narrow ledges, ice, deep snow, or water and the like, do. 
#If all combatants of a particular Melee are on this kind of difficult ground, 2 dice are deducted from everyone’s MP and the need for a Check simply done away with. If only one combatant is on poor ground, a Terrain Check must be made for that character. 
#If he achieves even a single Success with the dice he sets aside for this purpose, he can act and move normally, but if not, he slips, stumbles, or falls down.
#It is thus clearly advantageous to fight on level ground while forcing one’s oppo-nent into a position of poor footing. Provided there is poor ground nearby, Terrain Checks can also be used to force an opponent onto such bad footing, and keep him there, or to get out of it oneself. 
#Such attempts are handled through an Opposed Terrain Check.
#The initiator of the attempt announces a number of dice from his MP to be used,after which his opponent sets aside a number of dice from his MP as well, then both roll. To win the contest, the initiator needs a Quality of Success of 1 if he is currently the aggressor, or 2 if the defender – it is easier to force somebody somewhere than to lure him. 
#This can even be used to force somebody over a nearby drop, but only if initiated by the aggressor. As people are remarkably reluctant to fall from heights, success on such an attempt does not simply require a Quality of Success of 1, but now at least 3, provided that the drop is of a kind likely to injure the falling person.
#In many cases, somebody on bad footing facing an enemy on level ground need not force his opponent back so that he can get firm footing himself, but may well opt to simply step back up a pace or two, enticing the opponent to follow him onto the disadvantageous ground and thus evening the odds. 
#This need merely be announced and requires just a normal Terrain Check to avoid slippage on the poor surface, no opposed roll needed; if the opponent declines to follow, the bout ends.
#However, it is not always feasible to entice the opponent to follow; sometimes one will want to, and have to, fight one’s way onto the opponent’s better ground. 
#If the opponent is for example holding the head of a stairway or the top of a steep slope against all comers, no normal amount of enticement will force him down to his opponent.
#While these cases assume at least some room for lateral movement on the holding character’s part, there may be other scenarios, where he cannot move anywhere at all, such as when defending a doorway. 
#While such positions are advantageous in terms of limiting the number of possible attackers, they interdict footwork and thus cramp combat performance. 
#An attempt to remain firmly in one spot requires but one Success on a Terrain Check – if unopposed. If an enemy is actively trying to dislodge one from a position he is holding, the Terrain Check becomes Opposed. 
#The initiator of the attempt, who must be the current aggressor, declares the number of dice committed, after which his enemy does the same, then both roll. To dislodge the holding person, a victory with a QoS of 1+ is needed; ties signify that the holding opponent remains firmly in place.
#Higher footing (as provided by stairs or horses) adds 2 MP at the beginning of the Round (Step 2). This also affects attack zone targeting for all involved combatants according to common sense. 
#Finally, Terrain Checks can be used by a player with multiple opponents to avoid facing several at once. By moving so that his opponents foul each other’s attacks, and by exploiting the environment, the combatant tries to limit the number of op-ponents he fights this Combat Round. If these opponents are important NPCs, the Terrain Check is an Opposed one. 
#The player declares which opponent he wants to avoid. This opponent announces a number of dice from his MP to oppose the PC’s attempt to avoid him, and the player then sets aside a number of dice from his MP himself. An Opposed Check using these dice is then made. A Quality of Success of 0 suffices to attain the player’s objective if the PC wasn’t engaged with the opponent in the previous Combat Round, but a QoS of 1 is required to avoid an opponent with whom he was previously engaged.
#This means of breaking off a combat bout can only be used if facing multiple opponents at once, as it represents moving in a manner that has one opponent getting in the other’s way. If facing only one opponent, a bout can only be broken off after a successful Full Evasion, or if both combatants decline to attack.
#If the first opponent is thus avoided, the next opponent is treated in the same fashion. A number of dice from both MPs are again set aside and an Opposed Check made. The QoS of the previous Opposed Terrain Check for avoiding the first opponent is added as bonus dice to this second Check. There are no additional Checks needed, as it is physically impossible for more than three opponents to beset the same person at the same time.
#If the enemies aren’t important NPCs, the Terrain Check is unopposed. If the PC is trying to avoid one of his two opponents, he simply needs a Quality of Success of 1.
#If he is facing three opponents, a Quality of Success of 3 is required to avoid two opponents, while a QoS of 2 avoids one. At the very outset of the battle, the required QoS for avoiding one or two out of three opponents are reduced by one, provided the PC is not surrounded by his opponents. A QoS of 2 avoids two out of three opponents, and a QoS of 1 one out of three. As soon as the PC has become engaged in combat with any of his opponents, this reduced QoS to avoid opponents no longer applies, nor does it apply if the PC started out surrounded or in a comparably disadvantageous position.
#Please note that a character may use a Terrain Check to move into positions where the number of opponents who can engage him at once is limited, for example with his back against a wall. In such an instance a maximum of only two, not three opponents can attempt to engage the character at the same time.
#There are a few further uses for Terrain Checks, which are discussed in the section on ranged combat.

#7. FATIGUE IN THE COMBAT SCENE
#Fatigue is an optional rule used only in combat situations. No one enters a Combat Scene fatigued – if he might be considered fatigued from previous strenuous activity, the rush of adrenaline at the onset of a new combat can be considered to have temporarily drowned out any previous exhaustion.
#At the end of every Limelight, a character who engaged in highly strenuous activity like fighting must check BN, the Challenge Level of this Check being equal to one’s Encumbrance level plus one, or 1 if the optional Encumbrance mechanic is not being used. Passion Atributes do not aid with this Check, but the rules for automaticsuccesses (dice pool higher than three times the required QoS) do apply; dropping from fatigue is not something much in keeping with most protagonists of Sword & Sorcery.
#If this Check is failed, the character accrues a penalty of 2 dice on his MP, AP and SP pools, similar to (and cumulative with) diziness from Blood Loss. Also as with Blood Loss, his Attribute and Skill Checks will need 1 additional Success per full 4 dice Fatigue penalty to MP, AP and SP. Unlike Blood Loss, the BN Check to avoid further Fatigue is not exempt from this requirement for additional Successes.
#All Fatigue is reduced to 0 by spending but a single Limelight resting and catching one’s breath (no more strenuous activity than walking slowly). If a character spends a Limelight in light activity (nothing more strenuous than a slow jog), his Fatigue penalty is reduced by 2.

#II. Defense 
#Defense focuses squarely on a warrior’s efforts to avoid being struck by an opponent. 

#1. EVASION 
#Evasion can be done by anyone and used with every Proficiency. It doesn’t carry any Activation Cost, unless the character is encumbered and the optional Encumbrance rules are being used. In that case, there is an Activation Cost; it can be found on Table 5.3.
#Table 4.3 provides TNs for the three common forms of evasion.
#Full Evasion if successful, brings all melee to a halt as the fighters separate and possibly attempt to re-establish initiative. The bout ends, at least for the moment, and stances can once again be assumed. If a character conducts multiple Full Evasions during an Exchange, the QoS of the immediately preceding Full Evasion is added as bonus dice to the immediately following Full Evasion.
#Partial Evasion, if successful, does not allow the defender to assume the role of aggressor as usual. No matter what the actual QoS of the successful Partial Evasion, assuming the role of aggressor requires the immediate expenditure of 2 MP. If the successful defender is unwilling or unable to spend those dice out of the MP still remaining for the Exchange on which the Partial Evasion was performed, the aggressor retains his role.
#Duck and Weave if successful, gives the evading warrior a great opportunity to strike his opponent. He automatically assumes the role of aggressor (even if his QoS was merely 0) and moves into the optimum range for his weapon’s Reach. His opponent may not employ a shield against his follow-up attack on the next Exchange, and loses dice from his MP equal to the successes on the attack roll Duck and Weave defended against successfully. Should this penalty take the MP into the negative range, those dice are added as bonus dice to the other party’s MP.
#Evasion can also be used to defend against missile attacks, provided the defending person is aware of them. The TN for this is 8 (Partial Evasion) for thrown weapons, and 10 (“Duck and Weave”) for arrows, crossbow bolts, and bullets.
#If the defending person is both aware that a gun, bow, or crossbow is being aimed at him, and has the opportunity to start evasive movement before the missile is fired, the Evasion TN is now merely 8 (Partial Evasion). This represents weaving around in a highly unpredictable way. If the character is at the time engaged in a bout of melee combat, his unpredictable combat moves automatically count as this type of weaving movement, allowing him to use the Partial Evasion TN against a missile attack.
#Evading missile attacks as outlined above is also possible when a character is not in a melee situation. In this case, he may use dice equal to half his best MP, even if he may not currently have the equipment necessary for fighting with that Proficiency at hand. Applicable PAs figure normally in this halved MP, i.e. they are added before dividing the pool in two.
#When a character does during an Exchange use Duck & Weave as a defense against either a melee or a missile attack, the result of this single Duck & Weave is applied against all missile attacks aimed at him during this Exchange. Equally, if a character not currently in a melee is fired upon uses Evasion to defend against one missile attack, the result of this one roll is applied against all missile attacks upon him within this Combat Round. 
#Should he be targeted by both thrown and launched weapons, requiring different TNs to defend against (8 and 10), a single roll is still used to defend against all of them, but this roll will still cover two different QoSs, one against TN 8 and one against TN 10.
#Example: Otho evades both a javelin and a crossbow. He is not aware of the crossbowman and does not use erratic movement, so his DTN against the javelin is 8 and against the crossbow bolt 10. His MP is 13, but a she is currently not in a melee, he rolls half his MP, i.e. 7 dice. The dice come up 2, 5, 6, 7, 8, 10, 12 – he has 3 successes against the javelin (8, 10, 12) and 2 against the crossbow (10, 12).
#If somebody fires into a melee combat, the missile attack is always resolved on Exchange 1.

#2. DEFENSIVE ACTIONS
#The bedrock of all Defensive Maneuvers discussed in Chapter Three is the Block, the Parry, and the before mentioned Evasion. Most defensive Maneuvers are directly tied to these basics.
#Parrying is the preferred defense of warriors everywhere. Most warriors grasp the basic idea of turning the attack of an opponent’s weapon with their own. Any amount of MP dice may be devoted to parrying while defending. The challenge of deflecting another’s weapon is reflected by the defending weapon’s Defense Target Number (DTN).
#Some weapon schools, for instance those of the Cut & Thrust Proficiency, teach using a secondary parrying weapon, usually a dagger, in the off hand, allowing the person thus armed to potentially parry twice in a single Exchange or to perform such Maneuvers as Simultaneous Block/Strike. 
#However, though parrying does not involve great manual dexterity, a person’s secondary arm is still handicapped. The DTN of any parry conducted with the offhand is therefore increased by +1.
#Blocking is the action of interposing an object, usually a shield, between oneself and the attack, perhaps in a rather unsophisticated way, but also by skilfully angling a shield, or using it offensively to beat aside an attacking weapon. 
#In this use it is not dissimilar to parrying. Every blocking object is assigned a TN for defending with it, this TN being dependent on the size of the object, and how quickly and gracefully it can be moved. 
#It is thus almost identical to a weapon’s DTN, but with one important difference: Shields (and only shields, not improvised blocking objects like chairs and the like) are designed to be used in the offhand and therefore suffer no penalty for being used with the “wrong” hand. 
#Shields are divided into three types, depending on size; Large, small, and bucklers.
#A large shield is just that – a very large shield, measuring over one meter in length if an oblong shape, or having a diameter of not much less than one meter if more squarish or round. It offers superior protection but is unwieldy to carry about andvery awkward to use on horseback as one’s horse constantly gets in the way of the shield. On the positive side, most large shields are big enough to completely hunker down behind, removing its owner, provided he remains static, completely from the danger of missile attacks.
#Chart page 118
#A small shield is anything clearly larger than a buckler and smaller than a large shield. It is very versatile and of equal use on foot or horseback.
#Finally, a buckler is a very small, but agile shield, never strapped to the arm, but always carried in a fist grip. It is rarely any larger than 0.3 meters in diameter.
#All types of shields have variable DTNs against different forms of attack such as melee, missile attacks with thrown weapons such as javelins or hatchets, or against “fired” projectiles like arrows, crossbow bolts, and sling stones – though fired objects are often so fast (causing the defender to roll vs. a high DTN) as to often rule out blocking as a viable defence against fired missiles. 
#The applicable Defensive Target Number depends on both the type of shield, and the attack being resisted. See Table 4.4.

#3. ARMOR OVERVIEW
#The function of armor is to reduce or outright prevent injury to somebody being hit in armoured spot. It does so by reducing the Wound Level of any hit to an armoured location by the Armor Value (AV) of that armor. If the Wound Level is thus reduced to 0 or less, no wound is inflicted.
#But armor in Blade does not equally apply to all locations of the armoured person, but to each location only to the extent that armor is worn in exactly the spot being struck. 
#Somebody wearing a short tunic of sturdy leather and an iron helmet will thus have a different AV to the crown of his head than to his guts or shins. It is therefore essential to record which spot is armoured to what degree, and the Blade character sheet provides space for such notation.
#Armor doesn’t provide the same AV against all types of damage; a thickly padded gambeson will for example provide decent protection against Blunt damage, but much less so against Piercing. 
#Each and every armor has three AVs, one against Piercing, one against Blunt, and one vs. Cleaving. These AVs can be found in Table 4.5.
#Not all armors have an AV against Cleaving damage. Metal armors are virtually impossible to actually cut through with any weapon driven by human strength; the most that can be achieved is a dent or a very small rip, a far cry from a serious wound. 
#But that doesn’t mean that the wearer of such armor is immune against Cleaving weapons – even if a blade does not actually cut such armor, the impact will still transfer Blunt trauma through the armor, possibly breaking bones, or perhaps even killing, all without greatly damaging the armor.
#For this reason, all weapon stats in the Appendix include Blunt DRs, even those that traditionally in RPG games haven’t caused Blunt damage, such as swords. 
#Armor lacking a Cleaving AV uses Blunt AV against Cleaving attacks, while attacking weapons calculate damage inflicted against such armor not with Cleaving, but with Blunt DR.

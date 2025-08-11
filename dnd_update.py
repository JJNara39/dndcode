import random
import math


#Define a function called hpcalc that determines your hp, given your level, and what dice you give it
def hpcalc(chlvl, dicefunc, sides):
    result = 0
    for i in range(chlvl):
        result += dicefunc(sides)  # Call the function with the sides
    return result

def dice(sides):
    # Rolls a dice with dicenum sides
    result = random.randint(1, sides)
    return result

def dnd_update(player):
    player.ChaMod = math.floor((player.ability_scores["Charisma"]-10)/2)
    player.ConMod = math.floor((player.ability_scores["Constitution"]-10)/2)
    player.DexMod = math.floor((player.ability_scores["Dexterity"]-10)/2)
    player.IntMod = math.floor((player.ability_scores["Intelligence"]-10)/2)
    player.StrMod = math.floor((player.ability_scores["Strength"]-10)/2)
    player.WisMod = math.floor((player.ability_scores["Wisdom"]-10)/2)       


    #### race section ####
    if player.race == "Aarakocra":
        player.attacksspellcasting = {
            "Unarmed Strikes: Talons": {
                'Name' : "Unarmed Strikes: Talons",
                'Modifier': "STR",
                'Damage' : "1d6",
                'Damage Type' : "Slashing",
            }
        }
    if player.race == "Aasimar":
        player.notes["Healing Hands"] = f"As an action, you can touch a creature and cause it to regain a number of hit points equal to your level, {player.level}. Once you use this trait, you can't use it again until you finish a long rest."
        #Healing Hands falls under general notes, if touch == True and Healing Hands = True, then they heal X hp
        if player.subrace == "Protector Aasimar":
            if player.level >= 3:
                player.notes["Radiant Soul"] = f"You can use your action to unleash the divine energy within yourself, causing your eyes to glimmer and two luminous, incorporeal wings to sprout from your back.\nYour transformation lasts for 1 minute or until you end it as a bonus action. During it, you have a flying speed of 30 feet, and once on each of your turns, you can deal extra radiant damage to one target when you deal damage to it with an attack or a spell. The extra radiant damage equals your level, {player.level}.\nOnce you use this trait, you can't use it again until you finish a long rest."
                #if flight !in speed and Radiant Soul is active, then they gain following flight
                player.speed["Flight"] = "30ft"
        if player.subrace == "Scourge Aasimar":
            if player.level >= 3:
                player.notes["Radiant Consumption"] = f"You can use your action to unleash the divine energy within yourself, causing a searing light to radiate from you, pour out of your eyes and mouth, and threaten to char you.\nYour transformation lasts for 1 minute or until you end it as a bonus action. During it, you shed bright light in a 10-foot radius and dim light for an additional 10 feet, and at the end of each of your turns, you and each creature within 10 feet of you take radiant damage equal to half your level (rounded up), or {math.ceil(player.level/2)}. In addition, once on each of your turns, you can deal extra radiant damage to one target when you deal damage to it with an attack or a spell. The extra radiant damage equals your level, {player.level}.\nOnce you use this trait, you can't use it again until you finish a long rest."
        if player.subrace == "Fallen Aasimar":
            if player.level >= 3:
                player.notes["Necrotic Shroud"] = f"You can use your action to unleash the divine energy within yourself, causing your eyes to turn into pools of darkness and two skeletal, ghostly, flightless wings to sprout from your back. The instant you transform, other creatures within 10 feet of you that can see you must succeed on a Charisma saving throw, DC 8 + your proficiency bonus + your Charisma modifier, or DC = {8+player.profbonus+player.ChaMod} or become frightened of you until the end of your next turn.\nYour transformation lasts for 1 minute or until you end it as a bonus action. During it, once on each of your turns, you can deal extra necrotic damage to one target when you deal damage to it with an attack or a spell. The extra necrotic damage equals your level, {player.level}.\nOnce you use this trait, you can't use it again until you finish a long rest."
    if player.race == "Autognome":
        player.notes["Healing Machine"] = f"If the Mending spell is cast on you, you can spend a Hit Die, roll it, and regain a number of hit points equal to the roll plus your Constitution modifier, roll + {player.ConMod}, minimum of 1 hit point.\nIn addition, your creator designed you to benefit from several spells that preserve life but that normally don't affect Constructs: Cure Wounds, Healing Word, Mass Cure Wounds, Mass Healing Word, and Spare the Dying."
        #Combat notes
        player.armor_class = 13 + player.DexMod
    if player.race == "Centaur":
        player.attacksspellcasting = {
            "Unarmed Strikes: Hooves": {
                'Name' : "Unarmed Strikes: Hooves",
                'Modifier': "STR",
                'Damage' : "1d4",
                'Damage Type' : "Bludgeoning",                
            }
        }
    if player.race == "Cervan":
        if player.subrace == "Pronghorn Cervan":
            player.attacksspellcasting = {
                "Unarmed Strikes: Antlers": {
                    'Name' : "Unarmed Strikes: Antlers",
                    'Modifier': "STR",
                    'Damage' : "1d6",
                    'Damage Type' : "Piercing",                    
                }
            }         
    if player.race == "Corginian":
        player.attacksspellcasting = {
            "Unarmed Strikes: Strong Jaw": {
                'Name' : "Unarmed Strikes: Strong Jaw",
                'Modifier': "STR",
                'Damage' : "1d4",
                'Damage Type' : "Piercing",                
            }
        }    
    if player.race == "Corvum":
        player.attacksspellcasting = {
            "Unarmed Strikes: Talons": {
                'Name' : "Unarmed Strikes: Talons",
                'Modifier': "STR",
                'Damage' : "1d4",
                'Damage Type' : "Piercing",                
            }
        }     
    if player.race == "Dhampir":
        player.attacksspellcasting = {
            "Natural Weapon: Fangs": {
                'Name' : "Natural Weapon: Fangs",
                'Modifier': "CON",
                'Damage' : "1d4",
                'Damage Type' : "Piercing",                
            }
        }   
    if player.race == "Elf":
        if player.subrace == "Eladrin":
            if player.season == "Spring":
                if player.level >= 3:
                    player.notes["Fey Step(Spring)"] = "When you use your Fey Step, you can touch one willing creature within 5 feet of you. That creature then teleports instead of you, appearing in an unoccupied space of your choice that you can see within 30 feet of you."
                if player.level >= 3:
                    player.notes["Fey Step(Summer)"] = "Immediately after you use your Fey Step, each creature of your choice that you can see within 5 feet of you takes fire damage equal to your Charisma modifier (minimum of 1 damage)."
                if player.level >= 3:
                    player.notes["Fey Step(Autumn/Fall)"] = "Immediately after you use your Fey Step, up to two creatures of your choice that you can see within 10 feet of you must succeed on a Wisdom saving throw or be charmed by you for 1 minute, or until you or your companions deal any damage to it."
                if player.level >= 3:
                    player.notes["Fey Step(Winter)"] = "When you use your Fey Step, one creature of your choice that you can see within 5 feet of you before you teleport must succeed on a Wisdom saving throw or be frightened of you until the end of your next turn."
    if player.race == "Hedge":
        player.armor_class = 14 + player.DexMod
        if player.curlup == True: #currently this isn't implemented
            player.armor_class = 19
    if player.race == "Leonin":
        player.attacksspellcasting = {
            "Unarmed Strikes: Claws": {
                'Name' : "Unarmed Strikes: Claws",
                'Modifier': "STR",
                'Damage' : "1d4",
                'Damage Type' : "Slashing",                
            }
        }      
    if player.race == "Lizardfolk":
        player.attacksspellcasting = {
            "Unarmed Strike: Bite": {
                'Name' : "Unarmed Strike: Bite",
                'Modifier': "STR",
                'Damage' : "1d6",
                'Damage Type' : "Piercing",                
            }
        }   
        if player.armordon == False: #armordon is not implemented, but also there is an additional note
            player.armor_class = 13+player.DexMod
    if player.race == "Locathah":
        if player.armordon == False: #armordon is not implemented, but also there is an additional note
            player.armor_class = 12+player.DexMod 
    if player.race == "Loxodon":
        if player.armordon == False: #armordon is not implemented, but also there is an additional note
            player.armor_class = 12+player.ConMod                               
    if player.race == "Minotaur":
        player.attacksspellcasting = {
            "Unarmed Strike: Horns": {
                'Name' : "Unarmed Strike: Horns",
                'Modifier': "STR",
                'Damage' : "1d6",
                'Damage Type' : "Piercing",                
            }
        }      
    if player.race == "Raptor (Bird)":
        player.attacksspellcasting = {
            "Unarmed Strike: Talons": {
                'Name' : "Unarmed Strike: Talons",
                'Modifier': "STR",
                'Damage' : "1d4",
                'Damage Type' : "Piercing",                
            }
        }       
    if player.race == "Sharkin":
        player.sharkinviciousbitedmg = "1d6"
        if ((player.level >= 5) and (player.level < 10)):
            player.sharkinviciousbitedmg = "2d6"
        if ((player.level >= 10) and (player.level < 20)):
            player.sharkinviciousbitedmg = "3d6"
        if player.level == 20:
            player.sharkinviciousbitedmg = "4d6"
        player.attacksspellcasting = {
            "Vicious Bite": {
                'Name' : "Vicious Bite",
                'Modifier': "STR",
                'Damage' : "ViciousBite",
                'Damage Type' : "Piercing",                
            }
        }       
    if player.race == "Shifter":
        if player.subrace == "Beasthide Shifter":
            if player.shiftershift == True: #not implemented yet
                player.armor_class += 1            
        if player.subrace == "Longtooth Shifter":
            player.attacksspellcasting = {
                "Unarmed Strikes: Fangs": {
                    'Name' : "Unarmed Strikes: Fangs",
                    'Modifier': "STR",
                    'Damage' : "1d6",
                    'Damage Type' : "Piercing",                    
                }
            }         
    if player.race == "Strig":
        player.attacksspellcasting = {
            "Unarmed Strikes: Talons": {
                'Name' : "Unarmed Strikes: Talons",
                'Modifier': "STR",
                'Damage' : "1d4",
                'Damage Type' : "Piercing",                
            }
        }      
    if player.race == "Tabaxi":
        player.attacksspellcasting = {
            "Unarmed Strikes: Cat Claws": {
                'Name' : "Unarmed Strikes: Cat Claws",
                'Modifier': "STR",
                'Damage' : "1d4",
                'Damage Type' : "Slashing",                
            }
        }        
    if player.race == "Thri-Kreen":
        if player.armordon == False: #armordon is not implemented, but also there is an additional note
            player.armor_class = 13+player.DexMod #if not wearing armor        
    if player.race == "Tortle":
        player.attacksspellcasting = {
            "Unarmed Strikes: Claws": {
                'Modifier': "STR",
                'Damage' : "1d4",
                'Damage Type' : "Slashing",                
            }
        }       
    if player.race == "Vulpin":
        player.attacksspellcasting = {
            "Unarmed Strikes: Bite": {
                'Modifier': "Finesse",
                'Damage' : "1d6",
                'Damage Type' : "Piercing",                
            }
        }       

#### class section

    if player.level >= 4:
        player.notes["Ability Score/Feat(1)"] = "You can increase one score by 2, two by one, or a feat. As normal, you can't increase an ability score above 20 using this feature."
    if player.level >= 8:
        player.notes["Ability Score/Feat(2)"] = "You can increase one score by 2, two by one, or a feat. As normal, you can't increase an ability score above 20 using this feature."
    if player.level >= 12:
        player.notes["Ability Score/Feat(3)"] = "You can increase one score by 2, two by one, or a feat. As normal, you can't increase an ability score above 20 using this feature."   
    if player.level >= 16:
        player.notes["Ability Score/Feat(4)"] = "You can increase one score by 2, two by one, or a feat. As normal, you can't increase an ability score above 20 using this feature."
    if player.level >= 19:
        player.notes["Ability Score/Feat(5)"] = "You can increase one score by 2, two by one, or a feat. As normal, you can't increase an ability score above 20 using this feature."          

    for i in range(len(player.Class)):

        if player.Class[i] == "Artificer":
            player.hitdice["Artificer Hitdie"] = f"{player.artlvl}d8"
            if player.artlvl == 1:
                player.hitpoints += (8 + player.ConMod)
            else:
                player.hitpoints += (8 + player.ConMod + hpcalc(player.artlvl, dice, 8))
            if player.artlvl >= 2:
                player.artinfknown = 4
                player.artinfitems = 2
                player.notes["Artificer 1st Level Spell Slots Known"] = 2
            if player.artlvl >= 3:
                player.notes["Artificer 1st Level Spell Slots Known"] = 3
            if player.artlvl >= 5:
                player.notes["Artificer 1st Level Spell Slots Known"] = 4
                player.notes["Artificer 2nd Level Spell Slots Known"] = 2
            if player.artlvl >= 6:
                player.artinfknown = 6
                player.artinfitems = 3                
            if player.artlvl >= 7:
                player.notes["Artificer 2nd Level Spell Slots Known"] = 3
            if player.artlvl >= 9:
                player.notes["Artificer 3rd Level Spell Slots Known"] = 2
            if player.artlvl >= 10:
                player.artinfknown = 8
                player.artinfitems = 4  
                player.notes["Artificer Cantrips Known"] = 3
            if player.artlvl >= 11:
                player.notes["Artificer 3rd Level Spell Slots Known"] = 3                               
            if player.artlvl >= 14:
                player.artinfknown = 10
                player.artinfitems = 5 
                player.notes["Artificer Cantrips Known"] = 4               
            if player.artlvl >= 15:
                player.notes["Artificer 4th Level Spell Slots Known"] = 2
            if player.artlvl >= 17:
                player.notes["Artificer 4th Level Spell Slots Known"] = 3
                player.notes["Artificer 5th Level Spell Slots Known"] = 1
            if player.artlvl >= 18:
                player.artinfknown = 12
                player.artinfitems = 6 
            if player.artlvl >= 19:
                player.notes["Artificer 5th Level Spell Slots Known"] = 2
            player.notes["Infuse Item"] = f"You have the ability to imbue mundane items with certain magical infusions. The magic items you create with this feature are effectively prototypes of permanent items. You learn additional infusions of your choice when you reach certain levels in this class. Currently you know: {player.artinfknown} infusions.\nWhenever you gain a level in this class, you can replace one of the artificer infusions you learned with a new one."
            player.notes["Infusing an Item"] = f"Whenever you finish a long rest, you can touch a nonmagical object and imbue it with one of your artificer infusions, turning it into a magic item. An infusion works on only certain kinds of objects, as specified in the infusion's description. If the item requires attunement, you can attune yourself to it the instant you infuse the item. If you decide to attune to the item later, you must do so using the normal process for attunement (see 'Attunement' in chapter 7 of the Dungeon Master's Guide).\nYour infusion remains in an item indefinitely, but when you die, the infusion vanishes after a number of days have passed equal to your Intelligence modifier, or {player.IntMod} days, minimum of 1 day. The infusion also vanishes if you give up your knowledge of the infusion for another one.\nYou can infuse more than one nonmagical object at the end of a long rest; the maximum number of objects you can infuse is {player.artinfitems} objects. You must touch each of the objects, and each of your infusions can be in only one object at a time. Moreover, no object can bear more than one of your infusions at a time. If you try to exceed your maximum number of infusions, the oldest infusion immediately ends, and then the new infusion applies."
            player.notes["Magical Tinkering"] = f"You learn how to invest a spark of magic into mundane objects. To use this ability, you must have tinker's tools or other artisan's tools in hand. You then touch a Tiny nonmagical object as an action and give it one of the following magical properties of your choice:\n - The object sheds bright light in a 5-foot radius and dim light for an additional 5 feet \n - Whenever tapped by a creature, the object emits a recorded message that can be heard up to 10 feet away \n - You utter the message when you bestow this property on the object, and the recording can be no more than 6 seconds long \n - The object continuously emits your choice of an odor or a nonverbal sound (wind, waves, chirping, or the like). The chosen phenomenon is perceivable up to 10 feet away \n - A static visual effect appears on one of the object's surfaces. This effect can be a picture, up to 25 words of text, lines and shapes, or a mixture of these elements, as you like. \n The chosen property lasts indefinitely. As an action, you can touch the object and end the property early. \n You can bestow magic on multiple objects, touching one object each time you use this feature, though a single object can only bear one property at a time. The maximum number of objects you can affect with this feature at one time is equal to your Intelligence modifier, or {player.IntMod} objects, minimum of one object. If you try to exceed your maximum, the oldest property immediately ends, and then the new property applies."
            player.spellsavedc["Artificer Spell Save DC"] = 8 + player.profbonus + player.IntMod
            player.spellattackmod["Artificer Spell Attack Mod"] = player.profbonus + player.IntMod

        if player.Class[i] == "Barbarian":
            player.hitdice["Barbarian Hitdie"] = f"{player.barblvl}d12"
            if player.barblvl == 1:
                player.hitpoints += (12 + player.ConMod)
            else:
                player.hitpoints += (12 + player.ConMod + hpcalc(player.barblvl, dice, 12))
            if player.barblvl >= 3:
                player.barbrages = 3
            if player.barblvl >= 6:
                player.barbrages = 4
            if player.barblvl >= 9:
                player.barbragedmg = 3
            if player.barblvl >= 12:
                player.barbrages = 5
            if player.barblvl >= 16:
                player.barbragedmg = 4
            if player.barblvl >= 17:
                player.barbrages = 6
            if player.barblvl == 20:
                player.barbrages = "Unlimited"
            player.notes["Rage"] = f"In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action.\nWhile raging, you gain the following benefits if you aren’t wearing heavy armor:\nYou have advantage on Strength checks and Strength saving throws.\nWhen you make a melee weapon attack using Strength, you gain a +{player.barbragedmg} to your damage roll.\nYou have resistance to bludgeoning, piercing, and slashing damage.\nIf you are able to cast spells, you can’t cast them or concentrate on them while raging.\nYour rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven’t attacked a hostile creature since your last turn or taken damage since then. You can also end your rage on your turn as a bonus action.\nOnce you have raged {player.barbrages} times, you must finish a long rest before you can rage again."
            player.notes["Unarmored Defense"] = f"While you are not wearing any armor, your Armor Class equals 10 + your Dexterity modifier + your Constitution modifier, or AC {10 + player.DexMod + player.ConMod}. You can use a shield and still gain this benefit."
        
        if player.Class[i] == "Bard":
            player.hitdice["Bard Hitdie"] = f"{player.bardlvl}d8"
            if player.bardlvl == 1:
                player.hitpoints += (8 + player.ConMod)
            else:
                player.hitpoints += (8 + player.ConMod + hpcalc(player.bardlvl, dice, 8))        
            if player.bardlvl >= 2:  
                player.bardsongrest = "d6"           
                player.notes["Bard Spells Known"] = 5
                player.notes["Bard 1st Level Spell Slots Known"] = 3    
            if player.bardlvl >= 3:
                player.notes["Bard Spells Known"] = 6
                player.notes["Bard 1st Level Spell Slots Known"] = 4
                player.notes["Bard 2nd Level Spell Slots Known"] = 2                
            if player.bardlvl >= 4:
                player.notes["Bard Cantrips Known"] = 3
                player.notes["Bard Spells Known"] = 7
                player.notes["Bard 2nd Level Spell Slots Known"] = 3                
            if player.bardlvl >= 5:
                player.bardicinspiration = "d8"
                player.notes["Bard Spells Known"] = 8
                player.notes["Bard 3rd Level Spell Slots Known"] = 2              
            if player.bardlvl >= 6:
                player.notes["Bard Spells Known"] = 9
                player.notes["Bard 3rd Level Spell Slots Known"] = 3                 
            if player.bardlvl >= 7:
                player.notes["Bard Spells Known"] = 10
                player.notes["Bard 4th Level Spell Slots Known"] = 1                   
            if player.bardlvl >= 8:
                player.notes["Bard Spells Known"] = 11
                player.notes["Bard 4th Level Spell Slots Known"] = 2                  
            if player.bardlvl >= 9:
                player.bardsongrest = "d8"           
                player.notes["Bard Spells Known"] = 12
                player.notes["Bard 4th Level Spell Slots Known"] = 3
                player.notes["Bard 5th Level Spell Slots Known"] = 1   
            if player.bardlvl > 10:
                player.bardicinspiration = "d10"
                player.notes["Bard Cantrips Known"] = 4
                player.notes["Bard Spells Known"] = 14
                player.notes["Bard 5th Level Spell Slots Known"] = 2                   
            if player.bardlvl >= 11:
                player.notes["Bard Spells Known"] = 15
                player.notes["Bard 6th Level Spell Slots Known"] = 1   
            if player.bardlvl >= 13:
                player.bardsongrest = "d10" 
                player.notes["Bard Spells Known"] = 16
                player.notes["Bard 7th Level Spell Slots Known"] = 1                   
            if player.bardlvl >= 14:
                player.notes["Bard Spells Known"] = 18
            if player.bardlvl >= 15:
                player.bardicinspiration = "d12"
                player.notes["Bard Spells Known"] = 19
                player.notes["Bard 8th Level Spell Slots Known"] = 1                  
            if player.bardlvl >= 17:
                player.bardsongrest = "d12" 
                player.notes["Bard Spells Known"] = 20
                player.notes["Bard 9th Level Spell Slots Known"] = 1                    
            if player.bardlvl >= 18:
                player.notes["Bard Spells Known"] = 22
                player.notes["Bard 5th Level Spell Slots Known"] = 3
            if player.bardlvl >= 19:
                player.notes["Bard 6th Level Spell Slots Known"] = 2
            if player.bardlvl == 20:
                player.notes["Bard 7th Level Spell Slots Known"] = 2
            player.bardicinspiration = "d6"
            player.notes["Song of Rest"] = f"You can use soothing music or oration to help revitalize your wounded allies during a short rest. If you or any friendly creatures who can hear your performance regain hit points at the end of the short rest by spending one or more Hit Dice, each of those creatures regains an extra {player.bardsongrest} hit points.\nThe extra hit points increase when you reach certain levels in this class."
            player.notes["Bardic Inspiration"] = f"You can inspire others through stirring words or music. To do so, you use a bonus action on your turn to choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one Bardic Inspiration die, a {player.bardicinspiration}.\nOnce within the next 10 minutes, the creature can roll the die and add the number rolled to one ability check, attack roll, or saving throw it makes. The creature can wait until after it rolls the d20 before deciding to use the Bardic Inspiration die, but must decide before the DM says whether the roll succeeds or fails. Once the Bardic Inspiration die is rolled, it is lost. A creature can have only one Bardic Inspiration die at a time.\nYou can use this feature a number of times equal to your Charisma modifier, or {player.ChaMod} times, a minimum of once. You regain any expended uses when you finish a long rest.\nYour Bardic Inspiration die changes when you reach certain levels in this class."
            player.spellsavedc["Bard Spell Save DC"] = 8 + player.profbonus + player.ChaMod
            player.spellattackmod["Bard Spell Attack Mod"] = player.profbonus + player.ChaMod

        if player.Class[i] == "Cleric":
            player.hitdice["Cleric Hitdie"] = f"{player.clerlvl}d8"
            if player.clerlvl == 1:
                player.hitpoints += (8 + player.ConMod)
            else:
                player.hitpoints += (8 + player.ConMod + hpcalc(player.clerlvl, dice, 8))   
            player.spellsavedc["Cleric Spell Save DC"] = 8 + player.profbonus + player.WisMod
            player.spellattackmod["Cleric Spell Attack Mod"] = player.profbonus + player.WisMod        
            if player.clerlvl >= 2: 
                player.notes["Cleric 1st Level Spell Slots Known"] = 3
                player.clericchanneldivinity = 1
            if player.clerlvl >= 3: 
                player.notes["Cleric 1st Level Spell Slots Known"] = 4
                player.notes["Cleric 2nd Level Spell Slots Known"] = 2
            if player.clerlvl >= 4: 
                player.notes["Cleric Cantrips Known"] = 4
                player.notes["Cleric 2nd Level Spell Slots Known"] = 3
            if player.clerlvl >= 5: 
                player.notes["Cleric 3rd Level Spell Slots Known"] = 2
                player.clericdestroyundeadcr = "CR 1/2 or lower"
            if player.clerlvl >= 6: 
                player.notes["Cleric 3rd Level Spell Slots Known"] = 3
                player.clericchanneldivinity = 2
            if player.clerlvl >= 7: 
                player.notes["Cleric 4th Level Spell Slots Known"] = 1
            if player.clerlvl >= 8: 
                player.notes["Cleric 4th Level Spell Slots Known"] = 2
                player.clericdestroyundeadcr = "CR 1 or lower"
            if player.clerlvl >= 9: 
                player.notes["Cleric 4th Level Spell Slots Known"] = 3
                player.notes["Cleric 5th Level Spell Slots Known"] = 1
            if player.clerlvl >= 10: 
                player.notes["Cleric Cantrips Known"] = 5
                player.notes["Cleric 5th Level Spell Slots Known"] = 2
            if player.clerlvl >= 11: 
                player.notes["Cleric 6th Level Spell Slots Known"] = 1
                player.clericdestroyundeadcr = "CR 2 or lower"
            if player.clerlvl >= 13: 
                player.notes["Cleric 7th Level Spell Slots Known"] = 1
            if player.clerlvl >= 14: 
                player.clericdestroyundeadcr = "CR 3 or lower"
            if player.clerlvl >= 15: 
                player.notes["Cleric 8th Level Spell Slots Known"] = 1
            if player.clerlvl >= 17: 
                player.notes["Cleric 9th Level Spell Slots Known"] = 1
                player.clericdestroyundeadcr = "CR 4 or lower"
            if player.clerlvl >= 18: 
                player.notes["Cleric 5th Level Spell Slots Known"] = 3
                player.clericchanneldivinity = 3
            if player.clerlvl >= 19: 
                player.notes["Cleric 6th Level Spell Slots Known"] = 2
            if player.clerlvl == 20:                        
                player.notes["Cleric 7th Level Spell Slots Known"] = 2
            player.notes["Destroy Undead"] = f"When an undead fails its saving throw against your Turn Undead feature, the creature is instantly destroyed if its challenge rating is {player.clericdestroyundeadcr}."
            player.notes["Channel Divinity"] = f"You gain the ability to channel divine energy directly from your deity, using that energy to fuel magical effects. You start with two such effects: Turn Undead and an effect determined by your domain. Some domains grant you additional effects as you advance in levels, as noted in the domain description.When you use your Channel Divinity, you choose which effect to create. You must then finish a short or long rest to use your Channel Divinity again.\nSome Channel Divinity effects require saving throws. When you use such an effect from this class, the DC equals your cleric spell save DC, or against {player.spellsavedc['Cleric Spell Save DC']}.\nYou can use Channel Divinity {player.clericchanneldivinity} times between rests. When you finish a short or long rest, you regain your expended uses."

        if player.Class[i] == "Druid":
            player.hitdice["Druid Hitdie"] = f"{player.druidlvl}d8"
            if player.druidlvl == 1:
                player.hitpoints += (8 + player.ConMod)
            else:
                player.hitpoints += (8 + player.ConMod + hpcalc(player.druidlvl, dice, 8))  
            player.spellsavedc['Druid Spell Save DC'] = 8 + player.profbonus + player.WisMod
            player.spellattackmod["Druid Spell Attack Mod"] = player.profbonus + player.WisMod 
            
            if player.druidlvl >= 2:
                player.notes["Druid 1st Level Spell Slots Known"] = 3
                player.druidwildshapecr = "CR 1/4 or lower"
                player.druidwildshapelimit = "No flying or swimming speed"
            if player.druidlvl >= 3:
                player.notes["Druid 1st Level Spell Slots Known"] = 4
                player.notes["Druid 2nd Level Spell Slots Known"] = 2
            if player.druidlvl >= 4:
                player.notes["Druid Cantrips Known"] = 3
                player.notes["Druid 2nd Level Spell Slots Known"] = 3
                player.druidwildshapecr = "CR 1/2 or lower"
                player.druidwildshapelimit = "No flying speed"
            if player.druidlvl >= 5:
                player.notes["Druid 3rd Level Spell Slots Known"] = 2
            if player.druidlvl >= 6:
                player.notes["Druid 3rd Level Spell Slots Known"] = 3
            if player.druidlvl >= 7:
                player.notes["Druid 4th Level Spell Slots Known"] = 1
            if player.druidlvl >= 8:
                player.notes["Druid 4th Level Spell Slots Known"] = 2
                player.druidwildshapecr = "CR 1 or lower"
                player.druidwildshapelimit = "No limitations"
            if player.druidlvl >= 9:
                player.notes["Druid 4th Level Spell Slots Known"] = 3
                player.notes["Druid 5th Level Spell Slots Known"] = 1
            if player.druidlvl >= 10:
                player.notes["Druid Cantrips Known"] = 4
                player.notes["Druid 5th Level Spell Slots Known"] = 2
            if player.druidlvl >= 11:
                player.notes["Druid 6th Level Spell Slots Known"] = 1
            if player.druidlvl >= 13:
                player.notes["Druid 7th Level Spell Slots Known"] = 1
            if player.druidlvl >= 15:
                player.notes["Druid 8th Level Spell Slots Known"] = 1
            if player.druidlvl >= 17:
                player.notes["Druid 9th Level Spell Slots Known"] = 1
            if player.druidlvl >= 18:
                player.notes["Druid 5th Level Spell Slots Known"] = 3
            if player.druidlvl >= 19:
                player.notes["Druid 6th Level Spell Slots Known"] = 2
            if player.druidlvl == 20:                                          
                player.notes["Druid 7th Level Spell Slots Known"] = 2
            player.notes["Wild Shape"] = f"You can use your action to magically assume the shape of a beast that you have seen before. You can use this feature twice. You regain expended uses when you finish a short or long rest.\nYour Druid level determines the beasts you can transform into, the Max CR is {player.druidwildshapecr} and the Limitations on it, if any, are {player.druidwildshapelimit}.\nYou can stay in a beast shape for a number of hours equal to half your Druid level (rounded down), or {math.floor(player.druidlvl/2)} hourd. You then revert to your normal form unless you expend another use of this feature. You can revert to your normal form earlier by using a bonus action on your turn. You automatically revert if you fall unconscious, drop to 0 hit points, or die.\nWhile you are transformed, the following rules apply:\nYour game statistics are replaced by the statistics of the beast, but you retain your alignment, personality, and Intelligence, Wisdom, and Charisma scores. You also retain all of your skill and saving throw proficiencies, in addition to gaining those of the creature. If the creature has the same proficiency as you and the bonus in its stat block is higher than yours, use the creature's bonus instead of yours. If the creature has any legendary or lair actions, you can't use them.\n- When you transform, you assume the beast's hit points and Hit Dice. When you revert to your normal form, you return to the number of hit points you had before you transformed. However, if you revert as a result of dropping to 0 hit points, any excess damage carries over to your normal form. For example, if you take 10 damage in animal form and have only 1 hit point left, you revert and take 9 damage. As long as the excess damage doesn't reduce your normal form to 0 hit points, you aren't knocked unconscious.\n- You can't cast spells, and your ability to speak or take any action that requires hands is limited * to the capabilities of your beast form. Transforming doesn't break your concentration on a spell you've already cast, however, or prevent you from taking actions that are part of a spell, such as call lightning, that you've already cast.\n- You retain the benefit of any features from your class, race, or other source and can use them if the new form is physically capable of doing so. However, you can't use any of your special senses, such as darkvision, unless your new form also has that sense.\n- You choose whether your equipment falls to the ground in your space, merges into your new form, or is worn by it. Worn equipment functions as normal, but the DM decides whether it is practical for the new form to wear a piece of equipment, based on the creature's shape and size. Your equipment doesn't change size or shape to match the new form, and any equipment that the new form can't wear must either fall to the ground or merge with it. Equipment that merges with the form has no effect until you leave the form."
            player.notes["Wild Companion"] = f"You gain the ability to summon a spirit that assumes an animal form: as an action, you can expend a use of your Wild Shape feature to cast the Find Familiar spell, without material components.\nWhen you cast the spell in this way, the familiar is a fey instead of a beast, and the familiar disappears after a number of hours equal to half your Druid level, rounded down, or {math.floor(player.druidlvl / 2)} hours. This beast follows the same rules as Wild Shape, in that the Max CR is {player.druidwildshapecr} and if it is limited, it is limited by {player.druidwildshapelimit}."            

        if player.Class[i] == "Fighter":
            player.hitdice["Fighter Hitdie"] = f"{player.figlvl}d10"
            if player.figlvl == 1:
                player.hitpoints += (10 + player.ConMod)
            else:
                player.hitpoints += (10 + player.ConMod + hpcalc(player.figlvl, dice, 10))
            player.notes["Fighting Style"] = f"You adopt a particular style of fighting as your specialty. Choose one of the following options. You can’t take a Fighting Style option more than once, even if you later get to choose again.\n- Archery - You gain a +2 bonus to attack rolls you make with ranged weapons.\n- Blind Fighting - You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you.\n- Defense - While you are wearing armor, you gain a +1 bonus to AC.\n- Dueling - When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.\n- Great Weapon Fighting - When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit.\n- Interception - When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by 1d10 + your Proficiency Bonus, or reduction by 1d10 + {player.profbonus}, to a minimum of 0 damage. You must be wielding a shield or a simple or martial weapon to use this reaction.\n- Protection - When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.\n- Superior Technique - You learn one maneuver of your choice from among those available to the Battle Master archetype. If a maneuver you use requires your target to make a saving throw to resist the maneuver's effects, the saving throw DC equals 8 + your Proficiency Bonus, {8 + player.profbonus}, + your Strength or Dexterity modifier (your choice). You gain one superiority die, which is a d6 (this die is added to any superiority dice you have from another source). This die is used to fuel your maneuvers. A superiority die is expended when you use it. You regain your expended superiority dice when you finish a short or long rest.\n- Thrown Weapon Fighting - You can draw a weapon that has the thrown property as part of the attack you make with the weapon. In addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll.\n- Two-Weapon Fighting - When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.\n- Unarmed Fighting - Your unarmed strikes can deal bludgeoning damage equal to 1d6 + your Strength modifier, or 1d6 + {player.StrMod} bludgeoning damage, on a hit. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8. At the start of each of your turns, you can deal 1d4 bludgeoning damage to one creature grappled by you."
            player.notes["Second Wind"] = f"You have a limited well of stamina that you can draw on to protect yourself from harm. On your turn, you can use a bonus action to regain hit points equal to 1d10 + your Fighter level, or 1d10 + {player.figlvl} hit points. Once you use this feature, you must finish a short or long rest before you can use it again."
            if player.figlvl >= 2:
                player.figactionsurge = "one time"
            if player.figlvl >= 5:
                player.figextraatk = 1
            if player.figlvl >= 9:
                player.figindomitable = "one time"
            if player.figlvl >= 11:
                player.figextraatk = 2
            if player.figlvl >= 13:
                player.figindomitable = "two times"                
            if player.figlvl >= 17:
                player.figactionsurge = "two times"
                player.figindomitable = "three times"
            if player.figlvl == 20:
                player.figextraatk = 3
            player.notes["Action Surge"] = f"You can push yourself beyond your normal limits for a moment. On your turn, you can take an additional action.\nCurrently you can use Action Surge {player.figactionsurge}. Once you use this feature, you must finish a short or long rest before you can use it again."
            player.notes["Extra Attack"] = f"You can attack {player.figextraatk} times, instead of once, whenever you take the Attack action on your turn."
            player.notes["Indomitable"] = f"You can reroll a saving throw that you fail. If you do so, you must use the new roll, and you can't use this feature again until you finish a long rest.\nYou can use this feature {player.figindomitable} between long rests."
            if player.subclass[i] == "Eldrich Knight Archetype Fighter":
                if player.figlvl >= 3:
                    if "EldKngt Fig" not in player.spellcastingclass:
                        player.spellcastingclass.append("EldKngt Fig")
                        player.spellcastingability.append("Int")                    
                    player.spellsavedc["Eldritch Knight Fighter Spell Save DC"] = 8 + player.profbonus + player.IntMod
                    player.spellattackmod["Eldritch Knight Fighter Spell Attack Mod"] = player.profbonus + player.IntMod                    
                    player.notes["Eldritch Knight Fighter Cantrips Known"] = 2
                    player.notes["Eldritch Knight Fighter Spells Known"] = 3
                    player.notes["Eldritch Knight Fighter 1st Level Spell Slots Known"] = 2
                    player.notes["Eldritch Knight Fighter 2nd Level Spell Slots Known"] = 0
                    player.notes["Eldritch Knight Fighter 3rd Level Spell Slots Known"] = 0
                    player.notes["Eldritch Knight Fighter 4th Level Spell Slots Known"] = 0
                if player.figlvl >= 4:
                    player.notes["Eldritch Knight Fighter Spells Known"] = 4
                    player.notes["Eldritch Knight Fighter 1st Level Spell Slots Known"] = 3
                if player.figlvl >= 7:
                    player.notes["Eldritch Knight Fighter Spells Known"] = 5
                    player.notes["Eldritch Knight Fighter 1st Level Spell Slots Known"] = 4
                    player.notes["Eldritch Knight Fighter 2nd Level Spell Slots Known"] = 2
                if player.figlvl >= 8:
                    player.notes["Eldritch Knight Fighter Spells Known"] = 6
                if player.figlvl >= 10:
                    player.notes["Eldritch Knight Fighter Cantrips Known"] = 3
                    player.notes["Eldritch Knight Fighter Spells Known"] = 7
                    player.notes["Eldritch Knight Fighter 2nd Level Spell Slots Known"] = 3
                if player.figlvl >= 11:
                    player.notes["Eldritch Knight Fighter Spells Known"] = 8
                if player.figlvl >= 13:
                    player.notes["Eldritch Knight Fighter Spells Known"] = 9
                    player.notes["Eldritch Knight Fighter 3rd Level Spell Slots Known"] = 2
                if player.figlvl >= 14:
                    player.notes["Eldritch Knight Fighter Spells Known"] = 10
                if player.figlvl >= 16:
                    player.notes["Eldritch Knight Fighter Spells Known"] = 11
                    player.notes["Eldritch Knight Fighter 3rd Level Spell Slots Known"] = 3
                if player.figlvl >= 19:
                    player.notes["Eldritch Knight Fighter Spells Known"] = 12
                    player.notes["Eldritch Knight Fighter 4th Level Spell Slots Known"] = 1
                if player.figlvl == 20:
                    player.notes["Eldritch Knight Fighter Spells Known"] = 13
                
        if player.Class[i] == "Monk":
            player.hitdice["Monk Hitdie"] = f"{player.monklvl}d8"
            if player.monklvl == 1:
                player.hitpoints += (8 + player.ConMod)
            else:
                player.hitpoints += (8 + player.ConMod + hpcalc(player.monklvl, dice, 8)) 
            player.notes["Unarmored Defense"] = f"While you are wearing no armor and not wielding a shield, your AC equals 10 + your Dexterity modifier + your Wisdom modifier, or AC {10 + player.DexMod + player.WisMod}."
            if player.monklvl >= 2:
                player.monkkipoints = player.monklvl
                player.monkunmov = 10
                player.spellsavedc["Monk Spell Save DC"] = 8 + player.profbonus + player.WisMod
            if player.monklvl >= 5:
                player.monkmartialarts = "1d6"
            if player.monklvl >= 6:
                player.monkunmov = 15
            if player.monklvl >= 10:
                player.monkunmov = 20
            if player.monklvl >= 11:
                player.monkmartialarts = "1d8"
            if player.monklvl >= 14:
                player.monkunmov = 25
            if player.monklvl >= 17:
                player.monkmartialarts = "1d10"
            if player.monklvl >= 18:
                player.monkunmov = 30
            player.notes["Unarmored Defense"] = f"While you are wearing no armor and not wielding a shield, your AC equals 10 + your Dexterity modifier + your Wisdom modifier, or AC {10 + player.DexMod + player.WisMod}."
            player.notes["Ki"] = f"Your training allows you to harness the mystic energy of ki. Your access to this energy is represented by a number of ki points, {player.monkkipoints}.\nYou can spend these points to fuel various ki features. You start knowing three such features: Flurry of Blows, Patient Defense, and Step of the Wind. You learn more ki features as you gain levels in this class.\nWhen you spend a ki point, it is unavailable until you finish a short or long rest, at the end of which you draw all of your expended ki back into yourself. You must spend at least 30 minutes of the rest meditating to regain your ki points.\nSome of your ki features require your target to make a saving throw to resist the feature's effects. The saving throw DC is calculated as follows:\nKi save DC = 8 + your Proficiency Bonus + your Wisdom modifier, or DC {8 + player.profbonus + player.WisMod}."
            player.notes["Unarmored Movement(1)"] = f"Your speed increases by {player.monkunmov} feet while you are not wearing armor or wielding a shield."
            player.monkmartialarts = "1d4"
            player.notes["Martial Arts"] = f"Your practice of martial arts gives you mastery of combat styles that use unarmed strikes and monk weapons, which are shortswords and any simple melee weapons that don't have the two-handed or heavy property.\nYou gain the following benefits while you are unarmed or wielding only monk weapons and you aren't wearing armor or wielding a shield:\n- You can use Dexterity instead of Strength for the attack and damage rolls of your unarmed strikes and monk weapons.\n- You can roll a {player.monkmartialarts} in place of the normal damage of your unarmed strike or monk weapon.\n- When you use the Attack action with an unarmed strike or a monk weapon on your turn, you can make one unarmed strike as a bonus action. For example, if you take the Attack action and attack with a quarterstaff, you can also make an unarmed strike as a bonus action, assuming you haven't already taken a bonus action this turn.\nCertain monasteries use specialized forms of the monk weapons. For example, you might use a club that is two lengths of wood connected by a short chain (called a nunchaku) or a sickle with a shorter, straighter blade (called a kama). Whatever name you use for a monk weapon, you can use the game statistics provided for the weapon in the Weapons section."            

        if player.Class[i] == "Paladin":
            player.hitdice["Paladin Hitdie"] = f"{player.pallvl}d10"
            if player.pallvl == 1:
                player.hitpoints += (10 + player.ConMod)
            else:
                player.hitpoints += (10 + player.ConMod + hpcalc(player.pallvl, dice, 10))      
            player.notes["Divine Sense"] = f"The presence of strong evil registers on your senses like a noxious odor, and powerful good rings like heavenly music in your ears. As an action, you can open your awareness to detect such forces. Until the end of your next turn, you know the location of any celestial, fiend, or undead within 60 feet of you that is not behind total cover. You know the type (celestial, fiend, or undead) of any being whose presence you sense, but not its identity (the vampire Count Strahd von Zarovich, for instance). Within the same radius, you also detect the presence of any place or object that has been consecrated or desecrated, as with the hallow spell.\nYou can use this feature a number of times equal to 1 + your Charisma modifier, or {1 + player.ChaMod} times. When you finish a long rest, you regain all expended uses."
            player.notes["Lay on Hands"] = f"Your blessed touch can heal wounds. You have a pool of healing power that replenishes when you take a long rest. With that pool, you can restore a total number of hit points equal to {player.pallvl * 5}.\nAs an action, you can touch a creature and draw power from the pool to restore a number of hit points to that creature, up to the maximum amount remaining in your pool.\nAlternatively, you can expend 5 hit points from your pool of healing to cure the target of one disease or neutralize one poison affecting it. You can cure multiple diseases and neutralize multiple poisons with a single use of Lay on Hands, expending hit points separately for each one.\nThis feature has no effect on undead and constructs."
            if player.pallvl >= 2:
                if "Paladin" not in player.spellcastingclass:
                    player.spellcastingclass.append("Paladin")
                    player.spellcastingability.append("Cha")                
                player.spellsavedc["Paladin Spell Save DC"] = 8 + player.profbonus + player.ChaMod
                player.spellattackmod["Paladin Spell Attack Mod"] = player.profbonus + player.ChaMod                 
                player.notes["Paladin 1st Level Spell Slots Known"] = 2
            if player.pallvl >= 3:
                player.notes["Paladin 1st Level Spell Slots Known"] = 3
            if player.pallvl >= 5:
                player.notes["Paladin 1st Level Spell Slots Known"] = 4
                player.notes["Paladin 2nd Level Spell Slots Known"] = 2
            if player.pallvl >= 7:
                player.notes["Paladin 2nd Level Spell Slots Known"] = 3
            if player.pallvl >= 9:
                player.notes["Paladin 3rd Level Spell Slots Known"] = 2
            if player.pallvl >= 11:
                player.notes["Paladin 3rd Level Spell Slots Known"] = 3
            if player.pallvl >= 13:
                player.notes["Paladin 4th Level Spell Slots Known"] = 1
            if player.pallvl >= 15:
                player.notes["Paladin 4th Level Spell Slots Known"] = 2
            if player.pallvl >= 17:
                player.notes["Paladin 4th Level Spell Slots Known"] = 3
                player.notes["Paladin 5th Level Spell Slots Known"] = 1
            if player.pallvl >= 19:
                player.notes["Paladin 5th Level Spell Slots Known"] = 2

        if player.Class[i] == "Ranger":
            player.hitdice["Ranger Hitdie"] = f"{player.ranlvl}d10"
            if player.ranlvl == 1:
                player.hitpoints += (10 + player.ConMod)
            else:
                player.hitpoints += (10 + player.ConMod + hpcalc(player.ranlvl, dice, 10))   
            if player.ranlvl >= 2:
                if "Ranger" not in player.spellcastingclass:
                    player.spellcastingclass.append("Ranger")
                    player.spellcastingability.append("Wis")                
                player.spellsavedc["Ranger Spell Save DC"] = 8 + player.profbonus + player.WisMod
                player.spellattackmod["Ranger Spell Attack Mod"] = player.profbonus + player.WisMod 
                player.notes["Ranger Spells Known"] = 2
                player.notes["Ranger 1st Level Spell Slots Known"] = 2
            if player.ranlvl >= 3:
                player.notes["Ranger Spells Known"] = 3
                player.notes["Ranger 1st Level Spell Slots Known"] = 3
            if player.ranlvl >= 5:
                player.notes["Ranger Spells Known"] = 4
                player.notes["Ranger 1st Level Spell Slots Known"] = 4
                player.notes["Ranger 2nd Level Spell Slots Known"] = 2
            if player.ranlvl >= 7:
                player.notes["Ranger Spells Known"] = 5
                player.notes["Ranger 2nd Level Spell Slots Known"] = 3
            if player.ranlvl >= 9:
                player.notes["Ranger Spells Known"] = 6
                player.notes["Ranger 3rd Level Spell Slots Known"] = 2
            if player.ranlvl >= 11:
                player.notes["Ranger Spells Known"] = 7
                player.notes["Ranger 3rd Level Spell Slots Known"] = 3
            if player.ranlvl >= 13:
                player.notes["Ranger Spells Known"] = 8
                player.notes["Ranger 4th Level Spell Slots Known"] = 1
            if player.ranlvl >= 15:
                player.notes["Ranger Spells Known"] = 9
                player.notes["Ranger 4th Level Spell Slots Known"] = 2
            if player.ranlvl >= 17:
                player.notes["Ranger Spells Known"] = 10
                player.notes["Ranger 4th Level Spell Slots Known"] = 3
                player.notes["Ranger 5th Level Spell Slots Known"] = 1
            if player.ranlvl >= 19:
                player.notes["Ranger Spells Known"] = 11
                player.notes["Ranger 5th Level Spell Slots Known"] = 2

        if player.Class[i] == "Rogue":
            player.hitdice["Rogue Hitdie"] = f"{player.roglvl}d8"
            if player.roglvl == 1:
                player.hitpoints += (8 + player.ConMod)
            else:
                player.hitpoints += (8 + player.ConMod + hpcalc(player.roglvl, dice, 8))     
            player.rogsnkatk = "1d6"
            if player.roglvl >= 3:
                player.rogsnkatk = "2d6"
            if player.roglvl >= 5:
                player.rogsnkatk = "3d6"
            if player.roglvl >= 7:
                player.rogsnkatk = "4d6"
            if player.roglvl >= 9:
                player.rogsnkatk = "5d6"
            if player.roglvl >= 11:
                player.rogsnkatk = "6d6"
            if player.roglvl >= 13:
                player.rogsnkatk = "7d6"
            if player.roglvl >= 15:
                player.rogsnkatk = "8d6"
            if player.roglvl >= 17:
                player.rogsnkatk = "9d6"
            if player.roglvl >= 19:
                player.rogsnkatk = "10d6"
            player.notes["Sneak Attack"] = f"You know how to strike subtly and exploit a foe's distraction. Once per turn, you can deal an extra {player.rogsnkatk} damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon.\nYou don't need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and you don't have disadvantage on the attack roll.\nThe amount of the extra damage increases as you gain levels in this class."
            if player.subclass[i] == "Arcane Trickster Archetype Rogue":
                if player.roglvl >= 3:
                    if "Arcane Trickster Rogue" not in player.spellcastingclass:
                        player.spellcastingclass.append("Arcane Trickster Rogue")
                        player.spellcastingability.append("Int")                    
                    player.spellsavedc["Arcane Trickster Rogue Spell Save DC"] = 8 + player.profbonus + player.IntMod
                    player.spellattackmod["Arcane Trickster Rogue Spell Attack Mod"] = player.profbonus + player.IntMod                    
                    player.notes["Arcane Trickster Rogue Cantrips"] = 2
                    player.notes["Arcane Trickster Rogue Spells Known"] = 3
                    player.notes["Arcane Trickster Rogue 1st Level Spell Slots"] = 2
                if player.roglvl >= 4:
                    player.notes["Arcane Trickster Rogue Spells Known"] = 4
                    player.notes["Arcane Trickster Rogue 1st Level Spell Slots"] = 3
                if player.roglvl >= 7:
                    player.notes["Arcane Trickster Rogue Spells Known"] = 5
                    player.notes["Arcane Trickster Rogue 1st Level Spell Slots"] = 4
                    player.notes["Arcane Trickster Rogue 2nd Level Spell Slots"] = 2
                if player.roglvl >= 8:
                    player.notes["Arcane Trickster Rogue Spells Known"] = 6
                if player.roglvl >= 10:
                    player.notes["Arcane Trickster Rogue Cantrips"] = 3
                    player.notes["Arcane Trickster Rogue Spells Known"] = 7
                    player.notes["Arcane Trickster Rogue 2nd Level Spell Slots"] = 3
                if player.roglvl >= 11:
                    player.notes["Arcane Trickster Rogue Spells Known"] = 8
                if player.roglvl >= 13:
                    player.notes["Arcane Trickster Rogue Spells Known"] = 9
                    player.notes["Arcane Trickster Rogue 3rd Level Spell Slots"] = 2
                if player.roglvl >= 14:
                    player.notes["Arcane Trickster Rogue Spells Known"] = 10
                if player.roglvl >= 16:
                    player.notes["Arcane Trickster Rogue Spells Known"] = 11
                    player.notes["Arcane Trickster Rogue 3rd Level Spell Slots"] = 3
                if player.roglvl >= 19:
                    player.notes["Arcane Trickster Rogue Spells Known"] = 12
                    player.notes["Arcane Trickster Rogue 4th Level Spell Slots"] = 1
                if player.roglvl == 20:
                    player.notes["Arcane Trickster Rogue Spells Known"] = 13                

        if player.Class[i] == "Sorcerer":
            player.hitdice["Sorcerer Hitdie"] = f"{player.sorclvl}d6"
            if player.sorclvl == 1:
                player.hitpoints += (6 + player.ConMod)
            else:
                player.hitpoints += (6 + player.ConMod + hpcalc(player.sorclvl, dice, 6))   
            player.spellsavedc["Sorcerer Spell Save DC"] = 8 + player.profbonus + player.ChaMod
            player.spellattackmod["Sorcerer Spell Attack Mod"] = player.profbonus + player.ChaMod                             
            if player.sorclvl >= 2:
                player.notes["Sorcerer Spells Known"] = 3
                player.notes["Sorcerer 1st Level Spell Slots Known"] = 3
                player.sorcsorcerypoints = player.sorclvl
            if player.sorclvl >= 3:
                player.notes["Sorcerer Spells Known"] = 4
                player.notes["Sorcerer 1st Level Spell Slots Known"] = 4
                player.notes["Sorcerer 2nd Level Spell Slots Known"] = 2
            if player.sorclvl >= 4:
                player.notes["Sorcerer Cantrips Known"] = 5
                player.notes["Sorcerer Spells Known"] = 5
                player.notes["Sorcerer 2nd Level Spell Slots Known"] = 3
            if player.sorclvl >= 5:
                player.notes["Sorcerer Spells Known"] = 6
                player.notes["Sorcerer 3rd Level Spell Slots Known"] = 2
            if player.sorclvl >= 6:
                player.notes["Sorcerer Spells Known"] = 7
                player.notes["Sorcerer 3rd Level Spell Slots Known"] = 3
            if player.sorclvl >= 7:
                player.notes["Sorcerer Spells Known"] = 8
                player.notes["Sorcerer 4th Level Spell Slots Known"] = 1
            if player.sorclvl >= 8:
                player.notes["Sorcerer Spells Known"] = 9
                player.notes["Sorcerer 4th Level Spell Slots Known"] = 2
            if player.sorclvl >= 9:
                player.notes["Sorcerer Spells Known"] = 10
                player.notes["Sorcerer 4th Level Spell Slots Known"] = 3
                player.notes["Sorcerer 5th Level Spell Slots Known"] = 1
            if player.sorclvl >= 10:
                player.notes["Sorcerer Cantrips Known"] = 6
                player.notes["Sorcerer Spells Known"] = 11
                player.notes["Sorcerer 5th Level Spell Slots Known"] = 2
            if player.sorclvl >= 11:
                player.notes["Sorcerer Spells Known"] = 12
                player.notes["Sorcerer 6th Level Spell Slots Known"] = 1
            if player.sorclvl >= 13:
                player.notes["Sorcerer Spells Known"] = 13
                player.notes["Sorcerer 7th Level Spell Slots Known"] = 1
            if player.sorclvl >= 15:
                player.notes["Sorcerer Spells Known"] = 14
                player.notes["Sorcerer 8th Level Spell Slots Known"] = 1
            if player.sorclvl >= 17:
                player.notes["Sorcerer Spells Known"] = 15
                player.notes["Sorcerer 9th Level Spell Slots Known"] = 1
            if player.sorclvl >= 18:
                player.notes["Sorcerer 5th Level Spell Slots Known"] = 3
            if player.sorclvl >= 19:
                player.notes["Sorcerer 6th Level Spell Slots Known"] = 2
            if player.sorclvl == 20:
                player.notes["Sorcerer 7th Level Spell Slots Known"] = 2
            player.notes["Sorcery Points"] = f"You have a number of sorcery points, determined by your level, or {player.sorcsorcerypoints} points. You can never have more sorcery points than your level. You regain all spent sorcery points when you finish a long rest.\nFlexible Casting - You can use your sorcery points to gain additional spell slots, or sacrifice spell slots to gain additional sorcery points. You learn other ways to use your sorcery points as you reach higher levels.\nCreating Spell Slots - You can transform unexpended sorcery points into one spell slot as a bonus action on your turn. The Creating Spell Slots table shows the cost of creating a spell slot of a given level. You can create spell slots no higher in level than 5th. Any spell slot you create with this feature vanishes when you finish a long rest.\n1st Spell Slot costs 2 Sorcery Points\n2nd Spell Slot costs 3 Sorcery Points\n3rd Spell Slot costs 5 Sorcery Points\n4th Spell Slot costs 6 Sorcery Points\n5th Spell Slot costs 7 Sorcery Points\nConverting a Spell Slot to Sorcery Points. As a bonus action on your turn, you can expend one spell slot and gain a number of sorcery points equal to the slot's level."

        if player.Class[i] == "Warlock":   
            player.hitdice["Warlock Hitdie"] = f"{player.warlvl}d8"
            if player.warlvl == 1:
                player.hitpoints += (8 + player.ConMod)
            else:
                player.hitpoints += (8 + player.ConMod + hpcalc(player.warlvl, dice, 8))       
            player.spellsavedc["Warlock Spell Save DC"] = 8 + player.profbonus + player.ChaMod
            player.spellattackmod["Warlock Spell Attack Mod"] = player.profbonus + player.ChaMod       
            if player.warlvl >= 2:
                player.notes["Warlock Spells Known"] = 3
                player.wareldinv = 2
            if player.warlvl >= 3:
                player.notes["Warlock Spells Known"] = 4
                player.notes["Warlock Spell Slot Level"] = "2nd"
            if player.warlvl >= 4:
                player.notes["Warlock Cantrips Known"] = 3
                player.notes["Warlock Spells Known"] = 5
            if player.warlvl >= 5:
                player.notes["Warlock Spells Known"] = 6
                player.notes["Warlock Spell Slot Level"] = "3rd"
                player.wareldinv = 3
            if player.warlvl >= 6:
                player.notes["Warlock Spells Known"] = 7
            if player.warlvl >= 7:
                player.notes["Warlock Spells Known"] = 8
                player.notes["Warlock Spell Slot Level"] = "4th"
                player.wareldinv = 4
            if player.warlvl >= 8:
                player.notes["Warlock Spells Known"] = 9
            if player.warlvl >= 9:
                player.notes["Warlock Spells Known"] = 10
                player.notes["Warlock Spell Slot Level"] = "5th"
                player.wareldinv = 5
            if player.warlvl >= 10:
                player.notes["Warlock Cantrips Known"] = 4
            if player.warlvl >= 11:
                player.notes["Warlock Spells Known"] = 11
                player.warmysticarcanum = "One 6th Level Spell Slot"
            if player.warlvl >= 12:
                player.wareldinv = 6
            if player.warlvl >= 13:
                player.notes["Warlock Spells Known"] = 12
                player.warmysticarcanum == "One 6th Level Spell Slot, One 7th Level Spell Slot"
            if player.warlvl >= 15:
                player.notes["Warlock Spells Known"] = 13
                player.wareldinv = 7
                player.warmysticarcanum == "One 6th Level Spell Slot, One 7th Level Spell Slot, One 8th Level Spell Slot"
            if player.warlvl >= 17:
                player.notes["Warlock Spells Known"] = 14
                player.warmysticarcanum == "One 6th Level Spell Slot, One 7th Level Spell Slot, One 8th Level Spell Slot, One 9th Level Spell Slot"
            if player.warlvl >= 18:
                player.wareldinv = 8
            if player.warlvl >= 19:
                player.notes["Warlock Spells Known"] = 15
            player.notes["Warlock Mystic Arcanum"] = f"Your patron bestows upon you a magical secret called an arcanum. The spells acquired by this are: {player.warmysticarcanum}, from the warlock spell list as this arcanum.\nYou can cast your arcanum spell once without expending a spell slot. You must finish a long rest before you can do so again.\nMore spells are unlocked at higher levels. You regain all uses of your Mystic Arcanum when you finish a long rest."
            player.notes["Warlock Eldritch Invocations"] = f"In your study of occult lore, you have unearthed eldritch invocations, fragments of forbidden knowledge that imbue you with an abiding magical ability. A level prerequisite refers to your level in this class.\nYou have {player.wareldinv} available to you, of your choice.\nAdditionally, when you gain a level in this class, you can choose one of the invocations you know and replace it with another invocation that you could learn at that level.\nIf an eldritch invocation has prerequisites, you must meet them to learn it. You can learn the invocation at the same time that you meet its prerequisites. A level prerequisite refers to your level in this class."

        if player.Class[i] == "Wizard":
            player.hitdice["Wizard Hitdie"] = f"{player.wizlvl}d6"
            if player.wizlvl == 1:
                player.hitpoints += (6 + player.ConMod)
            else:
                player.hitpoints += (6 + player.ConMod + hpcalc(player.wizlvl, dice, 6))    
            player.spellsavedc["Wizard Spell Save DC"] = 8 + player.profbonus + player.ChaMod
            player.spellattackmod["Wizard Spell Attack Mod"] = player.profbonus + player.ChaMod                    
            player.notes["Arcane Recovery"] = f"You have learned to regain some of your magical energy by studying your spellbook. Once per day when you finish a short rest, you can choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your Wizard level (rounded up), or {math.ceil(player.wizlvl/2)}, and none of the slots can be 6th level or higher."
            if player.wizlvl >= 2:
                player.notes["Wizard 1st Level Spell Slots Known"] = 3
            if player.wizlvl >= 3:
                player.notes["Wizard 1st Level Spell Slots Known"] = 4
                player.notes["Wizard 2nd Level Spell Slots Known"] = 2
            if player.wizlvl >= 4:
                player.notes["Wizard Cantrips Known"] = 4
                player.notes["Wizard 2nd Level Spell Slots Known"] = 3
            if player.wizlvl >= 5:
                player.notes["Wizard 3rd Level Spell Slots Known"] = 2
            if player.wizlvl >= 6:
                player.notes["Wizard 3rd Level Spell Slots Known"] = 3
            if player.wizlvl >= 7:
                player.notes["Wizard 4th Level Spell Slots Known"] = 1
            if player.wizlvl >= 8:
                player.notes["Wizard 4th Level Spell Slots Known"] = 2
            if player.wizlvl >= 9:
                player.notes["Wizard 4th Level Spell Slots Known"] = 3
                player.notes["Wizard 5th Level Spell Slots Known"] = 1
            if player.wizlvl >= 10:
                player.notes["Wizard Cantrips Known"] = 5
                player.notes["Wizard 5th Level Spell Slots Known"] = 2
            if player.wizlvl >= 11:
                player.notes["Wizard 6th Level Spell Slots Known"] = 1
            if player.wizlvl >= 13:
                player.notes["Wizard 7th Level Spell Slots Known"] = 1
            if player.wizlvl >= 15:
                player.notes["Wizard 8th Level Spell Slots Known"] = 1
            if player.wizlvl >= 17:
                player.notes["Wizard 9th Level Spell Slots Known"] = 1  
            if player.wizlvl >= 18:
                player.notes["Wizard 5th Level Spell Slots Known"] = 3
            if player.wizlvl >= 19:
                player.notes["Wizard 6th Level Spell Slots Known"] = 2
            if player.wizlvl == 20:
                player.notes["Wizard 7th Level Spell Slots Known"] = 1

    #Add in smth here, does the player want to multiclass?
    #Occurs at every level
    #All subclasses and blanks if the player is below the requisite level, no blanks if they meet the level
    #Should just start with "do you wish to multiclass" ... 

    #When the player levels up, they choose first if they want to multiclass, then choose that first before hp is assigned

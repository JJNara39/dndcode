import random
import math
from dnd_languagesskills import *
import dnd_tools


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

def dndchargen_class(param, player):
###This section is for picking a class    
    Classes = {
        "Artificer": [
            "Alchemist Specialist Artificer",
            "Armorer Specialist Artificer",
            "Artilierist Specialist Artificer",
            "Battle Smith Specialist Artificer",
            ""
        ],
        "Barbarian": [
            "Path of the Ancestral Guardian Barbarian",
            "Path of the Battlerager Barbarian",
            "Path of the Beast Barbarian",
            "Path of the Berserker Barbarian",
            "Path of the Giant Barbarian",
            "Path of the Juggernaut Barbarian",
            "Path of the Storm Herald Barbarian",
            "Path of the Totem Warrior Barbarian",
            "Path of the Zealot Barbarian",
            "Path of the Wild Magic Barbarian",
            ""
        ],
        "Bard": [
            "College of Creation Bard",
            "College of Eloquence Bard",
            "College of Glamour Bard",
            "College of Lore Bard",
            "College of the Road Bard",
            "College of Spirits Bard",
            "College of Swords Bard",
            "College of Tragedy Bard",
            "College of Valor Bard",
            "College of Whispers Bard",
            ""
        ],
        "Cleric": [
            "Arcana Domain Cleric",
            "Blood Domain Cleric",
            "Community Domain Cleric",
            "Death Domain Cleric",
            "Forge Domain Cleric",
            "Grave Domain Cleric",
            "Knowledge Domain Cleric",
            "Life Domain Cleric",
            "Light Domain Cleric",
            "Moon Domain Cleric",
            "Nature Domain Cleric",
            "Night Domain Cleric",
            "Order Domain Cleric",
            "Peace Domain Cleric",
            "Tempest Domain Cleric",
            "Trickery Domain Cleric",
            "Twilight Domain Cleric",
            "War Domain Cleric"
        ],
        "Druid": [
            "Circle of the Blighted Druid",
            "Circle of Dreams Druid",
            "Circle of the Land Druid",
            "Circle of the Moon Druid",
            "Circle of the Sheppard Druid",
            "Circle of Spores Druid",
            "Circle of the Stars Druid",
            "Circle of Wildfire Druid",
            ""
        ],
        "Fighter": [
            "Arcane Archer Archetype Fighter",
            "Battle Master Archetype Fighter",
            "Cavalier Archetype Fighter",
            "Champion Archetype Fighter",
            "Echo Knight Archetype Fighter",
            "Eldritch Knight Archetype Fighter",
            "Psi Warrior Archetype Fighter",
            "Purple Dragon Knight Archetype Fighter",
            "Rune Knight Archetype Fighter",
            "Samurai Archetype Fighter",
            "Scofflaw Archetype Fighter",
            ""
        ],
        "Monk": [
            "Way of the Ascendant Dragon Monk",
            "Way of the Astral Self Monk",
            "Way of the Cobalt Soul Monk",
            "Way of the Drunken Master Monk",
            "Way of the Four Elements Monk",
            "Way of the Kensei Monk",
            "Way of the Long Death Monk",
            "Way of Mercy Monk",
            "Way of the Open Hand Monk",
            "Way of the Shadow Monk",
            "Way of the Sun Soul Monk",
            ""
        ],
        "Paladin": [
            "Oath of the Ancients Paladin",
            "Oath of Conquest Paladin",
            "Oath of the Crown Paladin",
            "Oath of Devotion Paladin",
            "Oath of Glory Paladin",
            "Oath of the Open Sea Paladin",
            "Oath of Redemption Paladin",
            "Oath of the Watchers Paladin",
            "Oath of Vengeance Paladin",
            "Oathbreaker Paladin",
            ""
        ],
        "Ranger": [
            "Beast Master Archetype Ranger",
            "Drakewarden Ranger",
            "Fey Wanderer Archetype Ranger",
            "Gloom Stalker Archetype Ranger",
            "Horizon Walker Archetype Ranger",
            "Hunter Archetype Ranger",
            "Monster Slayer Archetype Ranger",
            "Swarmkeeper Archetype Ranger",
            ""
        ],
        "Rogue": [
            "Arcane Trickster Archetype Rogue",
            "Assassin Archetype Rogue",
            "Inquisitive Archetype Rogue",
            "Mastermind Archetype Rogue",
            "Phantom Archetype Rogue",
            "Scout Archetype Rogue",
            "Soulknife Archetype Rogue",
            "Swashbuckler Archetype Rogue",
            "Thief Archetype Rogue",
            ""
        ],
        "Sorcerer": [
            "Aberrant Mind Origin Sorcerer",
            "Clockwork Soul Origin Sorcerer",
            "Divine Soul Origin Sorcerer",
            "Draconic Bloodline Origin Sorcerer",
            "Lunar Magic Origin Sorcerer",
            "Runechild Origin Sorcerer",
            "Shadow Origin Sorcerer",
            "Storm Origin Sorcerer",
            "Wild Magic Origin Sorcerer"
        ],
        "Warlock": [
            "Archfey Patron Warlock",
            "Beachball Patron Warlock",
            "Celestial Patron Warlock",
            "The Fathomless Patron Warlock",
            "Fiend Patron Warlock",
            "The Genie Patron Warlock",
            "Great Old One Patron Warlock",
            "Hexblade Patron Warlock",
            "Undead Patron Warlock",
            "Undying Patron Warlock"
        ],
        "Wizard": [
            "Abjuration Arcane Tradition Wizard",
            "Bladesinging Arcane Tradition Wizard",
            "Blood Magic Arcane Tradition Wizard",
            "Chronurgy Magic Wizard",
            "Conjuration Arcane Tradition Wizard",
            "Divination Arcane Tradition Wizard",
            "Enchantment Arcane Tradition Wizard",
            "Evocation Arcane Tradition Wizard",
            "Graviturgy Magic Wizard",
            "Illusion Arcane Tradition Wizard",
            "Necromancy Arcane Tradition Wizard",
            "Order of Scribes Arcane Tradition Wizard",
            "Transmutation Arcane Tradition Wizard",
            "War Magic Arcane Tradition Wizard",
            ""
        ],
    }
    class_list = list(Classes.keys())
    if param == "Y":
        if player.level > 1:
            while True:
                smclass = input("Do you wish to multi-class? Y/N ").strip().lower()
                if smclass in {"y", "ye", "yes"}:
                    player.singlemulticlass = "Y"
                    break
                elif smclass in {"n", "no"}:
                    player.singlemulticlass = "N"
                    break
                else:
                    print("Invalid choice, please select Y/N")  
            if player.singlemulticlass == "N":
                player.classnum = 1
            if player.singlemulticlass == "Y":
                while True:
                    try:
                        classnum = int(input(f"Given your player level of {player.level}, how many classes are you multiclassing into? "))
                        if classnum == 0:
                            print("You cannot have 0 classes, please try again.")
                        elif (classnum >= 1) and (classnum <= player.level):
                            player.classnum = classnum
                            break
                        elif classnum > player.level:
                            print(f"You cannot have more classes than your level of {player.level}, please reselect")
                    except ValueError: #Handles non-numeric choices  
                        print("Invalid input. Please enter a number.")    
            if player.singlemulticlass == "N":
                player.classnum = 1
        if player.level == 1:
            player.classnum = 1
        for cn in range(player.classnum):
            print("0 - Random")
            for idx, cl in enumerate(class_list, 1):
                print(f"{idx} - {cl}")
            while True:
                try:
                    cla = int(input("Class? "))
                    if cla == 0:
                        RandomClass = random.choice(class_list)
                        RandomSubclass = random.choice(Classes[RandomClass])
                        player.Class.append(RandomClass)
                        class_list.remove(RandomClass)
                        player.subclass.append(RandomSubclass)
                        break
                    elif 1 <= cla <= len(class_list):
                        chosen_class = class_list[cla - 1]  # Get the class name
                        player.Class.append(chosen_class)
                        class_list.remove(chosen_class)
                        # Generate the subclass list for the chosen class
                        subclass_list = Classes.get(chosen_class, [])

                        while True:
                            try:
                                print("0 - Random")
                                for idx, sbcl in enumerate(subclass_list, 1):
                                    print(f"{idx} - {sbcl}")
                                subc = int(input("Which subclass would you like? ")) 
                                if subc == 0:
                                    RandomSubclass = random.choice(subclass_list)
                                    if RandomSubclass == "Beachball Patron Warlock":
                                        Classes["Warlock"].remove("Beachball Patron Warlock")
                                        WarRand = random.choice(Classes["Warlock"])
                                        player.subclass.append(WarRand)
                                        player.beachballflag = True
                                    else:
                                        player.subclass.append(RandomSubclass)
                                    break                       
                                elif 1 <= subc <= len(subclass_list):
                                    subcl = subclass_list[subc - 1]
                                    if subcl == "Beachball Patron Warlock":
                                        Classes["Warlock"].remove("Beachball Patron Warlock")
                                        WarRand = random.choice(Classes["Warlock"])
                                        player.subclass.append(WarRand)
                                        player.beachballflag = True
                                    else:
                                        player.subclass.append(subcl)  
                                    break 
                                else:
                                    print("Invalid choice, please choose a valid option.")            
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")       
                        break             
                    else:
                        print("Invalid choice, please choose a valid option.") 
                               
                except ValueError: #Handles non-numeric choices  
                    print("Invalid input. Please enter a number.")       

    if param == "N":
        RandomClass = random.choice(class_list)
        if RandomClass == "Warlock":
            WarRand = random.choice(Classes["Warlock"])
            if WarRand == "Beachball Patron Warlock":
                Classes["Warlock"].remove("Beachball Patron Warlock")
                WarRand = random.choice(Classes["Warlock"])
                player.subclass.append(WarRand)
                player.beachballflag = True
            else:
                player.Class.append(RandomClass)
                player.subclass.append(WarRand)
        else:
            player.Class.append(RandomClass)
            RandomSubclass = random.choice(Classes[RandomClass])
            player.subclass.append(RandomSubclass)

### This section is for assigning 1-time aspects of the class like equipment
    poollevel = player.level
    
    MartialWeapons = list(dnd_tools.martial_weapons.keys())
    MartialWeaponsNames = [wep["Name"] for wep in dnd_tools.martial_weapons.values()]
    mw_keys_to_remove = ["Blowgun", "HandCrossbow", "HeavyCrossbow", "Longbow", "Net"]
    MartialMeleeWeapons = [key for key in MartialWeapons if key not in mw_keys_to_remove]
    MartialMeleeWeaponsNames = [key["Name"] for key in dnd_tools.martial_weapons.values() if key not in mw_keys_to_remove]
    SimpleWeapons = list(dnd_tools.simple_weapons.keys())
    SimpleWeaponsNames = [wep["Name"] for wep in dnd_tools.simple_weapons.values()]
    sw_keys_to_remove = ["LightCrossbow", "Dart", "Shortbow", "Sling"]
    SimpleMeleeWeapons = [key for key in SimpleWeapons if key not in sw_keys_to_remove]
    SimpleMeleeWeaponsNames = [key["Name"] for key in dnd_tools.simple_weapons.values() if key not in sw_keys_to_remove]
    MusicalInstr = list(dnd_tools.musical_instr.keys())
    MusicalInstrNames = [mi["Name"] for mi in dnd_tools.musical_instr.values()]
    mi_key_to_remove = ["Lute"]
    MusicalInstrWOLute = [key for key in MusicalInstr if key not in mi_key_to_remove]
    MusicalInstrWOLuteNames = [key["Name"] for key in dnd_tools.musical_instr.values() if key not in mi_key_to_remove]
    AllWeapons = MartialWeapons + SimpleWeapons
    ohw_keys = ["Club", "Dagger", "Handaxe", "Javelin", "LightHammer", "Mace", "Quarterstaff", "Sickle", "Spear", 
                        "Battleaxe", "Flail", "Lance", "Longsword", "Morningstar", "Rapier", "Scimitar", "Shortsword", 
                        "Trident", "WarPick", "Warhammer", "Whip"
                    ]
    OneHandedWeapons = [key for key in AllWeapons if key in ohw_keys]
    OneHandedWeaponsNames = [
        dnd_tools.simple_weapons[key]["Name"] if key in dnd_tools.simple_weapons 
        else dnd_tools.martial_weapons[key]["Name"] 
        for key in OneHandedWeapons
    ]

    for i in range(len(player.Class)):

        #Artificer
        if player.Class[i] == "Artificer":
            if param == "N":
                player.artlvl = player.level
                player.classlvl.append(player.artlvl)            
            if param == "Y":
                if player.singlemulticlass == "Y":
                    while True:
                        try:
                            artlvl = int(input(f"Given your pool of levels of {poollevel}, What is your Artificer level? "))
                            if artlvl <= 0:
                                print("Your Artificer level must be at least 1, please try again.")
                            elif artlvl <= poollevel:
                                break
                            else:
                                print("You are only able to invest within your pool.")
                        except ValueError: #Handles non-numeric choices  
                            print("Invalid input. Please enter a number.")                                
                    poollevel = poollevel - player.artlvl
                    player.classlvl.append(artlvl)
                    player.artlvl = artlvl
                if player.singlemulticlass == "N":
                    player.artlvl = player.level
                    player.classlvl.append(player.artlvl)    
            if player.artlvl >= 1:
                if i == 0:
                    profs = ["Light Armor", "Medium Armor", "Shield", "Simple Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    player.proficiencies.append(dnd_tools.kits["ThievKit"]["Name"])
                    player.proficiencies.append(dnd_tools.artisan_tools["TinkTools"]["Name"])                                                
                    player.proficiencies = artisantools(param, player.proficiencies)
                    player.skills.append(dnd_tools.saving_throws["ConST"])
                    player.skills.append(dnd_tools.saving_throws["IntST"])
                    ArtSkillsList = [
                        dnd_tools.skills["Arcana"], 
                        dnd_tools.skills["History"], 
                        dnd_tools.skills["Investigation"], 
                        dnd_tools.skills["Medicine"], 
                        dnd_tools.skills["Nature"], 
                        dnd_tools.skills["Perception"], 
                        dnd_tools.skills["SleightofHand"]
                        ]
                    player.skills = twoskillsfromlist(param, player.skills, ArtSkillsList)
                    ArtChoices = ["Starting Equipment", "Gold"]
                    ArtChoices2 = ["Studded Leather Armor", "Scale Mail"]
                    if param == "Y":
                        while True:
                            try:
                                print("0 - Random")
                                for idx, artch in enumerate(ArtChoices,1):
                                    print(f"{idx} - {artch}")
                                sego = int(input("Would you like the starting equipment or gold(5d4 x 10gp, must forgo starting equipment from background, Artificer Only)? "))
                                if sego == 0:
                                    RandArtChoice = random.choice(ArtChoices)
                                    if RandArtChoice == "Starting Equipment":    
                                        player.equipment = twosimpleweapons(param, player.equipment)
                                        player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                                        player.equipment.append("20 Bolts")
                                        RandArtChoice2 = random.choice(ArtChoices2)
                                        if RandArtChoice2 == "Studded Leather Armor":
                                            player.equipment.append(dnd_tools.light_armor["StuddedLeather"].copy())
                                        if RandArtChoice2 == "Scale Mail":
                                            player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                                        player.equipment.append(dnd_tools.kits["ThievKit"].copy())
                                        player.equipment.append(dnd_tools.packs["DungeoneersPack"].copy())
                                    elif RandArtChoice == "Gold":
                                        player.gold = player.gold + dice(4) + dice(4) + dice(4) + dice(4) + dice(4)  
                                    break                              
                                elif sego == 1:
                                    player.equipment = twosimpleweapons(param, player.equipment)
                                    player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                                    player.equipment.append("20 Bolts")

                                    while True:
                                        try:                            
                                            print("0 - Random")
                                            for idx, artch2 in enumerate(ArtChoices2,1):
                                                print(f"{idx} - {artch2}")                            
                                            artchoice3 = int(input("Which armor would you like to add to your equipment? "))
                                            if artchoice3 == 0:
                                                RandArtChoice2 = random.choice(ArtChoices2)
                                                if RandArtChoice2 == "Studded Leather Armor":
                                                    player.equipment.append(dnd_tools.light_armor["StuddedLeather"].copy())
                                                if RandArtChoice2 == "Scale Mail":
                                                    player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())                                            
                                            elif artchoice3 == 1:
                                                player.equipment.append(dnd_tools.light_armor["StuddedLeather"].copy())
                                                break
                                            elif artchoice3 == 2:
                                                player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                                                break
                                            else:
                                                print("Invalid choice, please choose a valid option.")                                            
                                            player.equipment.append(dnd_tools.kits["ThievKit"].copy())
                                            player.equipment.append(dnd_tools.packs["DungeoneersPack"].copy())
                                        except ValueError: #Handles non-numeric choices  
                                            print("Invalid input. Please enter a number.")      
                                    break                                         

                                elif sego == 2:
                                    player.gold = player.gold + dice(4) + dice(4) + dice(4) + dice(4) + dice(4)
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")                                     
                    if param == "N":
                        RandArtChoice = random.choice(ArtChoices)
                        if RandArtChoice == "Starting Equipment":    
                            player.equipment = twosimpleweapons(param, player.equipment)
                            player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                            player.equipment.append("20 Bolts")
                            RandArtChoice2 = random.choice(ArtChoices2)
                            if RandArtChoice2 == "Studded Leather Armor":
                                player.equipment.append(dnd_tools.light_armor["StuddedLeather"].copy())
                            if RandArtChoice2 == "Scale Mail":
                                player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                            player.equipment.append(dnd_tools.kits["ThievKit"].copy())
                            player.equipment.append(dnd_tools.packs["DungeoneersPack"].copy())
                        if RandArtChoice == "Gold":
                            player.gold = player.gold + dice(4) + dice(4) + dice(4) + dice(4) + dice(4)
                else:
                    profs = ["Light Armor", "Medium Armor", "Shield", dnd_tools.artisan_tools("ThievKit")["Name"], dnd_tools.artisan_tools("TinkTools")["Name"]]
                    for prof in profs:                                                                     
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)                       
            profs2 = ["Firearms"]
            for prof in profs2:
                if prof not in player.proficiencies:
                    player.proficiencies.append(prof)
            player.spellcastingclass.append("Artificer")
            player.spellcastingability.append("Int")
            player.notes["Artificer Cantrips Known"] = 2
            player.notes["Artificer 1st Level Spell Slots Known"] = 0
            player.notes["Artificer 2nd Level Spell Slots Known"] = 0
            player.notes["Artificer 3rd Level Spell Slots Known"] = 0
            player.notes["Artificer 4th Level Spell Slots Known"] = 0
            player.notes["Artificer 5th Level Spell Slots Known"] = 0

        #Barbarian
        if player.Class[i] == "Barbarian":
            if param == "N":
                player.barblvl = player.level
                player.classlvl.append(player.barblvl)              
            if param == "Y":
                if player.singlemulticlass == "Y":
                    while True:
                        try:
                            barblvl = int(input(f"Given your pool of levels of {poollevel}, What is your Barbarian level? "))
                            if barblvl <= 0:
                                print("Your Barbarian level must be at least 1, please try again.")
                            elif barblvl <= poollevel:
                                break
                            else:
                                print("You are only able to invest within your pool.")
                        except ValueError: #Handles non-numeric choices  
                            print("Invalid input. Please enter a number.")                   
                    poollevel = poollevel - barblvl
                    player.classlvl.append(barblvl)    
                    player.barblvl = barblvl
                if player.singlemulticlass == "N":
                    player.barblvl = player.level
                    player.classlvl.append(player.barblvl)                      
            if player.barblvl >= 1:
                if i == 0:
                    profs = ["Light Armor", "Medium Armor", "Shield", "Simple Weapons", "Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    player.skills.append(dnd_tools.saving_throws["StrST"])
                    player.skills.append(dnd_tools.saving_throws["ConST"])
                    BarbSkillsList = [
                        dnd_tools.skills["AnimalHandling"], 
                        dnd_tools.skills["Athletics"], 
                        dnd_tools.skills["Intimidation"], 
                        dnd_tools.skills["Nature"], 
                        dnd_tools.skills["Perception"], 
                        dnd_tools.skills["Survival"]
                        ]
                    player.skills = twoskillsfromlist(param, player.skills, BarbSkillsList)
                    StartEquip1 = ["Greataxe", "Martial Melee Weapon"]
                    StartEquip2 = ["Two Handaxes", "Any Simple Weapon"]
                    if param == "Y":
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - Greataxe")
                                print("2 - Martial Melee Weapon")
                                se1 = int(input("What would you like your first choice for starting equipment to be? "))
                                if se1 == 0:
                                    SE1rand = random.choice(StartEquip1)
                                    if SE1rand == "Greataxe":
                                        player.equipment.append(dnd_tools.martial_weapons["Greataxe"].copy())
                                    if SE1rand == "Martial Melee Weapon":
                                        MartWepRandKey = random.choice(MartialMeleeWeapons)
                                        player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey].copy())
                                    break
                                elif se1 == 1:
                                    player.equipment.append(dnd_tools.martial_weapons["Greataxe"].copy())
                                    break
                                elif se1 == 2:
                                    while True:
                                        try:                               
                                            print("0 - Random")
                                            for j, mmw in enumerate(MartialMeleeWeaponsNames, 1):
                                                print(f"{j} - {mmw}")
                                            se1mmw = int(input("Which martial melee weapon would you like to add to your inventory? "))
                                            if se1mmw == 0:
                                                MartWepRandKey = random.choice(MartialMeleeWeapons)
                                                player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey].copy())
                                                break
                                            elif 1 <= se1mmw <= len(MartialMeleeWeapons):
                                                MartWepKey = MartialMeleeWeapons[se1mmw-1]
                                                player.equipment.append(dnd_tools.martial_weapons[MartWepKey].copy())
                                                break
                                            else:
                                                print("Invalid choice, please choose a valid option.") 
                                        except ValueError: #Handles non-numeric choices  
                                            print("Invalid input. Please enter a number.")
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.") 
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        while True:
                            try:                                   
                                print("0 - Random")
                                print("1 - Two Handaxes")
                                print("2 - Any Simple Weapon")
                                se2 = int(input("What would you like your second choice for starting equipment to be? "))
                                if se2 == 0:
                                    SE2rand = random.choice(StartEquip2)
                                    if SE2rand == "Two Handaxes":
                                        player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                                        player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                                    if SE2rand == "Any Simple Weapon":
                                        SimpRandKey = random.choice(SimpleWeapons)
                                        player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                                    break
                                elif se2 == 1:
                                    player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                                    player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                                    break
                                elif se2 == 2:
                                    while True:
                                        try:                               
                                            print("0 - Random")
                                            for j, sw in enumerate(SimpleWeaponsNames, 1):
                                                print(f"{j} - {sw}")
                                            se2sw = int(input("Which simple weapon would you like to add to your inventory? "))
                                            if se2sw == 0:
                                                SimpRandKey = random.choice(SimpleWeapons)
                                                player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                                                break
                                            elif 1 <= se2sw <= len(SimpleWeapons):
                                                SimpKey = SimpleWeapons[se2sw-1]
                                                player.equipment.append(dnd_tools.simple_weapons[SimpKey].copy())
                                                break
                                            else:
                                                print("Invalid choice, please choose a valid option.")
                                        except ValueError: #Handles non-numeric choices  
                                            print("Invalid input. Please enter a number.")
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                        for idx in range(0,4):
                            player.equipment.append(dnd_tools.simple_weapons["Javelin"].copy())
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "Greataxe":
                            player.equipment.append(dnd_tools.martial_weapons["Greataxe"].copy())
                        if SE1rand == "Martial Melee Weapon":
                            MartWepRandKey = random.choice(MartialMeleeWeapons)
                            player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey].copy())
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "Two Handaxes":
                            player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                            player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                        if SE2rand == "Any Simple Weapon":
                            SimpRandKey = random.choice(SimpleWeapons)
                            player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                        player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                        for idx in range(0,4):
                            player.equipment.append(dnd_tools.simple_weapons["Javelin"].copy())
                else:
                    profs = ["Shield", "Simple Weapons", "Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)         
            player.barbrages = 2
            player.barbragedmg = 2             

        #Bard
        if player.Class[i] == "Bard":
            if param == "N":
                player.bardlvl = player.level
                player.classlvl.append(player.bardlvl)             
            if param == "Y":
                if player.singlemulticlass == "Y":
                    while True:
                        try:
                            bardlvl = int(input(f"Given your pool of levels of {poollevel}, What is your Bard level? "))
                            if bardlvl <= 0:
                                print("Your Bard level must be at least 1, please try again.")
                            elif bardlvl <= poollevel:
                                break
                            else:
                                print("You are only able to invest within your pool.")
                        except ValueError: #Handles non-numeric choices  
                            print("Invalid input. Please enter a number.")                  
                    poollevel = poollevel - bardlvl
                    player.classlvl.append(bardlvl)
                    player.bardlvl = bardlvl    
                if player.singlemulticlass == "N":
                    player.bardlvl = player.level
                    player.classlvl.append(player.bardlvl)    
            if player.bardlvl >= 1:     
                if i == 0:
                    profs = ["Light Armor", "Simple Weapons", 
                             dnd_tools.martial_weapons["HandCrossbow"]["Name"], 
                             dnd_tools.martial_weapons["Longsword"]["Name"], 
                             dnd_tools.martial_weapons["Rapier"]["Name"],
                             dnd_tools.martial_weapons["Shortsword"]["Name"]
                             ]                    
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    player.proficiencies = musicalinstr(param, player.proficiencies)
                    player.proficiencies = musicalinstr(param, player.proficiencies)
                    player.proficiencies = musicalinstr(param, player.proficiencies)
                    player.skills.append(dnd_tools.saving_throws["DexST"])
                    player.skills.append(dnd_tools.saving_throws["ChaST"])
                    player.skills = skillprof3(param, player.skills)  
                    StartEquip1 = ["Rapier", "Longsword", "Any Simple Weapon"]
                    StartEquip2 = ["Diplomat's Pack", "Entertainer's Pack"]     
                    StartEquip3 = ["Lute", "Any Other Musical Instrument"]                                   
                    if param == "Y":
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - Rapier")
                                print("2 - Longsword")
                                print("3 - Any Simple Weapon")
                                se1 = int(input("What would you like your first choice for starting equipment to be? "))
                                if se1 == 0:
                                    SE1rand = random.choice(StartEquip1)
                                    if SE1rand == "Rapier":
                                        player.equipment.append(dnd_tools.martial_weapons["Rapier"].copy())
                                    if SE1rand == "Longsword":
                                        player.equipment.append(dnd_tools.martial_weapons["Longsword"].copy())
                                    if SE1rand == "Any Simple Weapon":
                                        SimpRandKey = random.choice(SimpleWeapons)
                                        player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                                    break
                                elif se1 == 1:
                                    player.equipment.append(dnd_tools.martial_weapons["Rapier"].copy())
                                    break
                                elif se1 == 2:
                                    player.equipment.append(dnd_tools.martial_weapons["Longsword"].copy())
                                    break
                                elif se1 == 3:
                                    while True:
                                        try:                               
                                            print("0 - Random")
                                            for j, sw in enumerate(SimpleWeaponsNames, 1):
                                                print(f"{j} - {sw}")
                                            se1sw = int(input("Which simple weapon would you like to add to your inventory? "))
                                            if se1sw == 0:
                                                SimpRandKey = random.choice(SimpleWeapons)
                                                player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                                                break
                                            elif 1 <= se1sw <= len(SimpleWeapons):
                                                SimpKey = SimpleWeapons[se1sw-1]
                                                player.equipment.append(dnd_tools.simple_weapons[SimpKey].copy())
                                                break
                                            else:
                                                print("Invalid choice, please choose a valid option.")
                                        except ValueError: #Handles non-numeric choices  
                                            print("Invalid input. Please enter a number.")
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        while True:
                            try:                                   
                                print("0 - Random")
                                print("1 - Diplomat's Pack")
                                print("2 - Entertainer's Pack")
                                se2 = int(input("What would you like your second choice for starting equipment to be? "))
                                if se2 == 0:
                                    SE2rand = random.choice(StartEquip2)
                                    if SE2rand == "Diplomat's Pack":
                                        player.equipment.append(dnd_tools.packs["DiplomatsPack"].copy())
                                    if SE2rand == "Entertainer's Pack":
                                        player.equipment.append(dnd_tools.packs["EntertainersPack"].copy())
                                    break
                                elif se2 == 1:
                                    player.equipment.append(dnd_tools.packs["DiplomatsPack"].copy())
                                    break
                                elif se2 == 2:
                                    player.equipment.append(dnd_tools.packs["EntertainersPack"].copy())
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        while True:
                            try:                               
                                print("0 - Random")
                                print("1 - Lute")
                                print("2 - Any Other Musical Instrument")
                                se3 = int(input("What would you like your third choice for starting equipment to be? "))
                                if se3 == 0:
                                    SE3rand = random.choice(StartEquip3)
                                    if SE3rand == "Lute":
                                        player.equipment.append(dnd_tools.musical_instr["Lute"].copy())
                                    if SE2rand == "Any Other Musical Instrument":
                                        MIWOLRandKey = random.choice(MusicalInstrWOLute)
                                        player.equipment.append(dnd_tools.musical_instr[MIWOLRandKey].copy())
                                    break
                                elif se3 == 1:
                                    player.equipment.append(dnd_tools.musical_instr["Lute"].copy())
                                    break
                                elif se3 == 2:
                                    while True:
                                        try:                               
                                            print("0 - Random")
                                            for j, miwl in enumerate(MusicalInstrWOLuteNames, 1):
                                                print(f"{j} - {miwl}")
                                            se3mi = int(input("Which Musical Instrument, minus the Lute, would you like to add to your inventory? "))
                                            if se3mi == 0:
                                                MIWOLRandKey = random.choice(MusicalInstrWOLute)
                                                player.equipment.append(dnd_tools.musical_instr[MIWOLRandKey].copy())
                                                break
                                            elif 1 <= se3mi <= len(SimpleWeapons):
                                                MIWOLKey = MusicalInstrWOLute[se3mi-1]
                                                player.equipment.append(dnd_tools.musical_instr[MIWOLKey].copy())
                                                break
                                            else:
                                                print("Invalid choice, please choose a valid option.")
                                        except ValueError: #Handles non-numeric choices  
                                            print("Invalid input. Please enter a number.")
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "Rapier":
                            player.equipment.append(dnd_tools.martial_weapons["Rapier"].copy())
                        if SE1rand == "Longsword":
                            player.equipment.append(dnd_tools.martial_weapons["Longsword"].copy())
                        if SE1rand == "Any Simple Weapon":
                            SimpRandKey = random.choice(SimpleWeapons)
                            player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "Diplomat's Pack":
                            player.equipment.append(dnd_tools.packs["DiplomatsPack"].copy())
                        if SE2rand == "Entertainer's Pack":
                            player.equipment.append(dnd_tools.packs["EntertainersPack"].copy())
                        SE3rand = random.choice(StartEquip3)
                        if SE3rand == "Lute":
                            player.equipment.append(dnd_tools.musical_instr["Lute"].copy())
                        if SE2rand == "Any Other Musical Instrument":
                            MIWOLRandKey = random.choice(MusicalInstrWOLute)
                            player.equipment.append(dnd_tools.musical_instr[MIWOLRandKey].copy())                           
                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())                         
                else:
                    profs = ["Light Armor"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    player.skills = skillprof(param, player.skills)   
                    player.proficiencies = musicalinstr(param, player.proficiencies)                                                                                                      
            player.spellcastingclass.append("Bard")
            player.spellcastingability.append("Cha")
            player.notes["Bard Cantrips Known"] = 2
            player.notes["Bard Spells Known"] = 4
            player.notes["Bard 1st Level Spell Slots Known"] = 2
            player.notes["Bard 2nd Level Spell Slots Known"] = 0
            player.notes["Bard 3rd Level Spell Slots Known"] = 0
            player.notes["Bard 4th Level Spell Slots Known"] = 0
            player.notes["Bard 5th Level Spell Slots Known"] = 0
            player.notes["Bard 6th Level Spell Slots Known"] = 0
            player.notes["Bard 7th Level Spell Slots Known"] = 0
            player.notes["Bard 8th Level Spell Slots Known"] = 0
            player.notes["Bard 9th Level Spell Slots Known"] = 0
            player.spellcastingfocus = "Musical Instrument"    
            

        #Cleric
        if player.Class[i] == "Cleric":
            if param == "N":
                player.clerlvl = player.level
                player.classlvl.append(player.clerlvl) 
            if param == "Y":
                if player.singlemulticlass == "Y":
                    while True:
                        try:
                            clerlvl = int(input(f"Given your pool of levels of {poollevel}, What is your Cleric level? "))
                            if clerlvl <= 0:
                                print("Your Cleric level must be at least 1, please try again.")
                            elif clerlvl <= poollevel:
                                break
                            else:
                                print("You are only able to invest within your pool.")
                        except ValueError: #Handles non-numeric choices  
                            print("Invalid input. Please enter a number.")                 
                    poollevel = poollevel - clerlvl
                    player.classlvl.append(clerlvl)
                    player.clerlvl = clerlvl
                if player.singlemulticlass == "N":
                    player.clerlvl = player.level
                    player.classlvl.append(player.clerlvl)
            if player.clerlvl >= 1:
                if i == 0:    
                    profs = ["Light Armor", "Medium Armor", "Shield"]         
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    player.skills.append(dnd_tools.saving_throws["WisST"])
                    player.skills.append(dnd_tools.saving_throws["ChaST"])
                    SkillsList = [
                        dnd_tools.skills["History"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Medicine"], 
                        dnd_tools.skills["Persuasion"], 
                        dnd_tools.skills["Religion"]
                        ]
                    player.skills = twoskillsfromlist(param, player.skills, SkillsList)   
                    StartEquip1 = ["Mace", "Warhammer (if proficient)"]
                    StartEquip2 = ["Scale Mail", "Leather Armor", "Chain Mail (if proficient)"]     
                    StartEquip3 = ["Light Crossbow w/ 20 Bolts", "Any Simple Weapon"]
                    StartEquip4 = ["Priest's Pack", "Explorer's Pack"]    
                    if param == "Y":
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - Mace")
                                print("2 - Warhammer (if proficient)")
                                se1 = int(input("What would you like your first choice for starting equipment to be? "))
                                if se1 == 0:
                                    SE1rand = random.choice(StartEquip1)
                                    if SE1rand == "Mace":
                                        player.equipment.append(dnd_tools.simple_weapons["Mace"].copy())
                                    if SE1rand == "Warhammer (if proficient)":
                                        if "Warhammer" in player.proficiencies:
                                            player.equipment.append(dnd_tools.martial_weapons["Warhammer"].copy())
                                        else:
                                            player.equipment.append(dnd_tools.simple_weapons["Mace"].copy())
                                    break
                                elif se1 == 1:
                                    player.equipment.append(dnd_tools.simple_weapons["Mace"].copy())
                                    break
                                elif se1 == 2:
                                    if "Warhammer" in player.proficiencies:
                                        player.equipment.append(dnd_tools.martial_weapons["Warhammer"].copy())
                                    else:
                                        player.equipment.append(dnd_tools.simple_weapons["Mace"].copy())
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        while True:
                            try:                                   
                                print("0 - Random")
                                print("1 - Scale Mail")
                                print("2 - Leather Armor")
                                print("3 - Chain Mail (if proficient)")
                                se2 = int(input("What would you like your second choice for starting equipment to be? "))
                                if se2 == 0:
                                    SE2rand = random.choice(StartEquip2)
                                    if SE2rand == "Scale Mail":
                                        player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                                    if SE2rand == "Leather Armor":
                                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                                    if SE2rand == "Chain Mail (if proficient)":
                                        while True:
                                            if ("Chain Mail" in player.proficiencies) or ("Heavy Armor" in player.proficiencies):
                                                player.equipment.append(dnd_tools.heavy_armor["ChainMail"].copy())
                                                break
                                            else:
                                                SE2rand = random.choice(StartEquip2)
                                                if SE2rand != "Chain Mail (if proficient)":
                                                    if SE2rand == "Scale Mail":
                                                        player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                                                    if SE2rand == "Leather Armor":
                                                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                                                    break      
                                    break                          
                                elif se2 == 1:
                                    player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                                    break
                                elif se2 == 2:
                                    player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                                    break
                                elif se2 == 3:
                                    if ("Chain Mail" in player.proficiencies) or ("Heavy Armor" in player.proficiencies):
                                        player.equipment.append(dnd_tools.heavy_armor["ChainMail"].copy())
                                    else:
                                        while True:
                                            try:                                   
                                                print("0 - Random")
                                                print("1 - Scale Mail")
                                                print("2 - Leather Armor")
                                                se2 = int(input("You are not proficient in Chain Mail, please make a different choice. "))
                                                if se2 == 0:
                                                    SE2rand = random.choice(StartEquip2)
                                                    if SE2rand == "Scale Mail":
                                                        player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                                                    if SE2rand == "Leather Armor":
                                                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())   
                                                    break   
                                                elif se2 == 1:
                                                    player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                                                    break
                                                elif se2 == 2:
                                                    player.equipment.append(dnd_tools.light_armor["Leather"].copy())  
                                                    break   
                                                else:
                                                    print("Invalid choice, please choose a valid option.")
                                            except ValueError: #Handles non-numeric choices  
                                                print("Invalid input. Please enter a number.")
                                        break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")      
                        while True:
                            try:                                                                                                           
                                print("0 - Random")
                                print("1 - Light Crossbow w/ 20 Bolts")
                                print("2 - Any Simple Weapon")
                                se3 = int(input("What would you like your third choice for starting equipment to be? "))
                                if se3 == 0:
                                    SE3rand = random.choice(StartEquip3)
                                    if SE3rand == "Light Crossbow w/ 20 Bolts":
                                        player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                                        player.equipment.append("20 Bolts")
                                    if SE3rand == "Any Simple Weapon":    
                                        SimpKeyRand = random.choice(SimpleWeapons)                        
                                        player.equipment.append(dnd_tools.simple_weapons[SimpKeyRand].copy())
                                    break
                                elif se3 == 1:
                                    player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                                    player.equipment.append("20 Bolts")
                                    break
                                elif se3 == 2:
                                    while True:
                                        try:                           
                                            print("0 - Random")
                                            for j, sw in enumerate(SimpleWeaponsNames, 1):
                                                print(f"{j} - {sw}")
                                            se3sw = int(input("Which simple weapon would you like to add to your inventory? "))
                                            if se3sw == 0:
                                                SimpKeyRand = random.choice(SimpleWeapons)                        
                                                player.equipment.append(dnd_tools.simple_weapons[SimpKeyRand].copy())
                                                break
                                            elif 1 <= se3sw <= len(SimpleWeapons):
                                                SimpKey = SimpleWeapons[se3sw-1]
                                                player.equipment.append(dnd_tools.simple_weapons[SimpKey].copy())  
                                                break
                                            else:
                                                print("Invalid choice, please choose a valid option.")
                                        except ValueError: #Handles non-numeric choices  
                                            print("Invalid input. Please enter a number.")
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")  
                        while True:
                            try:                                                        
                                print("0 - Random")
                                print("1 - Priest's Pack")
                                print("2 - Explorer's Pack")
                                se4 = int(input("What would you like your fourth choice for starting equipment to be? "))                        
                                if se4 == 0:
                                    SE4rand = random.choice(StartEquip4)
                                    if SE4rand == "Priest's Pack":
                                        player.equipment.append(dnd_tools.packs["PriestsPack"].copy())
                                    if SE4rand == "Explorer's Pack":
                                        player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                                    break
                                elif se4 == 1:
                                    player.equipment.append(dnd_tools.packs["PriestsPack"].copy())
                                    break
                                elif se4 == 2:
                                    player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        player.equipment.append(dnd_tools.heavy_armor["ChainMail"].copy())
                        player.equipment.append("A Holy Symbol")
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "Mace":
                            player.equipment.append(dnd_tools.simple_weapons["Mace"].copy())
                        if SE1rand == "Warhammer (if proficient)":
                            if "Warhammer" in player.proficiencies:
                                player.equipment.append(dnd_tools.martial_weapons["Warhammer"].copy())
                            else:
                                player.equipment.append(dnd_tools.simple_weapons["Mace"].copy())           
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "Scale Mail":
                            player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                        if SE2rand == "Leather Armor":
                            player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        if SE2rand == "Chain Mail (if proficient)":
                            while True:
                                if ("Chain Mail" in player.proficiencies) or ("Heavy Armor" in player.proficiencies):
                                    player.equipment.append(dnd_tools.heavy_armor["ChainMail"].copy())
                                    break
                                else:
                                    SE2rand = random.choice(StartEquip2)
                                    if SE2rand != "Chain Mail (if proficient)":
                                        if SE2rand == "Scale Mail":
                                            player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                                        if SE2rand == "Leather Armor":
                                            player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                                        break
                        SE3rand = random.choice(StartEquip3)
                        if SE3rand == "Light Crossbow w/ 20 Bolts":
                            player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                            player.equipment.append("20 Bolts")
                        if SE3rand == "Any Simple Weapon":    
                            SimpKeyRand = random.choice(SimpleWeapons)                        
                            player.equipment.append(dnd_tools.simple_weapons[SimpKeyRand].copy())                                                               
                        SE4rand = random.choice(StartEquip4)
                        if SE4rand == "Priest's Pack":
                            player.equipment.append(dnd_tools.packs["PriestsPack"].copy())
                        if SE4rand == "Explorer's Pack":
                            player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())                           
                        player.equipment.append(dnd_tools.heavy_armor["ChainMail"].copy())
                        player.equipment.append("A Holy Symbol")      
                else:
                    profs = ["Light Armor", "Medium Armor", "Shield"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof) 
            player.spellcastingclass.append("Cleric")
            player.spellcastingability.append("Wis")
            player.notes["Cleric Cantrips Known"] = 3
            player.notes["Cleric 1st Level Spell Slots Known"] = 2
            player.notes["Cleric 2nd Level Spell Slots Known"] = 0
            player.notes["Cleric 3rd Level Spell Slots Known"] = 0
            player.notes["Cleric 4th Level Spell Slots Known"] = 0
            player.notes["Cleric 5th Level Spell Slots Known"] = 0
            player.notes["Cleric 6th Level Spell Slots Known"] = 0
            player.notes["Cleric 7th Level Spell Slots Known"] = 0
            player.notes["Cleric 8th Level Spell Slots Known"] = 0
            player.notes["Cleric 9th Level Spell Slots Known"] = 0
            if player.subclass[i] == "Arcana Domain Cleric":
                player.skills.append(dnd_tools.skills["Arcana"])  

        #Druid
        if player.Class[i] == "Druid":
            if param == "N":
                player.druidlvl = player.level
                player.classlvl.append(player.druidlvl) 
            if param == "Y":
                if player.singlemulticlass == "Y":
                    while True:
                        try:
                            drulvl = int(input(f"Given your pool of levels of {poollevel}, What is your Druid level? "))
                            if drulvl <= 0:
                                print("Your Druid level must be at least 1, please try again.")
                            elif drulvl <= poollevel:
                                break
                            else:
                                print("You are only able to invest within your pool.")
                        except ValueError: #Handles non-numeric choices  
                            print("Invalid input. Please enter a number.")                  
                    poollevel = poollevel - drulvl
                    player.classlvl.append(drulvl)
                    player.druidlvl = drulvl
                if player.singlemulticlass == "N":
                    player.druidlvl = player.level
                    player.classlvl.append(player.druidlvl) 
            if player.druidlvl >= 1:
                if i == 0:
                    profs = ["Light Armor", "Medium Armor", "Shield"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    player.notes["Druid Metal Notes"] = "Druids will not wear armor or use shields made of metal"
                    firstprofs = [
                        dnd_tools.simple_weapons["Club"]["Name"],
                        dnd_tools.simple_weapons["Dagger"]["Name"],
                        dnd_tools.simple_weapons["Dart"]["Name"],
                        dnd_tools.simple_weapons["Javelin"]["Name"],
                        dnd_tools.simple_weapons["Mace"]["Name"],
                        dnd_tools.simple_weapons["Quarterstaff"]["Name"],
                        dnd_tools.martial_weapons["Scimitar"]["Name"],
                        dnd_tools.simple_weapons["Sickle"]["Name"],
                        dnd_tools.simple_weapons["Sling"]["Name"],
                        dnd_tools.simple_weapons["Spear"]["Name"],
                        dnd_tools.kits["HerbKit"]["Name"]      
                        ]    
                    for fprof in firstprofs:
                        if fprof not in player.proficiencies:
                            player.proficiencies.append(fprof)
                    player.skills.append(dnd_tools.saving_throws["WisST"])
                    player.skills.append(dnd_tools.saving_throws["IntST"])
                    SkillsList = [
                        dnd_tools.skills["Arcana"], 
                        dnd_tools.skills["AnimalHandling"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Medicine"], 
                        dnd_tools.skills["Nature"], 
                        dnd_tools.skills["Perception"], 
                        dnd_tools.skills["Religion"], 
                        dnd_tools.skills["Survival"]
                        ]
                    player.skills = twoskillsfromlist(param, player.skills, SkillsList)  
                    StartEquip1 = ["Wooden Shield", "Any Simple Weapon"]
                    StartEquip2 = ["Scimitar", "Any Simple Melee Weapon"]
                    if param == "Y":
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - Wooden Shield")
                                print("2 - Any Simple Weapon")
                                se1 = int(input("What would you like your first choice for starting equipment to be? "))
                                if se1 == 0:
                                    SE1rand = random.choice(StartEquip1)
                                    if SE1rand == "Wooden Shield":
                                        player.equipment.append(dnd_tools.shields["Wooden Shield"].copy())
                                    if SE1rand == "Any Simple Weapon":
                                        SimpRandKey = random.choice(SimpleWeapons)
                                        player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                                    break
                                elif se1 == 1:
                                    player.equipment.append(dnd_tools.shields["Wooden Shield"].copy())
                                    break
                                elif se1 == 2:
                                    while True:
                                        try:                               
                                            print("0 - Random")
                                            for j, sw in enumerate(SimpleWeaponsNames, 1):
                                                print(f"{j} - {sw}")
                                            se1sw = int(input("Which simple weapon would you like to add to your inventory? "))
                                            if se1sw == 0:
                                                SimpRandKey = random.choice(SimpleWeapons)
                                                player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                                                break
                                            elif 1 <= se1sw <= len(SimpleWeapons):
                                                SimpKey = SimpleWeapons[se1sw-1]
                                                player.equipment.append(dnd_tools.simple_weapons[SimpKey].copy()) 
                                                break
                                            else:
                                                print("Invalid choice, please choose a valid option.")
                                        except ValueError: #Handles non-numeric choices  
                                            print("Invalid input. Please enter a number.")
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - Scimitar")
                                print("2 - Any Simple Melee Weapon")
                                se2 = int(input("What would you like your second choice for starting equipment to be? "))
                                if se2 == 0:
                                    SE2rand = random.choice(StartEquip2)
                                    if SE2rand == "Scimitar":
                                        player.equipment.append(dnd_tools.martial_weapons["Scimitar"].copy())
                                    if SE2rand == "Any Simple Melee Weapon":
                                        SimpRandMKey = random.choice(SimpleMeleeWeapons)
                                        player.equipment.append(dnd_tools.simple_weapons[SimpRandMKey].copy())
                                    break
                                elif se2 == 1:
                                    player.equipment.append(dnd_tools.martial_weapons["Scimitar"].copy())
                                    break
                                elif se2 == 2:
                                    while True:
                                        try:                               
                                            print("0 - Random")
                                            for j, smw in enumerate(SimpleMeleeWeaponsNames, 1):
                                                print(f"{j} - {smw}")
                                            se2smw = int(input("Which simple melee weapon would you like to add to your inventory? "))
                                            if se2smw == 0:
                                                SimpRandMKey = random.choice(SimpleMeleeWeapons)
                                                player.equipment.append(dnd_tools.simple_weapons[SimpRandMKey].copy())
                                                break
                                            elif 1 <= se2smw <= len(SimpleMeleeWeaponsNames):
                                                SimpMKey = SimpleMeleeWeapons[se2smw-1]
                                                player.equipment.append(dnd_tools.simple_weapons[SimpMKey].copy()) 
                                                break
                                            else:
                                                print("Invalid choice, please choose a valid option.")
                                        except ValueError: #Handles non-numeric choices  
                                            print("Invalid input. Please enter a number.")
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                        player.equipment.append("Druidic Focus")
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "Wooden Shield":
                            player.equipment.append(dnd_tools.shields["Wooden Shield"].copy())
                        if SE1rand == "Any Simple Weapon":
                            SimpRandKey = random.choice(SimpleWeapons)
                            player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "Scimitar":
                             player.equipment.append(dnd_tools.martial_weapons["Scimitar"].copy())
                        if SE2rand == "Any Simple Melee Weapon":
                            SimpRandMKey = random.choice(SimpleMeleeWeapons)
                            player.equipment.append(dnd_tools.simple_weapons[SimpRandMKey].copy())
                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                        player.equipment.append("Druidic Focus")
                else:
                    profs = ["Light Armor", "Medium Armor", "Shield"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)   
            player.spellcastingclass.append("Druid")
            player.spellcastingability.append("Wis")
            player.notes["Druid Cantrips Known"] = 2
            player.notes["Druid 1st Level Spell Slots Known"] = 2
            player.notes["Druid 2nd Level Spell Slots Known"] = 0
            player.notes["Druid 3rd Level Spell Slots Known"] = 0
            player.notes["Druid 4th Level Spell Slots Known"] = 0
            player.notes["Druid 5th Level Spell Slots Known"] = 0
            player.notes["Druid 6th Level Spell Slots Known"] = 0
            player.notes["Druid 7th Level Spell Slots Known"] = 0
            player.notes["Druid 8th Level Spell Slots Known"] = 0
            player.notes["Druid 9th Level Spell Slots Known"] = 0
            player.notes["Druidic"] = "You know Druidic, the secret language of druids. You can speak the language and use it to leave hidden messages. You and others who know this language automatically spot such a message. Others spot the message's presence with a successful DC 15 Wisdom (Perception) check but can't decipher it without magic."
        
        #Fighter
        if player.Class[i] == "Fighter":
            if param == "N":
                player.figlvl = player.level
                player.classlvl.append(player.figlvl)   
            if param == "Y":
                if player.singlemulticlass == "Y":
                    while True:
                        try:
                            figlvl = int(input(f"Given your pool of levels of {poollevel}, What is your Fighter level? "))
                            if figlvl <= 0:
                                print("Your Fighter level must be at least 1, please try again.")
                            elif figlvl <= poollevel:
                                break
                            else:
                                print("You are only able to invest within your pool.")
                        except ValueError: #Handles non-numeric choices  
                            print("Invalid input. Please enter a number.")                     
                    poollevel = poollevel - figlvl
                    player.classlvl.append(figlvl)
                    player.figlvl = figlvl
                if player.singlemulticlass == "N":
                    player.figlvl = player.level
                    player.classlvl.append(player.figlvl) 
            if player.figlvl >= 1:
                if i == 0:       
                    profs = ["Light Armor", "Medium Armor", "Heavy Armor", "Shield", "Simple Weapons", "Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)                                
                    player.skills.append(dnd_tools.saving_throws["StrST"])
                    player.skills.append(dnd_tools.saving_throws["ConST"])
                    SkillsList = [
                        dnd_tools.skills["Acrobatics"], 
                        dnd_tools.skills["AnimalHandling"], 
                        dnd_tools.skills["Athletics"], 
                        dnd_tools.skills["History"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Intimidation"], 
                        dnd_tools.skills["Perception"], 
                        dnd_tools.skills["Survival"]
                        ]
                    player.skills = twoskillsfromlist(param, player.skills, SkillsList)  
                    StartEquip1 = ["Chain Mail", "Leather Armor, Longbow and 20 Arrows"]
                    StartEquip2 = ["Martial Weapon and Shield", "Two Martial Weapons"]
                    StartEquip3 = ["Light Crossbow and 20 Bolts", "Two Handaxes"]
                    StartEquip4 = ["Dungeoneer's Pack", "Explorer's Pack"]
                    if param == "Y":
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - Chain Mail")
                                print("2 - Leather Armor, Longbow and 20 Arrows")
                                se1 = int(input("What would you like your first choice for starting equipment to be? "))
                                if se1 == 0:
                                    SE1rand = random.choice(StartEquip1)
                                    if SE1rand == "Chain Mail":
                                        player.equipment.append(dnd_tools.heavy_armor["ChainMail"].copy())
                                    if SE1rand == "Leather Armor, Longbow and 20 Arrows":
                                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                                        player.equipment.append(dnd_tools.martial_weapons["Longbow"].copy())
                                        player.equipment.append("20 Arrows")
                                    break
                                elif se1 == 1:
                                    player.equipment.append(dnd_tools.heavy_armor["ChainMail"].copy())
                                    break
                                elif se1 == 2:
                                    player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                                    player.equipment.append(dnd_tools.martial_weapons["Longbow"].copy())
                                    player.equipment.append("20 Arrows")
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        while True:
                            try:                               
                                print("0 - Random")
                                print("1 - Martial Weapon and Shield")
                                print("2 - Two Martial Weapons")
                                se2 = int(input("What would you like your second choice for starting equipment to be? "))
                                if se2 == 0:
                                    SE2rand = random.choice(StartEquip2)
                                    if SE2rand == "Martial Weapon and Shield":
                                        chosen_weapon = random.choice(MartialWeapons)
                                        player.equipment.append(dnd_tools.martial_weapons[chosen_weapon].copy())
                                        player.equipment.append(dnd_tools.shields["Shield"].copy())
                                    if SE2rand == "Two Martial Weapons":
                                        MartWepRandKey1 = random.choice(MartialWeapons)
                                        player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey1].copy())
                                        MartWepRandKey2 = random.choice(MartialWeapons)
                                        player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey2].copy())
                                    break
                                elif se2 == 1:
                                    while True:
                                        try:                               
                                            print("0 - Random")
                                            for j, mw in enumerate(MartialWeaponsNames, 1):
                                                print(f"{j} - {mw}")
                                            se2mw = int(input("Which martial weapon would you like to add to your inventory? "))
                                            if se2mw == 0:
                                                MartWepRandKey = random.choice(MartialWeapons)
                                                player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey].copy())
                                                player.equipment.append(dnd_tools.shields["Shield"].copy())
                                                break
                                            elif 1 <= se2mw <= len(MartialWeapons):
                                                MartWepKey = MartialMeleeWeapons[se2mw-1]
                                                player.equipment.append(dnd_tools.martial_weapons[MartWepKey].copy())
                                                player.equipment.append(dnd_tools.shields["Shield"].copy())
                                                break
                                            else:
                                                print("Invalid choice, please choose a valid option.")
                                        except ValueError: #Handles non-numeric choices  
                                            print("Invalid input. Please enter a number.")
                                    break
                                    
                                elif se2 == 2:
                                    while True:
                                        try:                               
                                            print("0 - Random")
                                            for j, mw1 in enumerate(MartialWeaponsNames, 1):
                                                print(f"{j} - {mw1}")
                                            se2mw1 = int(input("Choose your first martial weapon to add to your inventory? "))
                                            if se2mw1 == 0:
                                                MartWepRandKey1 = random.choice(MartialWeapons)
                                                player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey1].copy())
                                                break
                                            elif 1 <= se2mw1 <= len(MartialWeapons):
                                                MartWepKey1 = MartialMeleeWeapons[se2mw1-1]
                                                player.equipment.append(dnd_tools.martial_weapons[MartWepKey1].copy())
                                                break
                                            else:
                                                print("Invalid choice, please choose a valid option.")
                                        except ValueError: #Handles non-numeric choices  
                                            print("Invalid input. Please enter a number.")
                                    while True:
                                        try:                               
                                            print("0 - Random")
                                            for j, mw in enumerate(MartialWeaponsNames, 1):
                                                print(f"{j} - {mw}")
                                            se2mw2 = int(input("Choose your second martial weapon to add to your inventory? "))
                                            if se2mw2 == 0:
                                                MartWepRandKey2 = random.choice(MartialWeapons)
                                                player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey2].copy())
                                                break
                                            elif 1 <= se2mw2 <= len(MartialWeapons):
                                                MartWepKey2 = MartialMeleeWeapons[se2mw2-1]
                                                player.equipment.append(dnd_tools.martial_weapons[MartWepKey2].copy())
                                                break
                                            else:
                                                print("Invalid choice, please choose a valid option.")
                                        except ValueError: #Handles non-numeric choices  
                                            print("Invalid input. Please enter a number.")
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")      
                        while True:
                            try:                                                         
                                print("0 - Random")
                                print("1 - Light Crossbow and 20 Bolts")
                                print("2 - Two Handaxes")       
                                se3 = int(input("What would you like your third choice for starting equipment to be? "))
                                if se3 == 0:
                                    SE3rand = random.choice(StartEquip3)
                                    if SE3rand == "Light Crossbow and 20 Bolts":
                                        player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                                        player.equipment.append("20 Bolts")
                                    if SE3rand == "Two Handaxes":
                                        player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                                        player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                                    break
                                elif se3 == 1:
                                    player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                                    player.equipment.append("20 Bolts")
                                    break
                                elif se3 == 2: 
                                    player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                                    player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy()) 
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        while True:
                            try:                               
                                print("0 - Random")
                                print("1 - Dungeoneer's Pack")
                                print("2 - Explorer's Pack")       
                                se4 = int(input("What would you like your fourth choice for starting equipment to be? "))                       
                                if se4 == 0:
                                    SE4rand = random.choice(StartEquip4)
                                    if SE4rand == "Dungeoneer's Pack":
                                        player.equipment.append(dnd_tools.packs["DungeoneersPack"].copy())
                                    if SE4rand == "Explorer's Pack":
                                        player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                                    break
                                elif se4 == 1:
                                    player.equipment.append(dnd_tools.packs["DungeoneersPack"].copy())
                                    break
                                elif se4 == 2:
                                    player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "Chain Mail":
                            player.equipment.append(dnd_tools.heavy_armor["ChainMail"].copy())
                        if SE1rand == "Leather Armor, Longbow and 20 Arrows":
                            player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                            player.equipment.append(dnd_tools.martial_weapons["Longbow"].copy())
                            player.equipment.append("20 Arrows")
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "Martial Weapon and Shield":
                            MartWepRandKey = random.choice(MartialWeapons)
                            player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey].copy())
                            player.equipment.append(dnd_tools.shields["Shield"].copy())
                        if SE2rand == "Two Martial Weapons":
                            MartWepRandKey1 = random.choice(MartialWeapons)
                            player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey1].copy())
                            MartWepRandKey2 = random.choice(MartialWeapons)
                            player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey2].copy())
                        SE3rand = random.choice(StartEquip3)
                        if SE3rand == "Light Crossbow and 20 Bolts":
                            player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                            player.equipment.append("20 Bolts")
                        if SE3rand == "Two Handaxes":
                            player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                            player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                        SE4rand = random.choice(StartEquip4)
                        if SE4rand == "Dungeoneer's Pack":
                            player.equipment.append(dnd_tools.packs["DungeoneersPack"].copy())
                        if SE4rand == "Explorer's Pack":
                            player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                else:
                    profs = ["Light Armor", "Medium Armor", "Shield", "Simple Weapons", "Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)                                                                             

        #Monk
        if player.Class[i] == "Monk":
            if param == "N":
                player.monklvl = player.level
                player.classlvl.append(player.monklvl) 
            if param == "Y":
                if player.singlemulticlass == "Y":
                    while True:
                        try:
                            monklvl = int(input(f"Given your pool of levels of {poollevel}, What is your Monk level? "))
                            if monklvl <= 0:
                                print("Your Monk level must be at least 1, please try again.")
                            elif monklvl <= poollevel:
                                break
                            else:
                                print("You are only able to invest within your pool.")
                        except ValueError: #Handles non-numeric choices  
                            print("Invalid input. Please enter a number.")          
                    poollevel = poollevel - monklvl
                    player.classlvl.append(monklvl)
                    player.monklvl = monklvl   
                if player.singlemulticlass == "N":
                    player.monklvl = player.level
                    player.classlvl.append(player.monklvl) 
            if player.monklvl >= 1:
                if i == 0:
                    profs = ["Simple Weapons", dnd_tools.martial_weapons["Shortsword"]["Name"]]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)       
                    player.proficiencies = artisantoolsmusicalinstr(param, player.proficiencies)
                    player.skills.append(dnd_tools.saving_throws["StrST"])
                    player.skills.append(dnd_tools.saving_throws["DexST"])
                    SkillsList = [
                        dnd_tools.skills["Acrobatics"], 
                        dnd_tools.skills["Athletics"], 
                        dnd_tools.skills["History"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Religion"], 
                        dnd_tools.skills["Stealth"]
                        ]    
                    player.skills = twoskillsfromlist(param, player.skills, SkillsList)  
                    StartEquip1 = ["Shortsword", "Any Simple Weapon"]
                    StartEquip2 = ["Dungeoneer's Pack", "Explorer's Pack"]
                    if param == "Y":
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - Shortsword")
                                print("2 - Any Simple Weapon")
                                se1 = int(input("What would you like your first choice for starting equipment to be? "))
                                if se1 == 0:
                                    SE1rand = random.choice(StartEquip1)
                                    if SE1rand == "Shortsword":
                                        player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                                    if SE1rand == "Any Simple Weapon":
                                        SimpRandKey = random.choice(SimpleWeapons)
                                        player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                                    break
                                elif se1 == 1:
                                    player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                                    break
                                elif se1 == 2:
                                    while True:
                                        try:                               
                                            print("0 - Random")
                                            for j, sw in enumerate(SimpleWeaponsNames, 1):
                                                print(f"{j} - {sw}")
                                            se1 = int(input("Which simple weapon would you like to add to your inventory? "))
                                            if se1 == 0:
                                                SimpRandKey = random.choice(SimpleWeapons)
                                                player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                                                break
                                            elif 1 <= se1 <= len(SimpleWeapons):
                                                SimpKey = SimpleWeapons[se1-1]
                                                player.equipment.append(dnd_tools.simple_weapons[SimpKey].copy())
                                                break
                                            else:
                                                print("Invalid choice, please choose a valid option.")
                                        except ValueError: #Handles non-numeric choices  
                                            print("Invalid input. Please enter a number.")
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        while True:
                            try:                                   
                                print("0 - Random")
                                print("1 - Dungeoneer's Pack")
                                print("2 - Explorer's Pack")
                                se2 = int(input("What would you like your second choice for starting equipment to be? "))
                                if se2 == 0:
                                    SE2rand = random.choice(StartEquip2)
                                    if SE2rand == "Dungeoneer's Pack":
                                        player.equipment.append(dnd_tools.packs["DungeoneersPack"].copy())
                                    if SE2rand == "Explorer's Pack":
                                        player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                                    break
                                elif se2 == 1:
                                    player.equipment.append(dnd_tools.packs["DungeoneersPack"].copy())
                                    break
                                elif se2 == 2:
                                    player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        player.equipment.append("10 Darts")
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "Shortsword":
                             player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                        if SE1rand == "Any Simple Weapon":
                            SimpRandKey = random.choice(SimpleWeapons)
                            player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "Dungeoneer's Pack":
                            player.equipment.append(dnd_tools.packs["DungeoneersPack"].copy())
                        if SE2rand == "Explorer's Pack":
                            player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                        player.equipment.append("10 Darts")
                else:  
                    profs = ["Simple Weapons", "Shortsword"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)

        #Paladin
        if player.Class[i] == "Paladin":
            if param == "N":
                player.pallvl = player.level
                player.classlvl.append(player.pallvl) 
            if param == "Y":
                if player.singlemulticlass == "Y":
                    while True:
                        try:
                            pallvl = int(input(f"Given your pool of levels of {poollevel}, What is your Paladin level? "))
                            if pallvl <= 0:
                                print("Your Paladin level must be at least 1, please try again.")
                            elif pallvl <= poollevel:
                                break
                            else:
                                print("You are only able to invest within your pool.")
                        except ValueError: #Handles non-numeric choices  
                            print("Invalid input. Please enter a number.")                 
                    poollevel = poollevel - pallvl
                    player.classlvl.append(pallvl)
                    player.pallvl = pallvl
                if player.singlemulticlass == "N":
                    player.pallvl = player.level
                    player.classlvl.append(player.pallvl) 
            if player.pallvl >= 1:
                if i == 0:
                    profs = ["Light Armor", "Medium Armor", "Heavy Armor", "Shield", "Simple Weapons", "Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)                            
                    player.skills.append(dnd_tools.saving_throws["WisST"])
                    player.skills.append(dnd_tools.saving_throws["ChaST"])
                    SkillsList = [
                        dnd_tools.skills["Athletics"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Intimidation"], 
                        dnd_tools.skills["Medicine"], 
                        dnd_tools.skills["Persuasion"], 
                        dnd_tools.skills["Religion"]
                        ]
                    player.skills = twoskillsfromlist(param, player.skills, SkillsList)      
                    StartEquip1 = ["A Martial Weapon and a Shield", "Two Martial Weapons"]
                    StartEquip2 = ["Five Javelins", "Any Simple Melee Weapon"]
                    StartEquip3 = ["Priest's Pack", "Explorer's Pack"]
                    if param == "Y":
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - A Martial Weapon and a Shield")
                                print("2 - Two Martial Weapons")
                                se1 = int(input("What would you like your first choice for starting equipment to be? "))
                                if se1 == 0:
                                    SE1rand = random.choice(StartEquip1)
                                    if SE1rand == "Martial Weapon and Shield":
                                        chosen_weapon = random.choice(MartialWeapons)
                                        player.equipment.append(dnd_tools.martial_weapons[chosen_weapon].copy())
                                        player.equipment.append(dnd_tools.shields["Shield"].copy())
                                    if SE1rand == "Two Martial Weapons":
                                        MartWepRandKey1 = random.choice(MartialWeapons)
                                        player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey1].copy())
                                        MartWepRandKey2 = random.choice(MartialWeapons)
                                        player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey2].copy())
                                    break
                                elif se2 == 1:
                                    while True:
                                        try:                               
                                            print("0 - Random")
                                            for j, mw in enumerate(MartialWeaponsNames, 1):
                                                print(f"{j} - {mw}")
                                            se2mw = int(input("Which martial weapon would you like to add to your inventory? "))
                                            if se2mw == 0:
                                                MartWepRandKey = random.choice(MartialWeapons)
                                                player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey].copy())
                                                player.equipment.append(dnd_tools.shields["Shield"].copy())
                                                break
                                            elif 1 <= se2mw <= len(MartialWeapons):
                                                MartWepKey = MartialMeleeWeapons[se2mw-1]
                                                player.equipment.append(dnd_tools.martial_weapons[MartWepKey].copy())
                                                player.equipment.append(dnd_tools.shields["Shield"].copy())
                                                break
                                            else:
                                                print("Invalid choice, please choose a valid option.")
                                        except ValueError: #Handles non-numeric choices  
                                            print("Invalid input. Please enter a number.")
                                    break
                                elif se2 == 2:
                                    while True:
                                        try:                               
                                            print("0 - Random")
                                            for j, mw1 in enumerate(MartialWeaponsNames, 1):
                                                print(f"{j} - {mw1}")
                                            se2mw1 = int(input("Choose your first martial weapon to add to your inventory? "))
                                            if se2mw1 == 0:
                                                MartWepRandKey1 = random.choice(MartialWeapons)
                                                player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey1].copy())
                                                break
                                            elif 1 <= se2mw1 <= len(MartialWeapons):
                                                MartWepKey1 = MartialMeleeWeapons[se2mw1-1]
                                                player.equipment.append(dnd_tools.martial_weapons[MartWepKey1].copy())
                                                break
                                            else:
                                                print("Invalid choice, please choose a valid option.")
                                        except ValueError: #Handles non-numeric choices  
                                            print("Invalid input. Please enter a number.")                              
                                    while True:
                                        try:                               
                                            print("0 - Random")
                                            for j, mw in enumerate(MartialWeaponsNames, 1):
                                                print(f"{j} - {mw}")
                                            se2mw2 = int(input("Choose your second martial weapon to add to your inventory? "))
                                            if se2mw2 == 0:
                                                MartWepRandKey2 = random.choice(MartialWeapons)
                                                player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey2].copy())
                                                break
                                            elif 1 <= se2mw2 <= len(MartialWeapons):
                                                MartWepKey2 = MartialMeleeWeapons[se2mw2-1]
                                                player.equipment.append(dnd_tools.martial_weapons[MartWepKey2].copy())
                                                break
                                            else:
                                                print("Invalid choice, please choose a valid option.")
                                        except ValueError: #Handles non-numeric choices  
                                            print("Invalid input. Please enter a number.")
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")                                
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - Five Javelins")
                                print("2 - Any Simple Melee Weapon")
                                se2 = int(input("What would you like your second choice for starting equipment to be? "))
                                if se2 == 0:
                                    SE2rand = random.choice(StartEquip2)
                                    if SE2rand == "Five Javelins":
                                        for idx in range(0,5):
                                            player.equipment.append(dnd_tools.simple_weapons["Javelin"].copy())
                                    if SE2rand == "Any Simple Melee Weapon":
                                        SimpRandMKey = random.choice(SimpleMeleeWeapons)
                                        player.equipment.append(dnd_tools.simple_weapons[SimpRandMKey].copy())
                                    break
                                elif se2 == 1:
                                    for idx in range(0,5):
                                        player.equipment.append(dnd_tools.simple_weapons["Javelin"].copy())
                                    break
                                elif se2 == 2:
                                    while True:
                                        try:                               
                                            print("0 - Random")
                                            for j, smw in enumerate(SimpleMeleeWeaponsNames, 1):
                                                print(f"{j} - {smw}")
                                            se2smw = int(input("Which simple melee weapon would you like to add to your inventory? "))
                                            if se2smw == 0:
                                                SimpRandMKey = random.choice(SimpleMeleeWeapons)
                                                player.equipment.append(dnd_tools.simple_weapons[SimpRandMKey].copy())
                                            elif 1 <= se2smw <= len(SimpleMeleeWeaponsNames):
                                                SimpMKey = SimpleMeleeWeapons[se2smw-1]
                                                player.equipment.append(dnd_tools.simple_weapons[SimpMKey].copy())  
                                            else:
                                                print("Invalid choice, please choose a valid option.")
                                        except ValueError: #Handles non-numeric choices  
                                            print("Invalid input. Please enter a number.")
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - A Priest's Pack")
                                print("2 - An Explorer's Pack")
                                se3 = int(input("What would you like your third choice for starting equipment to be? "))
                                if se3 == 0:
                                    SE3rand = random.choice(StartEquip3)
                                    if SE3rand == "Priest's Pack":
                                        player.equipment.append(dnd_tools.packs["PriestsPack"].copy())
                                    if SE3rand == "Explorer's Pack":
                                        player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                                    break
                                elif se3 == 1:
                                    player.equipment.append(dnd_tools.packs["PriestsPack"].copy())
                                    break
                                elif se3 == 2:
                                    player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        player.equipment.append(dnd_tools.heavy_armor["ChainMail"].copy())
                        player.equipment.append("A Holy Symbol")
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "Martial Weapon and Shield":
                            MartWepRandKey = random.choice(MartialWeapons)
                            player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey].copy())
                            player.equipment.append(dnd_tools.shields["Shield"].copy())
                        if SE1rand == "Two Martial Weapons":
                            MartWepRandKey1 = random.choice(MartialWeapons)
                            player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey1].copy())
                            MartWepRandKey2 = random.choice(MartialWeapons)
                            player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey2].copy())
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "Five Javelins":
                            for idx in range(0,5):
                                player.equipment.append(dnd_tools.simple_weapons["Javelin"].copy())
                        if SE2rand == "Any Simple Melee Weapon":
                            SimpRandMKey = random.choice(SimpleMeleeWeapons)
                            player.equipment.append(dnd_tools.simple_weapons[SimpRandMKey].copy())
                        SE3rand = random.choice(StartEquip3)
                        if SE3rand == "Priest's Pack":
                            player.equipment.append(dnd_tools.packs["PriestsPack"].copy())
                        if SE3rand == "Explorer's Pack":
                            player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())                            
                        player.equipment.append(dnd_tools.heavy_armor["ChainMail"].copy())
                        player.equipment.append("A Holy Symbol")  
                else:
                    profs = ["Light Armor", "Medium Armor", "Shield", "Simple Weapons", "Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)  

        #Ranger
        if player.Class[i] == "Ranger":
            if param == "N":
                player.ranlvl = player.level
                player.classlvl.append(player.ranlvl)
            if param == "Y":
                if player.singlemulticlass == "Y":
                    while True:
                        try:
                            ranlvl = int(input(f"Given your pool of levels of {poollevel}, What is your Ranger level? "))
                            if ranlvl <= 0:
                                print("Your Ranger level must be at least 1, please try again.")
                            elif ranlvl <= poollevel:
                                break
                            else:
                                print("You are only able to invest within your pool.")
                        except ValueError: #Handles non-numeric choices  
                            print("Invalid input. Please enter a number.")               
                    poollevel = poollevel - ranlvl
                    player.classlvl.append(ranlvl)
                    player.ranlvl = ranlvl 
                if player.singlemulticlass == "N":
                    player.ranlvl = player.level
                    player.classlvl.append(player.ranlvl)
            if player.ranlvl >= 1:
                if i == 0:                               
                    profs = ["Light Armor", "Medium Armor", "Shield", "Simple Weapons", "Martial Weapons"]
                    for prof in profs:      
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)                             
                    player.skills.append(dnd_tools.saving_throws["StrST"])
                    player.skills.append(dnd_tools.saving_throws["DexST"])
                    SkillsList = [
                        dnd_tools.skills["AnimalHandling"], 
                        dnd_tools.skills["Athletics"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Investigation"], 
                        dnd_tools.skills["Nature"], 
                        dnd_tools.skills["Perception"], 
                        dnd_tools.skills["Stealth"], 
                        dnd_tools.skills["Survival"]
                        ]
                    player.skills = threeskillsfromlist(param, player.skills, SkillsList)         
                    StartEquip1 = ["Scale Mail", "Leather Armor"]
                    StartEquip2 = ["Two Shortswords", "Two Simple Melee Weapons"]
                    StartEquip3 = ["Dungeoneer's Pack", "Explorer's Pack"]
                    if param == "Y":
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - Scale Mail")
                                print("2 - Leather Armor")
                                se1 = int(input("What would you like your first choice for starting equipment to be? "))
                                if se1 == 0:
                                    SE1rand = random.choice(StartEquip1)
                                    if SE1rand == "Scale Mail":
                                        player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                                    if SE1rand == "Leather Armor":
                                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                                    break
                                elif se1 == 1:
                                    player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                                    break
                                elif se1 == 2:
                                    player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - Two Shortswords")
                                print("2 - Two Simple Melee Weapons")
                                se2 = int(input("What would you like your second choice for starting equipment to be? "))
                                if se2 == 0:
                                    SE2rand = random.choice(StartEquip2)
                                    if SE2rand == "Two Shortswords":
                                        player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                                        player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                                    if SE2rand == "Two Simple Melee Weapons":
                                        SimpMRandKey1 = random.choice(SimpleMeleeWeapons)
                                        player.equipment.append(dnd_tools.simple_weapons[SimpMRandKey1].copy())
                                        SimpMRandKey2 = random.choice(SimpleMeleeWeapons)
                                        player.equipment.append(dnd_tools.simple_weapons[SimpMRandKey2].copy())
                                    break
                                elif se2 == 1:
                                    player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                                    player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                                    break
                                elif se2 == 2:
                                    while True:
                                        try:                               
                                            print("0 - Random")
                                            for j, smw in enumerate(SimpleMeleeWeaponsNames, 1):
                                                print(f"{j} - {smw}")
                                            se2smw1 = int(input("Which simple melee weapon would you like to add to your inventory first? "))
                                            if se2smw1 == 0:
                                                SimpMRandKey1 = random.choice(SimpleMeleeWeapons)
                                                player.equipment.append(dnd_tools.simple_weapons[SimpMRandKey1].copy())
                                                break
                                            elif 1 <= se2smw1 <= len(SimpleMeleeWeaponsNames):
                                                SimpMKey = SimpleMeleeWeapons[se2smw1-1]
                                                player.equipment.append(dnd_tools.simple_weapons[SimpMKey].copy())
                                                break
                                            else:
                                                print("Invalid choice, please choose a valid option.")
                                        except ValueError: #Handles non-numeric choices  
                                            print("Invalid input. Please enter a number.")
                                    while True:
                                        try:                               
                                            print("0 - Random")
                                            for j, smw in enumerate(SimpleMeleeWeaponsNames, 1):
                                                print(f"{j} - {smw}")
                                            se2smw2 = int(input("Which simple melee weapon would you like to add to your inventory second? "))
                                            if se2smw2 == 0:
                                                SimpMRandKey2 = random.choice(SimpleMeleeWeapons)
                                                player.equipment.append(dnd_tools.simple_weapons[SimpMRandKey2].copy())
                                                break
                                            elif 1 <= se2smw2 <= len(SimpleMeleeWeaponsNames):
                                                SimpMKey = SimpleMeleeWeapons[se2smw2-1]
                                                player.equipment.append(dnd_tools.simple_weapons[SimpMKey].copy())
                                                break
                                            else:
                                                print("Invalid choice, please choose a valid option.")
                                        except ValueError: #Handles non-numeric choices  
                                            print("Invalid input. Please enter a number.")
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")                            
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - Dungeoneer's Pack")
                                print("2 - Explorer's Pack")
                                se3 = int(input("What would you like your third choice for starting equipment to be? "))
                                if se3 == 0:
                                    SE3rand = random.choice(StartEquip3)
                                    if SE3rand == "Dungeoneer's Pack":
                                        player.equipment.append(dnd_tools.packs["DungeoneersPack"].copy())                       
                                    if SE3rand == "Explorer's Pack":
                                        player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                                    break
                                elif se3 == 1:
                                    player.equipment.append(dnd_tools.packs["DungeoneersPack"].copy())
                                    break
                                elif se3 == 2:
                                    player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        player.equipment.append(dnd_tools.martial_weapons["Longbow"].copy())
                        player.equipment.append("A Quiver of 20 Arrows")
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "Scale Mail":
                            player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                        if SE1rand == "Leather Armor":
                            player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "Two Shortswords":
                             player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                             player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                        if SE2rand == "Two Simple Melee Weapons":
                            SimpMRandKey1 = random.choice(SimpleMeleeWeapons)
                            player.equipment.append(dnd_tools.simple_weapons[SimpMRandKey1].copy())
                            SimpMRandKey2 = random.choice(SimpleMeleeWeapons)
                            player.equipment.append(dnd_tools.simple_weapons[SimpMRandKey2].copy())
                        SE3rand = random.choice(StartEquip3)
                        if SE3rand == "Dungeoneer's Pack":
                            player.equipment.append(dnd_tools.packs["DungeoneersPack"].copy())                       
                        if SE3rand == "Explorer's Pack":
                            player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())                        
                        player.equipment.append(dnd_tools.martial_weapons["Longbow"].copy())
                        player.equipment.append("A Quiver of 20 Arrows")
                else:
                    profs = ["Light Armor", "Medium Armor", "Shield", "Simple Weapons", "Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)      
                    SkillsList = [
                        dnd_tools.skills["AnimalHandling"], 
                        dnd_tools.skills["Athletics"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Investigation"], 
                        dnd_tools.skills["Nature"], 
                        dnd_tools.skills["Perception"], 
                        dnd_tools.skills["Stealth"], 
                        dnd_tools.skills["Survival"]
                        ]
                    player.skills = oneskillfromlist(param, player.skills, SkillsList)       
            player.notes["Favored Enemy(1)"] = "You have significant experience studying, tracking, hunting, and even talking to a certain type of enemy.\nChoose a type of favored enemy: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies.\nYou have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.\nWhen you gain this feature, you also learn one language of your choice that is spoken by your favored enemies, if they speak one at all (not adapted into your languages).\nMore options are available at higher levels. As you gain levels, your choices should reflect the types of monsters you have encountered on your adventures."
            player.notes["Natural Explorer"] = "You are particularly familiar with one type of natural environment and are adept at traveling and surviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, grassland, mountain, swamp, or the Underdark. When you make an Intelligence or Wisdom check related to your favored terrain, your Proficiency Bonus is doubled if you are using a skill that you're proficient in.\nWhile traveling for an hour or more in your favored terrain, you gain the following benefits:\n- Difficult terrain doesn't slow your group's travel.\n- Your group can't become lost except by magical means.\n- Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.\n- If you are traveling alone, you can move stealthily at a normal pace.\n- When you forage, you find twice as much food as you normally would.\n- While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.\nYou choose additional favored terrain types at 6th and 10th level."

        #Rogue
        if player.Class[i] == "Rogue":
            if param == "N":
                player.roglvl = player.level
                player.classlvl.append(player.roglvl)
            if param == "Y":
                if player.singlemulticlass == "Y":
                    while True:
                        try:
                            roglvl = int(input(f"Given your pool of levels of {poollevel}, What is your Rogue level? "))
                            if roglvl <= 0:
                                print("Your Rogue level must be at least 1, please try again.")
                            elif roglvl <= poollevel:
                                break
                            else:
                                print("You are only able to invest within your pool.")
                        except ValueError: #Handles non-numeric choices  
                            print("Invalid input. Please enter a number.")                 
                    poollevel = poollevel - roglvl
                    player.classlvl.append(roglvl)
                    player.roglvl = roglvl
                if player.singlemulticlass == "N":
                    player.roglvl = player.level
                    player.classlvl.append(player.roglvl)
            if player.roglvl >= 1:
                if i == 0:       
                    profs = ["Light Armor", "Simple Weapons",
                            dnd_tools.martial_weapons["HandCrossbow"]["Name"],
                            dnd_tools.martial_weapons["Longsword"]["Name"],
                            dnd_tools.martial_weapons["Rapier"]["Name"],
                            dnd_tools.martial_weapons["Shortsword"]["Name"]
                            ]     
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    player.proficiencies.append(dnd_tools.kits["ThievKit"]["Name"]) 
                    player.skills.append(dnd_tools.saving_throws["IntST"])
                    player.skills.append(dnd_tools.saving_throws["DexST"])
                    SkillsList = [
                        dnd_tools.skills["Acrobatics"], 
                        dnd_tools.skills["Athletics"], 
                        dnd_tools.skills["Deception"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Intimidation"], 
                        dnd_tools.skills["Investigation"], 
                        dnd_tools.skills["Perception"], 
                        dnd_tools.skills["Performance"], 
                        dnd_tools.skills["Persuasion"], 
                        dnd_tools.skills["SleightofHand"], 
                        dnd_tools.skills["Stealth"]
                        ]
                    player.skills = fourskillsfromlist(param, player.skills, SkillsList)   
                    StartEquip1 = ["Rapier", "Shortsword"]
                    StartEquip2 = ["Shortbow and Quiver of 20 Arrows", "Shortsword"]
                    StartEquip3 = ["Burglar's Pack", "Dungeoneer's Pack", "Explorer's Pack"]
                    if param == "Y":
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - Rapier")
                                print("2 - Shortsword")
                                se1 = int(input("What would you like your first choice for starting equipment to be? "))
                                if se1 == 0:
                                    SE1rand = random.choice(StartEquip1)
                                    if SE1rand == "Rapier":
                                        player.equipment.append(dnd_tools.martial_weapons["Rapier"].copy())
                                    if SE1rand == "Shortsword":
                                        player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                                    break
                                elif se1 == 1:
                                    player.equipment.append(dnd_tools.martial_weapons["Rapier"].copy())
                                    break
                                elif se1 == 2:
                                    player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - Shortbow and Quiver of 20 Arrows")
                                print("2 - Shortsword")
                                se2 = int(input("What would you like your second choice for starting equipment to be? "))
                                if se2 == 0:
                                    SE2rand = random.choice(StartEquip2)
                                    if SE2rand == "Shortbow and Quiver of 20 Arrows":
                                        player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                                        player.equipment.append("Quiver of 20 Arrows")
                                    if SE2rand == "Shortsword":
                                        player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                                    break
                                elif se2 == 1:
                                    player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                                    player.equipment.append("Quiver of 20 Arrows")
                                    break
                                elif se2 == 2:
                                    player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - Burglar's Pack")
                                print("2 - Dungeoneer's Pack")
                                print("3 - Explorer's Pack")
                                se3 = int(input("What would you like your third choice for starting equipment to be? "))     
                                if se3 == 0:
                                    SE3rand = random.choice(StartEquip3)
                                    if SE3rand == "Burglar's Pack":
                                        player.equipment.append(dnd_tools.packs["BurglarsPack"].copy())
                                    if SE3rand == "Dungeoneer's Pack":
                                        player.equipment.append(dnd_tools.packs["DungeoneersPack"].copy())
                                    if SE3rand == "Explorer's Pack":
                                        player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                                    break
                                elif se3 == 1:
                                    player.equipment.append(dnd_tools.packs["BurglarsPack"].copy())
                                    break
                                elif se3 == 2:
                                    player.equipment.append(dnd_tools.packs["DungeoneersPack"].copy())
                                    break
                                elif se3 == 3:
                                    player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                        player.equipment.append(dnd_tools.kits["ThievKit"].copy())
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "Rapier":
                            player.equipment.append(dnd_tools.martial_weapons["Rapier"].copy())
                        if SE1rand == "Shortsword":
                            player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "Shortbow and Quiver of 20 Arrows":
                            player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                            player.equipment.append("Quiver of 20 Arrows")
                        if SE2rand == "Shortsword":
                             player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                        SE3rand = random.choice(StartEquip3)
                        if SE3rand == "Burglar's Pack":
                            player.equipment.append(dnd_tools.packs["BurglarsPack"].copy())
                        if SE3rand == "Dungeoneer's Pack":
                            player.equipment.append(dnd_tools.packs["DungeoneersPack"].copy())
                        if SE3rand == "Explorer's Pack":
                            player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())                            
                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                        player.equipment.append(dnd_tools.kits["ThievKit"].copy())                                                   
                else:
                    profs = ["Light Armor"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    SkillsList = [
                        dnd_tools.skills["Acrobatics"], 
                        dnd_tools.skills["Athletics"], 
                        dnd_tools.skills["Deception"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Intimidation"], 
                        dnd_tools.skills["Investigation"], 
                        dnd_tools.skills["Perception"], 
                        dnd_tools.skills["Performance"], 
                        dnd_tools.skills["Persuasion"], 
                        dnd_tools.skills["SleightofHand"], 
                        dnd_tools.skills["Stealth"]
                        ]                            
                    player.skills = oneskillfromlist(param, player.skills, SkillsList)
                    player.proficiencies.append(dnd_tools.kits["ThievKit"]["Name"]) 
            player.notes["Thieves' Cant"] = "During your rogue training you learned thieves' cant, a secret mix of dialect, jargon, and code that allows you to hide messages in seemingly normal conversation. Only another creature that knows thieves' cant understands such messages. It takes four times longer to convey such a message than it does to speak the same idea plainly.\nIn addition, you understand a set of secret signs and symbols used to convey short, simple messages, such as whether an area is dangerous or the territory of a thieves' guild, whether loot is nearby, or whether the people in an area are easy marks or will provide a safe house for thieves on the run."

        #Sorcerer
        if player.Class[i] == "Sorcerer":
            if param == "N":
                player.sorclvl = player.level
                player.classlvl.append(player.sorclvl)              
            if param == "Y":
                if player.singlemulticlass == "Y":
                    while True:
                        try:
                            sorclvl = int(input(f"Given your pool of levels of {poollevel}, What is your Sorcerer level? "))
                            if sorclvl <= 0:
                                print("Your Sorcerer level must be at least 1, please try again.")
                            elif sorclvl <= poollevel:
                                break
                            else:
                                print("You are only able to invest within your pool.")
                        except ValueError: #Handles non-numeric choices  
                            print("Invalid input. Please enter a number.")               
                    poollevel = poollevel - sorclvl
                    player.classlvl.append(sorclvl)
                    player.sorclvl = sorclvl
                if player.singlemulticlass == "N":
                    player.sorclvl = player.level
                    player.classlvl.append(player.sorclvl)  
            if player.sorclvl >= 1:  
                if i == 0: 
                    profs = [
                        dnd_tools.simple_weapons["Dagger"]["Name"],
                        dnd_tools.simple_weapons["Dart"]["Name"],
                        dnd_tools.simple_weapons["Sling"]["Name"],
                        dnd_tools.simple_weapons["Quarterstaff"]["Name"],
                        dnd_tools.simple_weapons["LightCrossbow"]["Name"]
                        ]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)       
                    player.skills.append(dnd_tools.saving_throws["ConST"])
                    player.skills.append(dnd_tools.saving_throws["ChaST"])
                    SkillsList = [
                        dnd_tools.skills["Arcana"], 
                        dnd_tools.skills["Deception"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Intimidation"], 
                        dnd_tools.skills["Persuasion"], 
                        dnd_tools.skills["Religion"]
                        ]
                    player.skills = twoskillsfromlist(param, player.skills, SkillsList)  
                    StartEquip1 = ["A Light Crossbow and 20 Bolts", "Any Simple Weapon"]
                    StartEquip2 = ["A Component Pouch", "An Arcane Focus"]
                    StartEquip3 = ["Dungeoneer's Pack", "Explorer's Pack"]
                    if param == "Y":
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - A Light Crossbow and 20 Bolts")
                                print("2 - Any Simple Weapon")
                                se1 = int(input("What would you like your first choice for starting equipment to be? "))
                                if se1 == 0:
                                    SE1rand = random.choice(StartEquip1)
                                    if SE1rand == "A Light Crossbow and 20 Bolts":
                                        player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                                        player.equipment.append("20 Bolts")
                                    if SE1rand == "Any Simple Weapon":
                                        SimpRandKey = random.choice(SimpleWeapons)
                                        player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                                    break
                                elif se1 == 1:
                                    player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                                    player.equipment.append("20 Bolts")
                                    break
                                elif se1 == 2:
                                    while True:
                                        try:                               
                                            print("0 - Random")
                                            for j, sw in enumerate(SimpleWeaponsNames, 1):
                                                print(f"{j} - {sw}")
                                            se1 = int(input("Which simple weapon would you like to add to your inventory? "))
                                            if se1 == 0:
                                                SimpRandKey = random.choice(SimpleWeapons)
                                                player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                                                break
                                            elif 1 <= se1 <= len(SimpleWeapons):
                                                SimpKey = SimpleWeapons[se1-1]
                                                player.equipment.append(dnd_tools.simple_weapons[SimpKey].copy())
                                                break
                                            else:
                                                print("Invalid choice, please choose a valid option.")
                                        except ValueError: #Handles non-numeric choices  
                                            print("Invalid input. Please enter a number.")
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - A Component Pouch")
                                print("2 - An Arcane Focus")
                                se2 = int(input("What would you like your second choice for starting equipment to be? "))
                                if se2 == 0:
                                    SE2rand = random.choice(StartEquip2)
                                    if SE2rand == "A Component Pouch":
                                        player.equipment.append(dnd_tools.CompPouch.copy())
                                    if SE2rand == "An Arcane Focus":
                                        player.equipment.append("Arcane Focus")
                                    break
                                elif se2 == 1:
                                    player.equipment.append(dnd_tools.CompPouch.copy())
                                    break
                                elif se2 == 2:
                                    player.equipment.append("Arcane Focus")
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - Dungeoneer's Pack")
                                print("2 - Explorer's Pack")
                                se3 = int(input("What would you like your third choice for starting equipment to be? "))  
                                if se3 == 0:
                                    SE3rand = random.choice(StartEquip3)
                                    if SE3rand == "Dungeoneer's Pack":
                                        player.equipment.append(dnd_tools.packs["DungeoneersPack"].copy())
                                    if SE3rand == "Explorer's Pack":
                                        player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                                    break
                                elif se3 == 1:
                                    player.equipment.append(dnd_tools.packs["DungeoneersPack"].copy())
                                    break
                                elif se3 == 2:    
                                    player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")        
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "A Light Crossbow and 20 Bolts":
                            player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                            player.equipment.append("20 Bolts")
                        if SE1rand == "Any Simple Weapon":
                            SimpRandKey = random.choice(SimpleWeapons)
                            player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "A Component Pouch":
                            player.equipment.append(dnd_tools.CompPouch.copy())
                        if SE2rand == "An Arcane Focus":
                            player.equipment.append("Arcane Focus")
                        SE3rand = random.choice(StartEquip3)
                        if SE3rand == "Dungeoneer's Pack":
                            player.equipment.append(dnd_tools.packs["DungeoneersPack"].copy())
                        if SE3rand == "Explorer's Pack":
                            player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())                            
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())  
            player.spellcastingclass.append("Sorcerer")
            player.spellcastingability.append("Cha")
            player.notes["Sorcerer Cantrips Known"] = 4
            player.notes["Sorcerer Spells Known"] = 2
            player.notes["Sorcerer 1st Level Spell Slots Known"] = 2
            player.notes["Sorcerer 2nd Level Spell Slots Known"] = 0
            player.notes["Sorcerer 3rd Level Spell Slots Known"] = 0
            player.notes["Sorcerer 4th Level Spell Slots Known"] = 0
            player.notes["Sorcerer 5th Level Spell Slots Known"] = 0
            player.notes["Sorcerer 6th Level Spell Slots Known"] = 0
            player.notes["Sorcerer 7th Level Spell Slots Known"] = 0
            player.notes["Sorcerer 8th Level Spell Slots Known"] = 0
            player.notes["Sorcerer 9th Level Spell Slots Known"] = 0

        #Warlock
        if player.Class[i] == "Warlock":   
            if param == "N":
                player.warlvl = player.level
                player.classlvl.append(player.warlvl) 
            if param == "Y":
                if player.singlemulticlass == "Y":
                    while True:
                        try:
                            warlvl = int(input(f"Given your pool of levels of {poollevel}, What is your Warlock level? "))
                            if warlvl <= 0:
                                print("Your Warlock level must be at least 1, please try again.")
                            elif warlvl <= poollevel:
                                break
                            else:
                                print("You are only able to invest within your pool.")
                        except ValueError: #Handles non-numeric choices  
                            print("Invalid input. Please enter a number.")                
                    poollevel = poollevel - warlvl
                    player.classlvl.append(warlvl)
                    player.warlvl = warlvl
                if player.singlemulticlass == "N":
                    player.warlvl = player.level
                    player.classlvl.append(player.warlvl) 
            if player.warlvl >= 1:
                if i == 0: 
                    profs = ["Light Armor", "Simple Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)                                
                    player.skills.append(dnd_tools.saving_throws["ChaST"])
                    player.skills.append(dnd_tools.saving_throws["WisST"])
                    SkillsList = [
                        dnd_tools.skills["Arcana"], 
                        dnd_tools.skills["Deception"], 
                        dnd_tools.skills["History"], 
                        dnd_tools.skills["Intimidation"], 
                        dnd_tools.skills["Investigation"], 
                        dnd_tools.skills["Nature"], 
                        dnd_tools.skills["Religion"]
                        ]
                    player.skills = twoskillsfromlist(param, player.skills, SkillsList)  
                    StartEquip1 = ["A Light Crossbow and 20 Bolts", "Any Simple Weapon"]
                    StartEquip2 = ["A Component Pouch", "An Arcane Focus"]
                    StartEquip3 = ["Scholar's Pack", "Dungeoneer's Pack"]
                    if param == "Y":
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - A Light Crossbow and 20 Bolts")
                                print("2 - Any Simple Weapon")
                                se1 = int(input("What would you like your first choice for starting equipment to be? "))
                                if se1 == 0:
                                    SE1rand = random.choice(StartEquip1)
                                    if SE1rand == "A Light Crossbow and 20 Bolts":
                                        player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                                        player.equipment.append("20 Bolts")
                                    if SE1rand == "Any Simple Weapon":
                                        SimpRandKey = random.choice(SimpleWeapons)
                                        player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                                    break
                                elif se1 == 1:
                                    player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                                    player.equipment.append("20 Bolts")
                                    break
                                elif se1 == 2:
                                    while True:
                                        try:                               
                                            print("0 - Random")
                                            for j, sw in enumerate(SimpleWeaponsNames, 1):
                                                print(f"{j} - {sw}")
                                            se1sw = int(input("Which simple weapon would you like to add to your inventory? "))
                                            if se1sw == 0:
                                                SimpRandKey = random.choice(SimpleWeapons)
                                                player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                                                break
                                            elif 1 <= se1sw <= len(SimpleWeapons):
                                                SimpKey = SimpleWeapons[se1sw - 1]
                                                player.equipment.append(dnd_tools.simple_weapons[SimpKey].copy())
                                                break
                                            else:
                                                print("Invalid choice, please choose a valid option.")
                                        except ValueError: #Handles non-numeric choices  
                                            print("Invalid input. Please enter a number.")
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - A Component Pouch")
                                print("2 - An Arcane Focus")
                                se2 = int(input("What would you like your second choice for starting equipment to be? "))
                                if se2 == 0:
                                    SE2rand = random.choice(StartEquip2)
                                    if SE2rand == "A Component Pouch":
                                        player.equipment.append(dnd_tools.CompPouch.copy())
                                    if SE2rand == "An Arcane Focus":
                                        player.equipment.append("Arcane Focus")
                                    break
                                elif se2 == 1:
                                    player.equipment.append(dnd_tools.CompPouch.copy())
                                    break
                                elif se2 == 2:
                                    player.equipment.append("Arcane Focus")
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - A Scholar's Pack")
                                print("2 - A Dungeoneer's Pack")
                                se3 = int(input("What would you like your third choice for starting equipment to be? "))    
                                if se3 == 0:
                                    SE3rand = random.choice(StartEquip3)
                                    if SE3rand == "Scholar's Pack":
                                        player.equipment.append(dnd_tools.packs["ScholarsPack"].copy())
                                    if SE3rand == "Dungeoneer's Pack":
                                        player.equipment.append(dnd_tools.packs["DungeoneersPack"].copy())
                                    break
                                elif se3 == 1:
                                    player.equipment.append(dnd_tools.packs["ScholarsPack"].copy())
                                    break
                                elif se3 == 2:
                                    player.equipment.append(dnd_tools.packs["DungeoneersPack"].copy())
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")                                      
                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        while True:
                            try:                           
                                print("0 - Random")
                                for j, sw in enumerate(SimpleWeaponsNames, 1):
                                    print(f"{j} - {sw}")
                                sesw = int(input("Which simple weapon would you like to add to your inventory? "))
                                if sesw == 0:
                                    SimpRandKey = random.choice(SimpleWeapons)
                                    player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                                    break
                                elif 1 <= sesw <= len(SimpleWeapons):
                                    SimpKey = SimpleWeapons[sesw - 1]
                                    player.equipment.append(dnd_tools.simple_weapons[SimpKey].copy())
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "A Light Crossbow and 20 Bolts":
                            player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                            player.equipment.append("20 Bolts")
                        if SE1rand == "Any Simple Weapon":
                            SimpRandKey = random.choice(SimpleWeapons)
                            player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "A Component Pouch":
                            player.equipment.append(dnd_tools.CompPouch.copy())
                        if SE2rand == "An Arcane Focus":
                            player.equipment.append("Arcane Focus")
                        SE3rand = random.choice(StartEquip3)
                        if SE3rand == "Scholar's Pack":
                            player.equipment.append(dnd_tools.packs["ScholarsPack"].copy())
                        if SE3rand == "Dungeoneer's Pack":
                            player.equipment.append(dnd_tools.packs["DungeoneersPack"].copy())                            
                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        SimpRandKey = random.choice(SimpleWeapons)
                        player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())  
                else:
                    profs = ["Light Armor", "Simple Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)                                                                         
            player.spellcastingclass.append("Warlock")
            player.spellcastingability.append("Cha")
            player.notes["Warlock Cantrips Known"] = 2
            player.notes["Warlock Spells Known"] = 2
            player.notes["Warlock Spell Slots"] = 1
            player.notes["Warlock Spell Slot Level"] = "1st"
            
        #Wizard
        if player.Class[i] == "Wizard":
            if param == "N":
                player.wizlvl = player.level
                player.classlvl.append(player.wizlvl)  
            if param == "Y":
                if player.singlemulticlass == "Y":
                    while True:
                        try:
                            wizlvl = int(input(f"Given your pool of levels of {poollevel}, What is your Wizard level? "))
                            if wizlvl <= 0:
                                print("Your Wizard level must be at least 1, please try again.")
                            elif wizlvl <= poollevel:
                                break
                            else:
                                print("You are only able to invest within your pool.")
                        except ValueError: #Handles non-numeric choices  
                            print("Invalid input. Please enter a number.")                 
                    poollevel = poollevel - wizlvl
                    player.classlvl.append(wizlvl)   
                    player.wizlvl = wizlvl 
                if player.singlemulticlass == "N": 
                    player.wizlvl = player.level
                    player.classlvl.append(player.wizlvl)          
            if player.wizlvl >= 1:
                if i == 0:
                    profs = [
                        dnd_tools.simple_weapons["Dagger"]["Name"],
                        dnd_tools.simple_weapons["Dart"]["Name"],
                        dnd_tools.simple_weapons["Sling"]["Name"],
                        dnd_tools.simple_weapons["Quarterstaff"]["Name"],
                        dnd_tools.simple_weapons["LightCrossbow"]["Name"]
                        ]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)   
                    player.skills.append(dnd_tools.saving_throws["IntST"])
                    player.skills.append(dnd_tools.saving_throws["WisST"])
                    SkillsList = [
                        dnd_tools.skills["Arcana"], 
                        dnd_tools.skills["History"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Investigation"], 
                        dnd_tools.skills["Medicine"], 
                        dnd_tools.skills["Religion"]
                        ]
                    player.skills = twoskillsfromlist(param, player.skills, SkillsList) 
                    StartEquip1 = ["Quarterstaff", "Dagger"]
                    StartEquip2 = ["A Component Pouch", "An Arcane Focus"]
                    StartEquip3 = ["Scholar's Pack", "Explorer's Pack"]
                    if param == "Y":
                        while True:
                            try:                           
                                print("0 - Random")
                                print("1 - Quarterstaff")
                                print("2 - Dagger")
                                se1 = int(input("What would you like your first choice for starting equipment to be? "))
                                if se1 == 0:
                                    SE1rand = random.choice(StartEquip1)
                                    if SE1rand == "Quarterstaff":
                                        player.equipment.append(dnd_tools.simple_weapons["Quarterstaff"].copy())
                                    if SE1rand == "Dagger":
                                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                                    break
                                elif se1 == 1:
                                    player.equipment.append(dnd_tools.simple_weapons["Quarterstaff"].copy())
                                    break
                                elif se1 == 2:
                                    player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        while True:
                            try:                               
                                print("0 - Random")
                                print("1 - A Component Pouch")
                                print("2 - An Arcane Focus")
                                se2 = int(input("What would you like your second choice for starting equipment to be? "))
                                if se2 == 0:
                                    SE2rand = random.choice(StartEquip2)
                                    if SE2rand == "A Component Pouch":
                                        player.equipment.append(dnd_tools.CompPouch.copy())
                                    if SE2rand == "An Arcane Focus":
                                        player.equipment.append("Arcane Focus")
                                    break
                                elif se2 == 1:
                                    player.equipment.append(dnd_tools.CompPouch.copy())
                                    break
                                elif se2 == 2:
                                    player.equipment.append("Arcane Focus")
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        while True:
                            try:                               
                                print("0 - Random")
                                print("1 - A Scholar's Pack")
                                print("2 - An Explorer's Pack")
                                se3 = int(input("What would you like your third choice for starting equipment to be? "))
                                if se3 == 0:
                                    SE3rand = random.choice(StartEquip3)
                                    if SE3rand == "Scholar's Pack":
                                        player.equipment.append(dnd_tools.packs["ScholarsPack"].copy())
                                    if SE3rand == "Explorer's Pack":
                                        player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                                    break
                                elif se3 == 1:
                                    player.equipment.append(dnd_tools.packs["ScholarsPack"].copy())   
                                    break
                                elif se3 == 2:
                                    player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError: #Handles non-numeric choices  
                                print("Invalid input. Please enter a number.")
                        player.equipment.append("Spellbook")
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "Quarterstaff":
                            player.equipment.append(dnd_tools.simple_weapons["Quarterstaff"].copy())
                        if SE1rand == "Dagger":
                            player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "A Component Pouch":
                            player.equipment.append(dnd_tools.CompPouch.copy())
                        if SE2rand == "An Arcane Focus":
                            player.equipment.append("Arcane Focus")
                        SE3rand = random.choice(StartEquip3)
                        if SE3rand == "Scholar's Pack":
                            player.equipment.append(dnd_tools.packs["ScholarsPack"].copy())
                        if SE3rand == "Explorer's Pack":
                            player.equipment.append(dnd_tools.packs["ExplorersPack"].copy())                            
                        player.equipment.append("Spellbook")       
            player.spellcastingclass.append("Wizard")
            player.spellcastingability.append("Int")
            player.notes["Wizard Cantrips Known"] = 3
            player.notes["Wizard 1st Level Spell Slots Known"] = 2
            player.notes["Wizard 2nd Level Spell Slots Known"] = 0
            player.notes["Wizard 3rd Level Spell Slots Known"] = 0
            player.notes["Wizard 4th Level Spell Slots Known"] = 0
            player.notes["Wizard 5th Level Spell Slots Known"] = 0
            player.notes["Wizard 6th Level Spell Slots Known"] = 0
            player.notes["Wizard 7th Level Spell Slots Known"] = 0
            player.notes["Wizard 8th Level Spell Slots Known"] = 0
            player.notes["Wizard 9th Level Spell Slots Known"] = 0
            player.notes["Learning Spells of 1st Level and Higher"] = "Each time you gain a Wizard level, you can add two wizard spells of your choice to your spellbook for free. Each of these spells must be of a level for which you have spell slots, as shown on the Wizard table. On your adventures, you might find other spells that you can add to your spellbook (see the “Your Spellbook” sidebar)."
            player.notes["Your Spellbook"] = "The spells that you add to your spellbook as you gain levels reflect the arcane research you conduct on your own, as well as intellectual breakthroughs you have had about the nature of the multiverse. You might find other spells during your adventures. You could discover a spell recorded on a scroll in an evil wizard's chest, for example, or in a dusty tome in an ancient library.\nCopying a Spell into the Book. When you find a wizard spell of 1st level or higher, you can add it to your spellbook if it is of a spell level you can prepare and if you can spare the time to decipher and copy it.\nCopying that spell into your spellbook involves reproducing the basic form of the spell, then deciphering the unique system of notation used by the wizard who wrote it. You must practice the spell until you understand the sounds or gestures required, then transcribe it into your spellbook using your own notation.\nFor each level of the spell, the process takes 2 hours and costs 50 gp. The cost represents material components you expend as you experiment with the spell to master it, as well as the fine inks you need to record it. Once you have spent this time and money, you can prepare the spell just like your other spells.\nReplacing the Book. You can copy a spell from your own spellbook into another book—for example, if you want to make a backup copy of your spellbook. This is just like copying a new spell into your spellbook, but faster and easier, since you understand your own notation and already know how to cast the spell. You need spend only 1 hour and 10 gp for each level of the copied spell.\nIf you lose your spellbook, you can use the same procedure to transcribe the spells that you have prepared into a new spellbook. Filling out the remainder of your spellbook requires you to find new spells to do so, as normal. For this reason, many wizards keep backup spellbooks in a safe place.\nThe Book's Appearance. Your spellbook is a unique compilation of spells, with its own decorative flourishes and margin player.notes. It might be a plain, functional leather volume that you received as a gift from your master, a finely bound gilt-edged tome you found in an ancient library, or even a loose collection of notes scrounged together after you lost your previous spellbook in a mishap."

import random

def dndchargen_class(param, player):
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
            "War Domain Cleric",
            ""
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
            "Wild Magic Origin Sorcerer",
            ""
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
            "Undying Patron Warlock",
            ""
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
            smclass = input("Do you wish to multi-class? Y/N ").strip().lower()
            if smclass in {"y", "ye", "yes"}:
                player.singlemulticlass = "Y"
            elif smclass in {"n", "no"}:
                player.singlemulticlass = "N"  
            if player.singlemulticlass == "N":
                player.classnum = 1
            if player.singlemulticlass == "Y":
                smwhile = False
                while not smwhile:
                    classnum = int(input(f"Given your player level of {player.level}, how many classes are you multiclassing into? "))
                    if classnum == 0:
                        print("You cannot have 0 classes, please try again.")
                        classnum = int(input(f"Given your player level of {player.level}, how many classes are you multiclassing into? "))
                    if classnum >= 1:
                        player.classnum = classnum
                        smwhile = True
            if player.singlemulticlass == "N":
                player.classnum = 1
        if player.level == 1:
            player.classnum = 1
        for cn in range(player.classnum):
            print("0 - Random")
            for idx, cl in enumerate(class_list, 1):
                print(f"{idx} - {cl}")
            cla = int(input("Class? "))
            if cla == 0:
                RandomClass = random.choice(class_list)
                RandomSubclass = random.choice(Classes[RandomClass])
                player.Class.append(RandomClass)
                class_list.remove(RandomClass)
                player.subclass.append(RandomSubclass)
            elif 1 <= cla <= len(class_list):
                chosen_class = class_list[cla - 1]  # Get the class name
                player.Class.append(chosen_class)
                class_list.remove(chosen_class)
                # Generate the subclass list for the chosen class
                subclass_list = Classes.get(chosen_class, [])
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
                elif 1 <= subc <= len(subclass_list):
                    subcl = subclass_list[subc - 1]
                    if subcl == "Beachball Patron Warlock":
                        Classes["Warlock"].remove("Beachball Patron Warlock")
                        WarRand = random.choice(Classes["Warlock"])
                        player.subclass.append(WarRand)
                        player.beachballflag = True
                    else:
                        player.subclass.append(subcl)                 
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
import random

def dndchargen_class(param, plLvl):
    Class = []
    subclass = []
    submulticlass = ""
    BeachballFlag = False
    Arti = ["Alchemist Specialist Artificer", "Armorer Specialist Artificer", "Artilierist Specialist Artificer", "Battle Smith Specialist Artificer", ""]
    Barb = ["Path of the Ancestral Guardian Barbarian", "Path of the Battlerager Barbarian", "Path of the Beast Barbarian", "Path of the Berserker Barbarian", "Path of the Giant Barbarian", "Path of the Juggernaut Barbarian", "Path of the Storm Herald Barbarian", "Path of the Totem Warrior Barbarian", "Path of the Zealot Barbarian", "Path of the Wild Magic Barbarian", ""]
    Bar = ["College of Creation Bard", "College of Eloquence Bard", "College of Glamour Bard", "College of Lore Bard", "College of the Road Bard", "College of Spirits Bard", "College of Swords Bard", "College of Tragedy Bard", "College of Valor Bard", "College of Whispers Bards", ""]
    Cle = ["Arcana Domain Cleric", "Blood Domain Cleric", "Commmunity Domain Cleric", "Death Domain Cleric", 'Forge Domain Cleric', "Grave Domain Cleric", "Knowledge Domain Cleric", "Life Domain Cleric", "Light Domain Cleric", "Moon Domain Cleric", "Nature Domain Cleric", "Night Domain Cleric", "Order Domain Cleric", "Peace Domain Cleric", "Tempest Domain Cleric", "Trickery Domain Cleric", "Twilight Domain Cleric", "War Domain Cleric", ""]
    Dru = ["Circle of the Blighted Druid", "Circle of Dreams Druid", "Circle of the Land Druid", "Circle of the Moon Druid", "Circle of the Sheppard Druid", "Circle of Spores Druid", "Circle of the Stars Druid", "Circle of Wildfire Druid", ""]
    Fig = ["Arcane Archer Archetype Fighter", "Battle Master Archetype Fighter", "Cavalier Archetype Fighter", "Champion Archetype Fighter", "Echo Knight Archetype Fighter", "Eldrich Knight Archetype Fighter", "Psi Warrior Archetype Fighter", "Purple Dragon Knight Archetype Fighter", "Rune Knight Archetype Fighter", "Samurai Archetype Fighter", "Scofflaw Archetype Fighter", ""]
    Mon = ["Way of the Ascendant Dragon Monk", "Way of the Astral Self Monk", "Way of the Cobalt Soul Monk", "Way of the Drunken Master Monk", "Way of the Four Elements Monk", "Way of the Kensei Monk", "Way of the Long Death Monk", "Way of Mercy Monk", "Way of the Open Hand Monk", "Way of the Shadow Monk", "Way of the Sun Soul Monk", ""]
    Pal = ["Oath of the Ancients Paladin", "Oath of Conquest Paladin", "Oath of the Crown Paladin", "Oath of Devotion Paladin", "Oath of Glory Paladin", "Oath of the Open Sea Paladin", "Oath of Redemption Paladin", "Oath of the Watchers Paladin", "Oath of Vengeance Paladin", "Oathbreaker Paladin", ""]
    Ran = ["Beast Master Archetype Ranger", "Drakewarden Ranger", "Fey Wanderer Archetype Ranger", "Gloom Stalker Archetype Ranger", "Horizon Walker Archetype Ranger", "Hunter Archetype Ranger", "Monster Slayer Archetype Ranger", "Swarmkeeper Archetype Ranger", ""]
    Rog = ["Arcane Trickster Archetype Rogue", "Assassin Archetype Rogue", "Inquisitive Archetype Rogue", "Mastermind Archetype Rogue", "Phantom Archetype Rogue", "Scout Archetype Rogue", "Soulknife Archetype Rogue", "Swashbuckler Archetype Rogue", "Thief Archetype Rogue", ""]
    Sor = ["Aberrant Mind Origin Sorcerer", "Clockwork Soul Origin Sorcerer", "Divine Soul Origin Sorcerer", "Draconic Bloodline Origin Sorcerer", "Lunar Magic Origin Sorcerer", "Runechild Origin Sorcerer", "Shadow Origin Sorcerer", "Storm Origin Sorcerer", "Wild Magic Origin Sorcerer", ""]
    War = ["Archfey Patron Warlock", "Beachball Patron Warlock", "Celestial Patron Warlock", "The Fathomless Patron Warlock", "Fiend Patron Warlock", "The Genie Patron Warlock", "Great Old One Patron Warlock", "Hexblade Patron Warlock", "Undead Patron Warlock", "Undying Patron Warlock", ""]    
    Wiz = ["Abjuration Arcane Tradition Wizard", "Bladesinging Arcane Tradition Wizard", "Blood Magic Arcane Tradition Wizard", "Chronurgy Magic Wizard", "Conjuration Arcane Tradition Wizard", "Divination Arcane Tradition Wizard", "Enchantment Arcane Tradition Wizard", "Evocation Arcane Tradition Wizard", "Graviturgy Magic Wizard", "Illusion Arcane Tradition Wizard", "Necromancy Arcane Tradition Wizard", "Order of Scribes Arcane Tradition Wizard", "Transmutation Arcane Tradition Wizard", "War Magic Arcane Tradition Wizard", ""]
    Clas = ["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    if param == "Y":
        if plLvl > 1:
            smclass = input("Do you wish to multi-class? Y/N ")
            if smclass == "Y":
                submulticlass = "Y"
            if smclass == "y":
                submulticlass = "Y"
            if smclass == "Yes":
                submulticlass = "Y"
            if smclass == "yes":
                submulticlass = "Y"
            if smclass == "Ye":
                submulticlass = "Y"
            if smclass == "ye":
                submulticlass = "Y"
            if smclass == "N":
                submulticlass = "N"
            if smclass == "n":
                submulticlass = "N"
            if smclass == "No":
                submulticlass = "N"
            if smclass == "no":
                submulticlass = "N"    
            if submulticlass == "N":
                classnum = 1
            if submulticlass == "Y":
                smwhile = False
                while not smwhile:
                    classnum = int(input(f"Given your player level of {plLvl}, how many classes are you multiclassing into? "))
                    if classnum == 0:
                        print("You cannot have 0 classes, please try again.")
                        classnum = int(input(f"Given your player level of {plLvl}, how many classes are you multiclassing into? "))
                    if classnum >= 1:
                        smwhile = True
            if submulticlass == "N":
                classnum = 1
        if plLvl == 1:
            classnum = 1
        for cn in range(classnum):
            print("0 - Random")
            print("1 - Artificer")
            print("2 - Barbarian")
            print("3 - Bard")
            print("4 - Cleric")
            print("5 - Druid")
            print("6 - Fighter")
            print("7 - Monk")
            print("8 - Paladin")
            print("9 - Ranger")
            print("10 - Rogue")
            print("11 - Sorcerer")
            print("12 - Warlock")
            print("13 - Wizard")
            cla = input("Class? ")
            if cla == "1":
                Class.append("Artificer")
                print("0 - Random")
                print("1 - Alchemist Specialist Artificer")
                print("2 - Armorer Specialist Artificer")
                print("3 - Artilierist Specialist Artificer")
                print("4 - Battle Smith Specialist Artificer")
                print("5 - Unsure/Leave Blank")
                subc = int(input("Which subclass would you like? ")) 
                if subc == 1:
                    subclass.append("Alchemist Specialist Artificer")
                if subc == 2:
                    subclass.append("Armorer Specialist Artificer")
                if subc == 3:
                    subclass.append("Artilierist Specialist Artificer")
                if subc == 4:
                    subclass.append("Battle Smith Specialist Artificer")
                if subc == 5:
                    subclass.append("")
                if subc == 0:
                    subclass.append(random.choice(Arti))
            if cla == "2":
                Class.append("Barbarian")
                print("0 - Random")
                print("1 - Path of the Ancestral Guardian Barbarian")
                print("2 - Path of the Battlerager Barbarian")
                print("3 - Path of the Beast Barbarian")
                print("4 - Path of the Berserker Barbarian")
                print("5 - Path of the Giant Barbarian")
                print("6 - Path of the Juggernaut Barbarian")
                print("7 - Path of the Storm Herald Barbarian")
                print("8 - Path of the Totem Warrior Barbarian")
                print("9 - Path of the Wild Magic Barbarian")
                print("10 - Path of the Zealot Barbarian")
                print("11 - Unsure/Leave Blank")
                subc = int(input("Which subclass would you like? ")) 
                if subc == 1:
                    subclass.append("Path of the Ancestral Guardian Barbarian")
                if subc == 2:
                    subclass.append("Path of the Battlerager Barbarian")
                if subc == 3:
                    subclass.append("Path of the Beast Barbarian")
                if subc == 4:
                    subclass.append("Path of the Berserker Barbarian")   
                if subc == 5:
                    subclass.append("Path of the Giant Barbarian") 
                if subc == 6:
                    subclass.append("Path of the Juggernaut Barbarian") 
                if subc == 7:
                    subclass.append("Path of the Storm Herald Barbarian") 
                if subc == 8:
                    subclass.append("Path of the Totem Warrior Barbarian")
                if subc == 9:
                    subclass.append("Path of the Wild Magic Barbarian")
                if subc == 10:
                    subclass.append("Path of the Zealot Barbarian")
                if subc == 11:
                    subclass.append("")
                if subc == 0:
                    subclass.append(random.choice(Barb))
            if cla == "3":
                Class.append("Bard")
                print("0 - Random")
                print("1 - College of Creation Bard")
                print("2 - College of Eloquence Bard")
                print("3 - College of Glamour Bard")
                print("4 - College of Lore Bard")
                print("5 - College of the Road Bard")
                print("6 - College of Spirits Bard")
                print("7 - College of Swords Bard")
                print("8 - College of Tragedy Bard")
                print("9 - College of Valor Bard")
                print("10 - College of Whispers Bard")
                print("11 - Unsure/Leave Blank")
                subc = int(input("Which subclass would you like? ")) 
                if subc == 1:
                    subclass.append("College of Creation Bard")
                if subc == 2:
                    subclass.append("College of Eloquence Bard")
                if subc == 3:
                    subclass.append("College of Glamour Bard")
                if subc == 4:
                    subclass.append("College of Lore Bard")
                if subc == 5:
                    subclass.append("College of the Road Bard")
                if subc == 6:
                    subclass.append("College of Spirits Bard")               
                if subc == 7:
                    subclass.append("College of Swords Bard")
                if subc == 8:
                    subclass.append("College of Tragedy Bard")
                if subc == 9:
                    subclass.append("College of Valor Bard")
                if subc == 10:
                    subclass.append("College of Whispers Bard")                                                                                                                             
                if subc == 11:
                    subclass.append("")
                if subc == 0:
                    subclass.append(random.choice(Bar))
            if cla == "4":
                Class.append("Cleric")
                print("0 - Random")
                print("1 - Arcana Domain Cleric")
                print("2 - Blood Domain Cleric")
                print("3 - Commmunity Domain Cleric")
                print("4 - Death Domain Cleric")
                print("5 - Forge Domain Cleric")
                print("6 - Grave Domain Cleric")
                print("7 - Knowledge Domain Cleric")
                print("8 - Life Domain Cleric")
                print("9 - Light Domain Cleric")
                print("10 - Moon Domain Cleric")
                print("11 - Nature Domain Cleric")
                print("12 - Night Domain Cleric")
                print("13 - Order Domain Cleric")
                print("14 - Peace Domain Cleric")
                print("15 - Tempest Domain Cleric")
                print("16 - Trickery Domain Cleric")
                print("17 - Twilight Domain Cleric")
                print("18 - War Domain Cleric")
                print("19 - Unsure/Leave Blank")
                subc = int(input("Which subclass would you like? ")) 
                if subc == 1:
                    subclass.append("Arcana Domain Cleric")
                if subc == 2:
                    subclass.append("Blood Domain Cleric")
                if subc == 3:
                    subclass.append("Commmunity Domain Cleric")
                if subc == 4:
                    subclass.append("Death Domain Cleric")
                if subc == 5:
                    subclass.append("Forge Domain Cleric")
                if subc == 6:
                    subclass.append("Grave Domain Cleric")
                if subc == 7:
                    subclass.append("Knowledge Domain Cleric")
                if subc == 8:
                    subclass.append("Life Domain Cleric")
                if subc == 9:
                    subclass.append("Light Domain Cleric")
                if subc == 10:
                    subclass.append("Moon Domain Cleric")
                if subc == 11:
                    subclass.append("Nature Domain Cleric")
                if subc == 12:
                    subclass.append("Night Domain Cleric")
                if subc == 13:
                    subclass.append("Order Domain Cleric")
                if subc == 14:
                    subclass.append("Peace Domain Cleric")
                if subc == 15:
                    subclass.append("Tempest Domain Cleric") 
                if subc == 16:
                    subclass.append("Trickery Domain Cleric") 
                if subc == 17:
                    subclass.append("Twilight Domain Cleric")
                if subc == 18:
                    subclass.append("War Domain Cleric")                 
                if subc == 19:
                    subclass.append("")
                if subc == 0:
                    subclass.append(random.choice(Cle))                          
            if cla == "5":
                Class.append("Druid")
                print("0 - Random")
                print("1 - Circle of the Blighted Druid")
                print("2 - Circle of Dreams Druid")
                print("3 - Circle of the Land Druid")
                print("4 - Circle of the Moon Druid")
                print("5 - Circle of the Sheppard Druid")
                print("6 - Circle of Spores Druid")
                print("7 - Circle of the Stars Druid")
                print("8 - Circle of Wildfire Druid")
                print("9 - Unsure/Leave Blank")
                subc = int(input("Which subclass would you like? ")) 
                if subc == 1:
                    subclass.append("Circle of the Blighted Druid")
                if subc == 2:
                    subclass.append("Circle of Dreams Druid")
                if subc == 3:
                    subclass.append("Circle of the Land Druid")
                if subc == 4:
                    subclass.append("Circle of the Moon Druid")    
                if subc == 5:
                    subclass.append("Circle of the Sheppard Druid")
                if subc == 6:
                    subclass.append("Circle of Spores Druid")
                if subc == 7:
                    subclass.append("Circle of the Stars Druid")   
                if subc == 8:
                    subclass.append("Circle of Wildfire Druid")
                if subc == 9:
                    subclass.append("")                                                             
                if subc == 0:
                    subclass.append(random.choice(Dru))                        
            if cla == "6":
                Class.append("Fighter")
                print("0 - Random")
                print("1 - Arcane Archer Archetype Fighter")
                print("2 - Battle Master Archetype Fighter")
                print("3 - Cavalier Archetype Fighter")
                print("4 - Champion Archetype Fighter")
                print("5 - Echo Knight Archetype Fighter")
                print("6 - Eldrich Knight Archetype Fighter")
                print("7 - Psi Warrior Archetype Fighter")
                print("8 - Purple Dragon Knight Archetype Fighter")
                print("9 - Rune Knight Archetype Fighter")
                print("10 - Samurai Archetype Fighter")
                print("11 - Scofflaw Archetype Fighter")
                print("12 - Unsure/Leave Blank")
                subc = int(input("Which subclass would you like? ")) 
                if subc == 1:
                    subclass.append("Arcane Archer Archetype Fighter")
                if subc == 2:
                    subclass.append("Battle Master Archetype Fighter")
                if subc == 3:
                    subclass.append("Cavalier Archetype Fighter")
                if subc == 4:
                    subclass.append("Champion Archetype Fighter")     
                if subc == 5:
                    subclass.append("Echo Knight Archetype Fighter")
                if subc == 6:
                    subclass.append("Eldrich Knight Archetype Fighter")
                if subc == 7:
                    subclass.append("Psi Warrior Archetype Fighter")   
                if subc == 8:
                    subclass.append("Purple Dragon Knight Archetype Fighter")    
                if subc == 9:
                    subclass.append("Rune Knight Archetype Fighter")    
                if subc == 10:
                    subclass.append("Samurai Archetype Fighter")    
                if subc == 11:
                    subclass.append("Scofflaw Archetype Fighter")          
                if subc == 12:
                    subclass.append("")
                if subc == 0:
                    subclass.append(random.choice(Fig))                           
            if cla == "7":
                Class.append("Monk")
                print("0 - Random")
                print("1 - Way of the Ascendant Dragon Monk")
                print("2 - Way of the Astral Self Monk")
                print("3 - Way of the Cobalt Soul Monk")
                print("4 - Way of the Drunken Master Monk")
                print("5 - Way of the Four Elements Monk")
                print("6 - Way of the Kensei Monk")
                print("7 - Way of the Long Death Monk")
                print("8 - Way of Mercy Monk")
                print("9 - Way of the Open Hand Monk")
                print("10 - Way of the Shadow Monk")
                print("11 - Way of the Sun Soul Monk")
                print("12 - Unsure/Leave Blank")
                subc = int(input("Which subclass would you like? ")) 
                if subc == 1:
                    subclass.append("Way of the Ascendant Dragon Monk")
                if subc == 2:
                    subclass.append("Way of the Astral Self Monk")
                if subc == 3:
                    subclass.append("Way of the Cobalt Soul Monk")
                if subc == 4:
                    subclass.append("Way of the Drunken Master Monk")     
                if subc == 5:
                    subclass.append("Way of the Four Elements Monk")
                if subc == 6:
                    subclass.append("Way of the Kensei Monk")
                if subc == 7:
                    subclass.append("Way of the Long Death Monk")   
                if subc == 8:
                    subclass.append("Way of Mercy Monk")    
                if subc == 9:
                    subclass.append("Way of the Open Hand Monk")
                if subc == 10:
                    subclass.append("Way of the Shadow Monk")    
                if subc == 11:
                    subclass.append("Way of the Sun Soul Monk")                  
                if subc == 12:
                    subclass.append("")
                if subc == 0:
                    subclass.append(random.choice(Mon))                
            if cla == "8":
                Class.append("Paladin")
                print("0 - Random")
                print("1 - Oath of the Ancients Paladin")
                print("2 - Oath of Conquest Paladin")
                print("3 - Oath of the Crown Paladin")
                print("4 - Oath of Devotion Paladin")
                print("5 - Oath of Glory Paladin")
                print("6 - Oath of the Open Sea Paladin")
                print("7 - Oath of Redemption Paladin")
                print("8 - Oath of the Watchers Paladin")
                print("9 - Oath of Vengeance Paladin")
                print("10 - Oathbreaker Paladin")
                print("11 - Unsure/Leave Blank")
                subc = int(input("Which subclass would you like? ")) 
                if subc == 1:
                    subclass.append("Oath of the Ancients Paladin")
                if subc == 2:
                    subclass.append("Oath of Conquest Paladin")
                if subc == 3:
                    subclass.append("Oath of the Crown Paladin")
                if subc == 4:
                    subclass.append("Oath of Devotion Paladin")   
                if subc == 5:
                    subclass.append("Oath of Glory Paladin")
                if subc == 6:
                    subclass.append("Oath of the Open Sea Paladin")
                if subc == 7:
                    subclass.append("Oath of Redemption Paladin")
                if subc == 8:
                    subclass.append("Oath of the Watchers Paladin")    
                if subc == 9:
                    subclass.append("Oath of Vengeance Paladin")    
                if subc == 10:
                    subclass.append("Oathbreaker Paladin")
                if subc == 11:
                    subclass.append("")
                if subc == 0:
                    subclass.append(random.choice(Pal))                            
            if cla == "9":
                Class.append("Ranger")
                print("0 - Random")
                print("1 - Beast Master Archetype Ranger")
                print("2 - Drakewarden Ranger")
                print("3 - Fey Wanderer Archetype Ranger")
                print("4 - Gloom Stalker Archetype Ranger")
                print("5 - Horizon Walker Archetype Ranger")
                print("6 - Hunter Archetype Ranger")
                print("7 - Monster Slayer Archetype Ranger")
                print("8 - Shooting Star Archetype Ranger")
                print("9 - Swarmkeeper Archetype Ranger")
                print("10 - Unsure/Leave Blank")
                subc = int(input("Which subclass would you like? ")) 
                if subc == 1:
                    subclass.append("Beast Master Archetype Ranger")
                if subc == 2:
                    subclass.append("Drakewarden Ranger")
                if subc == 3:
                    subclass.append("Fey Wanderer Archetype Ranger")
                if subc == 4:
                    subclass.append("Gloom Stalker Archetype Ranger")     
                if subc == 5:
                    subclass.append("Horizon Walker Archetype Ranger")
                if subc == 6:
                    subclass.append("Hunter Archetype Ranger")
                if subc == 7:
                    subclass.append("Monster Slayer Archetype Ranger")     
                if subc == 8:
                    subclass.append("Swarmkeeper Archetype Ranger")  
                if subc == 9:
                    subclass.append("")        
                if subc == 0:
                    subclass.append(random.choice(Ran))                          
            if cla == "10":
                Class.append("Rogue")
                print("0 - Random")
                print("1 - Arcane Trickster Archetype Rogue")
                print("2 - Assassin Archetype Rogue")
                print("3 - Inquisitive Archetype Rogue")
                print("4 - Mastermind Archetype Rogue")
                print("5 - Phantom Archetype Rogue")
                print("6 - Scout Archetype Rogue")
                print("7 - Soulknife Archetype Rogue")
                print("8 - Swashbuckler Archetype Rogue")
                print("9 - Thief Archetype Rogue")
                print("10 - Unsure/Leave Blank")
                subc = int(input("Which subclass would you like? ")) 
                if subc == 1:
                    subclass.append("Arcane Trickster Archetype Rogue")
                if subc == 2:
                    subclass.append("Assassin Archetype Rogue")
                if subc == 3:
                    subclass.append("Inquisitive Archetype Rogue")
                if subc == 4:
                    subclass.append("Mastermind Archetype Rogue")     
                if subc == 5:
                    subclass.append("Phantom Archetype Rogue")
                if subc == 6:
                    subclass.append("Scout Archetype Rogue")   
                if subc == 7:
                    subclass.append("Soulknife Archetype Rogue")    
                if subc == 8:
                    subclass.append("Swashbuckler Archetype Rogue")    
                if subc == 9:
                    subclass.append("Thief Archetype Rogue")             
                if subc == 10:
                    subclass.append("")
                if subc == 0:
                    subclass.append(random.choice(Rog))                    
            if cla == "11":
                Class.append("Sorcerer")
                print("0 - Random")
                print("1 - Aberrant Mind Origin Sorcerer")
                print("2 - Clockwork Soul Origin Sorcerer")
                print("3 - Divine Soul Origin Sorcerer")
                print("4 - Draconic Bloodline Origin Sorcerer")
                print("5 - Lunar Magic Origin Sorcerer")
                print("6 - Runechild Origin Sorcerer")
                print("7 - Shadow Origin Sorcerer")
                print("8 - Storm Origin Sorcerer")
                print("9 - Wild Magic Origin Sorcerer")
                print("10 - Unsure/Leave Blank")
                subc = int(input("Which subclass would you like? ")) 
                if subc == 1:
                    subclass.append("Aberrant Mind Origin Sorcerer")
                if subc == 2:
                    subclass.append("Clockwork Soul Origin Sorcerer")
                if subc == 3:
                    subclass.append("Divine Soul Origin Sorcerer")
                if subc == 4:
                    subclass.append("Draconic Bloodline Origin Sorcerer")     
                if subc == 5:
                    subclass.append("Lunar Magic Origin Sorcerer")
                if subc == 6:
                    subclass.append("Runechild Origin Sorcerer")       
                if subc == 7:
                    subclass.append("Shadow Origin Sorcerer")       
                if subc == 8:
                    subclass.append("Storm Origin Sorcerer")    
                if subc == 9:
                    subclass.append("Wild Magic Origin Sorcerer")            
                if subc == 10:
                    subclass.append("")
                if subc == 0:
                    subclass.append(random.choice(Sor))                       
            if cla == "12":
                Class.append("Warlock")
                print("0 - Random")
                print("1 - Archfey Patron Warlock")
                print("2 - Celestial Patron Warlock")
                print("3 - The Fathomless Patron Warlock")
                print("4 - Fiend Patron Warlock")
                print("5 - The Genie Patron Warlock")
                print("6 - Great Old One Patron Warlock")
                print("7 - Hexblade Patron Warlock")
                print("8 - Undead Patron Warlock")
                print("9 - Undying Patron Warlock")
                print("10 - Beachball Patron Warlock")
                print("11 - Unsure/Leave Blank")
                subc = int(input("Which subclass would you like? ")) 
                if subc == 1:
                    subclass.append("Archfey Patron Warlock")
                if subc == 2:
                    subclass.append("Celestial Patron Warlock")
                if subc == 3:
                    subclass.append("The Fathomless Patron Warlock")     
                if subc == 4:
                    subclass.append("Fiend Patron Warlock")
                if subc == 5:
                    subclass.append("The Genie Patron Warlock")
                if subc == 6:
                    subclass.append("Great Old One Patron Warlock")  
                if subc == 7:
                    subclass.append("Hexblade Patron Warlock")
                if subc == 8:
                    subclass.append("Undead Patron Warlock")   
                if subc == 9:
                    subclass.append("Undying Patron Warlock")                                                                                                    
                if subc == 10:
                    War.remove("Beachball Patron Warlock")
                    subclass.append(random.choice(War))
                    BeachballFlag = True
                if subc == 11:
                    subclass.append("")
                if subc == 0:
                    WarRand = random.choice(War)
                    if WarRand == "Beachball Patron Warlock":
                        War.remove("Beachball Patron Warlock")
                        WarRand = random.choice(War)
                        subclass.append(WarRand)
                        BeachballFlag = True
            if cla == "13":
                Class.append("Wizard")
                print("0 - Random")
                print("1 - Abjuration Arcane Tradition Wizard")
                print("2 - Bladesinging Arcane Tradition Wizard")
                print("3 - Blood Magic Arcane Tradition Wizard")
                print("4 - Chronurgy Magic Arcane Tradition Wizard")
                print("5 - Conjuration Arcane Tradition Wizard")
                print("6 - Divination Arcane Tradition Wizard")
                print("7 - Enchantment Arcane Tradition Wizard")
                print("8 - Evocation Arcane Tradition Wizard")
                print("9 - Graviturgy Magic Arcane Tradition Wizard")
                print("10 - Illusion Arcane Tradition Wizard")
                print("11 - Necromancy Arcane Tradition Wizard")
                print("12 - Order of Scribes Arcane Tradition Wizard")
                print("13 - Transmutation Arcane Tradition Wizard")
                print("14 - War Magic Arcane Tradition Wizard")
                print("15 - Unsure/Leave Blank")
                subc = int(input("Which subclass would you like? ")) 
                if subc == 1:
                    subclass.append("Abjuration Arcane Tradition Wizard")
                if subc == 2:
                    subclass.append("Bladesinging Arcane Tradition Wizard")
                if subc == 3:
                    subclass.append("Blood Magic Arcane Tradition Wizard")
                if subc == 4:
                    subclass.append("Chronurgy Magic Arcane Tradition Wizard")     
                if subc == 5:
                    subclass.append("Conjuration Arcane Tradition Wizard")
                if subc == 6:
                    subclass.append("Divination Arcane Tradition Wizard")
                if subc == 7:
                    subclass.append("Enchantment Arcane Tradition Wizard")
                if subc == 8:
                    subclass.append("Evocation Arcane Tradition Wizard")  
                if subc == 9:
                    subclass.append("Graviturgy Magic Arcane Tradition Wizard")     
                if subc == 10:
                    subclass.append("Illusion Arcane Tradition Wizard")
                if subc == 11:
                    subclass.append("Necromancy Arcane Tradition Wizard")     
                if subc == 12:
                    subclass.append("Order of Scribes Arcane Tradition Wizard")                                                                 
                if subc == 13:
                    subclass.append("Transmutation Arcane Tradition Wizard")
                if subc == 14:
                    subclass.append("War Magic Arcane Tradition Wizard")                                                     
                if subc == 15:
                    subclass.append("")
                if subc == 0:
                    subclass.append(random.choice(Wiz))            
            if cla == "0":
                ClassRandomWhile = False
                while not ClassRandomWhile:
                    try:
                        ClassRandom = random.choice(Clas)
                        Clas.remove(ClassRandom)
                        ClassRandomWhile = True
                    except IndexError:    
                        pass                       
                Class.append(ClassRandom) 
                if ClassRandom == "Artificer":
                    subclass.append(random.choice(Arti)) 
                if ClassRandom == "Barbarian":
                    subclass.append(random.choice(Barb))
                if ClassRandom == "Bard":
                    subclass.append(random.choice(Bar))
                if ClassRandom == "Cleric":
                    subclass.append(random.choice(Cle))
                if ClassRandom == "Druid":
                    subclass.append(random.choice(Dru))
                if ClassRandom == "Fighter":
                    subclass.append(random.choice(Fig))
                if ClassRandom == "Monk":
                    subclass.append(random.choice(Mon))
                if ClassRandom == "Paladin":
                    subclass.append(random.choice(Pal))
                if ClassRandom == "Ranger":
                    subclass.append(random.choice(Ran))
                if ClassRandom == "Rogue":
                    subclass.append(random.choice(Rog))
                if ClassRandom == "Sorcerer":
                    subclass.append(random.choice(Sor))
                if ClassRandom == "Warlock":
                    WarRand = random.choice(War)
                    if WarRand == "Beachball Patron Warlock":
                        War.remove("Beachball Patron Warlock")
                        WarRand = random.choice(War)
                        subclass.append(WarRand)
                        BeachballFlag = True
                if ClassRandom == "Wizard":
                    subclass.append(random.choice(Wiz))
    if param == "N":
        ClassRand = random.choice(Clas)
        Class.append(ClassRand)
        if ClassRand == "Artificer":
            subclass.append(random.choice(Arti)) 
        if ClassRand == "Barbarian":
            subclass.append(random.choice(Barb))
        if ClassRand == "Bard":
            subclass.append(random.choice(Bar))
        if ClassRand == "Cleric":
            subclass.append(random.choice(Cle))
        if ClassRand == "Druid":
            subclass.append(random.choice(Dru))
        if ClassRand == "Fighter":
            subclass.append(random.choice(Fig))
        if ClassRand == "Monk":
            subclass.append(random.choice(Mon))
        if ClassRand == "Paladin":
            subclass.append(random.choice(Pal)) 
        if ClassRand == "Ranger":
            subclass.append(random.choice(Ran))
        if ClassRand == "Rogue":
            subclass.append(random.choice(Rog))
        if ClassRand == "Sorcerer":
            subclass.append(random.choice(Sor))
        if ClassRand == "Warlock":
            WarRand = random.choice(War)
            if WarRand == "Beachball Patron Warlock":
                War.remove("Beachball Patron Warlock")
                WarRand = random.choice(War)
                subclass.append(WarRand)
                BeachballFlag = True
        if ClassRand == "Wizard":
            subclass.append(random.choice(Wiz))      
    return Class, subclass, submulticlass, BeachballFlag

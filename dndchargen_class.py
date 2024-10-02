import random

def classchoice(param):
    Arti = ["Alchemist Speciliast Artificer", "Armorer Speciliast Artificer", "Artilierist Speciliast Artificer", "Battle Smith Speciliast Artificer"]
    Artificer = random.choice (Arti)
    Barb = ["Path of the Ancestral Guardian Barbarian", "Path of the Battlerager Barbarian", "Path of the Beast Barbarian", "Path of the Berserker Barbarian", "Path of the Giant Barbarian", "Path of the Juggernaut Barbarian", "Path of the Storm Herald Barbarian", "Path of the Totem Warrior Barbarian", "Path of the Zealot Barbarian", "Path of the Wild Magic Barbarian"]
    Barbarian = random.choice(Barb)
    Bar = ["College of Creation Bard", "College of Eloquence Bard", "College of Glamour Bard", "College of Lore Bard", "College of the Road Bard", "College of Satire Bard", "College of Spirits Bard", "College of Swords Bard", "College of Tragedy Bard", "College of Valor Bard", "College of Whispers Bards"]
    Bard = random.choice(Bar)
    Cle = ["Arcana Domain Cleric", "Blood Domain Cleric", "Commmunity Domain Cleric", "Death Domain Cleric", 'Forge Domain Cleric', "Grave Domain Cleric", "Knowledge Domain Cleric", "Life Domain Cleric", "Light Domain Cleric", "Moon Domain Cleric", "Nature Domain Cleric", "Night Domain Cleric", "Order Domain Cleric", "Peace Domain Cleric", "Tempest Domain Cleric", "Trickery Domain Cleric", "Twilight Domain Cleric", "War Domain Cleric", "Zeal Domain Cleric"]
    Cleric = random.choice(Cle)
    Dru = ["Circle of the Blighted Druid", "Circle of Dreams Druid", "Circle of the Land Druid", "Circle of the Moon Druid", "Circle of the Sheppard Druid", "Circle of Spores Druid", "Circle of the Stars Druid", "Circle of Wildfire Druid"]
    Druid = random.choice(Dru)
    Fig = ["Arcane Archer Archetype Fighter", "Battle Master Archetype Fighter", "Cavalier Archetype Fighter", "Champion Archetype Fighter", "Echo Knight Archetype Fighter", "Eldrich Knight Archetype Fighter", "Psi Warrior Archetype Fighter", "Purple Dragon Knight Archetype Fighter", "Rune Knight Archetype Fighter", "Samurai Archetype Fighter", "Scofflaw Archetype Fighter"]
    Fighter = random.choice(Fig)
    Mon = ["Way of the Ascendant Dragon Monk", "Way of the Astral Self Monk", "Way of the Cobalt Soul Monk", "Way of the Drunken Master Monk", "Way of the Four Elements Monk", "Way of the Kensei Monk", "Way of the Long Death Monk", "Way of Mercy Monk", "Way of the Open Hand Monk", "Way of the Shadow Monk", "Way of the Sun Soul Monk"]
    Monk = random.choice(Mon)
    Pal= ["Oath of the Ancients Paladin", "Oath of Conquest Paladin", "Oath of the Crown Paladin", "Oath of Devotion Paladin", "Oath of Glory Paladin", "Oath of the Open Sea Paladin", "Oath of Redemption Paladin", "Oath of the Watchers Paladin", "Oath of Vengeance Paladin", "Oathbreaker Paladin"]
    Paladin = random.choice(Pal)
    Ran = ["Beast Master Archetype Ranger", "Drakewarden Ranger", "Fey Wanderer Archetype Ranger", "Gloom Stalker Archetype Ranger", "Horizon Walker Archetype Ranger", "Hunter Archetype Ranger", "Monster Slayer Archetype Ranger", "Shooting Star Archetype Ranger", "Swarmkeeper Archetype Ranger"]
    Ranger = random.choice(Ran)
    Rog = ["Arcane Trickster Archetype Rogue", "Assassin Archetype Rogue", "Inquisitive Archetype Rogue", "Mastermind Archetype Rogue", "Mountebank Archetype Rogue", "Phantom Archetype Rogue", "Scout Archetype Rogue", "Soulknife Archetype Rogue", "Swashbuckler Archetype Rogue", "Thief Archetype Rogue"]
    Rogue = random.choice(Rog)
    Sor = ["Aberrant Mind Origin Sorcerer", "Clockwork Soul Origin Sorcerer", "Divine Soul Origin Sorcerer", "Draconic Bloodline Origin Sorcerer", "Lunar Magic Origin Sorcerer", "Phoenix Origin Sorcerer", "Runechild Origin Sorcerer", "Sea Origin Sorcerer", "Shadow Origin Sorcerer", "Stone Origin Sorcerer", "Storm Origin Sorcerer", "Wild Magic Origin Sorcerer"]
    Sorcerer = random.choice(Sor)
    War = ["Ancient Dragon Patron Warlock", "Archfey Patron Warlock", "Celestial Patron Warlock", "The Fathomless Patron Warlock", "Fiend Patron Warlock", "The Genie Patron Warlock", "Great Old One Patron Warlock", "Hexblade Patron Warlock", "Mysterious Feline Patron Warlock", "Queen of Spiders Patron Warlock", "Raven Queen Patron Warlock", "Serpent Patron Warlock", "Undead Patron Warlock", "Undying Patron Warlock"]    
    Warlock = random.choice(War)
    Wiz = ["Abjuration Arcane Tradition Wizard", "Bladesinging Arcane Tradition Wizard", "Blood Magic Arcane Tradition Wizard", "Chronurgy Magic Wizard", "Conjuration Arcane Tradition Wizard", "Divination Arcane Tradition Wizard", "Enchantment Arcane Tradition Wizard", "Evocation Arcane Tradition Wizard", "Graviturgy Magic Wizard", "Illusion Arcane Tradition Wizard", "Necromancy Arcane Tradition Wizard", "Order of Scribes Arcane Tradition Wizard", "Transmutation Arcane Tradition Wizard", "War Arcane Tradition Wizard"]
    Wizard = random.choice(Wiz)
    Clas = ["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    subclass = ""
    if param == "Y":
        print("0 - random")
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
        cla = input ("Class? ")
        if cla == "1":
            Class = "Artificer"
            print("0 - Random")
            print("1 - Alchemist Speciliast Artificer")
            print("2 - Armorer Speciliast Artificer")
            print("3 - Artilierist Speciliast Artificer")
            print("4 - Battle Smith Speciliast Artificer")
            subc = int(input("Which subclass would you like? ")) 
            if subc == 1:
                subclass = "Alchemist Speciliast Artificer"
            if subc == 2:
                subclass = "Armorer Speciliast Artificer"
            if subc == 3:
                subclass = "Artilierist Speciliast Artificer"
            if subc == 4:
                subclass = "Battle Smith Speciliast Artificer"
            if subc == 0:
                subclass = random.choice(Arti)
        if cla == "2":
            Class = "Barbarian"
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
            subc = int(input("Which subclass would you like? ")) 
            if subc == 1:
                subclass = "Path of the Ancestral Guardian Barbarian"
            if subc == 2:
                subclass = "Path of the Battlerager Barbarian"
            if subc == 3:
                subclass = "Path of the Beast Barbarian"
            if subc == 4:
                subclass = "Path of the Berserker Barbarian"   
            if subc == 5:
                subclass = "Path of the Giant Barbarian"   
            if subc == 6:
                subclass = "Path of the Juggernaut Barbarian"   
            if subc == 7:
                subclass = "Path of the Storm Herald Barbarian"   
            if subc == 8:
                subclass = "Path of the Totem Warrior Barbarian"  
            if subc == 9:
                subclass = "Path of the Wild Magic Barbarian" 
            if subc == 10:
                subclass = "Path of the Zealot Barbarian"
            if subc == 0:
                subclass == random.choice(Barb)                                                                                              
        if cla == "3":
            Class = "Bard"
            print("0 - Random")
            print("1 - College of Creation Bard")
            print("2 - College of Eloquence Bard")
            print("3 - College of Glamour Bard")
            print("4 - College of Lore Bard")
            print("5 - College of the Road Bard")
            print("6 - College of Satire Bard")
            print("7 - College of Spirits Bard")
            print("8 - College of Swords Bard")
            print("9 - College of Tragedy Bard")
            print("10 - College of Valor Bard")
            print("11 - College of Whispers Bard")
            subc = int(input("Which subclass would you like? ")) 
            if subc == 1:
                subclass = "College of Creation Bard"
            if subc == 2:
                subclass = "College of Eloquence Bard"
            if subc == 3:
                subclass = "College of Glamour Bard"
            if subc == 4:
                subclass = "College of Lore Bard"
            if subc == 5:
                subclass = "College of the Road Bard"
            if subc == 6:
                subclass = "College of Satire Bard"
            if subc == 7:
                subclass = "College of Spirits Bard"                 
            if subc == 8:
                subclass = "College of Swords Bard"
            if subc == 9:
                subclass = "College of Tragedy Bard" 
            if subc == 10:
                subclass = "College of Valor Bard" 
            if subc == 11:
                subclass = "College of Whispers Bard"                                                                                                                             
            if subc == 0:
                subclass = random.choice(Bar)
        if cla == "4":
            Class = "Cleric"
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
            print("19 - Zeal Domain Cleric")
            subc = int(input("Which subclass would you like? ")) 
            if subc == 1:
                subclass = "Arcana Domain Cleric"
            if subc == 2:
                subclass = "Blood Domain Cleric"
            if subc == 3:
                subclass = "Commmunity Domain Cleric"
            if subc == 4:
                subclass = "Death Domain Cleric"
            if subc == 5:
                subclass = "Forge Domain Cleric"
            if subc == 6:
                subclass = "Grave Domain Cleric"
            if subc == 7:
                subclass = "Knowledge Domain Cleric"
            if subc == 8:
                subclass = "Life Domain Cleric"
            if subc == 9:
                subclass = "Light Domain Cleric"
            if subc == 10:
                subclass = "Moon Domain Cleric"
            if subc == 11:
                subclass = "Nature Domain Cleric"
            if subc == 12:
                subclass = "Night Domain Cleric" 
            if subc == 13:
                subclass = "Order Domain Cleric" 
            if subc == 14:
                subclass = "Peace Domain Cleric" 
            if subc == 15:
                subclass = "Tempest Domain Cleric" 
            if subc == 16:
                subclass = "Trickery Domain Cleric" 
            if subc == 17:
                subclass = "Twilight Domain Cleric" 
            if subc == 18:
                subclass = "War Domain Cleric" 
            if subc == 19:
                subclass = "Zeal Domain Cleric"                                                                                                                                                                                                                                                   
            if subc == 0:
                subclass = random.choice(Cle)                          
        if cla == "5":
            Class = "Druid"
            print("0 - Random")
            print("1 - Circle of the Blighted Druid")
            print("2 - Circle of Dreams Druid")
            print("3 - Circle of the Land Druid")
            print("4 - Circle of the Moon Druid")
            print("5 - Circle of the Sheppard Druid")
            print("6 - Circle of Spores Druid")
            print("7 - Circle of the Stars Druid")
            print("8 - Circle of Wildfire Druid")
            subc = int(input("Which subclass would you like? ")) 
            if subc == 1:
                subclass = "Circle of the Blighted Druid"
            if subc == 2:
                subclass = "Circle of Dreams Druid"
            if subc == 3:
                subclass = "Circle of the Land Druid"
            if subc == 4:
                subclass = "Circle of the Moon Druid"     
            if subc == 5:
                subclass = "Circle of the Sheppard Druid"
            if subc == 6:
                subclass = "Circle of Spores Druid"
            if subc == 7:
                subclass = "Circle of the Stars Druid"   
            if subc == 8:
                subclass = "Circle of Wildfire Druid"                                                             
            if subc == 0:
                subclass = random.choice(Dru)                        
        if cla == "6":
            Class = "Fighter"
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
            subc = int(input("Which subclass would you like? ")) 
            if subc == 1:
                subclass = "Arcane Archer Archetype Fighter"
            if subc == 2:
                subclass = "Battle Master Archetype Fighter"
            if subc == 3:
                subclass = "Cavalier Archetype Fighter"
            if subc == 4:
                subclass = "Champion Archetype Fighter"     
            if subc == 5:
                subclass = "Echo Knight Archetype Fighter"
            if subc == 6:
                subclass = "Eldrich Knight Archetype Fighter"
            if subc == 7:
                subclass = "Psi Warrior Archetype Fighter"   
            if subc == 8:
                subclass = "Purple Dragon Knight Archetype Fighter"    
            if subc == 9:
                subclass = "Rune Knight Archetype Fighter"    
            if subc == 10:
                subclass = "Samurai Archetype Fighter"    
            if subc == 11:
                subclass = "Scofflaw Archetype Fighter"          
            if subc == 0:
                subclass = random.choice(Fig)                           
        if cla == "7":
            Class = "Monk"
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
            subc = int(input("Which subclass would you like? ")) 
            if subc == 1:
                subclass = "Way of the Ascendant Dragon Monk"
            if subc == 2:
                subclass = "Way of the Astral Self Monk"
            if subc == 3:
                subclass = "Way of the Cobalt Soul Monk"
            if subc == 4:
                subclass = "Way of the Drunken Master Monk"     
            if subc == 5:
                subclass = "Way of the Four Elements Monk"
            if subc == 6:
                subclass = "Way of the Kensei Monk"
            if subc == 7:
                subclass = "Way of the Long Death Monk"   
            if subc == 8:
                subclass = "Way of Mercy Monk"    
            if subc == 9:
                subclass = "Way of the Open Hand Monk"    
            if subc == 10:
                subclass = "Way of the Shadow Monk"    
            if subc == 11:
                subclass = "Way of the Sun Soul Monk"                  
            if subc == 0:
                subclass = random.choice(Mon)                
        if cla == "8":
            Class = "Paladin"
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
            subc = int(input("Which subclass would you like? ")) 
            if subc == 1:
                subclass = "Oath of the Ancients Paladin"
            if subc == 2:
                subclass = "Oath of Conquest Paladin"
            if subc == 3:
                subclass = "Oath of the Crown Paladin"
            if subc == 4:
                subclass = "Oath of Devotion Paladin"     
            if subc == 5:
                subclass = "Oath of Glory Paladin"
            if subc == 6:
                subclass = "Oath of the Open Sea Paladin"
            if subc == 7:
                subclass = "Oath of Redemption Paladin"   
            if subc == 8:
                subclass = "Oath of the Watchers Paladin"    
            if subc == 9:
                subclass = "Oath of Vengeance Paladin"    
            if subc == 10:
                subclass = "Oathbreaker Paladin"       
            if subc == 0:
                subclass = random.choice(Pal)                            
        if cla == "9":
            Class = "Ranger"
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
            subc = int(input("Which subclass would you like? ")) 
            if subc == 1:
                subclass = "Beast Master Archetype Ranger"
            if subc == 2:
                subclass = "Drakewarden Ranger"
            if subc == 3:
                subclass = "Fey Wanderer Archetype Ranger"
            if subc == 4:
                subclass = "Gloom Stalker Archetype Ranger"     
            if subc == 5:
                subclass = "Horizon Walker Archetype Ranger"
            if subc == 6:
                subclass = "Hunter Archetype Ranger"
            if subc == 7:
                subclass = "Monster Slayer Archetype Ranger"   
            if subc == 8:
                subclass = "Shooting Star Archetype Ranger"    
            if subc == 9:
                subclass = "Swarmkeeper Archetype Ranger"          
            if subc == 0:
                subclass = random.choice(Ran)                          
        if cla == "10":
            Class = "Rogue"
            print("0 - Random")
            print("1 - Arcane Trickster Archetype Rogue")
            print("2 - Assassin Archetype Rogue")
            print("3 - Inquisitive Archetype Rogue")
            print("4 - Mastermind Archetype Rogue")
            print("5 - Mountebank Archetype Rogue")
            print("6 - Phantom Archetype Rogue")
            print("7 - Scout Archetype Rogue")
            print("8 - Soulknife Archetype Rogue")
            print("9 - Swashbuckler Archetype Rogue")
            print("10 - Thief Archetype Rogue")
            subc = int(input("Which subclass would you like? ")) 
            if subc == 1:
                subclass = "Arcane Trickster Archetype Rogue"
            if subc == 2:
                subclass = "Assassin Archetype Rogue"
            if subc == 3:
                subclass = "Inquisitive Archetype Rogue"
            if subc == 4:
                subclass = "Mastermind Archetype Rogue"     
            if subc == 5:
                subclass = "Mountebank Archetype Rogue"
            if subc == 6:
                subclass = "Phantom Archetype Rogue"
            if subc == 7:
                subclass = "Scout Archetype Rogue"   
            if subc == 8:
                subclass = "Soulknife Archetype Rogue"    
            if subc == 9:
                subclass = "Swashbuckler Archetype Rogue"    
            if subc == 10:
                subclass = "Thief Archetype Rogue"             
            if subc == 0:
                subclass = random.choice(Rog)                    
        if cla == "11":
            Class = "Sorcerer"
            print("0 - Random")
            print("1 - Aberrant Mind Origin Sorcerer")
            print("2 - Clockwork Soul Origin Sorcerer")
            print("3 - Divine Soul Origin Sorcerer")
            print("4 - Draconic Bloodline Origin Sorcerer")
            print("5 - Lunar Magic Origin Sorcerer")
            print("6 - Phoenix Origin Sorcerer")
            print("7 - Runechild Origin Sorcerer")
            print("8 - Sea Origin Sorcerer")
            print("9 - Shadow Origin Sorcerer")
            print("10 - Stone Origin Sorcerer")
            print("11 - Storm Origin Sorcerer")
            print("12 - Wild Magic Origin Sorcerer")
            subc = int(input("Which subclass would you like? ")) 
            if subc == 1:
                subclass = "Aberrant Mind Origin Sorcerer"
            if subc == 2:
                subclass = "Clockwork Soul Origin Sorcerer"
            if subc == 3:
                subclass = "Divine Soul Origin Sorcerer"
            if subc == 4:
                subclass = "Draconic Bloodline Origin Sorcerer"     
            if subc == 5:
                subclass = "Lunar Magic Origin Sorcerer"
            if subc == 6:
                subclass = "Phoenix Origin Sorcerer"
            if subc == 7:
                subclass = "Runechild Origin Sorcerer"   
            if subc == 8:
                subclass = "Sea Origin Sorcerer"    
            if subc == 9:
                subclass = "Shadow Origin Sorcerer"    
            if subc == 10:
                subclass = "Stone Origin Sorcerer"    
            if subc == 11:
                subclass = "Storm Origin Sorcerer"    
            if subc == 12:
                subclass = "Wild Magic Origin Sorcerer"             
            if subc == 0:
                subclass = random.choice(Sor)                       
        if cla == "12":
            Class = "Warlock"
            print("0 - Random")
            print("1 - Ancient Dragon Patron Warlock")
            print("2 - Archfey Patron Warlock")
            print("3 - Celestial Patron Warlock")
            print("4 - The Fathomless Patron Warlock")
            print("5 - Fiend Patron Warlock")
            print("6 - The Genie Patron Warlock")
            print("7 - Great Old One Patron Warlock")
            print("8 - Hexblade Patron Warlock")
            print("9 - Mysterious Feline Patron Warlock")
            print("10 - Queen of Spiders Patron Warlock")
            print("11 - Raven Queen Patron Warlock")
            print("12 - Serpent Patron Warlock")
            print("13 - Undead Patron Warlock")
            print("14 - Undying Patron Warlock")
            subc = int(input("Which subclass would you like? ")) 
            if subc == 1:
                subclass = "Ancient Dragon Patron Warlock"
            if subc == 2:
                subclass = "Archfey Patron Warlock"
            if subc == 3:
                subclass = "Celestial Patron Warlock"
            if subc == 4:
                subclass = "The Fathomless Patron Warlock"     
            if subc == 5:
                subclass = "Fiend Patron Warlock"
            if subc == 6:
                subclass = "The Genie Patron Warlock"
            if subc == 7:
                subclass = "Great Old One Patron Warlock"   
            if subc == 8:
                subclass = "Hexblade Patron Warlock"    
            if subc == 9:
                subclass = "Mysterious Feline Patron Warlock"    
            if subc == 10:
                subclass = "Queen of Spiders Patron Warlock"    
            if subc == 11:
                subclass = "Raven Queen Patron Warlock"    
            if subc == 12:
                subclass = "Serpent Patron Warlock"    
            if subc == 13:
                subclass = "Undead Patron Warlock"     
            if subc == 14:
                subclass = "Undying Patron Warlock"                                                                                                    
            if subc == 0:
                subclass = random.choice(War)                            
        if cla == "13":
            Class = "Wizard"
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
            print("14 - War Arcane Tradition Wizard")
            subc = int(input("Which subclass would you like? ")) 
            if subc == 1:
                subclass = "Abjuration Arcane Tradition Wizard"
            if subc == 2:
                subclass = "Bladesinging Arcane Tradition Wizard"
            if subc == 3:
                subclass = "Blood Magic Arcane Tradition Wizard"
            if subc == 4:
                subclass = "Chronurgy Magic Arcane Tradition Wizard"     
            if subc == 5:
                subclass = "Conjuration Arcane Tradition Wizard"
            if subc == 6:
                subclass = "Divination Arcane Tradition Wizard"
            if subc == 7:
                subclass = "Enchantment Arcane Tradition Wizard"   
            if subc == 8:
                subclass = "Evocation Arcane Tradition Wizard"     
            if subc == 9:
                subclass = "Graviturgy Magic Arcane Tradition Wizard"     
            if subc == 10:
                subclass = "Illusion Arcane Tradition Wizard"     
            if subc == 11:
                subclass = "Necromancy Arcane Tradition Wizard"     
            if subc == 12:
                subclass = "Order of Scribes Arcane Tradition Wizard"                                                                 
            if subc == 13:
                subclass = "Transmutation Arcane Tradition Wizard" 
            if subc == 14:
                subclass = "War Arcane Tradition Wizard"                                                                
            if subc == 0:
                subclass = random.choice(Wiz)                        
        if cla == "0":
            Class = random.choice(Clas)    
            if Class == "Artificer":
                subclass = random.choice(Arti) 
            if Class == "Barbarian":
                subclass = random.choice(Barb) 
            if Class == "Bard":
                subclass = random.choice(Bar) 
            if Class == "Cleric":
                subclass = random.choice(Cle) 
            if Class == "Druid":
                subclass = random.choice(Dru) 
            if Class == "Fighter":
                subclass = random.choice(Fig) 
            if Class == "Monk":
                subclass = random.choice(Mon) 
            if Class == "Paladin":
                subclass = random.choice(Pal) 
            if Class == "Ranger":
                subclass = random.choice(Ran) 
            if Class == "Rogue":
                subclass = random.choice(Rog) 
            if Class == "Sorcerer":
                subclass = random.choice(Sor) 
            if Class == "Warlock":
                subclass = random.choice(War) 
            if Class == "Wizard":
                subclass = random.choice(Wiz) 
    if param == "N":
        Class = random.choice(Clas)
        if Class == "Artificer":
            subclass = random.choice(Arti) 
        if Class == "Barbarian":
            subclass = random.choice(Barb) 
        if Class == "Bard":
            subclass = random.choice(Bar) 
        if Class == "Cleric":
            subclass = random.choice(Cle) 
        if Class == "Druid":
            subclass = random.choice(Dru) 
        if Class == "Fighter":
            subclass = random.choice(Fig) 
        if Class == "Monk":
            subclass = random.choice(Mon) 
        if Class == "Paladin":
            subclass = random.choice(Pal) 
        if Class == "Ranger":
            subclass = random.choice(Ran) 
        if Class == "Rogue":
            subclass = random.choice(Rog) 
        if Class == "Sorcerer":
            subclass = random.choice(Sor) 
        if Class == "Warlock":
            subclass = random.choice(War) 
        if Class == "Wizard":
            subclass = random.choice(Wiz)       

    if Class == "Barbarian":
        if subclass == "Path of the Beast Barbarian":
            BPBO1 = "One of your parents is a lycanthrope, and you've inherited some of their curse."
            BPBO2 = "You are descended from an archdruid and inherited the ability to partially change shape."
            BPBO3 = "A fey spirit gifted you with the ability to adopt different bestial aspects."
            BPBO4 = "An ancient animal spirit dwells within you, allowing you to walk this path."
            BPBO = [BPBO1, BPBO2, BPBO3, BPBO4]
            BarbPathBeastOrigin = random.choice(BPBO)
            print(f"As a Path of the Beast Barbarian, the Origin of the Beast is: {BarbPathBeastOrigin}")
    if Class == "Monk":
        if subclass == "Way of the Ascendant Dragon Monk":
            ADO1 = "You honed your abilities by aligning your spirit with a dragon's world-altering power."
            ADO2 = "A dragon personally took an active role in shaping your inner energy."
            ADO3 = "You studied at a monastery that traces its teachings back centuries or more to a single dragon's instruction, or one that is devoted to a dragon god."
            ADO4 = "You spent long stretches meditating in the region around an ancient dragon's lair, absorbing that lair's ambient magic."
            ADO5 = "You found a scroll written in Draconic that contained inspiring new techniques."
            ADO6 = "After a dream featuring a five-handed dragonborn, you awoke with the mystical breath of dragons."
            ADO = [ADO1, ADO2, ADO3, ADO4, ADO5, ADO6]
            AscenDragOrigin = random.choice(ADO)
            print(f"As a Way of the Ascendant Dragon Monk, your Ascendant Origin: {AscenDragOrigin}")
    if Class == "Ranger":
        if subclass == "Drakewarden Ranger":
            DWO1 = "You studied a dragon's scale or claw, or a trinket from a dragon's hoard, creating your bond through that token's lingering draconic magic."
            DWO2 = "A secret order of rangers who collect and guard draconic lore taught you their ways."
            DWO3 = "A dragon gave you a geode or gemstone to care for. To your surprise, the drake hatched from that stone."
            DWO4 = "You ingested a few drops of dragon blood, forever infusing your nature magic with draconic power."
            DWO5 = "An ancient Draconic inscription on a standing stone empowered you when you read it aloud."
            DWO6 = "You had a vivid dream of a mysterious figure accompanied by seven yellow canaries, who warned you of impending doom. When you awoke, your drake was there, watching you."
            DWO = [DWO1, DWO2, DWO3, DWO4, DWO5, DWO6]
            DrakewardenOrigin = random.choice(DWO)
            print(f"As a Drakewarden Ranger, your Drakewarden Origin: {DrakewardenOrigin}")
    if Class == "Sorcerer":
        if subclass == "Aberrant Mind Origin Sorcerer":
            AbSO1 = "You were exposed to the Far Realm's warping influence. You are confinced that a tentacle is now growing on you, but no one else can see it."
            AbSO2 = "A psychic wind from the Astral Plane carried psionic energy to you. When you use your powers, faint motes of light sparkle around you."
            AbSO3 = "You once suffered the dominating powers of an aboleth, leaving a psychic splinter in your mind."
            AbSO4 = "You were implanted with a mind flayer tadpole, but the ceremorphosis never completed. And now its psionic power is yours. When you use it, your flesh shines with a strange mucus."
            AbSO5 = "As a child, you had an imaginary friend that looked like a flumph or a strange platypus-like creature. One day, it gifted you with psionic powers, which have ended up being not so imaginary."
            AbSO6 = "Your nightmares whisper the truth to you: your psionic powers are not your own. You draw them from your parasitic twin."
            AbSO = [AbSO1, AbSO2, AbSO3, AbSO4, AbSO5, AbSO6]
            AberrantOrigin = random.choice(AbSO)
            print(f"As an Aberrant Mind Origin Sorcerer, the Aberrant Origin is {AberrantOrigin}")
    if Class == "Warlock":
        if subclass == "The Genie Patron Warlock":
            GenK1 = "Dao, or Earth Genie"
            GenK2 = "Djinni, or Air Genie"
            GenK3 = "Efreeti, or Fire Genie"
            GenK4 = "Marid, or Water Genie"
            GenK = [GenK1, GenK2, GenK3, GenK4]
            GenieKind = random.choice(GenK)
            print(f"As a Genie Patron Warlock, your Genie is a(n): {GenieKind}")

    print("Your Class is " + subclass)

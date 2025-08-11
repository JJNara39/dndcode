import random
import os
import shutil
from fractions import Fraction
from dnd_python_classes import Player
import json
import dndcombat
from dnd_languagesskills import choose_spells, switch_spells
import dnd_tools

def save_character(player):
    with open(f"{player.name}_{player.playername}_level{player.level}.json", "w") as file:
        json.dump(player.__dict__, file, indent=4)

def load_character(choice):
    # Look through all files in current directory
    for filename in os.listdir():    
        # Find the one that starts with choice and ends in .json
        if filename.startswith(choice) and filename.endswith(".json"):
            with open(filename, "r") as file:
                data = json.load(file)
        
            # Create the Player object using values from the JSON file
            player = Player(data["name"], data["playername"], data["level"])

            player.__dict__.update(data)  # Update attributes from the file
            return player

def archive_character_files(player):
    archive_path = "Archive"
    os.makedirs(archive_path, exist_ok=True)
    file_variants = [
        f"{player.name}_{player.playername}_level{player.level}.json",
        f"{player.name}_{player.playername}_level{player.level}_charsheet.pdf",
        f"{player.name}_{player.playername}_level{player.level}_notes.txt"
    ]
    for fname in file_variants:
        if os.path.exists(fname):
            dest = os.path.join(archive_path, fname)
            shutil.move(fname, dest)
            print(f"Archived {fname}")
        else:
            print(f"{fname} not found for archiving.")    

def don_armor(player):
    armor_have_list = []
    armor_have_list_mod = []

    #Loop through equipment
    for eq in player.equipment:
        if isinstance(eq, dict):
            eq_name = eq.get('Name')
            print(f"Equipment I have: {eq_name}")
            for key, armor in dnd_tools.all_armor.items(): #armor would apply to all the subkeys
                proficiency = armor.get('Armor Type') in player.proficiencies
                tag = "Proficient" if proficiency else "Not Proficient"
                if eq_name == armor['Name']:  #so armor['Name'] looks through all the keys, finds 'Name', and assigns those words to armor['Name']
                    armor_have_list.append(eq_name)
                    armor_have_list_mod.append(f"{eq_name}, +{dnd_tools.all_armor[key]['Armor Class']} AC, {tag}")
                if "shield" in eq.get('Name', '').lower():
                    while True:
                        shield = input("Put on your shield, adding a +2 to AC? Y/N ").strip().lower()
                        if shield in {"y", "ye", "yes"}:
                            if "wooden shield" in eq.get('Name', '').lower():                                
                                player.offhand = eq
                            elif "shield" in eq.get('Name', '').lower():
                                player.offhand = eq
                            old_ac = player.armor_class
                            new_ac = old_ac + 2
                            print(f"You put on a shield, increasing your AC by 2, from {old_ac} to {new_ac}.")
                            player.armor_class += 2
                            break
                        elif shield in {"n", "no"}:
                            print("You choose not to equip the shield.")
                            break
                        else:
                            print("Invalid choice, please choose a valid option (Y/N).")
                    break
    if not armor_have_list:
        print("You have no armor to don.")
        return
    
    while True:
        try:
            print("Choose armor to don:")
            print("0 - No armor, exit")
            for idx, arm in enumerate(armor_have_list_mod, 1):
                print(f"{idx} - {arm}")
            choice = int(input("Your choice: "))
            if choice == 0:
                break
            elif 1 <= choice <= len(armor_have_list):
                chosen_armor = armor_have_list[choice - 1]
            else:
                print("Invalid choice. Please pick a valid number.")
                continue                                
            for key, armor in dnd_tools.all_armor.items():
                if chosen_armor == armor['Name']:
                    if armor['Armor Type'] in player.proficiencies:
                        ac = armor['Armor Class']
                        try:
                            mod = player.DexMod if dnd_tools.all_armor[key]['DexMod'] == True else 0
                        except KeyError:
                            mod = 0
                        old_ac = player.armor_class
                        player.armor_class += (ac+mod)
                        player.armordon = True
                        print(f"You don the {chosen_armor}. AC set to {player.armor_class}, from {old_ac}, since base AC is 10, the armor gives {ac} and your DexMod is {mod}.")
                    else:
                        print(f"You are not proficient with {chosen_armor}. Wearing it may impose disadvantage (not yet implemented).")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

def dndCharGen(param, player):
    CharacterGen = ["Race", "Class", "Background"]
    if param == "Y":
        
        print("0 - Random")
        print("1 - Race")
        print("2 - Class")
        print("3 - Background")
        while True:
            try:
                chargen1 = int(input("Which aspect of your character do you want to define first? "))
                if chargen1 == 0:
                    CharacterGenRand1 = random.choice(CharacterGen)
                    if CharacterGenRand1 == "Race":
                        player.choose_race(param)
                    if CharacterGenRand1 == "Class":
                        player.choose_class(param)
                    if CharacterGenRand1 == "Background":
                        player.choose_bkg(param)
                    CharacterGen.remove(CharacterGenRand1)
                    break
                elif 1 <= chargen1 <= 3:
                    first_choice = CharacterGen[chargen1 - 1]
                    if first_choice == "Race":
                        player.choose_race(param)
                    if first_choice == "Class":
                        player.choose_class(param)
                    if first_choice == "Background":
                        player.choose_bkg(param)
                    CharacterGen.remove(first_choice)
                    break
                else:
                    print("Invalid choice. Please choose a valid option (0-3).")           
            except ValueError:
                print("Invalid input. Please enter a number.") 

        print("0 - Random")        
        for i, option in enumerate(CharacterGen, 1):
            print(f"{i} - {option}")
        while True:
            try:
                chargen2 = int(input("Which aspect of your character do you want to define next? "))
                if chargen2 == 0:
                    CharacterGenRand2 = random.choice(CharacterGen)
                    if CharacterGenRand2 == "Race":
                        player.choose_race(param)
                    if CharacterGenRand2 == "Class":
                        player.choose_class(param)
                    if CharacterGenRand2 == "Background":
                        player.choose_bkg(param)
                    CharacterGen.remove(CharacterGenRand2)
                    break
                elif 1 <= chargen2 <= len(CharacterGen):
                    second_choice = CharacterGen[chargen2 - 1]
                    if second_choice == "Race":
                        player.choose_race(param)
                    if second_choice == "Class":
                        player.choose_class(param)
                    if second_choice == "Background":
                        player.choose_bkg(param)
                    CharacterGen.remove(second_choice)
                    break
                else:
                    print("Invalid choice. Please choose a valid option (0-2).")           
            except ValueError:
                print("Invalid input. Please enter a number.") 

        last_choice = CharacterGen[0]
        if last_choice == "Race":
            player.choose_race(param)
        if last_choice == "Class":
            player.choose_class(param)
        if last_choice == "Background":
            player.choose_bkg(param)

    if param == "N":
        CharacterGenRand1 = random.choice(CharacterGen)
        if CharacterGenRand1 == "Race":
            player.choose_race(param)
        if CharacterGenRand1 == "Class":
            player.choose_class(param)
        if CharacterGenRand1 == "Background":
            player.choose_bkg(param)
        CharacterGen.remove(CharacterGenRand1)
        CharacterGenRand2 = random.choice(CharacterGen)
        if CharacterGenRand2 == "Race":
            player.choose_race(param)
        if CharacterGenRand2 == "Class":
            player.choose_class(param)
        if CharacterGenRand2 == "Background":
            player.choose_bkg(param)
        CharacterGen.remove(CharacterGenRand2)
        CharacterGenRand3 = random.choice(CharacterGen)
        if CharacterGenRand3 == "Race":
            player.choose_race(param)
        if CharacterGenRand3 == "Class":
            player.choose_class(param)
        if CharacterGenRand3 == "Background":       
            player.choose_bkg(param)
    
    boon_chance = random.randint(1, 100)
    if boon_chance >= 90:
        print(f"{player.name} has gotten the boon of Beachball, granting them access to Wild Magic.")
        player.beachballflag = True
    player.summation(param)
    player.update(param)
    player.class_explained(param)  #This WAS after update  
    choose_spells(player, param)  
    player.post_spell_update()
    player.create_sheet()
    player.write_notes()

                         


    #If a player wants to know what attributes the character has before making the sheet
    #for attribute, value in player.data.items():
    #    if value not in [None, []]:  # Exclude None and empty lists
    #        print(f"{attribute}: {value}")
    


#This was just a test to make sure I can make 300 pages
'''
for chi in range(3):
    for ch in range(100):
        playername = f"Marik{chi}.{ch}"
        charactername = f"({chi}.{ch})Nara"
        param = "N"
        plLvl = 5
        player = Player(charactername, playername, plLvl) 
        dndCharGen(param, player)
'''
#Dice are in dndchargen


# DMorPlay = int(input("Are you a 1 - DM or 2 - Player? ")) This is not needed
# party = int(input("How many characters will your party have? ")) #This can be used later when I implement CR encounters, it will function on party size
# plLvlList = []
#numMon = 1 #Lets just say for now there is one monster per encounter; Nor is this needed

##########################################################################################
'''
def mixedFraction(numerator, denominator): #Plugging in 1 lvl 10 character has CR at 2&3/2; This is a problem pre-Python 3.10, otherwise I couldve done _normalize
    #ecrFract = Fraction(ecr)
    num = int(numerator)
    den = int(denominator)
    remainder = num % den
    if remainder != 0:
        quotient = int(num/den)
        if quotient != 0:
            for q in range(quotient):
                num = num-den
            return str(quotient) + " & " + str(Fraction(num/den))
        else:
            return str(Fraction(num/den))
    else:
        return str(Fraction(num/den))
'''
    
###########################################################################################
'''
#This is meant to include the dm and their abilities, but for now it is commented out
if DMorPlay == 1:
    encounterYN = input("Are you building an encounter? Y/N ")
    if encounterYN == "Y":
        eYN = "Y"
    if encounterYN == "y":
        eYN = "Y"
    if encounterYN == "Yes":
        eYN = "Y"
    if encounterYN == "yes":
        eYN = "Y"
    if encounterYN == "Ye":
        eYN = "Y"
    if encounterYN == "ye":
        eYN = "Y"
    if encounterYN == "N":
        eYN = "N"
    if encounterYN == "n":
        eYN = "N"
    if encounterYN == "No":
        eYN = "N"
    if encounterYN == "no":
        eYN = "N"

    if eYN == "Y":
        for p in range(party):
            playername = input("Who is the player behind this character? ")
            charactername = input("What is this character's name? ")
            plLvlWhile = False
            while not plLvlWhile:
                plLvl = int(input(f"What level is {charactername}? "))
                if (plLvl > 0 and  plLvl <= 20):
                    plLvlWhile = True
                else:
                    print("Player level is out of range, the range is 1-20, please try again.")
            plLvlList.append(plLvl)
            para = input(f"Set parameters on {charactername}? Y/N ")
            if para == "Y":
                param = "Y"
            if para == "y":
                param = "Y"
            if para == "Yes":
                param = "Y"
            if para == "yes":
                param = "Y"
            if para == "Ye":
                param = "Y"
            if para == "ye":
                param = "Y"
            if para == "N":
                param = "N"
            if para == "n":
                param = "N"
            if para == "No":
                param = "N"
            if para == "no":
                param = "N"            
            dndCharGen(param, plLvl, charactername, playername)
            
        properPL = sum(plLvlList) / party
        #encounterCR = int(properPL) * party * (1/4) #Instead of making this fraction that auto reduces, lets instead plug the numerator and denominator in an let it do its thing
        eCRMixednum = int(properPL) * party
        eCRMixedden = 4 #The initial scenario was a lvl 1 character could handle a CR of 1/4
        eCRMixed = mixedFraction(eCRMixednum,eCRMixedden)
        #eCRMixed = mixedFraction(encounterCR) #Going to plug numerator and denominator into our mixedFraction function instead
        print("With a party size of {} and a total party level of {}, The Total Encounter CR to work with is {}".format(party, sum(plLvlList), eCRMixed))

    if eYN == "N":
        for p in range(party):
            #Add in a level check for classes, if the level is 3+, the subclass is available.
            playername = input("Who is the player behind this character? ")
            charactername = input("What is this character's name? ")
            plLvlWhile = False
            while not plLvlWhile:
                plLvl = int(input(f"What level is {charactername}? "))
                if (plLvl > 0 and  plLvl <= 20):
                    plLvlWhile = True
                else:
                    print("Player level is out of range, the range is 1-20, please try again.")
            plLvlList.append(plLvl)            
            para = input(f"Set parameters on {charactername}? (Y/N) ").strip().lower()
            if para in {"y", "yes", "ye"}:
                param = "Y"
            elif para in {"n", "no"}:
                param = "N"                     
            dndCharGen(param, plLvl, charactername, playername)
else:
Removing dm/player for now, there for the first part of this if statement is null and the following for loop was shift-tabbed'''
#for p in range(party): #Commented out party, so un-tabbed the following (all the way to dndchargen)
player_list = [] #later i will load a player list

#Temporary

'''for _ in range(10000):
    playername = "Nara"
    charactername = "Marik"
    plLvl = 1
    player = Player(charactername, playername, plLvl)
    param = "N"
    dndCharGen(param, player)'''



while True: #This is temporarily commented out to do the 10000 loop
    print("1 - Create a Character")
    print("2 - Load a Character")
    print("3 - Exit")
    try:
        start_choice = int(input("What would you like to do first? "))
        if start_choice == 1:
            playername = input("Who is the player behind this character? ")        
            charactername = input("What is this character's name? ")
            while True:
                try:
                    plLvl = int(input(f"What level is {charactername}? "))
                    if (plLvl > 0 and plLvl <= 20):
                        break   
                    else:
                        print("Player level is out of range, the range is 1-20, please try again.")
                except ValueError:  # Handles non-numeric input
                    print("Invalid input. Please enter a number.")            
                #plLvlList.append(plLvl)   
            player = Player(charactername, playername, plLvl) 
            while True:
                multi_choice = input(f"Do you want {player.name} to have the option to multiclass? Y/N ").strip().lower()
                if multi_choice in {"y", "ye", "yes"}:
                    player.multi = True
                    break
                elif multi_choice in {"n", "no"}:
                    player.multi = False  
                    break
            while True:
                nat1_choice = input(f"Do you want {player.name} to have the ability to do self damage on a nat1? Y/N ").strip().lower()
                if nat1_choice in {"y", "ye", "yes"}:
                    player.nat1choice = True
                    break
                elif nat1_choice in {"n", "no"}:
                    player.nat1choice = False  
                    break            
            while True:
                para = input(f"Set parameters on {charactername}? Y/N ").strip().lower()
                if para in {"y", "ye", "yes"}:
                    param = "Y"
                    break
                elif para in {"n", "no"}:
                    param = "N"   
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            dndCharGen(param, player)
            while True:
                savepara = input(f"Save parameters for {player.name}? Y/N ").strip().lower()
                if savepara in {"y", "ye", "yes"}:
                    saveparam = "Y"
                    break
                elif savepara in {"n", "no"}:
                    saveparam = "N"
                    break   
                else:
                    print("Invalid choice, please choose a valid option.")
            if saveparam == "Y":                
                entry = f"{player.name}_{player.playername}"
                if entry not in player_list:
                    player_list.append(entry) #Makes the all_character list
                with open("player_list.json", "w") as file: #Should it not just dump the entire player list into the file?
                    json.dump(player_list, file, indent=4)
                save_character(player) #Makes a character's own list
                if os.path.exists("group_characters.json"):
                    with open("group_characters.json", "r") as file:
                        group_characters = json.load(file)
                else:
                    group_characters = {}
                # Ask which group to save to
                print("Choose a group to save this character to:")
                group_list = list(group_characters.keys())
                for idx, group in enumerate(group_list, start=1):
                    print(f"{idx}: {group}")
                print("0: Create new group")

                while True:
                    try:
                        group_choice = int(input("Enter the number of the group: "))
                        if group_choice == 0:
                            new_group = input("Enter new group name: ").strip()
                            group_characters.setdefault(new_group, [])
                            selected_group = new_group
                            break
                        elif 1 <= group_choice <= len(group_list):
                            selected_group = group_list[group_choice - 1]
                            break
                        else:
                            print("Invalid choice.")
                    except ValueError:
                        print("Please enter a number.")     
                char_identifier = f"{player.name}_{player.playername}"
                group_characters[selected_group].append(char_identifier)

                # Save updated group dictionary
                with open("group_characters.json", "w") as file:
                    json.dump(group_characters, file, indent=4)              
            continue
        elif start_choice == 2:
            player = None
            player_group = []
            if os.path.exists("player_list.json"):
                with open("player_list.json", "r") as file:
                    player_list = json.load(file)
            
            if not player_list:
                print("Player list is empty, please create a character and add to list.")
            else:
                while True:
                    try:
                        print("0 - All Characters")
                        print("1 - Select from Group")
                        grouporall = int(input("Would you like to load a Character from a Group or would you like to see every Character? "))
                        if grouporall == 0: #All characters
                            print("Available characters:")
                            for pl, player in enumerate(player_list, 0):
                                print(f"{pl+1} - {player}")
                            while True:
                                try:
                                    character_choice = int(input("Which character would you like to load? "))
                                    if 0 <= character_choice <= len(player_list):
                                        selected_player = player_list[character_choice-1]
                                        player = load_character(selected_player)
                                        break
                                    else:
                                        print("Invalid choice. Please enter a number from the list.")
                                except ValueError:
                                    print("Invalid input. Please enter a valid number.")  
                            break     
                        elif grouporall == 1: #Pick a group
                            if os.path.exists("group_characters.json"):
                                with open("group_characters.json", "r") as file:
                                    group_characters = json.load(file)
                            else:
                                print("No group file exists yet. Showing all characters instead.")
                                for pl, pname in enumerate(player_list, 1):
                                    print(f"{pl} - {pname}")
                                while True:
                                    try:
                                        character_choice = int(input("Which character would you like to load? "))
                                        if 1 <= character_choice <= len(player_list):
                                            selected_player = player_list[character_choice - 1]
                                            player = load_character(selected_player)
                                            break
                                        else:
                                            print("Invalid choice. Please enter a number from the list.")
                                    except ValueError:
                                        print("Invalid input. Please enter a valid number.")  
                                break
                            group_list = list(group_characters.keys())
                            if not group_list:
                                print("No groups found.")
                                break

                            print("Available groups:")
                            for idx, gname in enumerate(group_list, 1):
                                print(f"{idx} - {gname}")

                            while True:
                                try:
                                    group_choice = int(input("Choose a group: "))
                                    if 1 <= group_choice <= len(group_list):
                                        selected_group = group_list[group_choice - 1]
                                        break
                                    else:
                                        print("Invalid group choice.")
                                except ValueError:
                                    print("Please enter a number.")

                            characters_in_group = group_characters[selected_group]

                            if not characters_in_group:
                                print("No characters in this group.")
                                break

                            print(f"\nCharacters in group '{selected_group}':")
                            print(f"0 - Load ALL characters in group")
                            for idx, char in enumerate(characters_in_group, 1):
                                print(f"{idx} - {char}")

                            while True:
                                try:
                                    group_char_choice = int(input("Which character would you like to load? "))
                                    if group_char_choice == 0:
                                        player_group = []
                                        for ch_id in characters_in_group:
                                            player_group.append(load_character(ch_id))
                                        print(f"{len(player_group)} characters loaded from group '{selected_group}'.")
                                        break
                                    elif 1 <= group_char_choice <= len(characters_in_group):
                                        selected_player = characters_in_group[group_char_choice - 1]
                                        player = load_character(selected_player)
                                        print(f"Loaded {player.name}")
                                        break
                                    else:
                                        print("Invalid choice.")
                                except ValueError:
                                    print("Please enter a number.")
                            break  # done loading

                        else:
                            print("Invalid choice, select 0 or 1.")
                    except ValueError:
                        print("Please enter a number.")

                print(f"Player list is currently {player_list}")    
                if player_group == []:
                    player_group.append(player)                    
                while True: #While true will let this be infinite
                    try:
                        print("\nWhat would you like to do?")
                        print("1 - Rest")
                        print("2 - Level Up")
                        print("3 - Combat Tester")
                        print("4 - Return to Main Menu")
                        update_choice = int(input("Enter your choice: "))
                        if update_choice == 1:
                            #Rest Notes
                            print("Resting...")
                            for pl in player_group: #I may need to make sure player_group gets defined before running This, Level Up, or Combat 
                                print(f"Currently, the spellslots is {pl.spellslots_list_editable}")
                                while True:
                                    try:
                                        print("1 - Short Rest")
                                        print("2 - Long Rest")
                                        choice = int(input("What kind of rest is this? "))
                                        if choice == 1:
                                            rest_type = "Short Rest"
                                            break
                                        elif choice == 2:
                                            rest_type = "Long Rest"
                                            break
                                        else:
                                            print("Invalid choice. Please enter a number from the list.")
                                    except ValueError:
                                        print("Invalid input. Please enter a valid number.")  
                                if rest_type == "Short Rest":
                                    for cl in pl.Class:
                                        if cl == "Warlock":
                                            print(f"You editable spellslots look like: {pl.spellslots_list_editable}")
                                            if "Warlock Spell Slots" in pl.spellslots_list_editable:
                                                current = pl.spellslots_list_editable["Warlock Spell Slots"]
                                                print(f"Current Warlock Spell Slots: {current}")
                                                pl.spellslots_list_editable["Warlock Spell Slots"] = pl.spellslots_list["Warlock Spell Slots"]
                                                print(f"Warlock Spell Slots have been restored to {pl.spellslots_list_editable['Warlock Spell Slots']}")
                                elif rest_type == "Long Rest":
                                    for cl in pl.Class:
                                        if cl in ["Artificer", "Cleric", "Druid", "Paladin", "Ranger", "Warlock", "Wizard"]:
                                            if cl in ["Artificer", "Cleric", "Druid", "Wizard"]:
                                                spellcount = []
                                                spelllistkeys = list(player.spelllist.keys())
                                                for splk in spelllistkeys:
                                                    full_spell = player.spelllist[splk]
                                                    if full_spell["Level"] > 0:
                                                        spellcount.append(splk)
                                                count = len(spellcount)
                                                switch_spells(pl, cantrip = False, count = count)
                                                if cl in ["Artificer", "Wizard"]:
                                                    switch_spells(pl, cantrip = True, count = 1)
                                                
                                            elif cl in ["Paladin", "Ranger"]:
                                                switch_spells(pl, cantrip = False, count = 1)
                                            
                                            pl.spellslots_list_editable = pl.spellslots_list                    
                                            print(f"Now the spellslot is {pl.spellslots_list_editable}")    
                                    available_actions = list(pl.actions.keys())
                                    for act in available_actions:
                                        if act == "Breath Weapon":
                                            pl.actions[act]["Current Uses"] = pl.actions[act]["Uses"]
                                with open(f"{pl.name}_{pl.playername}_level{pl.level}.json", "w") as f: #These 2 lines update the sheet
                                    json.dump(pl.__dict__, f, indent=4)                                                    
                            break
                        elif update_choice == 2:
                            while True:
                                try:
                                    for idx, pl in enumerate(player_group, 1):
                                        print(f'{idx} - {pl.name}')
                                    who_level_up = int(input("Who is leveling up? "))
                                    if 1 <= who_level_up <= len(player_group):
                                        player = player_group[who_level_up - 1]
                                        break
                                    else:
                                        print(f"Invalid input, please enter from 1 to {len(player_group + 1)}")
                                except ValueError:
                                    print("Invalid input. Please enter a number")
                            archive_character_files(player)
                            print(f"group_characters is {group_characters}")
                            print(f"selected_group is {selected_group}")
                            while True:
                                try:
                                    level_up = int(input(f"What level is {player.name} now? "))
                                    if (level_up > player.level and level_up <= 20):
                                        break   
                                    else:
                                        print(f"Player level is out of range, the range is {player.level}-20, please try again.")
                                except ValueError:  # Handles non-numeric input
                                    print("Invalid input. Please enter a number.")
                            player.hitpointsset = False
                            player.leveldiff = level_up - player.level
                            player.level = level_up
                            if player.multi == False:
                                while True:
                                    smclass = input(f"Do you wish {player.name} to have the option to multi-class at this or higher levels? Y/N ").strip().lower()
                                    if smclass in {"y", "ye", "yes"}:
                                        player.multi = True
                                        player.singlemulticlass = "Y"
                                        break
                                    elif smclass in {"n", "no"}:
                                        player.singlemulticlass = "N"
                                        break
                                    else:
                                        print("Invalid choice, please select Y/N")  
                                        ###More to this?                                
                            player.class_explained(param = "Y")
                            player.update(param = "Y")
                            for cl in player.Class:
                                if cl in ["Bard", "Cleric", "Druid", "Sorcerer", "Warlock"]:
                                    print(f"On level up you can switch a spell, because you are a {cl}")
                                    switch_spells(player, cantrip = True, count = 1)
                                    if cl in ["Bard", "Sorcerer", "Warlock"]:
                                        print(f"On level up you can switch a spell, because you are a {cl}")
                                        switch_spells(player, cantrip = False, count = 1)
                            player.create_sheet()
                            player.write_notes()
                            while True:
                                savepara = input(f"Save parameters for {player.name}? Y/N ").strip().lower()
                                if savepara in {"y", "ye", "yes"}:
                                    saveparam = "Y"
                                    break
                                elif savepara in {"n", "no"}:
                                    saveparam = "N"
                                    break   
                                else:
                                    print("Invalid Response, try again.")
                            if saveparam == "Y":
                                char_identifier = f"{player.name}_{player.playername}"
                                player_list = [p for p in player_list if p != char_identifier]
                                player_list.append(char_identifier)
                                with open("player_list.json", "w") as file:
                                    json.dump(player_list, file, indent=4)                                      
                                group_characters[selected_group] = [p for p in group_characters[selected_group] if p != char_identifier]                                        
                                group_characters[selected_group].append(char_identifier)
                                with open("group_characters.json", "w") as file:
                                    json.dump(group_characters, file, indent=4)   
                                save_character(player)        
                                continue

                            if saveparam == "N":
                                continue       
                        elif update_choice == 3:
                                #for pl in player_group:
                                #    print(f"Currently entering is {pl.name}") #This block is a debug
                            while True:
                                try:
                                    pl_choice = input("Knowing the player(s), do you want to add more? Y/N ").strip().lower()
                                    if pl_choice in {"y", "ye", "yes"}:
                                        while True:
                                            used_names = [(f"{pg.name}" + "_" + f"{pg.playername}") for pg in player_group]
                                            new_player_list = [pl for pl in player_list if pl not in used_names]
                                            

                                            if not new_player_list:
                                                print("No more characters to choose from.")
                                                break         

                                            print("Available characters:")
                                            for idx, player in enumerate(new_player_list, 1):
                                                print(f"{idx} - {player}")
                                        
                                            while True:
                                                try:
                                                    character_choice = int(input("Which character would you like to load? "))
                                                    if 1 <= character_choice <= len(new_player_list):
                                                        selected_player = new_player_list[character_choice-1]
                                                        player = load_character(selected_player)
                                                        player_group.append(player)
                                                        break
                                                    else:
                                                        print("Invalid choice. Please enter a number from the list.")
                                                except ValueError:
                                                    print("Invalid input. Please enter a valid number.")      
                                            for pl in player_group:
                                                print(f"Now Entering is entering is {pl.name}") #debug                                                      
                                            cont = input("Would you like to add another character? (Y/N): ").strip().lower()
                                            if cont in ['n', 'no']:
                                                break 
                                        for pl in player_group:
                                            if pl.armordon == False:
                                                don_armor(pl)    
                                        dndcombat.combat(player_group) 
                                        break                                                                                                                     
                                    elif pl_choice in ['n', 'no']:
                                        for pl in player_group:
                                            if pl.armordon == False:
                                                don_armor(pl)
                                        dndcombat.combat(player_group)
                                        break
                                    else:
                                        print("Invalid choice, please choose a valid option.")
                                except ValueError: #Handles non-numeric choices  
                                    print("Invalid input. Please enter a number.")  
                            continue
                        elif update_choice == 4:
                            break
                        else:
                            print("Invalid choice, please choose a valid option.")
                    except ValueError: #Handles non-numeric choices  
                        print("Invalid input. Please enter a number.")   
        elif start_choice == 3:
            break            
        else:
            print("Invalid choice, please choose a valid option.")
    except ValueError: #Handles non-numeric choices  
        print("Invalid input. Please enter a number.") 

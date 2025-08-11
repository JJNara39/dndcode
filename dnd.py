import random
import os
from fractions import Fraction
from dnd_python_classes import Player
import json

def save_character(player):
    with open(f"{player.name}_{player.playername}_level{player.level}.json", "w") as file:
        json.dump(player.__dict__, file, indent=4)

def load_character(choice):
    with open(f"{choice}.json", "r") as file:
        data = json.load(file)
    
    # Create the Player object using values from the JSON file
    player = Player(data["name"], data["playername"], data["level"])

    player.__dict__.update(data)  # Update attributes from the file
    return player



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
    
    player.summation(param)
    if player.proficiencies is None:
        player.proficiencies = []
    player.class_explained(param)
    player.update()
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
            print("Invalid choice, please choose a valid option.")
    if saveparam == "Y":
        player_list.append(f"{player.name}_{player.playername}_level{player.level}")
        with open("player_list.json", "w") as file:
            json.dump(player_list, file, indent=4)
        save_character(player)


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


while True:
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
            break
        elif start_choice == 2:
            if os.path.exists("player_list.json"):
                with open("player_list.json", "r") as file:
                    player_list = json.load(file)
            if not player_list:
                print("Player list is empty, please create a character and add to list.")
            else:
                print("Available characters:")
                for pl, player in enumerate(player_list, 1):
                    print(f"{pl} - {player}")
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
                    while True: #While true will let this be infinite
                        print("1 - Rest")
                        print("2 - Level Up")
                        try:
                            update_choice = int(input(f"How is {player.name} changing? "))            
                            if update_choice == 1:
                                #Rest Notes
                                print("Resting...")
                                break
                            elif update_choice == 2:
                                while True:
                                    try:
                                        level_up = int(input(f"What level is {player.name} now? "))
                                        if (level_up > player.level and level_up <= 20):
                                            break   
                                        else:
                                            print(f"Player level is out of range, the range is {player.level}-20, please try again.")
                                    except ValueError:  # Handles non-numeric input
                                        print("Invalid input. Please enter a number.")
                                player.level = level_up
                                player.class_explained(param = "Y")
                                player.update()  
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
                                    player_list.append(f"{player.name}_{player.playername}_level{player.level}")
                                    with open("player_list.json", "w") as file:
                                        json.dump(player_list, file, indent=4)
                                    save_character(player)        
                                    continue
                                if saveparam == "N":
                                    continue       
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

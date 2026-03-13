import random
import math
import dnd_tools
import dnd_spells

def languagegen(param, PlLang, SLANG):
    if param == "Y":
        # Display options
        while True:
            try:
                print("0 - Random")
                for index, language in enumerate(SLANG, 1):
                    print(f"{index} - {dnd_tools.languages[language]}")        
                # Player selects a language
                pllang_input = int(input("Please pick a language from the above list: "))
                if pllang_input == 0:  # Random selection
                    PlRandLang = random.choice(SLANG)
                    PlLang.append(dnd_tools.languages[PlRandLang])
                    SLANG.remove(PlRandLang)
                    break
                elif 1 <= pllang_input <= len(SLANG):  # Specific selection
                    selected_language = SLANG[pllang_input - 1]
                    PlLang.append(dnd_tools.languages[selected_language])
                    SLANG.remove(selected_language)
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.")
    elif param == "N":  # Random assignment
        PlRandLang = random.choice(SLANG)
        PlLang.append(dnd_tools.languages[PlRandLang])
        SLANG.remove(PlRandLang)
    
    return PlLang, SLANG

def gamingsetsmusicalinstr(param, PlProf):
    GamingSets = [tool["Name"] for tool in dnd_tools.gaming_sets.values()]
    musicalinstr = [tool["Name"] for tool in dnd_tools.musical_instr.values()] 
    
    all_tools = GamingSets+musicalinstr+[dnd_tools.kits["ThievKit"]["Name"]]

    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, alltl in enumerate(all_tools, 1):
                    print(f"{idx} - {alltl}")
                gsmit = int(input("Choose a gaming set/musical instrument to be proficient in. "))
                if gsmit == 0:
                    PlProf.append(random.choice(all_tools))
                    break
                elif 1 <= gsmit <= len(all_tools):
                    PlProf.append(all_tools[gsmit - 1])  
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.")          
    if param == "N":
        PlProf.append(random.choice(all_tools))
    return PlProf

def gamingsetmusicalinstrthieves(param, PlProf):
    GamingSets = [tool["Name"] for tool in dnd_tools.gaming_sets.values()]
    musicalinstr = [tool["Name"] for tool in dnd_tools.musical_instr.values()] 
    
    all_tools = GamingSets+musicalinstr+[dnd_tools.kits["ThievKit"]["Name"]]

    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, alltl in enumerate(all_tools, 1):
                    print(f"{idx} - {alltl}")
                gsmit1 = int(input("Choose a tool to be proficient in. "))
                if gsmit1 == 0:
                    PlProf.append(random.choice(all_tools))
                    break
                elif 1 <= gsmit1 <= len(all_tools):
                    PlProf.append(all_tools[gsmit1 - 1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.")
        while True:
            try:
                print("0 - Random")
                for idx, alltl in enumerate(all_tools, 1):
                    print(f"{idx} - {alltl}")
                gsmit2 = int(input("Choose a second tool to be proficient in. "))
                if gsmit2 == 0:
                    PlProf.append(random.choice(all_tools))
                    break
                elif 1 <= gsmit2 <= len(all_tools):
                    PlProf.append(all_tools[gsmit2 - 1]) 
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.")           
    if param == "N":
        PlProf.append(random.choice(all_tools))
        PlProf.append(random.choice(all_tools))        
    return PlProf

def musicalinstr(param, PlProf):
    musicalinstr = [tool["Name"] for tool in dnd_tools.musical_instr.values()] 
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, mi in enumerate(musicalinstr, 1):
                    print(f"{idx} - {mi}")
                musi = int(input("Choose a musical instrument to be proficient in. "))
                if musi == 0:
                    PlProf.append(random.choice(musicalinstr))
                    break
                elif 1 <= musi <= len(musicalinstr):
                    PlProf.append(musicalinstr[musi - 1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.")
    if param == "N":    
        PlProf.append(random.choice(musicalinstr))
    return PlProf

def choicefourlang(param, PlLang, SLANG, langlist):
    FourLang = []
    FourLangNames = []
    for lang in langlist:
        if lang in SLANG:
            FourLang.append(lang)
            FourLangNames.append(dnd_tools.languages[lang])
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, cfl in enumerate(FourLangNames, 1):
                    print(f"{idx} - {cfl}")
                flang_input = int(input("Please pick a language from the above list. "))
                if flang_input == 0:
                    flang_rand = random.choice(FourLang)
                    PlLang.append(dnd_tools.languages[flang_rand])
                    SLANG.remove(flang_rand)
                    break
                elif 1 <= flang_input <= len(FourLang):
                    PlLang.append(FourLangNames[flang_input - 1])
                    SLANG.remove(FourLang[flang_input - 1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.")
    if param == "N":
        flang_rand = random.choice(FourLang)
        PlLang.append(dnd_tools.languages[flang_rand])
        SLANG.remove(flang_rand)
    return PlLang, SLANG  
 
def artisantools(param, PlProf):
    artisantools = [tool['Name'] for tool in dnd_tools.artisan_tools.values()]
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, fullatname in enumerate(artisantools, 1):
                    print(f"{idx} - {fullatname}")
                arttools = int(input("Choose a tool to be proficient in. "))
                if arttools == 0:
                    PlProf.append(random.choice(artisantools))
                    break
                elif 1 <= arttools <= len(artisantools):
                    print(f"Choice: You chose {arttools}")
                    selected = artisantools[arttools - 1]
                    print(f"Aka, you picked {selected}")
                    PlProf.append(artisantools[arttools - 1])     
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 
    if param == "N":           
        PlProf.append(random.choice(artisantools)) 
    return PlProf  
   
def gamingsets(param, PlProf):  
    GamingSets = [tool["Name"] for tool in dnd_tools.gaming_sets.values()]
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, gs in enumerate(GamingSets, 1):
                    print(f"{idx} - {gs}")
                gamset = int(input("Choose a gaming set to be proficient in. "))
                if gamset == 0:
                    PlProf.append(random.choice(GamingSets))
                    break
                elif 1 <= gamset <= len(GamingSets):
                    PlProf.append(GamingSets[gamset - 1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.")
    if param == "N":
        PlProf.append(random.choice(GamingSets))
    return PlProf

def choicethreelang(param, PlLang, SLANG, langlist):
    ThreeLang = []
    ThreeLangNames = []
    for lang in langlist:
        if lang in SLANG:
            ThreeLang.append(lang)
            ThreeLangNames.append(dnd_tools.languages[lang])
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, ctl in enumerate(ThreeLangNames, 1):
                    print(f"{idx} - {ctl}")
                thlang_input = int(input("Please pick a language from the above list. "))
                if thlang_input == 0:
                    thlang_rand = random.choice(ThreeLang)
                    PlLang.append(dnd_tools.languages[thlang_rand])
                    SLANG.remove(thlang_rand)
                    break
                elif 1 <= thlang_input <= len(ThreeLang):
                    PlLang.append(ThreeLangNames[thlang_input - 1])
                    SLANG.remove(ThreeLang[thlang_input - 1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.")
    if param == "N":
        thlang_rand = random.choice(ThreeLang)
        PlLang.append(dnd_tools.languages[thlang_rand])
        SLANG.remove(thlang_rand)
    return PlLang, SLANG

def choicefourskill(param, skills_dict, skill1, skill2, skill3, skill4, skillname1, skillname2, skillname3, skillname4):
    FourSkill = [skill1, skill2, skill3, skill4]
    FourSkillName = [skillname1, skillname2, skillname3, skillname4]
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, sknm in enumerate(FourSkillName, 1):
                    print(f"{idx} - {sknm}")
                fskl = int(input("Please pick a skill from the above list. "))
                if fskl == 0:
                    skills_dict[random.choice(FourSkill)] += 1
                    break
                elif 1 <= fskl <= len(FourSkill):
                    skills_dict[FourSkill[fskl - 1]] += 1
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.")
    if param == "N":
        skills_dict[random.choice(FourSkill)] += 1
    return (skills_dict[skill1], skills_dict[skill2], skills_dict[skill3], skills_dict[skill4])

def choicethreeskill(param, skills_dict, skill1, skill2, skill3, skillname1, skillname2, skillname3):
    ThreeSkill = [skill1, skill2, skill3]
    ThreeSkillName = [skillname1, skillname2, skillname3]
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, skl in enumerate(ThreeSkillName, 1):
                    print(f"{idx} - {skl}")
                thrskl = int(input("Please pick a skill from the above list. "))
                if thrskl == 0:
                    randomSkill = random.choice(ThreeSkill)
                    skills_dict[randomSkill] += 1
                    break
                elif 1 <= thrskl <= len(ThreeSkill):
                    skills_dict[ThreeSkill[thrskl - 1]] += 1
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.")
    if param == "N":
        randomSkill = random.choice(ThreeSkill)
        skills_dict[randomSkill] += 1
    return (skills_dict[skill1], skills_dict[skill2], skills_dict[skill3])

def choicethreeskill2(param, skills_dict, skill1, skill2, skill3, skillname1, skillname2, skillname3):
    ThreeSkill = [skill1, skill2, skill3]
    ThreeSkillName = [skillname1, skillname2, skillname3]
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, skl in enumerate(ThreeSkillName, 1):
                    print(f"{idx} - {skl}")
                thrskl = int(input("Please pick a skill from the above list. "))
                if thrskl == 0:
                    randomSkill = random.choice(ThreeSkill)
                    skills_dict[randomSkill] += 1
                    break
                elif 1 <= thrskl <= len(ThreeSkill):
                    skills_dict[ThreeSkill[thrskl - 1]] += 1
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.")
        while True:
            try:
                print("0 - Random")
                for idx, skl in enumerate(ThreeSkillName, 1):
                    print(f"{idx} - {skl}")
                thrskl2 = int(input("Please pick a second skill from the above list. "))
                if thrskl2 == 0:
                    randomSkill = random.choice(ThreeSkill)
                    skills_dict[randomSkill] += 1
                    break
                elif 1 <= thrskl2 <= len(ThreeSkill):
                    skills_dict[ThreeSkill[thrskl2 - 1]] += 1    
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.")                    
    if param == "N":
        randomSkill1 = random.choice(ThreeSkill)
        randomSkill2 = random.choice(ThreeSkill)
        skills_dict[randomSkill1] += 1
        skills_dict[randomSkill2] += 1
    return (skills_dict[skill1], skills_dict[skill2], skills_dict[skill3])
    
def choicefourskill2(param, skills_dict, skill1, skill2, skill3, skill4, skillname1, skillname2, skillname3, skillname4):
    FourSkill = [skill1, skill2, skill3, skill4]
    FourSkillName = [skillname1, skillname2, skillname3, skillname4]
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, skl in enumerate(FourSkillName, 1):
                    print(f"{idx} - {skl}")
                fskl = int(input("Please pick a skill from the above list. "))
                if fskl == 0:
                    randomSkill = random.choice(FourSkill)
                    skills_dict[randomSkill] += 1
                    break
                elif 1 <= fskl <= len(FourSkill):
                    skills_dict[FourSkill[fskl - 1]] += 1 
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.")
        while True:
            try:
                print("0 - Random")
                for idx, skl in enumerate(FourSkillName, 1):
                    print(f"{idx} - {skl}")
                fskl2 = int(input("Please pick a second skill from the above list. "))
                if fskl2 == 0:
                    randomSkill = random.choice(FourSkill)
                    skills_dict[randomSkill] += 1 
                    break  
                elif 1 <= fskl2 <= len(FourSkill):
                    skills_dict[FourSkill[fskl2 - 1]] += 1   
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.")          
    if param == "N":
        randomSkill1 = random.choice(FourSkill)
        randomSkill2 = random.choice(FourSkill)
        skills_dict[randomSkill1] += 1
        skills_dict[randomSkill2] += 1
    return (skills_dict[skill1], skills_dict[skill2], skills_dict[skill3], skills_dict[skill4])

def musicalinstrthiev(param, PlProf):
    print(f"PlProf is {PlProf}")
    musicalinstr = [tool["Name"] for tool in dnd_tools.musical_instr.values()] 
    all_tools = musicalinstr+[dnd_tools.kits["ThievKit"]["Name"]]
    print(f"All tools are: {all_tools}")

    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, alltl in enumerate(all_tools, 1):
                    print(f"{idx} - {alltl}")
                gsmit = int(input("Choose a tool to be proficient in. "))
                if gsmit == 0:
                    PlProf.append(random.choice(all_tools))
                    break
                elif 1 <= gsmit <= len(all_tools):
                    PlProf.append(all_tools[gsmit - 1])        
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 
    if param == "N": 
        PlProf.append(random.choice(all_tools))
    return PlProf

def ArtTlNavTlLang(param, PlProf, PlLang, SLANG):
    artisantools = [tool["Name"] for tool in dnd_tools.artisan_tools.values()]
    all_tools = artisantools + [dnd_tools.kits["NavTools"]["Name"]]
    all_tools_langs = all_tools + SLANG
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, atll in enumerate(all_tools_langs, 1):
                    if atll in SLANG:
                        all_tool_lang = dnd_tools.languages[atll]
                        print(f"{idx} - {all_tool_lang}")        
                arttlnavtlslang = int(input("Choose an artisan tool, navigation tools, or language to be proficient in. "))
                if arttlnavtlslang == 0:
                    rand_tool_lang = random.choice(all_tools_langs)
                    if rand_tool_lang in all_tools:
                        PlProf.append(rand_tool_lang)
                    else:
                        rand_tool_lang_full = dnd_tools.languages[rand_tool_lang]
                        PlLang.append(rand_tool_lang_full)
                        SLANG.remove(rand_tool_lang)
                    break
                elif 1 <= arttlnavtlslang <= len(all_tools_langs):
                    tool_lang = all_tools_langs[arttlnavtlslang - 1]
                    if tool_lang in all_tools:
                        PlProf.append(tool_lang)
                    else:
                        tool_lang_full = dnd_tools.languages[tool_lang]
                        PlLang.append(tool_lang_full)
                        SLANG.remove(tool_lang)      
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.")                                      
    if param == "N":
        rand_tool_lang = random.choice(all_tools_langs)
        if rand_tool_lang in all_tools:
            PlProf.append(rand_tool_lang)
        else:
            rand_tool_lang_full = dnd_tools.languages[rand_tool_lang]
            PlLang.append(rand_tool_lang_full)
            SLANG.remove(rand_tool_lang)
    return PlProf, PlLang, SLANG

def ExoticLang(param, PlLang, SLANG):
    ExoticLang = ["Abys", "Cele", "DpSp", "Drac", "Infe", "Prim", "Sylv", "Unde"]
    ExoticLangAvail = []
    for ExLang in ExoticLang:
        if ExLang in SLANG:
            ExoticLangAvail.append(ExLang)
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, exlang in enumerate(ExoticLangAvail, 1):
                    print(f"{idx} - {dnd_tools.languages[exlang]}")
                exoticlang_input = int(input("Please pick a language from the above list: "))
                if exoticlang_input == 0:
                    ExoticLangRand = random.choice(ExoticLangAvail)
                    PlLang.append(dnd_tools.languages[ExoticLangRand])
                    SLANG.remove(ExoticLangRand)
                    break
                elif 1 <= exoticlang_input <= len(ExoticLangAvail):
                    PlLang.append(dnd_tools.languages[ExoticLangAvail[exoticlang_input - 1]])
                    SLANG.remove(ExoticLangAvail[exoticlang_input - 1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 
    if param == "N":
        ExoticLangRand = random.choice(ExoticLangAvail)
        PlLang.append(dnd_tools.languages[ExoticLangRand])
        SLANG.remove(ExoticLangRand)    
    return PlLang, SLANG

def musicalinstrdisg(param, PlProf): #Fix this
    musicalinstr = [tool["Name"] for tool in dnd_tools.musical_instr.values()] 
    all_tools = musicalinstr+[dnd_tools.kits["DisgKit"]["Name"]]
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, at in enumerate(all_tools, 1):
                    print(f"{idx} - {at}")
                musid = int(input("Choose a Musical Instrument or Disguise Kit to be proficient in. "))
                if musid == 0:
                    PlProf.append(random.choice(all_tools))
                    break
                elif 1 <= musid <= len(all_tools):
                    PlProf.append(all_tools[musid - 1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 
    if param == "N":
        PlProf.append(random.choice(all_tools))
    return PlProf

def artisantoolsmusicalinstr(param, PlProf):
    artisantools = [tool["Name"] for tool in dnd_tools.artisan_tools.values()]
    musicalinstr = [tool["Name"] for tool in dnd_tools.musical_instr.values()] 
    
    all_tools = artisantools+musicalinstr

    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, alltl in enumerate(all_tools, 1):
                    print(f"{idx} - {alltl}")
                atsi = int(input("Choose an artisan tool/musical instrument to be proficient in. "))
                if atsi == 0:
                    PlProf.append(random.choice(all_tools))
                    break
                elif 1 <= atsi <= len(all_tools):
                    PlProf.append(all_tools[atsi - 1]) 
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.")            
    if param == "N":
        PlProf.append(random.choice(all_tools))
    return PlProf

def abilityscores(param, abil_scores_dict):
    # Unpack the ability scores into a list for easy manipulation
    abilities = list(abil_scores_dict.keys())
    scores = list(abil_scores_dict.values())

    def increase_random_scores(scores, increases):
        """Randomly distribute increases to scores."""
        for _ in increases: #_ is a throwaway, it does not matter what the character is, so we use a throwaway
            idx = random.randint(0, len(scores) - 1)
            scores[idx] += _

    def increase_specific_scores(scores, increases):
        """Allow user to specify which scores to increase."""
        for inc in increases:
            while True:
                try:
                    print("0 - Random")
                    for i, ability in enumerate(abilities, start=1):
                        print(f"{i} - {ability}")
                    choice = int(input(f"Choose an Ability Score to increase by {inc}. "))
                    if choice == 0:
                        idx = random.randint(0, len(scores) - 1)
                        scores[idx] += inc
                        break
                    elif 1 <= choice <= len(abilities):
                        idx = choice - 1
                        scores[idx] += inc
                        break
                    else:
                        print("Invalid choice, please choose a valid option.")
                except ValueError: #Handles non-numeric choices  
                    print("Invalid input. Please enter a number.") 
                    

    if param == "Y":
        while True:
            try:
                print("0 - Random")
                print("1 - Increase One Ability Score by 2 and One Ability Score by 1")
                print("2 - Increase Three Ability Scores by 1")
                abinc = int(input("Choose how to increase ability scores. "))

                if abinc == 1:
                    increase_specific_scores(scores, [2, 1])
                    break
                elif abinc == 2:
                    increase_specific_scores(scores, [1, 1, 1])
                    break
                elif abinc == 0:
                    if random.choice(["One by 2, One by 1", "Three by 1"]) == "One by 2, One by 1":
                        increase_random_scores(scores, [2, 1])
                    else:
                        increase_random_scores(scores, [1, 1, 1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 
    elif param == "N":
        if random.choice(["One by 2, One by 1", "Three by 1"]) == "One by 2, One by 1":
            increase_random_scores(scores, [2, 1])
        else:
            increase_random_scores(scores, [1, 1, 1])

    # Update the dictionary with the new scores
    for i, ability in enumerate(abilities):
        abil_scores_dict[ability] = scores[i]

    return abil_scores_dict

def arttool2(param, PlProf):
    artisantools = [tool['Name'] for tool in dnd_tools.artisan_tools.values()]
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, fullatname in enumerate(artisantools, 1):
                    print(f"{idx} - {fullatname}")
                arttools1 = int(input("Choose a tool to be proficient in. "))
                if arttools1 == 0:
                    PlProf.append(random.choice(artisantools))
                    break
                elif 1 <= arttools1 <= len(artisantools):
                    PlProf.append(artisantools[arttools1 - 1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 
        while True:
            try:
                print("0 - Random")
                for idx, fullatname in enumerate(artisantools, 1):
                    print(f"{idx} - {fullatname}")
                arttools2 = int(input("Choose a second tool to be proficient in. "))
                if arttools2 == 0:
                    PlProf.append(random.choice(artisantools))
                    break
                elif 1 <= arttools2 <= len(artisantools):
                    PlProf.append(artisantools[arttools2 - 1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 
    if param == "N":           
        # Ensure unique random picks
        selected_tools = random.sample(artisantools, 2)
        PlProf.extend(selected_tools) 
    return PlProf     

def singleabilityscore(param, abil_scores_dict):
    """Boost one ability score by 1."""
    abilities = list(abil_scores_dict.keys())
    
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for i, ability in enumerate(abilities, 1):
                    print(f"{i} - {ability}")
                choice = int(input("Choose a score to increase by 1. "))
                if choice == 0:
                    idx = random.randint(0, len(abilities) - 1)
                    # Increase the selected ability score
                    selected_ability = abilities[idx]
                    abil_scores_dict[selected_ability] += 1                    
                    break
                elif 1 <= choice <= len(abilities):
                    idx = choice - 1  # Convert 1-based input to 0-based index
                    # Increase the selected ability score
                    selected_ability = abilities[idx]
                    abil_scores_dict[selected_ability] += 1                    
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 

    if param == "N":
        idx = random.randint(0, len(abilities) - 1)
        # Increase the selected ability score
        selected_ability = abilities[idx]
        abil_scores_dict[selected_ability] += 1

    return abil_scores_dict   

def skillprof2(param, SkillsProf):
    skills = list(dnd_tools.skills.values())
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, skill in enumerate(skills, 1):
                    print(f"{idx} - {skill}")
                sklprof1 = int(input("Choose a skill to be proficient in. "))
                if sklprof1 == 0:
                    SkillsProf.append(random.choice(skills))
                    break
                elif 1 <= sklprof1 <= len(skills):
                    SkillsProf.append(skills[sklprof1 - 1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 
        while True:
            try:
                print("0 - Random")
                for idx, skill in enumerate(skills, 1):
                    print(f"{idx} - {skill}")
                sklprof2 = int(input("Choose a second skill to be proficient in. "))
                if sklprof2 == 0:
                    SkillsProf.append(random.choice(skills))
                    break
                elif 1 <= sklprof2 <= len(skills):
                    SkillsProf.append(skills[sklprof2 - 1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 
    if param == "N":
        SkillsProf.append(random.choice(skills))
        SkillsProf.append(random.choice(skills))
    return SkillsProf

def toolprof(param, PlProf, ToolList):
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, tool in enumerate(ToolList, 1):
                    print(f"{idx} - {tool}")
                tlchoice = int(input("Please pick a tool from the above list. "))
                if tlchoice == 0:
                    PlProf.append(random.choice(ToolList))
                    break
                elif 1 <= tlchoice == 1 <= len(ToolList):
                    PlProf.append(ToolList[tlchoice - 1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 
    if param == "N":
        PlProf.append(random.choice(ToolList)) 
    return PlProf    

def toolskillprof(param, PlProf, SkillsProf):
    # Combine skills and tools into a single list
    skills = list(dnd_tools.skills.values())  # Get all skill names
    tools = [tool["Name"] for tool in dnd_tools.artisan_tools.values()]  # Get all tool names
    toolskills = tools + skills  # Combine tools and skills
    
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, name in enumerate(toolskills, 1):
                    print(f"{idx} - {name}")
                tlsklchoice = int(input("Choose a tool or skill to be proficient in: "))
                if tlsklchoice == 0:
                    random_choice = random.choice(toolskills)
                    if random_choice in tools:
                        PlProf.append(random_choice)
                    else:
                        SkillsProf.append(random_choice)
                    break
                elif 1 <= tlsklchoice <= len(toolskills):
                    choice = toolskills[tlsklchoice - 1]
                    if choice in tools:
                        PlProf.append(choice)
                    else:
                        SkillsProf.append(choice)
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 
    
    if param == "N":
        for _ in range(2):  # Two random proficiencies
            random_choice = random.choice(toolskills)
            if random_choice in tools:
                PlProf.append(random_choice)
            else:
                SkillsProf.append(random_choice)
    
    return PlProf, SkillsProf

def martwepprof(param, PlProf):
    martialweapons = [martwep["Name"] for martwep in dnd_tools.martial_weapons.values()]
    for item in PlProf:
        if item in martialweapons:
            martialweapons.remove(item)
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, mw in enumerate(martialweapons, 1):
                    print(f"{idx} - {mw}")
                choice = int(input("Choose your martial weapon proficiency: "))
                if choice == 0:  # Random choice
                    choice = random.choice(martialweapons)
                    PlProf.append(choice)
                    break
                elif 1 <= choice <= len(martialweapons):
                    choice = martialweapons[choice - 1]
                    PlProf.append(choice)
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 

    if param == "N":
        # Randomly select one weapon
        PlProf.append(random.choice(martialweapons))
    
    return PlProf

def vedsixskillprof(param, Notes, SkillsProf, SkillsList):
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, skill in enumerate(SkillsList, 1):
                    print(f"{idx} - {skill}")
                profsklsix = int(input("Choose a skill to be proficient in. "))
                if profsklsix == 0:
                    randskillslist = random.choice(SkillsList)
                    SkillsProf.append(randskillslist)
                    Notes["Vedalken Skill"] = f"Whenever you make an ability check with {randskillslist}, roll a d4 and add the number rolled to the check's total."
                    break
                elif 1 <= profsklsix <= len(SkillsList):
                    SkillsProf.append([SkillsList[profsklsix - 1]])
                    Notes["Vedalken Skill"] = f"Whenever you make an ability check with {SkillsList[profsklsix - 1]}, roll a d4 and add the number rolled to the check's total."
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 
    if param == "N": 
        randskillslist = random.choice(SkillsList)
        SkillsProf.append(randskillslist)
        Notes["Vedalken Skill"] = f"Whenever you make an ability check with {randskillslist}, roll a d4 and add the number rolled to the check's total."
    return Notes, SkillsProf

def vedartisantools(param, PlProf):
    tools = [arttool["Name"] for arttool in dnd_tools.artisan_tools.values()]
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, at in enumerate(tools, 1):
                    print(f"{idx} - {at}")
                arttool = int(input("Choose an artisan tool to be proficient in. "))
                if arttool == 0:
                    PlProf.append(random.choice(tools) + "; " + "Whenever you make an ability check with this tool, roll a d4 and add the number rolled to the check's total.")
                    break
                elif 1 <= arttool <= len(tools):
                    PlProf.append(tools[arttool - 1] + "; " + "Whenever you make an ability check with this tool, roll a d4 and add the number rolled to the check's total.")
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 
    if param == "N":           
        PlProf.append(random.choice(tools) + "; " + "Whenever you make an ability check with this tool, roll a d4 and add the number rolled to the check's total.")
    return PlProf

def skillprof(param, SkillsProf):
    skills = list(dnd_tools.skills.values())
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, skill in enumerate(skills, 1):
                    print(f"{idx} - {skill}")
                sklprof = int(input("Choose a skill to be proficient in. "))
                if sklprof == 0:
                    SkillsProf.append(random.choice(skills))
                    break
                elif 1 <= sklprof <= len(skills):
                    SkillsProf.append(skills[sklprof - 1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 
    if param == "N":
        SkillsProf.append(random.choice(skills))
    return SkillsProf

def fourskillsfromlist(param, SkillsProf, SkillsList):
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for i, skill in enumerate(SkillsList, 1):
                    print(f"{i} - {skill}")
                skillone = int(input("Which is the first skill to be proficient in? "))
                if skillone == 0:
                    SkillsProf.append(random.choice(SkillsList))
                    break
                elif 1 <= skillone <= len(SkillsList):
                    SkillsProf.append(SkillsList[skillone-1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 
        while True:
            try:
                print("0 - Random")
                for i, skill in enumerate(SkillsList, 1):
                    print(f"{i} - {skill}")                
                skilltwo = int(input("Which is the second skill to be proficient in? "))
                if skilltwo == 0:
                    SkillsProf.append(random.choice(SkillsList))
                    break
                elif 1 <= skilltwo <= len(SkillsList):
                    SkillsProf.append(SkillsList[skilltwo-1]) 
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 
        while True:
            try:
                print("0 - Random")
                for i, skill in enumerate(SkillsList, 1):
                    print(f"{i} - {skill}")                
                skillthree = int(input("Which is the third skill to be proficient in? "))
                if skillthree == 0:
                    SkillsProf.append(random.choice(SkillsList))
                    break
                elif 1 <= skillthree <= len(SkillsList):
                    SkillsProf.append(SkillsList[skillthree-1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 
        while True:
            try:
                print("0 - Random")
                for i, skill in enumerate(SkillsList, 1):
                    print(f"{i} - {skill}")                
                skillfour = int(input("Which is the fourth skill to be proficient in? "))
                if skillfour == 0:
                    SkillsProf.append(random.choice(SkillsList))
                    break
                elif 1 <= skillfour <= len(SkillsList):
                    SkillsProf.append(SkillsList[skillfour-1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 
    if param == "N":
        SkillsProf.extend(random.sample(SkillsList, 4))
    return SkillsProf

def threeskillsfromlist(param, SkillsProf, SkillsList):
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for i, skill in enumerate(SkillsList, 1):
                    print(f"{i} - {skill}")
                skillone = int(input("Which is the first skill to be proficient in? "))
                if skillone == 0:
                    SkillsProf.append(random.choice(SkillsList))
                    break
                elif 1 <= skillone <= len(SkillsList):
                    SkillsProf.append(SkillsList[skillone-1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 
        while True:
            try:
                print("0 - Random")
                for i, skill in enumerate(SkillsList, 1):
                    print(f"{i} - {skill}")
                skilltwo = int(input("Which is the second skill to be proficient in? "))
                if skilltwo == 0:
                    SkillsProf.append(random.choice(SkillsList))
                    break
                elif 1 <= skilltwo <= len(SkillsList):
                    SkillsProf.append(SkillsList[skilltwo-1])  
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 
        while True:
            try:  
                print("0 - Random")
                for i, skill in enumerate(SkillsList, 1):
                    print(f"{i} - {skill}")
                skillthree = int(input("Which is the third skill to be proficient in? "))
                if skillthree == 0:
                    SkillsProf.append(random.choice(SkillsList))
                    break
                elif 1 <= skillthree <= len(SkillsList):
                    SkillsProf.append(SkillsList[skillthree-1])
                    break  
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.")                     
    if param == "N":
        SkillsProf.extend(random.sample(SkillsList, 3))
    return SkillsProf

def twoskillsfromlist(param, SkillsProf, SkillsList):
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for i, skill in enumerate(SkillsList, 1):
                    print(f"{i} - {skill}")
                skillone = int(input("Which is the first skill to be proficient in? "))
                if skillone == 0:
                    SkillsProf.append(random.choice(SkillsList))
                    break
                elif 1 <= skillone <= len(SkillsList):
                    SkillsProf.append(SkillsList[skillone-1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.") 
        while True:
            try:
                print("0 - Random")
                for i, skill in enumerate(SkillsList, 1):
                    print(f"{i} - {skill}")
                skilltwo = int(input("Which is the second skill to be proficient in? "))
                if skilltwo == 0:
                    SkillsProf.append(random.choice(SkillsList))
                    break
                elif 1 <= skilltwo <= len(SkillsList):
                    SkillsProf.append(SkillsList[skilltwo-1])   
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError: #Handles non-numeric choices  
                print("Invalid input. Please enter a number.")          
    if param == "N":
        SkillsProf.extend(random.sample(SkillsList, 2))
    return SkillsProf

def oneskillfromlist(param, SkillsProf, SkillsList):
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for i, skill in enumerate(SkillsList, 1):
                    print(f"{i} - {skill}")
                skillone = int(input("Which skill would you like to be proficient in? "))
                if skillone == 0:
                    SkillsProf.append(random.choice(SkillsList))
                    break
                elif 1 <= skillone <= len(SkillsList):
                    SkillsProf.append(SkillsList[skillone - 1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    elif param == "N":
        SkillsProf.append(random.choice(SkillsList))
    return SkillsProf

def twosimpleweapons(param, EQP):
    SimpleWeaponsKeys = list(dnd_tools.simple_weapons.keys())
    SimpleWeapons = [wep["Name"] for wep in dnd_tools.simple_weapons.values()]
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for i, sw in enumerate(SimpleWeapons,1):
                    print(f"{i} - {sw}")
                simpleweapon1 = int(input("Which simple weapon do you want to be proficient in first? "))
                if simpleweapon1 == 0:
                    SWRand = random.choice(SimpleWeaponsKeys)
                    EQP.append(dnd_tools.simple_weapons[SWRand].copy())
                    break
                elif 1 <= simpleweapon1 <= len(SimpleWeapons):
                    SimpleWep1 = SimpleWeaponsKeys[simpleweapon1 - 1]
                    EQP.append(dnd_tools.simple_weapons[SimpleWep1].copy())
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        while True:
            try:
                print("0 - Random")
                for i, sw in enumerate(SimpleWeapons,1):
                    print(f"{i} - {sw}")
                simpleweapon2 = int(input("Which simple weapon do you want to be proficient in second? "))
                if simpleweapon2 == 0:
                    SWRand2 = random.choice(SimpleWeapons)
                    EQP.append(dnd_tools.simple_weapons[SWRand2].copy())  
                    break
                elif 1 <= simpleweapon2 <= len(SimpleWeapons):
                    SimpleWep2 = SimpleWeaponsKeys[simpleweapon2 - 1]
                    EQP.append(dnd_tools.simple_weapons[SimpleWep2].copy())
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    if param == "N":
        SWRand = random.choice(SimpleWeaponsKeys)
        SWRand2 = random.choice(SimpleWeaponsKeys)
        EQP.append(dnd_tools.simple_weapons[SWRand].copy())
        EQP.append(dnd_tools.simple_weapons[SWRand2].copy())
    return EQP

def skillprof3(param, SkillsProf):
    skills = list(dnd_tools.skills.values())
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, skl in enumerate(skills, 1):
                    print(f"{idx} - {skl}")
                sklprof1 = int(input("Choose a skill to be proficient in. "))
                if sklprof1 == 0:
                    SkillsProf.append(random.choice(skills))
                    break
                elif 1 <= sklprof1 <= len(skills):
                    SkillsProf.append(skills[sklprof1-1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        while True:
            try:
                print("0 - Random")
                for idx, skl in enumerate(skills, 1):
                    print(f"{idx} - {skl}")
                sklprof2 = int(input("Choose a second skill to be proficient in. "))
                if sklprof2 == 0:
                    SkillsProf.append(random.choice(skills))
                    break
                elif 1 <= sklprof2 <= len(skills):
                    SkillsProf.append(skills[sklprof2-1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        while True:
            try:
                print("0 - Random")
                for idx, skl in enumerate(skills, 1):
                    print(f"{idx} - {skl}")
                sklprof3 = int(input("Choose a third skill to be proficient in. "))
                if sklprof3 == 0:
                    SkillsProf.append(random.choice(skills))
                    break
                elif 1 <= sklprof3 <= len(skills):
                    SkillsProf.append(skills[sklprof3-1])    
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")    
    if param == "N":
        SkillsProf.append(random.choice(skills))
        SkillsProf.append(random.choice(skills))
        SkillsProf.append(random.choice(skills))
    return SkillsProf    

def onehandedweaponprof(param, PlProf):
    SimpleWeapons = list(dnd_tools.simple_weapons.keys())
    MartialWeapons = list(dnd_tools.martial_weapons.keys())
    AllWeapons = MartialWeapons + SimpleWeapons
    ohw_keys = ["Club", "Dagger", "Handaxe", "Javelin", "LightHammer", "Mace", "Quarterstaff", "Sickle", "Spear", 
                "Battleaxe", "Flail", "Lance", "Longsword", "Morningstar", "Rapier", "Scimitar", "Shortsword", 
                "Trident", "WarPick", "Warhammer", "Whip"]
    OneHandedWeapons = [key for key in AllWeapons if key in ohw_keys]
    OneHandedWeaponsNames = [
        dnd_tools.simple_weapons[key]["Name"] if key in dnd_tools.simple_weapons 
        else dnd_tools.martial_weapons[key]["Name"] 
        for key in OneHandedWeapons
    ]
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for wiz, ohw in enumerate(OneHandedWeaponsNames, 1):
                    print(f"{wiz} - {ohw}")
                ohwinput = int(input("Choose a one-handed melee weapon to be gain proficiency in. "))
                if ohwinput == 0:
                    Ohw_choice_rand = random.choice(OneHandedWeaponsNames)
                    PlProf.append(Ohw_choice_rand)
                    break
                elif 1 <= ohwinput <= len(OneHandedWeaponsNames):
                    PlProf.append(OneHandedWeaponsNames[ohwinput-1])
                    break
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    if param == "N":
        Ohw_choice_rand = random.choice(OneHandedWeaponsNames)
        PlProf.append(Ohw_choice_rand)
    return PlProf


def determine_modifier(casting_class):
    class_to_stat = {
        "Warlock": "CHA",
        "Sorcerer": "CHA",
        "Bard": "CHA",
        "Wizard": "INT",
        "Artificer": "INT",
        "Cleric": "WIS",
        "Druid": "WIS",
        "Paladin": "CHA",
        "Ranger": "WIS"
    }

    return class_to_stat.get(casting_class, "")

def choose_spells(player, param):
    for i, cl in enumerate(player.Class):
        spelllistkeys = list(player.spelllist.keys())
        for sp in spelllistkeys:               
            using_class = player.spelllist[sp].get('Using Class', None)
            spell_list = player.spelllist[sp]['Spell List']
            if not using_class:
                using_class = random.choice(player.Class)                
            if using_class not in spell_list:
                spell_list.append(using_class) #This for sp block adds using class to the class list of the spell if its not in there  
        spell_levels = [
            "1st Level Spell", "2nd Level Spell", "3rd Level Spell",
            "4th Level Spell", "5th Level Spell", "6th Level Spell",
            "7th Level Spell", "8th Level Spell", "9th Level Spell"
        ]
        ordinal_to_number = {
            "1st": 1, "2nd": 2, "3rd": 3,
            "4th": 4, "5th": 5, "6th": 6,
            "7th": 7, "8th": 8, "9th": 9
        }      

        cantrips_known = player.notes.get(f"{cl} Cantrips Known", 0)
        class_cantrips = []        
        for dnd_sp in dnd_spells.spells:
            dnd_spell = dnd_spells.spells[dnd_sp]
            if ((dnd_spell["Level"] == 0) and (cl in dnd_spell["Spell List"]) and (dnd_sp not in player.spelllist)): 
                class_cantrips.append(dnd_sp)
        spells_known = player.notes.get(f"{cl} Spells Known", 6) #6 is the default start for a Wizard, really the # is the length of their spellbook, once i write the ability for wizards to write a spellbook, I will put the spell portion in an if cl is not "Wizard" check
        class_spells = []
        if cl == "Warlock":
            spellslot_level = player.notes[f"{cl} Spell Slot Level"]
            print(f"Spellslot Level is {spellslot_level}")
            highest_ss = ordinal_to_number.get(spellslot_level)
        else:
            spell_slots_ordinal = []
            for key in player.notes:
                for spell_level in spell_levels:
                    if f"{cl} {spell_level} Slots Known" in key:
                        # Extract the ordinal ("1st", "2nd", etc.)
                        first_word = key.split()[1]
                        if first_word in ordinal_to_number and player.notes[key] > 0:
                            spell_slots_ordinal.append(ordinal_to_number[first_word])
            if len(spell_slots_ordinal) != 0:
                highest_ss = max(spell_slots_ordinal)
            else:
                continue        
        for dnd_sp in dnd_spells.spells:
            dnd_spell = dnd_spells.spells[dnd_sp]
            if (
                0 < dnd_spell["Level"] <= highest_ss and
                cl in dnd_spell["Spell List"] and
                dnd_sp not in player.spelllist
            ): 
                class_spells.append(dnd_sp)         
        if param == "Y":
            cantrips_known_while = cantrips_known
            #print(f"You can know {cantrips_known} cantrips") #debug
            while cantrips_known_while != 0:
                try:
                    print("0 - Random")
                    for idx, cc in enumerate(class_cantrips, 1):
                        print(f"{idx} - {cc}")
                    choice = int(input("Which cantrip would you like to add to your spelllist? "))
                    if choice == 0:
                        sp_choice = random.choice(class_cantrips)
                        spell_choice = dnd_spells.spells[sp_choice].copy()
                        spell_choice["Original Name"] = spell_choice['Name']
                        if not spell_choice.get('Using Class'):
                            spell_choice["Using Class"] = cl
                        spell_choice["Modifier"] = determine_modifier(cl)                        
                        spell_choice['Name'] = f"{spell_choice['Name']} ({cl} Cantrip)"
                        player.spelllist[spell_choice['Name']] = spell_choice
                        class_cantrips.remove(sp_choice)
                        cantrips_known_while -= 1
                    elif 1 <= choice <= len(class_cantrips):
                        sp_choice = class_cantrips[choice - 1]
                        spell_choice = dnd_spells.spells[sp_choice].copy()
                        spell_choice["Original Name"] = spell_choice['Name']
                        spell_choice["Using Class"] = cl
                        spell_choice["Modifier"] = determine_modifier(cl)                        
                        spell_choice['Name'] = f"{spell_choice['Name']} ({cl} Cantrip)"
                        player.spelllist[spell_choice['Name']] = spell_choice
                        class_cantrips.remove(sp_choice)
                        cantrips_known_while -= 1                        
                    else:
                        print("Invalid choice, please choose a valid option.")
                except ValueError:
                    print("Invalid input. Please enter a number.")                          
            spells_known_while = spells_known
            #print(f"You can know {spells_known} spells") #debug
            while spells_known_while != 0:
                try:
                    print("0 - Random")
                    for idx, cs in enumerate(class_spells, 1):
                        print(f"{idx} - {cs}")
                    choice = int(input("Which spell would you like to add to your spelllist? "))
                    if choice == 0:
                        sp_choice = random.choice(class_spells)
                        spell_choice = dnd_spells.spells[sp_choice].copy()
                        spell_choice["Original Name"] = spell_choice['Name']
                        spell_choice["Using Class"] = cl
                        spell_choice["Modifier"] = determine_modifier(cl)
                        spell_choice['Name'] = f"{spell_choice['Name']} ({cl} Spell)"
                        player.spelllist[spell_choice['Name']] = spell_choice
                        class_spells.remove(sp_choice)
                        spells_known_while -= 1
                    elif 1 <= choice <= len(class_spells):
                        sp_choice = class_spells[choice - 1]
                        spell_choice = dnd_spells.spells[sp_choice].copy()
                        spell_choice["Original Name"] = spell_choice['Name']
                        spell_choice["Using Class"] = cl
                        spell_choice["Modifier"] = determine_modifier(cl)
                        spell_choice['Name'] = f"{spell_choice['Name']} ({cl} Spell)"
                        player.spelllist[spell_choice['Name']] = spell_choice
                        class_spells.remove(sp_choice)
                        spells_known_while -= 1                        
                    else:
                        print("Invalid choice, please choose a valid option.")
                except ValueError:
                    print("Invalid input. Please enter a number.")                 
        elif param == "N":
            random_cantrips = random.sample(class_cantrips, min(cantrips_known, len(class_cantrips)))
            random_spells = random.sample(class_spells, min(spells_known, len(class_spells)))
            print(f"Random cantrips are:\n{random_cantrips}")
            print(f"Random cantrips are:\n{random_spells}")
            for spell_name in random_cantrips:
                spell = dnd_spells.spells[spell_name].copy()
                spell["Original Name"] = spell['Name']
                spell["Using Class"] = cl
                spell["Modifier"] = determine_modifier(cl)                
                spell['Name'] = f"{spell['Name']} ({cl} Cantrip)"
                player.spelllist[spell['Name']] = spell

            for spell_name in random_spells:
                spell = dnd_spells.spells[spell_name].copy()
                spell["Original Name"] = spell['Name']
                spell["Using Class"] = cl
                spell["Modifier"] = determine_modifier(cl)                
                spell['Name'] = f"{spell['Name']} ({cl} Spell)"
                player.spelllist[spell['Name']] = spell   
        spelllistkeys = list(player.spelllist.keys())
        spellllistkeys_all_before = '\n'.join(sp for sp in spelllistkeys) #debug
        #print(f"{player.name} knows, before modification:" + "\n" + f"{spellllistkeys_all_before}") #debug
        for sp in spelllistkeys:
            #print(f"{player.name} now knows {sp}") #debug
            spell = player.spelllist[sp]
            spell['Attack Type'] = "Spell"
            #print(f"Spell before hand, is {spell}") #debug
            if cl == spell["Using Class"] or spell['Flavor'] == True: #added this line to stop wizard from overwriting warlock
                if spell.get('Effect', {}).get('Type') == 'Damage':
                    spell_level = spell.get('Level', None)
                    spell['Proficient'] = True
                    player.attacksspellcasting[sp] = spell.copy() 
                    player.actions[sp] = spell.copy() 
                    #print(f"This spell, after modifying, is: {player.actions[sp]}")
                    #print(f"{player.attacksspellcasting[sp]['Name']} learned, added to attacks") #debug
                else:
                    player.actions[sp] = spell
                    #player.actions[sp]['Name'] = f"{spell['Name']} ({cl} {spell_levels[lvl]})"
            #print(f"Spell after hand is {spell}") #debug
        #spelllistkeys = list(player.spelllist.keys())
        #spellllistkeys_all_after = '\n'.join(sp for sp in spelllistkeys)
        #print(f"{player.name} knows, after:" + "\n" + f"{spellllistkeys_all_after}") #This block of 3 is a debug block
                 
def switch_spells(player, cantrip, count):
    spell_levels = [
        "1st Level Spell", "2nd Level Spell", "3rd Level Spell",
        "4th Level Spell", "5th Level Spell", "6th Level Spell",
        "7th Level Spell", "8th Level Spell", "9th Level Spell"
    ]
    ordinal_to_number = {
        "1st": 1, "2nd": 2, "3rd": 3,
        "4th": 4, "5th": 5, "6th": 6,
        "7th": 7, "8th": 8, "9th": 9
    }       
    for cl in player.Class:
        class_spells = []
        if cl == "Warlock":
            spellslot_level = player.notes[f"{cl} Spell Slot Level"]
            print(f"Spellslot Level is {spellslot_level}")
            highest_ss = ordinal_to_number.get(spellslot_level)
        else:
            spell_slots_ordinal = []
            for key in player.notes:
                for spell_level in spell_levels:
                    if f"{cl} {spell_level} Slots Known" in key:
                        # Extract the ordinal ("1st", "2nd", etc.)
                        first_word = key.split()[1]
                        if first_word in ordinal_to_number and player.notes[key] > 0:
                            spell_slots_ordinal.append(ordinal_to_number[first_word])
            highest_ss = max(spell_slots_ordinal)             
        spelllistkeys = list(player.spelllist.keys())
        class_cantrips = []        
        for dnd_sp in dnd_spells.spells:
            dnd_spell = dnd_spells.spells[dnd_sp]
            if (
                dnd_spell["Level"] == 0 and
                cl in dnd_spell["Spell List"] and
                not any(dnd_sp in sp for sp in player.spelllist)
            ): 
                class_cantrips.append(dnd_sp)
        for dnd_sp in dnd_spells.spells:
            dnd_spell = dnd_spells.spells[dnd_sp]
            #print(f"Dnd spell is {dnd_spell}") #debug
            #print(f"Highest spell slot is {highest_ss}") #debug
            #print(f"Dnd sp is {dnd_sp}") #debug
            #print(f"Their spelllist is {player.spelllist}") #debug
            if (
                0 < dnd_spell["Level"] <= highest_ss and
                cl in dnd_spell["Spell List"] and
                not any(dnd_sp in sp for sp in player.spelllist)
            ): 
                class_spells.append(dnd_sp)                   
        spells_switch = []
        if cantrip == True:
            for sp in spelllistkeys:
                full_spell = player.spelllist[sp]
                if full_spell['Level'] == 0:
                    spells_switch.append(sp)
        elif cantrip == False:
            for sp in spelllistkeys:
                full_spell = player.spelllist[sp]
                if full_spell['Level'] != 0:
                    spells_switch.append(sp)                    
        #print(f"Currently you know:\n{'\n'.join(sp for sp in spelllistkeys)}") #debug
        if cantrip == True:
            spell_cantrip = "Cantrip" 
            if count > 1:
                spell_cantrip = "Cantrips"
        elif cantrip == False:
            spell_cantrip = "Spell" 
            if count > 1:
                spell_cantrip = "Spells"                
        print(f"You can switch out {count} {spell_cantrip}")
        print(f"Spells_switch looks like {spells_switch}")
        #Gonna comment this while loop for the moment so we can debug this
        while count > 0:
            try:
                print("0 - Skip exchanging spell")
                for idx, splk in enumerate(spells_switch, 1):
                    print(f"{idx} - {splk}")
                choice = int(input("Which spell would you like to switch out, or would you? "))
                if choice == 0:
                    break
                elif 1 <= choice <= len(spells_switch):
                    if cantrip == True:
                        known_cantrip = spells_switch[choice - 1]
                        known_full_cantrip = player.spelllist[known_cantrip]
                        while True:
                            try:
                                for idx, can in enumerate(class_cantrips, 1):
                                    print(f"{idx} - {can}")
                                switch_choice = int(input("Pick a new spell. "))
                                if 1 <= switch_choice <= len(class_cantrips):
                                    replace_cantrip = class_cantrips[switch_choice - 1]
                                    replace_full_cantrip = dnd_spells.spells[replace_cantrip]
                                    del player.spelllist[known_full_cantrip["Name"]]
                                    replace_full_cantrip["Original Name"] = replace_full_cantrip["Name"]
                                    replace_full_cantrip["Modifier"] = determine_modifier(cl)
                                    replace_full_cantrip["Name"] = f"{replace_full_cantrip['Name']} ({cl} Cantrip)"
                                    player.spelllist[replace_full_cantrip["Name"]] = replace_full_cantrip.copy()
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError:
                                print("Invalid input. Please enter a number.")                                   
                    elif cantrip == False:
                        #print(f"Class spells looks like {class_spells}") #debug
                        known_spell = spells_switch[choice - 1]
                        #print(f"You chose known spell to be {known_spell}") #debug
                        known_full_spell = player.spelllist[known_spell]
                        #print(f"So the full spell is {known_full_spell}") #debug
                        while True:
                            try:
                                for idx, clsp in enumerate(class_spells, 1):
                                    print(f"{idx} - {clsp}")
                                switch_choice = int(input("Pick a new spell. "))
                                if 1 <= switch_choice <= len(class_spells):
                                    replace_spell = class_spells[switch_choice - 1]
                                    replace_full_spell = dnd_spells.spells[replace_spell]
                                    del player.spelllist[known_full_spell["Name"]]
                                    replace_full_spell["Original Name"] = replace_full_spell["Name"]
                                    replace_full_spell["Modifier"] = determine_modifier(cl)
                                    replace_full_spell["Name"] = f"{replace_full_spell['Name']} ({cl} Cantrip)"
                                    player.spelllist[replace_full_spell["Name"]] = replace_full_spell.copy()
                                    break
                                else:
                                    print("Invalid choice, please choose a valid option.")
                            except ValueError:
                                print("Invalid input. Please enter a number.")                                   
                    count -= 1
                else:
                    print("Invalid choice, please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

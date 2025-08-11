import random
import dnd_tools

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
    artisantools = [tool["Name"] for tool in dnd_tools.artisan_tools.values()]
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
    musicalinstr = [tool["Name"] for tool in dnd_tools.musical_instr.values()] 
    all_tools = musicalinstr+[dnd_tools.kits["ThievKit"]["Name"]]

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

def ArtTlNavTlLang(param, PlProf, PlLang, SLANG):
    artisantools = [tool["Name"] for tool in dnd_tools.artisan_tools.values()]
    all_tools = artisantools + [dnd_tools.kits["NavTools"]["Name"]]
    all_tools_langs = all_tools + SLANG
    if param == "Y":
        while True:
            try:
                print("0 - Random")
                for idx, atll in enumerate(all_tools_langs, 1):
                    if attl in SLANG:
                        attl = dnd_tools.languages[attl]
                    print(f"{idx} - {atll}")        
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
    artisantools = list(dnd_tools.artisan_tools.keys())
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

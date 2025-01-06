import random
import dnd_tools
from dnd_languagesskills import *

def dice(dicenum):
    # Rolls a dice with dicenum sides
    result = random.randint(1, dicenum)
    return result

def dndCharGenRace(param, player):
    #Add Race info for Hollow One
    ##Remember, now HolOne is a boolean
    #Add info for Lineage
    if param == "Y":
        HlwOne = input("Do you want to be a Hollow One (Zombie)? Y/N ").strip().lower()
        if HlwOne in {"y", "ye", "yes"}:
            player.hollowone = True
        elif HlwOne in {"n", "no"}:
            player.hollowone = False
    if param == "N":
        player.hollowone = random.choice([True, False])
    subraces = {
        "Aasimar": ["Fallen Aasimar", "Protector Aasimar", "Scourge Aasimar"],
        "Cervan": ["Grove Cervan", "Pronghorn Cervan"],
        "Corginian": ["Cardigan Corginian", "Pembroke Corginian"],
        "Corvum": ["Dusk Corvum", "Kindled Corvum"],
        "Dragonborn": ["Black Scale Dragonborn", "Blue Scale Dragonborn", "Brass Scale Dragonborn", "Bronze Scale Dragonborn", 
                    "Chromatic Dragonborn", "Copper Scale Dragonborn", "Draconblood Dragonborn", "Gem Dragonborn", 
                    "Gold Scale Dragonborn", "Green Scale Dragonborn", "Metallic Dragonborn", "Red Scale Dragonborn", 
                    "Ravenite Dragonborn", "Silver Scale Dragonborn", "White Scale Dragonborn"],
        "Dwarf": ["Duergar", "Hill Dwarf", "Mountain Dwarf"],
        "Elf": ["Astral Elf", "Dark Elf", "Eladrin", "High Elf", "Sea Elf", "Shadar-kai", "Wood Elf"],
        "Gallus": ["Bright Gallus", "Huden Gallus"],
        "Genasi": ["Air Genasi", "Earth Genasi", "Fire Genasi", "Water Genasi"],
        "Gith": ["Githyanki", "Githzerai"],
        "Gnome": ["Forest Gnome", "Rock Gnome", "Svirfneblin (Deep) Gnome"],
        "Halfling": ["Ghostwise Halfling", "Lightfoot Halfling", "Stout Halfling"],
        "Half-Elf": ["Half-Elf: Aquatic Elf Descent", "Half-Elf: Drow Descent", "Half-Elf: Moon Elf Descent", 
                    "Half-Elf: Sun Elf Descent", "Half-Elf: Wood Elf Descent"],
        "Human": ["Human", "Variant Human"],
        "Luma": ["Sable Luma", "Sera Luma"],
        "Raptor": ["Maran Raptor (Bird)", "Mistral Raptor (Bird)"],
        "Sharkin": ["Blue Sharkin", "Basking Sharkin", "Bull Sharkin", "Cookie Cutter Sharkin", "Goblin Sharkin", 
                    "Hammerhead Sharkin", "Leopard Sharkin", "Mako Sharkin", "Nurse Sharkin", "Thresher Sharkin", 
                    "Tiger Sharkin", "Whale Sharkin", "Great White Sharkin", "Cladoselache", "Cretoxyrhina", 
                    "Edestus", "Helicoprion", "Hybodus", "Megalodon", "Ptychodus", "Scapanorhynchus", "Stethacanthus", 
                    "Xenacanthus"],
        "Shifter": ["Beasthide Shifter", "Longtooth Shifter", "Swiftstride Shifter", "Wildhunt Shifter"],
        "Strig": ["Stout Strig", "Swift Strig"],
        "Tiefling": ["Asmodeus Subject Tiefling", "Baalzebul Subject Tiefling", "Dispater Subject Tiefling", 
                    "Fierna Subject Tiefling", "Glasya Subject Tiefling", "Levistus Subject Tiefling", 
                    "Mammon Subject Tiefling", "Mephistopheles Subject Tiefling", "Zariel Subject Tiefling"]
    }
    actual_races = [
        "Aarakocra", "Aasimar", "Autognome", "Bugbear", "Centaur", "Cervan", "Changeling", "Corginian", 
        "Corvum", "Dhampir", "Disembodied", "Dragonborn", "Dwarf", "Elf", "Fairy", "Firbolg", "Gallus", 
        "Genasi", "Giff", "Gith", "Gnome", "Goblin", "Goliath", "Grung", "Hadozee", "Half-Elf", "Halfling", 
        "Half-Orc", "Harengon", "Hedge", "Hexblood", "Hobgoblin", "Human", "Jerbeen", "Kalashtar", "Kender", 
        "Kenku", "Kobold", "Leonin", "Lizardfolk", "Locathah", "Loxodon", "Luma", "Mapach", "Minotaur", 
        "Orc", "Owlin", "Plasmoid", "Raptor", "Reborn", "Satyr", "Sharkin", "Shifter", "Simic Hybrid", 
        "Strig", "Tabaxi", "Thri-Kreen", "Tiefling", "Tortle", "Triton", "Vedalken", "Verdan", "Vulpin", 
        "Warforged", "Wechselkind", "Yuan-ti"
    ]


    commented_races = [
        "Aarakocra (Bird-People)", "Aasimar (Celestial-Humans)", "Autognome (Robot-Gnomes)", "Bugbear (Large-Goblins)",
        "Centaur (Horse-People)", "Cervan (Deer-Folk)", "Changeling (Shape-shifters)", "Corginian (Dog-People)",
        "Corvum (Crow-Folk)", "Dhampir (Vampire-Hybrids)", "Disembodied (Ghost-People)", "Dragonborn (Dragon-Humans)",
        "Dwarf", "Elf", "Fairy", "Firbolg (Giant-Folk)", "Gallus (Chicken-Folk)",
        "Genasi", "Giff (Hippo-People)", "Gith (Demon-Drow)", "Gnome",
        "Goblin", "Goliath (Mountain-Giants)", "Grung (Frog-People)", "Hadozee (Lemur-People)",
        "Half-Elf", "Halfling (Small-Folk)", "Half-Orc", 
        "Harengon (Rabbit-People)", "Hedge (Hedgehog-Folk)", "Hexblood (Witch-People)", "Hobgoblin (Militaristic-Goblins)",
        "Human", "Jerbeen (Mouse-Folk)", "Kalashtar (Human-Spirit-Compound)", "Kender (Innocent-Humans)",
        "Kenku (Crow-People)", "Kobold (Small-Dragonkin)", "Leonin (Lion-People)", "Lizardfolk (Reptilian-Folk)",
        "Locathah (Fish-Folk)", "Loxodon (Elephant-People)", "Luma (Dove-Folk)", "Mapach (Raccoon-People)",
        "Minotaur (Bull-Humanoids)", "Orc", "Owlin (Owl-People)", "Plasmoid (Slime-People)",
        "Raptor (Bird-of-Prey-Folk)", "Reborn (Revived-Undead)", "Satyr (Goat-People)", "Sharkin (Shark-Folk)",
        "Shifter (Lycanthrope-Folk)", "Simic Hybrid (Bio-Engineered-Humanoids)", "Strig (Owl-Folk)",
        "Tabaxi (Cat-Folk)", "Thri-Kreen (Insectoid-People)", "Tiefling (Demon-Blooded-Humans)", "Tortle (Turtle-People)",
        "Triton (Sea-People)", "Vedalken (Blue-Perfectionists)", "Verdan (Humanoid-Goblins)", "Vulpin (Fox-Folk)",
        "Warforged (Sentient-Constructs)", "Wechselkind (Puppet-People)", "Yuan-ti (Snake-Dragons)"
    ]

    # Additional options for Dragonborn and Eladrin subraces
    colors = ["Black", "Blue", "Green", "Red", "White"]
    gems = ["Amethyst", "Crystal", "Emerald", "Sapphire", "Topaz"]
    metals = ["Brass", "Bronze", "Copper", "Gold", "Silver"]
    seasons = ["Spring", "Summer", "Autumn/Fall", "Winter"]    

    if param == "Y":
        print("0 - Random")
        for r, race in enumerate(commented_races, 1):
            print(f"{r} - {race}")
        rce = int(input("What race would you like? "))
        if rce == 0:
            player.race = random.choice(actual_races)
        elif 1 <= rce <= len(actual_races):
            player.race = actual_races[rce - 1]
        if player.race in subraces: #only if the race is in subraces
            print("0 - Random")
            for idx, subr in enumerate(subraces[player.race], 1): #lists JUST subraces linked to race
                print(f"{idx} - {subr}")   
            subrace_index = int(input("Which subrace would you like? "))
            if subrace_index == 0:
                player.subrace = random.choice(subraces[player.race])
            elif 1 <= subrace_index <= len(subraces[player.race]):
                player.subrace = subraces[player.race][subrace_index - 1]
        if player.subrace == "Chromatic Dragonborn":
            print("0 - Random")
            for idx, color in enumerate(colors, 1):
                print(f"{idx} - {color}")
            color_choice = int(input(f"Which {player.subrace} color would you like? "))
            if color_choice == 0:
                player.color = random.choice(colors)
            elif 1 <= color_choice <= len(colors):
                player.color = colors[color_choice - 1]
        elif player.subrace == "Gem Dragonborn":
            print("0 - Random")
            for idx, gem in enumerate(gems, 1):
                print(f"{idx} - {gem}")
            gem_choice = int(input(f"Which {player.subrace} gem would you like? "))
            if gem_choice == 0:
                player.gem = random.choice(gems)
            elif 1 <= gem_choice <= len(gems):
                player.gem = gems[gem_choice - 1]
        elif player.subrace == "Metallic Dragonborn":
            print("0 - Random")
            for idx, metal in enumerate(metals, 1):
                print(f"{idx} - {metal}")
            metal_choice = int(input(f"Which {player.subrace} metal would you like? "))
            if metal_choice == 0:
                player.metal = random.choice(metals)
            elif 1 <= metal_choice <= len(metals):
                player.metal = metals[metal_choice - 1]
        elif player.subrace == "Eladrin":
            print("0 - Random")
            for idx, season in enumerate(seasons, 1):
                print(f"{idx} - {season}")
            season_choice = int(input(f"Which {player.subrace} season would you like? "))
            if season_choice == 0:
                player.season = random.choice(seasons)
            elif 1 <= season_choice <= len(seasons):
                player.season = seasons[season_choice - 1]
    elif param == "N":
        player.race = random.choice(actual_races)
        if player.race in subraces:
            player.subrace = random.choice(subraces[player.race])
            if player.subrace == "Chromatic Dragonborn":
                player.color = random.choice(colors)
            elif player.subrace == "Gem Dragonborn":
                player.gem = random.choice(gems)
            elif player.subrace == "Metallic Dragonborn":
                player.metal = random.choice(metals)
            elif player.subrace == "Eladrin":
                player.season = random.choice(seasons)


    Line = ["Dhampir", "Hexblood", "Reborn", "No lineage"]
    if param == "Y":
        if ((player.race != "Dhampir") and (player.race != "Hexblood") and (player.race != "Reborn")):
            Lin = input("Would you like a Ravenloft-Styled lineage (in the form of Dhampir, Hexblood or Reborn) to add to your race? Y/N ").strip().lower()
            if Lin in {"y", "yes", "ye"}:
                linea = "Y"
            elif Lin in {"n", "no"}:
                linea = "N"
        if linea == "Y":
            LINE = ["Dhampir, Hexblood, Reborn"]          
            print("0 - Random")
            for ldx, lineage in enumerate(LINE, 1):
                print(f"{ldx} - {lineage}")
            lineag = int(input("Which Ravenloft-Styled would you like to add to your race? "))
            if lineag == 0:
                player.lineage = random.choice(LINE)
            elif 1 <= lineag <= len(LINE):
                player.lineage = LINE[lineag - 1]
        if linea == "N":
            player.lineage = "No lineage"
    if param == "N":
        if ((player.race != "Dhampir") and (player.race != "Hexblood") and (player.race != "Reborn")):
            player.lineage = random.choice(Line)       

    if player.race in {"Corvum", "Gallus", "Luma", "Raptor", "Strig", "Cervan", "Hedge", "Jerbeen", "Mapach", "Vulpin"}:
        if "Bird" in player.slang:
            player.languages.append(dnd_tools.languages["Bird"])
            player.slang.remove("Bird")
    else:
        if "Comm" in player.slang:
            player.languages.append(dnd_tools.languages["Comm"])
            player.slang.remove("Comm")



    
    if player.race == "Aarakocra":
        Hmo1 = dice(4)
        Hmo2 = dice(4)
        Hmod = Hmo1 + Hmo2
        Hbase = 58
        Wmo1 = dice(10)
        Wmo2 = dice(10)
        Wmod = Wmo1 + Wmo2
        Wbase = 80
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs=["Aara", "Aura"]
        # Iterate through the languages to update player's attributes
        for lang in langs:
            if lang in player.slang:  # Check if language exists in available player.slang
                player.languages.append(dnd_tools.languages[lang])  # Add the language to player's known languages
                player.slang.remove(lang)    # Remove it from available player.slang
        player.ability_scores["Dexterity"] += 2
        player.ability_scores["Wisdom"] += 1
        player.speed["Walking"] = 25
        player.creaturetype = "Avian Humanoid"
        player.speed["Flight"] = "50ft (see notes)"
        player.notes.append("Flight: You have a flying speed of 50 feet. To use this speed, you can't be wearing medium or heavy armor.")
        #General notes, if Flight and if player !don medium/heavy armor, player has flight of 50
        player.notes.append("Talons: You have talons that you can use to make unarmed strikes. When you hit with them, the strike deals 1d6 + your Strength modifier slashing damage, instead of the bludgeoning damage normal for an unarmed strike.")
    if player.race == "Aasimar":
        Hmo1 = dice(12)
        Hmo2 = dice(12)
        Hmo3 = dice(12)
        Hmod = Hmo1 + Hmo2 + Hmo3
        Hbase = 56
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Cele"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.ability_scores["Charisma"] += 2
        player.speed["Walking"] = 30
        player.creaturetype = "Humanoid"
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.damresimm.append("Celestial Resistance: Necrotic Damage Resistance.")
        player.damresimm.append("Celestial Resistance: Radiant Damage Resistance.")        
        player.racenotes.append("Healing Hands (see notes)")
        player.racenotes.append("Light Bearer: You know the Light cantrip. Charisma is your spellcasting ability for it.")
        player.spells.append(dnd_tools.SPELLS["Light"])
    if player.race == "Autognome":
        Hmo1 = dice(4)
        Hmo2 = dice(4)
        Hmod = Hmo1 + Hmo2
        Hbase = 31
        Wmo1 = 1
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 35
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Gnom"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)          
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.ability_scores = abilityscores(param, player.ability_scores)
        player.speed["Walking"] = 30
        player.racenotes.append("Built for Success (see notes)")
        player.notes.append(f"Built for Success: You can add a d4 to one attack roll, ability check, or saving throw you make, and you can do so after seeing the d20 roll but before the effects of the roll are resolved. You can use this trait {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
        #Combat notes
        player.racenotes.append("Healing Machine (see notes)")
        player.racenotes.append("Mechanical Nature (see notes)")
        player.notes.append("Mechanical Nature: You have resistance to poison damage and immunity to disease, and you have advantage on saving throws against being paralyzed or poisoned. You don't need to eat, drink, or breathe.")
        player.racenotes.append("Sentry's Rest (see notes)")
        player.notes.append("Sentry's Rest: When you take a long rest, you spend at least 6 hours in an inactive, motionless state, instead of sleeping. In this state, you appear inert, but you remain conscious.")
        #Resting notes
        player.proficiencies = arttool2(param, player.proficiencies)
        player.creaturetype = "Construct"
    if player.race == "Bugbear":
        Hmo1 = dice(12)
        Hmo2 = dice(12)
        Hmod = Hmo1 + Hmo2
        Hbase = 72
        Wmo1 = dice(6)
        Wmo2 = dice(6)
        Wmod = Wmo1 + Wmo2
        Wbase = 200
        langs = ["Gobl"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)    
        player.ability_scores["Strength"] += 2
        player.ability_scores["Dexterity"] += 1
        player.speed["Walking"] = 30
        player.creaturetype = "Goblinoid"
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.racenotes.append("Long-Limbed: When you make a melee attack on your turn, your reach for it is 5 feet greater than normal.")
        #Combat notes
        player.racenotes.append("Powerful Build: You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.")
        #General notes
        player.skills.append(dnd_tools.skills["Stealth"])
        player.racenotes.append("Surprise Attack (see notes)")
        #Combat notes
        player.notes.append("Surprise Attack: If you surprise a creature and hit it with an attack on your first turn in combat, the attack deals an extra 2d6 damage to it. You can use this trait only once per combat." )
    if player.race == "Centaur":
        Hmo1 = dice(10)
        Hmo2 = 0
        Hmod = Hmo1 + Hmo2
        Hbase = 72
        Wmo1 = dice(12)
        Wmo2 = dice(12)
        Wmod = Wmo1 + Wmo2
        Wbase = 600
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.speed["Walking"] = 40
        langs = ["Sylv"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)    
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.creaturetype = "Fey"
        player.racenotes.append("Charge (see notes)")
        player.notes.append("Charge: If you move at least 30 feet straight toward a target and then hit it with a melee weapon attack on the same turn, you can immediately follow that attack with a bonus action, making one attack against the target with your hooves.")
        #Combat Notes
        player.racenotes.append("Hooves (see notes)")
        player.notes.append("Hooves: Your hooves are natural melee weapons, which you can use to make unarmed strikes. If you hit with them, you deal bludgeoning damage equal to 1d4 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.")
        player.racenotes.append("Equine Build (see notes)")
        player.notes.append("Equine Build: You count as one size larger when determining your carrying capacity and the weight you can push or drag.\nIn addition, any climb that requires hands and feet is especially difficult for you because of your equine legs. When you make such a climb, each foot of movement costs you 4 extra feet, instead of the normal 1 extra foot.")
        #General Notes
        SkillsList = [
            dnd_tools.skills["AnimalHandling"],
            dnd_tools.skills["Medicine"],
            dnd_tools.skills["Nature"],
            dnd_tools.skills["Survival"],
        ]
        player.skills = oneskillfromlist(param, player.skills, SkillsList)
    if player.race == "Cervan":
        player.ability_scores["Constitution"] += 2
        player.creaturetype = "Humanoid"
        player.racenotes.append("Practical (see notes)")
        player.notes.append("Practical: Cervans are eminently practical and like to spend their time learning useful skills for life in their woodland villages. You gain proficiency in one of the following skills: Athletics, Medicine, Nature, or Survival.")
        player.racenotes.append("Surge of Vigor (see notes)")
        player.notes.append("Surge of Vigor: All cervans possess a great tenacity and will to survive, which allows them to bounce back from even the most devastating blows. If an attack deals over half of your current remaining hit points in damage, (even if your hit points are reduced to 0 by the attack) you immediately regain hit points equal to 1d12 + your Constitution Modifier.\nYou can’t use this feature again until you have completed a long rest.")
        #Combat Notes
        langs = ["Cerva"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        if player.subrace == "Grove Cervan":
            Hmo1 = dice(10)
            Hmo2 = dice(10)
            Hmod = Hmo1 + Hmo2
            Hbase = 56
            Wmo1 = dice(4)
            Wmo2 = 0
            Wmod = Wmo1 + Wmo2
            Wbase = 110
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            player.height = str(tl)
            player.weight = str(hy)
            player.ability_scores["Dexterity"] += 1
            player.speed["Walking"] = 35
            player.racenotes.append("Standing Leap: Your base long jump is 30 feet, and your base high jump is 15 feet, with or without a running start.")
            #General notes
            player.racenotes.append("Nimble Step: Opportunity attacks made against you are rolled with disadvantage.")     
            #Combat Notes 
        if player.subrace == "Pronghorn Cervan":
            Hmo1 = dice(10)
            Hmo2 = dice(10)
            Hmod = Hmo1 + Hmo2
            Hbase = 73
            Wmo1 = dice(4)
            Wmo2 = dice(4)
            Wmod = Wmo1 + Wmo2
            Wbase = 120
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            player.height = str(tl)
            player.weight = str(hy)
            player.ability_scores["Strength"] += 1
            player.speed["Walking"] = 30
            player.racenotes.append("Robust Build: Your carrying capacity is doubled, as is the weight you can push, drag, or lift.")
            #General Notes
            player.racenotes.append("Antlers (see notes)")
            player.notes.append("Antlers: You have a set of large, strong antlers that can be used to make devastating charge attacks. You can use your unarmed strike to gore opponents, dealing 1d6 + your Strength Modifier piercing damage on a hit.\nAdditionally, if you move at least 20 feet in a straight line towards an opponent, you can spend a bonus action to charge them, dealing an extra 1d6 points of piercing damage. If the target of your charge is Large or smaller, they must make a Strength saving throw against a DC of your Proficiency Bonus + 8 + your Strength Modifier. On failure, the target is pushed 10 feet away from you into a space of your choice.")
            #Combat Notes
    if player.race == "Changeling":
        Hmo1 = dice(12)
        Hmo2 = dice(12)
        Hmo3 = dice(12)
        Hmod = Hmo1 + Hmo2 + Hmo3
        Hbase = 43
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 25
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.ability_scores["Charisma"] += 2
        player.ability_scores = singleabilityscore(param, player.ability_scores)
        player.speed["Walking"] = 30
        player.creaturetype = "Humanoid"
        player.racenotes.append("Shapechanger (see notes)")
        player.notes.append("Shapechanger: As an action, you can change your appearance and your voice. You determine the specifics of the changes, including your coloration, hair length, and sex. You can also adjust your height and weight, but not so much that your size changes. You can make yourself appear as a member of another race, though none of your game statistics change. You can't duplicate the appearance of a creature you've never seen, and you must adopt a form that has the same basic arrangement of limbs that you have. Your clothing and equipment aren't changed by this trait.\nYou stay in the new form until you use an action to revert to your true form or until you die.")
        #General Notes
        SkillsList = [
            dnd_tools.skills["Deception"], 
            dnd_tools.skills["Insight"], 
            dnd_tools.skills["Intimidation"], 
            dnd_tools.skills["Persuasion"]
        ]
        player.skills = oneskillfromlist(param, player.skills, SkillsList)
    if player.race == "Corginian":
        Hmo1 = dice(4)
        Hmo2 = dice(4)
        Hmod = Hmo1 + Hmo2
        Hbase = 36
        Wmo1 = 1
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 40
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.ability_scores["Charisma"] += 2
        player.ability_scores["Wisdom"] += 1
        walkspeed = 25
        player.creaturetype = "Fey"
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.racenotes.append("Nimble: You can move through the space of any creature that is of a size larger than yours.")
        #General Notes
        player.racenotes.append("Slippery: You have advantage on Strength (Athletics) and Dexterity (Acrobatics) checks made to escape a grapple.")
        #Combat Notes
        player.racenotes.append("Strong Jaws (see notes)")
        player.notes.append("Strong Jaws: Your jaws are natural weapons, which you can use to make unarmed strikes. If you attack with them, you deal piercing damage equal to 1d4 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.")
        #Combat notes
        if player.subrace == "Cardigan Corginian":
            player.racenotes.append("Keen Smell: Cardigan Corginians have sharp, observant snouts. You have advantage on Intelligence (Investigation) and Wisdom (Perception) checks involving smell.")                        
            #General Notes
        if player.subrace == "Pembroke Corginian":
            player.racenotes.append("Keen Hearing: Pembroke Corginians have sharp, observant ears. You have advantage on Intelligence (Investigation) and Wisdom (Perception) checks involving hearing.")
            #General Notes
    if player.race == "Corvum":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 52
        Wmo1 = dice(4)
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 70
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.languages.append(dnd_tools.UAur)
        player.ability_scores["Intelligence"] += 2
        player.speed["Walking"] = 30
        player.creaturetype = "Avian Humanoid"
        player.racenotes.append("Glide (see notes)")
        player.notes.append("Glide: Using your feathered arms, you can slow your fall, and glide short distances. When falling you can use your reaction to spread your arms, stiffen your wing feathers, and slow your descent. While doing so, you continue to fall gently at a speed of 60 feet per round, taking no fall damage when you land. If you would fall at least 10 feet in this way, you may fly up to your movement speed in one direction you choose, although you cannot choose to move upwards, landing in the space you finish your movement. You cannot glide while carrying heavy weapons or wielding a shield (though you may drop any held items as part of your reaction to spread your arms). You cannot glide while wearing heavy armor, or if you are encumbered.")
        player.racenotes.append("Talons (see notes)")
        player.notes.append("Talons: Your sharp claws aid you in unarmed combat and while climbing. Your damage for an unarmed strike is 1d4 piercing damage. Additionally, you have advantage on Strength (Athletics) checks made to climb any surface your talons could reasonably grip.")
        #General notes
        SkillsList = [
            dnd_tools.skills["Arcana"], 
            dnd_tools.skills["History"], 
            dnd_tools.skills["Nature"], 
            dnd_tools.skills["Religion"]
        ]
        player.skills = oneskillfromlist(param, player.skills, SkillsList)
        player.racenotes.append("Appraising Eye (see notes)")
        player.notes.append("Appraising Eye: You have an almost supernatural ability to appraise objects. By spending an action examining any object, you can determine any magical properties the item has, how they might be used or activated, as well as a fair estimation of market price. Using this skill strains the eyes, and you must complete a long or short rest before you can use it again.")
        #General notes
        if player.subrace == "Dusk Corvum":
            player.ability_scores["Dexterity"] += 1
            player.racenotes.append("Skulker: You have advantage on Dexterity (Stealth) checks made in dim light or darkness.")
            #General Notes
            player.skills.append(dnd_tools.skills["Insight"])
        if player.subrace == "Kindled Corvum":
            player.ability_scores["Charisma"] += 1
            player.racenotes.append("Convincing (see notes)")
            player.notes.append("Convincing: Kindled corvums have a way with words, and are accomplished at saying what someone wants or needs to hear. You have proficiency in either the Deception or Persuasion skill. Additionally, you have advantage on all Charisma checks made to convince someone of your exceptional knowledge on any topic related to the skill you selected with your learned trait (Arcana, History, Nature, or Religion).")
            #General Notes
            KindledCorvumProf = ["Languages", "Tools"]
            KindledCorvumProfRand = random.choice(KindledCorvumProf)
            if param == "Y":
                print("0 - Random")
                print("1 - One language of your choice")
                print("2 - One Tool of your choice")
                kcprof = int(input("Choose whether to gain proficiency in a language or a tool. "))
                if kcprof == 1:
                    player.languages, player.slang = languagegen(param, player.languages, player.slang)
                if kcprof == 2:
                    player.proficiencies = artisantools(param, player.proficiencies)
                if kcprof == 0:
                    if KindledCorvumProfRand == "Languages":
                        player.languages, player.slang = languagegen(param, player.languages, player.slang)
                    if KindledCorvumProfRand == "Tools":
                        player.proficiencies = artisantools(param, player.proficiencies)
            if param == "N":
                if KindledCorvumProfRand == "Languages":
                    player.languages, player.slang = languagegen(param, player.languages, player.slang)
                if KindledCorvumProfRand == "Tools":
                    player.proficiencies = artisantools(param, player.proficiencies)
            player.racenotes.append("Sharp Mind: You are able to accurately recall with perfect clarity anything you have seen or heard within the past month.")
    if player.race == "Dhampir":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.ability_scores = abilityscores(param, player.ability_scores)
        player.creaturetype = "Humanoid"
        player.speed["Walking"] = 35
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.racenotes.append("Deathless Nature: You don’t need to breathe.")
        #General Notes
        player.racenotes.append("Spider Climb (see notes)")
        player.speed["Climbing"] = player.speed["Walking"]
        player.notes.append("Spider Climb: You have a climbing speed equal to your walking speed. In addition, at 3rd level, you can move up, down, and across vertical surfaces and upside down along ceilings, while leaving your hands free.")
        player.racenotes.append("Vampiric Bite (see notes)")
        player.notes.append(f"Vampiric Bite: Your fanged bite is a natural weapon, which counts as a simple melee weapon with which you are proficient. You add your Constitution modifier, instead of your Strength modifier, to the attack and damage rolls when you attack with this bite. It deals 1d4 piercing damage on a hit. While you are missing half or more of your hit points, you have advantage on attack rolls you make with this bite. When you attack with this bite and hit a creature that isn’t a Construct or an Undead, you can empower yourself in one of the following ways of your choice: You regain hit points equal to the piercing damage dealt by the bite. You gain a bonus to the next ability check or attack roll you make; the bonus equals the piercing damage dealt by the bite. You can empower yourself with this bite {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
        #Combat Notes
        player.proficiencies.append("Natural Weapon: Fangs")
    if player.race == "Disembodied":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.ability_scores["Intelligence"] += 1
        player.ability_scores["Dexterity"] += 1
        player.speed["Walking"] = 30
        player.creaturetype = "Humanoid"
        player.racenotes.append("Fade Away (see notes)")
        player.notes.append("Fade Away: On your turn, as an action, you can fade from the Material Realm and disappear into the ethereal plane. While you remain faded away, you cannot interact with the Material Plane, and effects on the Material Plane cannot interact with you, including spells and creatures. However, you can move and hear as normal, and see everything in shades of grey.\nThis effect lasts for 1 minute, or until you use a bonus action to end it. When the effect ends, you reappear in the Material Plane, in the closest unoccupied space you disappeared from. Once you use this feature, you cannot use it again until you complete a long rest.")
        #Combat Notes
        player.racenotes.append("Planar Outcast(1) (see notes). More options are available at higher levels.")
        player.notes.append("Planar Outcast(1): You may cast the Feather Fall spell once per day, targeting yourself only. Intelligence is your spellcasting ability for this spell. More options are available at higher levels.")
        if player.level >= 3:
            player.racenotes.append("Planar Outcast(2) (see notes)")
            player.notes.append("Planar Outcast(2): You may cast the Blur spell once per day. Intelligence is your spellcasting ability for this spell.")
        if player.level >= 5:
            player.racenotes.append("Planar Outcast(3) (see notes)")
            player.notes.append("Planar Outcast(3): You may cast the Blink spell once per day. Intelligence is your spellcasting ability for this spell.")
        #These are all general notes, NOT spellcasting
        player.skills.append(dnd_tools.skills["Arcana"])
    if player.race == "Dragonborn":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 66
        Wmo1 = dice(6)
        Wmo2 = dice(6)
        Wmod = Wmo1 + Wmo2
        Wbase = 175
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Drac"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)          
        player.creaturetype = "Dragonoid"
        player.speed["Walking"] = 30
        if player.subrace == "Black Scale Dragonborn":
            player.ability_scores["Strength"] += 2
            player.ability_scores["Charisma"] += 1
            player.damresimm.append("Acid Damage Resistance")
            BWDT = "Acid Damage"
            player.racenotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "5 by 30 ft. line (Dex. save)"
            player.racenotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            #Any and all breath weapon attacks can be added to combat notes
            if ((player.level >= 1) and (player.level < 6)):
                BreathWeaponDMG = "2d6"
            if ((player.level >= 6) and (player.level < 11)):
                BreathWeaponDMG = "3d6"
            if ((player.level >= 11) and (player.level < 16)):
                BreathWeaponDMG = "4d6"
            if player.level >= 16:
                BreathWeaponDMG = "5d6"  
            player.notes.append(f"Breath Weapon: You can use your action to exhale destructive energy. The size of this breath weapon is {BreathWeaponSize} and deals {BWDT}. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw (described in the last sentence). The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {BreathWeaponDMG} damage on a failed save, and half as much damage on a successful one. After you use your breath weapon, you can’t use it again until you complete a short or long rest.")            
        if player.subrace == "Blue Scale Dragonborn":
            player.ability_scores["Strength"] += 2
            player.ability_scores["Charisma"] += 1
            player.damresimm.append("Lightning Damage Resistance")
            BWDT = "Lightning Damage"
            player.racenotes.append("Breath Weapon (see notes)")
            BreathWeaponSize  = "5 by 30 ft. line (Dex. save)"
            player.racenotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((player.level >= 1) and (player.level < 6)):
                BreathWeaponDMG = "2d6"
            if ((player.level >= 6) and (player.level < 11)):
                BreathWeaponDMG = "3d6"
            if ((player.level >= 11) and (player.level < 16)):
                BreathWeaponDMG = "4d6"
            if player.level >= 16:
                BreathWeaponDMG = "5d6"  
            player.notes.append(f"Breath Weapon: You can use your action to exhale destructive energy. The size of this breath weapon is {BreathWeaponSize} and deals {BWDT}. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw (described in the last sentence). The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {BreathWeaponDMG} damage on a failed save, and half as much damage on a successful one. After you use your breath weapon, you can’t use it again until you complete a short or long rest.")            
        if player.subrace == "Brass Scale Dragonborn":
            player.ability_scores["Strength"] += 2
            player.ability_scores["Charisma"] += 1
            player.damresimm.append("Fire Damage Resistance")
            BWDT = "Fire Damage"
            player.racenotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "5 by 30 ft. line (Dex. save)"
            player.racenotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((player.level >= 1) and (player.level < 6)):
                BreathWeaponDMG = "2d6"
            if ((player.level >= 6) and (player.level < 11)):
                BreathWeaponDMG = "3d6"
            if ((player.level >= 11) and (player.level < 16)):
                BreathWeaponDMG = "4d6"
            if player.level >= 16:
                BreathWeaponDMG = "5d6"  
            player.notes.append(f"Breath Weapon: You can use your action to exhale destructive energy. The size of this breath weapon is {BreathWeaponSize} and deals {BWDT}. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw (described in the last sentence). The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {BreathWeaponDMG} damage on a failed save, and half as much damage on a successful one. After you use your breath weapon, you can’t use it again until you complete a short or long rest.")
        if player.subrace == "Bronze Scale Dragonborn":
            player.ability_scores["Strength"] += 2
            player.ability_scores["Charisma"] += 1
            player.damresimm.append("Lightning Damage Resistance")
            BWDT = "Lightning Damage"
            player.racenotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "5 by 30 ft. line (Dex. save)"
            player.racenotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((player.level >= 1) and (player.level < 6)):
                BreathWeaponDMG = "2d6"
            if ((player.level >= 6) and (player.level < 11)):
                BreathWeaponDMG = "3d6"
            if ((player.level >= 11) and (player.level < 16)):
                BreathWeaponDMG = "4d6"
            if player.level >= 16:
                BreathWeaponDMG = "5d6"  
            player.notes.append(f"Breath Weapon: You can use your action to exhale destructive energy. The size of this breath weapon is {BreathWeaponSize} and deals {BWDT}. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw (described in the last sentence). The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {BreathWeaponDMG} damage on a failed save, and half as much damage on a successful one. After you use your breath weapon, you can’t use it again until you complete a short or long rest.")
        if player.subrace == "Chromatic Dragonborn":
            player.ability_scores = abilityscores(param, player.ability_scores)
            player.notes.append("Chromatic Dragonborn: If need be, please see Fizban's Treasury of Dragons (tm) for more details about Chromatic Dragonborn.") 
            if player.color == "Black":
                player.damresimm.append("Acid Damage Resistance")
                BWDT = "Acid Damage"
            if player.color == "Blue":
                player.damresimm.append("Lightning Damage Resistance")
                BWDT = "Lightning Damage"
            if player.color == "Green":
                player.damresimm.append("Poison Damage Resistance")
                BWDT = "Poison Damage"
            if player.color == "Red":
                player.damresimm.append("Fire Damage Resistance")
                BWDT = "Fire Damage"
            if player.color == "White":
                player.damresimm.append("Cold Damage Resistance")
                BWDT = "Cold Damage"                                                        
            player.racenotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "5 by 30 ft. line (Dex. save)"
            player.racenotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((player.level >= 1) and (player.level < 5)):
                BreathWeaponDMG = "1d10"
            if ((player.level >= 5) and (player.level < 11)):
                BreathWeaponDMG = "2d10"
            if ((player.level >= 11) and (player.level < 17)):
                BreathWeaponDMG = "3d10"
            if player.level >= 17:
                BreathWeaponDMG = "4d10"                                
            player.notes.append(f"Breath Weapon: When you take the Attack action on your turn, you can replace one of your attacks with an exhalation of magical energy in a 30-foot line that is 5 feet wide. Each creature in that area must make a Dexterity saving throw (DC = 8 + your Constitution modifier + your proficiency bonus). On a failed save, the creature takes {BreathWeaponDMG} {BWDT}. On a successful save, it takes half as much damage.\nYou can use your Breath Weapon {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
            if player.level >= 5:
                player.notes.append("As an action, you can channel your draconic energy to protect yourself. For 1 minute, you become immune to the damage type associated with your Chromatic Ancestry (color). Once you use this trait, you can't do so again until you finish a long rest.")
                #Combat notes
        if player.subrace == "Copper Scale Dragonborn":
            player.ability_scores["Strength"] += 2
            player.ability_scores["Charisma"] += 1
            player.damresimm.append("Acid Damage Resistance")
            BWDT = "Acid Damage"
            player.racenotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "5 by 30 ft. line (Dex. save)"
            player.racenotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((player.level >= 1) and (player.level < 6)):
                BreathWeaponDMG = "2d6"
            if ((player.level >= 6) and (player.level < 11)):
                BreathWeaponDMG = "3d6"
            if ((player.level >= 11) and (player.level < 16)):
                BreathWeaponDMG = "4d6"
            if player.level >= 16:
                BreathWeaponDMG = "5d6"  
            player.notes.append(f"Breath Weapon: You can use your action to exhale destructive energy. The size of this breath weapon is {BreathWeaponSize} and deals {BWDT}. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw (described in the last sentence). The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {BreathWeaponDMG} damage on a failed save, and half as much damage on a successful one. After you use your breath weapon, you can’t use it again until you complete a short or long rest.")
        if player.subrace == "Draconblood Dragonborn":
            player.ability_scores["Intelligence"] += 2
            player.ability_scores["Charisma"] += 1
            player.racenotes.append("Darkvision (see notes)") 
            player.notes.append(dnd_tools.Darkvision)
            #Darkvision notes
            player.racenotes.append("Forceful Presence (see notes)")
            player.notes.append("Forceful Presence: You can use your understanding of creative diplomacy or intimidation to guide a conversation in your favor. When you make a Charisma (Intimidation or Persuasion) check, you can do so with advantage. Once you use this trait, you can't do so again until you finish a short or long rest.")
            #General notes
        if player.subrace == "Gem Dragonborn":
            player.ability_scores = abilityscores(param, player.ability_scores)
            player.notes.append("Gem Dragonborn: If need be, please see Fizban's Treasury of Dragons (tm) for more details about Gem Dragonborn.")
            if player.gem == "Amethyst":
                player.damresimm.append("Force Damage Resistance")
                BWDT = "Force Damage"
            if player.gem == "Crystal":
                player.damresimm.append("Radiant Damage Resistance")
                BWDT = "Radiant Damage"
            if player.gem == "Emerald":
                player.damresimm.append("Psychic Damage Resistance")
                BWDT = "Psychic Damage"
            if player.gem == "Sapphire":
                player.damresimm.append("Thunder Damage Resistance")
                BWDT = "Thunder Damage"
            if player.gem == "Topaz":
                player.damresimm.append("Necrotic Damage Resistance")
                BWDT = "Necrotic Damage"   
            player.racenotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "5 by 30 ft. line (Dex. save)"
            player.racenotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((player.level >= 1) and (player.level < 5)):
                BreathWeaponDMG = "1d10"
            if ((player.level >= 5) and (player.level < 11)):
                BreathWeaponDMG = "2d10"
            if ((player.level >= 11) and (player.level < 17)):
                BreathWeaponDMG = "3d10"
            if player.level >= 17:
                BreathWeaponDMG = "4d10"                                
            player.notes.append(f"Breath Weapon: When you take the Attack action on your turn, you can replace one of your attacks with an exhalation of magical energy in a 30-foot line that is 5 feet wide. Each creature in that area must make a Dexterity saving throw (DC = 8 + your Constitution modifier + your proficiency bonus). On a failed save, the creature takes {BreathWeaponDMG} {BWDT}. On a successful save, it takes half as much damage.\nYou can use your Breath Weapon {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
            player.racenotes.append("Psionic Mind (see notes)")
            player.notes.append("Psionic Mind: You can send telepathic messages to any creature you can see within 30 feet of you. You don't need to share a language with the creature for it to understand these messages, but it must be able to understand at least one language to comprehend them.")
            #General notes
            if player.level >= 5:
                player.racenotes.append("Gem Flight (see notes)")
                player.notes.append("Gem Flight: You can use a bonus action to manifest spectral wings on your body. These wings last for 1 minute. For the duration, you gain a flying speed equal to your walking speed and can hover. Once you use this trait, you can't do so again until you finish a long rest.")
                #General notes? Flight info
        if player.subrace == "Gold Scale Dragonborn":
            player.ability_scores["Strength"] += 2
            player.ability_scores["Charisma"] += 1
            player.damresimm.append("Fire Damage Resistance")
            BWDT = "Fire Damage"
            player.racenotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "5 by 30 ft. line (Dex. save)"
            player.racenotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((player.level >= 1) and (player.level < 6)):
                BreathWeaponDMG = "2d6"
            if ((player.level >= 6) and (player.level < 11)):
                BreathWeaponDMG = "3d6"
            if ((player.level >= 11) and (player.level < 16)):
                BreathWeaponDMG = "4d6"
            if player.level >= 16:
                BreathWeaponDMG = "5d6"  
            player.notes.append(f"Breath Weapon: You can use your action to exhale destructive energy. The size of this breath weapon is {BreathWeaponSize} and deals {BWDT}. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw (described in the last sentence). The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {BreathWeaponDMG} damage on a failed save, and half as much damage on a successful one. After you use your breath weapon, you can’t use it again until you complete a short or long rest.")
        if player.subrace == "Green Scale Dragonborn":
            player.ability_scores["Strength"] += 2
            player.ability_scores["Charisma"] += 1
            player.damresimm.append("Poison Damage Resistance")
            BWDT = "Poison Damage"
            player.racenotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "15 ft. cone (Con. save)"
            player.racenotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((player.level >= 1) and (player.level < 6)):
                BreathWeaponDMG = "2d6"
            if ((player.level >= 6) and (player.level < 11)):
                BreathWeaponDMG = "3d6"
            if ((player.level >= 11) and (player.level < 16)):
                BreathWeaponDMG = "4d6"
            if player.level >= 16:
                BreathWeaponDMG = "5d6"  
            player.notes.append(f"Breath Weapon: You can use your action to exhale destructive energy. The size of this breath weapon is {BreathWeaponSize} and deals {BWDT}. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw (described in the last sentence). The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {BreathWeaponDMG} damage on a failed save, and half as much damage on a successful one. After you use your breath weapon, you can’t use it again until you complete a short or long rest.")
        if player.subrace == "Metallic Dragonborn":
            player.ability_scores = abilityscores(param, player.ability_scores)
            player.notes.append("Metallic Dragonborn: If need be, please see Fizban's Treasury of Dragons (tm) for more details about Metallic Dragonborn.")
            if player.metal == "Brass":
                player.damresimm.append("Fire Damage Resistance")
                BWDT = "Fire Damage"
            if player.metal == "Bronze":
                player.damresimm.append("Lightning Damage Resistance")
                BWDT = "Lightning Damage"
            if player.metal == "Copper":
                player.damresimm.append("Acid Damage Resistance")
                BWDT = "Acid Damage"
            if player.metal == "Gold":
                player.damresimm.append("Fire Damage Resistance")
                BWDT = "Fire Damage"
            if player.metal == "Silver":
                player.damresimm.append("Cold Damage Resistance")
                BWDT = "Cold Damage" 
            player.racenotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "15 ft. cone (Con. save)"
            player.racenotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((player.level >= 1) and (player.level < 5)):
                BreathWeaponDMG = "1d10"
            if ((player.level >= 5) and (player.level < 11)):
                BreathWeaponDMG = "2d10"
            if ((player.level >= 11) and (player.level < 17)):
                BreathWeaponDMG = "3d10"
            if player.level >= 17:
                BreathWeaponDMG = "4d10"                                
            player.notes.append(f"Breath Weapon: When you take the Attack action on your turn, you can replace one of your attacks with an exhalation of magical energy in a 30-foot line that is 5 feet wide. Each creature in that area must make a Dexterity saving throw (DC = 8 + your Constitution modifier + your proficiency bonus). On a failed save, the creature takes {BreathWeaponDMG} {BWDT}. On a successful save, it takes half as much damage.\nYou can use your Breath Weapon {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
            if player.level >= 5:
                player.racenotes.append("Metallic Breath Weapon (see notes)")
                player.notes.append("Metallic Breath Weapon: You gain a second breath weapon. When you take the Attack action on your turn, you can replace one of your attacks with an exhalation in a 15-foot cone. The save DC for this breath is 8 + your Constitution modifier + your proficiency bonus. Whenever you use this trait, choose one:\nEnervating Breath - Each creature in the cone must succeed on a Constitution saving throw or become incapacitated until the start of your next turn.\nRepulsion Breath - Each creature in the cone must succeed on a Strength saving throw or be pushed 20 feet away from you and be knocked prone.\nOnce you use your Metallic Breath Weapon, you can't do so again until you finish a long rest.")
                #Combat noted
        if player.subrace == "Red Scale Dragonborn":
            player.ability_scores["Strength"] += 2
            player.ability_scores["Charisma"] += 1
            player.damresimm.append("Fire Damage Resistance")
            BWDT = "Fire Damage"
            player.racenotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "15 ft. cone (Con. save)"
            player.racenotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((player.level >= 1) and (player.level < 6)):
                BreathWeaponDMG = "2d6"
            if ((player.level >= 6) and (player.level < 11)):
                BreathWeaponDMG = "3d6"
            if ((player.level >= 11) and (player.level < 16)):
                BreathWeaponDMG = "4d6"
            if player.level >= 16:
                BreathWeaponDMG = "5d6"  
            player.notes.append(f"Breath Weapon: You can use your action to exhale destructive energy. The size of this breath weapon is {BreathWeaponSize} and deals {BWDT}. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw (described in the last sentence). The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {BreathWeaponDMG} damage on a failed save, and half as much damage on a successful one. After you use your breath weapon, you can’t use it again until you complete a short or long rest.")
        if player.subrace == "Ravenite Dragonborn":
            player.ability_scores["Strength"] += 2
            player.ability_scores["Constitution"] += 1
            player.racenotes.append("Darkvision (see notes)")
            player.notes.append(dnd_tools.Darkvision)
            #Darkvision notes
            player.racenotes.append("Vengeful Assault (see notes)")
            player.notes.append("Vengeful Assault: When you take damage from a creature in range of a weapon you are wielding, you can use your reaction to make an attack with the weapon against that creature. Once you use this trait, you can't do so again until you finish a short or long rest.")
        if player.subrace == "Silver Scale Dragonborn":
            player.ability_scores["Strength"] += 2
            player.ability_scores["Charisma"] += 1
            player.damresimm.append("Cold Damage Resistance")
            BWDT = "Cold Damage"
            player.racenotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "15 ft. cone (Con. save)"
            player.racenotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((player.level >= 1) and (player.level < 6)):
                BreathWeaponDMG = "2d6"
            if ((player.level >= 6) and (player.level < 11)):
                BreathWeaponDMG = "3d6"
            if ((player.level >= 11) and (player.level < 16)):
                BreathWeaponDMG = "4d6"
            if player.level >= 16:
                BreathWeaponDMG = "5d6"  
            player.notes.append(f"Breath Weapon: You can use your action to exhale destructive energy. The size of this breath weapon is {BreathWeaponSize} and deals {BWDT}. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw (described in the last sentence). The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {BreathWeaponDMG} damage on a failed save, and half as much damage on a successful one. After you use your breath weapon, you can’t use it again until you complete a short or long rest.")
        if player.subrace == "White Scale Dragonborn":
            player.ability_scores["Strength"] += 2
            player.ability_scores["Charisma"] += 1
            player.damresimm.append("Cold Damage Resistance")
            BWDT = "Cold Damage"
            player.racenotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "15 ft. cone (Con. save)"
            player.racenotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((player.level >= 1) and (player.level < 6)):
                BreathWeaponDMG = "2d6"
            if ((player.level >= 6) and (player.level < 11)):
                BreathWeaponDMG = "3d6"
            if ((player.level >= 11) and (player.level < 16)):
                BreathWeaponDMG = "4d6"
            if player.level >= 16:
                BreathWeaponDMG = "5d6"  
            player.notes.append(f"Breath Weapon: You can use your action to exhale destructive energy. The size of this breath weapon is {BreathWeaponSize} and deals {BWDT}. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw (described in the last sentence). The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {BreathWeaponDMG} damage on a failed save, and half as much damage on a successful one. After you use your breath weapon, you can’t use it again until you complete a short or long rest.")
    if player.race == "Dwarf":
        player.ability_scores["Constitution"] += 2
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.racenotes.append("Dwarven Resilience: You have advantage on saving throws against poison, and you have resistance against poison Damage")
        #General notes
        profs = ["Battleaxe", "Handaxe", "Light Hammer", "Warhammer"]
        for prof in profs:
            if prof not in player.proficiencies:
                player.proficiencies.append(prof)
        ToolList = [
            dnd_tools.artisan_tools["SmthTools"]["Name"],
            dnd_tools.artisan_tools["BrewSupp"]["Name"],
            dnd_tools.artisan_tools["MasnTools"]["Name"]
        ]
        player.proficiencies = toolprof(param, player.proficiencies, ToolList)
        player.racenotes.append("Stonecunning (see notes)")
        player.notes.append(f"Stonecunning: Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, or {2*player.profbonus}, instead of your normal proficiency bonus.")
        #General notes
        player.speed["Walking"] = 25
        player.creaturetype = "Humanoid"
        player.racenotes.append("Speed: Your speed is not reduced by wearing heavy armor.") 
        if player.subrace == "Duergar":
            Hmo1 = dice(4)
            Hmo2 = dice(4)
            Hmod = Hmo1 + Hmo2
            Hbase = 48
            Wmo1 = dice(6)
            Wmo2 = dice(6)
            Wmod = Wmo1 + Wmo2
            Wbase = 115
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            player.height = str(tl)
            player.weight = str(hy)
            langs = ["Dwarvi"]
            for lang in langs:
                if lang in player.slang:
                    player.languages.append(dnd_tools.languages[lang])
                    player.slang.remove(lang)             
            player.ability_scores["Strength"] += 1
            player.racenotes.remove("Darkvision (see notes)")
            player.racenotes.append("Superior Darkvision (see notes)")
            #Darkvision+ Notes
            player.notes.append("Superior Darkvision: You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.")
            player.racenotes.append("Duergar Resilience: You have advantage on saving throws against illusions and against being charmed or paralyzed.")
            #General Notes
            player.racenotes.append("Duergar Magic(1) (see notes). More options are available at higher levels.")
            player.notes.append("Duergar Magic(1): You can cast the Enlarge/Reduce spell on yourself once with this trait, using only the spell's enlarge option. You don't need material components for this spell, and you can't cast it while you're in direct sunlight, although sunlight has no effect on it once cast. You regain the ability to cast this spell with this trait when you finish a long rest. Intelligence is your spellcasting ability for this spell.")
            #General Notes
            if player.level >= 5:
                player.racenotes.append("Duergar Magic(2) (see notes)")
                player.notes.append("Duergar Magic(2): You can cast the Invisibility spell on yourself once with this trait. You don't need material components for this spell, and you can't cast it while you're in direct sunlight, although sunlight has no effect on it once cast. You regain the ability to cast this spell with this trait when you finish a long rest. Intelligence is your spellcasting ability for this spell.")
                #General Notes
            player.racenotes.append("Sunlight Sensitivity (see notes)")
            player.notes.append("Sunlight Sensitivity: You have disadvantage on Attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight.")
            #Combat Notes
        if player.subrace == "Hill Dwarf":
            Hmo1 = dice(4)
            Hmo2 = dice(4)
            Hmod = Hmo1 + Hmo2
            Hbase = 46
            Wmo1 = dice(6)
            Wmo2 = dice(6)
            Wmod = Wmo1 + Wmo2
            Wbase = 115    
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            player.height = str(tl)
            player.weight = str(hy)               
            langs = ["Dwarvi"]
            for lang in langs:
                if lang in player.slang:
                    player.languages.append(dnd_tools.languages[lang])
                    player.slang.remove(lang)                  
            player.ability_scores["Wisdom"] += 1
            player.racenotes.append("Dwarven Toughness: Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.")
            #General Notes
        if player.subrace == "Mountain Dwarf":
            Hmo1 = dice(4)
            Hmo2 = dice(4)
            Hmod = Hmo1 + Hmo2
            Hbase = 46
            Wmo1 = dice(6)
            Wmo2 = dice(6)
            Wmod = Wmo1 + Wmo2
            Wbase = 115  
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            player.height = str(tl)
            player.weight = str(hy)                
            langs = ["Dwarvi"]
            for lang in langs:
                if lang in player.slang:
                    player.languages.append(dnd_tools.languages[lang])
                    player.slang.remove(lang)      
            player.ability_scores["Strength"] += 2
            profs = ["Light Armor", "Medium Armor"]
            for prof in profs:
                if prof not in player.proficiencies:
                    player.proficiencies.append(prof)
    if player.race == "Elf":
        player.speed["Walking"] = 30
        player.creaturetype = "Humanoid"
        player.ability_scores["Dexterity"] += 2
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.skills.append(dnd_tools.skills["Perception"])
        player.racenotes.append("Fey Ancestry: You have advantage on saving throws against being charmed, and magic can’t put you to sleep.")
        #Combat notes
        #Add "Trance" to general notes, since every elf except dark elf and astral elf have it
        if player.subrace == "Astral Elf":
            Hmo1 = dice(6)
            Hmo2 = dice(6)
            Hmod = Hmo1 + Hmo2
            Hbase = 44
            Wmo1 = dice(6)
            Wmo2 = dice(6)
            Wmod = Wmo1 + Wmo2
            Wbase = 75
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            player.height = str(tl)
            player.weight = str(hy)
            langs = ["Elvi"]
            for lang in langs:
                if lang in player.slang:
                    player.languages.append(dnd_tools.languages[lang])
                    player.slang.remove(lang)      
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.ability_scores = abilityscores(param, player.ability_scores)
            player.racenotes.append("Astral Fire (see notes)")
            player.notes.append("Astral Fire: You know one of the following cantrips of your choice: dancing lights, light, or sacred flame. Intelligence, Wisdom, or Charisma is your spellcasting ability for it (choose when you select this race).")
            #Spell notes           
            player.racenotes.append("Starlight Step (see Notes)")
            player.notes.append(f"Starlight Step - As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. You can use this trait {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
            #Combat notes
            player.racenotes.append("Astral Trance (see notes)")
            player.notes.append("Astral Trance - You don't need to sleep, and magic can't put you to sleep. You can finish a long rest in 4 hours if you spend those hours in a trancelike meditation, during which you remain conscious.\nWhenever you finish this trance, you gain proficiency in one skill of your choice and with one weapon or tool of your choice, selected from the Player's Handbook. You mystically acquire these proficiencies by drawing them from shared elven memory and the experiences of entities on the Astral Plane, and you retain them until you finish your next long rest.")
        if player.subrace == "Dark Elf":
            Hmo1 = dice(6)
            Hmo2 = dice(6)
            Hmod = Hmo1 + Hmo2
            Hbase = 44
            Wmo1 = dice(6)
            Wmo2 = dice(6)
            Wmod = Wmo1 + Wmo2
            Wbase = 75
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            player.height = str(tl)
            player.weight = str(hy)
            langs = ["Elvi"]
            for lang in langs:
                if lang in player.slang:
                    player.languages.append(dnd_tools.languages[lang])
                    player.slang.remove(lang)             
            player.ability_scores["Charisma"] += 1
            player.racenotes.remove("Darkvision (see notes)")
            player.racenotes.append("Superior Darkvision (see notes)")
            player.notes.append("Superior Darkvision: You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.")
            #Darkvision Notes
            player.racenotes.append("Sunlight Sensitivity (see notes)")
            player.notes.append("Sunlight Sensitivity: You have disadvantage on Attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight.")            
            #Combat Notes
            player.racenotes.append("Drow Magic(1) (see notes). More options are available at higher levels.")
            player.notes.append("Drow Magic(1): You know the Dancing Lights cantrip. More options are available at higher levels.")
            #Spell notes, for just the cantrip, general notes for rest
            if player.level >= 3:
                player.racenotes.append("Drow Magic(2) (see notes).")
                player.notes.append("Drow Magic(2): You can cast the Faerie Fire spell once per day; you must finish a long rest in order to cast the spell again using this trait. Charisma is your spellcasting ability for this spell.")
            if player.level >= 5:
                player.racenotes.append("Drow Magic(3) (see notes).")
                player.notes.append("Drow Magic(3): You can also cast the Darkness spell once per day; you must finish a long rest in order to cast the spell again using this trait. Charisma is your spellcasting ability for this spell.")                             
            player.racenotes.append("Trance (see notes)")
            player.notes.append("Trance: Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is “trance.”) While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.")                
            #General notes
            profs = ["Rapier", "Shortsword", "Hand Crossbow"]
            for prof in profs:
                if prof not in player.proficiencies:
                    player.proficiencies.append(prof)
        if player.subrace == "Eladrin":
            Hmo1 = dice(12)
            Hmo2 = dice(12)
            Hmod = Hmo1 + Hmo2
            Hbase = 54
            Wmo1 = dice(4)
            Wmo2 = 0
            Wmod = Wmo1 + Wmo2
            Wbase = 90
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            player.height = str(tl)
            player.weight = str(hy)
            langs = ["Elvi"]
            for lang in langs:
                if lang in player.slang:
                    player.languages.append(dnd_tools.languages[lang])
                    player.slang.remove(lang)        
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.ability_scores["Charisma"] += 1
            player.racenotes.append("Trance (see notes)")
            player.notes.append("Trance: Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is “trance.”) While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.")    
        if player.subrace == "High Elf": 
            Hmo1 = dice(10)
            Hmo2 = dice(10)
            Hmod = Hmo1 + Hmo2
            Hbase = 90
            Wmo1 = dice(4)
            Wmo2 = dice(4)
            Wmod = Wmo1 + Wmo2
            Wbase = 100
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            player.height = str(tl)
            player.weight = str(hy)
            langs = ["Elvi"]
            for lang in langs:
                if lang in player.slang:
                    player.languages.append(dnd_tools.languages[lang])
                    player.slang.remove(lang)        
            player.languages, player.slang = languagegen(param, player.languages, player.slang)     
            player.ability_scores["Intelligence"] += 1
            profs = ["Longsword", "Shortsword", "Shortbow", "Longbow"]
            for prof in profs:
                if prof not in player.proficiencies:
                    player.proficiencies.append(prof)
            player.racenotes.append("Wizard Cantrip (see notes)")
            player.notes.append("Wizard Cantrip: You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it.")
            #Spell Notes
            player.racenotes.append("Trance (see notes)")
            player.notes.append("Trance: Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is “trance.”) While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.")            
        if player.subrace == "Sea Elf":
            Hmo1 = dice(8)
            Hmo2 = dice(8)
            Hmod = Hmo1 + Hmo2
            Hbase = 54
            Wmo1 = dice(4)
            Wmo2 = 0
            Wmod = Wmo1 + Wmo2
            Wbase = 90
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            player.height = str(tl)
            player.weight = str(hy)
            langs = ["Elvi", "Aqua"]
            for lang in langs:
                if lang in player.slang:
                    player.languages.append(dnd_tools.languages[lang])
                    player.slang.remove(lang)                    
            player.ability_scores["Constitution"] += 1
            profs = ["Spear", "Trident", "Light Crossbow", "Net"]
            for prof in profs:
                if prof not in player.proficiencies:
                    player.proficiencies.append(prof)            
            player.racenotes.append("Child of the Sea: You have a swimming speed of 30 feet, and you can breathe air and water.")
            #General notes
            player.speed["Swimming"] = 30
            player.racenotes.append("Friend of the Sea: Using gestures and sounds, you can communicate simple ideas with any beast that has an innate swimming speed.")
            #General notes
            player.racenotes.append("Trance (see notes)")
            player.notes.append("Trance: Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is “trance.”) While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.")
        if player.subrace == "Shadar-kai":
            Hmo1 = dice(8)
            Hmo2 = dice(8)
            Hmod = Hmo1 + Hmo2
            Hbase = 56
            Wmo1 = dice(4)
            Wmo2 = 0
            Wmod = Wmo1 + Wmo2
            Wbase = 90
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            player.height = str(tl)
            player.weight = str(hy)
            langs = ["Elvi"]
            for lang in langs:
                if lang in player.slang:
                    player.languages.append(dnd_tools.languages[lang])
                    player.slang.remove(lang)        
            player.ability_scores["Constitution"] += 1
            player.damresimm.append("Necrotic Damage Resistance")
            player.racenotes.append("Blessing of the Raven Queen(1) (see notes). More options are available at higher levels.")
            player.notes.append("Blessing of the Raven Queen(1): As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. Once you use this trait, you can't do so again until you finish a long rest.")
            #General notes
            if player.level >= 3:
                player.racenotes.append("Blessing of the Raven Queen(2) (see notes)")
                player.notes.append("Blessing of the Raven Queen(2): You also gain resistance to all damage when you teleport using this trait. The resistance lasts until the start of your next turn. During that time, you appear ghostly and translucent.")
                #General noted
            player.racenotes.append("Trance (see notes)")
            player.notes.append("Trance: Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is “trance.”) While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.")
        if player.subrace == "Wood Elf":
            Hmo1 = dice(10)
            Hmo2 = dice(10)
            Hmod = Hmo1 + Hmo2
            Hbase = 90
            Wmo1 = dice(4)
            Wmo2 = dice(4)
            Wmod = Wmo1 + Wmo2
            Wbase = 100
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            player.height = str(tl)
            player.weight = str(hy)
            langs = ["Elvi"]
            for lang in langs:
                if lang in player.slang:
                    player.languages.append(dnd_tools.languages[lang])
                    player.slang.remove(lang)        
            player.ability_scores["Wisdom"] += 1
            profs = ["Longsword", "Shortsword", "Shortbow", "Longbow"]
            for prof in profs:
                if prof not in player.proficiencies:
                    player.proficiencies.append(prof)            
            player.speed["Walking"] = 35
            player.racenotes.append("Mask of the Wild: You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.")
            #General notes
            player.racenotes.append("Trance (see notes)")
            player.notes.append("Trance: Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is “trance.”) While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.")            
    if player.race == "Fairy":
        Hmo1 = dice(4)
        Hmo2 = dice(4)
        Hmod = Hmo1 + Hmo2
        Hbase = 21
        Wmo1 = 1
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 20
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.ability_scores = abilityscores(param, player.ability_scores)
        player.creaturetype = "Fey"
        player.speed["Walking"] = 30
        player.racenotes.append("Flight: Because of your wings, you have a flying speed equal to your walking speed. You can't use this flying speed if you're wearing medium or heavy armor.")
        player.speed["Flying"] = "30ft (see notes)"
        player.racenotes.append("Fairy Magic(1) (see notes). More options are available at higher levels.")
        player.notes.append("Fairy Magic(1): You know the Druidcraft cantrip. More options are available at higher levels.")
        #Spells notes for cantrip, General notes for rest
        if player.level >= 3:
            player.racenotes.append("Fairy Magic(2) (see notes)")
            player.notes.append("Fairy Magic(2): You can cast the Faerie Fire spell with this trait. Once you cast Faerie Fire with this trait, you can't cast that spell with it again until you finish a long rest. You can also cast this spell using any spell slots you have of the appropriate level. Intelligence, Wisdom, or Charisma is your spellcasting ability for this spell when you cast it with this trait (choose when you select this race).")
        if player.level >= 5:
            player.racenotes.append("Fairy Magic(3) (see notes)")
            player.notes.append("Fairy Magic(3): You can also cast the Enlarge/Reduce spell with this trait. Once you cast Enlarge/Reduce with this trait, you can't cast that spell with it again until you finish a long rest. You can also cast this spell using any spell slots you have of the appropriate level. Intelligence, Wisdom, or Charisma is your spellcasting ability for this spell when you cast it with this trait (choose when you select this race).")
    if player.race == "Firbolg":
        Hmo1 = dice(12)
        Hmo2 = dice(12)
        Hmod = Hmo1 + Hmo2
        Hbase = 74
        Wmo1 = dice(6)
        Wmo2 = dice(6)
        Wmod = Wmo1 + Wmo2
        Wbase = 175
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Elvi", "Gian"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)                
        player.ability_scores["Strength"] += 1
        player.ability_scores["Wisdom"] += 2
        player.speed["Walking"] = 30
        player.creaturetype = "Fey"
        player.racenotes.append("Firbolg Magic (see notes)")
        player.notes.append("Firbolg Magic: You can cast Detect Magic and Disguise Self with this trait, using Wisdom as your spellcasting ability for them. Once you cast either spell, you can't cast it again with this trait until you finish a short or long rest. When you use this version of Disguise Self, you can seem up to 3 feet shorter than normal, allowing you to more easily blend in with humans and elves.")
        #General Notes
        player.racenotes.append("Hidden Step (see notes)")
        player.notes.append("Hidden Step: As a bonus action, you can magically turn invisible until the start of your next turn or until you attack, make a damage roll, or force someone to make a saving throw. Once you use this trait, you can't use it again until you finish a short or long rest.")
        #Combat Notes
        player.racenotes.append("Powerful Build: You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.")
        player.racenotes.append("Speech of Beast and Leaf (see notes)")
        player.notes.append("Speech of Beast and Leaf: You have the ability to communicate in a limited manner with beasts and plants. They can understand the meaning of your words, though you have no special ability to understand them in return. You have advantage on all Charisma checks you make to influence them.")
        #General notes
    if player.race == "Gallus":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmo3 = dice(10)
        Hmod = Hmo1 + Hmo2 + Hmo3
        Hbase = 40
        Wmo1 = dice(4)
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 55
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.languages.append(dnd_tools.UAur)
        player.ability_scores["Wisdom"] += 2
        player.speed["Walking"] = 30
        player.creaturetype = "Avian Humanoid"
        player.racenotes.append("Glide (see notes)")
        player.notes.append("Glide: Using your feathered arms, you can slow your fall, and glide short distances. When falling you can use your reaction to spread your arms, stiffen your wing feathers, and slow your descent. While doing so, you continue to fall gently at a speed of 60 feet per round, taking no fall damage when you land. If you would fall at least 10 feet in this way, you may fly up to your movement speed in one direction you choose, although you cannot choose to move upwards, landing in the space you finish your movement. You cannot glide while carrying heavy weapons or wielding a shield (though you may drop any held items as part of your reaction to spread your arms). You cannot glide while wearing heavy armor, or if you are encumbered.")
        #General Notes
        player.racenotes.append("Wing Flap (see notes)")
        player.notes.append("Wing Flap: As a bonus action, you can use your powerful feathered arms to propel yourself upward a distance equal to half your movement speed. You can use it in conjunction with a regular jump, but not while gliding.")
        #Combat Notes
        player.racenotes.append("Communal (see notes)")
        player.notes.append(f"Communal: Whenever you make an Intelligence (History) check related to the history of your race, culture, or community, you are considered proficient in the History skill and add double your proficiency bonus to the check, or {2*player.profbonus}, instead of your normal proficiency bonus.")
        #General Notes
        if "Simple Weapons" not in player.proficiencies:
            player.proficiencies.append("Simple Weapons")
        ToolList = [
            dnd_tools.artisan_tools["BrewSupp"]["Name"],
            dnd_tools.artisan_tools["CarpTools"]["Name"],
            dnd_tools.artisan_tools["SmthTools"]["Name"]
        ]
        player.proficiencies = toolprof(param, player.proficiencies, ToolList)
        if player.subrace == "Bright Gallus":
            player.ability_scores["Charisma"] += 1
            player.racenotes.append("Inspiring (see notes)")
            player.notes.append("Inspiring: By spending an action and giving words of advice or encouragement, you can inspire an ally who is able to see and hear you. The ally can roll a d4 and add the number rolled to their next ability check, attack roll, or saving throw.")
            #General Notes
            player.skills.append(dnd_tools.skills["Insight"])
        if player.subrace == "Huden Gallus":
            player.ability_scores["Dexterity"] += 1
            player.racenotes.append("Seedspeech (see notes)")
            player.notes.append("Seedspeech: Your connection to the Great Rhythm is such that you can speak with the greenery of the forest itself. Through speech and touch you can communicate simple ideas to living plants. You are able to interpret their responses in simple language. Plants in the Wood do not experience the world in terms of sight, but most can feel differences in temperature, describe things that have touched them, as well as hear vibrations that happened around them (including speech).")
            #General Notes
            player.skills.append(dnd_tools.skills["Nature"])
    if player.race == "Genasi":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Prim"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)    
        player.creaturetype = "Humanoid"
        player.ability_scores["Constitution"] += 2
        player.speed["Walking"] = 30
        if player.subrace == "Air Genasi":
            player.ability_scores["Dexterity"] += 1
            player.racenotes.append("Unending Breath: You can hold your breath indefinitely while you're not incapacitated.")
            #General Notes
            player.racenotes.append("Mingle with the Wind (see notes)")
            player.notes.append("Mingle with the Wind: You can cast the Levitate spell once with this trait, requiring no material components, and you regain the ability to cast it this way when you finish a long rest. Constitution is your spellcasting ability for this spell.")
            #General Notes
        if player.subrace == "Earth Genasi":
            player.ability_scores["Strength"] += 1
            player.racenotes.append("Earth Walk: You can move across difficult terrain made of earth or stone without expending extra movement.")
            #General Notes
            player.racenotes.append("Merge With Stone (see notes)")
            player.notes.append("Merge With Stone: You can cast the Pass Without Trace spell once with this trait, requiring no material components, and you regain the ability to cast it this way when you finish a long rest. Constitution is your spellcasting ability for this spell.")
            #General Notes
        if player.subrace == "Fire Genasi":
            player.ability_scores["Intelligence"] += 1
            player.racenotes.append("Darkvision (see notes)")
            player.notes.append(dnd_tools.Darkvision)
            #Darkvision notes
            player.damresimm.append("Fire Damage Resistance")
            player.racenotes.append("Reach to the Blaze(1) (see notes). More options are available at higher levels.")
            player.notes.append("Reach to the Blaze(1): You know the Produce Flame cantrip. Constitution is your spellcasting ability for this spell.")
            #Spell Notes for (1) and General Notes for (2)
            if player.level >= 3:
                player.racenotes.append("Reach to the Blaze(2) (see notes)")
                player.notes.append("Reach to the Blaze(2): You can cast the Burning Hands spell once with this trait as a 1st-level spell, and you regain the ability to cast it this way when you finish a long rest. Constitution is your spellcasting ability for this spell.")
        if player.subrace == "Water Genasi":
            player.ability_scores["Wisdom"] += 1
            player.damresimm.append("Acid Damage Resistance")
            player.racenotes.append("Amphibious: You can breathe air and water.")
            #General Notes
            player.speed["Swimming"] = 30
            player.racenotes.append("Swim: You have a swimming speed of 30 feet.")
            player.racenotes.append("Call to the Wave(1) (see notes). More options are available at higher levels.")
            player.notes.append("Call to the Wave(1): You know the Shape Water cantrip. Constitution is your spellcasting ability for is spell.")
            #Spell Notes for (1) and General Notes for (2)
            if player.level >= 3:
                player.racenotes.append("Call to the Wave(2) (see notes)")
                player.notes.append("Call to the Wave(2): You can cast the Create or Destroy Water spell once with this trait as a 2nd-level spell, and you regain the ability to cast it this way when you finish a long rest. Constitution is your spellcasting ability for is spell.")
    if player.race == "Giff":
        Hmo1 = dice(12)
        Hmo2 = dice(12)
        Hmod = Hmo1 + Hmo2
        Hbase = 74
        Wmo1 = dice(6)
        Wmo2 = dice(6)
        Wmod = Wmo1 + Wmo2
        Wbase = 175
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.ability_scores = abilityscores(param, player.ability_scores)
        player.creaturetype = "Humanoid"
        player.speed["Walking"] = 30
        player.racenotes.append("Swim: Your swimming speed is the same as your walking speed")
        player.speed["Swimming"] = player.speed["Walking"]
        player.racenotes.append("Astral Spark (see notes)")
        player.notes.append(f"Astral Spark: Your psychic connection to the Astral Plane enables you to mystically access a spark of divine power, which you can channel through your weapons. When you hit a target with a simple or martial weapon, you can cause the target to take an extra {player.profbonus} force damage.\nYou can use this trait {player.profbonus} times, but you can use it no more than once per turn. You regain all expended uses when you finish a long rest.")
        #Combat Noted
        if "Firearms" not in player.proficiencies:
            player.proficiencies.append("Firearms")
        player.racenotes.append("Firearms Mastery - You have a mystical connection to firearms that traces back to the gods of the giff, who delighted in such weapons. You have proficiency with all firearms (already in proficiencies) and ignore the loading property of any firearm. In addition, attacking at long range with a firearm doesn't impose disadvantage on your attack roll.")
        player.racenotes.append("Hippo Build (see notes)")
        player.notes.append("Hippo Build: You have advantage on Strength-based ability checks and Strength saving throws. In addition, you count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.")
        #General Notes
    if player.race == "Gith":
        player.speed["Walking"] = 30
        player.creaturetype = "Humanoid"
        player.ability_scores["Intelligence"] += 1
        if player.subrace == "Githyanki":
            Hmo1 = dice(12)
            Hmo2 = dice(12)
            Hmod = Hmo1 + Hmo2
            Hbase = 60
            Wmo1 = dice(4)
            Wmo2 = dice(4)
            Wmod = Wmo1 + Wmo2
            Wbase = 100
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            player.height = str(tl)
            player.weight = str(hy)
            langs = ["GithL"]
            for lang in langs:
                if lang in player.slang:
                    player.languages.append(dnd_tools.languages[lang])
                    player.slang.remove(lang)  
            player.ability_scores["Strength"] += 2
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.proficiencies, player.skills = toolskillprof(param, player.proficiencies, player.skills)
            player.racenotes.append("Githyanki Psionics(1) (see notes). More options are available at higher levels.")
            player.notes.append("Githyanki Psionics(1): You know the Mage Hand cantrip, and the hand is invisible when you cast the cantrip with this trait.\nIntelligence is your spellcasting ability for this spell. When you cast it with this trait, it doesn't require components.")
            #Spell Notes for (1), general notes for (2) and (3)
            if player.level >= 3:
                player.racenotes.append("Githyanki Psionics(2) (see notes)")
                player.notes.append("Githyanki Psionics(2): You can cast Jump once with this trait, and you regain the ability to do so when you finish a long rest.\nIntelligence is your spellcasting ability for this spell. When you cast it with this trait, it doesn't require components.")
            if player.level >= 5:
                player.racenotes.append("Githyanki Psionics(3) (see notes)")
                player.notes.append("Githyanki Psionics(3): You can cast the Misty Step spell once with this trait, and you regain the ability to do so when you finish a long rest.\nIntelligence is your spellcasting ability for this spell. When you cast it with this trait, it doesn't require components.")
            profs = ["Light Armor", "Medium Armor", "Shortsword", "Longsword", "Greatsword"]
            for prof in profs:
                if prof not in player.proficiencies:
                    player.proficiencies.append(prof)
        if player.subrace == "Githzerai":
            Hmo1 = dice(12)
            Hmo2 = dice(12)
            Hmod = Hmo1 + Hmo2
            Hbase = 59
            Wmo1 = dice(4)
            Wmo2 = 0
            Wmod = Wmo1 + Wmo2
            Wbase = 90
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            player.height = str(tl)
            player.weight = str(hy)
            langs = ["GithL"]
            for lang in langs:
                if lang in player.slang:
                    player.languages.append(dnd_tools.languages[lang])
                    player.slang.remove(lang)  
            player.ability_scores["Wisdom"] += 2
            player.racenotes.append("Mental Discipline (see notes)")
            player.notes.append("Mental Discipline: You have advantage on saving throws against the charmed and frightened conditions. Under the tutelage of monastic masters, githzerai learn to govern their own minds.")
            #General Notes
            player.racenotes.append("Githzerai Psionics(1) (see notes). More options available at higher levels.")
            player.notes.append("Githzerai Psionics(1): You know the Mage Hand cantrip, and the hand is invisible when you cast the cantrip with this trait.\nWisdom is your spellcasting ability for this spell. When you cast it with this trait, it doesn't require components.")
            #Spell Notes for (1), general notes for (2) and (3)
            if player.level >= 3:
                player.racenotes.append("Githzerai Psionics(2) (see notes)")
                player.notes.append("Githzerai Psionics(2): You can cast Shield once with this trait, and you regain the ability to do so when you finish a long rest.\nWisdom is your spellcasting ability for this spell. When you cast it with this trait, it doesn't require components.")
            if player.level >= 5:
                player.racenotes.append("Githzerai Psionics(3) (see notes)")
                player.notes.append("Githzerai Psionics(3): You can cast the Detect Thoughts spell once with this trait, and you regain the ability to do so when you finish a long rest.\nWisdom is your spellcasting ability for this spell. When you cast it with this trait, it doesn't require components.")
    if player.race == "Gnome":
        Hmo1 = dice(4)
        Hmo2 = dice(4)
        Hmod = Hmo1 + Hmo2
        Hbase = 31
        Wmo1 = 1
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 35
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Gnom"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.creaturetype = "Humanoid"
        player.ability_scores["Intelligence"] += 2
        player.speed["Walking"] = 25
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.racenotes.append("Proficent in Intelligence(Saving Throw) against magic")
        player.racenotes.append("Proficent in Wisdom(Saving Throw) against magic")
        player.racenotes.append("Proficent in Charisma(Saving Throw) against magic")
        #All 3 of those are General Notes
        if player.subrace == "Forest Gnome":
            player.ability_scores["Dexterity"] += 1
            player.racenotes.append("Natural Illusionist: You know the Minor Illusion cantrip. Intelligence is your spellcasting modifier for it.")
            #Spell Notes
            player.racenotes.append("Speak with Small Beasts: Through sound and gestures, you may communicate simple ideas with Small or smaller beasts.")
            #General Notes
        if player.subrace == "Rock Gnome":
            player.ability_scores["Constitution"] += 1
            player.racenotes.append("Artificer's Lore (see notes)")
            player.notes.append(f"Artificer's Lore: Whenever you make an Intelligence (History) check related to magic items, alchemical objects, or technological devices, you can add twice your proficiency bonus, or {2*player.profbonus}, instead of any proficiency bonus you normally apply.")
            #General Notes
            player.racenotes.append("Tinker (see notes)")
            player.notes.append("Tinker - You have proficiency with artisan’s tools (tinker’s tools). Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it; at that time, you can reclaim the materials used to create it. You can have up to three such devices active at a time.\nWhen you create a device, choose one of the following options:\nClockwork Toy. This toy is a clockwork animal, monster, or person, such as a frog, mouse, bird, dragon, or soldier. When placed on the ground, the toy moves 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents.\nFire Starter. The device produces a miniature flame, which you can use to light a candle, torch, or campfire. Using the device requires your action.\nMusic Box - When opened, this music box plays a single song at a moderate volume. The box stops playing when it reaches the song’s end or when it is closed.")
            if dnd_tools.artisan_tools["TinkTools"]["Name"] not in player.proficiencies:
                player.proficiencies.append(dnd_tools.artisan_tools["TinkTools"]["Name"])
        if player.subrace == "Svirfneblin (Deep) Gnome":
            langs = ["Unde"]
            for lang in langs:
                if lang in player.slang:
                    player.languages.append(dnd_tools.languages[lang])
                    player.slang.remove(lang)  
            player.ability_scores["Dexterity"] += 1
            player.racenotes.append("Superior Darkvision: Your darkvision has a radius of 120 feet.")
            #Darkvision Notes
            player.racenotes.append("Stone Camouflage: You have advantage on Dexterity (stealth) checks to hide in rocky terrain.")
            #General Notes
    if player.race == "Goblin":
        Hmo1 = dice(4)
        Hmo2 = dice(4)
        Hmod = Hmo1 + Hmo2
        Hbase = 41
        Wmo1 = 1
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 35
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Gobl"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.creaturetype = "Goblinoid"
        player.ability_scores["Dexterity"] += 2
        player.ability_scores["Constitution"] += 1
        player.speed["Walking"] = 30
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.racenotes.append("Fury of the Small (see notes)")
        player.notes.append(f"Fury of the Small: When you damage a creature with an attack or a spell and the creature's size is larger than yours, you can cause the attack or spell to deal extra damage to the creature. The extra damage equals your player level, {player.level}. Once you use this trait, you can't use it again until you finish a short or long rest.")
        #Combat Notes
        player.racenotes.append("Nimble Escape: You can take the Disengage or Hide action as a bonus action on each of your turns.")
        #Combat Notes
    if player.race == "Goliath":
        Hmo1 = dice(6)
        Hmo2 = dice(6)
        Hmod = Hmo1 + Hmo2
        Hbase = 84
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 140
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Gian"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.creaturetype = "Humanoid"
        player.ability_scores["Strength"] += 2
        player.ability_scores["Constitution"] += 1
        player.speed["Walking"] = 30
        player.skills.append(dnd_tools.skills["Athletics"])
        player.racenotes.append("Stone's Endurance (see notes)")
        player.notes.append("Stone's Endurance: You can focus yourself to occasionally shrug off injury. When you take damage, you can use your reaction to roll a d12. Add your Constitution modifier to the number rolled, and reduce the damage by that total. After you use this trait, you can't use it again until you finish a short or long rest.")
        #Combat Notes
        player.racenotes.append("Powerful Build: You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.")
        #General Notes
        player.racenotes.append("Mountain Born (see notes)")
        player.notes.append("Mountain Born: You're acclimated to high altitude, including elevations above 20,000 feet. You're also naturally adapted to cold climates, as described in chapter 5 of the Dungeon Master's Guide.")
        #General Notes
    if player.race == "Grung":
        Hmo1 = dice(6)
        Hmo2 = dice(6)
        Hmod = Hmo1 + Hmo2
        Hbase = 30
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 30
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Grun"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.ability_scores["Dexterity"] += 2
        player.ability_scores["Constitution"] += 1
        player.skills.append(dnd_tools.skills["Perception"])
        player.speed["Walking"] = 25
        player.creaturetype = "Humanoid"
        player.racenotes.append("Your climbing speed is equal to your walking speed.")
        player.speed["Climbing"] = player.speed["Walking"]
        player.racenotes.append("Amphibious: You can breathe air and water.")
        #General Notes
        player.damresimm.append("Poison Damage Immunity")
        player.damresimm.append("Poison Condition Immunity")
        player.racenotes.append("Poison Immunity: You’re immune to poison damage and the poisoned condition.")
        player.racenotes.append("Poisonous Skin (see notes)")
        player.notes.append("Poisonous Skin: Any creature that grapples you or otherwise comes into direct contact with your skin must succeed on a DC 12 Constitution saving throw or become poisoned for 1 minute. A poisoned creature no longer in direct contact with you can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.\nYou can also apply this poison to any piercing weapon as part of an attack with that weapon, though when you hit the poison reacts differently. The target must succeed on a DC 12 Constitution saving throw or take 2d4 poison damage.")
        #Combat Notes
        player.racenotes.append("Standing Leap: Your long jump is up to 25 feet and your high jump is up to 15 feet, with or without a running start.")
        #General Notes
        player.racenotes.append("Water Dependency (see notes)")
        player.notes.append("Water Dependency: If you fail to immerse yourself in water for at least 1 hour during a day, you suffer one level of exhaustion at the end of that day. You can only recover from this exhaustion through magic or by immersing yourself in water for at least 1 hour.")
        #General Notes
    if player.race == "Hadozee":
        Hmo1 = dice(8)
        Hmo2 = dice(8)
        Hmod = Hmo1 + Hmo2
        Hbase = 57
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.ability_scores = abilityscores(param, player.ability_scores)
        player.creaturetype = "Humanoid"
        player.speed["Walking"] = 30
        player.racenotes.append("Your Climbing speed is the same as your walking speed")
        player.speed["Climbing"] = player.speed["Walking"]
        player.racenotes.append("Dexterous Feet: As a bonus action, you can use your feet to manipulate an object, open or close a door or container, or pick up or set down a Tiny object.")
        #Combat Notes
        player.racenotes.append("Glide (see notes)")
        player.notes.append("Glide: If you are not incapacitated or wearing heavy armor, you can extend your skin membranes and glide. When you do so, you can perform the following aerial maneuvers:\nYou can move up to 5 feet horizontally for every 1 foot you descend in the air, at no movement cost to you.\nWhen you would take damage from a fall, you can use your reaction to reduce the fall's damage to 0.")
        player.racenotes.append("Hadozee Resilience (see notes)")
        player.notes.append(f"Hadozee Resilience: The magic that runs in your veins heightens your natural defenses. When you take damage, you can use your reaction to roll a d6. Add your proficiency bonus to the number rolled, ({player.profbonus}), and reduce the damage you take by an amount equal to that total (minimum of 0 damage).\nYou can use this trait {player.profbonus} times. You regain all expended uses when you finish a long rest.")
        #Combat Notes
    if player.race == "HalfElf":
        Hmo1 = dice(8)
        Hmo2 = dice(8)
        Hmod = Hmo1 + Hmo2
        Hbase = 57
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Elvi"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.ability_scores["Charisma"] += 2
        player.ability_scores = singleabilityscore(param, player.ability_scores)
        player.ability_scores = singleabilityscore(param, player.ability_scores)
        player.speed["Walking"] = 30
        player.creaturetype = "Humanoid"
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.racenotes.append("Fey Ancestry: You have advantage on saving throws against being charmed, and magic can’t put you to sleep.")
        #Combat Notes
        player.skills = skillprof2(param, player.skills) 
        if player.subrace == "Half-Elf: Aquatic Elf Descent":
            player.racenotes.append("Swim: You gain a swimming speed of 30 ft.")
            player.speed["Swimming"] = 30
        if player.subrace == "Half-Elf: Drow Descent":
            player.racenotes.append("Drow Magic(1) (see notes). More options are available at higher levels.")
            player.notes.append("Drow Magic(1): You know the Dancing Lights cantrip. More options are available at higher levels.")
            #Spell Notes for (1) and general notes for rest
            if player.level >= 3:
                player.racenotes.append("Drow Magic(2) (see notes)")
                player.notes.append("Drow Magic(2): You can cast the Faerie Fire spell once per day; you must finish a long rest in order to cast the spell again using this trait. Charisma is your spellcasting ability for this spell.")
            if player.level >= 5:
                player.racenotes.append("Drow Magic(3) (see notes)")
                player.notes.append("Drow Magic(3): You can also cast the Darkness spell once per day; you must finish a long rest in order to cast the spell again using this trait. Charisma is your spellcasting ability for this spell.")
        if (player.subrace == "Half-Elf: Moon Elf Descent") or (player.subrace == "Half-Elf: Sun Elf Descent"):
            VariantFeatures = ["Proficiencies", "Cantrip"]
            VariantFeatureRand = random.choice(VariantFeatures)
            if param == "Y":
                print("0 - Random")
                print("1 - Longsword, Shortsword, Shortbow, and Longbow Proficiency")
                print("2 - Wizard Cantrip")
                varfeat = int(input("Which variant feature would you prefer? "))
                if varfeat == 1:
                    profs = ["Longsword", "Shortsword", "Shortbow", "Longbow"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                if varfeat == 2:
                    player.racenotes.append("Wizard Cantrip (see notes)")
                    player.notes.append("Wizard Cantrip: You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it.")
                    #Spell Notes
                if varfeat == 0:
                    if VariantFeatureRand == "Proficiencies":
                        profs = ["Longsword", "Shortsword", "Shortbow", "Longbow"]
                        for prof in profs:
                            if prof not in player.proficiencies:
                                player.proficiencies.append(prof)
                    if VariantFeatureRand == "Cantrip":
                        player.racenotes.append("Wizard Cantrip")
                        player.notes.append("Wizard Cantrip: You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it.")
                    #Spell Notes
            if param == "N":
                if VariantFeatureRand == "Proficiencies":
                    profs = ["Longsword", "Shortsword", "Shortbow", "Longbow"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                if VariantFeatureRand == "Cantrip":
                    player.racenotes.append("Wizard Cantrip (see notes)")
                    player.notes.append("Wizard Cantrip: You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it.")               
                    #Spell Notes
        if player.subrace == "Half-Elf: Wood Elf Descent":
            VariantFeatures = ["Proficiencies", "Fleet of Foot", "Mask of the Wild"]
            VariantFeatureRand = random.choice(VariantFeatures)
            if param == "Y":
                print("0 - Random")
                print("1 - Longsword, Shortsword, Shortbow, and Longbow Proficiency")
                print("2 - Fleet of Foot: Walking Speed of 35 ft")
                print("3 - Mask of the Wild: You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.")
                varfeat = int(input("Which variant feature would you prefer? "))
                if varfeat == 1:
                    profs = ["Longsword", "Shortsword", "Shortbow", "Longbow"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                if varfeat == 2:
                    player.speed["Walking"] = 35
                if varfeat == 3:
                    player.racenotes.append("Mask of the Wild (see notes)")
                    player.notes.append("Mask of the Wild: You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.")
                    #General Notes
                if varfeat == 0:
                    if VariantFeatureRand == "Proficiencies":
                        profs = ["Longsword", "Shortsword", "Shortbow", "Longbow"]
                        for prof in profs:
                            if prof not in player.proficiencies:
                                player.proficiencies.append(prof)
                    if VariantFeatureRand == "Fleet of Foot":
                        player.speed["Walking"] = 35  
                    if VariantFeatureRand == "Mask of the Wild":  
                        player.racenotes.append("Mask of the Wild (see notes)")
                        player.notes.append("Mask of the Wild: You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.")
                        #General Notes
            if param == "N":
                if VariantFeatureRand == "Proficiencies":
                    profs = ["Longsword", "Shortsword", "Shortbow", "Longbow"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)               
                if VariantFeatureRand == "Fleet of Foot":
                    player.speed["Walking"] = 35  
                if VariantFeatureRand == "Mask of the Wild":  
                    player.racenotes.append("Mask of the Wild (see notes)")
                    player.notes.append("Mask of the Wild: You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.")       
                    #General Notes
    if player.race == "Halfling":
        Hmo1 = dice(6)
        Hmo2 = dice(6)
        Hmod = Hmo1 + Hmo2
        Hbase = 28
        Wmo1 = 1
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 35
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Hafl"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.ability_scores["Dexterity"] += 2
        player.speed["Walking"] = 25
        player.creaturetype = "Humanoid"
        player.racenotes.append("Lucky: When you roll a 1 on the d20 for an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll.")
        #Combat Notes
        player.racenotes.append("Brave: You have advantage on saving throws against being frightened.")
        #Combat Notes
        player.racenotes.append("Halfling Nimbleness: You can move through the space of any creature that is of a size larger than yours.")
        #General Notes
        if player.subrace == "Ghostwise Halfling":
            player.ability_scores["Wisdom"] += 1
            player.racenotes.append("Silent Speech (see notes)")
            player.notes.append("Silent Speech: You can speak telepathically to any creature within 30 feet of you. The creature understands you only if the two of you share a language. You can speak telepathically in this way to one creature at a time.")
            #General Notes
        if player.subrace == "Lightfoot Halfling":
            player.ability_scores["Charisma"] += 1
            player.racenotes.append("Naturally Stealthy: You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you.")
            #General Notes
        if player.subrace == "Stout Halfling":
            player.ability_scores["Constitution"] += 1
            player.racenotes.append("Stout Resilience: You have advantage on saving throws against poison, and you have resistance against poison damage.")
            #General Notes
    if player.race == "Half-Orc":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 58
        Wmo1 = dice(6)
        Wmo2 = dice(6)
        Wmod = Wmo1 + Wmo2
        Wbase = 140
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Orc"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.ability_scores["Strength"] += 2
        player.ability_scores["Constitution"] += 1
        player.speed["Walking"] = 30
        player.creaturetype = "Humanoid"
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.skills.append(dnd_tools.skills["Intimidation"])
        player.racenotes.append("Relentless Endurance (see notes)")
        player.notes.append("Relentless Endurance: When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can’t use this feature again until you finish a long rest.")
        #Combat Notes
        player.racenotes.append("Savage Attacks (see notes)")
        player.notes.append("Savage Attacks: When you score a critical hit with a melee weapon attack, you can roll one of the weapon’s damage dice one additional time and add it to the extra damage of the critical hit.")
        #Combat Notes
    if player.race == "Harengon":
        Hmo1 = dice(12)
        Hmo2 = dice(12)
        Hmo3 = dice(12)
        Hmo4 = dice(12)
        Hmod = Hmo1 + Hmo2 + Hmo3 + Hmo4
        Hbase = 42
        Wmo1 = dice(6)
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 25
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.ability_scores = abilityscores(param, player.ability_scores)
        player.creaturetype = "Humanoid"
        player.speed["Walking"] = 30
        player.racenotes.append(f"Hare-Trigger: You can add your proficiency bonus, {player.profbonus}, to your initiative rolls.")
        #initiative notes
        player.skills.append(dnd_tools.skills["Perception"])
        player.racenotes.append("Lucky Footwork (see notes)")
        player.notes.append("Lucky Footwork: When you fail a Dexterity saving throw, you can use your reaction to roll a d4 and add it to the save, potentially turning the failure into a success. You can't use this reaction if you're prone or your speed is 0.")
        #Combat Notes
        player.racenotes.append("Rabbit Hop (see notes)")
        player.notes.append(f"Rabbit Hop: As a bonus action, you can jump a number of feet equal to five times your proficiency bonus, or {5*player.profbonus} feet, without provoking opportunity attacks. You can use this trait only if your speed is greater than 0. You can use it {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
        #General Notes
    if player.race == "Hedge":
        Hmo1 = dice(6)
        Hmo2 = dice(6)
        Hmod = Hmo1 + Hmo2
        Hbase = 35
        Wmo1 = dice(4)
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 30
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Hedg"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.ability_scores["Charisma"] += 2
        player.ability_scores["Wisdom"] += 1
        player.speed["Walking"] = 25
        player.creaturetype = "Humanoid"
        player.racenotes.append("Natural Burrowers (see notes)")
        player.notes.append("Natural Burrowers: You have a burrowing speed of 15 feet. You are capable of burrowing through soil, but are unable to dig through anything more substantial with just your clawed hands.")
        player.speed["Burrowing"] = 15
        player.racenotes.append("Spiny Quills (see notes)")
        player.notes.append("Spiny Quills: The backs of hedges are covered with spiny quills, which makes it impossible for hedges to wear armor. These quills provide exceptional protection, therefore you have a base armor class of 14 + your Dexterity modifier. Even though you can’t wear armor, you can still benefit from the armor class bonus provided by shields so long as you are proficient with them.")
        #General Notes
        player.racenotes.append("Curl Up (see notes)")
        player.notes.append("Curl Up: You can use your action to curl up, exposing attackers to a wall of your toughened quills. While curled up you cannot move, attack, or cast spells with somatic components, and your base armor class becomes 19. You cannot benefit from any Dexterity bonus to armor class while curled up, but you can still use shields.\nAny creature that misses you with a melee attack while you are curled up takes 2d4 points of piercing damage from your sharp quills. If a creature hits you while you are curled up, you are knocked prone in your space at the end of the turn. You may uncurl yourself at any point during your turn.")
        #General Notes
        player.racenotes.append("Forest Magic (see notes)")
        player.notes.append("Forest Magic: You have a deep connection to the magic of the Wood. You know the Druidcraft cantrip. Additionally, you can cast Animal Messenger as a 2nd level spell once with this trait, and regain the ability to do so after a short or long rest. Charisma is your spellcasting ability for these spells.")
        #Spell Notes
        player.racenotes.append("Speak With Bugs (see notes)")
        player.notes.append("Speak With Bugs: Through sounds and gestures, you can communicate simple ideas with creatures of the beast subtype that represent insects, spiders, worms, and other creepy crawlies, regardless of their size.")
        #General Notes
    if player.race == "Hexblood":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.ability_scores = abilityscores(param, player.ability_scores)
        player.creaturetype = "Fey"
        player.speed["Walking"] = 30
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.racenotes.append("Eerie Token (see notes)")
        player.racenotes.append("Eerie Token: As a bonus action, you can harmlessly remove a lock of your hair, one of your nails, or one of your teeth. This token is imbued with magic until you finish a long rest. While the token is imbued in this way, you can take these actions:\nTelepathic Message - As an action, you can send a telepathic message to the creature holding or carrying the token, as long as you are within 10 miles of it. The message can contain up to twenty-five words.\nRemote Viewing - If you are within 10 miles of the token, you can enter a trance as an action. The trance lasts for 1 minute, but it ends early if you dismiss it (no action required) or are incapacitated. During this trance, you can see and hear from the token as if you were located where it is. While you are using your senses at the token’s location, you are blinded and deafened in regard to your own surroundings. When the trance ends, the token is harmlessly destroyed.\nOnce you create a token using this feature, you can’t do so again until you finish a long rest, at which point your missing part regrows.")
        #Combat Notes
        player.racenotes.append("Hex Magic (see notes)")
        player.racenotes.append("Hex Magic: You can cast the Disguise Self and Hex spells with this trait. Once you cast either of these spells with this trait, you can’t cast that spell with it again until you finish a long rest. You can also cast these spells using any spell slots you have.\nIntelligence, Wisdom, or Charisma is your spellcasting ability for these spells (choose the ability when you gain this lineage).")    
        #General Notes
    if player.race == "Hobgoblin":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Gobl"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.ability_scores["Constitution"] += 2
        player.ability_scores["Intelligence"] += 1
        player.speed["Walking"] = 30
        player.creaturetype = "Goblinoid"
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.proficiencies = martwepprof(param, player.proficiencies)
        player.proficiencies = martwepprof(param, player.proficiencies)
        if "Light Armor" not in player.proficiencies:
            player.proficiencies.append("Light Armor")
        player.racenotes.append("Saving Face (see notes)")
        player.notes.append("Saving Face: Hobgoblins are careful not to show weakness in front of their allies, for fear of losing status. If you miss with an attack roll or fail an ability check or a saving throw, you can gain a bonus to the roll equal to the number of allies you can see within 30 feet of you (maximum bonus of +5). Once you use this trait, you can't use it again until you finish a short or long rest.")
        #Combat Notes
    if player.race == "Human":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.speed["Walking"] = 30
        player.creaturetype = "Humanoid"
        if player.subrace == "Human":
            player.ability_scores["Charisma"] += 1
            player.ability_scores["Constitution"] += 1
            player.ability_scores["Dexterity"] += 1
            player.ability_scores["Intelligence"] += 1
            player.ability_scores["Strength"] += 1
            player.ability_scores["Wisdom"] += 1        
        if player.subrace == "Variant Human":
            player.ability_scores = singleabilityscore(param, player.ability_scores)
            player.ability_scores = singleabilityscore(param, player.ability_scores)
            player.skills = skillprof(param, player.skills)
            player.racenotes.append("Feat: You gain one feat of your choice.")  
            #Add in ability to choose feat
    if player.race == "Jerbeen":
        Hmo1 = dice(4)
        Hmo2 = dice(4)
        Hmod = Hmo1 + Hmo2
        Hbase = 28
        Wmo1 = dice(2)
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 20
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Jerb"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.ability_scores["Dexterity"] += 2
        player.ability_scores["Charisma"] += 1
        player.speed["Walking"] = 30
        player.creaturetype = "Humanoid"
        player.racenotes.append("Standing Leap: Your base long jump is 30 feet, and your base high jump is 15 feet, with or without a running start.")
        #General Notes
        player.racenotes.append("Nimbleness: You can move through the space of any creature that is of a size larger than yours.")
        #General Notes
        player.racenotes.append("Take Heart (see notes)")
        player.notes.append("Take Heart: You have advantage on Strength saving throws and saving throws against being frightened as long as you are within 5 feet of an ally who isn’t frightened or incapacitated that you can both see and hear.")
        #Combat Notes
        player.racenotes.append("Team Tactics: You can use the Help action as a bonus action.")
        #Combat Notes
    if player.race == "Kalashtar":
        Hmo1 = dice(6)
        Hmo2 = dice(6)
        Hmod = Hmo1 + Hmo2
        Hbase = 64
        Wmo1 = dice(6)
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Quo"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.creaturetype = "Humanoid"
        player.ability_scores["Wisdom"] += 2
        player.ability_scores["Charisma"] += 1
        player.speed["Walking"] = 30
        player.damresimm.append("Psychic Damage Resistance")
        player.racenotes.append("Dual Mind: You have advantage on all Wisdom saving throws.")
        #Combat Notes
        player.racenotes.append("Mind Link (see notes)")
        player.notes.append("Mind Link: You can speak telepathically to any creature you can see, provided the creature is within a number of feet of you equal to 10 times your level. You don't need to share a language with the creature for it to understand your telepathic utterances, but the creature must be able to understand at least one language.\nWhen you're using this trait to speak telepathically to a creature, you can use your action to give that creature the ability to speak telepathically with you for 1 hour or until you end this effect as an action. To use this ability, the creature must be able to see you and must be within this trait's range. You can give this ability to only one creature at a time; giving it to a creature takes it away from another creature who has it.")
        #General Notes
        player.racenotes.append("Severed from Dreams (see notes)")
        player.notes.append("Severed from Dreams: Kalashtar sleep, but they don't connect to the plane of dreams as other creatures do. Instead, their minds draw from the memories of their otherworldly spirit while they sleep. As such, you are immune to spells and other magical effects that require you to dream, like Dream, but not to spells and other magical effects that put you to sleep, like Sleep.")
        #General Notes
    if player.race == "Kender":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.ability_scores = abilityscores(param, player.ability_scores)
        player.creaturetype = "Humanoid"
        player.speed["Walking"] = 30
        SkillsList = [
            dnd_tools.skills["Insight"], 
            dnd_tools.skills["Investigation"], 
            dnd_tools.skills["SleightofHand"], 
            dnd_tools.skills["Stealth"], 
            dnd_tools.skills["Survival"]
        ]
        player.skills = oneskillfromlist(param, player.skills, SkillsList)
        player.racenotes.append("Fearless (see notes)")
        player.notes.append("Fearless: You have advantage on saving throws you make to avoid or end the frightened condition on yourself. When you fail a saving throw to avoid or end the frightened condition on yourself, you can choose to succeed instead. Once you succeed on a saving throw in this way, you can't do so again until you finish a long rest.")
        #Combat Notes
        player.racenotes.append("Taunt (see notes)")
        player.notes.append("Taunt: You have an extraordinary ability to fluster creatures. As a bonus action, you can unleash a string of provoking words at a creature within 60 feet of yourself that can hear and understand you. The target must succeed on a Wisdom saving throw, or it has disadvantage on attack rolls against targets other than you until the start of your next turn. The DC equals 8 + your proficiency bonus + your Intelligence, Wisdom, or Charisma modifier (choose when you select this race).\nYou can use this bonus action a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.")
        #Combat Notes
    if player.race == "Kenku":
        Hmo1 = dice(8)
        Hmo2 = dice(8)
        Hmod = Hmo1 + Hmo2
        Hbase = 52
        Wmo1 = dice(6)
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 50
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Aura"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.ability_scores["Dexterity"] += 2
        player.ability_scores["Wisdom"] += 1
        player.speed["Walking"] = 30
        player.creaturetype = "Avian Humanoid"
        player.racenotes.append("Expert Forgery (see notes)")
        player.notes.append("Expert Forgery: You can duplicate other creatures' handwriting and craftwork. You have advantage on all checks made to produce forgeries or duplicates of existing objects.")
        SkillsList = [
            dnd_tools.skills["Acrobatics"],
            dnd_tools.skills["Deception"], 
            dnd_tools.skills["Stealth"],
            dnd_tools.skills["SleightofHand"]
        ]
        player.skills = oneskillfromlist(param, player.skills, SkillsList)
        player.skills = oneskillfromlist(param, player.skills, SkillsList)
        player.racenotes.append("Mimicry (see notes)")
        player.notes.append("Mimicry: You can mimic sounds you have heard, including voices. A creature that hears the sounds can tell they are imitations with a successful Insight check opposed by your Deception check.")
        #General Notes
        player.languages.append("In addition to the languages you know, you can only speak using your Mimicry trait.")
        #General Notes
    if player.race == "Kobold":
        Hmo1 = dice(4)
        Hmo2 = dice(4)
        Hmod = Hmo1 + Hmo2
        Hbase = 25
        Wmo1 = 1
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 25
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Drac"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.creaturetype = "Humanoid"
        player.ability_scores["Strength"] -= 2
        player.ability_scores["Dexterity"] += 2
        player.speed["Walking"] = 30
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.racenotes.append("Grovel, Cower, and Beg (see notes)")
        player.notes.append("Grovel, Cower, and Beg: As an action on your turn, you can cower pathetically to distract nearby foes. Until the end of your next turn, your allies gain advantage on attack rolls against enemies within 10 feet of you that you can see. Once you use this trait, you can't use it again until you finish a short or long rest.")
        #Combat Notes
        player.racenotes.append("Pack Tactics: You have advantage on an attack roll against a creature if at least one of your allies is within 5 feet of the creature and the ally isn't incapacitated.")
        #Combat Notes
        player.racenotes.append("Sunlight Sensitivity (see notes)")
        player.notes.append("Sunlight Sensitivity: You have disadvantage on attack rolls and on Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight.")
        #Combat Notes
    if player.race == "Leonin":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 66
        Wmo1 = dice(6)
        Wmo2 = dice(6)
        Wmod = Wmo1 + Wmo2
        Wbase = 180
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Leon"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.creaturetype = "Humanoid"
        player.ability_scores["Constitution"] += 2
        player.ability_scores["Strength"] += 1
        player.speed["Walking"] = 35
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.racenotes.append("Claws (see notes)")
        player.notes.append("Claws: Your claws are natural weapons, which you can use to make unarmed strikes. If you hit with them, you can deal slashing damage equal to 1d4 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.")
        SkillsList = [
            dnd_tools.skills["Athletics"],
            dnd_tools.skills["Intimidation"], 
            dnd_tools.skills["Perception"], 
            dnd_tools.skills["Survival"]
        ]
        player.skills = oneskillfromlist(param, player.skills, SkillsList)
        player.racenotes.append("Daunting Roar (see notes)")
        player.notes.append("Daunting Roar: As a bonus action, you can let out an especially menacing roar. Creatures of your choice within 10 feet of you that can hear you must succeed on a Wisdom saving throw or become frightened of you until the end of your next turn. The DC of the save equals 8 + your proficiency bonus + your Constitution modifier. Once you use this trait, you can't use it again until you finish a short or long rest.")
        #Combat Notes
    if player.race == "Lizardfolk":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 57
        Wmo1 = dice(6)
        Wmo2 = dice(6)
        Wmod = Wmo1 + Wmo2
        Wbase = 120
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Drac"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.creaturetype = "Humanoid"
        player.ability_scores["Constitution"] += 2
        player.ability_scores["Wisdom"] += 1
        player.speed["Walking"] = 30
        player.racenotes.append("Your swim speed is the same as your walking speed.")
        player.speed["Swimming"] = player.speed["Walking"]
        player.racenotes.append("Bite (see notes)")
        player.notes.append("Bite: Your fanged maw is a natural weapon, which you can use to make unarmed strikes. If you hit with it, you deal piercing damage equal to 1d6 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.")
        player.racenotes.append("Cunning Artisan (see notes)")
        player.notes.append("Cunning Artisan: As part of a short rest, you can harvest bone and hide from a slain beast, construct, dragon, monstrosity, or plant creature of size small or larger to create one of the following items: a shield, a club, a javelin, or 1d4 darts or blowgun needles. To use this trait, you need a blade, such as a dagger, or appropriate artisan's tools, such as leatherworker's tools.")
        player.racenotes.append("Hold Breath: You can hold your breath for up to 15 minutes at a time.")
        SkillsList = [
            dnd_tools.skills["AnimalHandling"], 
            dnd_tools.skills["Nature"], 
            dnd_tools.skills["Perception"], 
            dnd_tools.skills["Stealth"], 
            dnd_tools.skills["Survival"]
        ]
        player.skills = oneskillfromlist(param, player.skills, SkillsList)
        player.skills = oneskillfromlist(param, player.skills, SkillsList)
        player.racenotes.append("Natural Armor (see notes)")
        player.notes.append("Natural Armor: You have tough, scaly skin. When you aren't wearing armor, your AC is 13 + your Dexterity modifier. You can use your natural armor to determine your AC if the armor you wear would leave you with a lower AC. A shield's benefits apply as normal while you use your natural armor.")
        #General Notes
        player.racenotes.append("Hungry Jaws (see notes)")
        player.notes.append("Hungry Jaws: In battle, you can throw yourself into a vicious feeding frenzy. As a bonus action, you can make a special attack with your bite. If the attack hits, it deals its normal damage, and you gain temporary hit points equal to your Constitution modifier (minimum of 1), and you can't use this trait again until you finish a short or long rest.")
        #Combat Notes
    if player.race == "Locathah":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Aqua"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.creaturetype = "Humanoid"
        player.ability_scores["Strength"] += 2
        player.ability_scores["Dexterity"] += 1
        player.racenotes.append("Natural Armor (see notes)")
        player.notes.append("Natural Armor: You have tough, scaly skin. When you aren’t wearing armor, your AC is 12 + your Dexterity modifier. You can use your natural armor to determine your AC if the armor you wear would leave you with a lower AC. A shield’s benefits apply as normal while you use your natural armor.")
        #General Notes
        player.skills.append(dnd_tools.skills["Athletics"])
        player.skills.append(dnd_tools.skills["Perception"])
        player.racenotes.append("Leviathan Will: You have advantage on saving throws against being charmed, frightened, paralyzed, poisoned, stunned, or put to sleep.")
        #General Notes
        player.racenotes.append("Limited Amphibiousness: You can breathe air and water, but you need to be submerged at least once every 4 hours to avoid suffocating.")
        #General Notes
        player.speed["Walking"] = 30
        player.racenotes.append("Your swim speed is the same as your walking speed.")
        player.speed["Swimming"] = player.speed["Walking"]
    if player.race == "Loxodon":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 79
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 295
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Loxo"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.creaturetype = "Humanoid"
        player.ability_scores["Constitution"] += 2
        player.ability_scores["Wisdom"] += 1
        player.speed["Walking"] = 30
        player.racenotes.append("Powerful Build: You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.")
        #General Notes
        player.racenotes.append("Loxodon Serenity: You have advantage on saving throws against being charmed or frightened.")
        #Combat Notes
        player.racenotes.append("Natural Armor (see notes)")
        player.notes.append("Natural Armor: You have thick, leathery skin. When you aren't wearing armor, your AC is 12 + your Constitution modifier. You can use your natural armor to determine your AC if the armor you wear would leave you with a lower AC. A shield's benefits apply as normal while you use your natural armor.")
        #General Notes
        player.racenotes.append("Trunk (see notes)")
        player.notes.append("Trunk: You can grasp things with your trunk, and you can use it as a snorkel. It has a reach of 5 feet, and it can lift a number of pounds equal to five times your Strength score. You can use it to do the following simple tasks: lift, drop, hold, push, or pull an object or a creature; open or close a door or a container; grapple someone; or make an unarmed strike. Your DM might allow other simple tasks to be added to that list of options.\nYour trunk can't wield weapons or shields or do anything that requires manual precision, such as using tools or magic items or performing the somatic components of a spell.")
        #Combat Notes
        player.racenotes.append("Keen Smell: Thanks to your sensitive trunk, you have advantage on Perception, Survival, and Investigation checks that involve smell.")
        #General Notes
    if player.race == "Luma":
        Hmo1 = dice(4)
        Hmo2 = dice(4)
        Hmod = Hmo1 + Hmo2
        Hbase = 32
        Wmo1 = 1
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 25
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.languages.append(dnd_tools.UAur)
        player.creaturetype = "Avian Humanoid"
        player.ability_scores["Charisma"] += 2
        player.speed["Walking"] = 25
        player.racenotes.append("Glide (see notes)")
        player.notes.append("Glide: Using your feathered arms, you can slow your fall, and glide short distances. When falling you can use your reaction to spread your arms, stiffen your wing feathers, and slow your descent. While doing so, you continue to fall gently at a speed of 60 feet per round, taking no fall damage when you land. If you would fall at least 10 feet in this way, you may fly up to your movement speed in one direction you choose, although you cannot choose to move upwards, landing in the space you finish your movement. You cannot glide while carrying heavy weapons or wielding a shield (though you may drop any held items as part of your reaction to spread your arms). You cannot glide while wearing heavy armor, or if you are encumbered.")
        #General Notes
        player.racenotes.append("Wing Flap (see notes)")
        player.notes.append("Wing Flap: As a bonus action, you can use your powerful feathered arms to propel yourself upward a distance equal to half your movement speed. You can use it in conjunction with a regular jump, but not while gliding.")
        #Combat Notes
        player.racenotes.append("Touched: Sorcerer Cantrip (see notes)")
        player.notes.append("Touched: You know one cantrip from the sorcerer spell list. Charisma is your spellcasting ability for this cantrip.")
        #Spell Notes
        player.racenotes.append("Fated (see notes)")
        player.notes.append("Fated: Whether by luck or a guiding presence, you always seem to find your way. You can choose to reroll any attack, skill check, or saving throw. You can decide to do this after your roll, but only before the outcome of the roll has been determined. You can’t use this feature again until you have completed a long rest.")
        #Combat Notes
        if player.subrace == "Sable Luma":
            player.ability_scores["Constitution"] += 1
            player.racenotes.append("Hard to Read (see notes)")
            player.notes.append("Hard to Read: Your innate eccentricities make it hard for other folk to figure you out. When someone performs a Wisdom (Insight) check against you, they have disadvantage on their roll. Additionally, you gain advantage on Charisma (Deception) checks made against creatures that are not lumas.")
            #General Notes
            player.racenotes.append("Resilience: You have advantage on saving throws against poison.")
            #General Notes
            player.damresimm.append("Poison Damage Resistance")
        if player.subrace == "Sera Luma":
            player.ability_scores["Wisdom"] += 1
            player.skills.append(dnd_tools.skills["Performance"])
            player.racenotes.append("Songbird (see notes)")
            player.notes.append("Songbird: When you perform, you can demonstrate the innate and mystical power of your Charisma. You may cast the charm person spell once per long rest. This spell does not require any somatic components to cast. Charisma is your spellcasting ability for this spell.")
            #General Notes
    if player.race == "Mapach":
        Hmo1 = dice(6)
        Hmo2 = dice(6)
        Hmod = Hmo1 + Hmo2
        Hbase = 47
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 85
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Mapa"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.ability_scores["Wisdom"] += 2
        player.ability_scores["Constitution"] += 1
        player.speed["Walking"] = 30
        player.creaturetype = "Humanoid"
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.racenotes.append("In addition to Darkvision, Mapachs are most comfortable under the cloak of night.")
        player.racenotes.append("Expert Climbers: You have a climb speed of 20 feet.")
        player.speed["Climbing"] = 20
        player.damresimm.append("Poison Damage Resistance")
        player.racenotes.append("Resilience: You have advantage on saving throws against poison.")
        #General Notes
        player.racenotes.append("Scroungecraft (see notes)")
        player.notes.append("Scroungecraft: You are proficient with tinker’s tools. Additionally, you have the ability to construct crude but functional versions of common items using materials present in your surroundings. You may spend 10 minutes to craft these materials into any tool or piece of adventuring gear worth 30 gold pieces or less. The item will be completely functional, even capable of passing for a disguise (if you crafted an article of clothing). Tools, along with any other item that would logically break on its first use (caltrops, arrows), will become useless afterward. Scroungecrafted items will otherwise last 1 hour before falling apart.\nDepending on the materials available, a Game Master (GM) may rule that you cannot craft an item in this way. For example, a vial of acid might be easy to make if you happen to be near a nest of acidic beetle larvae, or bark can be bound into a makeshift flask, but it would be difficult to create a passable facsimile of silken robes from a pile of leaves.\nShould you have access to the proper materials, you can spend 8 hours converting an item you have scroungecrafted in this way into a permanent version, so long as you start this process before the item falls apart. Items crafted in such a way will function exactly as a normal version of the item, and if you have proficiency in the tools used to craft them, they can even look professionally-crafted. Otherwise, they retain a rather rough, cobbled-together appearance. You can also use scroungecraft to repair broken equipment, provided you have the materials on hand. Though, how long your repairs hold together is up to the GM.")
        if "Tinker's Tools" not in player.proficiencies:
            player.proficiencies.append("Tinker's Tools")
        player.racenotes.append("Skulker: You have advantage on Stealth checks made in dim light and darkness.")
        #General Notes
    if player.race == "Minotaur":
        Hmo1 = dice(8)
        Hmo2 = dice(8)
        Hmod = Hmo1 + Hmo2
        Hbase = 64
        Wmo1 = dice(6)
        Wmo2 = dice(6)
        Wmod = Wmo1 + Wmo2
        Wbase = 175
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Mino"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.creaturetype = "Humanoid"
        player.ability_scores["Strength"] += 2
        player.ability_scores["Constitution"] += 1
        player.speed["Walking"] = 30
        player.racenotes.append("Horns (see notes)")
        player.notes.append("Horns: Your horns are natural melee weapons, which you can use to make unarmed strikes. If you hit with them, you deal piercing damage equal to 1d6 +your Strength modifier. instead of the bludgeoning damage normal for an unarmed strike.")
        player.racenotes.append("Goring Rush: Immediately after you use the Dash action on your turn and move at least 20 feet, you can make one melee attack with your horns as a bonus action.")
        #Combat Notes
        player.racenotes.append("Hammering Horns (see notes)")
        player.notes.append("Hammering Horns: Immediately after you hit a creature with a melee attack as part of the Attack action on your turn, you can use a bonus action to attempt to shove that target with your horns. The target must be no more than one size larger than you and within 5 feet of you. Unless it succeeds on a Strength saving throw against a DC equal to 8 + your proficiency bonus+ your Strength modifier, you push it up to 10 feet away from you.")
        #Combat Notes
        SkillsList = [dnd_tools.skills["Intimidation"], dnd_tools.skills["Persuasion"]]
        player.skills = oneskillfromlist(param, player.skills, SkillsList)
    if player.race == "Orc":
        Hmo1 = dice(8)
        Hmo2 = dice(8)
        Hmod = Hmo1 + Hmo2
        Hbase = 64
        Wmo1 = dice(6)
        Wmo2 = dice(6)
        Wmod = Wmo1 + Wmo2
        Wbase = 175
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Orc"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.creaturetype = "Humanoid"
        player.ability_scores["Strength"] += 2
        player.ability_scores["Constitution"] += 1
        player.ability_scores["Intelligence"] -= 2
        player.speed["Walking"] = 30
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.racenotes.append("Aggressive (see notes)")
        player.notes.append("Aggressive: As a bonus action, you can move up to your movement speed toward a hostile creature you can see or hear. You must end this move closer to the enemy than you started.")
        #Combat Notes
        player.skills.append(dnd_tools.skills["Intimidation"])
        player.racenotes.append("Powerful Build: You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.")
        #General Notes
    if player.race == "Owlin":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.creaturetype = "Humanoid"
        player.ability_scores = abilityscores(param, player.ability_scores)
        player.speed["Walking"] = 30
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.racenotes.append("Flight: Thanks to your wings, you have a flying speed equal to your walking speed. You can't use this flying speed if you're wearing medium or heavy armor.")
        player.speed["Flying"] = player.speed["Walking"]
        player.skills.append(dnd_tools.skills["Stealth"])
    if player.race == "Plasmoid":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.ability_scores = abilityscores(param, player.ability_scores)
        player.creaturetype = "Ooze"
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.racenotes.append("Amorphous (see notes)")
        player.notes.append("Amorphous: You can squeeze through a space as narrow as 1 inch wide, provided you are wearing and carrying nothing. You have advantage on ability checks you make to initiate or escape a grapple.")
        #General Notes
        player.racenotes.append("Hold Breath: You can hold your breath for 1 hour.")
        #General Notes
        player.damresimm.append("Acid Damage Resistance")
        player.damresimm.append("Poison Damage Resistance")
        player.racenotes.append("You have advantage on saving throws against being poisoned.")
        #General Notes
        player.racenotes.append("Shape Self (see notes)")
        player.notes.append("Shape Self: As an action, you can reshape your body to give yourself a head, one or two arms, one or two legs, and makeshift hands and feet, or you can revert to a limbless blob. While you have a humanlike shape, you can wear clothing and armor made for a Humanoid of your size.\nAs a bonus action, you can extrude a pseudopod that is up to 6 inches wide and 10 feet long or reabsorb it into your body. As part of the same bonus action, you can use this pseudopod to manipulate an object, open or close a door or container, or pick up or set down a Tiny object. The pseudopod contains no sensory organs and can't attack, activate magic items, or lift more than 10 pounds.")
        #General Notes
    if player.race == "Raptor (Bird)":
        Hmo1 = dice(6)
        Hmo2 = dice(6)
        Hmod = Hmo1 + Hmo2
        Hbase = 35
        Wmo1 = 1
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 25
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.languages.append(dnd_tools.UAur)
        player.ability_scores["Dexterity"] += 2
        player.speed["Walking"] = 25
        player.creaturetype = "Avian Humanoid"
        player.racenotes.append("Glide (see notes)")
        player.notes.append("Glide: Using your feathered arms, you can slow your fall, and glide short distances. When falling you can use your reaction to spread your arms, stiffen your wing feathers, and slow your descent. While doing so, you continue to fall gently at a speed of 60 feet per round, taking no fall damage when you land. If you would fall at least 10 feet in this way, you may fly up to your movement speed in one direction you choose, although you cannot choose to move upwards, landing in the space you finish your movement. You cannot glide while carrying heavy weapons or wielding a shield (though you may drop any held items as part of your reaction to spread your arms). You cannot glide while wearing heavy armor, or if you are encumbered.")
        #General Notes
        player.racenotes.append("Talons (see notes)")
        player.racenotes.append("Talons: Your sharp claws aid you in unarmed combat and while climbing. Your damage for an unarmed strike is 1d4 piercing damage. Additionally, you have advantage on Strength (Athletics) checks made to climb any surface your talons could reasonably grip.")
        #General Notes
        player.skills.append(dnd_tools.skills["Perception"])
        profs = ["Longbow", "Shortbow", "Spear"]
        for prof in profs:
            if prof not in player.proficiencies:
                player.proficiencies.append(prof)
        player.racenotes.append("Your familiarity with the longbow means that it is not considered a heavy weapon for you.")
        #General Notes
        if player.subrace == "Maran Raptor (Bird)":
            player.ability_scores["Intelligence"] += 1
            player.racenotes.append("Swimmer: You have a swimming speed of 25 feet.")
            player.speed["Swimming"] = 25
            player.racenotes.append("Patient: When you react with a readied action, you have advantage on the first attack roll, skill check, or ability check you make as a part of that action.")
            #General Notes
        if player.subrace == "Mistral Raptor (Bird)":
            player.ability_scores["Wisdom"] += 1
            player.skills.append(dnd_tools.skills["Acrobatics"])
            player.racenotes.append("Aerial Defense: Creatures that attack you while you are falling, gliding, or jumping have disadvantage on their attack roll.")
            #Combat Notes
    if player.race == "Reborn":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.ability_scores = abilityscores(param, player.ability_scores)
        player.creaturetype = "Humanoid"
        player.speed["Walking"] = 30
        player.racenotes.append("Deathless Nature (see notes)")
        player.notes.append("Deathless Nature: You have escaped death, a fact represented by the following benefits:\nYou have advantage on saving throws against disease and being poisoned, and you have resistance to poison damage.\nYou have advantage on death saving throws.\nYou don’t need to eat, drink, or breathe.\nYou don’t need to sleep, and magic can’t put you to sleep. You can finish a long rest in 4 hours if you spend those hours in an inactive, motionless state, during which you retain consciousness.")
        #General Notes
        player.racenotes.append("Knowledge from a Past Life (see notes)")
        player.notes.append(f"Knowledge from a Past Life: You temporarily remember glimpses of the past, perhaps faded memories from ages ago or a previous life. When you make an ability check that uses a skill, you can roll a d6 immediately after seeing the number on the d20 and add the number on the d6 to the check. You can use this feature {player.profbonus} times, and you regain all expended uses when you finish a long rest.")    
        #General Notes
    if player.race == "Satyr":
        Hmo1 = dice(8)
        Hmo2 = dice(8)
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Sylv"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.ability_scores["Charisma"] += 2
        player.ability_scores["Dexterity"] += 1
        player.creaturetype = "Fey"
        player.speed["Walking"] = 35
        player.racenotes.append("Ram: You can use your head and horns to make unarmed strikes. If you hit with them, you deal bludgeoning damage equal to 1d4 + your Strength modifier.")
        #Combat Notes
        player.racenotes.append("Magic Resistance: You have advantage on saving throws against spells and other magical effects.")
        #Combat Notes
        player.racenotes.append("Mirthful Leaps (see notes)")
        player.notes.append("Mirthful Leaps: Whenever you make a long or high jump, you can roll a d8 and add the number rolled to the number of feet you cover, even when making a standing jump. This extra distance costs movement as normal.")
        #General Notes
        player.skills.append(dnd_tools.skills["Performance"])
        player.skills.append(dnd_tools.skills["Persuasion"])
        player.proficiencies = musicalinstr(param, player.proficiencies)
    if player.race == "Sharkin":
        Hmo1 = dice(4)
        Hmo2 = dice(4)
        Hmod = Hmo1 + Hmo2 + 2
        Hbase = 71
        Wmo1 = dice(4)
        Wmo2 = dice(4) + 3
        Wmod = Wmo1 + Wmo2
        Wbase = 160
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Aqua"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.creaturetype = "Humanoid"
        player.ability_scores["Constitution"] += 1
        player.ability_scores["Strength"] += 2
        player.speed["Walking"] = 30
        player.racenotes.append("Your swimming speed is 60 feet")
        player.speed["Swimming"] = 60
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.racenotes.append("Amphibious: You can breath air and water.")
        #General Notes
        player.racenotes.append("Fearless: Everyone has a disadvantage on Intimidation checks on you.")
        #General Notes
        if player.subrace == "Blue Sharkin":
            player.racenotes.append("Graceful Swimmer: Your swimming speed increases to 90 feet.")
            player.speed["Swimming"] = 90
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Basking Sharkin":
            player.racenotes.append("Tough Hide: You gain a +1 bonus to your AC.")
            #General Notes
            player.damresimm.append("Non-Magical Piercing Damage")
            player.damresimm.append("Poison Damage Resistance")
            player.racenotes.append("Huge Liver: You have advantage on saving throws against being poisoned.")
            #General Notes
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Bull Sharkin":
            player.racenotes.append("Oceanic Rage (see notes)")
            player.notes.append("Oceanic Rage: You may enter a rage as a bonus action. While raging, you gain a +2 to damage rolls at 1st level, +3 at 9th, and +4 at 16th. You have advantage on Strength Checks and Strength saving throws. You have resistance to bludgeoning, piercing, and slashing damage. If you are able to cast spells, you can't cast them or concentrate on them while raging. Your rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven't attacked a hostile creature since your last turn or taken damage since then. You can end your rage as a bonus action, and once you have raged you cannot do so again until you finish a long rest.")
            #Combat Notes
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Cookie Cutter Sharkin":
            player.racenotes.append("Photophores: You chest and stomach can emit 5 feet of dim light in the dark, while underwater you have advantage on Stealth checks.")
            #General Notes
            player.skills.append(dnd_tools.skills["Stealth"])
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Goblin Sharkin":
            player.skills.append(dnd_tools.skills["Investigation"])
            player.racenotes.append("Ampullae of Lorenzini: You have advantage on Perception and Investigation checks.")
            #General Notes
            player.racenotes.remove("Darkvision (see notes)")
            player.notes.remove(dnd_tools.Darkvision)
            player.racenotes.append("Superior Darkvision (see notes)")
            player.notes.append("Superior Darkvision: You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.")
            #Darkvision+ Notes
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Hammerhead Sharkin":
            player.skills.append(dnd_tools.skills["Investigation"])
            player.racenotes.append("Ampullae of Lorenzini: You have advantage on Perception and Investigation checks.")
            #General Notes
            player.racenotes.append("Lateral Vision: You gain a +2 bonus to your passive Perception.")
            #General Notes
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Leopard Sharkin":
            player.racenotes.append("Nictitating Membrane: You are able to see in murky environments and you have advantage on saving throws against being blinded.")
            #General Notes
            player.racenotes.append("Oxygen Efficient: Your short and long rest times are cut in half.")
            #General Notes
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Mako Sharkin":
            player.damresimm.append("Cold Damage Resistance")
            player.racenotes.append("Speedy Swimmer: Your swimming speed increases to 120 feet.")
            player.speed["Swimming"] = 120
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Nurse Sharkin":
            player.skills.append(dnd_tools.skills["Investigation"])
            player.racenotes.append("Ampullae of Lorenzini: You have advantage on Perception and Investigation checks.")
            #General Notes
            player.racenotes.remove("Darkvision (see notes)")
            player.notes.remove(dnd_tools.Darkvision)
            player.racenotes.append("Modified Darkvision: You have darkvision up to 90ft. You see dim light as if it were bright light, and you see darkness as if it were dim light.")
            #Darkvision+ Notes
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Thresher Sharkin":
            player.damresimm.append("Cold Damage Resistance")
            player.racenotes.append("Whiplash (see notes)")
            player.notes.append(f"Whiplash: As a bonus action, your tail can be used to strike a creature, potentially stunning it. The creature must make Constitution saving throw against a DC equal to 8 + your Constitution modifier + your proficiency bonus. On a failed save it becomes stunned until the end of its next turn. On a successful save, it does not get stunned. You can use this trait {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
            #Combat Notes
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Tiger Sharkin":
            player.racenotes.remove("Darkvision (see notes)")
            player.notes.remove(dnd_tools.Darkvision)
            player.racenotes.append("Modified Darkvision: You have darkvision up to 90ft. You see dim light as if it were bright light, and you see darkness as if it were dim light.")
            #Darkvision+ Notes
            player.racenotes.append("Shell Crusher: You gain a +2 to attack and damage rolls against armored creatures.")
            #Combat Notes
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Whale Sharkin":
            player.damresimm.append("Non-magical Bludgeoning damage")
            player.racenotes.append("Whale Toughness: Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.")
            #General Notes
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Great White Sharkin":
            player.racenotes.append("Blood Frenzy (see notes)")
            player.notes.append(f"Blood Frenzy: With the ability to smell blood from a range of 3 miles, the smell of it can excite your hunger for battle. When you make an attack against a creature that doesn't have all its hit points, you can choose to make the attack with advantage. You can use this trait {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
            #General Notes
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Cladoselache":
            player.skills.append(dnd_tools.skills["Investigation"])
            player.racenotes.append("Ampullae of Lorenzini: You have advantage on Perception and Investigation checks.")
            #General Notes
            player.racenotes.append("Speedy Swimmer: Your swimming speed increases to 90 feet.")
            player.speed["Swimming"] = 90
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Cretoxyrhina":
            player.skills.append(dnd_tools.skills["Investigation"])
            player.racenotes.append("Ampullae of Lorenzini: You have advantage on Perception and Investigation checks.")
            #General Notes
            player.racenotes.append("Blood Frenzy (see notes)")
            player.notes.append(f"Blood Frenzy: With the ability to smell blood from a range of 3 miles, the smell of it can excite your hunger for battle. When you make an attack against a creature that doesn't have all its hit points, you can choose to make the attack with advantage. You can use this trait {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
            #General Notes
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Edestus":
            player.skills.append(dnd_tools.skills["Investigation"])
            player.racenotes.append("Ampullae of Lorenzini: You have advantage on Perception and Investigation checks.")
            #General Notes
            player.racenotes.append("Razored Teeth: You gain a +2 bonus to attack and damage rolls against unarmored creatures.")
            #Combat Notes
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Helicoprion":
            player.skills.append(dnd_tools.skills["Investigation"])
            player.racenotes.append("Ampullae of Lorenzini: You have advantage on Perception and Investigation checks.")
            #General Notes
            player.racenotes.append("Hacksaw Jaw: You gain an extra 1d4 slashing damage bonus, against creatures that don't have all their hit points.")
            #Combat Notes
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Hybodus":
            player.racenotes.append("Dorsal Stinger (see notes)")
            DorsalStingerDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                DorsalStingerDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                DorsalStingerDmg = "3d6"
            if player.level == 20:
                DorsalStingerDmg = "4d6"
            player.notes.append(f"Dorsal Stinger: As a bonus action, you may pierce your foe. Your fins have stingers that does {DorsalStingerDmg} piercing damage.")
            #Combat Notes
            player.racenotes.append("Stream Burst: Whilst swimming in a body of water, you can use a bonus action to perform the dash action.")
            #Combat Notes
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Megalodon":
            player.skills.append(dnd_tools.skills["Investigation"])
            player.racenotes.append("Ampullae of Lorenzini: You have advantage on Perception and Investigation checks.")
            #General Notes
            player.racenotes.append("Blood Frenzy (see notes)")
            player.notes.append(f"Blood Frenzy: With the ability to smell blood from a range of 3 miles, the smell of it can excite your hunger for battle. When you make an attack against a creature that doesn't have all its hit points, you can choose to make the attack with advantage. You can use this trait {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
            #General Notes
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Ptychodus":
            player.racenotes.append("Shell Crusher: You gain a +2 to attack and damage rolls against armored creatures.")
            #Combat Notes
            player.racenotes.append("Stream Burst: Whilst swimming in a body of water, you can use a bonus action to perform the dash action.")
            #Combat Notes
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Scapanorhynchus":
            player.skills.append(dnd_tools.skills["Investigation"])
            player.racenotes.append("Ampullae of Lorenzini: You have advantage on Perception and Investigation checks.")
            #General Notes
            player.racenotes.remove("Darkvision (see notes)")
            player.notes.remove(dnd_tools.Darkvision)
            player.racenotes.append("Superior Darkvision (see notes)")
            player.notes.append("Superior Darkvision: You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.")
            #Darkvision+ Notes
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Stethacanthus":
            player.racenotes.append("Dorsal Stinger (see notes)")   
            DorsalStingerDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                DorsalStingerDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                DorsalStingerDmg = "3d6"
            if player.level == 20:
                DorsalStingerDmg = "4d6"
            player.notes.append(f"Dorsal Stinger: As a bonus action, you may pierce your foe. Your fins have stingers that does {DorsalStingerDmg} piercing damage.")
            #Combat Notes
            player.racenotes.remove("Darkvision (see notes)")
            player.notes.remove(dnd_tools.Darkvision)
            player.racenotes.append("Superior Darkvision (see notes)")
            player.notes.append("Superior Darkvision: You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.")
            #Darkvision+ Notes
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if player.subrace == "Xenacanthus":      
            player.racenotes.append("Graceful Swimmer: Your swimming speed increases to 90 feet.")
            player.speed["Swimming"] = 90
            player.racenotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((player.level >= 5) and (player.level < 10)):
                ViciousBiteDmg = "2d6"
            if ((player.level >= 10) and (player.level < 20)):
                ViciousBiteDmg = "3d6"
            if player.level == 20:
                ViciousBiteDmg = "4d6"
            player.notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
    if player.race == "Shifter":
        player.speed["Walking"] = 30
        player.creaturetype = "Humanoid"
        player.racenotes.append("Darkvision (see notes)") 
        player.racenotes.append(dnd_tools.Darkvision)
        #Darkvision notes   
        player.racenotes.append("Shifting (see notes)")
        player.notes.append("Shifting: As a bonus action, you can assume a more bestial appearance. This transformation lasts for 1 minute, until you die, or until you revert to your normal appearance as a bonus action. When you shift, you gain temporary hit points equal to your level + your Constitution modifier (minimum of 1 temporary hit point). You also gain additional benefits that depend on your shifter subrace, described below. Once you shift, you can't do so again until you finish a short or long rest.")
        #General/Combat Notes
        if player.subrace == "Beasthide Shifter":
            Hmo1 = dice(4)
            Hmo2 = dice(4)
            Hmod = Hmo1 + Hmo2
            Hbase = 62
            Wmo1 = dice(4)
            Wmo2 = dice(4)
            Wmod = Wmo1 + Wmo2
            Wbase = 130
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            player.height = str(tl)
            player.weight = str(hy)
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.ability_scores["Constitution"] += 2
            player.ability_scores["Strength"] += 1
            player.skills.append(dnd_tools.skills["Athletics"])
            player.racenotes.append("Shifting Feature: Whenever you shift, you gain 1d6 additional temporary hit points. While shifted, you have a + 1 bonus to your Armor Class.")
            #General Notes
        if player.subrace == "Longtooth Shifter":
            Hmo1 = dice(8)
            Hmo2 = dice(8)            
            Hmod = Hmo1 + Hmo2
            Hbase = 54
            Wmo1 = dice(4)
            Wmo2 = dice(4)
            Wmod = Wmo1 + Wmo2
            Wbase = 90
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            player.height = str(tl)
            player.weight = str(hy)
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.ability_scores["Strength"] += 2
            player.ability_scores["Dexterity"] += 1
            player.skills.append(dnd_tools.skills["Intimidation"])
            player.racenotes.append("Shifting Feature (see notes)")
            player.notes.append("Shifting Feature: While shifted, you can use your elongated fangs to make an unarmed strike as a bonus action. If you hit with your fangs, you can deal piercing damage equal to 1d6 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.")
        if player.subrace == "Swiftstride Shifter":
            Hmo1 = dice(6)
            Hmo2 = dice(6)        
            Hmod = Hmo1 + Hmo2
            Hbase = 58
            Wmo1 = dice(4)
            Wmo2 = dice(4)
            Wmod = Wmo1 + Wmo2
            Wbase = 110   
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            player.height = str(tl)
            player.weight = str(hy)        
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.ability_scores["Dexterity"] += 2
            player.ability_scores["Charisma"] += 1
            player.skills.append(dnd_tools.skills["Acrobatics"])
            player.racenotes.append("Shifting Feature: While shifted, your walking speed increases by 10 feet. Additionally, you can move up to 10 feet as a reaction when a creature ends its turn within 5 feet of you. This reactive movement doesn't provoke opportunity attacks.")
            player.speed["Walking"] += 10
            #Combat Notes
        if player.subrace == "Wildhunt Shifter":    
            Hmo1 = dice(10)
            Hmo2 = dice(10)
            Hmod = Hmo1 + Hmo2
            Hbase = 50
            Wmo1 = dice(4)
            Wmo2 = dice(4)
            Wmod = Wmo1 + Wmo2
            Wbase = 70
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            player.height = str(tl)
            player.weight = str(hy)
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.ability_scores["Wisdom"] += 2
            player.ability_scores["Dexterity"] += 1
            player.skills.append(dnd_tools.skills["Survival"])
            player.racenotes.append("Shifting Feature (see notes)")
            player.notes.append("Shifting Feature: While shifted, you have advantage on Wisdom checks, and no creature within 30 feet of you can make an attack roll with advantage against you, unless you're incapacitated.")
            #Combat Notes
    if player.race == "Simic Hybrid":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        SimHybLang = [dnd_tools.languages["Elvi"], dnd_tools.languages["Veda"]]
        if param == "Y":
            print("0 - Random")
            print("1 - Elvish")
            print("2 - Vedalken")
            shlang = int(input("Choose your symic hybrid language. "))
            if shlang == 1:
                langs = ["Elvi"]
                for lang in langs:
                    if lang in player.slang:
                        player.languages.append(dnd_tools.languages[lang])
                        player.slang.remove(lang)  
            if shlang == 2:
                langs = ["Veda"]
                for lang in langs:
                    if lang in player.slang:
                        player.languages.append(dnd_tools.languages[lang])
                        player.slang.remove(lang)  
            if shlang == 0:
                SimicHybridLang = random.choice(SimHybLang)
                for lang in langs:
                    if lang in player.slang:
                        player.languages.append(dnd_tools.languages[lang])
                        player.slang.remove(lang)  
        if param == "N":
            SimicHybridLang = random.choice(SimHybLang)
            langs = [str(SimicHybridLang)]
            for lang in langs:
                if lang in player.slang:
                    player.languages.append(dnd_tools.languages[lang])
                    player.slang.remove(lang)  
        player.creaturetype = "Humanoid"
        player.ability_scores["Constitution"] += 2
        player.ability_scores = singleabilityscore(param, player.ability_scores)
        player.speed["Walking"] = 30
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.racenotes.append("Animal Enhancement(1) (see notes)")
        player.notes.append("Animal Enhancement(1): Your body has been altered to incorporate certain animal characteristics. You choose one animal enhancement now and a second enhancement at 5th level.\nAt 1st level, choose one of the following options:\nManta Glide - You have ray-like fins that you can use as wings to slow your fall or allow you to glide. When you fall and aren't incapacitated, you can subtract up to 100 feet from the fall when calculating falling damage, and you can move up to 2 feet horizontally for every 1 foot you descend. \nNimble Climber - You have a climbing speed equal to your walking speed.\nUnderwater Adaptation - You can breathe air and water, and you have a swimming speed equal to your walking speed.")
        #General/Combat Notes
        if player.level >= 5:
            player.racenotes.append("Animal Enhancement(2) (see notes)")
            AnimalEnhDMG = "2d10"
            if ((player.level >= 11) and (player.level < 17)):
                AnimalEnhDMG = "3d10"
            if player.level > 17:
                AnimalEnhDMG = "4d10"
            player.notes.append(f"Animal Enhancement(2): Your body evolves further, developing new characteristics. Choose one of the options you didn't take at 1st level, or one of the following options:\nGrappling Appendage - You have two special appendages growing alongside your arms. Choose whether they're both claws or tentacles. As an action, you can use one of them to try to grapple a creature. Each one is also a natural weapon, which you can use to make an unarmed strike. If you hit with it, the target takes bludgeoning damage equal to 1d6 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike. Immediately after hitting, you can try to grapple the target as a bonus action. These appendages can't precisely manipulate anything and can't wield weapons, magic items, or other specialized equipment.\nCarapace - Your skin in places is covered by a thick shell. You gain a +1 bonus to AC when you're not wearing heavy armor.\nAcid Spit - As an action, you can spray acid from glands in your mouth, targeting one creature or object you can see within 30 feet of you. The target takes {AnimalEnhDMG} acid damage unless it succeeds on a Dexterity saving throw against a DC equal to 8 + your Constitution modifier + your proficiency bonus. You can use this trait a number of times equal to your Constitution modifier (minimum of once), and you regain all expended uses of it when you finish a long rest.")
    if player.race == "Strig":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 46
        Wmo1 = dice(6)
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 80
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.languages.append(dnd_tools.UAur)
        player.creaturetype = "Avian Humanoid"  
        player.ability_scores["Strength"] += 2
        player.speed["Walking"] = 30
        player.racenotes.append("Glide (see notes)")
        player.notes.append("Glide: Using your feathered arms, you can slow your fall, and glide short distances. When falling you can use your reaction to spread your arms, stiffen your wing feathers, and slow your descent. While doing so, you continue to fall gently at a speed of 60 feet per round, taking no fall damage when you land. If you would fall at least 10 feet in this way, you may fly up to your movement speed in one direction you choose, although you cannot choose to move upwards, landing in the space you finish your movement. You cannot glide while carrying heavy weapons or wielding a shield (though you may drop any held items as part of your reaction to spread your arms). You cannot glide while wearing heavy armor, or if you are encumbered.")
        #General Notes
        player.racenotes.append("Talons (see notes)")
        player.notes.append("Talons: Your sharp claws aid you in unarmed combat and while climbing. Your damage for an unarmed strike is 1d4 piercing damage. Additionally, you have advantage on Strength (Athletics) checks made to climb any surface your talons could reasonably grip.")
        #General Notes
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.racenotes.append("Patterned Feathers: You have advantage on Dexterity (Stealth) checks when you attempt to hide in a forest.")
        if player.subrace == "Stout Strig":
            player.ability_scores["Constitution"] += 1
            player.skills.append(dnd_tools.skills["Intimidation"])
            player.racenotes.append("Brawler: When you successfully attack a target with your talons, you can choose to grapple that target as a bonus action.")
            #Combat Notes
        if player.subrace == "Swift Strig":
            player.ability_scores["Dexterity"] += 1
            player.speed["Walking"] = 35
            player.skills.append(dnd_tools.skills["Survival"])
    if player.race == "Tabaxi":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 58
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 90
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.ability_scores["Dexterity"] += 2
        player.ability_scores["Charisma"] += 1
        player.speed["Walking"] = 30
        player.creaturetype = "Humanoid"
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.racenotes.append("Feline Agility (see notes)")
        player.notes.append("Feline Agility: Your reflexes and agility allow you to move with a burst of speed. When you move on your turn in combat, you can double your speed until the end of the turn. Once you use this trait, you can't use it again until you move 0 feet on one of your turns.")
        #Combat Notes
        player.racenotes.append("Cat's Claws (see notes)")
        player.notes.append("Cat's Claws: Because of your claws, you have a climbing speed of 20 feet. In addition, your claws are natural weapons, which you can use to make unarmed strikes. If you hit with them, you deal slashing damage equal to 1d4 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.")
        player.speed["Climbing"] = 20
        player.skills.append(dnd_tools.skills["Perception"])
        player.skills.append(dnd_tools.skills["Stealth"])
    if player.race == "Tiefling":
        Hmo1 = dice(8)
        Hmo2 = dice(8)
        Hmod = Hmo1 + Hmo2
        Hbase = 57
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Infe"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.creaturetype = "Humanoid"
        player.ability_scores["Charisma"] += 2
        player.speed["Walking"] = 30
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.damresimm.append("Fire Damage Resistance")
        if player.subrace == "Asmodeus Subject Tiefling":
            player.ability_scores["Intelligence"] += 1
            player.racenotes.append("Infernal Legacy(1) (see notes). More options are available at higher levels.")
            player.notes.append("Infernal Legacy(1): You know the Thaumaturgy cantrip. Charisma is your spellcasting ability for this spell. More options are available at higher levels.")
            #Spell Notes for (1), General for rest
            if player.level >= 3:
                player.racenotes.append("Infernal Legacy(2) (see notes)")
                player.notes.append("Infernal Legacy(2): You can cast the Hellish Rebuke spell as a 2nd-level spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for this spell.")
            if player.level >= 5:
                player.racenotes.append("Infernal Legacy(3) (see notes)")
                player.notes.append("Infernal Legacy(3): You can cast the Darkness spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for this spell.")
        if player.subrace == "Baalzebul Subject Tiefling":
            player.ability_scores["Intelligence"] += 1
            player.racenotes.append("Legacy of Maladomini(1) (see notes). More options are available at higher levels.")
            player.notes.append("Legacy of Maladomini(1): You know the Thaumaturgy cantrip. Charisma is your spellcasting ability for this spell.")
            #Spell Notes for (1), General for rest
            if player.level >= 3:
                player.racenotes.append("Legacy of Maladomini(2) (see notes)")
                player.notes.append("Legacy of Maladomini(2): You can cast the Ray of Sickness spell once as a 2nd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
            if player.level >= 5:
                player.racenotes.append("Legacy of Maladomini(3) (see notes)")
                player.notes.append("Legacy of Maladomini(3): You can also cast the Crown of Madness spell once. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
        if player.subrace == "Dispater Subject Tiefling":
            player.ability_scores["Dexterity"] += 1
            player.racenotes.append("Legacy of Dis(1) (see notes). More options are available at higher levels.")
            player.notes.append("Legacy of Dis(1): You know the Thaumaturgy cantrip. Charisma is your spellcasting ability for this spell.")
            #Spell Notes for (1), General for rest
            if player.level >= 3:
                player.racenotes.append("Legacy of Dis(2) (see notes)")
                player.notes.append("Legacy of Dis(2): You can cast the Disguise Self spell once as a 2nd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
            if player.level >= 5:
                player.racenotes.append("Legacy of Dis(3) (see notes)")            
                player.notes.append("Legacy of Dis(3): You can also cast the Detect Thoughts spell once. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
        if player.subrace == "Fierna Subject Tiefling":
            player.ability_scores["Wisdom"] += 1
            player.racenotes.append("Legacy of Phlegethos(1) (see notes). More options are available at higher levels.")
            player.notes.append("Legacy of Phlegethos(1): You know the Friends cantrip. Charisma is your spellcasting ability for this spell.")
            #Spell Notes for (1), General for rest
            if player.level >= 3:
                player.racenotes.append("Legacy of Phlegethos(2) (see notes)")
                player.notes.append("Legacy of Phlegethos(2): You can cast the Charm Person spell once as a 2nd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
            if player.level >= 5:
                player.racenotes.append("Legacy of Phlegethos(3) (see notes)")        
                player.notes.append("Legacy of Phlegethos(3): You can also cast the Suggestion spell once. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
        if player.subrace == "Glasya Subject Tiefling":
            player.ability_scores["Dexterity"] += 1
            player.racenotes.append("Legacy of Malbolge(1) (see notes). More options are available at higher levels.")
            player.notes.append("Legacy of Malbolge(1): You know the Minor Illusion cantrip. Charisma is your spellcasting ability for this spell.")
            #Spell Notes for (1), General for rest
            if player.level >= 3:
                player.racenotes.append("Legacy of Malbolge(2) (see notes)")
                player.notes.append("Legacy of Malbolge(2): You can cast the Disguise Self spell once as a 2nd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
            if player.level >= 5:
                player.racenotes.append("Legacy of Malbolge(3) (see notes)")        
                player.notes.append("Legacy of Malbolge(3): You can also cast the Invisibility spell once as a 3rd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
        if player.subrace == "Levistus Subject Tiefling":
            player.ability_scores["Constitution"] += 1
            player.racenotes.append("Legacy of Stygia(1) (see notes). More options are available at higher levels.")
            player.notes.append("Legacy of Stygia(1): You know the Ray of Frost cantrip. Charisma is your spellcasting ability for this spell.")
            #Spell Notes for (1), General for rest
            if player.level >= 3:
                player.racenotes.append("Legacy of Stygia(2) (see notes)")
                player.notes.append("Legacy of Stygia(2): You can cast the Armor of Agathys spell once as a 2nd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
            if player.level >= 5:
                player.racenotes.append("Legacy of Stygia(3) (see notes)")        
                player.notes.append("Legacy of Stygia(3): You can also cast the Darkness spell once. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
        if player.subrace == "Mammon Subject Tiefling":
            player.ability_scores["Intelligence"] += 1
            player.racenotes.append("Legacy of Minauros(1) (see notes). More options are available at higher levels.")
            player.notes.append("Legacy of Minauros(1): You know the Mage Hand cantrip. Charisma is your spellcasting ability for this spell.")
            #Spell Notes for (1), General for rest
            if player.level >= 3:
                player.racenotes.append("Legacy of Minauros(2) (see notes)")
                player.notes.append("Legacy of Minauros(2): You can cast the Tenser's Floating Disk spell once as a 2nd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
            if player.level >= 5:
                player.racenotes.append("Legacy of Minauros(3) (see notes)")        
                player.notes.append("Legacy of Minauros(3): You can also cast the Arcane Lock spell once. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
        if player.subrace == "Mephistopheles Subject Tiefling":
            player.ability_scores["Intelligence"] += 1
            player.racenotes.append("Legacy of Cania(1) (see notes). More options are available at higher levels.")
            player.notes.append("Legacy of Cania(1): You know the Mage Hand cantrip. Charisma is your spellcasting ability for this spell.")
            #Spell Notes for (1), General for rest
            if player.level >= 3:
                player.racenotes.append("Legacy of Cania(2) (see notes)")
                player.notes.append("Legacy of Cania(2): You can cast the Burning Hands spell once as a 2nd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
            if player.level >= 5:
                player.racenotes.append("Legacy of Cania(3) (see notes)")        
                player.notes.append("Legacy of Cania(3): You can also cast the Flame Blade spell once as a 3rd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
        if player.subrace == "Zariel Subject Tiefling":
            player.ability_scores["Strength"] += 1
            player.racenotes.append("Legacy of Avernus(1) (see notes). More options are available at higher levels.")
            player.notes.append("Legacy of Avernus(1): You know the Thaumaturgy cantrip. Charisma is your spellcasting ability for this spell.")
            #Spell Notes for (1), General for rest
            if player.level >= 3:
                player.racenotes.append("Legacy of Avernus(2) (see notes)")
                player.notes.append("Legacy of Avernus(2): You can cast the Searing Smite spell once as a 2nd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
            if player.level >= 5:
                player.racenotes.append("Legacy of Avernus(3) (see notes)")    
                player.notes.append("Legacy of Avernus(3): You can also cast the Branding Smite spell once as a 3rd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
    if player.race == "Thri-Kreen":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.ability_scores = abilityscores(param, player.ability_scores)
        player.creaturetype = "Monstrosity"
        player.speed["Walking"] = 35
        player.racenotes.append("Chameleon Carapace (see notes)")
        player.notes.append("Chameleon Carapace: While you aren't wearing armor, your carapace gives you a base Armor Class of 13 + your Dexterity modifier.\nAs an action, you can change the color of your carapace to match the color and texture of your surroundings, giving you advantage on Dexterity (Stealth) checks made to hide in those surroundings.")
        #General Notes
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.racenotes.append("Secondary Arms (see notes)")
        player.notes.append("Secondary Arms: You have two slightly smaller secondary arms below your primary pair of arms. The secondary arms can manipulate an object, open or close a door or container, pick up or set down a Tiny object, or wield a weapon that has the light property.")
        #General Notes
        player.racenotes.append("Sleepless (see notes)")
        player.notes.append("Sleepless: You do not require sleep and can remain conscious during a long rest, though you must still refrain from strenuous activity to gain the benefit of the rest.")
        #General Notes
        player.racenotes.append("Thri-kreen Telepathy (see notes)")
        player.notes.append("Thri-kreen Telepathy: Without the assistance of magic, you can't speak the non-thri-kreen languages you know. Instead you use telepathy to convey your thoughts. You have the magical ability to transmit your thoughts mentally to willing creatures you can see within 120 feet of yourself. A contacted creature doesn't need to share a language with you to understand your thoughts, but it must be able to understand at least one language. Your telepathic link to a creature is broken if you and the creature move more than 120 feet apart, if either of you is incapacitated, or if either of you mentally breaks the contact (no action required).")
        #General Notes
    if player.race == "Tortle":
        Hmo1 = dice(12)
        Hmo2 = dice(12)
        Hmo3 = dice(12)
        Hmod = Hmo1 + Hmo2 + Hmo3
        Hbase = 43
        Wmo1 = dice(6)
        Wmo2 = dice(6)
        Wmod = Wmo1 + Wmo2
        Wbase = 310
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Aqua"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.ability_scores["Strength"] += 2
        player.ability_scores["Wisdom"] += 1
        player.speed["Walking"] = 30
        player.creaturetype = "Humanoid"
        player.racenotes.append("Claws (see notes)")
        player.notes.append("Claws: Your claws are natural weapons, which you can use to make unarmed strikes. If you hit with them, you deal slashing damage equal to 1d4 + your Strength modifier, instead of bludgeoning damage normal for an unarmed strike.")
        player.racenotes.append("Hold Breath (see notes)")
        player.notes.append("Hold Breath: You can hold your breath for up to 1 hour at a time. Tortles aren't natural swimmers, but they can remain underwater for some time before needing to come up for air.")
        #General Notes
        player.racenotes.append("Natural Armor (see notes)")
        player.notes.append("Natural Armor: Due to your shell and the shape of your body, you are ill-suited to wearing armor. Your shell provides ample protection, however; it gives you a base AC of 17 (your Dexterity modifier doesn't affect this number). You gain no benefit from wearing armor, but if you are using a shield, you can apply the shield's bonus as normal.")
        #General Notes
        player.racenotes.append("Shell Defense (see notes)")
        player.notes.append("Shell Defense: You can withdraw into your shell as an action. until you emerge, you gain a +4 bonus to AC, and you have advantage on Strength and Constitution saving throws. While in your shell, you are prone, your speed is 0 and can't increase, you have disadvantage on Dexterity saving throws, you can't take reactions, and the only action you can take is a bonus action to emerge from your shell.")
        #General Notes
        player.skills.append(dnd_tools.skills["Survival"])
    if player.race == "Triton":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 54
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 90
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Prim"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.ability_scores["Strength"] += 1
        player.ability_scores["Constitution"] += 1
        player.ability_scores["Charisma"] += 1
        player.speed["Walking"] = 30
        player.creaturetype = "Humanoid"
        player.racenotes.append("You have a swimming speed of 30 feet.")
        player.speed["Swimming"] = 30
        player.racenotes.append("Amphibious: You can breathe air and water.")
        #General Notes
        player.racenotes.append("Control Air and Water (see notes)")
        player.notes.append("Control Air and Water: A child of the sea, you can call on the magic of elemental air and water. You can cast Fog Cloud with this trait. Starting at 3rd level, you can cast Gust of Wind with it, and starting at 5th level, you can also cast Wall of Water with it. Once you cast a spell with this trait, you can't cast that spell with it again until you finish a long rest. Charisma is your spellcasting ability for these spells.")
        #General Notes
        player.racenotes.append("Emissary of the Sea (see notes)")
        player.notes.append("Emissary of the Sea: Aquatic beasts have an extraordinary affinity with your people. You can communicate simple ideas with beasts that can breathe water. They can understand the meaning of your words, though you have no special ability to understand them in return.")
        #General Notes
        player.damresimm.append("Cold Damage Resistance")
        player.racenotes.append("Guardians of the Depths: You ignore any of the drawbacks caused by a deep, underwater environment.")
        #General Notes
    if player.race == "Vedalken":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 64
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)        
        langs = ["Veda"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.creaturetype = "Humanoid"
        player.ability_scores["Intelligence"] += 2
        player.ability_scores["Wisdom"] += 1
        player.speed["Walking"] = 30
        player.racenotes.append("Vedalken Dispassion: You have advantage on all Intelligence, Wisdom, and Charisma saving throws.")
        #Combat Notes
        SkillsList = [
            dnd_tools.skills["Arcana"],
            dnd_tools.skills["History"],
            dnd_tools.skills["Investigation"],
            dnd_tools.skills["Medicine"],
            dnd_tools.skills["Performance"],
            dnd_tools.skills["SleightofHand"]
        ]
        player.racenotes, player.skills = vedsixskillprof(param, player.racenotes, player.skills, SkillsList)
        player.proficiencies = vedartisantools(param, player.proficiencies)
        player.racenotes.append("Partially Amphibious (see notes)")
        player.notes.append("Partially Amphibious: By absorbing oxygen through your skin, you can breathe underwater for up to 1 hour. Once you've reached that limit, you can't use this trait again until you finish a long rest.")
        #General Notes
    if player.race == "Verdan":
        Hmo1 = dice(4)
        Hmo2 = dice(4)
        Hmod = Hmo1 + Hmo2
        Hbase = 41
        Wmo1 = 1
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 35
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)        
        langs = ["Gobl"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.ability_scores["Constitution"] += 1
        player.ability_scores["Charisma"] += 2
        player.speed["Walking"] = 30
        player.creaturetype = "Humanoid"
        player.racenotes.append("Black Blood Healing (see notes)")
        player.notes.append("Black Blood Healing: The black blood that is a sign of your people's connection to That-Which-Endures boosts your natural healing. When you roll a 1 or 2 on any Hit Die you spend at the end of a short rest, you can reroll the die and must use the new roll.")
        #General Notes
        player.racenotes.append("Limited Telepathy (see notes)")
        player.notes.append("Limited Telepathy: You can telepathically speak to any creature you can see within 30 feet of you. You don't need to share a language with the creature for it to understand your telepathy, but it must be able to understand at least one language. This process of communication is slow and limited, allowing you to transmit and receive only simple ideas and straightforward concepts.")
        #General Noted
        player.skills.append(dnd_tools.skills["Persuasion"])
        player.racenotes.append("Telepathic Insight: Your mind's connection to the world around you strengthens your will. You have advantage on all Wisdom and Charisma saving throws.")
        #Combat Notes
    #Currently Here
    if player.race == "Vulpin":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 50
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 80
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)        
        langs = ["Vulp"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.ability_scores["Intelligence"] += 2
        player.ability_scores["Charisma"] += 1
        player.speed["Walking"] = 30
        player.creaturetype = "Humanoid"
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.racenotes.append("Bite (see notes)")
        player.notes.append("Bite: You have sharp fangs that enable you to make natural bite attacks. You can choose to bite as an unarmed strike that deals 1d6 points of piercing damage, which can be calculated using either your Strength or Dexterity modifier for both the attack roll and damage bonus.")
        player.racenotes.append("Evasive: You add your Intelligence modifier as a bonus on all Dexterity saving throws.")
        #General/Combat Notes
        player.racenotes.append("Bewitching Guile(1) (see notes). More options are available at higher levels.")
        player.notes.append("Bewitching Guile(1): You can cast Charm Person as a 1st level spell with this trait, and regain the ability to do so when you finish a long rest. Intelligence is your spellcasting ability for this spell.")
        #General notes for all (3)
        if player.level >= 3:
            player.racenotes.append("Bewitching Guile(2) (see notes)")
            player.notes.append("Bewitching Guile(2): You can cast Ambush Prey as a 2nd level spell with this trait, and regain the ability to do so when you finish a long rest. Intelligence is your spellcasting ability for this spell.")
        if player.level >= 5:
            player.racenotes.append("Bewitching Guile(3) (see notes)")
            player.notes.append("Bewitching Guile(3): You can cast Fear with this trait, and regain the ability to do so when you finish a long rest. Intelligence is your spellcasting ability for this spell.")
    if player.race == "Warforged":
        Hmo1 = dice(6)
        Hmo2 = dice(6)
        Hmod = Hmo1 + Hmo2
        Hbase = 60
        Wmo1 = 4
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 270
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)        
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.creaturetype = "Construct"
        player.ability_scores["Constitution"] += 2
        player.ability_scores = singleabilityscore(param, player.ability_scores)
        player.speed["Walking"] = 30
        player.racenotes.append("Constructed Resilience (see notes)")
        player.notes.append("Constructed Resilience: You were created to have remarkable fortitude, represented by the following benefits:\nYou have advantage on saving throws against being poisoned, and you have resistance to poison damage.\nYou don't need to eat, drink, or breathe.\nYou are immune to disease.\nYou don't need to sleep, and magic can't put you to sleep.")
        #General Nots
        player.racenotes.append("Sentry's Rest (see notes)")
        player.notes.append("Sentry's Rest: When you take a long rest, you must spend at least six hours in an inactive, motionless state, rather than sleeping. In this state, you appear inert, but it doesn't render you unconscious, and you can see and hear as normal.")
        #General Notes
        player.racenotes.append("Integrated Protection (see notes)")
        player.notes.append("Integrated Protection: Your body has built-in defensive layers, which can be enhanced with armor:\nYou gain a +1 bonus to Armor Class.\nYou can don only armor with which you have proficiency. To don armor, you must incorporate it into your body over the course of 1 hour, during which you remain in contact with the armor. To doff armor, you must spend 1 hour removing it. You can rest while donning or doffing armor in this way.\nWhile you live, your armor can't be removed from your body against your will.")
        #General Notes
        player.skills = skillprof(param, player.skills)
        player.proficiencies = artisantools(param, player.proficiencies)
    if player.race == "Wechselkind":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)        
        langs = ["Sylv"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)  
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.creaturetype = "Fey"
        player.ability_scores["Constitution"] += 2
        player.ability_scores["Charisma"] += 1
        player.speed["Walking"] = 25
        player.damresimm.append("Poison Damage Resistance")
        player.racenotes.append("Artificial Form (see notes)")
        player.notes.append("Artificial Form: As a constructed creature, your body functions differently than a normal person.\nYou have advantage on saving throws against being poisoned, and you have resistance to poison damage.\nYou are immune to disease. You don’t need to eat, drink, sleep, or breathe. You are still considered humanoid.")
        #General Notes
        player.racenotes.append("Faerie Glamour (see notes)")
        player.notes.append("Faerie Glamour: When the faerie leaves a wechselkind in place of a mortal child, they cover it with a glamour to make it appear identical to the child that was stolen. Over time this glamour fades, but a wechselkind can still call upon it in times of need.\nYou may cast the Disguise Self spell once with this trait, but only to take on the appearance of the child you were intended to replace, and you regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for this spell.")
        #General Notes
        player.racenotes.append("Childish Agility: You can move through the space of any creature that is of a size larger than yours.")
        #General Notes
        player.skills.append(dnd_tools.skills["Acrobatics"])
    if player.race == "Yuan-ti":
        Hmo1 = dice(10)
        Hmo2 = dice(10)
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = dice(4)
        Wmo2 = dice(4)
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        player.height = str(tl)
        player.weight = str(hy)
        langs = ["Abys", "Drac"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)          
        player.creaturetype = "Humanoid"
        player.ability_scores["Intelligence"] += 1
        player.ability_scores["Charisma"] += 2
        player.speed["Walking"] = 30
        player.racenotes.append("Darkvision (see notes)")
        player.notes.append(dnd_tools.Darkvision)
        #Darkvision notes
        player.racenotes.append("Innate Spellcasting (see notes)")
        player.notes.append("Innate Spellcasting: You know the Poison Spray cantrip. You can cast Animal Friendship an unlimited number of times with this trait, but you can target only snakes with it. Starting at 3rd level, you can also cast Suggestion with this trait. Once you cast it, you can't do so again until you finish a long rest. Charisma is your spellcasting ability for these spells.")
        #Spell/General Notes
        player.racenotes.append("Magic Resistance: You have advantage on saving throws against spells and other magical effects.")
        #Combat Notes
        player.damresimm.append("Poison Damage Immunity")
        player.racenotes.append("You are immune to the poisoned condition.")

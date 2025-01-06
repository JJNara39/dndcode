import random
import dnd_tools
from dnd_languagesskills import *


def dndCharGenBkg(param, player):    
    Actual_Background = [
            "Acolyte", "Anthropologist", "Archaeologist", "Ashari", "Astral Drifter", "Athlete", "Azorius Functionary", "Bandit Defector", "Boros Legionnaire", "Celebrity Adventurer’s Scion", "Charlatan", "City Watch", "Clan Crafter", "Clasp Member",
            "Cloistered Scholar", "Courtier", "Criminal", "Dimir Operative", "Entertainer", "Faceless", "Faction Agent", "Failed Merchant", "Far Traveler", "Feylost", "Fisher", "Folk Hero", "Gambler", "Gate Warden", "Giant Foundling", "Gladiator",
            "Golgari Agent", "Grey Hunter", "Grinner", "Grounded", "Gruul Anarch", "Guild Artisan", "Guild Merchant", "Haunted One", "Hermit", "House Agent", "Inheritor", "Investigator", "Izzet Engineer", "Knight", "Knight of the Order",
            "Knight of Solamnia", "Lorehold Student", "Lyceum Scholar", "Mage of High Sorcery", "Marine", "Mercenary Veteran", "Myriad Operative", "Noble", "Orzhov Representative", "Outlander", "Pirate", "Plaintiff", "Planar Philosopher",
            "Prismari Student", "Quandrix Student", "Rakdos Cultist", "Reformed Cultist", "Rewarded", "Rival Intern", "Ruined", "Rune Carver", "Sage", "Sailor", "Selesnya Initiate", "Shipwright", "Silverquill Student", "Simic Scientist", "Smuggler",
            "Soldier", "Spy", "Urban Bounty Hunter", "Urchin", "Uthgardt Tribe Member", "Volstrucker Agent", "Waterdhavian Noble", "Whitestone Rifle Corps", "Wildspacer", "Wind-Touched", "Witchlight Hand", "Witherbloom Student"
        ]
    backgrounds_commented = [
        "Acolyte (Insight, Religion)",
        "Anthropologist (Insight, Religion)",
        "Archaeologist (History, Survival)",
        "Ashari (Nature, Arcana/Survival)",
        "Astral Drifter (Insight, Religion)",
        "Athlete (Acrobatics, Athletics)",
        "Azorius Functionary (Insight, Intimidation)",
        "Bandit Defector (Deception, Survival)",
        "Boros Legionnaire (Athletics, Intimidation)",
        "Celebrity Adventurer’s Scion (Perception, Performance)",
        "Charlatan (Deception, Sleight of Hand)",
        "City Watch (Athletics, Insight)",
        "Clan Crafter (History, Insight)",
        "Clasp Member (Deception, Sleight of Hand/Survival)",
        "Cloistered Scholar (History, Arcana/Nature/Religion)",
        "Courtier (Insight, Persuasion)",
        "Criminal (Deception, Stealth)",
        "Dimir Operative (Deception, Stealth)",
        "Entertainer (Acrobatics, Performance)",
        "Faceless (Deception, Intimidation)",
        "Faction Agent (Insight, Intelligence-based-skill/Wisdom-based-skill/Charisma-based-skill)",
        "Failed Merchant (Investigation, Persuasion)",
        "Far Traveler (Insight, Perception)",
        "Feylost (Deception, Survival)",
        "Fisher (History, Survival)",
        "Folk Hero (Animal Handling, Survival)",
        "Gambler (Deception, Insight)",
        "Gate Warden (Persuasion, Survival)",
        "Giant Foundling (Intimidation, Survival)",
        "Gladiator (Acrobatics, Performance)",
        "Golgari Agent (Nature, Survival)",
        "Grey Hunter (Pick 2: Athletics/Perception/Survival)",
        "Grinner (Deception, Performance)",
        "Grounded (Athletics, Insight)",
        "Gruul Anarch (Animal Handling, Athletics)",
        "Guild Artisan (Insight, Persuasion)",
        "Guild Merchant (Insight, Persuasion)",
        "Haunted One (Pick 2: Arcane/Investigation/Religion/Survival)",
        "Hermit (Medicine, Religion)",
        "House Agent (Investigation, Persuasion)",
        "Inheritor (Survival, Arcana/History/Religion)",
        "Investigator (Investigation, Insight)",
        "Izzet Engineer (Arcana, Investigation)",
        "Knight (History, Persuasion)",
        "Knight of the Order (Persuasion, Arcana/History/Nature/Religion)",
        "Knight of Solamnia (Athletics, Survival)",
        "Lorehold Student (History, Religion)",
        "Lyceum Scholar (Pick 2: Arcana/History/Persuasion)",
        "Mage of High Sorcery (Arcana, History)",
        "Marine (Athletics, Survival)",
        "Mercenary Veteran (Athletics, Persuasion)",
        "Myriad Operative (Deception, Sleight of Hand/Survival)",
        "Noble (History, Persuasion)",
        "Orzhov Representative (Intimidation, Religion)",
        "Outlander (Athletics, Survival)",
        "Pirate (Athletics, Perception)",
        "Plaintiff (Medicine, Persuasion)",
        "Planar Philosopher (Arcana, the skill associated with faction/your choice)",
        "Prismari Student (Acrobatics, Performance)",
        "Quandrix Student (Arcana, Nature)",
        "Rakdos Cultist (Acrobatics, Performance)",
        "Reformed Cultist (Deception, Religion)",
        "Rewarded (Insight, Persuasion)",
        "Rival Intern (History, Investigation)",
        "Ruined (Stealth, Survival)",
        "Rune Carver (History, Perception)",
        "Sage (Arcana, History)",
        "Sailor (Athletics, Perception)",
        "Selesnya Initiate (Nature, Persuasion)",
        "Shipwright (History, Perception)",
        "Silverquill Student (Intimidation, Persuasion)",
        "Simic Scientist (Arcana, Medicine)",
        "Smuggler (Athletics, Deception)",
        "Soldier (Athletics, Intimidation)",
        "Spy (Deception, Stealth)",
        "Urban Bounty Hunter (Pick 2: Deception/Insight/Persuasion/Stealth)",
        "Urchin (Sleight of Hand, Stealth)",
        "Uthgardt Tribe Member (Athletics, Survival)",
        "Volstrucker Agent (Deception, Stealth)",
        "Waterdhavian Noble (History, Persuasion)",
        "Whitestone Rifle Corps (Pick 2: Athletics/Perception/Survival)",
        "Wildspacer (Athletics, Survival)",
        "Wind-Touched (Acrobatics, Performance)",
        "Witchlight Hand (Performance, Sleight of Hand)",
        "Witherbloom Student (Nature, Survival)"
    ]
    if param == "Y":
        print("0 - random")
        for idx, bkg in enumerate(backgrounds_commented, 1):
            print(f"{idx} - {bkg}")
        print("If all tool proficiencies offered by the background are unknown, choose the random option within the background, it will add it to the list to be changed later.")
        backg = int(input("Background? "))
        if backg == 0:
            player.background = random.choice(Actual_Background)
        elif 1 <= backg <= len(Actual_Background):
            player.background = Actual_Background[backg - 1]
        
    if param == "N":
        player.background = random.choice(Actual_Background)      


##################################################################################
### BACKGROUND INFO ###  
    if (player.background == "Acolyte") or (player.background == "Faction Agent"):
        P1 = "I Idolize a particular hero of my faith, and constantly refer to that person’s deeds and example."
        P2 = "I can find common ground between the fiercest enemies, empathizing with them and always working towards peace."
        P3 = "I see omens in every event and action. The gods try to speak to us, we just need to listen."
        P4 = "Nothing can shake my optimistic attitude."
        P5 = "I quote (or misquote) sacred texts and proverbs in almost every situation."
        P6 = "I am tolerant of other faiths and respect the worship of other gods."
        P7 = "I have enjoyed fine food, drink, and high society among my temple’s elite. Rough living grates on me."
        P8 = "I have spent so long in the temple that I have little practical experience dealing with people in the outside world."
        PTR = [P1,P2, P3, P4, P5, P6, P7, P8]
        player.Trait = random.choice(PTR)
        I1 = "Tradition - The ancient traditions of worship and sacrifice must be upheld."
        I2 = "Charity - I always try to help those in need, no matter what the personal cost."
        I3 = "Change - We must help to bring about the changes the gods are constantly working in the world."
        I4 = "Power - I hope to one day rise to top of my faith’s religious hierarchy."
        I5 = "Faith - I trust that my deity will guide my actions. I have faith that if I work hard, things will go well."
        I6 = "Aspiration - I seek to prove myself worthy of my god’s favor, by matching my actions against his or her teachings."
        IDE = [I1, I2, I3, I4, I5, I6]
        player.Ideal = random.choice(IDE)
        B1 = "I would die to recover an ancient relic of my faith that was lost long ago."
        B2 = "I will someday get revenge on the corrupt temple hierarchy who branded me a heretic."
        B3 = "I owe my life to the priest who took me in when my parents died."
        B4 = "Everything I do is for the common people."
        B5 = "I will do anything to protect the temple where I served."
        B6 = "I seek to preserve a sacred text that my enemies considered heretical and seek to destroy."
        BND = [B1, B2, B3, B4, B5, B6]
        player.Bond = random.choice(BND)
        F1 = "I judge others harshly, and myself even more severely."
        F2 = "I put too much trust in those who wield power with my temple's hierarchy."
        F3 = "My piety sometimes leads me to blindly trust those that profess faith in my god."
        F4 = "I am inflexible in my thinking."
        F5 = "I am suspicious of strangers and expect the worst of them."
        F6 = "Once I pick a goal, I become obsessed with it to the detriment of everything else in my life."
        FLA = [F1, F2, F3, F4, F5, F6]
        player.Flaw = random.choice(FLA)
        player.gold = 15
        if player.background == "Acolyte": 
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.skills_dict["InsiNum"] += 1
            player.skills_dict["ReliNum"] += 1
            player.equipment = ["A Holy Symbol (a gift to you when you entered the priesthood)", "A Prayer Book or Prayer Wheel", "5 sticks of Incense", "Vestments", "A set of Common Clothes"]
        if player.background == "Faction Agent":
            player.skills_dict["InsiNum"] += 1
            FAskills = {
                "Intelligence Skill": ["ArcaNum", "HistNum", "InveNum", "NatuNum", "ReliNum"],
                "Wisdom Skill": ["AnHaNum", "InsiNum", "MediNum", "PercNum", "SurvNum"],
                "Charisma Skill": ["DeceNum", "IntiNum", "PerfNum", "PersNum"]
            } 
            skills_list = list(FAskills.keys())
            if param == "Y":
                print("0 - Random")
                for idx, skl in enumerate(FAskills.keys(), 1):
                    print(f"{idx} - {skl}")
                sklb = int(input("Which skill-type do you choose for a skill boost? "))
                if sklb == 0:
                    category = random.choice(skills_list)
                    skillboost = random.choice(FAskills[category])
                    player.skills_dict[skillboost] += 1
                elif 1 <= sklb <= len(skills_list):
                    sub_skill_list = FAskills[skills_list[sklb - 1]]
                    for idx, subskl in enumerate(sub_skill_list, 1):
                        print(f"{idx} - {subskl}")
                    sub_skl_choice = int(input("Which skill would you like to increase? "))   
                    if sub_skl_choice == 0:
                        skillboost = random.choice(sub_skill_list)
                        player.skills_dict[skillboost] += 1
                    elif 1 <= sub_skl_choice <= len(sub_skill_list):
                        skillboost = sub_skill_list[sub_skl_choice - 1]
                        player.skills_dict[skillboost] += 1                    
            if param == "N":
                category = random.choice(skills_list)
                skillboost = random.choice(FAskills[category])
                player.skills_dict[skillboost] += 1     
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.equipment = ["Badge or emblem of your faction", "A copy of a seminal faction text (or a code-book for a covert faction)", "A set of Common Clothes"]
    if player.background == "Anthropologist":
        AnthPT1 = "I prefer the company of those who aren't like me, including people of other races."
        AnthPT2 = "I'm a stickler when it comes to observing proper etiquette and local customs."
        AnthPT3 = "I would rather observe than meddle."
        AnthPT4 = "By living among violent people, I have become desensitized to violence."
        AnthPT5 = "I would risk life and limb to discover a new culture or unravel the secrets of a dead one."
        AnthPT6 = "When I arrive at a new settlement for the first time, I must learn all its customs."
        AnthPT = [AnthPT1, AnthPT2, AnthPT3, AnthPT4, AnthPT5, AnthPT6]
        player.Trait = random.choice(AnthPT)
        AnthId1 = "Discovery. I want to be the first person to discover a lost culture. (Any)"
        AnthId2 = "Distance. One must not interfere with the affairs of another culture – even one in need of aid. (Lawful)"
        AnthId3 = "Knowledge. By understanding other races and cultures, we learn to understand ourselves. (Any)"
        AnthId4 = "Power. Common people crave strong leadership, and I do my utmost to provide it. (Lawful)"
        AnthId5 = "Protection. I must do everything possible to save a society facing extinction. (Good)"
        AnthId6 = "Indifferent. Life is cruel. What's the point in saving people if they're going to die anyway? (Chaotic)"
        AnthId = [AnthId1, AnthId2, AnthId3, AnthId4, AnthId5, AnthId6]
        player.Ideal = random.choice(AnthId)
        AnthB1 = "My mentor gave me a journal filled with lore and wisdom. Losing it would devastate me."
        AnthB2 = "Having lived among the people of a primeval tribe or clan, I long to return and see how they are faring."
        AnthB3 = "Years ago, tragedy struck the members of an isolated society I befriended, and I will honor them."
        AnthB4 = "I want to learn more about a particular humanoid culture that fascinates me."
        AnthB5 = "I seek to avenge a clan, tribe, kingdom, or empire that was wiped out."
        AnthB6 = "I have a trinket that I believe is the key to finding a long-lost society."
        AnthB = [AnthB1, AnthB2, AnthB3, AnthB4, AnthB5, AnthB6]
        player.Bond = random.choice(AnthB)
        AnthF1 = "Boats make me seasick."
        AnthF2 = "I talk to myself, and I don't make friends easily."
        AnthF3 = "I believe that I'm intellectually superior to people from other cultures and have much to teach them."
        AnthF4 = "I've picked up some unpleasant habits living among races such as goblins, lizardfolk, or orcs."
        AnthF5 = "I complain about everything."
        AnthF6 = "I wear a tribal mask and never take it off."
        AnthF = [AnthF1, AnthF2, AnthF3, AnthF4, AnthF5, AnthF6]
        player.Flaw = random.choice(AnthF)
        player.gold = 10
        player.equipment = ["A leather-bound diary", "A Bottle of Ink", "An Ink pen", "A set of Traveler's Clothes", "One trinket of special significance"]
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.skills_dict["InsiNum"] += 1
        player.skills_dict["ReliNum"] += 1            
    if player.background == "Archaeologist":   
        ArchPT1 = "I love a good puzzle or mystery."
        ArchPT2 = "I'm a pack rat who never throws anything away."
        ArchPT3 = "Fame is more important to me than money."
        ArchPT4 = "I have no qualms about stealing from the dead."
        ArchPT5 = "I'm happier in a dusty old tomb than I am in the centers of civilization."
        ArchPT6 = "Traps don't make me nervous. Idiots who trigger traps make me nervous."
        ArchPT7 = "I might fail, but I will never give up."
        ArchPT8 = "You might think I'm a scholar, but I love a good brawl. These fists were made for punching."
        ArchPT = [ArchPT1,  ArchPT2, ArchPT3, ArchPT4, ArchPT5, ArchPT6, ArchPT7, ArchPT8]
        player.Trait = random.choice(ArchPT)
        ArchId1 = "Preservation. That artifact belongs in a museum. (Good)"
        ArchId2 = "Greed. I won't risk my life for nothing. I expect some kind of payment. (Any)"
        ArchId3 = "Death Wish. Nothing is more exhilarating than a narrow escape from the jaws of death. (Chaotic)"
        ArchId4 = "Dignity. The dead and their belongings deserve to be treated with respect. (Lawful)"
        ArchId5 = "Immortality. All my exploring is part of a plan to find the secret of everlasting life. (Any)"
        ArchId6 = "Danger. With every great discovery comes grave danger. The two walk hand in hand. (Any)"
        ArchId = [ArchId1,  ArchId2, ArchId3, ArchId4, ArchId5, ArchId6]
        player.Ideal = random.choice(ArchId)
        ArchB1 = "Ever since I was a child, I've heard stories about a lost city. I aim to find it, learn its secrets, and earn my place in the history books."
        ArchB2 = "I want to find my mentor, who disappeared on an expedition some time ago."
        ArchB3 = "I have a friendly rival. Only one of us can be the best, and I aim to prove it's me."
        ArchB4 = "I won't sell an art object or other treasure that has historical significance or is one of a kind."
        ArchB5 = "I'm secretly in love with the wealthy patron who sponsors my archaeological exploits."
        ArchB6 = "I hope to bring prestige to a library, a museum, or a university."
        ArchB = [ArchB1,  ArchB2, ArchB3, ArchB4, ArchB5, ArchB6]
        player.Bond = random.choice(ArchB)
        ArchF1 = "I have a secret fear of some common wild animal – and in my work, I see them everywhere."
        ArchF2 = "I can't leave a room without searching it for secret doors."
        ArchF3 = "When I'm not exploring dungeons or ruins, I get jittery and impatient."
        ArchF4 = "I have no time for friends or family. I spend every waking moment thinking about and preparing for my next expedition."
        ArchF5 = "When given the choice of going left or right, I always go left."
        ArchF6 = "I can't sleep except in total darkness."
        ArchF = [ArchF1,  ArchF2, ArchF3, ArchF4, ArchF5, ArchF6]
        player.Flaw = random.choice(ArchF)
        player.gold = 25
        player.equipment = ["A wooden case containing a map to a ruin or dungeon", "A Bullseye Lantern", "A Miner's Pick", "A set of Traveler's Clothes", "A Shovel", "A Two-Person Tent"]
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        ArchProf = [dnd_tools.artisan_tools["CartTools"]["Name"], dnd_tools.kits["NavTools"]["Name"]]      
        if param == "Y":
            print("0 - Random")
            for idx, archtl in enumerate(ArchProf, 1):
                print(f"{idx} - {archtl}")
            toolprof = int(input("What tool would you like to be proficient in? "))
            if toolprof == 0:
                player.proficiencies.append(random.choice(ArchProf))
            elif 1 <= toolprof <= len(ArchProf):
                player.proficiencies.append(ArchProf[tools - 1])
        if param == "N":
            player.proficiencies.append(random.choice(ArchProf))
    if player.background == "Ashari":
        AshPT1 = "I like to keep my hands busy, no matter where I am."
        AshPT2 = "I love to explore new places and meet new people."
        AshPT3 = "I meditate at dawn each day—and I can't stand it when my routine is interrupted."
        AshPT4 = "I like noticing patterns in the world around me, whether or not they mean anything."
        AshPT5 = "I don't let anything—or anyone—stand in the way of my mission."
        AshPT6 = "I'm a plain talker, even with people who outrank me."
        AshPT7 = "I've always got some of my native element with me in some form. (This might be modeling clay, pure water, special burning incense, or a bottled cloud.)"
        AshPT8 = "I talk with everyone like I've known them all my life. Because most people I know, I have known all my life!"
        AshPT = [AshPT1,  AshPT2, AshPT3, AshPT4, AshPT5, AshPT6, AshPT7, AshPT8]
        player.Trait = random.choice(AshPT)
        AshId1 = "Destiny. I believe that everyone has a role to play. Now I just have to find mine. (Neutral)"
        AshId2 = "Community. It's important to surround yourself with people you can count on, and who will support you. (Good)"
        AshId3 = "Knowledge. I want to learn everything I can about the Elemental Planes—and maybe even visit them myself. (Neutral)"
        AshId4 = "Freedom. I don't care what anyone says. Even if it causes problems, the elements must be free. And so should I. (Chaotic)"
        AshId5 = "Structure. The elements are in harmony when they are free to act as they will, within the safe boundaries set by the Ashari. People are much the same. (Lawful)"
        AshId6 = "Virtuous Cycle. If I see someone who needs help, I feel compelled to assist them. Surely they'll return the favor someday! (Good)"
        AshId = [AshId1,  AshId2, AshId3, AshId4, AshId5, AshId6]
        player.Ideal = random.choice(AshId)
        AshB1 = "I have a cousin in another Ashari tribe whom I've never met, but someday I want to visit my extended family."
        AshB2 = "The leader of my tribe thinks I could be their successor, but I worry that I don't have enough experience to lead my people."
        AshB3 = "A mysterious person killed a member of my family. I've left home to discover who the killer was—and to seek vengeance."
        AshB4 = "My older sibling set out on their Aramante a year ago, and I haven't seen them since."
        AshB5 = "When I was a baby, a giant eagle brought me to Zephrah. I love my family, but I often wonder who my birth parents are."
        AshB6 = "I trust my animal friends more than any humanoid ally."
        AshB = [AshB1,  AshB2, AshB3, AshB4, AshB5, AshB6]
        player.Bond = random.choice(AshB)
        AshF1 = "Big cities are overwhelming. I get nervous when surrounded by people I don't know."
        AshF2 = "I know all too well that elemental power is dangerous—but I like playing around with it anyway."
        AshF3 = "I get surly if I go too long without being in contact with my native element."
        AshF4 = "I think the mission of my people is a fool's errand. They should abandon isolation, let the elements be, and enjoy the pleasures of the world!"
        AshF5 = "I can't stand it when people say one thing and mean another! Just say what you mean!"
        AshF6 = "Ugh, I know it's not right, but I can't help but look down on people who can't manipulate the elements. It's not like it's hard!"
        AshF = [AshF1,  AshF2, AshF3, AshF4, AshF5, AshF6]
        player.Flaw = random.choice(AshF)
        player.gold = 10
        player.equipment = ["A set of traveler's clothes", "A staff carved with symbols of your tribe", "An herbalism kit"]
        langs = ["Prim"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)
        player.skills_dict["NatuNum"] += 1
        AshSkl = {
            "Arcana" : "ArcaNum",
            "Survival" : "SurvNum"
        }
        skills_list = list(AshSkl.keys())
        if param == "Y":
            print("0 - Random")
            for idx, skill in enumerate(skills_list, 1):
                print(f"{idx} - {skill}")
            skl = int(input("Which skill would you prefer? "))
            if skl == 0:
                player.skills_dict[AshSkl[random.choice(skills_list)]] += 1
            elif 1 <= skl <= len(skills_list):
                player.skills_dict[AshSkl[skills_list[skl - 1]]] += 1
        if param == "N":
            player.skills_dict[AshSkl[random.choice(skills_list)]] += 1
        player.proficiencies.append(dnd_tools.kits["HerbKit"]["Name"])    
    if player.background == "Astral Drifter":
        player.gold = 10
        player.equipment = ["A set of traveler's clothes", "A diary", "An ink pen", "A bottle of ink"]
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.skills_dict["InsiNum"] += 1
        player.skills_dict["ReliNum"] += 1    
        player.Trait = ""
        player.Ideal = ""
        player.Bond = ""
        player.Flaw = ""        
    if player.background == "Athlete":
        AthPT1 = "I feel most at peace during physical exertion, be it exercise or battle."
        AthPT2 = "I don't like to sit idle."
        AthPT3 = "I have a daily exercise routine that I refuse to break."
        AthPT4 = "Obstacles exist to be overcome."
        AthPT5 = "When I see others struggling, I offer to help."
        AthPT6 = "I love to trade banter and gibes."
        AthPT7 = "Anything worth doing is worth doing best."
        AthPT8 = "I get irritated if people praise someone else and not me."
        AthPT = [AthPT1, AthPT2, AthPT3, AthPT4, AthPT5, AthPT6, AthPT7, AthPT8]
        player.Trait = random.choice(AthPT)
        AthId1 = "Competition. I strive to test myself in all things. (Chaotic)"
        AthId2 = "Triumph. The best part of winning is seeing my rivals brought low. ( Evil)"
        AthId3 = "Camaraderie. The strongest bonds are forged through struggle. (Good)"
        AthId4 = "People. I strive to inspire my spectators. (Neutral)"
        AthId5 = "Tradition. Every game has rules, and the playing field must be level. (Lawful)"
        AthId6 = "Growth. Lessons hide in victory and defeat. (Any)"
        AthId = [AthId1, AthId2, AthId3, AthId4, AthId5, AthId6]
        player.Ideal = random.choice(AthId)
        AthBo1 = "My teammates are my family."
        AthBo2 = "I will overcome a rival and prove myself their better."
        AthBo3 = "My mistake got someone hurt. I'll never make that mistake again."
        AthBo4 = "I will be the best for the honor and glory of my home."
        AthBo5 = "The person who trained me is the most important person in my world."
        AthBo6 = "I strive to live up to a specific hero's example."
        AthBo = [AthBo1, AthBo2, AthBo3, AthBo4, AthBo5, AthBo6]
        player.Bond = random.choice(AthBo)
        AthF1 = "I indulge in a habit that threatens my reputation or my health."
        AthF2 = "I'll do absolutely anything to win."
        AthF3 = "I ignore anyone who doesn't compete and anyone who loses to me."
        AthF4 = "I have lingering pain from old injuries."
        AthF5 = "Any defeat or failure on my part is because my opponent cheated."
        AthF6 = "I must be the captain of any group I join."
        AthF = [AthF1, AthF2, AthF3, AthF4, AthF5, AthF6]
        player.Flaw = random.choice(AthF)
        player.gold = 10
        player.equipment = ["A bronze discus or leather ball", "A lucky charm or past trophy", "A set of Traveler's Clothes"]
        player.languages, player.slang = languagegen(param, player.languages, player.slang)        
        player.skills_dict["AcroNum"] += 1
        player.skills_dict["AthlNum"] += 1
        player.proficiencies.append(dnd_tools.vehicles["VehLand"])
    if player.background == "Azorius Functionary":
        AzFuPT1 = "I try never to let my judgment become clouded by emotion."
        AzFuPT2 = "I have infinite patience with the dolts and boors I'm forced to deal with every day."
        AzFuPT3 = "When I give an order, I expect it to be obeyed."
        AzFuPT4 = "I just want things the way I like them: neat, orderly, and clean."
        AzFuPT5 = "No wrongdoing can escape my watchful gaze."
        AzFuPT6 = "I always say exactly what I mean, no matter how many words it takes to communicate the particular nuance I am attempting to convey."
        AzFuPT7 = "I'm very literal and don't appreciate metaphor or sarcasm."
        AzFuPT8 = "I never change my mind once it's made up."
        AzFuPT = [AzFuPT1, AzFuPT2, AzFuPT3, AzFuPT4, AzFuPT5, AzFuPT6, AzFuPT7, AzFuPT8]
        player.Trait = random.choice(AzFuPT)
        AzFuI1 = "Guild: My guild is all that really matters. (Any)"
        AzFuI2 = "Order: The law is meant to ensure that the gears of society turn smoothly and quietly. (Lawful)"
        AzFuI3 = "Peace: The ultimate object of the law is to remove violence from society. (Good)"
        AzFuI4 = "Compliance: Coercion is a fine way of ensuring that the laws are obeyed. (Lawful)"
        AzFuI5 = "Legislation: The law embodies excellence in its precision and detail. (Lawful)"
        AzFuI6 = "Punishment: A public display of consequences is an excellent deterrent for other criminals. (Evil)"
        AzFuI = [AzFuI1, AzFuI2, AzFuI3, AzFuI4, AzFuI5, AzFuI6]
        player.Ideal = random.choice(AzFuI)
        AzFuB1 = "I am beholden to an Azorius arrester who captured the criminal who killed my parents, saving me from the same fate."
        AzFuB2 = "I hope one day to write the laws, not just enforce them."
        AzFuB3 = "I tried and failed to prevent a murder, and I have sworn to find and arrest the perpetrator."
        AzFuB4 = "I successfully preveted a murder, and the would-be perpetrator wants me dead."
        AzFuB5 = "One of my parents was prominent in the guild, and I resent constantly being compared to that standard."
        AzFuB6 = "I've modeled my career after a highly respected law-mage or arrester, but I fear that my role model might be involved in something illegal."
        AzFuB = [AzFuB1, AzFuB2, AzFuB3, AzFuB4, AzFuB5, AzFuB6]
        player.Bond = random.choice(AzFuB)
        AzFuF1 = "I'm unable to distinguish between the letter and the spirit of the law."
        AzFuF2 = "I seem like a harsh judge to others, but I judge myself most harshly of all."
        AzFuF3 = "I have a secret, illegal vice."
        AzFuF4 = "I was traumatized by witnessing a crime as a child."
        AzFuF5 = "I'm incapable of deception."
        AzFuF6 = "I wish I had joined the Boros, but I fear they'd never accept me."
        AzFuF = [AzFuF1, AzFuF2, AzFuF3, AzFuF4, AzFuF5, AzFuF6]
        player.Flaw = random.choice(AzFuF)
        player.gold = 10
        player.equipment = ["An Azorius insignia", "A scroll containing the text of a law important to you", "A Bottle of Blue Ink", "A Pen", "A set of Fine Clothes"]
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)       
        player.skills_dict["InsiNum"] += 1
        player.skills_dict["IntiNum"] += 1          
    if player.background == "Bandit Defector": 
        BanPT1 = "I am plucky and confident in my abilities, at least, that’s what I want others to think."
        BanPT2 = "I often crack jokes to lighten the mood."
        BanPT3 = "I like to keep my secrets, and those who try to pry into my life irritate me."
        BanPT4 = "I have trouble sleeping unless I’m on the ground (or floor) in my bedroll."
        BanPT5 = "I picked up many stories during my time on the road, and I have one for every occasion."
        BanPT6 = "You mess with my friends, you mess with me."
        BanPT7 = "I never really had a plan in life, I tend to just go with the flow."
        BanPT8 = "I’m as cautious as they come."
        BanPT = [BanPT1,  BanPT2, BanPT3, BanPT4, BanPT5, BanPT6, BanPT7, BanPT8]
        player.Trait = random.choice(BanPT)
        BanId1 = "Repentance. I’ve done terrible things in the past, and I want to try and make up for them. (Good)"
        BanId2 = "Nature. I’ve seen what’s happening to the forest, and it’s bigger than all of us. We’re all doomed unless we do something about it. (Neutral)"
        BanId3 = "Friendship. My friends are like family to me, and I’ll keep trying to do right by them until the end. (Good)"
        BanId4 = "Self-Preservation. Any good rat knows when it’s time to flee a sinking ship. I want to be clear of the Bandit Coalition when it goes down. (Evil)"
        BanId5 = "Compassion. The struggle between humblefolk and birdfolk will only lead to more bloodshed. It needs to stop somewhere. (Good)"
        BanId6 = "Freedom. I just want to be free to live my own life, and make my own way in the world. (Chaotic)"
        BanId = [BanId1,  BanId2, BanId3, BanId4, BanId5, BanId6]
        player.Ideal = random.choice(BanId)
        BanB1 = "I did some hard time in Alderheart’s prison, and the perch guard who arrested me still has it out for me."
        BanB2 = "I stole something valuable from the Captain of my unit. I’m in big trouble if they ever find me."
        BanB3 = "I harbor a terrible secret that might change how people think of me if it got out."
        BanB4 = "I still sympathize with the Coalition’s aims, I just believe there’s a better way."
        BanB5 = "My friends in the Coalition didn’t understand why I had to leave. They’ve branded me a traitor."
        BanB6 = "I had people in the Coalition who looked up to me as a leader. They might still follow me, if I could only reach them."
        BanB = [BanB1,  BanB2, BanB3, BanB4, BanB5, BanB6]
        player.Bond = random.choice(BanB)
        BanF1 = "I’m always ready to bail when something goes wrong."
        BanF2 = "Whenever I see something valuable, I can’t help but think of a way to steal it."
        BanF3 = "It’s hard for me to trust people. I’ve been burned before."
        BanF4 = "I have a problem with authority. Nobody tells me what to do."
        BanF5 = "There’s a warrant out for my arrest."
        BanF6 = "I have a bad habit that I picked up on the road."
        BanF = [BanF1,  BanF2, BanF3, BanF4, BanF5, BanF6]
        player.Flaw = random.choice(BanF)
        player.gold = 10
        player.equipment = ["A knife, a cooking pot", "A winter blanket", "An object you received as your cut from a successful robbery", "A set of common clothes"]
        player.proficiencies = gamingsetsmusicalinstr(param, player.proficiencies)
        player.skills_dict["DeceNum"] += 1
        player.skills_dict["SurvNum"] += 1
        player.proficiencies.append(dnd_tools.kits["DisgKit"]["Name"])      
    if player.background == "Boros Legionnaire":
        BoLgPT1 = "I approach every task with the same high degree of military precision."
        BoLgPT2 = "I am always the first into the fray."
        BoLgPT3 = "I bear any injury or indignity with stoic discipline."
        BoLgPT4 = "My righteous wrath is easily inflamed by the slightest iniquity."
        BoLgPT5 = "My honor is more important to me than my life."
        BoLgPT6 = "Dangerous work is best accomplished by an orderly group working with common purpose."
        BoLgPT7 = "I treat my weapons, uniform, and insignia with reverence, for they are gifts of the angels."
        BoLgPT8 = "I pace when standing and fidget incessantly when forced to sit."
        BoLgPT = [BoLgPT1, BoLgPT2, BoLgPT3, BoLgPT4, BoLgPT5, BoLgPT6, BoLgPT7, BoLgPT8]
        player.Trait = random.choice(BoLgPT)
        BoLgI1 = "Guild: My guild is all that really matters. (Any)"
        BoLgI2 = "Justice: Achieving justice requires establishing fair, equitable, and compassionate relationships within a community. (Good)"
        BoLgI3 = "Protection: It isn't right for innocents to suffer because of the arrogance of the powerful. (Good)"
        BoLgI4 = "Solidarity: It is most crucial to act with a single will, marching side by side in perfect accord. (Lawful)"
        BoLgI5 = "Order: Society functions only if people do their duty and respect the chain of command. (Lawful)"
        BoLgI6 = "Conviction: Anything worth doing is worth doing with your whole heart. (Lawful)"
        BoLgI = [BoLgI1, BoLgI2, BoLgI3, BoLgI4, BoLgI5, BoLgI6]
        player.Ideal = random.choice(BoLgI)
        BoLgB1 = "I would lay down my life for Aurelia and the angels."
        BoLgB2 = "I owe my life to the Boros captain who took me in when I was living on the streets."
        BoLgB3 = "My fellow legionnaires are my family."
        BoLgB4 = "I wield the same Boros weapon my grandparent did, for the honor of our family."
        BoLgB5 = "I ran with the Rakdos in my youth, and I'm striving to atone for my past misdeeds."
        BoLgB6 = "I do what I can to help out the spouse of a comrade who died in battle."
        BoLgB = [BoLgB1, BoLgB2, BoLgB3, BoLgB4, BoLgB5, BoLgB6]
        player.Bond = random.choice(BoLgB)
        BoLgF1 = "I act bravely when I'm in a group, but I'm a coward when I'm alone."
        BoLgF2 = "I see everything in clear-cut black and white."
        BoLgF3 = "I'm just a little fascinated by the ways of the Gruul."
        BoLgF4 = "I trust the chain of command more than anythingmore even than my closest friends."
        BoLgF5 = "I'm slow to trust members of other guilds."
        BoLgF6 = "I've been known to turn a blind eye to injustice, with the help of a modest bribe."
        BoLgF = [BoLgF1, BoLgF2, BoLgF3, BoLgF4, BoLgF5, BoLgF6]
        player.Flaw = random.choice(BoLgF)
        player.gold = 10
        player.equipment = ["A Boros insignia", "A feather from an angel's wing", "A tattered piece of a Boros banner (a souvenir from a famous battle)", "A set of Common Clothes"]
        langlist = ["Cele", "Drac", "Gobl", "Mino"]
        player.languages, player.slang = choicefourlang(param, player.languages, player.slang, langlist)
        player.skills_dict["AthlNum"] += 1
        player.skills_dict["IntiNum"] += 1
        BlProf = [dnd_tools.artisan_tools["CartTools"]["Name"], dnd_tools.kits["NavTools"]["Name"]]
        if param == "Y":
            print("0 - Random")
            for idx, bltl in enumerate(BlProf, 1):
                print(f"{idx} - {bltl}")
            toolprof = int(input("What tool would you like to be proficient in? "))
            if toolprof == 0:
                player.proficiencies.append(random.choice(BlProf))
            elif 1 <= toolprof <= len(BlProf):
                player.proficiencies.append(BlProf[toolprof - 1])
        if param == "N":
            player.proficiencies.append(random.choice(BlProf)) 
    if player.background == "Celebrity Adventurer’s Scion":
        CelAdvSPT1 = "I will never get out of my famous parent's shadow, and no one else will ever understand this burden."
        CelAdvSPT2 = "I've seen enough of the adventuring life to have realistic expectations and empathy for my peers."
        CelAdvSPT3 = "Living up to my legacy will be difficult, but I'm going to do it."
        CelAdvSPT4 = "I'm used to the very best in life, and that's a hard habit to break."
        CelAdvSPT5 = "My parent taught me a sense of duty. I strive to uphold it, even when the odds are against me."
        CelAdvSPT6 = "No one can fake a smile, a handshake, or an interested nod like I can."
        CelAdvSPT7 = "I've been part of the adventuring life since I was old enough to walk. Let me explain a few things to you."
        CelAdvSPT8 = "No risk is too great for the rewards of defeating my enemies… and taking their stuff."
        CelAdvSPT = [CelAdvSPT1, CelAdvSPT2, CelAdvSPT3, CelAdvSPT4, CelAdvSPT5, CelAdvSPT6, CelAdvSPT7, CelAdvSPT8]
        player.Trait = random.choice(CelAdvSPT)
        CelAdvSId1 = "Power. The only way to get ahead in this world is to attain power and hold onto it with all your might. (Evil)"
        CelAdvSId2 = "Peace. Those who can find or make peace in the chaotic world around them have everything. (Lawful)"
        CelAdvSId3 = "Fame. I've seen what fame can bring. And I'll do anything to get all that for myself. (Neutral)"
        CelAdvSId4 = "Training. Hard work, sacrifice, and training lead to success—and eventually to perfection. (Any)"
        CelAdvSId5 = "Anonymity. I want to be successful. And alone. With lots of guards and wards between me and everyone else in the world. (Any)"
        CelAdvSId6 = "Wisdom. Material wealth is an illusion. Wisdom is the real treasure. (Good)"
        CelAdvSId = [CelAdvSId1, CelAdvSId2, CelAdvSId3, CelAdvSId4, CelAdvSId5, CelAdvSId6]
        player.Ideal = random.choice(CelAdvSId) 
        CelAdvSB1 = "While my parent was out adventuring, a servant raised me, and I care about that person more than anyone."
        CelAdvSB2 = "I consider every member of my parent's former adventuring party to be family."
        CelAdvSB3 = "Despite their absences, my famous parent was kind and generous. I love them and want to make them proud."
        CelAdvSB4 = "My parent once brought a cursed magic item home. It is my obsession."
        CelAdvSB5 = "My childhood home holds all my best memories, and its upkeep is my primary concern."
        CelAdvSB6 = "Growing up, I had an imaginary friend I could always count on. That friend is still with me."
        CelAdvSB = [CelAdvSB1, CelAdvSB2, CelAdvSB3, CelAdvSB4, CelAdvSB5, CelAdvSB6]
        player.Bond = random.choice(CelAdvSB) 
        CelAdvSF1 = "You don't know what I'm going through. You never can."
        CelAdvSF2 = "You. Fetch my cloak. And maybe rub my feet for a while."
        CelAdvSF3 = "My comrades are brave, but I must defeat this threat alone to prove my worth."
        CelAdvSF4 = "Oh, yeah, that spell? Named after my parent's best friend. Let me tell you about them."
        CelAdvSF5 = "My best days are behind me. Ahead lies only toil, pain, and death."
        CelAdvSF6 = "You have to look out for yourself. No one else will."
        CelAdvSF = [CelAdvSF1, CelAdvSF2, CelAdvSF3, CelAdvSF4, CelAdvSF5, CelAdvSF6]
        player.Flaw = random.choice(CelAdvSF)
        player.gold = 30
        player.equipment = ["Disguise kit", "A set of Fine Clothes"]
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.skills_dict["PercNum"] += 1
        player.skills_dict["PerfNum"] += 1
        player.proficiencies.append(dnd_tools.kits["DisgKit"]["Name"])
    if player.background == "Charlatan":
        P1 = "I fall in and out of love easily, and am always pursuing someone."
        P2 = "I have a joke for every occasion, especially occasions where humor is inappropriate."
        P3 = "Flattery is my preferred trick for getting what I want."
        P4 = "I am a born gambler who cannot resist taking a risk for potential payout."
        P5 = "I lie about almost everything, even when there is no good reason to."
        P6 = "Sarcasm and insults are my weapons of choice."
        P7 = "I keep multiple holy symbols on me and invoke whatever deity might come in useful at any given time."
        P8 = "I pocket anything I see that might have some value."
        PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
        player.Trait = random.choice(PTR)
        I1 = "Independence - I am a free spirit, no one tells me what to do."
        I2 = "Fairness - I never target people who can not afford to lose a few coins."
        I3 = "Charity - I distribute the money I acquire to the people who really need it."
        I4 = "Creativity - I never run the same con twice."
        I5 = "Friendship - Material goods come and go. Bonds of friendship last forever."
        I6 = "Aspiration - I am determined to make something of myself."
        IDE = [I1, I2, I3, I4, I5, I6]
        player.Ideal = random.choice(IDE)
        B1 = "I fleeced the wrong person and must work to ensure that this individual never crosses paths with me or those I care about."
        B2 = "I owe everything to my mentor, a horrible person who is probably rotting in jail somewhere."
        B3 = "Somewhere out there, I have a child who does not know me. I am making the world better for him or her."
        B4 = "I come from a noble family and one day I will reclaim my lands and title from those who stole them from me."
        B5 = "A powerful person killed someone I loved. Someday soon, I will have my revenge."
        B6 = "I swindled and ruined a person who did not deserve it. I seek to atone for my misdeeds but might never be able to forgive myself. "
        BND = [B1, B2, B3, B4, B5, B6]
        player.Bond = random.choice(BND)
        F1 = "I cannot resist a pretty face."
        F2 = "I am always in debt. I spend my ill-gotten gains on decadent luxuries faster than I bring them in."
        F3 = "I am convinced that no one could ever fool me the way I fool others."
        F4 = "I am too greedy for my own good. I cannot resist taking a risk if there’s money involved."
        F5 = "I cannot resist swindling people who are more powerful than me."
        F6 = "I hate to admit and will hate myself for it, but I will run and hide to preserve my own hide if the going gets tough."
        FLA = [F1, F2, F3, F4, F5, F6]
        player.Flaw = random.choice(FLA)
        player.gold = 15
        player.equipment = ["A set of Fine Clothes", "A Disguise kit", "Tools of the con of your choice (ten stoppered bottles filled with colored liquid, a set of Weighted Dice, a deck of Marked Cards, or a Signet Ring of an imaginary duke)"]
        player.skills_dict["DeceNum"] += 1
        player.skills_dict["SloHNum"] += 1
        player.proficiencies.append(dnd_tools.kits["DisgKit"]["Name"])
        player.proficiencies.append(dnd_tools.kits["ForgKit"]["Name"])
    if (player.background == "Clasp Member") or (player.background == "Myriad Operative"): 
        ClaMPT1 = "I only show my emotions around people I really trust."
        ClaMPT2 = "I don't need friends; I need allies. When I do make 'friends,' I only consider what they can do for me."
        ClaMPT3 = "I look for simple solutions. The world's full of tough problems, but a well-placed knife is a one-size-fits-all answer."
        ClaMPT4 = "Money talks. I don't. We've got an efficient relationship."
        ClaMPT5 = "I used to have one rule—don't get involved in other people's problems. Why are things so complicated now?"
        ClaMPT6 = "Crime is a game, and I play to win. I have no sympathy for players who don't get that."
        ClaMPT7 = "This organization has a lot of folks who cling to ugly, brutal practices. I'm not like that. I'm a professional, and professionals have standards."
        ClaMPT = [ClaMPT1,  ClaMPT2, ClaMPT3, ClaMPT4, ClaMPT5, ClaMPT6, ClaMPT7]
        player.Trait = random.choice(ClaMPT)
        ClaMId1 = "By Any Means. I complete jobs. Collateral damage isn't my problem. (Chaotic)"
        ClaMId2 = "Ambition. I will climb to the top of the ladder. Everything I do is a stepping-stone to a Spireling's position. (Neutral)"
        ClaMId3 = "Decisiveness. It's important to make up your mind so you can act swiftly and without delay. (Neutral)"
        ClaMId4 = "Honor. There's room in the Clasp for both good and evil. Every day, I awake and choose to do what's right. (Good)"
        ClaMId5 = "Family. The Clasp is family. Anything that's good for the family is good for me. (Lawful)"
        ClaMId6 = "Self-Interest. There are too many bleeding hearts in the Clasp these days. Doing the right thing means doing the thing that makes my life better. (Evil)"
        ClaMId = [ClaMId1,  ClaMId2, ClaMId3, ClaMId4, ClaMId5, ClaMId6]
        player.Ideal = random.choice(ClaMId)
        ClaMB1 = "I'd do anything—anything—to protect my comrades."
        ClaMB2 = "I'll always be grateful to the Spireling who took me in when I was an orphaned kid."
        ClaMB3 = "I was inspired to join the Clasp by the stories my parents told of being saved from the Chroma Conclave's attack on Emon. I can look past the organization's flaws."
        ClaMB4 = "I was nearly killed by the Myriad. If the Clasp is the enemy of those villains, then the Clasp is my friend."
        ClaMB5 = "I've got family back in the old town who are counting on me for money. They don't know how I get it, but they don't need to know."
        ClaMB6 = "I joined the Clasp to become rich, powerful, and beloved. That's all there is to it."
        ClaMB = [ClaMB1,  ClaMB2, ClaMB3, ClaMB4, ClaMB5, ClaMB6]
        player.Bond = random.choice(ClaMB)
        ClaMF1 = "I'm hopeless at organizing my belongings, and I'm always losing things."
        ClaMF2 = "I get bored whenever a plan is going too smoothly. A win is always more fun when it's by the skin of my teeth!"
        ClaMF3 = "I've seen Spirelings walk out among cheering crowds of thousands. Gods, I wish that were me. I need that to be me."
        ClaMF4 = "I'm rubbish with money, and never seem to leave town with a full purse. Keeps me coming back to the life, I suppose."
        ClaMF5 = "I can't work with shoddy, makeshift thieves' tools. I need everything involving my work to be perfect."
        ClaMF6 = "Any slight against me, no matter how small, is cause for revenge."
        ClaMF = [ClaMF1,  ClaMF2, ClaMF3, ClaMF4, ClaMF5, ClaMF6]
        player.Flaw = random.choice(ClaMF)
        player.skills_dict["DeceNum"] += 1
        ClMeTl = [dnd_tools.kits["DisgKit"]["Name"], dnd_tools.kits["ForgKit"]["Name"], dnd_tools.kits["ThievKit"]["Name"]]
        ClMe_skills = {
                "Sleight of Hand" : "SloHNum",
                "Stealth" : "SteaNum"
            }
        skills_list = list(ClMe_skills.keys())
        if param == "Y":    
            print("0 - Random")
            for idx, clmeskls in enumerate(skills_list, 1):
                print(f"{idx} - {clmeskls}")
            clmeskl = int(input("Choose a skill to increase. "))
            if clmeskl == 0:
                random_skill_display = random.choice(skills_list)
                random_skill_key = ClMe_skills[random_skill_display]
                player.skills_dict[random_skill_key] += 1
            elif 1 <= clmeskl <= len(skills_list):
                skill_display = skills_list[clmeskl - 1]
                skill_key = ClMe_skills[skill_display]
                player.skills_dict[skill_key] += 1
            for idx, clmekit in enumerate(ClMeTl, 1):
                print(f"{idx} - {clmekit}")
            clmetl = int(input("Choose a tool to be proficient in. "))
            if clmetl == 0:
                player.proficiencies.append(random.choice(ClMeTl))
            elif 1 <= clmetl <= len(ClMeTl):
                player.proficiencies.append(ClMeTl[clmetl - 1])
        if param == "N":
            random_skill_display = random.choice(skills_list)
            random_skill_key = ClMe_skills[random_skill_display]
            player.skills_dict[random_skill_key] += 1
            player.proficiencies.append(random.choice(ClMeTl))
        if dnd_tools.TCant in player.languages:
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
        else:
            player.languages.append(dnd_tools.TCant)
        player.gold = 10
        player.equipment = ["A set of inconspicuous common clothes"]
        tools = [
            dnd_tools.artisan_tools["AlchSupp"],
            dnd_tools.artisan_tools["BrewSupp"],
            dnd_tools.artisan_tools["CallSupp"],
            dnd_tools.artisan_tools["CarpTools"],
            dnd_tools.artisan_tools["CartTools"],
            dnd_tools.artisan_tools["CobbTools"],
            dnd_tools.artisan_tools["CooksUten"],
            dnd_tools.artisan_tools["GlasTools"],
            dnd_tools.artisan_tools["JeweTools"],
            dnd_tools.artisan_tools["LthrwrkTools"],
            dnd_tools.artisan_tools["MasnTools"],
            dnd_tools.artisan_tools["PaintSupp"],
            dnd_tools.artisan_tools["PottTools"],
            dnd_tools.artisan_tools["SmthTools"],
            dnd_tools.artisan_tools["TinkTools"],
            dnd_tools.artisan_tools["WeavTools"],
            dnd_tools.artisan_tools["WdcrvTools"]
        ]
        for tool in tools:
            if tool["Name"] in player.proficiencies:
                player.equipment.append(tool)         
    if (player.background == "Criminal") or (player.background == "Spy") or (player.background == "Urban Bounty Hunter"):     
        P1 = "I always have a plan for what to do when things go wrong."
        P2 = "I am always calm, no matter what the situation. I never raise my voice or let my emotions control me."
        P3 = "The first thing I do in a new place is note the locations of everything valuable, or where such things could be hidden."
        P4 = "I would rather make a new friend than a new enemy."
        P5 = "I am incredibly slow to trust. Those who seem the fairest often have the most to hide."
        P6 = "I do not pay attention to the risks in a situation. Never tell me the odds."
        P7 = "The best way to get me to do something is to tell me I cannot do it."
        P8 = "I blow up at the slightest insult."
        PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
        player.Trait = random.choice(PTR)
        I1 = "Honor - I do not steal from others in the trade."
        I2 = "Freedom - Chains are meant to be broken, as are those who would forge them."
        I3 = "Charity - I steal from the wealthy so that I can help people in need."
        I4 = "Greed -  I will do whatever it takes to become wealthy."
        I5 = "People - I am loyal to my friends, not to any ideals, and everyone else can take a trip down the Styx for all I care. "
        I6 = "Redemption - There is a spark of good in everyone. "
        IDE = [I1, I2, I3, I4, I5, I6]
        player.Ideal = random.choice(IDE)
        B1 = "I am trying to pay off an old debt I owe to a generous benefactor."
        B2 = "My ill-gotten gains go to support my family."
        B3 = "Something important was taken from me, and I aim to steal it back."
        B4 = "I will become the greatest thief that ever lived."
        B5 = "I am guilty of a terrible crime. I hope I can redeem myself for it."
        B6 = "Someone I loved died because of a mistake I made. That will never happen again."
        BND = [B1, B2, B3, B4, B5, B6]
        player.Bond = random.choice(BND)
        F1 = "When I see something valuable, I can not think about anything but how to steal it."
        F2 = "When faced with a choice between money and my friends, I usually choose the money."
        F3 = "If there is a plan, I will forget it. If I do not forget it, I will ignore it."
        F4 = "I have a 'tell' that reveals when I am lying."
        F5 = "I turn tail and run when things look bad."
        F6 = "An innocent person is in prison for a crime that I committed. I am okay with that."
        FLA = [F1, F2, F3, F4, F5, F6]
        player.Flaw = random.choice(FLA)
        if ((player.background == "Criminal") or (player.background == "Spy")):
            player.gold = 15
            player.equipment = ["A Crowbar", "A set of dark common clothes including a hood"]
            player.skills_dict["DeceNum"] += 1
            player.skills_dict["SteaNum"] += 1
            player.proficiencies = gamingsets(param, player.proficiencies)
        if player.background == "Urban Bounty Hunter":
            player.gold = 20
            player.equipment = ["A set of clothes appropriate to your duties"]
            player.skills_dict["DeceNum"], player.skills_dict["InsiNum"], player.skills_dict["PersNum"], player.skills_dict["SteaNum"] = choicefourskill2(param, player.skills_dict, "DeceNum", "InsiNum", "PersNum", "SteaNum", dnd_tools.skills["Deception"], dnd_tools.skills["Insight"], dnd_tools.skills["Persuasion"], dnd_tools.skills["Stealth"])
            player.proficiencies = gamingsetmusicalinstrthieves(param, player.proficiencies)
    if player.background == "Dimir Operative":
        DOPT1 = "I'm good at hiding my true thoughts and feelings."
        DOPT2 = "When I'm in doubt about revealing something, I assume it's a secret, and I don't share it."
        DOPT3 = "I like to sound mysterious, because wisdom hidden grows deeper with time."
        DOPT4 = "I have no patience with people who get in my way."
        DOPT5 = "I love hearing about other people's nightmares."
        DOPT6 = "Combat is meant to be quick, clean, and one-sided."
        DOPT7 = "I like to stick to the shadows."
        DOPT8 = "I never show my anger. I just plot my revenge."
        DOPT = [DOPT1, DOPT2, DOPT3, DOPT4, DOPT5, DOPT6, DOPT7, DOPT8]
        player.Trait = random.choice(DOPT)
        DimOpI1 = "Guild: My true guild is all that really matters. (Any)"
        DimOpI2 = "Control: I like pulling the strings. (Lawful)"
        DimOpI3 = "Secrets: I collect secrets and never reveal them. (Any)"
        DimOpI4 = "Knowledge: I want to know as much as I can about this city and how it works. (Any)"
        DimOpI5 = "Independence: I value the freedom to pursue my own goals without interference. (Chaotic)"
        DimOpI6 = "Nihilism: I don't believe in anything, and anyone who does is a fool. (Neutral)"
        DimOpI = [DimOpI1, DimOpI2, DimOpI3, DimOpI4, DimOpI5, DimOpI6]
        player.Ideal = random.choice(DimOpI)
        DimOpB1 = "I discovered a secret I can't let anyone else uncover - including my guild superiors."
        DimOpB2 = "I formed a close friendship or romance with someone in the guild I'm infiltrating."
        DimOpB3 = "The Dimir agent who recruited me was unmasked and killed. My revenge on the killers will be thorough and painful."
        DimOpB4 = "I spend as much time as I can in the Ismeri Library because I'm certain an information hub operates behind its facade. I want its secrets!"
        DimOpB5 = "I'm utterly loyal to my superior in the guild, more than to the guild or its guildmaster."
        DimOpB6 = "Someone has discovered my true identity."
        DimOpB = [DimOpB1, DimOpB2, DimOpB3, DimOpB4, DimOpB5, DimOpB6]
        player.Bond = random.choice(DimOpB)
        DimOpF1 = "I like secrets so much that I'm reluctant to share details of a plan even with those who need to know."
        DimOpF2 = "I would let my friends die rather than reveal my true identity."
        DimOpF3 = "I have trouble trusting anyone but myself."
        DimOpF4 = "I have a particular vice that puts all my secrets at risk if I'm not careful."
        DimOpF5 = "I'm pretty sure I've done something horrible that I can't remember because of the guild's mind magic."
        DimOpF6 = "I put too much trust in the people who give me orders."
        DimOpF = [DimOpF1, DimOpF2, DimOpF3, DimOpF4, DimOpF5, DimOpF6]
        player.Flaw = random.choice(DimOpF)
        player.gold = 10
        player.equipment = ["A Dimir insignia", "Three small knives", "A set of dark-colored common clothes"]
        player.languages, player.slang = languagegen(param, player.languages, player.slang)   
        player.skills_dict["DeceNum"] += 1
        player.skills_dict["SteaNum"] += 1
        player.proficiencies.append(dnd_tools.kits["DisgKit"]["Name"])
    if (player.background == "Entertainer") or (player.background == "Gladiator"):         
        P1 = "I know a story relevant to almost every situation."
        P2 = "Whenever I come to a new place, I collect local rumors and spread gossip."
        P3 = "I'm a hopeless romantic, always searching for that 'special someone'."
        P4 = "Nobody stays angry at me or around me for long, since I can defuse any amount of tension."
        P5 = "I love a good insult, even one directed at me."
        P6 = "I get bitter if I'm not the center of attention."
        P7 = "I'll settle for nothing less than perfection."
        P8 = "I change my mood or my mind as quickly as I change key in a song."
        PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
        player.Trait = random.choice(PTR)
        I1 = "Beauty - When I perform, I make the world better than it was."
        I2 = "Tradition - The stories, legends, and songs of the past must never be forgotten, for they teach us who we are."
        I3 = "Creativity - The world is in need of new ideas and bold action."
        I4 = "Greed - I'm only in it for the money and fame."
        I5 = "People - I like seeing the smiles on people's faces when I perform. That's all that matters. "
        I6 = "Honesty - Art should reflect the soul; it should come from within and reveal who we really are. "
        IDE = [I1, I2, I3, I4, I5, I6]
        player.Ideal = random.choice(IDE)
        B1 = "My instrument is my most treasured possession, and it reminds me of someone I love."
        B2 = "Someone stole my precious instrument, and someday I'll get it back."
        B3 = "I want to be famous, whatever it takes."
        B4 = "I idolize a hero of the old tales and measure my deeds against that person's."
        B5 = "I will do anything to prove myself superior to my hated rival."
        B6 = "I would do anything for the other members of my old troupe."
        BND = [B1, B2, B3, B4, B5, B6]
        player.Bond = random.choice(BND)
        F1 = "I'll do anything to win fame and renown."
        F2 = "I'm a sucker for a pretty face."
        F3 = "A scandal prevents me from ever going home again. That kind of trouble seems to follow me around."
        F4 = "I once satirized a noble who still wants my head. It was a mistake that I will likely repeat."
        F5 = "I have trouble keeping my true feelings hidden. My sharp tongue lands me in trouble."
        F6 = "Despite my best efforts, I am unreliable to my friends."
        FLA = [F1, F2, F3, F4, F5, F6]
        player.Flaw = random.choice(FLA)
        player.proficiencies.append(dnd_tools.kits["DisgKit"]["Name"])
        player.proficiencies = musicalinstr(param, player.proficiencies)
        player.skills_dict["AcroNum"] += 1
        player.skills_dict["PerfNum"] += 1 
        player.gold = 15
        player.equipment = ["A Musical Instrument (one of your choice)", "The favor of an admirer (love letter, lock of hair, or trinket)", "A Costume"]
    if player.background == "Faceless":   
        FacPT1 = "I'm earnest and uncommonly direct."
        FacPT2 = "I strive to have no personality-it's easier to forget what's hardly there."
        FacPT3 = "I treasure a memento of the person or instance that set me upon my path."
        FacPT4 = "I sleep just as much as I need to and on an unusual schedule."
        FacPT5 = "I think far ahead, a detachedness often mistaken for daydreaming."
        FacPT6 = "I cultivate a single obscure hobby or study and eagerly discuss it at length."
        FacPT7 = "I am ever learning how to be among others-when to stay quiet, when to laugh."
        FacPT8 = "I behave like an extreme opposite of my persona."
        FacPT = [FacPT1,  FacPT2, FacPT3, FacPT4, FacPT5, FacPT6, FacPT7, FacPT8]
        player.Trait = random.choice(FacPT)
        FacId1 = "Justice. Place in society shouldn't determine one's access to what is right. (Good)"
        FacId2 = "Security. Doing what must be done can't bring the innocent to harm. (Lawful)"
        FacId3 = "Confusion. Deception is a weapon. Strike from where your foes won't expect. (Chaotic)"
        FacId4 = "Infamy. My name will be a malediction, a curse that fulfills my will. (Evil)"
        FacId5 = "Incorruptibility. Be a symbol, and leave your flawed being behind. (Any)"
        FacId6 = "Anonymity. It's my deeds that should be remembered, not their instrument. (Any)"
        FacId = [FacId1,  FacId2, FacId3, FacId4, FacId5, FacId6]
        player.Ideal = random.choice(FacId)
        FacB1 = "I do everything for my family. My first thought is keeping them safe."
        FacB2 = "What I do, I do for the world. The people don't realize how much they need me."
        FacB3 = "I've seen too many in need. I must not fail them as everyone else has."
        FacB4 = "I stand in opposition, less the wicked go unopposed."
        FacB5 = "I am exceptional. I do this because no one else can, and no one can stop me."
        FacB6 = "I do everything for those who were taken from me."
        FacB = [FacB1,  FacB2, FacB3, FacB4, FacB5, FacB6]
        player.Bond = random.choice(FacB)
        FacF1 = "I am callous about death. It comes to us all eventually."
        FacF2 = "I never make eye contact or hold it unflinchingly."
        FacF3 = "I have no sense of humor. Laughing is uncomfortable and embarrassing."
        FacF4 = "I overexert myself, sometimes needing to recuperate for a day or more."
        FacF5 = "I think far ahead, a detachedness often mistaken for daydreaming."
        FacF6 = "I see morality entirely in black and white."
        FacF = [FacF1,  FacF2, FacF3, FacF4, FacF5, FacF6]
        player.Flaw = random.choice(FacF)
        player.gold = 10
        player.equipment = ["A Disguise kit", "A Costume"]
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.skills_dict["DeceNum"] += 1
        player.skills_dict["IntiNum"] += 1
        player.proficiencies.append(dnd_tools.kits["DisgKit"]["Name"])                 
    if player.background == "Failed Merchant":
        FaMePT1 = "I didn't have the cutthroat attitude necessary to succeed. I won't make that mistake again."
        FaMePT2 = "Even my competitors said I was affable and talented. Those traits should serve me well."
        FaMePT3 = "To prosper, you have to be in control."
        FaMePT4 = "The customer is always right."
        FaMePT5 = "I was cutting corners and breaking deals to maximize profit. That's why I failed."
        FaMePT6 = "When I get an idea, I am single-minded in its execution—even if it's a terrible idea."
        FaMePT7 = "If I can be everyone's friend, I'll always have support."
        FaMePT8 = "My heart wasn't in being a merchant, so I failed. I'm not all that keen on adventuring either, but I need the money."
        FaMePT = [FaMePT1, FaMePT2, FaMePT3, FaMePT4, FaMePT5, FaMePT6, FaMePT7, FaMePT8]
        player.Trait = random.choice(FaMePT)
        FaMeId1 = "Survival. Where there's life, there's hope. If I remain alive and flexible, I can succeed. (Any)"
        FaMeId2 = "Generosity. People helped me when I was down. Now that I'm back on my feet, I'll pay it forward. (Good)"
        FaMeId3 = "Excitement. Caution got me nowhere in my previous business. I'm not going to let it hold me back now. (Chaotic)"
        FaMeId4 = "Wealth. With enough coin, I can buy comfort, power, knowledge, and even eternal life. Nothing will stand between me and money. (Evil)"
        FaMeId5 = "Stability. The mercantile trade was too chaotic for me. I need a nice stable profession, like adventuring. (Lawful)"
        FaMeId6 = "Redemption. Too many people consider me a failure. So I need to prove them wrong. (Any)"
        FaMeId = [FaMeId1, FaMeId2, FaMeId3, FaMeId4, FaMeId5, FaMeId6]
        player.Ideal = random.choice(FaMeId)
        FaMeB1 = "My family means everything to me. I failed them before, and I must not do so again."
        FaMeB2 = "My church provides a connection to my god, so I must ensure that it is protected and funded."
        FaMeB3 = "My former business partner fell ill, and then our business failed. Part of my new venture involves earning enough to take care of their family."
        FaMeB4 = "If I take care of my possessions, they'll take care of me. People come and go, but a weapon or a wand is something you can always rely on."
        FaMeB5 = "Although my business failed, the people of my community were kind to me. I'll do everything in my power to protect them."
        FaMeB6 = "I owe a dangerous person a lot of money. As long as they're happy, they let my debt rest unpaid."
        FaMeB = [FaMeB1, FaMeB2, FaMeB3, FaMeB4, FaMeB5, FaMeB6]
        player.Bond = random.choice(FaMeB)
        FaMeF1 = "Why spend gold here when you can buy the same thing for copper in the next town?"
        FaMeF2 = "I must have the best of everything. Like, right now."
        FaMeF3 = "You haven't heard of me? I'm sure that's because of your ignorance and low breeding."
        FaMeF4 = "I failed, but I'm awesome. So when anyone else is successful, it must be because of nepotism, dishonesty, or dumb luck."
        FaMeF5 = "I find that most people are trustworthy. Hey, where's my belt pouch?"
        FaMeF6 = "Nothing gets between me and danger except my fellow adventurers. So I'll be sure to put them there."
        FaMeF = [FaMeF1, FaMeF2, FaMeF3, FaMeF4, FaMeF5, FaMeF6]
        player.Flaw = random.choice(FaMeF)
        player.gold = 10
        player.equipment = ["One set of Artisan's Tools", "Merchant's Scale", "A set of Fine Clothes"]
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.proficiencies = artisantools(param, player.proficiencies)
        player.skills_dict["InveNum"] += 1
        player.skills_dict["PersNum"] += 1  
    if player.background == "Far Traveler":
        FTPT1 = "I have different assumptions from those around me concerning personal space, blithely invading others' space in innocence, or reacting to ignorant invasion of my own."
        FTPT2 = "I have my own ideas about what is and is not food, and I find the eating habits of those around me fascinating, confusing, or revolting."
        FTPT3 = "I have a strong code of honor or sense of propriety that others don't comprehend."
        FTPT4 = "I express affection or contempt in ways that are unfamiliar to others."
        FTPT5 = "I honor my deities through practices that are foreign to this land."
        FTPT6 = "I begin or end my day with small traditional rituals that are unfamiliar to those around me."
        FTPT = [FTPT1, FTPT2, FTPT3, FTPT4, FTPT5, FTPT6]
        player.Trait = random.choice(FTPT)
        FTIdeal1 = "Open. I have much to learn from the kindly folk I meet along my way. (Good)"
        FTIdeal2 = "Reserved. As someone new to these strange lands, I am cautious and respectful in my dealings. (Lawful)"
        FTIdeal3 = "Adventure. I'm far from home, and everything is strange and wonderful! (Chaotic)"
        FTIdeal4 = "Cunning. Though I may not know their ways, neither do they know mine, which can be to my advantage. (Evil)"
        FTIdeal5 = "Inquisitive. Everything is new, but I have a thirst to learn. (Neutral)"
        FTIdeal6 = "Suspicious. I must be careful, for I have no way of telling friend from foe here. (Any)"
        FTIdeal = [FTIdeal1, FTIdeal2, FTIdeal3, FTIdeal4, FTIdeal5, FTIdeal6]
        player.Ideal = random.choice(FTIdeal)
        FTBond1 = "So long as I have this token from my homeland, I can face any adversity in this strange land."
        FTBond2 = "The gods of my people are a comfort to me so far from home."
        FTBond3 = "I hold no greater cause than my service to my people."
        FTBond4 = "My freedom is my most precious possession. I'll never let anyone take it from me again."
        FTBond5 = "I'm fascinated by the beauty and wonder of this new land."
        FTBond6 = "Though I had no choice, I lament having to leave my loved ones behind. I hope to see them again one day."
        FTBond = [FTBond1, FTBond2, FTBond3, FTBond4, FTBond5, FTBond6]
        player.Bond = random.choice(FTBond)
        FTFlaw1 = "I am secretly (or not so secretly) convinced of the superiority of my own culture over that of this foreign land."
        FTFlaw2 = "I pretend not to understand the local language in order to avoid interactions I would rather not have."
        FTFlaw3 = "I have a weakness for the new intoxicants and other pleasures of this land."
        FTFlaw4 = "I don't take kindly to some of the actions and motivations of the people of this land, because these folk are different from me."
        FTFlaw5 = "I consider the adherents of other gods to be deluded innocents at best, or ignorant fools at worst."
        FTFlaw6 = "I have a weakness for the exotic beauty of the people of these lands."
        FTFlaw = [FTFlaw1, FTFlaw2, FTFlaw3, FTFlaw4, FTFlaw5, FTFlaw6]
        player.Flaw = random.choice(FTFlaw)
        player.proficiencies = gamingsetsmusicalinstr(param, player.proficiencies)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.skills_dict["InsiNum"] += 1
        player.skills_dict["PercNum"] += 1     
        player.gold = 15
        player.equipment = ["One set of Traveler's Clothes", "Poorly wrought maps from your homeland that depict where you are in Faerun"]     
        tools = [
            dnd_tools.gaming_sets["DiceSet"], 
            dnd_tools.gaming_sets["DrgnChSet"], 
            dnd_tools.gaming_sets["PlyCrdSet"], 
            dnd_tools.gaming_sets["ThrDgnASet"], 
            dnd_tools.musical_instr["Bagpipes"], 
            dnd_tools.musical_instr["Birdpipes"], 
            dnd_tools.musical_instr["Drum"], 
            dnd_tools.musical_instr["Dulcimer"], 
            dnd_tools.musical_instr["Flute"], 
            dnd_tools.musical_instr["Glaur"], 
            dnd_tools.musical_instr["HndDrum"], 
            dnd_tools.musical_instr["Horn"], 
            dnd_tools.musical_instr["Longhorn"], 
            dnd_tools.musical_instr["Lute"], 
            dnd_tools.musical_instr["Lyre"], 
            dnd_tools.musical_instr["PFlute"], 
            dnd_tools.musical_instr["Shawm"], 
            dnd_tools.musical_instr["Songhorn"], 
            dnd_tools.musical_instr["Tantan"], 
            dnd_tools.musical_instr["Thelarr"], 
            dnd_tools.musical_instr["Viol"], 
            dnd_tools.musical_instr["Wargong"], 
            dnd_tools.musical_instr["Yarting"], 
            dnd_tools.musical_instr["Zulkoon"]
        ]
        for tool in tools:
            if tool["Name"] in player.proficiencies:
                player.equipment.append(tool)    
    if player.background == "Feylost": 
        FeyWPT1 = "I'm haunted by fey laughter that only I can hear, though I know it's just my mind playing tricks on me."
        FeyWPT2 = "Like a nomad, I can't settle down in one place for very long."
        FeyWPT3 = "Good music makes me weep like a baby."
        FeyWPT4 = "Wherever I go, I try to bring a little of the warmth and tranquility of home with me."
        FeyWPT5 = "I have never lost my childlike sense of wonder."
        FeyWPT6 = "When I have a new idea, I get wildly excited about it until I come up with another, better idea."
        FeyWPT7 = "I live by my own set of weird and wonderful rules."
        FeyWPT8 = "I can't bring myself to trust most adults."
        FeyWPT = [FeyWPT1, FeyWPT2, FeyWPT3, FeyWPT4, FeyWPT5, FeyWPT6, FeyWPT7, FeyWPT8]
        player.Trait = random.choice(FeyWPT)
        FeyWId1 = "Friendship. I never leave a friend behind. (Good)"
        FeyWId2 = "Empathy. No creature should be made to suffer. (Good)"
        FeyWId3 = "Wanderlust. I prefer to take the less traveled path. (Chaotic)"
        FeyWId4 = "Changeability. Change is good, which is why I live by an ever-changing set of rules. (Chaotic)"
        FeyWId5 = "Honor. A deal is a deal, and I would never break one. (Lawful)"
        FeyWId6 = "Rule of Three. Everything in the multiverse happens in threes. I see the 'rule of three' everywhere. (Lawful)"
        FeyWId7 = "Obsession. I won't let go of a grudge. (Evil)"
        FeyWId8 = "Greed. I will do whatever it takes to get what I want, regardless of the harm it might cause. (Evil)"
        FeyWId = [FeyWId1,  FeyWId2, FeyWId3, FeyWId4, FeyWId5, FeyWId6, FeyWId7, FeyWId8]
        player.Ideal = random.choice(FeyWId)
        FeyWB1 = "I would never break my word."
        FeyWB2 = "I find magic in all its forms to be compelling. The more magical a place, the more I am drawn to it."
        FeyWB3 = "I do what I can to protect the natural world."
        FeyWB4 = "A trusted friend is the most important thing in the multiverse to me."
        FeyWB5 = "I can't bring myself to harm a Fey creature, either because I consider myself one or because I fear the repercussions."
        FeyWB6 = "The Witchlight Carnival feels like home to me."
        FeyWB7 = "I'm drawn to the Feywild and long to return there, if only for a short while."
        FeyWB8 = "I feel indebted to Mister Witch and Mister Light for giving me a home and a purpose."
        FeyWB = [FeyWB1,  FeyWB2, FeyWB3, FeyWB4, FeyWB5, FeyWB6, FeyWB7, FeyWB8]
        player.Bond = random.choice(FeyWB)
        FeyWF1 = "I easily lose track of time. My poor sense of time means I'm always late."
        FeyWF2 = "I think the whole multiverse is out to get me."
        FeyWF3 = "I'm always operating under a tight timeline, and I'm obsessed with keeping everything on schedule."
        FeyWF4 = "I'm a kleptomaniac who covets shiny, sparkling treasure."
        FeyWF5 = "I'm forgetful. Sometimes I can't remember even the simplest things."
        FeyWF6 = "I never give away anything for free and always expect something in return."
        FeyWF7 = "I have many vices and tend to indulge them."
        FeyWF8 = "I'm always changing my mind—well, almost always."
        FeyWF = [FeyWF1,  FeyWF2, FeyWF3, FeyWF4, FeyWF5, FeyWF6, FeyWF7, FeyWF8]
        player.Flaw = random.choice(FeyWF)
        player.gold = 8
        player.equipment = ["A musical instrument (one of your choice)", "A set of traveler's clothes", "Three trinkets (each determined by rolling on the Feywild Trinkets table)"]
        player.proficiencies = musicalinstr(param, player.proficiencies)
        langlist = ["Elvi", "Gnom", "Gobl", "Sylv"]
        player.languages, player.slang = choicefourlang(param, player.languages, player.slang, langlist)
        player.skills_dict["DeceNum"] += 1
        player.skills_dict["SurvNum"] += 1           
    if player.background == "Fisher":  
        FshPT1 = "I am unmoved by the wrath of nature."
        FshPT2 = "My friends are my crew; we sink or Roat together."
        FshPT3 = "I need long stretches of quiet to clear my head."
        FshPT4 = "Rich folk don't know the satisfaction of hard work."
        FshPT5 = "I laugh heartily, feel deeply, and fear nothing."
        FshPT6 = "I work hard; nature offers no handouts."
        FshPT7 = "I dislike bargaining; state your price and mean it."
        FshPT8 = "Luck favors me, and l take risks others might not."
        FshPT = [FshPT1, FshPT2, FshPT3, FshPT4, FshPT5, FshPT6, FshPT7, FshPT8]
        player.Trait = random.choice(FshPT)
        FshId1 = "Camaraderie. Good people make even the longest voyage bearable. (Good)"
        FshId2 = "Luck. Our luck depends on respecting its rules-now throw this salt over your shoulder (Lawful)"
        FshId3 = "Daring. The richest bounty goes to those who risk everything. (Chaotic)"
        FshId4 = "Plunder. Take all that you can and leave nothing for the scavengers. (Evil)"
        FshId5 = "Balance. Do not fish the same spot twice in a row; suppress your greed, and nature will reward you. (Neutral)"
        FshId6 = "Hard Work. No wave can move a soul hard at work. (Any)"
        FshId = [FshId1, FshId2, FshId3, FshId4, FshId5, FshId6]
        player.Ideal = random.choice(FshId)
        FshB1 = "I lost something important in the deep sea, and I intend to find it."
        FshB2 = "Someone else's greed destroyed my livelihood, and I will be compensated."
        FshB3 = "l will fish the many famous waters of this land."
        FshB4 = "The gods saved me during a terrible storm, and I will honor their gift."
        FshB5 = "My destiny awaits me at the bottom of a particular pond in the Feywild."
        FshB6 = "I must repay my village's debt."
        FshB = [FshB1, FshB2, FshB3, FshB4, FshB5, FshB6]
        player.Bond = random.choice(FshB)
        FshF1 = "l am judgmental, especially of those I deem homebodies or otherwise lazy."
        FshF2 = "I become depressed and anxious if I'm away from the sea too long."
        FshF3 = "l have lived a hard life and find it difficult to empathize with others."
        FshF4 = "I am inclined to tell long-winded stones at inopportune times."
        FshF5 = "I work hard, but l play harder."
        FshF6 = "l am obsessed with catching an elusive aquatic beast, often to the detriment of other pursuits."
        FshF = [FshF1, FshF2, FshF3, FshF4, FshF5, FshF6]
        player.Flaw = random.choice(FshF)
        player.gold = 10
        player.equipment = ["Fishing Tackle", "A net", "A favorite fishing lure or oiled leather wading boots", "A set of Traveler's Clothes"]
        player.languages, player.slang = languagegen(param, player.languages, player.slang)      
        player.skills_dict["HistNum"] += 1
        player.skills_dict["SurvNum"] += 1    
    if (player.background == "Folk Hero") or (player.background == "Inheritor"):       
        P1 = "I judge people by their actions, not their words."
        P2 = "If someone is in trouble, I am always ready to lend help."
        P3 = "When I set my mind to something, I follow through no matter what gets in my way."
        P4 = "I have a strong sense of fair play and always try to find the most equitable solution to arguments."
        P5 = "I am confident in my own abilities and do what I can to instill confidence in others."
        P6 = "Thinking is for other people. I prefer action."
        P7 = "I misuse long words in an attempt to sound smarter."
        P8 = "I get bored easily. When am I going to get on with my destiny?"
        PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
        player.Trait = random.choice(PTR)
        I1 = "Respect - People deserve to be treated with dignity and respect. "
        I2 = "Fairness - No one should get preferential treatment before the law, and no one is above the law. "
        I3 = "Freedom - Tyrants must not be allowed to oppress the people. "
        I4 = "Might - If I become strong, I can take what I want, what I deserve."
        I5 = "Sincerity - There is no good in pretending to be something I am not. "
        I6 = "Destiny - Nothing and no one can steer me away from my higher calling. "
        IDE = [I1, I2, I3, I4, I5, I6]
        player.Ideal = random.choice(IDE)
        B1 = "I have a family, but I have no idea where they are. One day, I hope to see them again."
        B2 = "I worked the land, I love the land, and I will protect the land."
        B3 = "A proud noble once gave me a horrible beating, and I will take my revenge on any bully I encounter."
        B4 = "My tools are symbols of my past life, and I carry them so that I will never forget my roots."
        B5 = "I protect those who cannot protect themselves."
        B6 = "I wish my childhood sweetheart had come with me to pursue my destiny."
        BND = [B1, B2, B3, B4, B5, B6]
        player.Bond = random.choice(BND)
        F1 = "The tyrant who rules my land will stop at nothing to see me killed."
        F2 = "I am convinced of the significance of my destiny, and blind to my shortcomings and the risk of failure."
        F3 = "The people who knew me when I was young know my shameful secret, so I can never go home again."
        F4 = "I have a weakness for the vices of the city, especially hard drink."
        F5 = "Secretly, I believe that things would be better if I were a tyrant lording over the land."
        F6 = "I have trouble trusting in my allies."
        FLA = [F1, F2, F3, F4, F5, F6]
        player.Flaw = random.choice(FLA)
        if player.background == "Folk Hero":
            player.skills_dict["AnHaNum"] += 1
            player.skills_dict["SurvNum"] += 1
            player.proficiencies.append(dnd_tools.vehicles["VehLand"])
            player.proficiencies = artisantools(param, player.proficiencies)
            player.gold = 10
            player.equipment = ["A set of Artisan's Tools (one of your choice)", "A Shovel", "An Iron Pot", "A set of Common Clothes"]
        if player.background == "Inheritor":
            player.skills_dict["SurvNum"] += 1
            player.skills_dict["ArcaNum"], player.skills_dict["HistNum"], player.skills_dict["ReliNum"] = choicethreeskill(param, player.skills_dict, "ArcaNum", "HistNum", "ReliNum", dnd_tools.skills["Arcana"], dnd_tools.skills["History"], dnd_tools.skills["Religion"])
            player.proficiencies = gamingsetsmusicalinstr(param, player.proficiencies)
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.gold = 15                  
            player.equipment = ["A set of Traveler's Clothes"]
            tools = [
                dnd_tools.gaming_sets["DiceSet"], 
                dnd_tools.gaming_sets["DrgnChSet"], 
                dnd_tools.gaming_sets["PlyCrdSet"], 
                dnd_tools.gaming_sets["ThrDgnASet"], 
                dnd_tools.musical_instr["Bagpipes"], 
                dnd_tools.musical_instr["Birdpipes"], 
                dnd_tools.musical_instr["Drum"], 
                dnd_tools.musical_instr["Dulcimer"], 
                dnd_tools.musical_instr["Flute"], 
                dnd_tools.musical_instr["Glaur"], 
                dnd_tools.musical_instr["HndDrum"], 
                dnd_tools.musical_instr["Horn"], 
                dnd_tools.musical_instr["Longhorn"], 
                dnd_tools.musical_instr["Lute"], 
                dnd_tools.musical_instr["Lyre"], 
                dnd_tools.musical_instr["PFlute"], 
                dnd_tools.musical_instr["Shawm"], 
                dnd_tools.musical_instr["Songhorn"], 
                dnd_tools.musical_instr["Tantan"], 
                dnd_tools.musical_instr["Thelarr"], 
                dnd_tools.musical_instr["Viol"], 
                dnd_tools.musical_instr["Wargong"], 
                dnd_tools.musical_instr["Yarting"], 
                dnd_tools.musical_instr["Zulkoon"]
            ]
            for tool in tools:
                if tool["Name"] in player.proficiencies:
                    player.equipment.append(tool) 
    if player.background == "Gambler":
        GamblerPT1 = "I plan for every contingency. Leave nothing to chance!"
        GamblerPT2 = "Every copper wants to be a silver. Each bet is an opportunity."
        GamblerPT3 = "I'm one of Lady Luck's favored. Anything I try is destined to succeed."
        GamblerPT4 = "I've lost so much to gambling that I refuse to spend money on anything anymore."
        GamblerPT5 = "Nothing is certain. Planning is a coward's act."
        GamblerPT6 = "I can't be sure who I've swindled, cheated, or defeated, so I keep a low profile in public."
        GamblerPT7 = "The perfect bet is out there somewhere. I just have to keep my eyes open."
        GamblerPT8 = "I have beaten my addiction, but all it takes is one weak moment and I'll be back at the card table."
        GamblerPT = [GamblerPT1, GamblerPT2, GamblerPT3, GamblerPT4, GamblerPT5, GamblerPT6, GamblerPT7, GamblerPT8]
        player.Trait = random.choice(GamblerPT)
        GamblerId1 = "Knowledge. Knowledge is power, and knowing which horse to back is the key to success. (Any)"
        GamblerId2 = "Fate. Whatever happens is fated, regardless of any planning or striving. (Lawful)"
        GamblerId3 = "Bravery. If you want to succeed, you have to take risks. (Chaotic)"
        GamblerId4 = "Survival. You can't win if you're dead. Live to fight another day—when the odds might be more in your favor. (Any)"
        GamblerId5 = "Reliability. When I was in need, I was able to rely on others. Now I want to be the one others rely on. (Good)"
        GamblerId6 = "Victory. Winning is the real measure of a person. In the end, the only thing that matters is the scoreboard. (Evil)"
        GamblerId = [GamblerId1, GamblerId2, GamblerId3, GamblerId4, GamblerId5, GamblerId6]
        player.Ideal = random.choice(GamblerId) 
        GamblerB1 = "One person in particular owes me a lot of money, and I need to keep them alive if I want to be repaid."
        GamblerB2 = "I'm loyal to the friend or family member who taught me how to gamble."
        GamblerB3 = "The person who saved me from my gambling addiction is the only reason I'm alive today."
        GamblerB4 = "A patron once fronted me money in exchange for a percentage of my winnings. I owe them a debt of gratitude. And a lot of cash."
        GamblerB5 = "A criminal syndicate I once played for isn't happy I left the game, and its enforcers are looking for me."
        GamblerB6 = "Urchins once helped me find marks for my games. Now I'm driven to help them escape the streets."
        GamblerB = [GamblerB1, GamblerB2, GamblerB3, GamblerB4, GamblerB5, GamblerB6]
        player.Bond = random.choice(GamblerB) 
        GamblerF1 = "I don't know when to quit. Especially when everyone else is telling me to."
        GamblerF2 = "I save my sympathy for my friends, and I have no friends."
        GamblerF3 = "You think we're in trouble now? Let me tell you how bad things are likely to get!"
        GamblerF4 = "You can loan me a little, right? I've got a sure thing. I'll double your money, guaranteed."
        GamblerF5 = "I was once a terribly flawed person, like you. Let me tell you how you can save yourself."
        GamblerF6 = "I'm a great gambler. I'm just bad at math and logic."
        GamblerF = [GamblerF1, GamblerF2, GamblerF3, GamblerF4, GamblerF5, GamblerF6]
        player.Flaw = random.choice(GamblerF)
        player.gold = 15
        player.equipment = ["One Gaming Set", "A lucky charm", "A set of Fine Clothes"]
        player.proficiencies = gamingsets(param, player.proficiencies)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.skills_dict["DeceNum"] += 1
        player.skills_dict["InsiNum"] += 1          
    if player.background == "Gate Warden":
        player.gold = 10
        player.equipment = ["A ring of keys to unknown locks", "A blank book", "An ink pen or quill", "A bottle of black ink", "A set of traveler's clothes"]
        player.skills_dict["PersNum"] += 1
        player.skills_dict["SurvNum"] += 1
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.Trait = ""
        player.Ideal = ""
        player.Bond = ""
        player.Flaw = ""                      
    if player.background == "Giant Foundling":
        player.gold = 10
        player.equipment = ["A backpack", "A set of traveler's clothes", "A small stone or sprig that reminds you of home"]
        player.skills_dict["IntiNum"] += 1
        player.skills_dict["SurvNum"] += 1
        langs = ["Gian"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.Trait = ""
        player.Ideal = ""
        player.Bond = ""
        player.Flaw = ""            
    if player.background == "Golgari Agent":
        GoAPT1 = "Remember, I could kill you in your sleep. Or put centipedes in your bedroll."
        GoAPT2 = "I like to remind people of their inevitable demise."
        GoAPT3 = "Sometimes I give voice to the whispers of the rot, which I hear but no one else does."
        GoAPT4 = "I do my best to discourage anyone from approaching or talking to me."
        GoAPT5 = "I have accepted my death. Hence, I don't fear it."
        GoAPT6 = "Like roots growing through stone, I am relentless and determined in my action."
        GoAPT7 = "I put my knowledge of anatomy to use by narrating the injuries my enemies suffer in grisly detail."
        GoAPT8 = "Like a wild animal, I lash out viciously when I'm provoked - and I'm easily provoked."
        GoAPT = [GoAPT1, GoAPT2, GoAPT3, GoAPT4, GoAPT5, GoAPT6, GoAPT7, GoAPT8]
        player.Trait = random.choice(GoAPT)
        GoAgI1 = "Guild: My guild is all that really matters. (Any)"
        GoAgI2 = "Stoicism: All of us are part of the cyclical march of nature, which will continue with or without us. (Neutral)"
        GoAgI3 = "Nature: The natural world is more important than the edifices of the city and civilization. (Neutral)"
        GoAgI4 = "Interdependence: We are all part of nature's web. (Lawful)"
        GoAgI5 = "Ambition: The time of Golgari ascendance is at hand, and I intend to have a prominent place in the new world order. (Evil)"
        GoAgI6 = "Live and Let Live: Meddling in the affairs of other guilds is a great way to get squashed like a bug. (Neutral)"
        GoAgI = [GoAgI1, GoAgI2, GoAgI3, GoAgI4, GoAgI5, GoAgI6]
        player.Ideal = random.choice(GoAgI)
        GoAgB1 = "I cherish the finger of a family member who was petrified by a medusa."
        GoAgB2 = "I have an identical twin who is as different from me as any person could be."
        GoAgB3 = "I want to lead one faction of the guild to a new position of dominance."
        GoAgB4 = "I love spending time in the moss-covered building where I took part in my first reclamation mission."
        GoAgB5 = "I found something in the sewer that must never come to light."
        GoAgB6 = "I am forever grateful to the reclaimer who found me floating facedown in the sewer, moments from death."
        GoAgB = [GoAgB1, GoAgB2, GoAgB3, GoAgB4, GoAgB5, GoAgB6]
        player.Bond = random.choice(GoAgB)
        GoAgF1 = "Death comes for us all, so you can't expect me to take care of someone who can't fight it off."
        GoAgF2 = "I assume that anyone outside the Golgari looks down on me."
        GoAgF3 = "I feel a need for revenge against those who enjoy the privilege of living above ground."
        GoAgF4 = "I don't bother to couch my opinions in flattering words."
        GoAgF5 = "I can't help but pocket any trinket or coin I come across, no matter how worthless."
        GoAgF6 = "I'm convinced that I'm better and stronger than members of other guilds, isolated as they are from the realities of life and death."
        GoAgF = [GoAgF1, GoAgF2, GoAgF3, GoAgF4, GoAgF5, GoAgF6]
        player.Flaw = random.choice(GoAgF)
        player.gold = 10
        player.equipment = ["A Golgari insignia", "A Poisoner's Kit", "A pet beetle or spider", "A set of Common Clothes"]
        player.skills_dict["NatuNum"] += 1
        player.skills_dict["SurvNum"] += 1
        player.proficiencies.append(dnd_tools.kits["PoisKit"]["Name"])
        langlist = ["Elvi", "Gian", "Krau"]
        player.languages, player.slang = choicethreelang(param, player.languages, player.slang, langlist)    
    if (player.background == "Grey Hunter") or (player.background == "Whitestone Rifle Corps"):       
        Trait1 = "I want to make a good impression at all times. That means keeping my clothes and gear clean and in top condition."
        Trait2 = "I don't like being the center of attention. I'd rather let someone else do the talking while I watch their back."
        Trait3 = "I feel safe only if I'm carrying my trusty rifle. And my dagger. And my concealed pistol. Oh, and of course my…"
        Trait4 = "I don't trust people with my secrets easily, so it feels like a big deal when someone else shares a secret with me."
        Trait5 = "I like coming up with solutions to problems using my esoteric knowledge of natural philosophy."
        Trait6 = "Everyone around me takes things so seriously. Sometimes I just want to let loose and have fun!"
        Trait7 = "Knowing things that other people don't know makes me feel special and important."
        Trait8 = "I'm most at home in woods and mountains, where everything feels at once familiar, always growing and changing."
        RifTrait = [Trait1, Trait2, Trait3, Trait4, Trait5, Trait6, Trait7, Trait8]
        player.Trait = random.choice(RifTrait)
        Ideal1 = "Responsibility. I have a duty to protect the people of Whitestone and to uphold the trust placed in me by the de Rolos. (Lawful)"
        Ideal2 = "Militarization. Everyone should have access to the most powerful weapons available, so they can defend themselves effectively. (Evil)"
        Ideal3 = "Cooperation. Any problem can be solved as long as people are willing to work together. (Good)"
        Ideal4 = "Camaraderie. It's important to have people you can trust to help out in a fight—and to uncork a bottle together afterward. (Any)"
        Ideal5 = "Context. There are no universal rights or wrongs. Every choice depends on the details of the situation. (Chaotic)"
        Ideal6 = "Secrecy. Information is valuable, but it can also be dangerous. I'll keep my mouth shut and gather as much intel as I can. (Neutral)"
        RifId = [Ideal1, Ideal2, Ideal3, Ideal4, Ideal5, Ideal6]
        player.Ideal = random.choice(RifId)
        Bond1 = "I never knew what to do with myself until I joined the Rifle Corps. Now I have a purpose and comrades to give me direction."
        Bond2 = "One of my fellow Rifle Corps soldiers saved my life—and then I saved theirs. That kind of bond lasts forever."
        Bond3 = "Whitestone is the best city in all of Tal'Dorei. Nowhere else has been blessed by the Dawnfather and has a clock that tracks the movement of the stars!"
        Bond4 = "My quick thinking saved a noble from assassination, and she showed me great kindness in return. I daren't say it, but I'm more loyal to her than I am to the de Rolos."
        Bond5 = "My weapon is my life. I clean it, repair it, and care for it—and it serves me loyally in return."
        Bond6 = "The people of Whitestone cared for my family when we had nothing. I promise to repay their compassion with my service."
        RifBond = [Bond1, Bond2, Bond3, Bond4, Bond5, Bond6]
        player.Bond = random.choice(RifBond)
        Flaw1 = "Who cares about keeping this gun safe? 'Don't let it fall into the wrong hands!' Ha! It's only a matter of time before someone slips up and these weapons are everywhere."
        Flaw2 = "I think being part of the Rifle Corps is so cool. I love telling people about my position so I can impress them."
        Flaw3 = "My weapon was stolen. I built a new one, but I can't return home until I've tracked down the thief and recovered the original."
        Flaw4 = "I'm tired of protecting spoiled people who don't know how to protect themselves."
        Flaw5 = "I shoot first and ask questions later."
        Flaw6 = "The first and only time I killed someone, it changed my life. I still dream about it, and I'll never be the carefree person I was before."
        RifFlaw = [Flaw1, Flaw2, Flaw3, Flaw4, Flaw5, Flaw6]
        player.Flaw = random.choice(RifFlaw)
        player.gold = 10
        player.equipment = ["Your choice of a musket or a pistol, A set of common clothes"]
        player.skills_dict["AthlNum"], player.skills_dict["PercNum"], player.skills_dict["SurvNum"] = choicethreeskill2(param, player.skills_dict, "AthlNum", "PercNum", "SurvNum", dnd_tools.skills["Athletics"], dnd_tools.skills["Perception"], dnd_tools.skills["Survival"])
        profs = ["Firearms"]
        for prof in profs:
            if prof not in player.proficiencies:
                player.proficiencies.append(prof)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)            
    if player.background == "Grinner":
        GrPT1 = "I love the spotlight. Everyone, look at me!"
        GrPT2 = "Give me a drink and I 'm your friend."
        GrPT3 = "Talk to me about yourself. I 'm a hell of a listener."
        GrPT4 = "I hate to start fights, but I love to finish them."
        GrPT5 = "I can't sit still."
        GrPT6 = "I'm always humming an old tune from my past."
        GrPT7 = "When I don't have a reason to smile, I 'm miserable."
        GrPT8 = "I'm lucky like you wouldn't believe."
        GrPT = [GrPT1, GrPT2, GrPT3, GrPT4, GrPT5, GrPT6, GrPT7, GrPT8]
        player.Trait = random.choice(GrPT)
        GrinI1 = "Revolution. Tyrants must fall, no matter the cost. (Chaotic)"
        GrinI2 = "Compassion. The only way to make a better world is to perform small kindnesses. (Good)"
        GrinI3 = "Justice. A nation built upon just foundations will uphold freedom for all. (Law)"
        GrinI4 = "Expression. Music, joy, and laughter are the keys to freedom. (Good)"
        GrinI5 = "Self-Determination. People should be free to do as they please. (Chaotic)"
        GrinI6 = "Vigilance. A free people must be carefully taught, lest they be misled. (Neutral)"
        GrinI = [GrinI1, GrinI2, GrinI3, GrinI4, GrinI5, GrinI6]
        player.Ideal = random.choice(GrinI)
        GrinB1 = "I lost someone important to an agent of the Dwendalian Empire. That regime will fall."
        GrinB2 = "The first people to be hurt by this war will be the common folk. I need to protect them."
        GrinB3 = "Music helped me through a dark time in my life. Now, I'll use music to change the world."
        GrinB4 = "I will be known as the greatest spy who ever lived."
        GrinB5 = "All life is precious to me. I know I can change the world without taking a humanoid life."
        GrinB6 = "The elite in their ivory towers don't understand how we suffer. I intend to show them."
        GrinB = [GrinB1, GrinB2, GrinB3, GrinB4, GrinB5, GrinB6]
        player.Bond = random.choice(GrinB)
        GrinF1 = "I've never lied once in my life. What? No, I'm not crossing my fingers!"
        GrinF2 = "I do everything big! Subtlety? I don't know the meaning of subtlety! Oh, that's a problem?"
        GrinF3 = "Being a spy in wartime is painful. I've seen so much suffering, I think I'm losing my mind."
        GrinF4 = "I can't focus on my mission. I just want to carouse and sing and play!"
        GrinF5 = "Yeah, that's my name. Yeah, I'm a Grinner spy. Who cares about staying undercover?"
        GrinF6 = "I can't afford to trust anyone. Not. Anyone"
        GrinF = [GrinF1, GrinF2, GrinF3, GrinF4, GrinF5, GrinF6]
        player.Flaw = random.choice(GrinF)
        player.gold = 15
        player.equipment = ["A set of Fine Clothes", "A Disguise Kit", "A Musical Instrument of your choice", "A gold-plated ring depicting a smiling face"]
        player.skills_dict["DeceNum"] += 1
        player.skills_dict["PerfNum"] += 1
        player.proficiencies = musicalinstrthiev(param, player.proficiencies)                                                         
    if player.background == "Grounded": 
        GrPT1 = "I always second guess my choices."
        GrPT2 = "I have learned to not let the comments of others affect me."
        GrPT3 = "I’m eager to show the benefits of my unique perspective."
        GrPT4 = "I’m slow to trust someone new, but open up over shared hardships."
        GrPT5 = "I manufacture difficult situations to prove my abilities."
        GrPT6 = "I get embarrassed easily, even when someone tries to compliment me."
        GrPT7 = "I will deny my fears to everyone."
        GrPT8 = "I want to see how others handle situations I’m afraid of."
        GrPT = [GrPT1, GrPT2, GrPT3, GrPT4, GrPT5, GrPT6, GrPT7, GrPT8]
        player.Trait = random.choice(GrPT)
        GrId1 = "Adversity. Others think of me as weak, but I will prove my worth with hard work and determination. (Lawful)"
        GrId2 = "Encouragement. I try to seek out and support others like me who are seen as outcasts. (Good)"
        GrId3 = "Exploration. I yearn to experience unique cultures and discover new places. (Chaotic)"
        GrId4 = "Safety. In this dangerous world, it’s best to keep your head down and stay cautious. (Neutral)"
        GrId5 = "Rebellion. Who cares what others think of me, so long as my actions reflect how I feel in my heart? (Chaotic)"
        GrId6 = "Compromise. The best way to respect each other’s differences is to find a solution that doesn’t exclude anyone. (Good)"
        GrId = [GrId1, GrId2, GrId3, GrId4, GrId5, GrId6]
        player.Ideal = random.choice(GrId)
        GrB1 = "My family has been the subject of ridicule ever since I left my home perch."
        GrB2 = "A bully from my childhood now holds a position of power in my home perch."
        GrB3 = "I follow the teachings of a wise outcast I met in my travels."
        GrB4 = "I feel kinship to a culture outside my own."
        GrB5 = "I won’t tolerate anyone who insults me or my friends."
        GrB6 = "I have found a new family on the forest floor, and they mean more to me than anything."
        GrB = [GrB1, GrB2, GrB3, GrB4, GrB5, GrB6]
        player.Bond = random.choice(GrB)
        GrF1 = "I am incapable of action when I’m at great heights."
        GrF2 = "I lash out at the slightest insult."
        GrF3 = "I keep a distance from others so they won’t learn of my fears."
        GrF4 = "I project my insecurities onto others."
        GrF5 = "I am uncouth and mannerless."
        GrF6 = "I find hard to trust other birdfolk."
        GrF = [GrF1, GrF2, GrF3, GrF4, GrF5, GrF6]
        player.Flaw = random.choice(GrF)
        player.gold = 5
        player.equipment = ["A set of Artisan’s Tools (one of your choice)", "A walking stick", "A trinket from another culture", "Traveling clothes"]
        player.skills_dict["AthlNum"] += 1
        player.skills_dict["InsiNum"] += 1
        player.proficiencies = artisantools(param, player.proficiencies)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)         
    if player.background == "Gruul Anarch":
        GrAPT1 = "Unlike people, the beasts of the wild are friends who won't stab me in the back."
        GrAPT2 = "Go ahead and insult me - I dare you."
        GrAPT3 = "I scorn those who can't survive away from the comforts of the city."
        GrAPT4 = "Don't tell me I'm not allowed to do something."
        GrAPT5 = "Laws are for people who are afraid to face their inner beasts."
        GrAPT6 = "I smear the blood of my enemies over my skin."
        GrAPT7 = "I was, in fact, raised by maaka."
        GrAPT8 = "HarrRRAAGGHH! [I rarely form a coherent sentence and prefer to express myself by breaking things.]"
        GrAPT = [GrAPT1, GrAPT2, GrAPT3, GrAPT4, GrAPT5, GrAPT6, GrAPT7, GrAPT8]
        player.Trait = random.choice(GrAPT)
        GrAnI1 = "Clan: My clan is all that really matters. (Any)"
        GrAnI2 = "Anarchy: No person or law or custom can tell another what to do. (Chaotic)"
        GrAnI3 = "Nature: We weren't born tame or domesticated, so we shouldn't have to live that way. (Neutral)"
        GrAnI4 = "Might: The strongest are meant to dominate the weak. (Evil)"
        GrAnI5 = "Rage: AAAAAARRRRggggh! [To live is to feel and express the rage burning in your belly.] (Chaotic)"
        GrAnI6 = "Tradition: The Old Ways must be preserved and upheld. (Any)"
        GrAnI = [GrAnI1, GrAnI2, GrAnI3, GrAnI4, GrAnI5, GrAnI6]
        player.Ideal = random.choice(GrAnI)
        GrAnB1 = "I am determined that one day I will lead my clan - or a new one."
        GrAnB2 = "I would give my life for my clan chieftain"
        GrAnB3 = "The chieftain of another clan has a grudge against me."
        GrAnB4 = "I am devoted to a sacred site in the m idst of the rubblebelt."
        GrAnB5 = "My weapon is made from the first raktusk I ever hunted."
        GrAnB6 = "GrrrRRAAAAGGHH! [I will do anything to prove myself greater than my siblings or ancestors.]"
        GrAnB = [GrAnB1, GrAnB2, GrAnB3, GrAnB4, GrAnB5, GrAnB6]
        player.Bond = random.choice(GrAnB)
        GrAnF1 = "If you question my courage, I will never back down."
        GrAnF2 = "HrrrGGGAAAARRuuuh! [My anger in battle led to the death of a loved one.]"
        GrAnF3 = "I'm as stubborn as a batterboar."
        GrAnF4 = "I'm so convinced of my superiority over soft, civilized people that I 'II take great risks to prove it."
        GrAnF5 = "I'm easily manipulated by people I find attractive."
        GrAnF6 = "I'm not actually all that angry."
        GrAnF = [GrAnF1, GrAnF2, GrAnF3, GrAnF4, GrAnF5, GrAnF6]
        player.Flaw = random.choice(GrAnF)
        player.gold = 10
        player.equipment = ["A Gruul insignia", "A Hunting Trap", "An Herbalism Kit", "The skull of a boar", "A beast-hide cloak", "A set of Traveler's Clothes"]
        player.skills_dict["AnHaNum"] += 1
        player.skills_dict["AthlNum"] += 1
        player.proficiencies.append(dnd_tools.kits["HerbKit"]["Name"])
        langlist = ["Drac", "Gian", "Gobl", "Sylv"]
        player.languages, player.slang = choicefourlang(param, player.languages, player.slang, langlist)       
    if (player.background == "Clan Crafter") or (player.background == "Courtier") or (player.background == "Guild Artisan") or (player.background == "Guild Merchant"):           
        P1 = "I believe that anything worth doing is worth doing right. I ca not help it – I am a perfectionist."
        P2 = "I'm a snob who looks down on those who can't appreciate fine art."
        P3 = "I always want to know how things work and what makes people tick."
        P4 = "I'm full of witty aphorisms and have a proverb for every occasion."
        P5 = "I'm rude to people who lack my commitment to hard work and fair play."
        P6 = "I like to talk at length about my profession."
        P7 = "I don't part with my money easily and will haggle tirelessly to get the best deal possible."
        P8 = "I'm well known for my work, and I want to make sure everyone appreciates it. I'm always taken aback when people haven't heard of me."
        PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
        player.Trait = random.choice(PTR)
        I1 = "I'll do anything to get my hands on something rare or priceless."
        I2 = "I'm quick to assume that someone is trying to cheat me."
        I3 = "No one must ever learn that I once stole money from guild coffers."
        I4 = "I am never satisfied with what I have – I always want more."
        I5 = "I would kill to acquire a noble title."
        I6 = "I'm terribly jealous of anyone who can outshine my handiwork. Everywhere I go, I'm surrounded by rivals."
        IDE = [I1, I2, I3, I4, I5, I6]
        player.Ideal = random.choice(IDE)
        B1 = "Community - It is the duty of all civilized people to strengthen the bonds of community and the security of civilization."
        B2 = "Generosity - My talents were given to me so that I could use them to benefit the world. "
        B3 = "Freedom - Everyone should be free to pursue his or her own livelihood. "
        B4 = "Greed - I'm only in it for the money. "
        B5 = "People - I'm committed to the people I care about, not to ideals. "
        B6 = "Aspiration - I work hard to be the best there is at my craft."
        BND = [B1, B2, B3, B4, B5, B6]
        player.Bond = random.choice(BND)
        F1 = "The workshop where I learned my trade is the most important place in the world to me."
        F2 = "I created a great work for someone, and then found them unworthy to receive it. I'm still looking for someone worthy."
        F3 = "I owe my guild a great debt for forging me into the person I am today."
        F4 = "I pursue wealth to secure someone's love."
        F5 = "One day I will return to my guild and prove that I am the greatest artisan of them all."
        F6 = "I will get revenge on the evil forces that destroyed my place of business and ruined my livelihood."
        FLA = [F1, F2, F3, F4, F5, F6]
        player.Flaw = random.choice(FLA)
        if player.background == "Clan Crafter":
            player.skills_dict["HistNum"] += 1
            player.skills_dict["InsiNum"] += 1
            langs = ["Dwarvi"]
            for lang in langs:
                if lang in player.slang:
                    player.languages.append(dnd_tools.languages[lang])
                    player.slang.remove(lang)
                else:
                    player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.proficiencies = artisantools(param, player.proficiencies)
            player.gold = 15
            player.equipment = ["A maker's mark chisel used to mark your handiwork with the symbol of the clan of crafters you learned your skill from", "A set of Traveler's Clothes"]
            tools = [
                dnd_tools.artisan_tools["AlchSupp"],
                dnd_tools.artisan_tools["BrewSupp"],
                dnd_tools.artisan_tools["CallSupp"],
                dnd_tools.artisan_tools["CarpTools"],
                dnd_tools.artisan_tools["CartTools"],
                dnd_tools.artisan_tools["CobbTools"],
                dnd_tools.artisan_tools["CooksUten"],
                dnd_tools.artisan_tools["GlasTools"],
                dnd_tools.artisan_tools["JeweTools"],
                dnd_tools.artisan_tools["LthrwrkTools"],
                dnd_tools.artisan_tools["MasnTools"],
                dnd_tools.artisan_tools["PaintSupp"],
                dnd_tools.artisan_tools["PottTools"],
                dnd_tools.artisan_tools["SmthTools"],
                dnd_tools.artisan_tools["TinkTools"],
                dnd_tools.artisan_tools["WeavTools"],
                dnd_tools.artisan_tools["WdcrvTools"]
            ]
            for tool in tools:
                if tool["Name"] in player.proficiencies:
                    player.equipment.append(tool)   
        if player.background == "Courtier":
            player.skills_dict["InsiNum"] += 1
            player.skills_dict["PersNum"] += 1
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.gold = 5
            player.equipment = ["A set of Fine Clothes"]
        if player.background == "Guild Artisan":
            player.skills_dict["InsiNum"] += 1
            player.skills_dict["PersNum"] += 1
            player.proficiencies = artisantools(param, player.proficiencies)
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.gold = 15
            player.equipment = ["A set of Artisan's Tools (one of your choice)", "A letter of introduction from your guild", "A set of Traveler's Clothes"]
        if player.background == "Guild Merchant":
            player.skills_dict["InsiNum"] += 1
            player.skills_dict["PersNum"] += 1
            player.proficiencies, player.languages, player.slang = ArtTlNavTlLang(param, player.proficiencies, player.languages, player.slang)
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.gold = 15   
            player.equipment = ["A set of Artisan's Tools (one of your choice) or a Mule and a cart", "A letter of introduction from your guild, a set of Traveler's Clothes"]
    if player.background == "Haunted One":
        HauOPT1 = "I don't run from evil. Evil runs from me."
        HauOPT2 = "I like to read and memorize poetry. It keeps me calm and brings me fleeting moments of happiness."
        HauOPT3 = "I spend money freely and live life to the fullest, knowing that tomorrow I might die."
        HauOPT4 = "I live for the thrill of the hunt."
        HauOPT5 = "I don’t talk about the thing that torments me. I’d rather not burden others with my curse."
        HauOPT6 = "I expect danger around every corner."
        HauOPT7 = "I refuse to become a victim, and I will not allow others to be victimized."
        HauOPT8 = "I put no trust in divine beings."
        HauOPT = [HauOPT1, HauOPT2, HauOPT3, HauOPT4, HauOPT5, HauOPT6, HauOPT7, HauOPT8]
        player.Trait = random.choice(HauOPT)
        HauOnId1 = "Selflessness. I try to help those in need, no matter what the personal cost. (Good)"
        HauOnId2 = "Determination. I’ll stop the spirits that haunt me or die trying. (Any)"
        HauOnId3 = "Greater Good. I kill monsters to make the world a safer place, and to exorcise my own demons. (Good)"
        HauOnId4 = "Freedom. I have a dark calling that puts me above the law. (Chaotic)"
        HauOnId5 = "Logic. I like to know my enemy’s capabilities and weaknesses before rushing into battle. (Lawful)"
        HauOnId6 = "Destruction. I’m a monster that destroys other monsters, and anything else that gets in my way. (Evil)"
        HauOnId = [HauOnId1, HauOnId2, HauOnId3, HauOnId4, HauOnId5, HauOnId6]
        player.Ideal = random.choice(HauOnId)
        HauOnB1 = "I keep my thoughts and discoveries in a journal. My journal is my legacy."
        HauOnB2 = "I would sacrifice my life and my soul to protect the innocent."
        HauOnB3 = "My torment drove away the person I love. I strive to win back the love I’ve lost."
        HauOnB4 = "A terrible guilt consumes me. I hope that I can find redemption through my actions."
        HauOnB5 = "There’s evil in me, I can feel it. It must never be set free."
        HauOnB6 = "I have a child to protect. I must make the world a safer place for them."
        HauOnB = [HauOnB1, HauOnB2, HauOnB3, HauOnB4, HauOnB5, HauOnB6]
        player.Bond = random.choice(HauOnB)
        HauOnF1 = "I have certain rituals that I must follow every day. I can never break them."
        HauOnF2 = "I assume the worst in people."
        HauOnF3 = "I feel no compassion for the dead. They’re the lucky ones."
        HauOnF4 = "I have an addiction."
        HauOnF5 = "I am a purveyor of doom and gloom who lives in a world without hope."
        HauOnF6 = "I talk to spirits that no one else can see."
        HauOnF = [HauOnF1, HauOnF2, HauOnF3, HauOnF4, HauOnF5, HauOnF6]
        player.Flaw = random.choice(HauOnF)
        player.gold = 0
        player.equipment = ["Monster Hunter’s Pack", "One Trinket of special significance"]
        player.skills_dict["ArcaNum"], player.skills_dict["InveNum"], player.skills_dict["ReliNum"], player.skills_dict["SurvNum"] = choicefourskill2(param, player.skills_dict, "ArcaNum", "InveNum", "ReliNum", "SurvNum", dnd_tools.skills["Arcana"], dnd_tools.skills["Investigation"], dnd_tools.skills["Religion"], dnd_tools.skills["Survival"])
        player.languages, player.slang = ExoticLang(param, player.languages, player.slang)
    #Left of here for OOP-ifying and shortening
    if player.background == "Hermit":
        P1 = "I have been isolated for so long that I speak rarely, preferring gestures and also the occasional grunt."
        P2 = "I am utterly serene, even in the face of disaster."
        P3 = "The leader of my community had something wise to say on every topic, and I am eager to share that wisdom."
        P4 = "I feel tremendous empathy for all who suffer."
        P5 = "I am oblivious to etiquette and social expectations."
        P6 = "I connect everything that happens to me to a grand, cosmic plan."
        P7 = "I often get lost in my own thoughts and contemplation, becoming oblivious to my surroundings."
        P8 = "I am working on a grand philosophical theory and love sharing my ideas."
        PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
        player.Trait = random.choice(PTR)
        I1 = "Greater Good.- My gifts are meant to be shared with all, not used for my own benefit. "
        I2 = "Logic - Emotions must not cloud our sense of what is right and true, or our logical thinking. "
        I3 = "Free Thinking - Inquiry and curiosity are the pillars of progress. "
        I4 = "Power - Solitude and contemplation are paths toward mystical or magical power."
        I5 = "Live and Let Live - Meddling in the affairs of others only causes trouble."
        I6 = "Self-Knowledge-  If you know yourself, there is nothing left to know."
        IDE = [I1, I2, I3, I4, I5, I6]
        player.Ideal = random.choice(IDE)
        B1 = "Nothing is more important than the other members of my hermitage, order, or association."
        B2 = "I entered seclusion to hide from the ones who might still be hunting me. I must someday confront them."
        B3 = "I am still seeking the enlightenment I pursued in my seclusion, and it still eludes me."
        B4 = "I entered seclusion because I loved someone I could not have."
        B5 = "Should my discovery come to light, it could bring ruin to the world."
        B6 = "My isolation gave me great insight into a great evil that only I can destroy."
        BND = [B1, B2, B3, B4, B5, B6]
        player.Bond = random.choice(BND)
        F1 = "Now that I've returned to the world, I enjoy its delights a little too much"
        F2 = "I harbor dark, bloodthirsty thoughts that my isolation and meditation failed to quell."
        F3 = "I am dogmatic in my thoughts and philosophy."
        F4 = "I let my need to win arguments overshadow friendships and harmony."
        F5 = "I would risk too much to uncover a lost bit of knowledge."
        F6 = "I like keeping secrets and will not share them with anyone."
        FLA = [F1, F2, F3, F4, F5, F6]
        player.Flaw = random.choice(FLA)
        player.gold = 5
        player.equipment = ["A scroll case stuffed full of notes from your studies or prayers", "A winter blanket", "A set of Common Clothes", "An Herbalism Kit"]
        player.skills_dict["MediNum"] += 1
        player.skills_dict["ReliNum"] += 1
        player.proficiencies.append(dnd_tools.kits["HerbKit"]["Name"])
        player.languages, player.slang = languagegen(param, player.languages, player.slang)   
    if player.background == "House Agent":
        HoAgPT1 = "I'm always looking to improve efficiency."
        HoAgPT2 = "I love to share trivia about my house's business."
        HoAgPT3 = "I never forget an insult against me or my house."
        HoAgPT4 = "I'm enthusiastic about everything my house does."
        HoAgPT5 = "I represent my house and take pride in my looks."
        HoAgPT6 = "I'm critical of monarchies and limits on the houses."
        HoAgPT = [HoAgPT1, HoAgPT2, HoAgPT3, HoAgPT4, HoAgPT5, HoAgPT6]
        player.Trait = random.choice(HoAgPT)
        HoAgId1 = "Common Good. My house serves a vital function, and its prosperity will help everyone. (Good)"
        HoAgId2 = "Tradition. I uphold traditions of my house and bring honor to my family. (Lawful)"
        HoAgId3 = "Innovation. Abandon old traditions and find better ways to do things. (Chaotic)"
        HoAgId4 = "Power. I want to ensure the prosperity of my house and wield its power myself. (Evil)"
        HoAgId5 = "Discovery. I want to learn all I can, both for my house and for my own curiosity. (Any)"
        HoAgId6 = "Comfort. I want to ensure that me and mine enjoy the best things in life. (Any)"
        HoAgId = [HoAgId1, HoAgId2, HoAgId3, HoAgId4, HoAgId5, HoAgId6]
        player.Ideal = random.choice(HoAgId)
        HoAgB1 = "My house is my family. I would do anything for it."
        HoAgB2 = "I love someone from another house, but the relationship is forbidden."
        HoAgB3 = "Someone I love was killed by a rival faction within my house, and I will have revenge."
        HoAgB4 = "I don't care about the house as a whole, but I would do anything for my old mentor."
        HoAgB5 = "My house must evolve, and I ' ll lead the evolution."
        HoAgB6 = "I'm determined to impress the leaders of my house, and to become a leader myself."
        HoAgB = [HoAgB1, HoAgB2, HoAgB3, HoAgB4, HoAgB5, HoAgB6]
        player.Bond = random.choice(HoAgB)
        HoAgF1 = "I'm fixated on following official protocols."
        HoAgF2 = "I'm obsessed with conspiracy theories and worried about secret societies and hidden demons."
        HoAgF3 = "My house and bloodline make me the best!"
        HoAgF4 = "My secret could get me expelled from my house."
        HoAgF5 = "My religious beliefs aren't widespread in my house."
        HoAgF6 = "I'm working for a hidden faction in my house that gives me secret assignments."
        HoAgF = [HoAgF1, HoAgF2, HoAgF3, HoAgF4, HoAgF5, HoAgF6]
        player.Flaw = random.choice(HoAgF)
        player.gold = 20  
        player.equipment = ["A set of Fine Clothes", "House Signet Ring", "Identification papers"] 
        player.skills_dict["InveNum"] += 1
        player.skills_dict["PersNum"] += 1   
    if player.background == "Investigator":
        InvPT1 = "I had an encounter that I believe gives me a special affinity with a supernatural creature or event."
        InvPT2 = "A signature piece of clothing or distinct weapon serves as an emblem of who I am."
        InvPT3 = "I never accept that I’m out of my depth."
        InvPT4 = "I must know the answer to every secret. No door remains unopened in my presence."
        InvPT5 = "I let people underestimate me, revealing my full competency only to those close to me."
        InvPT6 = "I compulsively seek to collect trophies of my travels and victories."
        InvPT7 = "It doesn’t matter if the whole world’s against me. I’ll always do what I think is right."
        InvPT8 = "I have morbid interests and a macabre aesthetic."
        InvPT9 = "I have a personal ritual, mantra, or relaxation method I use to deal with stress."
        InvPT10 = "Nothing is more important than life, and I never leave anyone in danger."
        InvPT11 = "I’m quick to jump to extreme solutions. Why risk a lesser option not working?"
        InvPT12 = "I’m easily startled, but I’m not a coward."
        InvPT = [InvPT1, InvPT2, InvPT3, InvPT4, InvPT5, InvPT6, InvPT7, InvPT8, InvPT9, InvPT10, InvPT11, InvPT12]
        player.Trait = random.choice(InvPT)
        InvId1 = "Adrenaline. I’ve experienced such strangeness that now I feel alive only in extreme situations."
        InvId2 = "Balance. I strive to counter the deeds of someone for whom I feel responsible."
        InvId3 = "Bound. I’ve wronged someone and must work their will to avoid their curse."
        InvId4 = "Escape. I believe there is something beyond the world I know, and I need to find it."
        InvId5 = "Legacy. I must do something great so that I’m remembered, and my time is running out."
        InvId6 = "Misdirection. I work vigorously to keep others from realizing my flaws or misdeeds."
        InvId7 = "Obsession. I’ve lived this way for so long that I can’t imagine another way."
        InvId8 = "Obligation. I owe it to my people, faith, family, or teacher to continue a vaunted legacy."
        InvId9 = "Promise. My life is no longer my own. I must fulfill the dream of someone who’s gone."
        InvId10 = "Revelation. I need to know what lies beyond the mysteries of death, the world, or the Mists."
        InvId11 = "Sanctuary. I know the forces at work in the world and strive to create islands apart from them."
        InvId12 = "Truth. I care about the truth above all else, even if it doesn’t benefit anyone."
        InvId = [InvId1, InvId2, InvId3, InvId4, InvId5, InvId6, InvId7, InvId8, InvId9, InvId10, InvId11, InvId12]
        player.Ideal = random.choice(InvId)
        InvB1 = "I desperately need to get back to someone or someplace, but I lost them in the Mists."
        InvB2 = "Everything I do is in the service of a powerful master, one I must keep a secret from everyone."
        InvB3 = "I owe much to my vanished mentor. I seek to continue their work even as I search to nd them."
        InvB4 = "I’ve seen great darkness, and I’m committed to being a light against it—the light of all lights."
        InvB5 = "Someone I love has become a monster, murderer, or other threat. It’s up to me to redeem them."
        InvB6 = "The world has been convinced of a terrible lie. It’s up to me to reveal the truth."
        InvB7 = "I deeply miss someone and am quick to adopt people who remind me of them."
        InvB8 = "A great evil dwells within me. I will fight against it and the world’s other evils for as long as I can."
        InvB9 = "I’m desperately seeking a cure to an affliction or a curse, either for someone close to me for myself."
        InvB10 = "Spirits are drawn to me. I do all I can to help them nd peace."
        InvB11 = "I use my cunning mind to solve mysteries and nd justice for those who’ve been wronged."
        InvB12 = "I lost someone I care about, but I still see them in guilty visions, recurring dreams, or as a spirit."
        InvB = [InvB1, InvB2, InvB3, InvB4, InvB5, InvB6, InvB7, InvB8, InvB9, InvB10, InvB11, InvB12]
        player.Bond = random.choice(InvB)
        InvFl1 = "I believe doom follows me and that anyone who gets close to me will face a tragic end."
        InvFl2 = "I’m convinced something is after me, appearing in mirrors, dreams, and places where no one could."
        InvFl3 = "I’m especially superstitious and live life seeking to avoid bad luck, wicked spirits, or the Mists."
        InvFl4 = "I’ve done unspeakable evil and will do anything to prevent others from finding out."
        InvFl5 = "I am exceptionally credulous and believe any story or legend immediately."
        InvFl6 = "I’m a skeptic and don’t believe in the power of rituals, religion, superstition, or spirits."
        InvFl7 = "I know my future is written and that anything I do will lead to a prophesied end."
        InvFl8 = "I need to nd the best in everyone and everything, even when that means denying obvious malice."
        InvFl9 = "I’ve seen the evil of a type of place—like forests, cities, or graveyards—and resist going there."
        InvFl10 = "I’m exceptionally cautious, planning laboriously and devising countless contingencies."
        InvFl11 = "I have a reputation for defeating a great evil, but that’s a lie and the wicked force knows."
        InvFl12 = "I know the ends always justify the means and am quick to make sacrifices to attain my goals"
        InvFl = [InvFl1, InvFl2, InvFl3, InvFl4, InvFl5, InvFl6, InvFl7, InvFl8, InvFl9, InvFl10, InvFl11, InvFl12]
        player.Flaw = random.choice(InvFl)        
        player.gold = 10   
        player.equipment = ["A uniform in the style of your unit and indicative of your rank", "A horn with which to summon help", "A set of Manacles"]
        player.skills_dict["InveNum"] += 1
        player.skills_dict["InsiNum"] += 1
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)     
    if player.background == "Izzet Engineer":
        IEPT1 = "I have a hard time staying focused on… oh, and my brain tends to jump from one… did I mention focus?"
        IEPT2 = "I get really excited about my ideas and I can't wait to talk about them and start putting them into practice and tinkering with them and I want to tell you about how exciting it all is!"
        IEPT3 = "It's not magic — or anything, really — if you do it only halfway. Whatever I do, I give it all I've got."
        IEPT4 = "I do what my gut tells me."
        IEPT5 = "Life's an experiment, and I can't wait to see what happens."
        IEPT6 = "I pepper my speech with the incomprehensible jargon of my trade, like mizzium droplets inserted into a weird.field suspension."
        IEPT7 = "Great ideas are fine, but great results are what counts."
        IEPT8 = "If you can guess what I'm about to do, that means I've run out of imagination."
        IEPT = [IEPT1, IEPT2, IEPT3, IEPT4, IEPT5, IEPT6, IEPT7, IEPT8]
        player.Trait = random.choice(IEPT)
        IzEnI1 = "Guild: My guild is all that really matters. (Any)"
        IzEnI2 = "Creativity: Half the world's troubles come from stodgy thinking, stuck in the past. We need innovative solutions. (Chaotic)"
        IzEnI3 = "Discovery: Every experiment has the potential to reveal more secrets of the multiverse. (Any)"
        IzEnI4 = "Science: A rigorous application of logical principles and protocols will lead us toward progress more surely than any belief system. (Lawful)"
        IzEnI5 = "Fun: I love my job! Despite the dangerous working conditions, there's nothing I'd rather do. (Chaotic)"
        IzEnI6 = "Power: Someday I'll find or create the magic that will make me the most powerful being in Ravnica. (Evil)"
        IzEnI = [IzEnI1, IzEnI2, IzEnI3, IzEnI4, IzEnI5, IzEnI6]
        player.Ideal = random.choice(IzEnI)
        IzEnB1 = "I have dedicated my life to finding a solution to a scientific problem."
        IzEnB2 = "I'll never forget the laboratory where I learned my skills, or the other attendants who learned alongside me."
        IzEnB3 = "I'm convinced it was sabotage that destroyed my first laboratory and killed many of my friends, and I seek revenge against whoever did it."
        IzEnB4 = "I have the schematics for an invention that I hope to build one day, once I have the necessary resources."
        IzEnB5 = "A fellow student and I are racing to solve the same scientific puzzle."
        IzEnB6 = "I would do anything the guildmaster told me to do."
        IzEnB = [IzEnB1, IzEnB2, IzEnB3, IzEnB4, IzEnB5, IzEnB6]
        player.Bond = random.choice(IzEnB)
        IzEnF1 = "If there's a plan, I'll probably forget it. If I don't forget it, I'll probably ignore it."
        IzEnF2 = "I get bored easily, and if nothing is happening I'll make something happen."
        IzEnF3 = "Nothing is ever simple, and if it seems simple, I'll find a way to make it complicated."
        IzEnF4 = "I tend to ignore sleep for days when I'm conducting research, often at the expense of my own health and safety."
        IzEnF5 = "I'm convinced there's not a soul in Ravnica, except maybe the great Niv-Mizzet, who can match my boundless intellect."
        IzEnF6 = "I'm incapable of admitting a flaw in my logic."
        IzEnF = [IzEnF1, IzEnF2, IzEnF3, IzEnF4, IzEnF5, IzEnF6]
        player.Flaw = random.choice(IzEnF)
        player.gold = 5   
        player.equipment = ["An Izzet insignia", "One set of Artisan's Tools", "The charred and twisted remains of a failed experiment", "A Hammer", "A Block and Tackle", "A set of Common Clothes"]
        player.skills_dict["ArcaNum"] += 1
        player.skills_dict["InveNum"] += 1
        player.proficiencies = artisantools(param, player.proficiencies)
        langlist = ["Drac", "Gobl", "Veda"]
        player.languages, player.slang = choicethreelang(param, player.languages, player.slang, langlist)     
    if player.background == "Knight of Solamnia":
        player.gold = 10
        player.equipment = ["An insignia of rank", "A deck of cards", "A set of common clothes"]
        player.skills_dict["AthlNum"] += 1
        player.skills_dict["SurvNum"] += 1
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.Trait = ""
        player.Ideal = ""
        player.Bond = ""
        player.Flaw = "" 
    if player.background == "Lorehold Student":   
        player.gold = 15
        player.equipment = ["A bottle of Black Ink", "An Ink Pen", "A Hammer", "A Hooded Lantern", "A Tinderbox", "A tome of history", "A school uniform"]
        player.skills_dict["HistNum"] += 1
        player.skills_dict["ReliNum"] += 1
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.Trait = ""
        player.Ideal = ""
        player.Bond = ""
        player.Flaw = ""          
    if player.background == "Lyceum Scholar":
        LySchPT1 = "I can't believe I'm here! At the Alabaster Lyceum. Oh, gods, I've dreamed of this my whole life, and now I'm here!"
        LySchPT2 = "I can't believe I squandered all the opportunities I had at school. I was supposed to be learning good stuff, but I wasted it all daydreaming about fighting monsters."
        LySchPT3 = "Every night at school, I'd knock back a couple of meads and read with my pals! Just a bunch of nerds having fun, and I loved it."
        LySchPT4 = "Everyone at school was such a stick in the mud. Dressing the same, listening to the same bards…ugh, it's sad. Just be yourself."
        LySchPT5 = "I'm happiest when I've got my little party with me. At school, it was like we were a squad of heroes, slaying projects like monsters."
        LySchPT6 = "I'd really rather you didn't bother me. Can't you see I'm studying here?"
        LySchPT7 = "I don't care. I just don't care about it all. The dates I had to memorize, the formulae I learned…I just want to run away and live!"
        LySchPT8 = "I'm just…tired. All the time. Oh, adventuring, sure, that's fine, as long as I can find time to…nap…goodnight."
        LySchPT = [LySchPT1, LySchPT2, LySchPT3, LySchPT4, LySchPT5, LySchPT6, LySchPT7, LySchPT8]
        player.Trait = random.choice(LySchPT)
        LySchId1 = "Preparedness. I can't go out into the world unless I know what I'm up against. Study first, act later. (Neutral)"
        LySchId2 = "Stardom. Having a team is good and all, but you can't win a game of ball without the star charger, and you know that's me. (Evil)"
        LySchId3 = "Individuality. The world keeps us down by trying to put us all into little boxes. I'm tired of living in my box, and I don't care what you think about it. (Chaotic)"
        LySchId4 = "Purpose. I study because there are things I need to know. I'll find my place in the world, and I'll make the world better. (Good)"
        LySchId5 = "Code of Conduct. The student code is there to benefit all students, you know. It's the same for laws! (Lawful)"
        LySchId6 = "Recreation. All this studying crap wasn't worth anything if you weren't partying when you were done. Meet me down at the tavern, okay? (Chaotic)"
        LySchId = [LySchId1, LySchId2, LySchId3, LySchId4, LySchId5, LySchId6]
        player.Ideal = random.choice(LySchId)
        LySchB1 = "I came to the Lyceum with no one, but I fell in love with the city of Emon. I've finally found a place that feels like home!"
        LySchB2 = "Most of my professors drove me to frustration, but there's one who was kind and wise. I know they'll always have my back."
        LySchB3 = "My family saved every copper piece to give me the opportunities I have now. I can't let them down."
        LySchB4 = "I came to the Lyceum with a childhood friend, but we've long been drifting apart."
        LySchB5 = "Discovery is the only thing that matters to me. The topic doesn't matter. Books keep me company on my loneliest days."
        LySchB6 = "The Lyceum is my life. I'd give up anything—everything—to protect it from harm."
        LySchB = [LySchB1, LySchB2, LySchB3, LySchB4, LySchB5, LySchB6]
        player.Bond = random.choice(LySchB)
        LySchF1 = "The Lyceum taught me to never want to leave my room. The campus was so huge, and the crowds were so horrible."
        LySchF2 = "You think you're so great just because you've got muscles, and endurance, and…shut up! Read a book sometime!"
        LySchF3 = "Huh? What? Sorry, I was thinking about a test I need to retake when I get back to school…."
        LySchF4 = "I spent too much time studying. Now I don't have any friends."
        LySchF5 = "If you don't match my aesthetic, I'm not interested in you. We can work together, but we won't be friends. Got it?"
        LySchF6 = "I'm always striving for perfection. I got top of my class, sure, but only with a 98 average. And that's. Not. Perfect."
        LySchF = [LySchF1, LySchF2, LySchF3, LySchF4, LySchF5, LySchF6]
        player.Flaw = random.choice(LySchF)
        player.gold = 10
        player.equipment = ["A set of fine clothes", "A student uniform", "A writing kit (small pouch with a quill, ink, folded parchment and a penknife)"]
        player.skills_dict["ArcaNum"], player.skills_dict["HistNum"], player.skills_dict["PersNum"] = choicethreeskill2(param, player.skills_dict, "ArcaNum", "HistNum", "PersNum", dnd_tools.skills["Arcana"], dnd_tools.skills["History"], dnd_tools.skills["Persuasion"])
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)        
    if player.background == "Mage of High Sorcery":
        player.gold = 10
        player.equipment = ["A bottle of colored ink"," An ink pen", "A set of common clothes"]
        player.skills_dict["ArcaNum"] += 1
        player.skills_dict["HistNum"] += 1
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.Trait = ""
        player.Ideal = ""
        player.Bond = ""
        player.Flaw = ""
    if player.background == "Marine":   
        MarPT1 = "I speak rarely but mean every word I say."
        MarPT2 = "I laugh loudly and see the humor in stressful situations."
        MarPT3 = "I prefer to solve problems without violence, but I finish fights decisively."
        MarPT4 = "I enjoy being out in nature; poor weather never sours my mood."
        MarPT5 = "I am dependable."
        MarPT6 = "I am always working on some project or other."
        MarPT7 = "I become cantankerous and quiet in the rain."
        MarPT8 = "When the sea is within my sight, my mood is jovial and optimistic."
        MarPT = [MarPT1, MarPT2, MarPT3, MarPT4, MarPT5, MarPT6, MarPT7, MarPT8]
        player.Trait = random.choice(MarPT)
        MarId1 = "Teamwork. Success depends on cooperation and communication. (Good)"
        MarId2 = "Code. The marines' code provides a solution for every problem, and following it is imperative. (Lawful)"
        MarId3 = "Embracing. Life is messy. Throwing yourself into the worst of it is necessary to get the job done. (Chaotic)"
        MarId4 = "Might. The strong train so that they might rule those who are weak. (Evil)"
        MarId5 = "Bravery. To act when others quake in fear- this is the essence of the warrior. (Any)"
        MarId6 = "Perseverance. No injury or obstacle can turn me from my goal. (Any)"
        MarId = [MarId1, MarId2, MarId3, MarId4, MarId5, MarId6]
        player.Ideal = random.choice(MarId)
        MarB1 = "I face danger and evil to offset an unredeemable act in my past."
        MarB2 = "I. Will. Finish. The. job."
        MarB3 = "I must set an example of hope for those who have given up."
        MarB4 = "I'm searching for a fellow marine captured by an elusive enemy."
        MarB5 = "Fear leads to tyranny, and both must be eradicated."
        MarB6 = "My commander betrayed my unit, and I will have revenge."
        MarB = [MarB1, MarB2, MarB3, MarB4, MarB5, MarB6]
        player.Bond = random.choice(MarB)
        MarF1 = "I grow combative and unpredictable when I drink."
        MarF2 = "I find civilian life difficult and struggle to say the right thing in social situations."
        MarF3 = "My intensity can drive others away."
        MarF4 = "I hold grudges and have difficulty forgiving others."
        MarF5 = "I become irrational when innocent people are hurt."
        MarF6 = "I sometimes stay up all night listening to the ghosts of my fallen enemies."
        MarF = [MarF1, MarF2, MarF3, MarF4, MarF5, MarF6]
        player.Flaw = random.choice(MarF)
        player.gold = 10
        player.equipment = ["A Dagger that belonged to a fallen comrade", "A folded Rag emblazoned with the symbol of your ship or company" , "A set of Traveler's Clothes"]
        player.skills_dict["AthlNum"] += 1
        player.skills_dict["SurvNum"] += 1
        player.proficiencies.append(dnd_tools.vehicles["VehLand"])
        player.proficiencies.append(dnd_tools.vehicles["VehSea"])                                     
    if (player.background == "Knight") or (player.background == "Noble") or (player.background == "Waterdhavian Noble"):         
        P1 = "My eloquent flattery makes everyone I talk to feel like the most wonderful and important person in the world."
        P2 = "The common folk love me for my kindness and generosity."
        P3 = "No one could doubt by looking at my regal bearing that I am a cut above the unwashed masses."
        P4 = "I take great pains to always look my best and follow the latest fashions."
        P5 = "I do not like to get my hands dirty, and I will not be caught dead in unsuitable accommodations."
        P6 = "Despite my noble birth, I do not place myself above other folk. We all have the same blood."
        P7 = "My favor, once lost, is lost forever."
        P8 = "If you do me an injury, I will crush you, ruin your name, and salt your fields."
        PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
        player.Trait = random.choice(PTR)
        I1 = "Respect - Respect is due to me because of my position, but all people regardless of station deserve to be treated with dignity."
        I2 = "Responsibility - It is my duty to respect the authority of those above me, just as those below me must respect mine."
        I3 = "Independence - I must prove that I can handle myself without the coddling of my family. "
        I4 = "Power - If I can attain more power, no one will tell me what to do. "
        I5 = "Family - Blood runs thicker than water. "
        I6 = "Noble Obligation -  It is my duty to protect and care for the people beneath me. "
        IDE = [I1, I2, I3, I4, I5, I6]
        player.Ideal = random.choice(IDE)
        B1 = "I will face any challenge to win the approval of my family."
        B2 = "My house’s alliance with another noble family must be sustained at all costs."
        B3 = "Nothing is more important than the other members of my family."
        B4 = "I am in love with the heir of a family that my family despises."
        B5 = "My loyalty to my sovereign is unwavering."
        B6 = "The common folk must see me as a hero of the people."
        BND = [B1, B2, B3, B4, B5, B6]
        player.Bond = random.choice(BND)
        F1 = "I secretly believe that everyone is beneath me."
        F2 = "I hide a truly scandalous secret that could ruin my family forever."
        F3 = "I too often hear veiled insults and threats in every word addressed to me, and I am quick to anger."
        F4 = "I have an insatiable desire for carnal pleasures."
        F5 = "In fact, the world does revolve around me."
        F6 = "By my words and actions, I often bring shame to my family."
        FLA = [F1, F2, F3, F4, F5, F6]
        player.Flaw = random.choice(FLA)
        if player.background == "Knight":
            player.skills_dict["HistNum"] += 1
            player.skills_dict["PersNum"] += 1
            player.proficiencies = gamingsets(param, player.proficiencies)
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.gold = 25
            player.equipment = ["A set of Fine Clothes", "A Signet Ring", "A scroll of pedigree"]
        if player.background == "Noble":
            player.skills_dict["HistNum"] += 1
            player.skills_dict["PersNum"] += 1
            player.proficiencies = gamingsets(param, player.proficiencies)
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.gold = 25
            player.equipment = ["A set of Fine Clothes", "A Signet Ring", "A scroll of pedigree"]
        if player.background == "Waterdhavian Noble":
            player.skills_dict["HistNum"] += 1
            player.skills_dict["PersNum"] += 1
            player.proficiencies = gamingsetsmusicalinstr(param, player.proficiencies)
            player.languages, player.slang = languagegen(param, player.languages, player.slang)   
            player.gold = 20
            player.equipment = ["A set of Fine Clothes", "A Signet Ring", "A scroll of pedigree", "A skin of fine zzar or wine"]                  
    if player.background == "Orzhov Representative":
        ORPT1 = "I am always willing to act in accordance with the financial incentive offered."
        ORPT2 = "Debts are never meant to be forgiven."
        ORPT3 = "I am accustomed to enjoying the finest pleasures money can buy."
        ORPT4 = "No one could doubt that I am a cut above the masses of pitiful peasants that infest the city."
        ORPT5 = "I can't stand to spend a zib more than necessary to purchase what I need."
        ORPT6 = "I hate it when people try to make light of a serious situation."
        ORPT7 = "I want to make sure everyone is aware of how wealthy, powerful, and important I am."
        ORPT8 = "I can't think of anything to look forward to."
        ORPT = [ORPT1, ORPT2, ORPT3, ORPT4, ORPT5, ORPT6, ORPT7, ORPT8]
        player.Trait = random.choice(ORPT)
        OrzRepI1 = "Guild: My guild is all that really matters. (Any)"
        OrzRepI2 = "Wealth: I will do whatever it takes to become as rich as the oligarchs. (Evil)"
        OrzRepI3 = "Power: One day, I will be the one giving orders. (Evil)"
        OrzRepI4 = "Prestige: I want to be admired, respected, feared, or even hated for my position and wealth. (Evil)"
        OrzRepI5 = "Stability: The economy functions best when chaos is kept under control and everyone knows their place. (Lawful)"
        OrzRepI6 = "Eternity: I want to live forever — in the flesh as long as possible, and as a spirit afterward. (Any)"
        OrzRepI = [OrzRepI1, OrzRepI2, OrzRepI3, OrzRepI4, OrzRepI5, OrzRepI6]
        player.Ideal = random.choice(OrzRepI)
        OrzRepB1 = "The unbearable weight of my debt has driven me to desperation."
        OrzRepB2 = "I'm duty-bound to obey the dictates of an ancestor on the Ghost Council."
        OrzRepB3 = "I value my worldly goods more highly than my mortal life."
        OrzRepB4 = "An oligarch publicly humiliated me, and I will exact revenge on that whole family."
        OrzRepB5 = "My faith in the Obzedat never wavers."
        OrzRepB6 = "I want to prove myself more worthy than an older sibling and thereby ensure that I inherit a greater share of my parents' wealth."
        OrzRepB = [OrzRepB1, OrzRepB2, OrzRepB3, OrzRepB4, OrzRepB5, OrzRepB6]
        player.Bond = random.choice(OrzRepB)
        OrzRepF1 = "I hold a scandalous secret that could ruin my family forever — but could also earn me the favor of the Ghost Council."
        OrzRepF2 = "I'm convinced that everyone I know is plotting against me."
        OrzRepF3 = "I'll brave any risk if the monetary reward is great enough."
        OrzRepF4 = "I am convinced that I am far more important than anyone else is willing to acknowledge."
        OrzRepF5 = "I have little respect for anyone who isn't wealthy."
        OrzRepF6 = "I'll take any opportunity to steal from wealthier people, even for worthless trinkets."
        OrzRepF = [OrzRepF1, OrzRepF2, OrzRepF3, OrzRepF4, OrzRepF5, OrzRepF6]
        player.Flaw = random.choice(OrzRepF)
        player.gold = 100    
        player.equipment = ["An Orzhov insignia", "A foot-long chain made of ten gold coins", "Vestments", "A set of Fine Clothes"]
        player.skills_dict["IntiNum"] += 1
        player.skills_dict["ReliNum"] += 1
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)       
    if (player.background == "Outlander") or (player.background == "Uthgardt Tribe Member"):
        P1 = "I am driven by a wanderlust that led me away from home."
        P2 = "I watch over my friends as if they were a litter of newborn pups."
        P3 = "I once ran twenty-five miles without stopping to warn  my clan of an approaching orc horde. I would do it again if I had to."
        P4 = "I have a lesson for every situation, drawn from observing nature."
        P5 = "I place no stock in wealthy or well-mannered folk. Money and manners will not save you from a hungry owlbear"
        P6 = "I am always picking things up, absently fiddling with them, and sometimes accidentally breaking them."
        P7 = "I feel far more comfortable around animals than people."
        P8 = "I was, in fact, raised by wolves."
        PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
        player.Trait = random.choice(PTR)
        I1 = "Change - Life is like the seasons, in constant change, and we must change with it."
        I2 = "Greater Good - It is each person’s responsibility to make the most happiness for the whole tribe."
        I3 = "Honor - If I dishonor myself, I dishonor my whole clan."
        I4 = "Might -  The strongest are meant to rule."
        I5 = "Nature - The natural world is more important than all the constructs of civilization."
        I6 = "Glory - I must earn glory in battle, for myself and my clan."
        IDE = [I1, I2, I3, I4, I5, I6]
        player.Ideal = random.choice(IDE)
        B1 = "My family, clan, or tribe is the most important thing in my life, even when they are far from me."
        B2 = "An injury to the unspoiled wilderness of my home is an injury to me."
        B3 = "I will bring terrible wrath down on the evildoers who destroyed my homeland."
        B4 = "I am the last of my tribe, and it is up to me to ensure their names enter legend."
        B5 = "I suffer awful visions of a coming disaster and will do anything to prevent it."
        B6 = "It is my duty to provide children to sustain my tribe."
        BND = [B1, B2, B3, B4, B5, B6]
        player.Bond = random.choice(BND)
        F1 = "I am too enamored of ale, wine, and other intoxicants."
        F2 = "There is no room for caution in a life lived to the fullest."
        F3 = "I remember every insult I’ve received and nurse a silent resentment toward anyone who hass ever wronged me."
        F4 = "I am slow to trust members of other races, tribes, and societies."
        F5 = "Violence is my answer to almost any challenge."
        F6 = "Do not expect me to save those who can’t save themselves. It is nature’s way that the strong thrive and the weak perish."
        FLA = [F1, F2, F3, F4, F5, F6]
        player.Flaw = random.choice(FLA)
        player.gold = 10
        if player.background == "Outlander":
            player.skills_dict["AthlNum"] += 1
            player.skills_dict["SurvNum"] += 1
            player.proficiencies = musicalinstr(param, player.proficiencies)
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.equipment = ["A staff", "A Hunting Trap", "A trophy from an animal you killed", "A set of Traveler's Clothes"]
        if player.background == "Uthgardt Tribe Member":
            player.skills_dict["AthlNum"] += 1
            player.skills_dict["SurvNum"] += 1
            player.proficiencies = artisantoolsmusicalinstr(param, player.proficiencies)
            player.languages, player.slang = languagegen(param, player.languages, player.slang)     
            player.equipment = ["A Hunting Trap", "A totemic token or set of tattoos marking your loyalty to Uthgar and your tribal totem", "A set of Traveler's Clothes"]
    if player.background == "Plaintiff":
        PlaintiffPT1 = "I can't believe I have a chance to join Acquisitions Incorporated! The fun I'm going to have!"
        PlaintiffPT2 = "I've been wronged my entire life, and the world owes me."
        PlaintiffPT3 = "I have always tried to make the best of a bad situation."
        PlaintiffPT4 = "The law doesn't protect the honest and the hard working. I'm going to do whatever needs to be done to make things right."
        PlaintiffPT5 = "I'm always in the wrong place at the wrong time."
        PlaintiffPT6 = "My superiors are smarter and wiser than I am. I do what I'm told."
        PlaintiffPT7 = "Never pass up the opportunity to make an easy bit of coin. That's my motto."
        PlaintiffPT8 = "I'm beginning to feel like the gods are not on my side."
        PlaintiffPT = [PlaintiffPT1, PlaintiffPT2, PlaintiffPT3, PlaintiffPT4, PlaintiffPT5, PlaintiffPT6, PlaintiffPT7, PlaintiffPT8]
        player.Trait = random.choice(PlaintiffPT)
        PlaintiffId1 = "Justice. Those who break the law need to answer for their crimes. (Lawful)"
        PlaintiffId2 = "Freedom. People must have the freedom to do what they want and pursue their dreams. (Chaotic)"
        PlaintiffId3 = "Greed. Everyone I see is getting theirs, so I'm surely going to get mine. (Evil)"
        PlaintiffId4 = "Chaos. You're out of order! And you're out of order! This whole realm is out of order! (Chaotic)"
        PlaintiffId5 = "Humility. I'm just a small part of a larger whole. So is everyone else. (Neutral)"
        PlaintiffId6 = "Responsibility. We all have our roles to play. I'll hold up my end of the bargain. (Any)"
        PlaintiffId = [PlaintiffId1, PlaintiffId2, PlaintiffId3, PlaintiffId4, PlaintiffId5, PlaintiffId6]
        player.Ideal = random.choice(PlaintiffId) 
        PlaintiffB1 = "Others hurt in the same accident that hurt me are my new family. I'll make sure they're taken care of."
        PlaintiffB2 = "The rulers of this place were kind to me, and they have my lifelong devotion."
        PlaintiffB3 = "My parents worry about me, but I'll make them proud."
        PlaintiffB4 = "The only bond that matters is the one holding my money pouch to my belt."
        PlaintiffB5 = "The other new hires at Acquisitions Incorporated are my allies. We have each other's backs."
        PlaintiffB6 = "My legal counsel is my best friend. I owe all my forthcoming opportunities to their hard work."
        PlaintiffB = [PlaintiffB1, PlaintiffB2, PlaintiffB3, PlaintiffB4, PlaintiffB5, PlaintiffB6]
        player.Bond = random.choice(PlaintiffB)
        PlaintiffF1 = "The person who gains the most reward for the least effort wins."
        PlaintiffF2 = "Three magic beans for just one cow? What a deal!"
        PlaintiffF3 = "I have only one vice, but it controls my life."
        PlaintiffF4 = "Sleep is for the weak. We need to keep training more if we're going to be ready for the challenges ahead."
        PlaintiffF5 = "Until my songs are sung in every tavern in this realm, I won't be satisfied."
        PlaintiffF6 = "If people find me unpleasant, that's their problem."
        PlaintiffF = [PlaintiffF1, PlaintiffF2, PlaintiffF3, PlaintiffF4, PlaintiffF5, PlaintiffF6]
        player.Flaw = random.choice(PlaintiffF)
        player.gold = 20
        player.equipment = ["One set of Artisan's Tools", "Fine Clothes"]
        player.skills_dict["MediNum"] += 1
        player.skills_dict["PersNum"] += 1
        player.proficiencies = artisantools(param, player.proficiencies)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)       
    if player.background == "Planar Philosopher": 
        player.gold = 10
        player.equipment = ["A portal key (such as a bag of golden tea leaves or the tooth of a planar beast)", "A manifesto of your guiding philosophy", "A set of common clothes in your faction's style"]
        player.skills_dict["ArcaNum"] += 1
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.Trait = ""
        player.Ideal = ""
        player.Bond = ""
        player.Flaw = ""               
    if player.background == "Prismari Student": 
        player.gold = 10
        player.equipment = ["A bottle of Black Ink", "An Ink Pen", "A set of Artisan's Tools or a Musical instrument (one of your choice)", "A school uniform"]
        player.skills_dict["AcroNum"] += 1
        player.skills_dict["PerfNum"] += 1
        player.proficiencies = artisantoolsmusicalinstr(param, player.proficiencies)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.Trait = ""
        player.Ideal = ""
        player.Bond = ""
        player.Flaw = ""            
    if player.background == "Quandrix Student":  
        player.gold = 15
        player.equipment = ["A bottle of Black Ink", "An Ink Pen", "An Abacus", "A book of arcane theory", "A school uniform"]
        player.skills_dict["ArcaNum"] += 1
        player.skills_dict["NatuNum"] += 1
        player.proficiencies = artisantools(param, player.proficiencies)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.Trait = ""
        player.Ideal = ""
        player.Bond = ""
        player.Flaw = ""               
    if player.background == "Rakdos Cultist":
        RCPT1 = "I revel in mayhem, the more destructive the better."
        RCPT2 = "When violence breaks out, I lose myself in rage, and it's sometimes hard to stop."
        RCPT3 = "Everything is funny to me, and the most hilarious and bloodiest things leave me cackling with sadistic glee."
        RCPT4 = "I derive genuine pleasure from the pain of others."
        RCPT5 = "I enjoy testing other people's patience."
        RCPT6 = "I can't stand it when things are predictable, so I like to add a little chaos to every situation."
        RCPT7 = "I throw my weight around to make sure I get my way."
        RCPT8 = "I enjoy breaking delicate works of art. And fingers, which are sort of the same."
        RCPT = [RCPT1, RCPT2, RCPT3, RCPT4, RCPT5, RCPT6, RCPT7, RCPT8]
        player.Trait = random.choice(RCPT)
        RakCulI1 = "Guild: My guild is all that really matters. (Any)"
        RakCulI2 = "Hedonism: Death comes for everyone, so take as much pleasure as you can from every moment of life. (Neutral)"
        RakCulI3 = "Creativity: I strive to find more ways to express my art through pain — my own as well as others'. (Chaotic)"
        RakCulI4 = "Freedom: No one tells me what to do. (Chaotic)"
        RakCulI5 = "Equality: I want to see Ravnica re made, with no guilds and no hierarchies. (Chaotic)"
        RakCulI6 = "Spectacle: People are inspired by the greatness they see in art. (Any)"
        RakCulI = [RakCulI1, RakCulI2, RakCulI3, RakCulI4, RakCulI5, RakCulI6]
        player.Ideal = random.choice(RakCulI)
        RakCulB1 = "I have belonged to the same performance troupe for years, and these people mean everything to me."
        RakCulB2 = "A blood witch told me I have a special destiny to fulfill, and I'm trying to figure out what it is."
        RakCulB3 = "I'm secretly hoping that I can change the cult from the inside, using my influence to help rein in the wanton violence."
        RakCulB4 = "I own something that Rakdos once touched (it's seared black at the spot), and I cherish it."
        RakCulB5 = "I want to be better at my chosen form of performance than any other member of my troupe."
        RakCulB6 = "I am devoted to Rakdos and live to impress him."
        RakCulB = [RakCulB1, RakCulB2, RakCulB3, RakCulB4, RakCulB5, RakCulB6]
        player.Bond = random.choice(RakCulB)
        RakCulF1 = "My family is prominent in another guild. I enjoy my wild life, but I don't want to embarrass them."
        RakCulF2 = "I couldn't hide my emotions and opinions even if I wanted to."
        RakCulF3 = "I throw caution to the wind."
        RakCulF4 = "I resent the rich and powerful."
        RakCulF5 = "When I'm angry, I lash out in violence."
        RakCulF6 = "There's no such thing as too much pleasure."
        RakCulF = [RakCulF1, RakCulF2, RakCulF3, RakCulF4, RakCulF5, RakCulF6]
        player.Flaw = random.choice(RakCulF)
        player.gold = 10
        player.skills_dict["AcroNum"] += 1
        player.skills_dict["PerfNum"] += 1
        player.proficiencies = musicalinstr(param, player.proficiencies)
        langs = ["Abys", "Gian"]
        langsavail = []
        for lang in langs:
            if lang in player.slang:
                langsavail.append(lang)
        if param == "Y":
            print("0 - Random")
            for idx, raklang in enumerate(langsavail, 1):
                print(f"{idx} - {raklang}")      
            twolang = int(input("Choose a language to know. "))
            if twolang == 0:
                randlang = random.choice(langsavail)
                full_langavail = dnd_tools.languages[randlang]
                player.languages.append(full_langavail)
            elif 1 <= twolang <= len(langsavail):
                player.languages.append(dnd_tools.languages[twolang - 1])
        if param == "N":
            randlang = random.choice(langsavail)
            full_langavail = dnd_tools.languages[randlang]
            player.languages.append(full_langavail)
        player.equipment = ["A Rakdos insignia", "A Musical Instrument (one of your choice)", "A Costume", "A Hooded Lantern made of wrought iron", "A 10-foot length of Chain with sharply spiked links", "A Tinderbox", "10 Torches", "A set of Common Clothes", "A bottle of sweet, red juice"]                    
    if player.background == "Reformed Cultist":
        RefCuPT1 = "I need a dagger close at hand at all times. Just in case they find me."
        RefCuPT2 = "I can't believe I'm out here fighting monsters. After everything I've been through, why can't I find a normal life?"
        RefCuPT3 = "I need a stiff drink before I do anything stressful these days. I know it's a problem. Just…let me have this."
        RefCuPT4 = "Murder is okay when it's for a good cause! I didn't tear my past out by the roots so I could let evil people cause more harm."
        RefCuPT5 = "My past is filled with stories like you wouldn't believe. Ones that'll really make your skin crawl. Do you want to hear…?"
        RefCuPT6 = "Yeah, I'm crying. I do that. Get over yourself."
        RefCuPT7 = "I know you've told me your name twice already, but that's not good enough. How can I be sure you are who you say you are?"
        RefCuPT8 = "My mind is always racing. I can't…I just need to…you have to give me a second—or else I can't…organize my thoughts."
        RefCuPT = [RefCuPT1, RefCuPT2, RefCuPT3, RefCuPT4, RefCuPT5, RefCuPT6, RefCuPT7, RefCuPT8]
        player.Trait = random.choice(RefCuPT)
        RefCuId1 = "Life. I've spent too long shackled to an evil master. No matter what happened before, I deserve my freedom now. (Chaotic)"
        RefCuId2 = "Redemption. People can change, but redemption must be something they choose for themselves. If they do, it is my duty to help them along that path. (Good)"
        RefCuId3 = "Power. When I abandoned the cult, it wasn't out of some misguided sense of righteousness. That pathetic organization was merely a shackle on my potential. (Evil)"
        RefCuId4 = "Vengeance. The cult has poisoned my life. I will see all its followers suffer. (Any)"
        RefCuId5 = "Hierarchy. The cult was vile, but its strength was in stability and organization. As long as good folk lack unity, evil will always triumph. (Lawful)"
        RefCuId6 = "Reparations. As a cultist, I harmed people whose names I'll never know. I feel obligated to repay my debt by aiding others. (Good)"
        RefCuId = [RefCuId1, RefCuId2, RefCuId3, RefCuId4, RefCuId5, RefCuId6]
        player.Ideal = random.choice(RefCuId)
        RefCuB1 = "My cousin escaped the cult with me. I lost track of them when we fled, but I know they're alive. I can feel it."
        RefCuB2 = "I was saved from the cult by a priest of one of the Prime Deities. If not for that sign of faith, I would surely be lost."
        RefCuB3 = "I was told by the person who saved me that a sage once said: 'Life needs things to live.' I don't know what that means, but I've dedicated my existence to finding out."
        RefCuB4 = "One of my cultist parents had a change of heart when I was a teenager, and we fled together in the dark of night. I didn't want to leave, but I understand now that their courage saved my life."
        RefCuB5 = "I was bested by a warrior when I fumbled a cult-ordered assassination. I don't know why that person took pity on me, but they gave me purpose when I was lost."
        RefCuB6 = "Now that I've saved myself, the only person important to me is my former cult leader—because I've sworn that they'll die by my hand."
        RefCuB = [RefCuB1, RefCuB2, RefCuB3, RefCuB4, RefCuB5, RefCuB6]
        player.Bond = random.choice(RefCuB)
        RefCuF1 = "I'm haunted by what I saw in those ritual chambers. Every time I see blood, I…oh, gods, I can't bear to even think about it."
        RefCuF2 = "I ran from the cult long ago. But deep down, there's a part of me that still thinks they were right about certain things."
        RefCuF3 = "I can't help but feel a rush whenever I see a life snuffed out before me. Just one more kill… just one more."
        RefCuF4 = "Organized religion terrifies me. Betrayer Gods or Prime Deities…it doesn't matter. The sight of the faithful freezes my blood cold."
        RefCuF5 = "Oh, I always tell the truth. Always. I've never had to keep a secret from anyone, so of course I'll be open with you."
        RefCuF6 = "I don't trust easily. If you grew up being lied to about every little thing? The fundamental nature of the world? You wouldn't, either."
        RefCuF = [RefCuF1, RefCuF2, RefCuF3, RefCuF4, RefCuF5, RefCuF6]
        player.Flaw = random.choice(RefCuF)
        player.gold = 15
        player.equipment = ["Vestments and a holy symbol of your previous cult", "A set of common clothes"]
        player.skills_dict["DeceNum"] += 1
        player.skills_dict["ReliNum"] += 1
        player.languages, player.slang = languagegen(param, player.languages, player.slang)             
    if player.background == "Rewarded":      
        player.gold = 18
        player.equipment = ["A bottle of black ink", "An ink pen", "Five sheets of paper", "A signet ring", "A set of fine clothes"]    
        player.skills_dict["InsiNum"] += 1
        player.skills_dict["PersNum"] += 1
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.proficiencies = gamingsets(param, player.proficiencies)
        player.Trait = ""
        player.Ideal = ""
        player.Bond = ""
        player.Flaw = ""      
        tools = [
            dnd_tools.gaming_sets["DiceSet"], 
            dnd_tools.gaming_sets["DrgnChSet"], 
            dnd_tools.gaming_sets["PlyCrdSet"], 
            dnd_tools.gaming_sets["ThrDgnASet"]
        ]   
        for tool in tools:
            if tool in player.proficiencies:
                player.equipment.append(tool)
    if player.background == "Rival Intern":
        RivInPT1 = "My previous employer didn't respect me, and now I'll do whatever I can to gain respect."
        RivInPT2 = "The job is important, but the relationships I forge with my coworkers are even more so."
        RivInPT3 = "The job is everything to me. Who needs relaxation, hobbies, and a social life?"
        RivInPT4 = "I know I'm not the best and brightest, but if I put my best self forward, I can overcome anything."
        RivInPT5 = "My former boss was an idiot. So was my boss before that. And before that. I'm sure those were all coincidences."
        RivInPT6 = "This company is so much better than my previous one. It will always be the best until they stop paying me."
        RivInPT7 = "I know this dagger belongs to the company, but I'm sure they won't miss it. Or this flask. Or this armor."
        RivInPT8 = "It's only a matter of time before I'll be upper management. I just have to kiss up to my superiors and kick down those beneath me."
        RivInPT = [RivInPT1, RivInPT2, RivInPT3, RivInPT4, RivInPT5, RivInPT6, RivInPT7, RivInPT8]
        player.Trait = random.choice(RivInPT)
        RivInId1 = "Advancement. Money and power can be gained more easily within an organization. I plan to gain as much as possible. (Evil)"
        RivInId2 = "Structure. Life goes much more smoothly when you follow the rules and work within a system. (Lawful)"
        RivInId3 = "Uncertainty. The more chaos that swirls around me, the more opportunities I can find to profit. (Chaotic)"
        RivInId4 = "Justice. I can't stand people being treated unjustly. I do whatever it takes to stop injustice and those who flout the law. (Lawful)"
        RivInId5 = "Pleasure. What's the use of working hard and making money if you can't enjoy the finer things in life? (Any)"
        RivInId6 = "Power. Money is fine, but real power means never having to say you're sorry. (Evil)"
        RivInId = [RivInId1, RivInId2, RivInId3, RivInId4, RivInId5, RivInId6]
        player.Ideal = random.choice(RivInId)
        RivInB1 = "I have a family member in need. I consider them in everything I do."
        RivInB2 = "My peers keep me grounded."
        RivInB3 = "My past mistakes cost someone else dearly. I have to rectify that."
        RivInB4 = "A childhood mentor put me on my current path. If I succeed, I want to repay that mentor in some way."
        RivInB5 = "I value an oath of loyalty I took to a group of friends over everything else in my life."
        RivInB6 = "Although I don't get along well with people, my pet means the world to me."
        RivInB = [RivInB1, RivInB2, RivInB3, RivInB4, RivInB5, RivInB6]
        player.Bond = random.choice(RivInB) 
        RivInF1 = "I know what's best. Trust me."
        RivInF2 = "Flaw? I have no flaws. I'm perfect."
        RivInF3 = "My loyalties are… fluid."
        RivInF4 = "If anything goes wrong, it must be someone else's fault. Let me explain that in detail."
        RivInF5 = "There's right and there's wrong, and there's no gray area in between."
        RivInF6 = "Our superiors might not like what you're doing. I'm going to have to put that in my report."
        RivInF = [RivInF1, RivInF2, RivInF3, RivInF4, RivInF5, RivInF6]
        player.Flaw = random.choice(RivInF)
        player.gold = 10
        player.equipment = ["One set of Artisan's Tools", "A ledger from your previous employer containing a small piece of useful information", "A set of Fine Clothes"]
        player.skills_dict["HistNum"] += 1
        player.skills_dict["InveNum"] += 1
        player.proficiencies = artisantools(param, player.proficiencies)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)             
    if player.background == "Ruined":     
        player.gold = 13
        player.equipment = ["A cracked hourglass", "A set of rusty manacles", "A half-empty bottle", "A hunting trap", "A set of traveler's clothes"]
        player.skills_dict["SteaNum"] += 1
        player.skills_dict["SurvNum"] += 1
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.proficiencies = gamingsets(param, player.proficiencies)
        tools = [
            dnd_tools.gaming_sets["DiceSet"], 
            dnd_tools.gaming_sets["DrgnChSet"], 
            dnd_tools.gaming_sets["PlyCrdSet"], 
            dnd_tools.gaming_sets["ThrDgnASet"]
        ]   
        for tool in tools:
            if tool in player.proficiencies:
                player.equipment.append(tool)      
        player.Trait = ""
        player.Ideal = ""
        player.Bond = ""
        player.Flaw = ""        
    if player.background == "Rune Carver":
        player.gold = 10
        player.equipment = ["A set of artisan's tools (one of your choice)", "A small knife", "A whetstone", "A set of common clothes"]
        player.skills_dict["HistNum"] += 1
        player.skills_dict["PercNum"] += 1
        player.proficiencies = artisantools(param, player.proficiencies)
        player.Trait = ""
        player.Ideal = ""
        player.Bond = ""
        player.Flaw = ""   
        langs = ["Gian"]     
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)     
    if (player.background == "Cloistered Scholar") or (player.background == "Sage"):
        P1 = "I use polysyllabic words that convey the impression of great erudition."
        P2 = "I have read every book in the world's greatest libraries, or I like to boast that I have."
        P3 = "I'm used to helping out those who aren't as smart as I am, and I patiently explain anything and everything to others."
        P4 = "There's nothing I like more than a good mystery."
        P5 = "I'm willing to listen to every side of an argument before I make my own judgment."
        P6 = "I… speak… slowly… when talking… to idiots,… which… almost… everyone… is… compared… to me."
        P7 = "I am horribly, horribly awkward in social situations."
        P8 = "I'm convinced that people are always trying to steal my secrets."
        PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
        player.Trait = random.choice(PTR)
        I1 = "Knowledge - The path to power and self-improvement is through knowledge."
        I2 = "Beauty - What is beautiful points us beyond itself toward what is true."
        I3 = "Logic - Emotions must not cloud our logical thinking."
        I4 = "No Limits - Nothing should fetter the infinite possibility inherent in all existence. "
        I5 = "Power - Knowledge is the path to power and domination. "
        I6 = "Self-Improvement - The goal of a life of study is the betterment of oneself. "
        IDE = [I1, I2, I3, I4, I5, I6]
        player.Ideal = random.choice(IDE)
        B1 = "It is my duty to protect my students."
        B2 = "I have an ancient text that holds terrible secrets that must not fall into the wrong hands."
        B3 = "I work to preserve a library, university, scriptorium, or monastery."
        B4 = "My life's work is a series of tomes related to a specific field of lore."
        B5 = "I've been searching my whole life for the answer to a certain question."
        B6 = "I sold my soul for knowledge. I hope to do great deeds and win it back."
        BND = [B1, B2, B3, B4, B5, B6]
        player.Bond = random.choice(BND)
        F1 = "I am easily distracted by the promise of information."
        F2 = "Most people scream and run when they see a demon. I stop and take notes on its anatomy."
        F3 = "Unlocking an ancient mystery is worth the price of a civilization."
        F4 = "I overlook obvious solutions in favor of complicated ones."
        F5 = "I speak without really thinking through my words, invariably insulting others."
        F6 = "I can't keep a secret to save my life, or anyone else's."
        FLA = [F1, F2, F3, F4, F5, F6]
        player.Flaw = random.choice(FLA)
        player.gold = 10
        if player.background == "Cloistered Solder":
            player.skills_dict["HistNum"] += 1
            player.skills_dict["ArcaNum"], player.skills_dict["NatuNum"], player.skills_dict["ReliNum"] = choicethreeskill(param, player.skills_dict, "ArcaNum", "NatuNum", "ReliNum", dnd_tools.skills["Arcana"], dnd_tools.skills["Nature"], dnd_tools.skills["Religion"])
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.equipment = ["The scholar's robes of your cloister", "A writing kit (small pouch with a Quill, Ink, folded Parchment, and a small penknife)", "A borrowed book on the subject of your current study"]
        if player.background == "Sage":
            player.equipment = ["A bottle of black Ink", "A Quill", "A small knife", "A letter from a dead colleague posing a question you have not yet been able to answer", "A set of Common Clothes"]
            player.skills_dict["ArcaNum"] += 1
            player.skills_dict["HistNum"] += 1
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.languages, player.slang = languagegen(param, player.languages, player.slang)      
    if (player.background == "Sailor") or (player.background == "Pirate"):        
        P1 = "My friends know they can rely on me, no matter what."
        P2 = "I work hard so that I can play hard when the work is done."
        P3 = "I enjoy sailing into new ports and making new friends over a flagon of ale."
        P4 = "I stretch the truth for the sake of a good story."
        P5 = "To me, a tavern brawl is a nice way to get to know a new city."
        P6 = "I never pass up a friendly wager."
        P7 = "My language is as foul as an otyugh nest."
        P8 = "I like a job well done, especially if I can convince someone else to do it."
        PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
        player.Trait = random.choice(PTR)
        I1 = "Respect - The thing that keeps a ship together is mutual respect between captain and crew"
        I2 = "Fairness -  We all do the work, so we all share in the rewards."
        I3 = "Freedom - The sea is freedom-the freedom to go anywhere and do anything."
        I4 = "Mastery -  I'm a predator, and the other ships on the sea are my prey."
        I5 = "People - I'm committed to my crewmates, not to ideals."
        I6 = "Aspiration - Someday I'll own my own ship and chart my own destiny.)"
        IDE = [I1, I2, I3, I4, I5, I6]
        player.Ideal = random.choice(IDE)
        B1 = "I'm loyal to my captain first, everything else second."
        B2 = "The ship is most important, crewmates and captains come and go."
        B3 = "I'll always remember my first ship."
        B4 = "In a harbor town, I have a paramour whose eyes nearly stole me from the sea."
        B5 = "I was cheated out of my fair share of the profits, and I want to get my due."
        B6 = "Ruthless pirates murdered my captain and crewmates, plundered our ship, and left me to die. Vengeance will be mine."
        BND = [B1, B2, B3, B4, B5, B6]
        player.Bond = random.choice(BND)
        F1 = "I follow orders, even if I think they're wrong."
        F2 = "I'll say anything to avoid having to do extra work."
        F3 = "Once someone questions my courage, I never back down no matter how dangerous the situation."
        F4 = "Once I start drinking, it's hard for me to stop."
        F5 = "I can't help but pocket loose coins and other trinkets I come across."
        F6 = "My pride will probably lead to my destruction."
        FLA = [F1, F2, F3, F4, F5, F6]
        player.Flaw = random.choice(FLA)
        player.gold = 10
        player.equipment = ["A belaying pin (club)", "50 feet of Silk Rope", "A lucky charm such as a rabbit foot or a small stone with a hole in the center (or you may roll for a random trinket)", "A set of Common Clothes"]
        player.skills_dict["AthlNum"] += 1
        player.skills_dict["PercNum"] += 1
        player.proficiencies.append(dnd_tools.kits["NavTools"]["Name"])
        player.proficiencies.append(dnd_tools.vehicles["VehSea"])   
    if player.background == "Selesnya Initiate":
        SIPT1 = "I never raise my voice or lose my temper."
        SIPT2 = "I feel the pains and joys of everyone around me, friend or foe."
        SIPT3 = "I would rather make a friend than thwart an enemy."
        SIPT4 = "I'm always straining to peer into another reality that seems to be just beyond my senses."
        SIPT5 = "I'm uneasy if I can't see plants growing or feel soil beneath my feet."
        SIPT6 = "Seeing illness or injury in any creature saddens me."
        SIPT7 = "I have much to be proud of, but I am still just one strand in the grand, interwoven tapestry of life."
        SIPT8 = "Nature offers rich and abundant metaphors for understanding the complexities of life."
        SIPT = [SIPT1, SIPT2, SIPT3, SIPT4, SIPT5, SIPT6, SIPT7, SIPT8]
        player.Trait = random.choice(SIPT)
        SelesInI1 = "Guild: My guild is all that really matters. (Any)"
        SelesInI2 = "Harmony: Nothing is more beautiful than voices and actions aligned in common purpose. (Good)"
        SelesInI3 = "Order: Like a well-pruned tree, society thrives when everything is kept in good order. (Lawful)"
        SelesInI4 = "Life: Preserving life and nature is always a worthwhile endeavor. (Good)"
        SelesInI5 = "Humility: Ambition and pride are the roots of strife. (Good)"
        SelesInI6 = "Evangelism: When all have joined the Selesnya Conclave, Ravnica will finally know peace. (Any)"
        SelesInI = [SelesInI1, SelesInI2, SelesInI3, SelesInI4, SelesInI5, SelesInI6]
        player.Ideal = random.choice(SelesInI)
        SelesInB1 = "I would give my life in the defense of the small enclave where I first encountered Mat'Selesnya."
        SelesInB2 = "I love beasts and plants of all kinds, and am loath to harm them."
        SelesInB3 = "A healer nursed me to recovery from a mortal illness."
        SelesInB4 = "I'll sing the invitation of Mat'Selesnya with my dying breath."
        SelesInB5 = "I cherish a leaf from Vitu-Ghazi that changes color with the seasons, even though it is no longer at-tached to the tree."
        SelesInB6 = "Every member of the conclave is my kin, and I would fight for any one of them."
        SelesInB = [SelesInB1, SelesInB2, SelesInB3, SelesInB4, SelesInB5, SelesInB6]
        player.Bond = random.choice(SelesInB)
        SelesInF1 = "I'm terrified of getting into a fight where my side is outnumbered."
        SelesInF2 = "I assume that people mean well until they prove otherwise."
        SelesInF3 = "I enjoy comfort and quiet, and prefer to avoid extra effort."
        SelesInF4 = "I have a fierce temper that doesn't reflect the inner calm I seek."
        SelesInF5 = "I'm convinced that everyone else in the conclave has a deeper connection to the Worldsoul than I do."
        SelesInF6 = "I'm trying to atone for the life of crime I led before I joined the Selesnya, but I find it hard to give up my bad habits."
        SelesInF = [SelesInF1, SelesInF2, SelesInF3, SelesInF4, SelesInF5, SelesInF6]
        player.Flaw = random.choice(SelesInF)
        player.gold = 5
        player.equipment = ["A Selesnya insignia", "A Healer's Kit", "Robes", "A set of Common Clothes"]
        player.skills_dict["NatuNum"] += 1
        player.skills_dict["PersNum"] += 1
        player.proficiencies = artisantoolsmusicalinstr(param, player.proficiencies)
        langlist = ["Elvi", "Loxo", "Sylv"]
        player.languages, player.slang = choicethreelang(param, player.languages, player.slang, langlist)   
    if player.background == "Shipwright": 
        ShipwPT1 = "I love talking and being heard more than I like to listen."
        ShipwPT2 = "I'm extremely fond of puzzles."
        ShipwPT3 = "I thrive under pressure."
        ShipwPT4 = "I love sketching and designing objects, especially boats."
        ShipwPT5 = "I'm not afraid of hard work-in fact, I prefer it."
        ShipwPT6 = "A pipe, an ale, and the smell of the sea: paradise."
        ShipwPT7 = "I have an endless supply of cautionary tales related to the sea."
        ShipwPT8 = "I don't mind getting my hands dirty."
        ShipwPT = [ShipwPT1, ShipwPT2, ShipwPT3, ShipwPT4, ShipwPT5, ShipwPT6, ShipwPT7, ShipwPT8]
        player.Trait = random.choice(ShipwPT)
        ShipwId1 = "Crew. If everyone on deck pitches in, we'll never sink. (Good)"
        ShipwId2 = "Careful Lines. A ship must be balanced according to the laws of the universe. (Lawful)"
        ShipwId3 = "Invention. Make what you need out of whatever is at hand. (Chaotic)"
        ShipwId4 = "Perfection. To measure a being and find it lacking is the greatest disappointment. (Evil)"
        ShipwId5 = "Reflection. Muddied water always clears in time. (Any)"
        ShipwId6 = "Hope. The horizon at sea holds the greatest promise. (Any)"
        ShipwId = [ShipwId1, ShipwId2, ShipwId3, ShipwId4, ShipwId5, ShipwId6]
        player.Ideal = random.choice(ShipwId)
        ShipwB1 = "I must visit all the oceans of the world and behold the ships that sail there."
        ShipwB2 = "Much of the treasure I claim will be used to enrich my community."
        ShipwB3 = "I must find a kind of wood rumored to possess magical qualities."
        ShipwB4 = "I repair broken things to redeem what's broken in myself."
        ShipwB5 = "I will craft a boat capable of sailing through the most dangerous of storms."
        ShipwB6 = "A kraken destroyed my masterpiece; its teeth shall adorn my hearth."
        ShipwB = [ShipwB1, ShipwB2, ShipwB3, ShipwB4, ShipwB5, ShipwB6]
        player.Bond = random.choice(ShipwB)
        ShipwF1 = "I don't know when to throw something away. You never know when it might be useful again."
        ShipwF2 = "I get frustrated to the point of distraction by shoddy craftsmanship."
        ShipwF3 = "Though I am an excellent crafter, my work tends to look as though it belongs on a ship."
        ShipwF4 = "I am so obsessed with sketching my ideas for elaborate inventions that I sometimes forget little thing like eating and sleeping."
        ShipwF5 = "I'm judgmental of those who are not skilled with tools of some kind."
        ShipwF6 = "I sometimes take things that don't belong to me, especially if they are very well made."
        ShipwF = [ShipwF1, ShipwF2, ShipwF3, ShipwF4, ShipwF5, ShipwF6]
        player.Flaw = random.choice(ShipwF)
        player.gold = 10
        player.equipment = ["A set of well-loved Carpenter's Tools", "A blank book", "1 ounce of Ink", "An Ink Pen", "A set of Traveler's Clothes"]
        player.skills_dict["HistNum"] += 1
        player.skills_dict["PercNum"] += 1
        player.proficiencies.append(dnd_tools.artisan_tools["CarpTools"]["Name"])
        player.proficiencies.append(dnd_tools.vehicles["VehSea"])
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)     
        #Start from here when normal resuming these edits
    if player.background == "Silverquill Student": 
        player.gold = 15
        player.equipment = ["A bottle of Black Ink", "An Ink Pen", "A book of poetry", "A school uniform"]
        player.skills_dict["IntiNum"] += 1
        player.skills_dict["PersNum"] += 1
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.Trait = ""
        player.Ideal = ""
        player.Bond = ""
        player.Flaw = ""         
    if player.background == "Simic Scientist":
        SSPT1 = "I can't wait to see what I become next!"
        SSPT2 = "I am convinced that everything inclines toward constant improvement."
        SSPT3 = "I'm eager to explain every detail of my most intricate experiments and theories to anyone who shows the least bit of interest."
        SSPT4 = "I assume that everyone needs even the most basic concepts explained to them."
        SSPT5 = "I describe everything that happens as if it were going into my research notes (and it often is)."
        SSPT6 = "I am insatiably curious about the seemingly infinite forms and adaptations of life."
        SSPT7 = "I can't resist prying into anything forbidden, since it must be terribly interesting."
        SSPT8 = "I employ a highly technical vocabulary to avoid imprecision and ambiguity in my communication."
        SSPT = [SSPT1, SSPT2, SSPT3, SSPT4, SSPT5, SSPT6, SSPT7, SSPT8]
        player.Trait = random.choice(SSPT)
        SimSciI1 = "Guild: My guild is all that really matters. (Any)"
        SimSciI2 = "Change: All life is meant to progress toward perfection, and our work is to hurry it along — no matter what must be upended along the way. (Chaotic)"
        SimSciI3 = "Knowledge: Understanding the world is more important than what you do with your knowledge. (Neutral)"
        SimSciI4 = "Greater Good: I want to reshape the world into higher forms of life so that all can enjoy evolution. (Good)"
        SimSciI5 = "Logic: It's foolish to let emotions and principles inter-fere with the conclusions of logic. (Lawful)"
        SimSciI6 = "Superiority: My vast intellect and strength are directed toward increasing my sway over others. (Evil)"
        SimSciI = [SimSciI1, SimSciI2, SimSciI3, SimSciI4, SimSciI5, SimSciI6]
        player.Ideal = random.choice(SimSciI)
        SimSciB1 = "I helped create a krasis that I love like a pet and would carry with me everywhere… except it's the size of a building, and it might eat me."
        SimSciB2 = "In my laboratory, I discovered something that I think could eliminate half the life on Ravnica."
        SimSciB3 = "The other researchers in my clade are my family — a big, eccentric family including members and parts of many species."
        SimSciB4 = "The laboratory where I did my research contains everything that is precious to me."
        SimSciB5 = "I will get revenge on the shortsighted fool who killed my precious krasis creation."
        SimSciB6 = "Everything I do is an attempt to impress someone I love."
        SimSciB = [SimSciB1, SimSciB2, SimSciB3, SimSciB4, SimSciB5, SimSciB6]
        player.Bond = random.choice(SimSciB)
        SimSciF1 = "I have a rather embarrassing mutation that I do everything I can to keep hidden."
        SimSciF2 = "I'm more interested in taking notes on monstrous anatomy than in lighting monsters."
        SimSciF3 = "Every social situation I'm in seems to lead to my asking rude personal questions."
        SimSciF4 = "I'm supremely confident in my ability to adapt to any situation and handle any danger."
        SimSciF5 = "I'll take any risk to earn recognition for my scientific brilliance."
        SimSciF6 = "I have a tendency to take shortcuts in my research and any other tasks I have to complete."
        SimSciF = [SimSciF1, SimSciF2, SimSciF3, SimSciF4, SimSciF5, SimSciF6]
        player.Flaw = random.choice(SimSciF)
        player.gold = 10
        player.equipment = ["A Simic insignia", "A set of Commoner's Clothes", "A book of research notes", "An Ink Pen", "A bottle of squid ink", "A flask of oil (made from blubber)", "A Vial of Acid (derived from digestive juices)", "A vial of fish scales", "A vial of seaweed", "A vial of jellyfish stingers", "A glass bottle of unidentified slime"]
        player.skills_dict["ArcaNum"] += 1
        player.skills_dict["MediNum"] += 1
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)            
    if player.background == "Smuggler":
        SmuPT1 = "I love being on the water but hate fishing."
        SmuPT2 = "I think of everything in terms of monetary value."
        SmuPT3 = "I never stop smiling."
        SmuPT4 = "Nothing rattles me; I have a lie for every occasion."
        SmuPT5 = "I love gold but won't cheat a friend."
        SmuPT6 = "I enjoy doing things others believe to be impossible."
        SmuPT7 = "I become wistful when I see the sun rise over the ocean."
        SmuPT8 = "I am no common criminal; I am a mastermind."
        SmuPT = [SmuPT1, SmuPT2, SmuPT3, SmuPT4, SmuPT5, SmuPT6, SmuPT7, SmuPT8]
        player.Trait = random.choice(SmuPT)
        SmuId1 = "Wealth. Heaps of coins in a secure vault is all I dream of. (Any)"
        SmuId2 = "Smuggler's Code. I uphold the unwritten rules of the smugglers, who do not cheat one another or directly harm innocents. (Lawful)"
        SmuId3 = "All for a Coin. I'll do nearly anything if it means I turn a profit. (Evil)"
        SmuId4 = "Peace and Prosperity. I smuggle only to achieve a greater goal that benefits my community. (Good)"
        SmuId5 = "People. For all my many lies, I place a high value on friendship. (Any)"
        SmuId6 = "Daring. I am most happy when risking everything. (Any)"
        SmuId = [SmuId1, SmuId2, SmuId3, SmuId4, SmuId5, SmuId6]
        player.Ideal = random.choice(SmuId)
        SmuB1 = "My vessel was stolen from me, and I burn with the desire to recover it."
        SmuB2 = "I intend to become the leader of the network of smugglers that I belong to."
        SmuB3 = "I owe a debt that cannot be repaid in gold."
        SmuB4 = "After one last job, I will retire from the business."
        SmuB5 = "I was tricked by a fellow smuggler who stole something precious from me. I will find that thief."
        SmuB6 = "I give most of my profits to a charitable cause, and I don't like to brag about it."
        SmuB = [SmuB1, SmuB2, SmuB3, SmuB4, SmuB5, SmuB6]
        player.Bond = random.choice(SmuB)
        SmuF1 = "Lying is reflexive, and I sometimes engage in it without realizing."
        SmuF2 = "I tend to assess my relationships in terms of profit and loss."
        SmuF3 = "I believe everyone has a price and am cynical toward those who present themselves as virtuous."
        SmuF4 = "I struggle to trust the words of others."
        SmuF5 = "Few people know the real me."
        SmuF6 = "Though I act charming, I feel nothing for others and don't know what friendship is."
        SmuF = [SmuF1, SmuF2, SmuF3, SmuF4, SmuF5, SmuF6]
        player.Flaw = random.choice(SmuF)
        player.gold = 15
        player.equipment = ["A fancy leather vest or a pair of leather boots", "A set of Common Clothes"]
        player.skills_dict["AthlNum"] += 1
        player.skills_dict["DeceNum"] += 1
        player.proficiencies.append(dnd_tools.vehicles["VehSea"])       
    if (player.background == "City Watch") or (player.background == "Knight of the Order") or (player.background == "Mercenary Veteran") or (player.background == "Soldier"):
        P1 = "I am always polite and respectful."
        P2 = "I am haunted by memories of war. I can't get the images of violence out of my mind."
        P3 = "I have lost too many friends and I am slow to make a new one."
        P4 = "I am full of inspiring and cautionary tales from my military experience which is relevant to almost every combat situation."
        P5 = "I can stare down a hell hound without flinching."
        P6 = "I enjoy being strong and I like breaking things."
        P7 = "I have a crude sense of humor."
        P8 = "I face problems head-on. A simple, direct solution is the best path to success."
        PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
        player.Trait = random.choice(PTR)
        I1 = "Greater Good - Our lot is to lay down our lives in defense of others."
        I2 = "Responsibility - I do what I must and obey just authority."
        I3 = "Independence - When people follow orders blindly, they embrace a kind of tyranny."
        I4 = "Might -  In life as in war, the stronger force wins."
        I5 = "Live and Let Live - Ideals are not worth killing over or going to war for."
        I6 = "Nation - My city, nation, or people are all that matter."
        IDE = [I1, I2, I3, I4, I5, I6]
        player.Ideal = random.choice(IDE)
        B1 = "I would still lay down my life for the people I served with."
        B2 = "Someone saved my life on the battlefield. To this day, I will never leave a friend behind."
        B3 = "My honor is my life."
        B4 = "I will never forget the crushing defeat my company suffered or the enemies who dealt it."
        B5 = "Those who fight beside me are those worth dying for."
        B6 = "I fight for those who cannot fight for themselves."
        BND = [B1, B2, B3, B4, B5, B6]
        player.Bond = random.choice(BND)
        F1 = "The monstrous enemy which we faced in battle still leaves me quivering with fear."
        F2 = "I have little respect for anyone who is not a proven warrior."
        F3 = "I made a terrible mistake in battle that cost many lives, and I would do anything to keep that mistake secret."
        F4 = "My hatred of my enemies is blind and unreasoning."
        F5 = "I obey the law, even if the law causes misery."
        F6 = "I would rather eat my armor than admit when I’m wrong."
        FLA = [F1, F2, F3, F4, F5, F6]
        player.Flaw = random.choice(FLA)
        player.gold = 10
        if player.background == "City Watch":
            player.skills_dict["AthlNum"] += 1
            player.skills_dict["InsiNum"] += 1
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.equipment = ["A uniform in the style of your unit and indicative of your rank", "A horn with which to summon help", "A set of Manacles"]
        if player.background == "Knight of the Order":
            player.skills_dict["PersNum"] += 1
            player.skills_dict["ArcaNum"], player.skills_dict["HistNum"], player.skills_dict["NatuNum"], player.skills_dict["ReliNum"] = choicefourskill(param, player.skills_dict, "ArcaNum", "HistNum", "NatuNum", "ReliNum", dnd_tools.skills["Arcana"], dnd_tools.skills["History"], dnd_tools.skills["Nature"], dnd_tools.skills["Religion"])
            player.proficiencies = gamingsetsmusicalinstr(param, player.proficiencies)
            player.languages, player.slang = languagegen(param, player.languages, player.slang)
            player.equipment = ["One set of Traveler's Clothes", "A Signet", "Banner or seal representing your place or rank in the order"]
        if player.background == "Mercenary Veteran":
            player.skills_dict["AthlNum"] += 1
            player.skills_dict["PersNum"] += 1
            player.proficiencies.append(dnd_tools.vehicles["VehLand"])
            player.proficiencies = gamingsets(param, player.proficiencies)
            player.equipment = ["A uniform of your company (Traveler's Clothes in quality)", "An insignia of your rank", "A Gaming Set of your choice"]
        if player.background == "Soldier":
            player.skills_dict["AthlNum"] += 1
            player.skills_dict["IntiNum"] += 1
            player.proficiencies.append(dnd_tools.vehicles["VehLand"])
            player.proficiencies = gamingsets(param, player.proficiencies)       
            player.equipment = ["An insignia of rank", "A trophy taken from a fallen enemy (a Dagger, broken blade, or piece of a banner)", "A set of Bone Dice or Deck of Cards", "A set of Common Clothes"]                 
    if player.background == "Urchin":
        P1 = "I hide scraps of food and trinkets away in my pockets."
        P2 = "I ask a lot of questions."
        P3 = "I like to squeeze into small places where no one else can get to me."
        P4 = "I sleep with my back to a wall or tree, with everything I own wrapped in a bundle in my arms."
        P5 = "I eat like a pig and have bad manners."
        P6 = "I think anyone who's nice to me is hiding evil intent."
        P7 = "I don't like to bathe."
        P8 = "I bluntly say what other people are hinting at or hiding."
        PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
        player.Trait = random.choice(PTR)
        I1 = "Respect - All people, rich or poor, deserve respect."
        I2 = "Community: We have to take care of each other, because no one else is going to do it."
        I3 = "Change - The low are lifted up, and the high and mighty are brought down. Change is the nature of things."
        I4 = "Retribution - The rich need to be shown what life and death are like in the gutters."
        I5 = "People - I help the people who help me-that's what keeps us alive."
        I6 = "Aspiration - I'm going to prove that I'm worthy of a better life."
        IDE = [I1, I2, I3, I4, I5, I6]
        player.Ideal = random.choice(IDE)
        B1 = "My town or city is my home, and I'll fight to defend it."
        B2 = "I sponsor an orphanage to keep others from enduring what I was forced to endure."
        B3 = "I owe my survival to another urchin who taught me to live on the streets."
        B4 = "I owe a debt I can never repay to the person who took pity on me."
        B5 = "I escaped my life of poverty by robbing an important person, and I'm wanted for it."
        B6 = "No one else should have to endure the hardships I've been through."
        BND = [B1, B2, B3, B4, B5, B6]
        player.Bond = random.choice(BND)
        F1 = "If I'm outnumbered, I will run away from a fight."
        F2 = "Gold seems like a lot of money to me, and I'll do just about anything for more of it."
        F3 = "I will never fully trust anyone other than myself."
        F4 = "I'd rather kill someone in their sleep then fight fair."
        F5 = "It's not stealing if I need it more than someone else."
        F6 = "People who can't take care of themselves get what they deserve."
        FLA = [F1, F2, F3, F4, F5, F6]
        player.Flaw = random.choice(FLA)
        player.gold = 10
        player.equipment = ["A small knife", "A map of the city you grew up in", "A pet mouse", "A token to remember your parents by", "A set of Common Clothes"]
        player.skills_dict["SloHNum"] += 1
        player.skills_dict["SteaNum"] += 1
        player.proficiencies.append(dnd_tools.kits["DisgKit"]["Name"])
        player.proficiencies.append(dnd_tools.kits["ThievKit"]["Name"])    
    if player.background == "Volstrucker Agent":
        VolsAgPT1 = "I prefer to keep my thoughts to myself."
        VolsAgPT2 = "I indulge vice in excess to quiet my conscience."
        VolsAgPT3 = "I've left emotion behind me. I'm now perfectly placid."
        VolsAgPT4 = "Some event from the past keeps worming its way into my mind, making me restless."
        VolsAgPT5 = "I always keep my word-except when I'm commanded to break it."
        VolsAgPT6 = "I laugh off insults and never take them personally."
        VolsAgPT = [VolsAgPT1, VolsAgPT2, VolsAgPT3, VolsAgPT4, VolsAgPT5, VolsAgPT6]
        player.Trait = random.choice(VolsAgPT)
        VolsAgId1 = "Order. The will of the crown is absolute. (Law)"
        VolsAgId2 = "True Loyalty. The Cerberus Assembly is greater than any power, even the crown. (Law)"
        VolsAgId3 = "Death. The penalty for disloyalty is death. (Evil)"
        VolsAgId4 = "Determination. I cannot fail. Not ever. (Neutral)"
        VolsAgId5 = "Fear. People should not respect power. They should fear it. (Evil)"
        VolsAgId6 = "Escape. The Volstrucker are pure evil! I can't atone for what I've done for them, but I can escape with my life. (Any)"
        VolsAgId = [VolsAgId1, VolsAgId2, VolsAgId3, VolsAgId4, VolsAgId5, VolsAgId6]
        player.Ideal = random.choice(VolsAgId)
        VolsAgB1 = "The job is all that matters. I will see it through."
        VolsAgB2 = "My orders are important, but my comrades are worth more than anything. I would die for them."
        VolsAgB3 = "Everything I've done, I've done to protect someone close to me."
        VolsAgB4 = "If the empire falls, all of civilization falls with it. I will hold back chaos and barbarism at any cost."
        VolsAgB = [VolsAgB1, VolsAgB2, VolsAgB3, VolsAgB4]
        player.Bond = random.choice(VolsAgB)
        VolsAgF1 = "I drink to dull the pain in the back of my head."
        VolsAgF2 = "I go a bit mad when I see blood."
        VolsAgF3 = "I can hear the voices of everyone I've killed. I see their faces. I can't be free of these ghosts."
        VolsAgF4 = "Fear is a powerful motivator. I will do whatever it takes to prevent those who know what I am from seeing me fail, and from those I care about from knowing what I am."
        VolsAgF = [VolsAgF1, VolsAgF2, VolsAgF3, VolsAgF4]
        player.Flaw = random.choice(VolsAgF)
        player.gold = 10
        player.equipment = ["A set of Common Clothes", "A black cloak with a hood", "A Poisoner's Kit"]
        player.skills_dict["DeceNum"] += 1
        player.skills_dict["SteaNum"] += 1
        player.proficiencies.append(dnd_tools.kits["PoisKit"]["Name"])
        player.languages, player.slang = languagegen(param, player.languages, player.slang)      
    if player.background == "Wildspacer":
        player.gold = 10
        player.equipment = ["A belaying pin (club)", "A set of traveler's clothes", "A grappling hook", "50 feet of hempen rope"]
        player.skills_dict["AthlNum"] += 1
        player.skills_dict["SurvNum"] += 1
        player.proficiencies.append(dnd_tools.kits["NavTools"]["Name"])
        player.proficiencies.append(dnd_tools.vehicles["VehSpace"])
        player.Trait = ""
        player.Ideal = ""
        player.Bond = ""
        player.Flaw = ""        
    if player.background == "Wind-Touched":
        WiToPT1 = "I never back down from a challenge."
        WiToPT2 = "I always end up being the center of attention."
        WiToPT3 = "I am gifted by the wind and destined for greatness."
        WiToPT4 = "I have no time for those who doubt me."
        WiToPT5 = "I seek out challenges to test myself."
        WiToPT6 = "I am better than everyone else."
        WiToPT7 = "I avoid showing my power at all costs."
        WiToPT8 = "I remain humble despite my blessing."
        WiToPT = [WiToPT1, WiToPT2, WiToPT3, WiToPT4, WiToPT5, WiToPT6, WiToPT7, WiToPT8]
        player.Trait = random.choice(WiToPT)
        WiToId1 = "Responsibility. The powers I have been gifted with are meant to serve the common good. (Good)"
        WiToId2 = "Heroism. The wind chose me to be a brave warrior and leader, so shall it be. (Lawful)"
        WiToId3 = "Egotism. My powers situate me above others. The masses should know their place. (Evil)"
        WiToId4 = "Mysticism. Connected to nature, I speak for the wind and divine its will for others. (Neutral)"
        WiToId5 = "Cynicism. What matters isn’t whether or not my powers are genuine, but what advantages I can reap because of that belief. (Evil)"
        WiToId6 = "Naturalism. The wind speaks to my soul, and I am bound to go wherever it directs me. (Chaotic)"
        WiToId = [WiToId1, WiToId2, WiToId3, WiToId4, WiToId5, WiToId6]
        player.Ideal = random.choice(WiToId)
        WiToB1 = "I am guided by a wise elder who prepares me for my destiny."
        WiToB2 = "I am estranged from my parents who don’t believe in my blessing."
        WiToB3 = "I seek to discredit the person who burdened me with this moniker."
        WiToB4 = "I live in the shadow of my mentor, seeking their approval."
        WiToB5 = "I have a sibling who is not blessed, which causes tension"
        WiToB6 = "I am one with the wind. Personal relationships are fleeting."
        WiToB = [WiToB1, WiToB2, WiToB3, WiToB4, WiToB5, WiToB6]
        player.Bond = random.choice(WiToB)
        WiToF1 = "I can’t accept another’s suggestion once I’ve set my path."
        WiToF2 = "I expect nothing less than reverence from common people."
        WiToF3 = "I blindly trust in the power of my blessing."
        WiToF4 = "I am overly concerned about how others see me."
        WiToF5 = "I will prove my worth, even if it means putting myself and my friends in danger."
        WiToF6 = "I am burdened with responsibility, and find it hard to make even the simplest decisions."
        WiToF = [WiToF1, WiToF2, WiToF3, WiToF4, WiToF5, WiToF6]
        player.Flaw = random.choice(WiToF)
        player.gold = 10
        player.equipment = ["A wind Musical Instrument (one of your choice)", "An ornate cloak", "A symbol of the wind", "Common clothes"]
        player.skills_dict["AcroNum"] += 1
        player.skills_dict["PerfNum"] += 1
        WindInstr = [
            dnd_tools.musical_instr["Bagpipes"]["Name"], 
            dnd_tools.musical_instr["Birdpipes"]["Name"],
            dnd_tools.musical_instr["Flute"]["Name"], 
            dnd_tools.musical_instr["Glaur"]["Name"], 
            dnd_tools.musical_instr["Horn"]["Name"], 
            dnd_tools.musical_instr["Longhorn"]["Name"], 
            dnd_tools.musical_instr["Shawm"]["Name"], 
            dnd_tools.musical_instr["Songhorn"]["Name"], 
            dnd_tools.musical_instr["Thelarr"]["Name"], 
            dnd_tools.musical_instr["Zulkoon"]["Name"]
            ]
        if param == "Y":
            print("0 - Random")
            for idx, wmi in enumerate(WindInstr, 1):
                print(f"{idx} - {wmi}")
            winstr = int(input("Choose a wind-based instrument to be proficient in. "))
            if winstr == 0:
                player.proficiencies.append(random.choice(WindInstr))
            elif 1 <= winstr <= len(WindInstr):
                player.proficiencies.append(WindInstr[winstr - 1])
        if param == "N":
            player.proficiencies.append(random.choice(WindInstr))
        langs = ["Aura"]
        for lang in langs:
            if lang in player.slang:
                player.languages.append(dnd_tools.languages[lang])
                player.slang.remove(lang)                 
    if player.background == "Witchlight Hand":
        WitHPT1 = "I'm haunted by fey laughter that only I can hear, though I know it's just my mind playing tricks on me."
        WitHPT2 = "Like a nomad, I can't settle down in one place for very long."
        WitHPT3 = "Good music makes me weep like a baby."
        WitHPT4 = "Wherever I go, I try to bring a little of the warmth and tranquility of home with me."
        WitHPT5 = "I have never lost my childlike sense of wonder."
        WitHPT6 = "When I have a new idea, I get wildly excited about it until I come up with another, better idea."
        WitHPT7 = "I live by my own set of weird and wonderful rules."
        WitHPT8 = "I can't bring myself to trust most adults."
        WitHPT = [WitHPT1, WitHPT2, WitHPT3, WitHPT4, WitHPT5, WitHPT6, WitHPT7, WitHPT8]
        player.Trait = random.choice(WitHPT)
        WitHId1 = "Friendship. I never leave a friend behind. (Good)"
        WitHId2 = "Empathy. No creature should be made to suffer. (Good)"
        WitHId3 = "Wanderlust. I prefer to take the less traveled path. (Chaotic)"
        WitHId4 = "Changeability. Change is good, which is why I live by an ever-changing set of rules. (Chaotic)"
        WitHId5 = "Honor. A deal is a deal, and I would never break one. (Lawful)"
        WitHId6 = "Rule of Three. Everything in the multiverse happens in threes. I see the 'rule of three' everywhere. (Lawful)"
        WitHId7 = "Obsession. I won't let go of a grudge. (Evil)"
        WitHId8 = "Greed. I will do whatever it takes to get what I want, regardless of the harm it might cause. (Evil)"
        WitHId = [WitHId1, WitHId2, WitHId3, WitHId4, WitHId5, WitHId6, WitHId7, WitHId8]
        player.Ideal = random.choice(WitHId)
        WitHB1 = "I would never break my word."
        WitHB2 = "I find magic in all its forms to be compelling. The more magical a place, the more I am drawn to it."
        WitHB3 = "I do what I can to protect the natural world."
        WitHB4 = "A trusted friend is the most important thing in the multiverse to me."
        WitHB5 = "I can't bring myself to harm a Fey creature, either because I consider myself one or because I fear the repercussions."
        WitHB6 = "The Witchlight Carnival feels like home to me."
        WitHB7 = "I'm drawn to the Feywild and long to return there, if only for a short while."
        WitHB8 = "I feel indebted to Mister Witch and Mister Light for giving me a home and a purpose."
        WitHB = [WitHB1, WitHB2, WitHB3, WitHB4, WitHB5, WitHB6, WitHB7, WitHB8]
        player.Bond = random.choice(WitHB)
        WitHF1 = "I easily lose track of time. My poor sense of time means I'm always late."
        WitHF2 = "I think the whole multiverse is out to get me."
        WitHF3 = "I'm always operating under a tight timeline, and I'm obsessed with keeping everything on schedule."
        WitHF4 = "I'm a kleptomaniac who covets shiny, sparkling treasure."
        WitHF5 = "I'm forgetful. Sometimes I can't remember even the simplest things."
        WitHF6 = "I never give away anything for free and always expect something in return."
        WitHF7 = "I have many vices and tend to indulge them."
        WitHF8 = "I'm always changing my mind—well, almost always."
        WitHF = [WitHF1, WitHF2, WitHF3, WitHF4, WitHF5, WitHF6, WitHF7, WitHF8]
        player.Flaw = random.choice(WitHF)
        player.gold = 8
        player.equipment = ["A Disguise Kit or a musical instrument of your choice", "A deck of cards", "A carnival uniform or costume", "One trinket (determined by rolling on the Feywild Trinkets)"]
        player.skills_dict["PerfNum"] += 1
        player.skills_dict["SloHNum"] += 1
        player.proficiencies = musicalinstrdisg(param, player.proficiencies)
        player.languages, player.slang = languagegen(param, player.languages, player.slang)  
    if player.background == "Witherbloom Student":    
        player.gold = 15
        player.equipment = ["A bottle of Black Ink", "An Ink Pen", "A book about plant identification", "An Iron Pot", "An Herbalism Kit", "A school uniform"]
        player.skills_dict["NatuNum"] += 1
        player.skills_dict["SurvNum"] += 1
        player.proficiencies.append(dnd_tools.kits["HerbKit"]["Name"])
        player.languages, player.slang = languagegen(param, player.languages, player.slang)
        player.Trait = ""
        player.Ideal = ""
        player.Bond = ""
        player.Flaw = ""
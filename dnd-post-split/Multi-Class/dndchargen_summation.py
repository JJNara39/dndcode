import random
import math
from dndchargen_languagesskills import *
from dndchargen_character_builder import *

def d6():
    result = random.randint(1,6)
    return result

def summation(param, playername, charactername, plLvl, Gender, race, subrace, color, gem, metal, Height, Weight, walkingspeed, RaceNotes, Class, subclass, submulticlass, BeachballFlag, HollowOne, Lineage, PlLang, SLANG, PlProf, SkillsProf, Notes, back, Trait, Ideal, Bond, Flaw, BGL, EQP, skills_dict, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom):
    AdditionalInfo = []
    if race == "Aasimar":
        CF1 = "A dusting of metallic, white, or charcoal freckles"
        CF2 = "Metallic, luminous, or dark eyes"
        CF3 = "Starkly colored hair"
        CF4 = "An unusual hue tinting your shadow"
        CF5 = "A ghostly halo crowning your head"
        CF6 = "Rainbows gleaming on your skin"
        CF = [CF1, CF2, CF3, CF4, CF5, CF6]
        CelesFeat = random.choice(CF)
        AdditionalInfo.append(f"As an Aasimar, your Celestial Feature is {CelesFeat}")
        if subrace == "Protector Aasimar":
            AngG1 = "Tadriel"
            AngG2 = "Myllandra"
            AngG3 = "Seraphina"
            AngG4 = "Galladia"
            AngG5 = "Mykiel"
            AngG6 = "Valandras"
            AngG = [AngG1, AngG2, AngG3, AngG4, AngG5, AngG6]
            AngelicGuide = random.choice(AngG)
            AngN1 = "Bookish and lecturing"
            AngN2 = "Compassionate and hopeful"
            AngN3 = "Practical and lighthearted"
            AngN4 = "Fierce and vengeful"
            AngN5 = "Stern and judgemental"
            AngN6 = "Kind and parental"
            AngN = [AngN1, AngN2, AngN3, AngN4, AngN5, AngN6]
            AngelicNature = random.choice(AngN)   
            AdditionalInfo.append(f"As an aasimar who has not turned evil, your Angelic Guide is {AngelicGuide} and your Angelic Nature is {AngelicNature}")     
    
    if race == "Autognome":
        AgnHist1 = "Your creator gave you autonomy and urged you to follow your dreams."
        AgnHist2 = "Your creator died, leaving you to fend for yourself."
        AgnHist3 = "A glitch caused you to forget your original programming. You don't remember who made you or where you came from."
        AgnHist4 = "You didn't like how you were being treated by your creator, so you ran away from home."
        AgnHist5 = "You were built to complete a special mission."
        AgnHist6 = "You felt trapped in the role for which you were built and abandoned your creator, determined to find a greater purpose."
        AgnHist = [AgnHist1, AgnHist2, AgnHist3, AgnHist4, AgnHist5, AgnHist6]
        AutognomeHistory = random.choice(AgnHist)
        AdditionalInfo.append(f"As an Autognome, your history: {AutognomeHistory}")

    if race == "Dwarf":
        if subrace == "Duergar":
            DASH1 = "You are a heretic,drawn to worship of Morad in."
            DASH2 = "Caught stealing, you escaped imprisonment but not before torture left you with a scar or lasting injury."
            DASH3 = "You were enslaved by drow or mind flayers but escaped to the surface."
            DASH4 = "You seek only to test yourself in battle with monsters."
            DASH5 = "Profit is all that matters to you."
            DASH6 = " The best way to defeat the folk of the surface is to study them firsthand."
            DASH = [DASH1, DASH2, DASH3, DASH4, DASH5, DASH6]
            DuergarHook = random.choice(DASH)
            DuerQ1 = "A separate personality in your mind provides advice and guidance to you."
            DuerQ2 = "Your gear must be perfectly arranged, otherwise someone must bleed."
            DuerQ3 = "When there isn't a roof over your head, you keep your eyes on the ground."
            DuerQ4 = "You don't talk unless you absolutely must."
            DuerQ5 = "The outside world is a giant cave, and nothing will convince you otherwise."
            DuerQ6 = "Humans fascinate you, and you collect odd trinkets of their culture."
            DuerQ = [DuerQ1, DuerQ2, DuerQ3, DuerQ4, DuerQ5, DuerQ6]
            DuergarQuirk = random.choice(DuerQ)
            AdditionalInfo.append(f"As a Duergar, your Story Hook: {DuergarHook}")
            AdditionalInfo.append(f"As a Duergar, your Duergar Quirk: {DuergarQuirk}") 
        else:
            DwaSH1 = "You were accused of stealing a fellow artisan's item and claiming it as your work. Innocent or guilty, you were made an outcast."
            DwaSH2 = "Your wanderlust prompted you to shirk your duties as a crafter in favor of wandering the world. Your clan isn't pleased with this choice."
            DwaSH3 = "You became separated from your clan due to an earthquake, a drow slave raid, or similar event and hope to return home."
            DwaSH4 = "You were assigned to become a merchant by the priests of Moradin and have yet to forgive them for their mistake. You should be working a forge, not wandering the outside world."
            DwaSH5 = "You are a spy, traveling incognito to gather information for the clan elders."
            DwaSH6 = "You struggle to resist the lure of Abbathor, but can't hold it at bay. Better to walk the world and sate your greed on non-dwarves."
            DwaSH = [DwaSH1, DwaSH2, DwaSH3, DwaSH4, DwaSH5, DwaSH6]
            DwarvenHook = random.choice(DwaSH)
            DwaQ1 = "Water from the sky! It always surprises you."
            DwaQ2 = "You have a fascination with the ocean and its chaos."
            DwaQ3 = "Any creature larger than a human makes you nervous."
            DwaQ4 = "You prefer to travel with a parasol or similar item that puts a comforting shelter over your head."
            DwaQ5 = "You prefer to sleep during the day."
            DwaQ6 = "You speak Common or any other non-dwarf language only if you must."
            DwaQ7 = "For you, relaxation is putting in a day at the forge."
            DwaQ8 = "You avoid contact with other dwarves, since you mistrust those who would leave their strongholds."
            DwaQ = [DwaQ1, DwaQ2, DwaQ3, DwaQ4, DwaQ5, DwaQ6, DwaQ7, DwaQ8]             
            DwarvenQuirk = random.choice(DwaQ)  
            AdditionalInfo.append(f"As a Dwarf, your Story Hook: {DwarvenHook}")
            AdditionalInfo.append(f"As a Dwarf, your Dwarven Quirk: {DwarvenQuirk}")
        AdditionalInfo.append("As a Dwarf, if the DM allows, you also have Dwarven Fortitude (feat) and Squat Nimbleness (feat).")   
    if race == "Elf":
        if subrace == "High Elf":
            AdditionalInfo.append("As a High Elf, if the DM allows, you also have Fey Teleportation (feat).")
        if subrace == "Wood Elf":
            AdditionalInfo.append("As a Wood Elf, if the DM allows, you also have Wood Elf Magic (feat).")        
        if subrace == "Eladrin":
            ElaSea = ["Spring", "Summer", "Autumn/Fall", "Winter"]
            if param == "Y":
                print("Pick a season of Eladrin? ")
                print("0 - Random")
                print("1 - Spring")
                print("2 - Summer")
                print("3 - Autumn/Fall")
                print("4 - Winter")
                sn = input("Season? ")
                if sn == "1":
                    season = "Spring"
                if sn == "2":
                    season = "Summer"
                if sn == "3":
                    season = "Autumn/Fall"
                if sn == "4":
                    season = "Winter"
                if sn == "0":
                    season = random.choice(ElaSea)
            if param == "N":
                season = random.choice(ElaSea)
            if season == "Spring":
                SpPT1 = "Every day is the greatest day of your life."
                SpPT2 = "You approach everything with enthusiasm, even the most mundane chores."
                SpPT3 = "You love music and song. You supply a tune yourself if no one else can."
                SpPT4 = "You can't stay still."
                SpPT = [SpPT1, SpPT2, SpPT3, SpPT4]
                SpringPT = random.choice(SpPT)
                SpF1 = "You overdrink."
                SpF2 = "Toil is for drudges. Yours should be a life of leisure."
                SpF3 = "A pretty face infatuates you in an instant, but your fancy passes with equal speed."
                SpF4 = "Anything worth doing is worth doing again and again."
                SpF = [SpF1, SpF2, SpF3, SpF4]
                SpringFlaw = random.choice(SpF)
                AdditionalInfo.append(f"Your Spring Personalty Trait: {SpringPT} and your Spring Flaw: {SpringFlaw}")
                if plLvl >= 3:
                    RaceNotes.append("Fey Step(Spring): When you use your Fey Step, you can touch one willing creature within 5 feet of you. That creature then teleports instead of you, appearing in an unoccupied space of your choice that you can see within 30 feet of you.")
            if season == "Summer":
                SuPT1 = "You believe that direct confrontation is the best way to solve problems."
                SuPT2 = "Overwhelming force can accomplish almost anything. The tougher the problem, the more force you apply."
                SuPT3 = "You stand tall and strong so that others can lean on you."
                SuPT4 = "You maintain an intimidating front. It's better to prevent fights with a show of force than to harm others."
                SuPT = [SuPT1, SuPT2, SuPT3, SuPT4]
                SummerPT = random.choice(SuPT)
                SuF1 = "You are stubborn. Let others change."
                SuF2 = "The best option is one that is swift, unexpected, and overwhelming."
                SuF3 = "Punch first. Talk later."
                SuF4 = "Your fury can carry you through anything."
                SuF = [SuF1, SuF2, SuF3, SuF4]
                SummerFlaw = random.choice(SuF)
                AdditionalInfo.append(f"Your Summer Personality Trait: {SummerPT} and your Summer Flaw {SummerFlaw}")
                if plLvl >= 3:
                    RaceNotes.append("Fey Step(Summer): Immediately after you use your Fey Step, each creature of your choice that you can see within 5 feet of you takes fire damage equal to your Charisma modifier (minimum of 1 damage).")
            if season == "Autumn/Fall":
                APT1 = "If someone is in need, you never withhold aid."
                APT2 = "You share what you have, with little regard for your own needs."
                APT3 = "There are no simple meals, only lavish feasts."
                APT4 = "You stock up on fine food and drink. You hate going without such comforts."
                APT = [APT1, APT2, APT3, APT4]
                AutumnPT = random.choice(APT)
                AF1 = "If someone is in need, you never withhold aid."
                AF2 = "You share what you have, with little regard for your own needs."
                AF3 = "There are no simple meals, only lavish feasts."
                AF4 = "You stock up on fine food and drink. You hate going without such comforts."
                AF = [AF1, AF2, AF3, AF4]
                AutumnFlaw = random.choice(AF)
                AdditionalInfo.append(f"Your Autumn Personalty Trait: {AutumnPT} and your Autumn Flaw: {AutumnFlaw}")
                if plLvl >= 3:
                    RaceNotes.append("Fey Step(Autumn/Fall): Immediately after you use your Fey Step, up to two creatures of your choice that you can see within 10 feet of you must succeed on a Wisdom saving throw or be charmed by you for 1 minute, or until you or your companions deal any damage to it.")
            if season == "Winter":
                WPT1 = "The worst case is the most likely to occur."
                WPT2 = "You preserve what you have. Better to be hungry today and have food for tomorrow."
                WPT3 = "Life is full of dangers, but you are ready for them."
                WPT4 = "A penny spent is a penny lost forever."
                WPT = [WPT1, WPT2, WPT3, WPT4] 
                WinterPT = random.choice(WPT)
                WF1 = "Everything dies eventually. Why bother building anything that is supposedly meant to last?"
                WF2 = "Nothing matters to you, and you allow others to guide your actions."
                WF3 = "Your needs come first.  In winter, all must watch out for themselves."
                WF4 = "You speak only to point out the flaws in others' plans."
                WF = [WF1, WF2, WF3, WF4]
                WinterFlaw = random.choice(WF)
                AdditionalInfo.append(f"Your Winter Personality Trait: {WinterPT} and your Winter Flaw: {WinterFlaw}")
                if plLvl >= 3:
                    RaceNotes.append("Fey Step(Winter): When you use your Fey Step, one creature of your choice that you can see within 5 feet of you before you teleport must succeed on a Wisdom saving throw or be frightened of you until the end of your next turn.")
        if subrace != "Dark Elf":
            ElfASH1 = "You believe the key to reuniting the elves with CorelIon lies somewhere in the wider world, not within elven society, and you're determined to find it."
            ElfASH2 = "Your sibling was killed by a rampaging monster. You won't rest until you track it down and slay it."
            ElfASH3 = "A raven brought you a cryptic message from an old friend who needs your help, but the message was vague about the friend's location. You're trying to follow a years-old trail and save your friend."
            ElfASH4 = "A beautiful elf won your heart, then broke it. If you earn enough gold and glory by adventuring, perhaps you can win back your love."
            ElfASH5 = "Your father thought you too weak to survive as an adventurer, but he's wrong, and you'll prove it."
            ElfASH6 = "Only those who perform great deeds are remembered long after their death. Bards will honor your exploits for generations to come."
            ElfASH7 = "You're secretlly in love with one of the other members of your adventuring group, and you can't bear the thought of any harm befalling that person."
            ElfASH8 = "When you were born, your grandmother prophesied you would one day rule a human kingdom. You've gone in search of that destiny."
            ElfASH = [ElfASH1, ElfASH2, ElfASH3, ElfASH4, ElfASH5, ElfASH6, ElfASH7, ElfASH8]
            ElfHook = random.choice(ElfASH)
            AdditionalInfo.append(f"Your Elvish Story Hook: {ElfHook}")
        if subrace == "Dark Elf":
            DrowASH1 = "You overheard members of your own house plotting to poison you, so you fled from the Underdark to save yourself. You won't return until you've amassed enough fortune to surround yourself with loyal mercenary bodyguards."
            DrowASH2 = "You were enslaved as punishment for trying to poison an influential rival, but you escaped and fled to the surface. If you return to the Underdark and are captured,you'll be re-enslaved."
            DrowASH3 = "You were the lover of a high-ranking priestess of Lolth as a means of enhancing your status. When she tired of you, the loss of status was humiliating, so you left."
            DrowASH4 = "You killed a drow from a more powerful house in a duel over a public insult. The slain drow's house vowed to destroy your house unless you were handed over. Your kin urged you to leave the Underdark. You wonder what became of them." 
            DrowASH5 = "A close friend of yours was revealed to be a worshiper of Eilistraee. Suspicion fell on everyone in her circle. Running was a tacit admission of guilt, even though you knew nothing about it, but you'd have been sacrificed to Lolth if you stayed."
            DrowASH6 = "You were among a group of surface raiders that was ambushed, and you were captured. During years of captivity, you learned that most of what Lolth's priestesses taught about the outer world was lies. Now you're experiencing the truth for yourself."
            DrowASH7 = "All your life, you were alienated and terrified by the cruelty of your kin. The first chance you got, you volunteered to go on a surface raid, then deserted the group and remained behind. Now you're hated and feared wherever you go, but at least you've found a small group of adventurous friends who trust and support each other."
            DrowASH8 = "You were part of a delegation carrying diplomatic messages to another drow city when duergar attacked the caravan for slaves and treasure. Only you and one other guard escaped. If you'd returned home, you'd have been poisoned or worse for failure. Becoming a mercenary was your best option."
            DrowASH = [DrowASH1, DrowASH2, DrowASH3, DrowASH4, DrowASH5, DrowASH6, DrowASH7, DrowASH8]
            DrowHook = random.choice(DrowASH)
            DrowSpe1 = "Adamantine weapons"
            DrowSpe2 = "Assassinations"
            DrowSpe3 = "Giant spiders subject to magical control"
            DrowSpe4 = "Hallucinogenic substances"
            DrowSpe5 = "High-status slaves and sacrificial victims"
            DrowSpe6 = "Items taken from surface world in raids"
            DrowSpe7 = "Low-cost, humanoid slaves"
            DrowSpe8 = "Maps of the Underdark"
            DrowSpe9 = "Poisons"
            DrowSpe10 = "Reptilian beasts of burden"
            DrowSpe = [DrowSpe1, DrowSpe2, DrowSpe3, DrowSpe4, DrowSpe5, DrowSpe6, DrowSpe7, DrowSpe8, DrowSpe9, DrowSpe10]
            DrowSpecialty = random.choice(DrowSpe) 
            AdditionalInfo.append(f"Your Drow Story Hook: {DrowHook}")
            AdditionalInfo.append(f"As a Drow, you specialize in: {DrowSpecialty}")
            AdditionalInfo.append("As a Dark Elf, if the DM allows, you also have Drow High Magic (feat).")
        ETrk1 = "A small notebook that causes anything written in it to disappear after 1 hour."
        ETrk2 = "A crystal les nmade of ivory and gold that causes any-thing observed through it to appear to be surrounded by motes of multicolored light."
        ETrk3 = "A small gold pyramid inscribed with elven symbols and about the size of a walnut."
        ETrk4 = "A cloak pin made from enamel in the shape of a butterfly; when you take the pin off, it turns into a real butterfly, and returns when you are ready to put your cloak back on again."
        ETrk5 = "A golden compass that points toward the nearest portal to the Feywild within 10 miles."
        ETrk6 = "A small silver spinning top that, when spun, endlessly spins until interrupted."
        ETrk7 = "A small songbird made of enamel, gold wire, and pre-cious stone; uttering the songbird's name in Elvish causes the trinket to emit that bird's birdsong."
        ETrk8 = "A smallenamel flower that, when put in one's hair, animates, tying back the wearer's hair with a living vine with flowers; plucking a single flower from this vine returns it to its inanimate form."
        ETrk = [ETrk1, ETrk2, ETrk3, ETrk4, ETrk5, ETrk6, ETrk7, ETrk8]
        ElvenTrinket = random.choice(ETrk)  
        EQP.append(ElvenTrinket)  
        AdditionalInfo.append("As an Elf, if the DM allows, you also have Elven Accuracy (feat).")

    if race == "Fairy":
        FaCh1 = "Your wings are like those of a bird."
        FaCh2 = "You have shimmering, multicolored skin."
        FaCh3 = "You have exceptionally large ears."
        FaCh4 = "A glittering mist constantly surrounds you."
        FaCh5 = "You have a small spectral horn on your forehead, like a little unicorn horn."
        FaCh6 = "Your legs are insectile."
        FaCh7 = "You smell like fresh brownies."
        FaCh8 = "A noticeable, harmless chill surrounds you."
        FaCh = [FaCh1, FaCh2, FaCh3, FaCh4, FaCh5, FaCh6, FaCh7, FaCh8]
        FairyChar = random.choice(FaCh)      
        AdditionalInfo.append(f"As a Fairy, your Fairy Characteristic: {FairyChar}")

    if race == "Firbolg":  
        A1 = "Outcast for murder."
        A2 = "Outcast for severely damaging home territory."
        A3 = "Clan slain by invading humanoids."
        A4 = "Clan slain by a dragon or demon."
        A5 = "Separated from the tribe and lost."
        A6 = "Homeland destroyed by natural disaster."
        A7 = "Personal quest ordained by omens."
        A8 = "Dispatched on a quest by tribe leaders."
        Adv = [A1, A2, A3, A4, A5, A6, A7, A8]
        Adve = random.choice(Adv)   
        AdditionalInfo.append(f"Your reason for adventuring: {Adve}")     

    if race == "Gith":        
        if subrace == "Githyanki":
            GithyPT1 = "When I'm bored I make my own excitement, and I'm always bored."
            GithyPT2 = "I treat others as if they were animals that simply don't know any better."
            GithyPT3 = "Violence is a spice that makes life worth living."
            GithyPT4 = "Old age is a concept that Ifind fascinating. Maybe someday I too will be aged."
            GithyPT = [GithyPT1, GithyPT2, GithyPT3, GithyPT4]
            GithyankiPersTrait = random.choice(GithyPT)
            GithyI1 = "Fidelity. Warriors are only as good as the vows they keep."
            GithyI2 = "Power. The weak rule the strong."
            GithyI3 = "Duty. It is by Vlaakith's will alone that I act."
            GithyI4 = "Freedom. No strong soul should be enslaved"
            GithyI = [GithyI1, GithyI2, GithyI3, GithyI4]
            GithyankiIdeal = random.choice(GithyI)
            GithyB1 = "There is no greater duty than to serve the Revered Queen."
            GithyB2 = "Humanity thrives only because we conquered the illithids. Therefore, what is theirs is ours."
            GithyB3 = "Without battle, life has no purpose."
            GithyB4 = "Life is but a spark in the dark. We all go dark, but those who dare can burn bright."
            GithyB = [GithyB1, GithyB2, GithyB3, GithyB4]
            GithyankiBond = random.choice(GithyB)
            GithyF1 = "Hunger and thirst are unbearable pains to me."
            GithyF2 = "I can't see a non-githyanki as a real threat."
            GithyF3 = "I follow orders, regardless of their implications."
            GithyF4 = "I start projects but never finish them."
            GithyF = [GithyF1, GithyF2, GithyF3, GithyF4]
            GithyankiFlaw = random.choice(GithyF)     
            AdditionalInfo.append(f"As a Githyanki, your Personality Trait: {GithyankiPersTrait}")
            AdditionalInfo.append(f"As a Githyanki, your Ideal: {GithyankiIdeal}")
            AdditionalInfo.append(f"As a Githyanki, your Bond: {GithyankiBond}")
            AdditionalInfo.append(f"As a Githyanki, your Flaw: {GithyankiFlaw}")                
        if subrace == "Githzerai":   
            GithzPT1 = "All energy must be expended to a useful end. Frivolity is the first step to defeat."
            GithzPT2 = "Patience in all things. The first step in any venture is the most treacherous."
            GithzPT3 = "Emotions are a trap, meant to weaken the intellect and disturb the nerves. Pay them no heed."
            GithzPT4 = "Begin only thoset asks you will finish. Strike only that which you will kill."
            GithzPT = [GithzPT1, GithzPT2, GithzPT3, GithzPT4]
            GithzeraiPersTrait = random.choice(GithzPT)
            GithzI1 = "Faith. Zerthimon shall return, and I will be worthy to walk beside him."
            GithzI2 = "Courage. The mind can master anything if it is unfettered by fear."
            GithzI3 = "Duty. My people survive only because those like me place their needs above our own."
            GithzI4 = "Freedom. No strong soulshould be enslaved. Better to die first than live as another's puppet."
            GithzI = [GithzI1, GithzI2, GithzI3, GithzI4]
            GithzeraiIdeal = random.choice(GithzI)
            GithzB1 = "Zerthimon provides an example of conduct that I strive to duplicate."
            GithzB2 = "Menyar-Ag hand-picked me for my duties, and I will never betray the trust he showed in me."
            GithzB3 = "Vlaakith and her toadies will be defeated, if not by me then by those who follow in my footsteps."
            GithzB4 = "I will not rest until the last elder brain is destroyed."
            GithzB = [GithzB1, GithzB2, GithzB3, GithzB4]
            GithzeraiBond = random.choice(GithzB)
            GithzF1 = "I see githyanki machinations behind every threat."
            GithzF2 = "I believe in the supremacy of the gith and that githzerai and githyanki will align to rule the multiverse."
            GithzF3 = "I respond to even minor threats with overwhelming displays of force."
            GithzF4 = "The next time I laugh will be the first. The sound of merriment takes me to the edge of violence."
            GithzF = [GithzF1, GithzF2, GithzF3, GithzF4]
            GithzeraiFlaw = random.choice(GithzF)            
            AdditionalInfo.append(f"As a Githzerai, your Personality Trait: {GithzeraiPersTrait}")
            AdditionalInfo.append(f"As a Githzerai, your Ideal: {GithzeraiIdeal}")
            AdditionalInfo.append(f"As a Githzerai, your Bond: {GithzeraiBond}")
            AdditionalInfo.append(f"As a Githzerai, your Flaw: {GithzeraiFlaw}")

    if race == "Gnome":
        GnPT1 = "Once you develop a liking for something, you quickly become obsessed with it."
        GnPT2 = "You live life like aleaf on the breeze, letting it take you where it will."
        GnPT3 = "The world is a miraculous place, and you are fascinated by everything in it."
        GnPT4 = "You study your friends and take notes about how they act, jotting down things they say that interest you."
        GnPT5 = "Your curiosity is so wide-ranging that you sometimes have trouble concentrating on any one thing."
        GnPT6 = "You like to make little objects and creatures out of twigs or bits of metal and give them to friends."
        GnPT = [GnPT1, GnPT2, GnPT3, GnPT4, GnPT5, GnPT6]
        GnomePT = random.choice(GnPT)
        GnI1 = "Love. You love little (and big) critters and go out of your way to help them."
        GnI2 = "Curiosity. You can't stand an unsolved mystery or an unopened door."
        GnI3 = "Knowledge. You are interested in everything. You never know when what you learn will come in handy."
        GnI4 = "Compassion. You never turn down a plea for help."
        GnI5 = "Helpfulness. Whether you see a broken contraption or a broken heart, you have to try to fix it."
        GnI6 = "Excellence. You strive to be and do the best you can."
        GnI = [GnI1, GnI2, GnI3, GnI4, GnI5, GnI6]
        GnomeIdeal = random.choice(GnI) 
        GnB1 = "You pledge to bring something of immense value back to your burrow."
        GnB2 = "Anything of great quality and artisanship is to be protected, respected, and cared for."
        GnB3 = "Kobolds have caused you and your people nothing but trouble. You will avenge those wrongs."
        GnB4 = "You are searching for your lost love."
        GnB5 = "You will recover a keepsake stolen from your clan."
        GnB6 = "You are willing to take risks to learn about the world."
        GnB = [GnB1, GnB2, GnB3, GnB4, GnB5, GnB6]
        GnomeBond = random.choice(GnB) 
        GnF1 = "You embody the typical absent-minded professor. If you could forget where you put your head, you would."
        GnF2 = "You prefer to hide during a fight."
        GnF3 = "There is no difference between what you think and what you say."
        GnF4 = "You can't keep a secret."
        GnF = [GnF1, GnF2, GnF3, GnF4]
        GnomeFlaw = random.choice(GnF)       
        AdditionalInfo.append(f"As a Gnome, your Personality Trait: {GnomePT}")
        AdditionalInfo.append(f"As a Gnome, your Ideal: {GnomeIdeal}")
        AdditionalInfo.append(f"As a Gnome, your Bond: {GnomeBond}")
        AdditionalInfo.append(f"As a Gnome, your Flaw: {GnomeFlaw}")         
        AdditionalInfo.append("As a Gnome, if the DM allows, you also have Fade Away (feat) and Squat Nimbleness (feat).")
        if subrace == "Svirfneblin (Deep) Gnome":
            AdditionalInfo.append("As a Deep Gnome, if the DM allows, you also optionally have Swirfneblin Magic (feat)")

    if race == "Half-Elf":
        AdditionalInfo.append("As a Half-Elf, if the DM allows, you also have Elven Accuracy (feat) and Prodigy (feat).")

    if race == "Half-Orc":
        AdditionalInfo.append("As a Half-Orc, if the DM allows, you also have Orcish Fury (feat) and Prodigy (feat).")

    if race == "Halfling":
        AdditionalInfo.append("As a Halfling, if the DM allows, you also have Bountiful Luck (feat), Second Change (feat) and Squat Nimbleness (feat).")

    if race == "Human":
        AdditionalInfo.append("As a Human, if the DM allows, you also have Prodigy (feat).")

    if race == "Leonin":
        LeonGods1 = "I'm amused by the antics of the gods and their earnest, but ultimately deluded, mortal champions, and I feel smugly superior in my detachment."
        LeonGods2 = "The meddling of the gods in mortal affairs makes me angry and bitter. I wish they would just leave us all alone!"
        LeonGods3 = "I view the gods as worthy adversaries-incredibly clever and well-prepared to play a long game but ultimately doomed to lose their games."
        LeonGods4 = "I'm certain every bad thing that happens can ultimately be blamed on the gods, but I roll my eyes at each new twist of fate and try to get on with my life."
        LeonGods5 = "I wish that I could be as naive as humans and other mortals who actually think the gods are looking out for them. I miss that kind of innocence."
        LeonGods6 = "I don't talk about it among other leonin, but I actually revere the gods and try to please them by my actions."
        LeonGods = [LeonGods1, LeonGods2, LeonGods3, LeonGods4, LeonGods5, LeonGods6]
        LeoninGods = random.choice(LeonGods)
        AdditionalInfo.append(f"As a Leonin, your relationship with the Gods: {LeoninGods}")

    if race == "Lizardfolk":
        LQ1 = "You hate waste and see no reason not to scavenge fallen enemies. Fingers are tasty and portable!"
        LQ2 = "You sleep best while mostly submerged in water."
        LQ3 = "Money is meaningless to you."
        LQ4 = "You think there are only two species of humanoid: lizardfolk and meat."
        LQ5 = "You have learned to laugh. You use this talent in response to all emotional situations, to better fit in with your comrades."
        LQ6 = "You still don't understand how metaphors work. That doesn't stop you from using them at every opportunity."
        LQ7 = "You appreciate the soft humanoids who realize they need chain mail and swords to match the gifts you were born with."
        LQ8 = "You enjoy eating your food while it's still wriggling."
        LQ = [LQ1, LQ2, LQ3, LQ4, LQ5, LQ6, LQ7, LQ8]
        LizQui = random.choice(LQ)        
        AdditionalInfo.append(f"Your Lizardfolk Quirk: {LizQui}")

    if race == "Minotaur":
        MinoNameSa1 = "My namesake defeated a massive enemy."
        MinoNameSa2 = "My namesake was known for fierce devotion to a god."
        MinoNameSa3 = "My namesake was a respected leader of other warriors."
        MinoNameSa4 = "My namesake ran the entire breadth of Phoberos in order to warn the minotaurs of an Akroan attack."
        MinoNameSa5 = "My namesake was famous for great magical ability."
        MinoNameSa6 = "My namesake was a hero's devoted companion."
        MinoNameSa7 = "My namesake is remembered for incredible generosity."
        MinoNameSa8 = "My namesake was a great oracle."
        MinoNameSa = [MinoNameSa1, MinoNameSa2, MinoNameSa3, MinoNameSa4, MinoNameSa5, MinoNameSa6, MinoNameSa7, MinoNameSa8]
        MinotaurNamesake = random.choice(MinoNameSa)
        AdditionalInfo.append(f"As a Minotaur, your namesake: {MinotaurNamesake}")     

    if race == "Satyr":   
        SatEcc1 = "Flowers are the most amazing things ever. I want to pick them, wear them, and discover their silent secrets."
        SatEcc2 = "There isn't a tree or statue that isn't fun to climb."
        SatEcc3 = "Nothing wards off bad luck like a jolly dance."
        SatEcc4 = "Sometimes talking to a plant really helps."
        SatEcc5 = "If stumped, I smoke a pipe. And if I'm going to smoke a pipe, it's going to be a splendid pipe."
        SatEcc6 = "I imagine that my clothes are my glorious soul on display for all the world to behold, and I dress accordingly."
        SatEcc7 = "Having horns is the best. They are fun to decorate, and they can pop open an amphora, no problem."
        SatEcc8 = "If I have something really important to say, I always make sure to sing it."
        SatEcc = [SatEcc1, SatEcc2, SatEcc3, SatEcc4, SatEcc5, SatEcc6, SatEcc7, SatEcc8]
        SatyrEccentricities = random.choice(SatEcc)
        AdditionalInfo.append(f"As a Satyr, you have certain Eccentricities, which are: {SatyrEccentricities}")  

    if race == "Shifter":
        LycAn1 = "Werebear"
        LycAn2 = "Wereboar"
        LycAn3 = "Wererat"
        LycAn4 = "Weretiger"
        LycAn5 = "Werewolf (wolflike)"
        LycAn6 = "Werewolf (doglike)"
        LycAn = [LycAn1, LycAn2, LycAn3, LycAn4, LycAn5, LycAn6]
        LycanAnces = random.choice(LycAn)        
        AdditionalInfo.append(f"As a Shifter, your Lycanthrope Ancestor: {LycanAnces}")

    if race == "Tabaxi":
        TO1 = "A god or planar entity"
        TO2 = "A monster"
        TO3 = "A lost civilization"
        TO4 = "A wizard's secrets"
        TO5 = "A mundane item"
        TO6 = "A magic item"
        TO7 = "A location"
        TO8 = "A legend or tale"
        TO = [TO1, TO2, TO3, TO4, TO5, TO6, TO7, TO8]
        TabObs = random.choice(TO)
        TaQ1 = "You miss your tropical home and complain endlessly about the freezing weather, even in summer."
        TaQ2 = "You never wear the same outfit twice, unless you absolutely must."
        TaQ3 = "You have a minor phobia of water and hate getting wet."
        TaQ4 = "Your tail always betrays your inner thoughts."
        TaQ5 = "You purr loudly when you are happy."
        TaQ6 = "You keep a small ball of yarn in your hand, which you constantly fidget with."
        TaQ7 = "You are always in debt, since you spend your gold on lavish parties and gifts for friends."
        TaQ8 = "When talking about something you're obsessed with, you speak quickly and never pause and others can't understand you."
        TaQ9 = "You are a font of random trivia from the lore and stories you have discovered."
        TaQ10 = "You can't help but pocket interesting objects you come across."
        TaQ = [TaQ1, TaQ2, TaQ3, TaQ4, TaQ5, TaQ6, TaQ7, TaQ8, TaQ9, TaQ10]
        TabQui = random.choice(TaQ)    
        AdditionalInfo.append(f"Your obsession as a Tabaxi: {TabObs}")
        AdditionalInfo.append(f"Your quirk as a Tabaxi: {TabQui}")            

    if race == "Tiefling":
        AdditionalInfo.append("As a Tiefling, if the DM allows, you also have Flames of Phlegethos (feat) and Infernal Constitution (feat).")

    if race == "Triton":
        TrQ1 = "You phrase requests as orders that you expect to be obeyed."
        TrQ2 = "You are quick to boast of the greatness of your civilization."
        TrQ3 = "You learned an antiquated version of Common and drop 'thee' and 'thou' into your speech."
        TrQ4 = "You assume that people are telling you the truth about local customs and expectations."
        TrQ5 = "The surface world is a wondrous place, and you catalog all its details in a journal."
        TrQ6 = "You mistakenly assume that surface folk know about and are impressed by your people's history."
        TrQ = [TrQ1, TrQ2, TrQ3, TrQ4, TrQ5, TrQ6]
        TriQui = random.choice(TrQ)
        AdditionalInfo.append(f"Your Triton Quirk: {TriQui}")

    if race == "Warforged":      
        WarfQ1 = "You analyze-out loud-the potential threat posed by every creature you meet."
        WarfQ2 = "You often misread emotional cues."
        WarfQ3 = "You are fiercely protective of your friends."
        WarfQ4 = "You try to apply wartime discipline to every situation."
        WarfQ5 = "You don't know how to filter your feelings and are prone to dramatic emotional outbursts."
        WarfQ6 = "You don't understand clothing beyond its utility and assume it denotes a person's function."
        WarfQ7 = "You are obsessed with your appearance and constantly polish and buff yourself."
        WarfQ8 = "War is the only thing that makes sense to you, and you're always looking for a fight."
        WarfQ = [WarfQ1, WarfQ2, WarfQ3, WarfQ4, WarfQ5, WarfQ6, WarfQ7, WarfQ8]
        WarforgedQuirk = random.choice(WarfQ)
        AdditionalInfo.append(f"As a Warforged, your quirk: {WarforgedQuirk}")    

    if ((race != "Dhampir") and (race != "Hexblood") and (race != "Reborn")):
        if Lineage == "Dhampir":
            DhaHun1 = "Blood"
            DhaHun2 = "Flesh or raw meat"
            DhaHun3 = "Cerebral spinal fluid"
            DhaHun4 = "Psychic energy"
            DhaHun5 = "Dreams"
            DhaHun6 = "Life energy"
            DhaHun = [DhaHun1, DhaHun2, DhaHun3, DhaHun4, DhaHun5, DhaHun6]
            DhampirHunger = random.choice(DhaHun)
            DhaOr1 = "You are the reincarnation of an ancestor who was a vampiric tyrant."
            DhaOr2 = "Your pact with a predatory deity, end, fey, or spirit causes you to share their hunger."
            DhaOr3 = "You survived being attacked by a vampire but were forever changed."
            DhaOr4 = "A parasite lives inside you. You indulge its hunger."
            DhaOr5 = "Tragedy interrupted your transformation into an immortal."
            DhaOr6 = "You are a diminished form of an otherworldly being. Slaking your hunger hastens your renewal."
            DhaOr7 = "One of your parents was a vampire."
            DhaOr8 = "A radical experiment changed your body, making you reliant on others for vital fluids."
            DhaOr = [DhaOr1, DhaOr2, DhaOr3, DhaOr4, DhaOr5, DhaOr6, DhaOr7, DhaOr8]
            DhampirOrigin = random.choice(DhaOr)             
            SkillsProf = skillprof2(param, SkillsProf)
            AdditionalInfo.append(f"You are a Dhampir in addition to being a(n) {race}, and thus have the Dhampir Hunger for {DhampirHunger}")
            AdditionalInfo.append(f"You also have the Dhampir Origin of: {DhampirOrigin}")
            RaceNotes.append("Ancestral Legacy (see notes)")
            Notes.append("Ancestral Legacy: If you replace a race with this lineage, you can keep the following elements of that race: any skill proficiencies you gained from it and any climbing, flying, or swimming speed you gained from it.\nIf you don’t keep any of those elements or you choose this lineage at character creation, you gain proficiency in two skills of your choice.")
        if Lineage == "Hexblood":
            HexO1 = "Seeking a child, your parent made a bargain with a hag. You are the result of that arrangement."
            HexO2 = "Fey kidnappers swapped you and your parents’ child."
            HexO3 = "A coven of hags lost one of its members. You were created to replace the lost hag."
            HexO4 = "You were cursed as a child. A deal with the spirits of the forest transformed you into a hexblood, now free of the curse."
            HexO5 = "You began life as a fey creature, but an accident changed you and forced you from your home."
            HexO6 = "A slighted druid transformed you and bound you to live only so long as a sacred tree bears fruit."
            HexO = [HexO1, HexO2, HexO3, HexO4, HexO5, HexO6]
            HexbloodOrigin = random.choice(HexO)            
            SkillsProf = skillprof2(param, SkillsProf)
            AdditionalInfo.append(f"You are a Hexblood in addition to being a(n) {race}, and thus have the Heblood Origin of {HexbloodOrigin}")
            RaceNotes.append("Ancestral Legacy (see notes)")
            Notes.append("Ancestral Legacy: If you replace a race with this lineage, you can keep the following elements of that race: any skill proficiencies you gained from it and any climbing, flying, or swimming speed you gained from it.\nIf you don’t keep any of those elements or you choose this lineage at character creation, you gain proficiency in two skills of your choice.")
        if Lineage == "Reborn":
            RebLoMe1 = "You recall a physically painful moment. What mark or scar on your body does it relate to?"
            RebLoMe2 = "A memory brings tears to your eyes. Is it a bitter or cheerful memory? Does recalling it make you feel the same way?"
            RebLoMe3 = "You recall a childhood memory. What about that event or who you were still inuences you?"
            RebLoMe4 = "A memory brings with it the voice of someone once close to you. How do they advise you?"
            RebLoMe5 = "You recall enjoying something that you can’t stand doing now. What is it? Why don’t you like it now?"
            RebLoMe6 = "A memory carries a vivid smell or sensation. What are you going to do to recreate that experience?"
            RebLoMe = [RebLoMe1, RebLoMe2, RebLoMe3, RebLoMe4, RebLoMe5, RebLoMe6]
            RebornLostMemories = random.choice(RebLoMe)
            RebO1 = "You were magically resurrected, but something went wrong."
            RebO2 = "Stitches bind your body’s mismatched pieces, and your memories come from multiple different lives."
            RebO3 = "After clawing free from your grave, you realized you have no memories except for a single name."
            RebO4 = "You were a necromancer’s undead servant for years. One day, your consciousness returned."
            RebO5 = "You awoke in an abandoned laboratory alongside complex designs for clockwork organs."
            RebO6 = "You were released after being petried for generations. Your memories have faded, though, and your body isn’t what it once was."
            RebO7 = "Your body hosts a possessing spirit that shares its memories and replaces your missing appendages with phantasmal limbs."
            RebO8 = "In public, you pass as an unremarkable individual, but you can feel the itchy straw stung inside you."
            RebO = [RebO1, RebO2, RebO3, RebO4, RebO5, RebO6, RebO7, RebO8]
            RebornOrigin = random.choice(RebO)             
            AdditionalInfo.append(f"You are a Reborn in addition to being a(n) {race}, and thus have Lost Memories of: {RebornLostMemories}")
            AdditionalInfo.append(f"You also have the Reborn Origin of: {RebornOrigin}")
            RaceNotes.append("Ancestal Legacy (see notes)")
            Notes.append("Ancestral Legacy: If you replace a race with this lineage, you can keep the following elements of that race: any skill proficiencies you gained from it and any climbing, flying, or swimming speed you gained from it.\nIf you don’t keep any of those elements or you choose this lineage at character creation, you gain proficiency in two skills of your choice.")
            SkillsProf = skillprof2(param, SkillsProf)         

########################################################################################################
    AlchSupp = "Alchemist's Supplies"
    BrewSupp = "Brewer's Supplies"
    CallSupp = "Calligrapher's Supplies"
    CarpTools = "Carpenter's Tools"
    CartTools = "Cartographer's Tools"
    CobbTools = "Cobbler's Tools"
    CooksUten = "Cook's Utensils"
    GlasTools = "Glassblower's Tools"
    JeweTools = "Jeweler's Tools"
    LthrwrkTools = "Leatherworker's Tools"
    MasnTools = "Mason's Tools"
    PaintSupp = "Painter's Supplies"
    PottTools = "Potter's Tools"
    SmthTools = "Smith's Tools"
    TinkTools = "Tinker's Tools"
    WeavTools = "Weaver's Tools"
    WdcrvTools = "Woodcarver's Tools"
    DisgKit = "Disguise Kit"
    ForgKit = "Forgery Kit"
    HerbKit = "Herbalism Kit"
    NavTools = "Navigator's Tools"
    PoisKit = "Poisoner's Kit"
    ThievKit = "Thieves' Tools"    
    VehLand = "Vehicles (Land)"
    VehSea = "Vehicles (Sea)"
    VehSpace = "Vehicles (Space)"   
    DiceSet = "Dice Set"
    DrgnChSet = "Dragonchess Set"
    PlyCrdSet = "Playing Card Set"
    ThrDgnASet = "Three-Dragon Ante Set"
    GamingSets = [DiceSet, DrgnChSet, PlyCrdSet, ThrDgnASet]
    GSrand = random.choice(GamingSets)     
    Bagpipes = "Bagpipes"
    Birdpipes = "Birdpipes"
    Drum = "Drum"
    Dulcimer = "Dulcimer"
    Flute = "Flute"
    Glaur = "Glaur"
    HndDrum = "Hand Drum"
    Horn = "Horn"
    Longhorn = "Longhorn"
    Lute = "Lute"
    Lyre = "Lyre"
    PFlute = "Pan Flute"
    Shawm = "Shawm"
    Songhorn = "Songhorn"
    Tantan = "Tantan"
    Thelarr = "Thelarr"
    Viol = "Viol"
    Wargong = "Wargong"
    Yarting = "Yarting"
    Zulkoon = "Zulkoon"
    MusicalInstruments = [Bagpipes, Birdpipes, Drum, Dulcimer, Flute, Glaur, HndDrum, Horn, Longhorn, Lute, Lyre, PFlute, Shawm, Songhorn, Tantan, Thelarr, Viol, Wargong, Yarting, Zulkoon]
    MusicalInstrumentsRand = random.choice(MusicalInstruments)    
    
    OtherBackgroundInfo = []
    AdditionalInfo = []
    AlliesOrg = []
    if back == "Acolyte":
        AdditionalInfo.append("Feature: Shelter of the Faithful (see notes)")
        Notes.append("Feature: Shelter of the Faithful - As an acolyte, you command the respect of those who share your faith, and you can perform the religious ceremonies of your deity. You and your adventuring companions can expect to receive free healing and care at a temple, shrine, or other established presence of your faith, though you must provide any material components needed for spells. Those who share your religion will support you (but only you) at a modest lifestyle.\nYou might also have ties to a specific temple dedicated to your chosen deity or pantheon, and you have a residence there. This could be the temple where you used to serve, if you remain on good terms with it, or a temple where you have found a new home. While near your temple, you can call upon the priests for assistance, provided the assistance you ask for is not hazardous and you remain in good standing with your temple.")
    if back == "Anthropologist":
        AdditionalInfo.append("Feature: Cultural Chameleon (see notes)")
        Notes.append("Feature: Cultural Chameleon - Before becoming an adventurer, you spent much of your adult life away from your homeland, living among people different from your kin. You came to understand these foreign cultures and the ways of their people, who eventually treated you as one of their own. One culture had more of an influence on you than any other, shaping your beliefs and customs. Choose a race whose culture you've adopted.")
        AdditionalInfo.append("Feature: Adept Linguist (see notes)")
        Notes.append("Feature: Adept Linguist - You can communicate with humanoids who don't speak any language you know. You must observe the humanoids interacting with one another for at least 1 day, after which you learn a handful of important words, expressions, and gestures – enough to communicate on a rudimentary level.")        
    if back == "Archaeologist":
        ArchSI1 = "10-foot pole"
        ArchSI2 = "Medallion"
        ArchSI3 = "Crowbar"
        ArchSI4 = "Shovel"
        ArchSI5 = "Hat"
        ArchSI6 = "Sledgehammer"
        ArchSI7 = "Hooded lantern"
        ArchSI8 = "Whip"
        ArchSI = [ArchSI1, ArchSI2, ArchSI3, ArchSI4, ArchSI5, ArchSI6, ArchSI7, ArchSI8]
        ArchaeSigItem = random.choice(ArchSI)
        EQP.append(ArchaeSigItem)
        AdditionalInfo.append(f"Feature: Dust Digger - Prior to becoming an adventurer, you spent most of your young life crawling around in the dust, pilfering relics of questionable value from crypts and ruins. Though you managed to sell a few of your discoveries and earn enough coin to buy proper adventuring gear, you have held onto an item that has great emotional value to you.\nThat item being {ArchaeSigItem}")    
        AdditionalInfo.append("Feature: Historical Knowledge (see notes)")
        Notes.append("Feature: Historical Knowledge - When you enter a ruin or dungeon, you can correctly ascertain its original purpose and determine its builders, whether those were dwarves, elves, humans, yuan-ti, or some other known race. In addition, you can determine the monetary value of art objects more than a century old.")
    if back == "Ashari":
        AdditionalInfo.append("Feature: Elemental Harmony (see notes)")
        Notes.append("Feature: Elemental Harmony - Growing up surrounded by wild elemental magics has attuned your senses to those chaotic forces, enabling you to subtly bend them to your will. As an action, you channel minor magic involving the element of your chosen Ashari order, giving you one of the following abilities:\nPyrah. You instantaneously create and control a burst of flame small enough to light a candle, a torch, or a small campfire. Alternatively, you snuff out a flame of the same size.\nTerrah. You instantaneously create a small rock no larger than a gold coin. The rock appears in your hand, then turns to dust after 1 minute.\nVesrah. You instantaneously create enough hot or cold water to fill a small drinking vessel.\nZephrah. You create an instantaneous puff of wind strong enough to blow papers off a desk or mess up someone's hair.")
    if back == "Astral Drifter":
        AsDrDC1 = "Corellon, god of art and magic (chaotic good)"
        AsDrDC2 = "Tymora, god of good fortune (chaotic good)"
        AsDrDC3 = "FhaPlLanghn, god of horizons and travel (neutral good)"
        AsDrDC4 = "Istus, god of fate and destiny (neutral)"
        AsDrDC5 = "Nuada, god of war and warriors (neutral)"
        AsDrDC6 = "Zivilyn, god of wisdom (neutral)"
        AsDrDC7 = "Arawn, god of life and death (neutral evil)"
        AsDrDC8 = "Hecate, god of magic and moons (chaotic evil)"
        AsDrDC9 = "Celestian, god of stars and wanderers (neutral)"
        AsDrDC10 = "Ptah, god of knowledge and secrets (lawful neutral)"
        AsDrDC = [AsDrDC1, AsDrDC2, AsDrDC3, AsDrDC4, AsDrDC5, AsDrDC6, AsDrDC7, AsDrDC8, AsDrDC9, AsDrDC10]
        AstralDrifDivCont = random.choice(AsDrDC)
        AdditionalInfo.append("Longevity - You are 20d6 years older than you look, because you have spent that much time in the Astral Sea without aging.")
        AdditionalInfo.append(f"Feature: Divine Contact - You gain the Magic Initiate feat from the Player's Handbook and must choose cleric for the feat.\nIn the Astral Sea, you crossed paths with a wandering deity. The encounter was brief and nonviolent, yet it made a lasting impression on you. This deity saw fit to share one secret or obscure bit of cosmic lore with you. Work with your DM to determine the details of this knowledge and its impact on the campaign\nThat contact being {AstralDrifDivCont}.")
    if back == "Athlete":
        AthFavEv1 = "Marathon"
        AthFavEv2 = "Long-distance running"
        AthFavEv3 = "Wrestling"
        AthFavEv4 = "Boxing"
        AthFavEv5 = "Chariot or horse race"
        AthFavEv6 = "Pankration (mixed unarmed combat)"
        AthFavEv7 = "Hoplite race (racing in full armor with a unit)"
        AthFavEv8 = "Pentathlon (running, long jump, discus, javelin, wrestling)"
        AthFavEv = [AthFavEv1, AthFavEv2, AthFavEv3, AthFavEv4, AthFavEv5, AthFavEv6, AthFavEv7, AthFavEv8]
        AthleteFavoriteEvent = random.choice(AthFavEv)    
        AdditionalInfo.append(f"Favored Event - While many athletes practice various games and events, most excel at a single form of competition.\nYou excel in {AthleteFavoriteEvent}.")
        AdditionalInfo.append("Feature: Echoes of Victory (see notes)")
        Notes.append("Feature: Echoes of Victory - You have attracted admiration among spectators, fellow athletes, and trainers in the region that hosted your past athletic victories. When visiting any settlement within 100 miles of where you grew up, there is a 50 percent chance you can find someone there who admires you and is willing to provide information or temporary shelter.\nBetween adventures, you might compete in athletic events sufficient enough to maintain a comfortable lifestyle, as per the 'Practicing a Profession' downtime activity in chapter 8 of the Player's Handbook.")
    if back == "Azorius Functionary":
        AdditionalInfo.append("Feature: Legal Authority (see notes)")
        Notes.append("Feature: Legal Authority - You have the authority to enforce the laws of Ravnica, and that status inspires a certain amount of respect and even fear in the populace. People mind their manners in your presence and avoid drawing your attention; they assume you have the right to be wherever you are. Showing your Azorius insignia gets you an audience with anyone you want to talk to (though it might cause more problems than it solves when you're dealing with incorrigible lawbreakers). If you abuse this privilege, though, you can get in serious trouble with your superiors and even be stripped of your position.")
        AlliesOrg.append("Azorius Guild Spells\nPrerequisite: Spellcasting or Pact Magic class feature\nFor you, the spells on the Azorius Guild Spells table are added to the spell list of your spellcasting class. (If you are a multiclass character with multiple spell lists, these spells are added to all of them.)\nCantrip: Friends, Message\n1st: Command, Ensnaring Strike\n2nd: Arcane Lock, Calm Emotions, Hold Person\n3rd: Clairvoyance, Counterspell\n4th: Compulsion, Divination\n5th: Dominate Person\nYour magic often takes the form of blue or golden runes floating and glowing in the air in circular patterns or of shimmering azure barriers of magical energy.")
        AzFuAzC1 = "As a teenager, I was a page for a prominent judge."
        AzFuAzC2 = "One of my childhood friends is now a precognitive mage in service of the guild."
        AzFuAzC3 = "I joined the Azorius hoping to impress an arrester whom I admire."
        AzFuAzC4 = "My former mentor is now a warden at Udzec, the new Azorius prison."
        AzFuAzC5 = "I was second best at everything in my legal training, and now I work with the person who was always just a little bit better."
        AzFuAzC6 = "A good friend was promoted into work they can't tell me about."
        AzFuAzC7 = "I know a homunculus in the halls of New Prahv who can get things done behind the scenes."
        AzFuAzC8 = "I was once summoned to the presence of Supreme Judge Isperia, the guildmaster of the Azorius, who complimented me on my work."
        AzFuAzC = [AzFuAzC1, AzFuAzC2, AzFuAzC3, AzFuAzC4, AzFuAzC5, AzFuAzC6, AzFuAzC7, AzFuAzC8]
        AzoriusFuncAzoriusCont1 = random.choice(AzFuAzC)
        AzFuAzC.remove(AzoriusFuncAzoriusCont1)
        randAzFuC = False
        while not randAzFuC:
            try:
                AzoriusFuncAzoriusCont2 = random.choice(AzFuAzC)
                randAzFuC = True
            except IndexError:
                AzoriusFuncAzoriusCont2 = random.choice(AzFuAzC)
        AzFuNAC1 = "Roll an additional Azorius contact; you can decide if the contact is an ally or a rival."
        AzFuNAC2 = "The person who recruited me into the Azorius left and joined the Boros."
        AzFuNAC3 = "I have a friendship with a Dimir agent who sometimes funnels me secrets about Azorius activities."
        AzFuNAC4 = "A Golgari spore druid would love to see me slip up and break the law."
        AzFuNAC5 = "A lesser Gruul chieftain seems to think I could be useful."
        AzFuNAC6 = "The black sheep of my family is putting their maniacal genius to use in the Izzet."
        AzFuNAC7 = "I'm friends with an Orzhov advokist; we compare notes on different forms of law magic."
        AzFuNAC8 = "I was ridiculed once in a Rakdos performance; the performer was impressed with my good humor about it and now does me occasional favors."
        AzFuNAC9 = "I have a fanatical Selesnya cousin who keeps trying to recruit me and everyone else in the family."
        AzFuNAC10 = "While growing up, I was bullied by a brat who's now a hybrid in the Simic Combine."
        AzFuNAC = [AzFuNAC1, AzFuNAC2, AzFuNAC3, AzFuNAC4, AzFuNAC5, AzFuNAC6, AzFuNAC7, AzFuNAC8, AzFuNAC9, AzFuNAC10]
        AzoriusFuncNonAzoriusCont = random.choice(AzFuNAC)
        AlliesOrg.append(f"Your Azorius Contact Ally: {AzoriusFuncAzoriusCont1}")
        AlliesOrg.append(f"Your Azorius Contact Rival: {AzoriusFuncAzoriusCont2}")
        AlliesOrg.append(f"Your Non-Azorius Contact: {AzoriusFuncNonAzoriusCont}")        
    if back == "Bandit Defector":
        BanSp1 = "Lookout"
        BanSp2 = "Lifter"
        BanSp3 = "Thug"
        BanSp4 = "Runner"
        BanSp5 = "Hustler"
        BanSp6 = "Captain"
        BanSp = [BanSp1,  BanSp2, BanSp3, BanSp4, BanSp5, BanSp6]
        BanditDefSpec = random.choice(BanSp)   
        AdditionalInfo.append(f"Bandit Specialty - The Bandit Coalition is a rather loose organization of rogues and brigands, but there is still a degree of specialization within the ranks. This ensures that everyone knows what their job is and lessens confusion in the heat of a robbery. Your bandit specialty is {BanditDefSpec}.\nLookouts typically watch the roads for any signs of Perch Guard patrols, signalling the team to bail if a heist looks too risky. They also keep an eye out for potential marks.\nLifters are the specialist thieves of an operation. They are usually as adept at pick-pocketing as they are at sneaking up behind a cart to liberate its valuables.\nThugs are the muscle of a bandit group, and use their size and strength to intimidate merchants into giving up without a fight. They also keep other bandits in line, at the captain’s discretion.\nRunners are the messengers and scouts of the Coalition, serving to smuggle pilfered goods to fences. Additionally, they pass information throughout the different camps of the organization. Their job often finds them working alone which makes them particularly vulnerable.\nHustlers are inveterate con-artists. Through careful planning and execution, their diversions can keep cart drivers occupied just long enough for the lifters to do their work, or create a seamless opening for an ambush.\nCaptains are the glue that holds each bandit team together, providing leadership, and stamping out dissention where necessary, often with force. They are figures that inspire with their skill and bravado.")
        AdditionalInfo.append("Feature: Bandit Routes (see notes)")
        Notes.append("Feature: Bandit Routes - As someone who once assisted in countless highway robberies, you are familiar with the roads of the Wood and escape paths used by bandits. When you are not in combat, you (and companions you lead) can travel between locations that cut through forested areas twice as fast as your speed would normally allow.")
    if back == "Boros Legionnaire":             
        BoLgC1 = "A former comrade in arms was promoted into the prestigious Sunhome Guard."
        BoLgC2 = "One of my parents is a ranking Boros officer."
        BoLgC3 = "A close friend serves aboard the Parhelion 11, a flying fortress."
        BoLgC4 = "I had a tangled affair with a Boros garrison captain."
        BoLgC5 = "I have maintained a relationship with one of my instructors at Horizon Military Academy."
        BoLgC6 = "I competed with a fellow student for the attention of a mentor at Horizon Military Academy."
        BoLgC7 = "The person who recruited me into the legion changed the course of my life."
        BoLgC8 = "A Boros angel knows my name."
        BoLgC = [BoLgC1, BoLgC2, BoLgC3, BoLgC4, BoLgC5, BoLgC6, BoLgC7, BoLgC8]
        BorosLegonCont1 = random.choice(BoLgC)
        BoLgC.remove(BorosLegonCont1)
        randBorosLegonCont2 = False
        while not randBorosLegonCont2:
            try:
                BorosLegonCont2 = random.choice(BoLgC)
                randBorosLegonCont2 = True
            except IndexError:
                BorosLegonCont2 = random.choice(BoLgC)        
        BoLgNonC1 = "One of my siblings is an Azorius arrester."
        BoLgNonC2 = "Roll an additional Boros contact; you can decide if the contact is an ally or a rival."
        BoLgNonC3 = "I showed mercy to an injured, now-grateful Dimir spy."
        BoLgNonC4 = "I suspect someone I know is a Golgari assassin, but I can't prove it."
        BoLgNonC5 = "An adolescent relative ran off to join the Gruul in an act of rebellion and has not yet returned."
        BoLgNonC6 = "I once befriended an Izzet scientist, and we're still cordial though the relationship ended messily."
        BoLgNonC7 = "I owe a monetary debt to an Orzhov syndic."
        BoLgNonC8 = "A Rakdos blood witch seems to enjoy harassing me."
        BoLgNonC9 = "I tried to recruit a friend who ended up joining the Selesnya."
        BoLgNonC10 = "I keep running into a particular Simic biomancer, and I enjoy the arguments that inevitably result."
        BoLgNonC = [BoLgNonC1, BoLgNonC2, BoLgNonC3, BoLgNonC4, BoLgNonC5, BoLgNonC6, BoLgNonC7, BoLgNonC8, BoLgNonC9, BoLgNonC10]
        BorosLegonNonCont = random.choice(BoLgNonC)        
        AlliesOrg.append(f"Your Boros Contact Ally: {BorosLegonCont1}")
        AlliesOrg.append(f"Your Boros Contact Rival: {BorosLegonCont2}")
        AlliesOrg.append(f"Your Non-Boros Contact: {BorosLegonNonCont}")
        AdditionalInfo.append("Feature: Legion Station (see notes)")
        Notes.append("Feature: Legion Station - You have an established place in the hierarchy of the Boros Legion. You can requisition simple equipment for temporary use, and you can gain access to any Boros garrison in Ravnica, where you can rest in safety and receive the attention of medics. You are also paid a salary of 1 gp (a Boros-minted 1-zino coin) per week, which (combined with free lodging in your garrison) enables you to maintain a poor lifestyle between adventures.")  
        AlliesOrg.append("Boros Guild Spells\nPrerequisite: Spellcasting or Pact Magic class feature\nFor you, the spells on the Boros Guild Spells table are added to the spell list of your spellcasting class.\nCantrip: Fire Bolt, Sacred Flame\n1st: Guiding Bolt, Heroism\n2nd: Aid, Scorching Ray\n3rd: Beacon of Hope, Blinding Smite\n4th: Death Ward, Wall of Fire\n5th: Flame Strike\nYour magic often features dramatic bursts of flame or radiance. When you cast beneficial spells on your allies, they appear momentarily surrounded with halos of bright fire.")
    if back == "Celebrity Adventurer's Scion":
        AdditionalInfo.append("Feature: Name Dropping (see notes)")
        Notes.append("Feature: Name Dropping - You know and have met any number of powerful people across the land—and some of them might even remember you. You might be able to wrangle minor assistance from a major figure in the campaign, at the DM's discretion. Additionally, the common folk treat you with deference, and your heritage and the stories you tell might be good for a free meal or a place to sleep.")
    if back == "Charlatan":
        S1 = "I cheat at games of chance."
        S2 = "I shave coins or forge documents."
        S3 = "I insinuate myself into people is lives to prey on their weaknesses, and secure their fortunes."
        S4 = "I put on new identities like clothes."
        S5 = "I run sleight-of-hand cons on street corners."
        S6 = "I convince people that worthless junk is worth their hard-earned money."
        SCM = [S1, S2, S3, S4, S5, S6]
        Scam = random.choice(SCM)   
        AdditionalInfo.append(f"Feature: Favorite Schemes - Every charlatan has an angle they use in preference to other schemes\nYour favorite scam being: {Scam}")
        AdditionalInfo.append("Feature: False Identity (see notes)")
        Notes.append("Feature: False Identity - You have created a second identity that includes documentation, established acquaintances, and disguises that allow you to assume that persona. Additionally, you can forge documents including official papers and personal letters, as long as you have seen an example of the kind of document or the handwriting you are trying to copy.")  
    if back == "City Watch":
        AdditionalInfo.append("Feature: Watcher's Eye (see notes)")
        Notes.append("Feature: Watcher's Eye - Your experience in enforcing the law, and dealing with lawbreakers, gives you a feel for local laws and criminals. You can easily find the local outpost of the watch or a similar organization, and just as easily pick out the dens of criminal activity in a community, although you're more likely to be welcome in the former locations rather than the latter.")
    if back == "Clasp Member":
        AdditionalInfo.append("Feature: A Favor in Turn (see notes)")
        Notes.append("Feature: A Favor in Turn - You have gained enough clout in the Clasp that you can call in a favor from your contacts whenever you're close enough to a center of syndicate activity. A request for a favor can be no longer than 20 words, and is passed up the chain to an undisclosed Spireling for approval. This favor can take on any form subject to the approval of the GM, who decides how it is fulfilled. If muscle is requested, an NPC member of the Clasp can temporarily aid your party. If money is needed, a small loan can be provided. If you've been imprisoned, Clasp operatives can look into breaking you out or paying off the jailer.\nAt some point, the favor will be called in for repayment, often without warning. Refusing the call will result in your termination—literally. You might be called on to commit a specific burglary, or to pressure an Emonian dignitary to reveal a secret at an upcoming ball. The Clasp might even demand that you assassinate a specific person, with no questions asked or answered. It's the GM's prerogative to ensure that the syndicate's request is proportionate to the favor they bestowed—or that they compensate you in other ways for a service that goes beyond the scope of repaying the initial favor.")
    if (back == "Criminal") or (back == "Spy"): 
        S1 = "Blackmailer"
        S2 = "Burglar"
        S3 = "Enforcer"
        S4 = "Fence"
        S5 = "Highway robber"
        S6 = "Hired killer"
        S7 = "Pickpocket"
        S8 = "Smuggler"
        SPC = [S1, S2, S3, S4, S5, S6]
        Specialty = random.choice(SPC)
        AdditionalInfo.append(f"Feature: Criminal Specialty - There are many kinds of criminals, and within a thieves' guild or similar criminal organization, individual members have particular specialties. Even criminals who operate outside of such organizations have strong preferences for certain kinds of crimes over others.\nYour specialty is {Specialty}")  
        AdditionalInfo.append("Feature: Criminal Contact (see notes)")
        Notes.append("Feature: Criminal Contact - You have a reliable and trustworthy contact who acts as your liaison to a network of other criminals. You know how to get messages to and from your contact, even over great distances; specifically, you know the local messengers, corrupt caravan masters, and seedy sailors who can deliver messages for you.")
    if back == "Urban Bounty Hunter":
        AdditionalInfo.append("Feature: Ear to the Ground (see notes)")
        Notes.append("Feature: Ear to the Ground - You are in frequent contact with people in the segment of society that your chosen quarries move through. These people might be associated with the criminal underworld, the rough-and-tumble folk of the streets, or members of high society. This connection comes in the form of a contact in any city you visit, a person who provides information about the people and places of the local area.")
    if back == "Dimir Operative":
        DORI1 = "My parents belong to this guild, and I let them think I'm following in their footsteps."
        DORI2 = "I've been assigned to track this guild's activities."
        DORI3 = "I've been assigned to get close to an individual in this guild and learn their secrets."
        DORI4 = "I've been assigned to recruit a new Dimir spy from the ranks of this guild."
        DORI5 = "I was a member of this guild before the Dimir recruited me."
        DORI6 = "I don't like what this guild stands for and want to destroy it from within."
        DORI7 = "I secretly wish I could leave the Dimir and join this guild, but there is no escaping the Dimir."
        DORI8 = "I chose this guild at random or on a lark."
        DORI = [DORI1, DORI2, DORI3, DORI4, DORI5, DORI6, DORI7, DORI8]
        DimirOperReasonInfil = random.choice(DORI)     
        DimOpC1 = "I know a Dimir courier who relays messages to me from someone higher up the chain of command."
        DimOpC2 = "I get orders from a shapeshifter I recognize only through a series of code phrases we exchange."
        DimOpC3 = "An ostentatiously wealthy vampire is my secret guild superior, summoning me to a luxurious estate by means of coded messages."
        DimOpC4 = "I have never met my guild contact, but I receive telepathic messages, usually in my dreams."
        DimOpC5 = "I've never met my guild contact, but I get coded messages from a pattern of street lights and graffiti."
        DimOpC6 = "I didn't discover the identity of my guild contact until after we had begun a romantic relationship."
        DimOpC7 = "My superior maintains an elaborate identity as a young street urchin… unless it's all a lie, and I'm being sent on ridiculous missions by a twisted child."
        DimOpC8 = "My sibling and I both get telepathic orders from a mysterious contact, and I'm starting to question the authenticity of my sibling's orders."
        DimOpC = [DimOpC1, DimOpC2, DimOpC3, DimOpC4, DimOpC5, DimOpC6, DimOpC7, DimOpC8]
        DimirOperGuildCon = random.choice(DimOpC)
        DimOpC.remove(DimirOperGuildCon)
        randDimirOperGuild2Ally = False
        while not randDimirOperGuild2Ally:
            try:
                DimirOperGuild2Ally = random.choice(DimOpC)
                randDimirOperGuild2Ally = True
            except IndexError:
                DimirOperGuild2Ally = random.choice(DimOpC)         
        DimOpC.remove(DimirOperGuild2Ally)
        randDimirOperGuild2Rival = False
        while not randDimirOperGuild2Rival:
            try:
                DimirOperGuild2Rival = random.choice(DimOpC)
                randDimirOperGuild2Rival = True
            except IndexError:
                DimirOperGuild2Rival = random.choice(DimOpC)
        AdditionalInfo.append(f"Feature: False Identity - You have more than one identity. The one you wear most of the time makes you appear to be a member of a guild other than House Dimir. You have documentation, established acquaintances, and disguises that allow you to assume that persona and fit into the secondary guild.\nWhenever you choose, you can drop this identity and blend into the guildless masses of the city. The reason for your infiltration is {DimirOperReasonInfil}")
        AlliesOrg.append(f"Your Dimir Guild Contact: {DimirOperGuildCon}")
        AlliesOrg.append(f"Your 2nd Guild Contact Ally: {DimirOperGuild2Ally}")
        AlliesOrg.append(f"Your 2nd Guild Contact Rival: {DimirOperGuild2Rival}")    
        AlliesOrg.append("Dimir Guild Spells\nPrerequisite: Spellcasting or Pact Magic class feature\nFor you, the spells on the Dimir Guild Spells table are added to the spell list of your spellcasting class.\nCantrip: Encode Thoughts, Mage Hand\n1st: Disguise Self, Sleep\n2nd: Detect Thoughts, Pass Without Trace\n3rd: Gaseous Form, Meld into Stone, Nondetection\n4th: Arcane Eye, Freedom of Movement\n5th: Modify Memory\nYour magic is meant to be subtle and undetectable, but it might pull shadows or clouds of mist around you as you cast your spells.")
        EQP.append("The starting equipment for your secondary guild")
    if (back == "Entertainer") or (back == "Gladiator"):
        S1 = "Actor"
        S2 = "Dancer"
        S3 = "Fire Eater"
        S4 = "Jester"
        S5 = "Juggler"
        S6 = "Instrumental"
        S7 = "Poet"
        S8 = "Singer"
        S9 = "Storyteller"
        S10 = "Tumbler"
        ROU = [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10]
        Routine = random.choice(ROU)     
        AdditionalInfo.append(f"Feature: Entertainer Routines - A good entertainer is versatile, spicing up every performance with a variety of different routines.\nYour routine being {Routine}.")
        AdditionalInfo.append("Feature: By Popular Demand (see notes)")
        Notes.append("Feature: By Popular Demand - You can always find a place to perform, usually in an inn or tavern but possibly with a circus, at a theater, or even in a noble's court. At such a place, you receive free lodging and food of a modest or comfortable standard (depending on the quality of the establishment), as long as you perform each night. In addition, your performance makes you something of a local figure. When strangers recognize you in a town where you have performed, they typically take a liking to you.")   
    if back == "Faceless":  
        FacPers1 = "A flamboyant spy or brigand"
        FacPers2 = "The incarnation of a nation or people"
        FacPers3 = "A scoundrel with a masked guise"
        FacPers4 = "A vengeful spirit"
        FacPers5 = "The manifestation of a deity or your faith"
        FacPers6 = "One whose beauty is greatly accented using makeup"
        FacPers7 = "An impersonation of another hero"
        FacPers8 = "The embodiment of a school of magic"
        FacPers9 = "A warrior with distinctive armor"
        FacPers10 = "A disguise with animalistic or monstrous characteristics, meant to inspire fear"
        FacPers = [FacPers1, FacPers2, FacPers3, FacPers4, FacPers5, FacPers6, FacPers7, FacPers8, FacPers9, FacPers10]
        FacelessPersona = random.choice(FacPers)  
        AdditionalInfo.append(f"Faceless Persona - A faceless character adventures behind the mask of a public persona. This persona is as natural to them as their hidden, true face, but it disguises their identity.\nYour Faceless Persona being {FacelessPersona}")
        Notes.append("Feature: Dual Personalities (see notes)")
        AdditionalInfo.append("Feature: Dual Personalities - Most of your fellow adventurers and the world know you as your persona. Those who seek to learn more about you- your weaknesses, your origins, your purpose-find themselves stymied by your disguise. Upon donning a disguise and behaving as your persona, you are unidentifiable as your true self. By removing your disguise and revealing your true face, you are no longer identifiable as your persona. This allows you to change appearances between your two personalities as often as you wish, using one to hide the other or serve as convenient camouflage. However, should someone realize the connection between your persona and your true self, your deception might lose its effectiveness.")
    if back == "Faction Agent":
        AdditionalInfo.append("Feature: Factions of the Sword Coast (see notes)")
        Notes.append("Feature: Factions of the Sword Coast - The lack of large, centralized governments in the North and along the Sword Coast is likely directly responsible for the proliferation of secret societies and conspiracies in those lands. If your background is as an agent for one of the main factions of the North and Sword Coast, here are some possibilities.\nThe Harpers. Founded more than a millennium ago, disbanded and reorganized several times, the Harpers remain a powerful, behind-the-scenes agency, which acts to thwart evil and promote fairness through knowledge, rather than brute force. Harper agents are often proficient in Investigation, enabling them to be adept at snooping and spying. They often seek aid from other Harpers, sympathetic bards and innkeepers, rangers, and the clergy of gods that are aligned with the Harpers' ideals.\nThe Order of the Gauntlet. One of the newest power groups in Faerûn, the Order of the Gauntlet has an agenda similar to that of the Harpers. Its methods are vastly different, however: bearers of the gauntlet are holy warriors on a righteous quest to crush evil and promote justice, and they never hide in the shadows. Order agents tend to be proficient in Religion, and frequently seek aid from law enforcement friendly to the order's ideals, and the clergy of the order's patron gods.\nThe Emerald Enclave. Maintaining balance in the natural order and combating the forces that threaten that balance is the twofold goal of the Emerald Enclave. Those who serve the faction are masters of survival and living off the land. They are often proficient in Nature, and can seek assistance from woodsmen, hunters, rangers, barbarian tribes, druid circles, and priests who revere the gods of nature.\nThe Lords' Alliance. On one level, the agents of the Lords' Alliance are representatives of the cities and other governments that constitute the alliance. But, as a faction with interests and concerns that transcend local politics and geography, the Alliance has its own cadre of individuals who work on behalf of the organizations, wider agenda. Alliance agents are required to be knowledgeable in History, and can always rely on the aid of the governments that are part of the Alliance, plus other leaders and groups who uphold the Alliance's ideals.\nThe Zhentarim. In recent years, the Zhentarim have become more visible in the world at large, as the group works to improve its reputation among the common people. The faction draws employees and associates from many walks of life, setting them to tasks that serve the goals of the Black Network but aren't necessarily criminal in nature. Agents of the Black Network must often work in secret, and are frequently proficient in Deception. They seek aid from the wizards, mercenaries, merchants and priesthoods allied with the Zhentarim.")
        AdditionalInfo.append("Feature: Save Haven (see notes)")
        Notes.append("Feature: Save Haven - As a faction agent, you have access to a secret network of supporters and operatives who can provide assistance on your adventures. You know a set of secret signs and passwords you can use to identify such operatives, who can provide you with access to a hidden safe house, free room and board, or assistance in finding information. These agents never risk their lives for you or risk revealing their true identities.")
    if back == "Failed Merchant":
        AdditionalInfo.append("Feature: Supply Chain (see notes)")
        Notes.append("Feature: Supply Chain - From your time as a merchant, you retain connections with wholesalers, suppliers, and other merchants and entrepreneurs. You can call upon these connections when looking for items or information.")
    if back == "Far Traveler":
        WhyH1 = "Emissary"
        WhyH2 = "Exile"
        WhyH3 = "Fugitive"
        WhyH4 = "Pilgrim"
        WhyH5 = "Sightseer"
        WhyH6 = "Wanderer"
        WhyH = [WhyH1, WhyH2, WhyH3, WhyH4, WhyH5, WhyH6]
        WhyHere = random.choice(WhyH)  
        AdditionalInfo.append(f"Feature: Why Are You Here? - A far traveler might have set out on a journey for one of a number of reasons, and the departure from his or her homeland could have been voluntary or involuntary.\nThat reason being {WhyHere}.")   
        AdditionalInfo.append("Feature: Where Are You From? (see notes)")
        Notes.append("Feature: Where Are You From? - The most important decision in creating a far traveler background is determining your homeland. The places discussed here are all sufficiently distant from the North and the Sword Coast to justify the use of this background.\nEvermeet. The fabled elven islands far to the west are home to elves who have never been to Faerun. They often find it a harsher place than they expected when they do make the trip. If you are an elf, Evermeet is a logical (though not mandatory) choice for your homeland.\nMost of those who emigrate from Evermeet are either exiles, forced out for committing some infraction of elven law, or emissaries who come to Faerun for a purpose that benefits elven culture or society.\nHalruaa. Located on the southern edges of the Shining South, and hemmed in by mountains all around, the magocracy of Halruaa is a bizarre land to most in Faerun who know about it. Many folk have heard of the strange skyships the Halruaans sail, and a few know of the tales that even the least of their people can work magic.\nHalruaans usually make their journeys into Faerun for personal reasons, since their government has a strict stance against unauthorized involvement with other nations and organizations. You might have been exiled for breaking one of Halruaa's many byzantine laws, or you could be a pilgrim who seeks the shrines of the gods of magic.\nKara-Tur. The continent of Kara-Tur, far to the east of Faerûn, is home to people whose customs are unfamiliar to the folk of the Sword Coast. If you come from Kara-Tur, the people of Faerûn likely refer to you as Shou, even if that isn't your true ethnicity, because that's the blanket term they use for everyone who shares your origin.\nThe folk of Kara-Tur occasionally travel to Faerûn as diplomats or to forge trade relations with prosperous merchant cartels. You might have come here as part of some such delegation, then decided to stay when the mission was over.\nMulhorand. From the terrain to the architecture to the god-kings who rule over these lands, nearly everything about Mulhorand is a lien to someone from the Sword Coast. You likely experienced the same sort of culture shock when you left your desert home and traveled to the unfamiliar climes of northern Faerûn. Recent events in your homeland have led to the abolition of slavery, and a corresponding increase in the traffic between Mulhorand and the distant parts of Faerûn.\nThose who leave behind Mulhorand's sweltering deserts and ancient pyramids for a glimpse at a different life do so for many reasons. You might be in the North simply to see the strangeness this wet land has to offer, or because you have made too many enemies among the desert communities of your home.\nSossal. Few have heard of your homeland, but many have questions about it upon seeing you. Humans from Sossal seem crafted from snow, with alabaster skin and white hair, and typically dressed in white.\nSossal exists far to the northeast, hard up against the endless ice to the north and bounded on its other sides by hundreds of miles of the Great Glacier and the Great Ice Sea. No one from your nation makes the effort to cross such colossal barriers without a convincing reason. You must fear something truly terrible or seek something incredibly important.\nZakhara. As the saying goes among those in Faerûn who know of the place, 'To get to Zakhara, go south. Then go south some more.' Of course, you followed an equally long route when you came north from your place of birth. Though it isn't unusual for Zakharans to visit the southern extremes of Faerûn for trading purposes, few of them stray as far from home as you have.\nYou might be traveling to discover what wonders are to be found outside the deserts and sword-like mountains of your homeland, or perhaps you are on a pilgrimage to understand the gods that others worship, so that you might better appreciate your own deities.\nThe Underdark. Though your home is physically closer to the Sword Coast than the other locations discussed here, it is far more unnatural. You hail from one of the settlements in the Underdark, each of which has its own strange customs and laws. If you are a native of one of the great subterranean cities or settlements, you are probably a member of the race that occupies the place but you might also have grown up there after being captured and brought below when you were a child.\nIf you are a true Underdark native, you might have come to the surface as an emissary of your people, or perhaps to escape accusations of criminal behavior (whether warranted or not). If you aren't a native, your reason for leaving 'home' probably has something to do with getting away from a bad situation.")
        AdditionalInfo.append("Feature: All Eyes on You (see notes)")
        Notes.append("Feature: All Eyes on You - Your accent, mannerisms, figures of speech, and perhaps even your appearance all mark you as foreign. Curious glances are directed your way wherever you go, which can be a nuisance, but you also gain the friendly interest of scholars and others intrigued by far-off lands, to say nothing of everyday folk who are eager to hear stories of your homeland.\nYou can parley this attention into access to people and places you might not otherwise have, for you and your traveling companions. Noble lords, scholars, and merchant princes, to name a few, might be interested in hearing about your distant homeland and people.")
    if back == "Feylost": 
        FeyWMa1 = "Your eyes swirl with iridescent colors."
        FeyWMa2 = "You have a sweet scent, like that of nectar or honey."
        FeyWMa3 = "You have long whiskers like those of a cat."
        FeyWMa4 = "Your ears are covered with soft tufts of fur."
        FeyWMa5 = "Your skin sparkles in moonlight."
        FeyWMa6 = "Flowers either bloom or wilt (your choice) in your presence."
        FeyWMa7 = "Your hair is made of vines or brambles and grows back to normal length within 1 hour of being cut."
        FeyWMa8 = "You have a tail like that of a dog or another animal."
        FeyWMa = [FeyWMa1, FeyWMa2, FeyWMa3, FeyWMa4, FeyWMa5, FeyWMa6, FeyWMa7, FeyWMa8]
        FeyMark = random.choice(FeyWMa)
        FeyWV1 = "Awakened creature (a Beast or an ordinary plant that has had the Awaken spell cast on it)"
        FeyWV2 = "Centaur"
        FeyWV3 = "Dryad"
        FeyWV4 = "Faerie dragon"
        FeyWV5 = "Pixie"
        FeyWV6 = "Satyr"
        FeyWV7 = "Sprite"
        FeyWV8 = "Unicorn"
        FeyWV = [FeyWV1, FeyWV2, FeyWV3, FeyWV4, FeyWV5, FeyWV6, FeyWV7, FeyWV8]
        FeywildVisitor = random.choice(FeyWV)     
        AdditionalInfo.append(f"Fey Mark - You were transformed in some small way by your stay in the Feywild and gained a fey mark.\nYour Fey Mark: {FeyMark}")
        AdditionalInfo.append(f"Feywild Visitor - Whenever you're sound asleep or in a deep trance during a long rest, a spirit of the Feywild might pay you a visit: {FeywildVisitor}\nNo harm ever comes to you as a result of such visits, which can last for minutes or hours, and you remember each visit when you wake up. Conversations that occur with a visitor can contain any number of things, from messages and insights to nonsense and red herrings, at the DM's discretion. Such conversations are always conducted in a language you can understand, even if the Feywild visitor can't speak that language normally.")      
        AdditionalInfo.append("Feature: Feywild Connection (see notes)")
        Notes.append("Feature: Feywild Connection - Your mannerisms and knowledge of fey customs are recognized by natives of the Feywild, who see you as one of their own. Because of this, friendly Fey creatures are inclined to come to your aid if you are lost or need help in the Feywild.")
    if back == "Fisher":  
        FshT1 = "Lobster Wrestling. You fought in hand-to-hand combat with an immense lobster."
        FshT2 = "It Dragged the Boat. You nearly caught a fish of monstrous size that pulled your boat for miles."
        FshT3 = "Fins of Pure Gold. You caught a sea animal whose fins were made of pure gold, but another fisher stole it."
        FshT4 = "Ghost Fish. You are haunted by a ghostly fish that only you can see."
        FshT5 = "Nemesis Clam. A large clam containing a pearl the size of your head claimed one of your fingers before jetting away; one day, you'll find that clam."
        FshT6 = "It Swallowed the Sun. You once saw a fish leap from the water and turn day into night."
        FshT7 = "Dive into the Abyss. You found yourself in an underwater cave leading to the Abyss, and your luck has been sour ever since."
        FshT8 = "Love Story. You fell in love with a creature of pure water, but your brief romance ended tragically."
        FshT = [FshT1, FshT2, FshT3, FshT4, FshT5, FshT6, FshT7, FshT8]
        FisherTale = random.choice(FshT)   
        AdditionalInfo.append("Feature: Harvest The Water (see notes)")
        Notes.append("Feature: Harvest The Water - You gain advantage on ability checks made using fishing tackle. If you have access to a body of water that sustains marine life, you can maintain a moderate lifestyle while working as a fisher, and you can catch enough food to feed yourself and up to ten other people each day.")
        AdditionalInfo.append(f"Fishing Tale - You can tell a compelling tale. whether tall or true. to impress and entertain others. Once a day, you can tell your story to willing listeners. At the DM's discretion, a number of those listeners become friendly toward you; this is not a magical effect, and continued amicability on their part depends on your actions.\nThat tale being: {FisherTale}")                                      
    if back == "Folk Hero":
        S1 = "I stood up to a tyrant’s agents."
        S2 = "I saved people during a natural disaster."
        S3 = "I stood alone against a terrible monster."
        S4 = "I stole from a corrupt merchant to help the poor."
        S5 = "I led a militia to fight off an invading army."
        S6 = "I broke into a tyrant’s castle and stole weapons to arm the people."
        S7 = "I trained the peasantry to use farm implements as weapons against a tyrant’s soldiers."
        S8 = "A lord rescinded an unpopular decree after I led a symbolic act of protest against it."
        S9 = "A celestial, fey, or similar creature gave me a blessing or revealed my secret origin."
        S10 = "Recruited into a lord’s army, I rose to leadership and was commended for my heroism."
        DEF = [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10]
        Event = random.choice(DEF)        
        AdditionalInfo.append(f"Feature: Defining Event - You previously pursued a simple profession among the peasantry, perhaps as a farmer, miner, servant, shepherd, woodcutter, or gravedigger. But something happened that set you on a different path and marked you for greater things,\nThat event being: {Event}")        
    if back == "Inheritor":  
        Inh1 = "A document such as a map, a letter, or a journal."
        Inh2 = "A trinket (see 'Trinkets' in chapter 5 of PHB)."
        Inh3 = "A trinket (see 'Trinkets' in chapter 5 of PHB)."
        Inh4 = "An article of clothing."
        Inh5 = "A piece of jewelry."
        Inh6 = "An arcane book or formulary."
        Inh7 = "A written story, song, poem, or secret."
        Inh8 = "A tattoo or other body marking."
        Inh = [Inh1, Inh2, Inh3, Inh4, Inh5, Inh6, Inh7, Inh8]
        Inheritance = random.choice(Inh)
        EQP.append(Inheritance)
        AdditionalInfo.append("Feature: Inheritance (see notes)")
        Notes.append("Feature: Inheritance - Work with your DM to come up with details for your inheritance: Why is your inheritance so important, and what is its full story? You might prefer for the DM to invent these details as part of the game, allowing you to learn more about your inheritance as your character does.\nThe DM is free to use your inheritance as a story hook, sending you on quests to learn more about its history or true nature, or confronting you with foes who want to claim it for themselves or prevent you from learning what you seek. The DM also determines the properties of your inheritance and how they figure into the item's history and importance. For instance, the object might be a minor magic item, or one that begins with a modest ability and increases in potency with the passage of time. Or, the true nature of your inheritance might not be apparent at first and is revealed only when certain conditions are met. When you begin your adventuring career, you can decide whether to tell your companions about your inheritance right away. Rather than attracting attention to yourself, you might want to keep your inheritance a secret until you learn more about what it means to you and what it can do for you.")
    if back == "Gambler":
        AdditionalInfo.append("Feature: Never Tell Me the Odds (see notes)")
        Notes.append("Feature: Never Tell Me the Odds - Odds and probability are your bread and butter. During downtime activities that involve games of chance or figuring odds on the best plan, you can get a solid sense of which choice is likely the best one and which opportunities seem too good to be true, at the DM's determination.")
    if back == "Gate Warden":
        GtWPT1 = "Strange events and otherworldly creatures don't faze me."
        GtWPT2 = "I think in terms of exchange: something for something, nothing for nothing."
        GtWPT3 = "I speak with an unusual cadence."
        GtWPT4 = "I pepper my speech with words or curses borrowed from planar languages."
        GtWPT5 = "I've seen enough to know that you can't take anyone at face value, so I scrutinize everyone."
        GtWPT6 = "I have a superstitious habit I picked up from my gate-town, such as touching iron when I'm nervous or arranging objects in a specific order."
        GtWPT = [GtWPT1, GtWPT2, GtWPT3, GtWPT4, GtWPT5, GtWPT6]
        Trait = random.choice(GtWPT)
        GtWTr1 = "A tiny vial pendant filled with a drop of honey that glows faintly"
        GtWTr2 = "A small lead ingot that has a strange thumbprint pressed into it and whispers when held tightly"
        GtWTr3 = "Two lodestone spheres that chime when they attract each other"
        GtWTr4 = "A smoldering pebble of coal that, while always hot, doesn't burn skin, fur, scales, or clothing"
        GtWTr5 = "A feather that sheds dim light in a 5-foot radius"
        GtWTr6 = "A ring made from a chain link that, once donned, won't come off without pulling painfully hard"
        GtWTr = [GtWTr1, GtWTr2, GtWTr3, GtWTr4, GtWTr5, GtWTr6]
        GateWardenTrinket = random.choice(GtWTr)
        EQP.append(GateWardenTrinket)
        AdditionalInfo.append("Feature: Planar Infusion (see notes)")
        Notes.append("Feature: Planar Infusion - Living in a gate-town or a similar location steeped you in planar energy. You gain the Scion of the Outer Planes feat. In addition, you know where to find free, modest lodging and food in the community you grew up in.")
    if back == "Giant Foundling":
        FoundO1 = "You were found as a baby by a family of nomadic giants who raised you as one of their own."
        FoundO2 = "A family of stone giants rescued you when you fell into a mountain chasm, and you have lived with them underground ever since."
        FoundO3 = "You were lost or abandoned as a child in a jungle that teemed with ravenous dinosaurs. There, you found an equally lost frost giant; together, you survived."
        FoundO4 = "Your farm was crushed and your family killed in a battle between warring groups of giants. Racked with guilt over the destruction, a sympathetic giant soldier promised to care for you."
        FoundO5 = "After you had a series of strange dreams as a child, your superstitious parents sent you to study with a powerful but aloof storm giant oracle."
        FoundO6 = "While playing hide-and-seek with your friends, you stumbled into the castle of a cloud giant, who immediately adopted you."
        FoundO = [FoundO1, FoundO2, FoundO3, FoundO4, FoundO5, FoundO6]
        FoundlingOrigin = random.choice(FoundO)
        GFPT1 = "What I lack in stature compared to giants, I make up for with sheer spite."
        GFPT2 = "I insist on being taken seriously as a full-grown adult. Nobody talks down to me!"
        GFPT3 = "Crowded spaces make me uncomfortable. I'd much rather be in an open field than a bustling tavern."
        GFPT4 = "I embrace my shorter stature. It helps me stay unnoticed—and underestimated."
        GFPT5 = "Every avalanche begins as a single pebble."
        GFPT6 = "The world always feels too big, and I'm afraid I'll never find my place in it."
        GFPT = [GFPT1, GFPT2, GFPT3, GFPT4, GFPT5, GFPT6]
        Trait = random.choice(GFPT)        
        AdditionalInfo.append(f"Origin Stories - How you came to live among colossal creatures is up to you to determine, but the Foundling Origin table suggests a variety of possibilities.\nAs a Giant Foundling, your Foundling Origin: {FoundlingOrigin}")
        OtherBackgroundInfo.append("With the Giant Foundling background, if the DM allows, you can have the feats: Skilled (feat) or Tough (feat), as well as Strike of the Giants (feat).")
    if back == "Golgari Agent":
        GoAgC1 = "One of my parents is an elite assassin, a member of the Ochran."
        GoAgC2 = "I learned combat from a kraul."
        GoAgC3 = "I know a medusa who is stationed in the guildhall."
        GoAgC4 = "I had a torrid romance with a spore druid responsible for a large rot farm."
        GoAgC5 = "There's a troll in a remote area of the undercity who seems to find me interesting — and who knows more than you'd think."
        GoAgC6 = "An elf lich is determined to see me become a lich someday, too."
        GoAgC7 = "A medusa decided it would be more fun to recruit me into the guild than to kill me."
        GoAgC8 = "I know a findbroker who can locate just about anything, for the right price."
        GoAgC = [GoAgC1, GoAgC2, GoAgC3, GoAgC4, GoAgC5, GoAgC6, GoAgC7, GoAgC8]
        GolgariAgentContactAlly = random.choice(GoAgC)
        GoAgC.remove(GolgariAgentContactAlly)
        randGolgariAgentConRival = False
        while not randGolgariAgentConRival:
            try:
                GolgariAgentContactRival = random.choice(GoAgC)
                randGolgariAgentConRival = True
            except IndexError:
                GolgariAgentContactRival = random.choice(GoAgC)            
        GoAgNonC1 = "An Azorius arrester I literally pulled out of the gutter will do anything for me."
        GoAgNonC2 = "Someone joined the Gruul in a battle against the Boros once, and the sergeant of that Boros squad would love to prove that it was me."
        GoAgNonC3 = "I had a romance with a Dimir agent whom I still feed secrets to."
        GoAgNonC4 = "Roll an additional Golgari contact; you can decide if the contact is an ally or a rival."
        GoAgNonC5 = "I joined the Gruul in a battle against the Boros once, and the chief of that small clan thanks me for turning the tide."
        GoAgNonC6 = "An Izzet scientist resents that I sold a scrapped invention I found in the sewer."
        GoAgNonC7 = "My undercity explorations led me into an Orzhov vault, and a spirit thinks I stole something valuable."
        GoAgNonC8 = "I found a baby beast and sold it to a Rakdos wrangler who remains grateful to me."
        GoAgNonC9 = "A Selesnya druid and I share an interest in the same garden, and we have enjoyable arguments there."
        GoAgNonC10 = "I regularly pick up refuse from beneath a Simic laboratory, and sometimes I talk to the researcher who dumps it there."
        GoAgNonC = [GoAgNonC1, GoAgNonC2, GoAgNonC3, GoAgNonC4, GoAgNonC5, GoAgNonC6, GoAgNonC7, GoAgNonC8, GoAgNonC9, GoAgNonC10]
        GolgariAgentNonGolgariCont = random.choice(GoAgNonC)
        AlliesOrg.append(f"Your Golgari Contact Ally: {GolgariAgentContactAlly}")
        AlliesOrg.append(f"Your Golgari Contact Rival: {GolgariAgentContactRival}")
        AlliesOrg.append(f"Your Golgari Non-Guild Contact: {GolgariAgentNonGolgariCont}")
        AdditionalInfo.append("Feature: Undercity Paths (see notes)")
        Notes.append("Feature: Undercity Paths - You know hidden, underground pathways that you can use to bypass crowds, obstacles, and observation as you move through the city. When you aren't in combat, you and companions you lead can travel between any two locations in the city twice as fast as your speed would normally allow. The paths of the undercity are haunted by dangers that rarely brave the light of the surface world, so your journey isn't guaranteed to be safe.")
        AlliesOrg.append("Golgari Guild Spells\nPrerequisite: Spellcasting or Pact Magic class feature.\nFor you, the spells on the Golgari Guild Spells table are added to the spell list of your spellcasting class.\nCantrip: Dancing Lights, Spare the Dying\n1st: Entangle, Ray of Sickness\n2nd: Protection from Poison, Ray of Enfeeblement, Spider Climb\n3rd: Animate Dead, Plant Growth\n4th: Giant Insect, Grasping Vine\n5th: Cloudkill, Insect Plague.\nGolgari magic is often accompanied by a sickly green glow and a rotting stench.")
    if (back == "Grey Hunter") or (back == "Whitestone Rifle Corps"):
        CurRel1 = "I retired honorably from the Rifle Corps—and now it's time for me to pursue my own adventures."
        CurRel2 = "I'm on an important mission to protect Whitestone or guard one of our allies."
        CurRel3 = "Whitestone is in trouble, and I was sent away to seek help."
        CurRel4 = "I don't think firearms technology should be kept secret, so I escaped from the Rifle Corps with my weapon and am on the run."
        CurRel5 = "I was on a mission with my company when I got separated from them. Now I need to find my way back home."
        CurRel6 = "My weapon was stolen. I built a new one, but I can't return home until I've tracked down the thief and recovered the original."
        CurRel = [CurRel1, CurRel2, CurRel3, CurRel4, CurRel5, CurRel6]
        CurrentRelationship = random.choice(CurRel)
        AdditionalInfo.append(f"You are—or were—a member of an elite and trusted band of Whitestone's staunchest defenders.\nYour current relationship: {CurrentRelationship}")
        if back == "Grey Hunter":
            AdditionalInfo.append("Feature: Grey Hunter (see notes)")
            Notes.append("Feature: Grey Hunter - As elite as they are, the members of the Whitestone Rifle Corps do not represent the apex of firearms skill in Whitestone. A clandestine group of elite soldiers and survivalists is drawn secretly from the Rifle Corps ranks. Called the Grey Hunters, these soldiers are special operatives of the de Rolo family, and loyally serve as spies, bodyguards, and even assassins when the job requires it. Though few officially know of them, rumors of the Grey Hunters' existence swirl constantly throughout the city-state, often in response to their activities after having been loaned out to protect Whitestone's allies.\nYou are one of these Grey Hunters, even if just a trainee (if you're starting your campaign at low levels). You have the ear of the lord and lady of Whitestone, though you must exercise this privilege graciously lest you lose it.")
        if back == "Whitestone Rifle Corps":    
            AdditionalInfo.append("Feature: Legacy of Secrecy (see notes)")
            Notes.append("Feature: Legacy of Secrecy - You have been entrusted with the use and care of a weapon both powerful and terrifying. The rifle you wield might transform the face of warfare and life in Tal'Dorei. It is a weapon that haunts the mind of its creator, Percival de Rolo, manifesting as a pain that lives always behind his kind eyes.\nYou were granted a musket or a pistol by your commander in the Whitestone Rifle Corps. This weapon is a symbol of your status, and when you display it, other folk around you—particularly adventurers, mercenaries, guards, engineers, and weapons enthusiasts—treat you differently. You might be seen as a noble defender of the people, a selfish hoarder of power, or anything in between, at the GM's discretion.")
    if back == "Grinner":
        FavCS1 = "Zan's Comin' Back. This hopeful Tal 'Dorei folk song declares the inevitable return of a just ruler. Use it to seek out potential allies."
        FavCS2 = "Blow Fire Down the Coast. A rowdy fighting song from the Clovis Concord, this ditty talks of blasting up pirate ships. Use it to encourage battle."
        FavCS3 = "Hush! Onward Come the Dragons. This Tal'Dorei folk song recounts the terror in the days after the invasion of the red dragon called the Cinder King. Use it to encourage caution in speech and deed."
        FavCS4 = "Let the Sword Grow Rust. An antiwar anthem from Marquet, this song has uncertain origins. Use it to help quell violent encounters."
        FavCS5 = "Drink Deep, Li'l Hummingbird. A drinking rondo from the Menagerie Coast, this song tel ls the tale of a young person who d rinks so heavily that they awaken to find they've stowed away on a ship. Use it to encourage alertness in social situations."
        FavCS6 = "Dirge for the Emerald Fire. This elven song supposedly has thousands of obscure verses. Use the first two verses to spread news of death or defeat."
        FavCS = [FavCS1, FavCS2, FavCS3, FavCS4, FavCS5, FavCS6]
        FavoriteCodeSong = random.choice(FavCS)
        AdditionalInfo.append(f"Favorite Code-Song - All members of the Golden Grin have learned a handful of folk songs in their travels, and use those songs to send secret codes and alert fellow Grinners to danger.\nYour Favorite Code-Song: {FavoriteCodeSong}")
        AdditionalInfo.append("Feature: Ballad of The Grinning Fool (see notes)")
        Notes.append("Feature: Ballad of The Grinning Fool - Like every Grinner, you know how to find a hideout. In any city of 10,000 people or more on the Menagerie Coast or in the lands of the Dwendalian Empire, you can play the 'Ballad of the Grinning Fool' in a major tavern or inn. A member of the Golden Grin will find you and give shelter to you and any companions you vouch for. This shelter might be discontinued if it becomes too dangerous to hide you, at the DM's discretion.\nThis feature must be used with caution, for not all who know the ballad are your friends. Some are traitors, counterspies, or agents of tyranny.")
    if back == "Grounded": 
        GrComPl1 = "I am considered weak or unskilled and many treat me like a fledgling."
        GrComPl2 = "I am looked upon as a traitor to my people."
        GrComPl3 = "My family wants me to return to the perch, but I just can’t."
        GrComPl4 = "I am not welcome back in my home perch."
        GrComPl5 = "I am viewed as an oddity, someone for others to laugh at and tease."
        GrComPl6 = "I have found a new community on the forest floor."
        GrComPl = [GrComPl1, GrComPl2, GrComPl3, GrComPl4, GrComPl5, GrComPl6]
        GroundedCommunityPlace = random.choice(GrComPl)
        AdditionalInfo.append(f"An Odd Bird - Among birdfolk you are somewhere between an oddity and an outcast. Some consider your aversion to heights a rejection of birdfolk culture, leading many to find you off-putting.\nAs a Grounded, your Community Place: {GroundedCommunityPlace}")
        AdditionalInfo.append("Feature: Find Another Path (see notes)")
        Notes.append("Feature: Find Another Path - Since you have lived your life close to the ground, you are familiar with the undergrowth in the same way other birdfolk are familiar with the canopy. You can always recall the general layout of the terrain around you while traveling along the forest floor. If your path is ever blocked by an obstacle that requires you to climb or otherwise gain height to circumvent it, you can always find a way around, so long as such a path exists. Additionally, you are adept at finding shelter in the Wood while traveling, and can usually locate a suitable safe shelter (a cave, a tree hollow, or bramble thicket) somewhere on the forest floor for you and up to five other creatures.")
    if back == "Gruul Anarch":
        GrAnGC1 = "One of my parents is a renowned warrior in my clan."
        GrAnGC2 = "My sibling has the ear of the clan chief."
        GrAnGC3 = "I have cousins in a different clan."
        GrAnGC4 = "When we were younger, I was romantically involved with a prominent warrior in my clan."
        GrAnGC5 = "A druid in my clan believes I have a destiny to fulfill."
        GrAnGC6 = "The warrior who trained me remembers me for my exceptional potential."
        GrAnGC7 = "My clan chief killed one of my parents, who had challenged the chief for leadership of the clan. Some combination of resentment and remorse stirs the clan chief to help me sometimes."
        GrAnGC8 = "I made a strong impression on Borborygmos."
        GrAnGC = [GrAnGC1, GrAnGC2, GrAnGC3, GrAnGC4, GrAnGC5, GrAnGC6, GrAnGC7, GrAnGC8]
        GruulAnarchGuildContact = random.choice(GrAnGC)
        GrAnNGC1 = "An Azorius arrester thinks I can be reformed."
        GrAnNGC2 = "A Boros soldier gives me gifts in exchange for information about other clans' movements."
        GrAnNGC3 = "I once caught and released a Dimir spy."
        GrAnNGC4 = "I consult with a Golgari shaman for spiritual guidance at times."
        GrAnNGC5 = "Roll an additional Gruul contact; you can decide if the contact is an ally or a rival."
        GrAnNGC6 = "An Izzet scientist blames the Gruul for the destruction of his life's work in a raid, but seems to think that I'm not like other Gruul."
        GrAnNGC7 = "I foolishly borrowed money from an Orzhov syndic to indulge a shameful vice."
        GrAnNGC8 = "A close friend left our clan and joined the Cult of Rakdos."
        GrAnNGC9 = "A distant relative is trying to recruit me into the Selesnya Conclave."
        GrAnNGC10 = "I stopped a Simic biomancer from trapping wild beasts to perform vile experiments on them."
        GrAnNGC = [GrAnNGC1, GrAnNGC2, GrAnNGC3, GrAnNGC4, GrAnNGC5, GrAnNGC6, GrAnNGC7, GrAnNGC8, GrAnNGC9, GrAnNGC10]
        GruulAnarchNonGuildContact = random.choice(GrAnNGC)
        AlliesOrg.append(f"Your Gruul Guild Contact: {GruulAnarchGuildContact}")
        AlliesOrg.append(f"Your Non-Guild Contact: {GruulAnarchNonGuildContact}")
        AdditionalInfo.append("Feature: Rubblebelt Refuge (see notes)")
        Notes.append("Feature: Rubblebelt Refuge - You are intimately familiar with areas of the city that most people shun: ruined neighborhoods where wurms rampaged, overgrown parks that no hand has tended in decades, and the vast, sprawling rubblebelts of broken terrain that civilized folk have long abandoned. You can find a suitable place for you and your allies to hide or rest in these areas. In addition, you can find food and fresh water in these areas for yourself and up to five other people each day.")
        AlliesOrg.append("Gruul Guild Spells\nPrerequisite: Spellcasting or Pact Magic class feature\nFor you, the spells on the Gruul Guild Spells table are added to the spell list of your spellcasting class.\nCantrip: Fire Bolt, Produce Flame\n1st: Compelled Duel, Speak With Animals, Thunderwave\n2nd: Beast Sense, Shatter; 3rd: Conjure Animals, Conjure Barrage\n4th: Dominate Beast, Stoneskin\n5th: Destructive Wave\nFueled by the fire of rage burning in your heart, your magic is almost always accompanied by fiery effects, such as flames smoldering behind your eyes or dancing over your hands.")
    if back == "Clan Crafter":
        AdditionalInfo.append("Feature: Respect of the Stout Folk (see notes)")
        Notes.append("Feature: Respect of the Stout Folk - As well respected as clan crafters are among outsiders, no one esteems them quite so highly as dwarves do. You always have free room and board in any place where shield dwarves or gold dwarves dwell, and the individuals in such a settlement might vie among themselves to determine who can offer you (and possibly your compatriots) the finest accommodations and assistance.")
    if back == "Courtier":
        AdditionalInfo.append("Feature: Court Functionary (see notes)")
        Notes.append("Feature: Court Functionary - Your knowledge of how bureaucracies function lets you gain access to the records and inner workings of any noble court or government you encounter. You know who the movers and shakers are, whom to go to for the favors you seek, and what the current intrigues of interest in the group are.")
    if (back == "Guild Artisan") or (back == "Guild Merchant"):
        S1 = "Alchemists and apothecaries"
        S2 = "Armorers, locksmiths, and fine smiths"
        S3 = "Brewers, distillers, and vintners"
        S4 = "Calligraphers, scribes, and scriveners"
        S5 = "Carpenters, roofers, and plasterers"
        S6 = "Cartographers, surveyors, and chart-makers"
        S7 = "Cobblers and shoemakers"
        S8 = "Cooks and bakers"
        S9 = "Glassblowers and glaziers"
        S10 = "Jewelers and gemcutters"
        S11 = "Leatherworkers, skinners, and tanners"
        S12 = "Masons and stonecutters"
        S13 = "Painters, limners, and sign-makers"
        S14 = "Potters and tile-makers"
        S15 = "Shipwrights and sailmakers"
        S16 = "Smiths and metal-forgers"
        S17 = "Tinkers, pewterers, and casters"
        S18 = "Wagon-makers and wheelwrights"
        S19 = "Weavers and dyers"
        S20 = "Woodcarvers, coopers, and bowyers"
        BUS = [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20]
        Business = random.choice(BUS)                
        AdditionalInfo.append(f"Feature: Guild Business - Guilds are generally found in cities large enough to support several artisans practicing the same trade. However, your guild might instead be a loose network of artisans who each work in a different village within a larger realm. Your Guild Business: {Business}\nAs a member of your guild, you know the skills needed to create finished items from raw materials (reflected in your proficiency with a certain kind of artisan's tools), as well as the principles of trade and good business practices. The question now is whether you abandon your trade for adventure, or take on the extra effort to weave adventuring and trade together.")
        AdditionalInfo.append("Feature: Guild Membership (see notes)")
        Notes.append("Feature: Guild Membership - As an established and respected member of a guild, you can rely on certain benefits that membership provides. Your fellow guild members will provide you with lodging and food if necessary, and pay for your funeral if needed. In some cities and towns, a guildhall offers a central place to meet other members of your profession, which can be a good place to meet potential patrons, allies, or hirelings.\nGuilds often wield tremendous political power. If you are accused of a crime, your guild will support you if a good case can be made for your innocence or the crime is justifiable. You can also gain access to powerful political figures through the guild, if you are a member in good standing. Such connections might require the donation of money or magic items to the guild's coffers.\nYou must pay dues of 5 gp per month to the guild. If you miss payments, you must make up back dues to remain in the guild's good graces.")
    if back == "Haunted One":
        HaOHarE1 = "A monster that slaughtered dozens of innocent people spared your life, and you don’t know why."
        HaOHarE2 = "You were born under a dark star. You can feel it watching you, coldly and distantly. Sometimes it beckons you in the dead of night."
        HaOHarE3 = "An apparition that has haunted your family for generations now haunts you. You don’t know what it wants, and it won’t leave you alone."
        HaOHarE4 = "Your family has a history of practicing the dark arts. You dabbled once and felt something horrible clutch at your soul, whereupon you fled in terror."
        HaOHarE5 = "An oni took your sibling one cold, dark night, and you were unable to stop it."
        HaOHarE6 = "You were cursed with lycanthropy and later cured. You are now haunted by the innocents you slaughtered."
        HaOHarE7 = "A hag kidnapped and raised you. You escaped, but the hag still has a magical hold over you and fills your mind with evil thoughts."
        HaOHarE8 = "You opened an eldritch tome and saw things unfit for a sane mind. You burned the book, but its words and images are burned into your psyche."
        HaOHarE9 = "A fiend possessed you as a child. You were locked away but escaped. The fiend is still inside you, but now you try to keep it locked away."
        HaOHarE10 = "You did terrible things to avenge the murder of someone you loved. You became a monster, and it haunts your waking dreams."
        HaOHarE = [HaOHarE1, HaOHarE2, HaOHarE3, HaOHarE4, HaOHarE5, HaOHarE6, HaOHarE7, HaOHarE8, HaOHarE9, HaOHarE10]
        HauntedOneHarrowingEvent = random.choice(HaOHarE)        
        AdditionalInfo.append(f"Feature: Harrowing Event - Prior to becoming an adventurer, your path in life was defined by one dark moment, one fateful decision, or one tragedy. Now you feel a darkness threatening to consume you, and you fear there may be no hope of escape.\nYour Harrowing Event: {HauntedOneHarrowingEvent}")
        AdditionalInfo.append("Feature: Heart of Darkness (see notes)")
        Notes.append("Feature: Heart of Darkness - Those who look into your eyes can see that you have faced unimaginable horror and that you are no stranger to darkness. Though they might fear you, commoners will extend you every courtesy and do their utmost to help you. Unless you have shown yourself to be a danger to them, they will even take up arms to fight alongside you, should you find yourself facing an enemy alone.")
    if back == "Hermit":
        S1 = "I was searching for spiritual enlightenment."
        S2 = "I was partaking of communal living in accordance with the dictates of a religious order."
        S3 = "I was exiled for a crime I did not commit."
        S4 = "I retreated from society after a life-altering event."
        S5 = "I needed a quiet place to work on my art, literature, music, or manifesto."
        S6 = "I needed to commune with nature, far from civilization."
        S7 = "I was the caretaker of an ancient ruin or relic."
        S8 = "I was a pilgrim in search of a person, place, or relic of spiritual significance."
        SEC = [S1, S2, S3, S4, S5, S6, S7, S8]
        Seclusion = random.choice(SEC)
        AdditionalInfo.append(f"Feature: Life of Seclusion - What was the reason for your isolation, and what changed to allow you to end your solitude?\nYour life of seclusion: {Seclusion}")
        AdditionalInfo.append("Feature: Discovery (see notes)")
        Notes.append("Feature: Discovery - The quiet seclusion of your extended hermitage gave you access to a unique and powerful discovery. The exact nature of this revelation depends on the nature of your seclusion. It might be a great truth about the cosmos, the deities, the powerful beings of the outer planes, or the forces of nature. It could be a site that no one else has ever seen. You might have uncovered a fact that has long been forgotten, or unearthed some relic of the past that could rewrite history. It might be information that would be damaging to the people who or consigned you to exile, and hence the reason for your return to society.\nWork with your DM to determine the details of your discovery and its impact on the campaign.")
    if back == "House Agent":
        HoAg1 = "Cannith, which specializes in Alchemist's supplies and tinker's tools"
        HoAg1Skl = [AlchSupp, TinkTools]
        HoAg2 = "Deneith, which specializes in One gaming set and vehicles (land)"
        HoAg2Skl = [GSrand, VehLand]
        HoAg3 = "Ghallanda, which specializes in Brewer's supplies and cook's utensils"
        HoAg3Skl = [BrewSupp, CooksUten]
        HoAg4 = "Jorasco, which specializes in Alchemist's supplies and herbalism kit"
        HoAg4Skl = [AlchSupp, HerbKit]
        HoAg5 = "Kundarak, which specializes in Thieves' tools and tinker's tools"
        HoAg5Skl = [ThievKit, TinkTools]
        HoAg6 = "Lyrandar, which specializes in Navigator's tools and vehicles (air and sea)"
        HoAg6Skl = [NavTools, VehLand, VehSea]
        HoAg7 = "Medani, which specializes in Disguise kit and thieves' tools"
        HoAg7Skl = [DisgKit, ThievKit]
        HoAg8 = "Orien, which specializes in One gaming set and vehicles (land)"
        HoAg8Skl = [GSrand, VehLand]
        HoAg9 = "Phiarlan, which specializes in Disguise kit and one musical instrument"
        HoAg9Skl = [DisgKit, MusicalInstrumentsRand]
        HoAg10 = "Sivis, which specializes in Calligrapher's tools and forgery kit"
        HoAg10Skl = [CallSupp, ForgKit]
        HoAg11 = "Tharashk, which specializes in One gaming set and thieves' tools"
        HoAg11Skl = [GSrand, ThievKit]
        HoAg12 = "Thuranni, which specializes in One musical instrument and poisoner's kit"
        HoAg12Skl = [MusicalInstrumentsRand, PoisKit]
        HoAg13 = "Vadalis, which specializes in Herbalism kit and vehicles (land)"
        HoAg13Skl = [HerbKit, VehLand]
        HoAg = [HoAg1, HoAg2, HoAg3, HoAg4, HoAg5, HoAg6, HoAg7, HoAg8, HoAg9, HoAg10, HoAg11, HoAg12, HoAg13]
        HouseAgentProf = random.choice(HoAg)
        if param == "Y":
            print(f"0 - Random")
            print(f"1 - Cannith, which specializes in Alchemist's supplies and tinker's tools")
            print(f"2 - Deneith, which specializes in One gaming set and vehicles (land)")
            print(f"3 - Ghallanda, which specializes in Brewer's supplies and cook's utensils")
            print(f"4 - Jorasco, which specializes in Alchemist's supplies and herbalism kit")
            print(f"5 - Kundarak, which specializes in Thieves' tools and tinker's tools")
            print(f"6 - Lyrandar, which specializes in Navigator's tools and vehicles (air and sea)")
            print(f"7 - Medani, which specializes in Disguise kit and thieves' tools")
            print(f"8 - Orien, which specializes in One gaming set and vehicles (land)")
            print(f"9 - Phiarlan, which specializes in Disguise kit and one musical instrument")
            print(f"10 - Sivis, which specializes in Calligrapher's tools and forgery kit")
            print(f"11 - Tharashk, which specializes in One gaming set and thieves' tools")
            print(f"12 - Thuranni, which specializes in One musical instrument and poisoner's kit")
            print(f"13 - Vadalis, which specializes in Herbalism kit and vehicles (land)")      
            hoag = int(input("Choose which house you wish to be an agent of. "))
            if hoag == 1:
                for item in HoAg1Skl:
                    PlProf.append(item)
            if hoag == 2:
                for item in HoAg2Skl:
                    PlProf.append(item)               
            if hoag == 3:
                for item in HoAg3Skl:
                    PlProf.append(item)                
            if hoag == 4:
                for item in HoAg4Skl:
                    PlProf.append(item)               
            if hoag == 5:
                for item in HoAg5Skl:
                    PlProf.append(item)               
            if hoag == 6:
                for item in HoAg6Skl:
                    PlProf.append(item)                
            if hoag == 7:
                for item in HoAg7Skl:
                    PlProf.append(item)                
            if hoag == 8:
                for item in HoAg8Skl:
                    PlProf.append(item)                
            if hoag == 9:
                for item in HoAg9Skl:
                    PlProf.append(item)                
            if hoag == 10:
                for item in HoAg10Skl:
                    PlProf.append(item)                
            if hoag == 11:
                for item in HoAg11Skl:
                    PlProf.append(item)                
            if hoag == 12:
                for item in HoAg12Skl:
                    PlProf.append(item)                
            if hoag == 13:
                for item in HoAg13Skl:
                    PlProf.append(item)                
            if hoag == 0:
                for item in HouseAgentProf:
                    PlProf.append(item)
        if param == "N":
            for item in HouseAgentProf:
                PlProf.append(item)            
        HoAgR1 = "Acquisition"
        HoAgR2 = "Investigation"
        HoAgR3 = "Research & Development"
        HoAgR4 = "Security"
        HoAgR5 = "Intimidation"
        HoAgR6 = "Exploration"
        HoAgR7 = "Negotiation"
        HoAgR8 = "Covert Operations"
        HoAgR = [HoAgR1, HoAgR2, HoAgR3, HoAgR4, HoAgR5, HoAgR6, HoAgR7, HoAgR8]
        HouseAgentRole = random.choice(HoAgR)  
        AdditionalInfo.append(f"Your House, and thus proficiencies, is: {HouseAgentProf}")
        AdditionalInfo.append(f"Role - You always gather information for your house, but when a baron give you a specific mission, what sort of work do you do?\nYour House Role: {HouseAgentRole}")    
        AdditionalInfo.append("Feature: House Connections (see notes)")
        Notes.append("Feature: House Connections - As an agent of your house, you can always get food and lodging for yourself and your friends at a house enclave. When the house assigns you a mission, it will usually provide you with the necessary supplies and transportation. Beyond this, you have many old friends, mentors, and rivals in your house, and you may encounter one of them when you interact with a house business. The degree to which such acquaintances are willing to help you depends on your current standing in your house.")
    if back == "Investigator":
        InvFirstCa1 = "A friend was wrongfully accused of murder. You tracked down the actual killer, proving your friend’s innocence and starting your career as a detective."
        InvFirstCa2 = "You’re told you went missing for weeks. When you were found, you had no memory of being gone. Now you search to discover what happened to you."
        InvFirstCa3 = "You helped a spirit nd peace by finding its missing corpse. Ever since, other spectral clients have sought you out to help them nd rest."
        InvFirstCa4 = "You revealed that the monsters terrorizing your home were illusions created by a cruel mage. The magic-user escaped, but you’ve continued to uncover magical hoaxes."
        InvFirstCa5 = "You were wrongfully accused and convicted of a crime. You managed to escape and seek to help others avoid the experience you suffered, even while still being pursued by the law."
        InvFirstCa6 = "You survived the destructive use of a magic device that wiped out your home. Members of a secret organization found you. You now work with them, tracking down dangerous supernatural phenomena and preventing them from doing harm."
        InvFirstCa7 = "You found evidence of a conspiracy underpinning society. You tried to expose this mysterious cabal, but no one believed you. You’re still trying to prove what you know is true."
        InvFirstCa8 = "You got a job with an agency that investigates crimes that local law enforcement can’t solve. You often wonder which you value more, the truth or your pay."
        InvFirstCa = [InvFirstCa1, InvFirstCa2, InvFirstCa3, InvFirstCa4, InvFirstCa5, InvFirstCa6, InvFirstCa7, InvFirstCa8]
        InvestigatorFirstCase = random.choice(InvFirstCa) 
        AdditionalInfo.append(f"Path to Mystery - Your first case influenced the types of mysteries you’re interested in. Why was this case so impactful, personal, or traumatic? Whom did it affect besides you? Why and how did you get involved? Was it solved? How did it set you on the path to investigating other mysteries?\nAs an Investigator, your first case: {InvestigatorFirstCase}") 
        AdditionalInfo.append("Feature: Watcher's Eye (see notes)")
        Notes.append("Feature: Watcher's Eye - Your experience in enforcing the law, and dealing with lawbreakers, gives you a feel for local laws and criminals. You can easily find the local outpost of the watch or a similar organization, and just as easily pick out the dens of criminal activity in a community, although you're more likely to be welcome in the former locations rather than the latter.")
    if back == "Izzet Engineer":
        IzEnC1 = "An older relative is a member of the guild's board of directors."
        IzEnC2 = "I know a sprite who carries important messages among the guild's laboratories."
        IzEnC3 = "A sibling is the head of a laboratory doing exotic research."
        IzEnC4 = "A former colleague is now an attendant in a laboratory in the central guildhall."
        IzEnC5 = "I'm in regular communication with an instructor who set me on the course of my life and research."
        IzEnC6 = "I had a romance with a chemister working in the Blistercoils."
        IzEnC7 = "As an attendant, I had a fierce rivalry with another attendant for our supervisor's attention."
        IzEnC8 = "The guildmaster, Niv-Mizzet, took note of one of my experiments!"
        IzEnC = [IzEnC1, IzEnC2, IzEnC3, IzEnC4, IzEnC5, IzEnC6, IzEnC7, IzEnC8]
        IzzetEngrContAlly = random.choice(IzEnC)
        IzEnC.remove(IzzetEngrContAlly)
        randIzzetEngrConRival = False
        while not randIzzetEngrConRival:
            try:
                IzzetEngrContRival = random.choice(IzEnC)
                randIzzetEngrConRival = True
            except IndexError:
                IzzetEngrContRival = random.choice(IzEnC)                   
        IzEnNIC1 = "An Azorius inspector seems interested in my work."
        IzEnNIC2 = "I was ready to join the Boros before I decided on Izzet, and I sometimes still hear from the sergeant who tried to recruit me."
        IzEnNIC3 = "One of my former assistants turned out to be a Dimir spy. We're not on friendly terms anymore, but we have a habit of running into each other."
        IzEnNIC4 = "A Golgari assassin killed a bitter rival of mine, leaving me with conflicted feelings."
        IzEnNIC5 = "I helped a minor Gruul chieftain acquire an Izzet weapon."
        IzEnNIC6 = "Roll an additional Izzet contact; you can decide if the contact is an ally or a rival."
        IzEnNIC7 = "An Orzhov banker financed my laboratory's current work and expects great returns."
        IzEnNIC8 = "I have a cousin in the Cult of Rakdos, and we get along quite well."
        IzEnNIC9 = "A former attendant from the same laboratory ran off to join the Selesnya, and we get into a big argument every time we run into each other."
        IzEnNIC10 = "I compare notes and techniques with a Simic scientist over lunch sometimes."
        IzEnNIC = [IzEnNIC1, IzEnNIC2, IzEnNIC3, IzEnNIC4, IzEnNIC5, IzEnNIC6, IzEnNIC7, IzEnNIC8, IzEnNIC9, IzEnNIC10]
        IzzetEngrNonIzzetCont = random.choice(IzEnNIC)  
        AlliesOrg.append(f"Your Izzet Guild Contact Ally: {IzzetEngrContAlly}")
        AlliesOrg.append(f"Your Izzet Guild Contact Rival: {IzzetEngrContRival}")
        AlliesOrg.append(f"Your Non-Guild Contact: {IzzetEngrNonIzzetCont}")    
        AdditionalInfo.append("Feature: Urban Infrastructure (see notes)")
        Notes.append("Feature: Urban Infrastructure - The popular conception of the Izzet League is based on mad inventions, dangerous experiments, and explosive blasts. Much of that perception is accurate, but the league is also involved with mundane tasks of construction and architecture — primarily in crafting the infrastructure that allows Ravnicans to enjoy running water, levitating platforms, and other magical and technological wonders.\nYou have a basic knowledge of the structure of buildings, including the stuff behind the walls. You can also find blueprints of a specific building in order to learn the details of its construction. Such blueprints might provide knowledge of entry points, structural weaknesses, or secret spaces. Your access to such information isn't unlimited. If obtaining or using the information gets you in trouble with the law, the guild can't shield you from the repercussions.")
        AlliesOrg.append("Izzet Guild Spells\nPrerequisite: Spellcasting or Pact Magic class feature\nFor you, the spells on the Izzet Guild Spells table are added to the spell list of your spellcasting class.\nCantrip: Produce Flame, Shocking Grasp\n1st: Chaos Bolt, Create or Destroy Water, Unseen Servant\n2nd: Heat Metal, Rope Trick\n3rd: Call Lightning, Elemental Weapon, Glyph of Warding\n4th: Conjure Minor Elementals, Divination, Otiluke's Resilient Sphere\n5th: Animate Objects, Conjure Elemental\nYour spells tend to be loud, flashy, or explosive, even when the effect is unremarkable. If you use an arcane focus, it probably takes the form of an intricate device that could include metal gauntlets, glass canisters, copper tubing, and leather straps attaching it to your body.")
    if back == "Knight":
        AdditionalInfo.append("Feature: Retainers (see notes)")
        Notes.append("Feature: Retainers - You have the service of three retainers loyal to your family. These retainers can be attendants or messengers, and one might be a majordomo. Your retainers are commoners who can perform mundane tasks for you, but they do not fight for you, will not follow you into obviously dangerous areas (such as dungeons), and will leave if they are frequently endangered or abused.")
    if back == "Knight of Solamnia":
        KnSolTr1 = "A flat silver disk you record your heroics upon"
        KnSolTr2 = "A piece of a fallen knight's armor"
        KnSolTr3 = "A pendant featuring a crown, a rose, or a sword"
        KnSolTr4 = "The pommel of your mentor's sword"
        KnSolTr5 = "A meaningful favor from someone you defended—perhaps a handkerchief or glove"
        KnSolTr6 = "A locket with a sketch of a silver dragon inside"
        KnSolTr = [KnSolTr1, KnSolTr2, KnSolTr3, KnSolTr4, KnSolTr5, KnSolTr6]
        KnightSolamniaTrinket = random.choice(KnSolTr)
        KnSolPT1 = "I pledge my sword to the greater good. If I must perish in pursuit of that good, so be it."
        KnSolPT2 = "My comrades-in-arms are my family. Ill do whatever it takes to keep them safe."
        KnSolPT3 = "The protection of innocent people comes first. All other concerns come second."
        KnSolPT4 = "I joined the knights for the free meals, but their lessons grew on me over time."
        KnSolPT5 = "I wish my deeds to become the stuff of legends just like those of the knighthoods heroic founders."
        KnSolPT6 = "A dishonorable act drove me to become a knight. I have acted with honor ever since."
        KnSolPT = [KnSolPT1, KnSolPT2, KnSolPT3, KnSolPT4, KnSolPT5, KnSolPT6]
        Trait = random.choice(KnSolPT)    
        EQP.append(KnightSolamniaTrinket)
        AdditionalInfo.append("Feature: Squire of Solamnia (see notes)")
        Notes.append("Feature: Squire of Solamnia - You gain the Squire of Solamnia feat.\nIn addition, the Knights of Solamnia provide you free, modest lodging and food at any of their fortresses or encampments.")
    if back == "Lorehold Student":   
        LoStPT1 = "I thrive on esoteric lore. The more obscure the historical references I can include in everyday conversation, the better."
        LoStPT2 = "By searching for these lost artifacts, I hope to find who I really am along the way."
        LoStPT3 = "I can barely go a minute without talking about my research. I have so much knowledge in my head, and it needs to be let out somewhere!"
        LoStPT4 = "The spirits of the dead are so much more interesting to talk with than living classmates."
        LoStPT5 = "I can speak eloquently about the historical ramifications of an ancient war. But ask me to add two-digit numbers together, and I'm a mess."
        LoStPT6 = "In the end, it's all just entropy. Everything falls apart someday."
        LoStPT = [LoStPT1, LoStPT2, LoStPT3, LoStPT4, LoStPT5, LoStPT6]
        Trait = random.choice(LoStPT)
        LoStTr1 = "A map made of concentric circles that can be rotated around the page"
        LoStTr2 = "A puzzle box bedecked with amber"
        LoStTr3 = "A dented brass compass with a red needle"
        LoStTr4 = "The head of a broken statue that houses the consciousness of a snarky sage"
        LoStTr5 = "A sheet of parchment embossed with tactile lettering, glowing red"
        LoStTr6 = "A broken dagger with a wavy blade and a serpentine hilt"
        LoStTr = [LoStTr1, LoStTr2, LoStTr3, LoStTr4, LoStTr5, LoStTr6]
        LoreholdStuTrinket = random.choice (LoStTr)  
        EQP.append(LoreholdStuTrinket)
        AdditionalInfo.append("Feature: Lorehold Initiate - You gain the Strixhaven Initiate feat and must choose Lorehold within it.\nIn addition, if you have the Spellcasting or Pact Magic feature, the spells on the Lorehold Spells table are added to the spell list of your spellcasting class.\n1st: Comprehend Languages, Identify\n2nd: Borrowed Knowledge, Locate Object\n3rd: Speak with Dead, Spirit Guardians\n4th: Arcane Eye, Stone Shape\n5th: Flame Strike, Legend Lore\nConsider customizing how your spells look when you cast them. Your Lorehold spells might create displays of golden light. You might use a tome or a scroll as a spellcasting focus, and your spell effects might reflect the appearance of the reference books you study.")
    if back == "Lyceum Scholar":
        AdditionalInfo.append("Feature: Academic Requisition (see notes)")
        Notes.append("Feature: Academic Requisition - You've cleared enough lessons—and have gained an ally or two among the staff—to enable access to certain private areas within the Lyceum and other allied universities. Whenever you're on Lyceum grounds or at another major academic institution, you can requisition any set of tools found in the fifth edition rules. Each set of tools is magically marked to sound an alarm if they are removed from the university's grounds.\nWhen you seek services such as spellcasting from an NPC at the Alabaster Lyceum or a related institution, you can use those services at a 25 percent discount, at the GM's discretion.")
    if back == "Mage of High Sorcery":
        MaHSTr1 = "An unopened letter from your first teacher"
        MaHSTr2 = "A broken wand made of black, red, or white wood"
        MaHSTr3 = "A scroll bearing an incomprehensible formula"
        MaHSTr4 = "A purposeless device covered in colored stones that can fold into various enigmatic shapes"
        MaHSTr5 = "A pouch or spellbook emblazoned with the triple moon symbol of the Mages of High Sorcery"
        MaHSTr6 = "A lens through which you can see Krynn's invisible black moon, Nuitari"
        MaHSTr = [MaHSTr1, MaHSTr2, MaHSTr3, MaHSTr4, MaHSTr5, MaHSTr6]
        MageHighSorcTrinket = random.choice(MaHSTr)
        MaHSPT1 = "I wish to use my knowledge of magic to better people’s lives."
        MaHSPT2 = "My study of magic might reveal all manner of secrets."
        MaHSPT3 = "Magic is a means to power, and I will use it to pursue my ambitions."
        MaHSPT4 = "I learned magic so I'd be able to protect those I care about."
        MaHSPT5 = "I use my magic to maintain the balance between all things."
        MaHSPT6 = "Whether in the past, present, or future, I will be the greatest mage ever known."
        MaHSPT = [MaHSPT1, MaHSPT2, MaHSPT3, MaHSPT4, MaHSPT5, MaHSPT6]
        Trait = random.choice(MaHSPT)    
        EQP.append(MageHighSorcTrinket)
        AdditionalInfo.append("Feature: Initiate of High Sorcery - You gain the Initiate of High Sorcery feat.\nIn addition, the Mages of High Sorcery provide you with free, modest lodging and food indefinitely at any occupied Tower of High Sorcery and for one night at the home of an organization member.")
    if back == "Marine":   
        MarH1 = "Nearly Drowned. You hid underwater to avoid detection by enemies and held your breath for an extremely long time. Just before you would have died, you had a revelation about your existence."
        MarH2 = "Captured. You spent months enduring thirst, starvation, and torture at the hands of your enemy, but you never broke."
        MarH3 = "Sacrifice. You enabled the escape of your fellow soldiers, but at great cost to yourself. Some of your past comrades may think you're dead."
        MarH4 = "Juggernaut. No reasonable explanation can explain how you survived a particular battle. Every arrow and bolt missed you. You slew scores of enemies single-handedly and led your comrades to victory."
        MarH5 = "Stowaway. For days, you hid in the bilge of an enemy ship, surviving on brackish water and foolhardy rats. At the right moment, you crept up to the deck and took over the ship on your own."
        MarH6 = "Leave None Behind. You carried an injured marine for miles to avoid capture and death."
        MarH = [MarH1, MarH2, MarH3, MarH4, MarH5, MarH6]
        MarineHardship = random.choice(MarH) 
        AdditionalInfo.append(f"Hardship Endured - Hardship in your past has forged you into an unstoppable living weapon. This hardship is essential to you and is at the heart of a personal philosophy or ethos that often guides your actions.\nYour Hardship: {MarineHardship}")       
        AdditionalInfo.append("Feature: Steady (see notes)")
        Notes.append("Feature: Steady - You can move twice the normal amount of time (up to 16 hours) each day before being subject to the effect of a forced march (see 'Travel Pace' in chapter 8 of the Player's Handbook). Additionally, you can automatically find a safe route to land a boat on shore, provided such a route exists.")
    if back == "Myriad Operative":
        AdditionalInfo.append("Feature: Myriad Operative (see notes)")
        Notes.append("Feature: Myriad Operative - Your skill set might be similar to that of many members of the Clasp, but you work for a criminal organization that is far more sophisticated—and even less scrupulous. As a Myriad operative in Tal'Dorei, you might have been given a specific task that furthers that syndicate's hunger to expand beyond Wildemount, or which gives them an edge in their rivalry with the Clasp. Moreover, you understand the wisdom of keeping your activities secret from fellow criminals as well as law enforcement, since the agents of the Clasp will show you no mercy if your true identity is ever revealed.")
    if back == "Noble":
        AdditionalInfo.append("Feature: Retainers (see notes)")
        Notes.append("Feature: Retainers - If your character has a noble background, you may select this background feature instead of Position of Privilege. You have the service of three retainers loyal to your family. These retainers can be attendants or messengers, and one might be a majordomo. Your retainers are commoners who can perform mundane tasks for you, but they do not fight for you, will not follow you into obviously dangerous areas (such as dungeons), and will leave if they are frequently endangered or abused.")
        AdditionalInfo.append("Feature: Position of Privilege (see notes)")
        Notes.append("Feature: Position of Privilege - Thanks to your noble birth, people are inclined to think the best of you. You are welcome in high society, and people assume you have the right to be wherever you are. The common folk make every effort to accommodate you and avoid your displeasure, and other people of high birth treat you as a member of the same social sphere. You can secure an audience with a local noble if you need to.")
    if back == "Orzhov Representative":
        OrzRepC1 = "The spirit of an ancestor has taken an interest in me."
        OrzRepC2 = "An older cousin has the ear of a powerful oligarch."
        OrzRepC3 = "I know a knight who is responsible for collecting debts from powerful people."
        OrzRepC4 = "A vampire pontiff tried to use me as a pawn in past schemes."
        OrzRepC5 = "A silent spirit follows me around."
        OrzRepC6 = "A sibling has keys to parts of Vizkopa Bank."
        OrzRepC7 = "A giant thinks I'm adorable."
        OrzRepC8 = "I regularly offer tribute to an angel, and the angel has been kind to me in turn."
        OrzRepC = [OrzRepC1, OrzRepC2, OrzRepC3, OrzRepC4, OrzRepC5, OrzRepC6, OrzRepC7, OrzRepC8]
        OrzhovRepContAlly = random.choice(OrzRepC)
        OrzRepC.remove(OrzhovRepContAlly)
        randOrzhovRepConRival = False
        while not randOrzhovRepConRival:
            try:
                OrzhovRepContRival = random.choice(OrzRepC)
                randOrzhovRepConRival = True
            except IndexError:
                OrzhovRepContRival = random.choice(OrzRepC)           
        OrzRepNOC1 = "An Azorius arrester is always snooping into my family's business transactions."
        OrzRepNOC2 = "A Boros paladin saved my life, to my everlasting shame."
        OrzRepNOC3 = "I know a shopkeeper who is secretly a Dimir agent and tries to make sure that I keep that secret hidden."
        OrzRepNOC4 = "I'm fascinated by the culture of the Golgari kraul, and I have formed a friendship with one of their death priests."
        OrzRepNOC5 = "A Gruul druid hates me but would never dare to touch me."
        OrzRepNOC6 = "I know an Izzet engineer who is desperate to pay off a debt accrued by a deceased relative."
        OrzRepNOC7 = "Roll an additional Orzhov contact; you can decide if the contact is an ally or a rival."
        OrzRepNOC8 = "My childhood friend is now a Rakdos torturer. We still meet for drinks occasionally."
        OrzRepNOC9 = "I have the key to a vault where a Selesnya druid is hiding an item of secret shame."
        OrzRepNOC10 = "I was married to a Simic bioengineer."
        OrzRepNOC = [OrzRepNOC1, OrzRepNOC2, OrzRepNOC3, OrzRepNOC4, OrzRepNOC5, OrzRepNOC6, OrzRepNOC7, OrzRepNOC8, OrzRepNOC9, OrzRepNOC10]
        OrzhovRepNonOrzCont = random.choice(OrzRepNOC)   
        AlliesOrg.append(f"Your Orzhov Guild Contact Ally: {OrzhovRepContAlly}")
        AlliesOrg.append(f"Your Orzhov Guild Contact Rival: {OrzhovRepContRival}")
        AlliesOrg.append(f"Your Non-Guild Contact: {OrzhovRepNonOrzCont}")    
        AdditionalInfo.append("Feature: Leverage (see notes)")
        Notes.append("Feature: Leverage - You can exert leverage over one or more individuals below you in the guild's hierarchy and demand their help as needs warrant. For example, you can have a message carried across a neighborhood, procure a short carriage ride without paying, or have others clean up a bloody mess you left in an alley. The DM decides if your demands are reasonable and if there are subordinates available to fulfill them. As your status in the guild improves, you gain influence over more people, including ones in greater positions of power.")
        AlliesOrg.append("Orzhov Guild Spells\nPrerequisite: Spellcasting or Pact Magic class feature\nFor you, the spells on the Orzhov Guild Spells table are added to the spell list of your spellcasting class.\nCantrip: Friends, Guidance\n1st: Command, Illusory Script\n2nd: Enthrall, Ray of Enfeeblement, Zone of Truth\n3rd: Bestow Curse, Speak With Dead, Spirit Guardians\n4th: Blight, Death Ward, Secret Chest | Leomund's Secret Chest\n5th: Geas\nYour magic tends to manifest as swirling shadows, brilliant light, or sometimes the momentary appearance of shadowy spirit forms. Your spells might draw the blood of your enemies, or even directly touch their souls.")
    if back == "Outlander":
        S1 = "Forester"
        S2 = "Trapper"
        S3 = "Homesteader"
        S4 = "Guide"
        S5 = "Bounty hunter"
        S6 = "Exile or outcast"
        S7 = "Pilgrim"
        S8 = "Tribal nomad"
        S9 = "Hunter-gatherer"
        S10 = "Tribal marauder"
        ORI = [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10]
        Origin = random.choice(ORI)
        AdditionalInfo.append(f"Feature: Origin - You've been to strange places and seen things that others cannot begin to fathom. Consider some of the distant lands you have visited, and how they impacted you.\nYour occupation during your time in the wild: {Origin}")
        AdditionalInfo.append("Feature: Wanderer (see notes)")
        Notes.append("Feature: Wanderer - You have an excellent memory for maps and geography, and you can always recall the general layout of terrain, settlements, and other features around you. In addition, you can find food and fresh water for yourself and up to five other people each day, provided that the land offers berries, small game, water, and so forth.")
    if back == "Uthgardt Tribe Member":
        AdditionalInfo.append("Feature: Barbarian Tribes of Faerun (see notes)")
        Notes.append("Feature: Barbarian Tribes of Faerun - Though this section details the Uthgardt specifically, either it or the Outlander background can be used for a character whose origin lies with one of the other barbarian tribes in Faerûn.\nYou might be a fair-haired barbarian of the Reghed, dwelling in the shadow of the Reghed Glacier in the far North near Icewind Dale. You might also be of the nomadic Rashemi, noted for their savage berserkers and their masked witches. Perhaps you hail from one of the wood elf tribes in the Chondalwood, or the magic-hating human tribes of the sweltering jungles of Chult.")
        AdditionalInfo.append("Feature: Uthgardt Tribes and Their Territories (see notes)")
        Notes.append("Feature: Uthgardt Tribes and Their Territories - For most Uthgardt tribes, the only stability in their history is the site of their ancestral mound. Most of the Uthgardt holy sites have existed since antiquity, but the fortunes of the tribes that revere them have hardly been static. Following are brief descriptions of the Uthgardt tribes today.\nBlue Bear. The easternmost of the Uthgardt are the Blue Bear – thought destroyed more than a century ago – who have recently emerged from inside the High Forest and reclaimed their ancestral mound at Stone Stand, just south of the Moon Pass and north of the forest. The Blue Bears have reoccupied much of their old territory in the time since they returned to prominence, though they don't venture near Hellgate Keep, considering it a taboo place.\nBlack Lion and Red Tiger. North of Blue Bear territory, in the Glimmering Wood, is Beorunna's Well, a settlement of some size that near the ancient ancestral mound of the Red Tiger tribe. The settlement was founded some time ago by members of the Black Lion tribe, who put down roots here rather than continuing to live as nomads. Though the Red Tigers are less than comfortable with the present situation, they consider Beorunna's Well their holy site, so they make the best of things. Bands of Red Tiger tribespeople often winter in Beorunna's Well, and many of its hunters and trappers use the settlement as a place to sell the leather and furs they acquire in nearby forests.\nSky Pony. In a part of the Glimmerwood called the Moonwood stands the One Stone, the ancestral mound of the Sky Pony tribe. These are a people divided; half of the tribe has settled and built a sizable steading around the One Stone, similar to what Black Lion has done at Beorunna's Well. The other half of the tribe considers this act an insult to their totem, so they launch raids on the settlement, burning as much of it as they can and then escaping, often on pegasus-back.\nTree Ghost. In the depths of the High Forest stands the Grandfather Tree, the ancestral mound of the Tree Ghost tribe. The Tree Ghosts split off from the Blue Bears long ago and all but disappeared into the forest, although occasional reports reach civilization that they are still alive and can sometimes be seen clustered around the Grandfather Tree. Some sages postulate that the newly reborn Blue Bear tribe might well be Tree Ghost Uthgardt who are following a call from a revived Blue Bear totem.\nGreat Worm. The Frost Hills, a small southern spike of the Spine of the World Mountains just north of the Evermoors, is the site of Great Worm Cavern, the ancestral mound of the Great Worm tribe. These Uthgardt are notoriously reclusive; it has been twenty years since the tribe has sent raiding parties out anywhere but against the ores of the Spine Mountains.\nBlack Raven. As forbidding as the Spine of the World Mountains they roam, the Black Ravens are fanatical in their adherence to the old Uthgardt ways. Ranging out from Raven Rock, their ancestral mound deep inside the mountains, they have been known to send raiding parties as far south as Silverymoon, but their most frequent targets are the caravans that come in and out of Mithral Hall.\nElk. Flint Rock in the midst of the Evermoors is the ancestral mound of the Elk tribe. The Elk were once prolific raiders, extending their reach even into Nesme and Mithral Hall, but the tribe was shattered a handful of decades past by the forces of those cities. Though their numbers have replenished, the Elk remain mostly hunters and foragers. They are masters at avoiding or repulsing the threats of the Evermoors, and often hire themselves out as guides for outsiders.\nThunderbeast. The Thunderbeast tribe has not been heard from in several years. When the Thunderbeasts made their annual pilgrimage to Morgur's Mound in Neverwinter Wood, they found their holy site desecrated. Soon thereafter, their chieftain took them back into the depths of the High Forest, and they have not emerged since.\nGray Wolf. The Gray Wolf tribe, made up of lycanthropes, was destroyed by a Selunite crusade because of the tribe's curse. Some of the surviving Gray Wolves took shelter among other Uthgardt tribes.\nGriffon. The Griffon tribe came to an untimely end when it rose against the forces of Luruar allied with giants and orcs.\nRed Pony and Golden Eagle. The Red Pony and Golden Eagle tribes vanished centuries ago. They were last seen in the vicinity of the One Stone, the ancestral mound those tribes shared with Sky Pony.")
        AdditionalInfo.append("Feature: Uthgardt Heritage (see notes)")
        Notes.append("Feature: Uthgardt Heritage - You have an excellent knowledge of not only your tribe's territory, but also the terrain and natural resources of the rest of the North. You are familiar enough with any wilderness area that you find twice as much food and water as you normally would when you forage there.\nAdditionally, you can call upon the hospitality of your people, and those folk allied with your tribe, often including members of druid circles, tribes of nomadic elves, the Harpers, and the priesthoods devoted to the gods of the First Circle.")
    if back == "Pirate":
        AdditionalInfo.append("Feature: Bad Reputation (see notes)")
        Notes.append("Feature: Bad Reputation - No matter where you go, people are afraid of you due to your reputation. When you are in a civilized settlement, you can get away with minor criminal offenses, such as refusing to pay for food at a tavern or breaking down doors at a local shop, since most people will not report your activity to the authorities.")
    if back == "Sailor":
        AdditionalInfo.append("Feature: Ship's Passage (see notes)")
        Notes.append("Feature: Ship's Passage - When you need to, you can secure free passage on a sailing ship for yourself and your adventuring companions. You might sail on the ship you served on, or another ship you have good relations with (perhaps one captained by a former crewmate). Because you're calling in a favor, you can't be certain of a schedule or route that will meet your every need. Your DM will determine how long it takes to get where you need to go. In return for your free passage, you and your companions are expected to assist the crew during the voyage.")
        AdditionalInfo.append("Feature: Bad Reputation (see notes)")
        Notes.append("Feature: Bad Reputation - If your character has a sailor background, you may select this background feature instead of Ship's Passage.\nNo matter where you go, people are afraid of you due to your reputation. When you are in a civilized settlement, you can get away with minor criminal offenses, such as refusing to pay for food at a tavern or breaking down doors at a local shop, since most people will not report your activity to the authorities.")
    if back == "Plaintiff":
        AdditionalInfo.append("Feature: Legalese (see notes)")
        Notes.append("Feature: Legalese - Your experience with your local legal system has given you a firm knowledge of the ins and outs of that system. Even when the law is not on your side, you can use complex terms like ex injuria jus non oritur and cogitationis poenam nemo patitur to frighten people into thinking you know what you're talking about. With common folks who don't know any better, you might be able to intimidate or deceive to get favors or special treatment.")
    if back == "Planar Philosopher": 
        PlaPhiSF1 = "Athar, and the skill associated with that faction is: Religion"
        PlaPhiSF2 = "Bleak Cabal, and the skill associated with that faction is: Insight"
        PlaPhiSF3 = "Doomguard, and the skill associated with that faction is: Nature"
        PlaPhiSF4 = "Fated, and the skill associated with that faction is: Intimidation"
        PlaPhiSF5 = "Fraternity of Order, and the skill associated with that faction is: History"
        PlaPhiSF6 = "Hands of Havoc, and the skill associated with that faction is: Stealth"
        PlaPhiSF7 = "Harmonium, and the skill associated with that faction is: Perception"
        PlaPhiSF8 = "Heralds of Dust, and the skill associated with that faction is: Medicine"
        PlaPhiSF9 = "Mercykillers, and the skill associated with that faction is: Survival"
        PlaPhiSF10 = "Mind's Eye, and the skill associated with that faction is: Persuasion"
        PlaPhiSF11 = "Society of Sensation, and the skill associated with that faction is: Performance"
        PlaPhiSF12 = "Transcendent Order, and the skill associated with that faction is: Athletics"
        PlaPhiSF = [PlaPhiSF1, PlaPhiSF2, PlaPhiSF3, PlaPhiSF4, PlaPhiSF5, PlaPhiSF6, PlaPhiSF7, PlaPhiSF8, PlaPhiSF9, PlaPhiSF10, PlaPhiSF11, PlaPhiSF12]
        PlanarPhilSigilFaction = random.choice(PlaPhiSF)
        if param == "Y":
            print(f"0 - Random")
            print(f"1 - Increase skill based on the faction you choose?")
            facskl = int(input("Would you like to increase a skill based on a faction you can decide, or keep it random? "))
            if facskl == 1:
                print(f"0 - Random")
                print(f"1 - Athar, and the skill associated with that faction is: Religion")
                print(f"2 - Bleak Cabal, and the skill associated with that faction is: Insight")
                print(f"3 - Doomguard, and the skill associated with that faction is: Nature")
                print(f"4 - Fated, and the skill associated with that faction is: Intimidation")
                print(f"5 - Fraternity of Order, and the skill associated with that faction is: History")
                print(f"6 - Hands of Havoc, and the skill associated with that faction is: Stealth")
                print(f"7 - Harmonium, and the skill associated with that faction is: Perception")
                print(f"8 - Heralds of Dust, and the skill associated with that faction is: Medicine")
                print(f"9 - Mercykillers, and the skill associated with that faction is: Survival")
                print(f"10 - Mind's Eye, and the skill associated with that faction is: Persuasion")
                print(f"11 - Society of Sensation, and the skill associated with that faction is: Performance")
                print(f"12 - Transcendent Order, and the skill associated with that faction is: Athletics")
                facfacskl = int(input("Choose a faction and thus a skill to increase. "))
                if facfacskl == 1:
                    PlanarPhilSigilFaction = "Athar"
                    ReliNum += 1
                if facfacskl == 2:
                    PlanarPhilSigilFaction = "Bleak Cabal"
                    InsiNum += 1
                if facfacskl == 3:
                    PlanarPhilSigilFaction = "Doomguard"
                    NatuNum += 1
                if facfacskl == 4:
                    PlanarPhilSigilFaction = "Fated"
                    IntiNum += 1
                if facfacskl == 5:
                    PlanarPhilSigilFaction = "Fraternity of Order"
                    HistNum += 1
                if facfacskl == 6:
                    PlanarPhilSigilFaction = "Hands of Havoc"
                    SteaNum += 1
                if facfacskl == 7:
                    PlanarPhilSigilFaction = "Harmonium"
                    PercNum += 1
                if facfacskl == 8:
                    PlanarPhilSigilFaction = "Heralds of Dust"
                    MediNum += 1
                if facfacskl == 9:
                    PlanarPhilSigilFaction = "Mercykillers"
                    SurvNum += 1
                if facfacskl == 10:
                    PlanarPhilSigilFaction = "Mind's Eye"
                    PersNum += 1
                if facfacskl == 11:
                    PlanarPhilSigilFaction = "Society of Sensation"
                    PerfNum += 1
                if facfacskl == 12:
                    PlanarPhilSigilFaction = "Transcendent Order"
                    AthlNum += 1
                if facfacskl == 0:
                    if PlanarPhilSigilFaction == "Athar":
                        ReliNum += 1
                    if PlanarPhilSigilFaction == "Bleak Cabal":
                        InsiNum += 1
                    if PlanarPhilSigilFaction == "Doomguard":
                        NatuNum += 1
                    if PlanarPhilSigilFaction == "Fated":
                        IntiNum += 1
                    if PlanarPhilSigilFaction == "Fraternity of Order":
                        HistNum += 1
                    if PlanarPhilSigilFaction == "Hands of Havoc":
                        SteaNum += 1
                    if PlanarPhilSigilFaction == "Harmonium":
                        PercNum += 1
                    if PlanarPhilSigilFaction == "Heralds of Dust":
                        MediNum += 1
                    if PlanarPhilSigilFaction == "Mercykillers":
                        SurvNum += 1
                    if PlanarPhilSigilFaction == "Mind's Eye":
                        PersNum += 1
                    if PlanarPhilSigilFaction == "Society of Sensation":
                        PerfNum += 1
                    if PlanarPhilSigilFaction == "Transcendent Order":
                        AthlNum += 1
            if facskl == 0:
                if PlanarPhilSigilFaction == "Athar":
                    ReliNum += 1
                if PlanarPhilSigilFaction == "Bleak Cabal":
                    InsiNum += 1
                if PlanarPhilSigilFaction == "Doomguard":
                    NatuNum += 1
                if PlanarPhilSigilFaction == "Fated":
                    IntiNum += 1
                if PlanarPhilSigilFaction == "Fraternity of Order":
                    HistNum += 1
                if PlanarPhilSigilFaction == "Hands of Havoc":
                    SteaNum += 1
                if PlanarPhilSigilFaction == "Harmonium":
                    PercNum += 1
                if PlanarPhilSigilFaction == "Heralds of Dust":
                    MediNum += 1
                if PlanarPhilSigilFaction == "Mercykillers":
                    SurvNum += 1
                if PlanarPhilSigilFaction == "Mind's Eye":
                    PersNum += 1
                if PlanarPhilSigilFaction == "Society of Sensation":
                    PerfNum += 1
                if PlanarPhilSigilFaction == "Transcendent Order":
                    AthlNum += 1
        if param == "N":
            if PlanarPhilSigilFaction == "Athar":
                ReliNum += 1
            if PlanarPhilSigilFaction == "Bleak Cabal":
                InsiNum += 1
            if PlanarPhilSigilFaction == "Doomguard":
                NatuNum += 1
            if PlanarPhilSigilFaction == "Fated":
                IntiNum += 1
            if PlanarPhilSigilFaction == "Fraternity of Order":
                HistNum += 1
            if PlanarPhilSigilFaction == "Hands of Havoc":
                SteaNum += 1
            if PlanarPhilSigilFaction == "Harmonium":
                PercNum += 1
            if PlanarPhilSigilFaction == "Heralds of Dust":
                MediNum += 1
            if PlanarPhilSigilFaction == "Mercykillers":
                SurvNum += 1
            if PlanarPhilSigilFaction == "Mind's Eye":
                PersNum += 1
            if PlanarPhilSigilFaction == "Society of Sensation":
                PerfNum += 1
            if PlanarPhilSigilFaction == "Transcendent Order":
                AthlNum += 1
        PlaPhiPT1 = "I don't venerate any gods. With time, we can be as powerful as them or greater."
        PlaPhiPT2 = "Experience is everything; live in the moment."
        PlaPhiPT3 = "When things crumble, I find meaning in the dust."
        PlaPhiPT4 = "Life thrives through order, and I seek to maintain that order."
        PlaPhiPT5 = "When others make plans, the multiverse laughs and so do I."
        PlaPhiPT6 = "I know what's right, and none will stand in my way."
        PlaPhiPT = [PlaPhiPT1, PlaPhiPT2, PlaPhiPT3, PlaPhiPT4, PlaPhiPT5, PlaPhiPT6]
        Trait = random.choice(PlaPhiPT)
        PlaPhiTr1 = "Locket with a picture of my mentor and an inscription I can't read"
        PlaPhiTr2 = "Bleached cranium rat skull with colored glass beads in its eye sockets"
        PlaPhiTr3 = "Torn parchment with half a rebus painted on it"
        PlaPhiTr4 = "Bracelet of twisted razorvine stems"
        PlaPhiTr5 = "Fragment of a bronze blade covered in verdigris"
        PlaPhiTr6 = "Broken holy symbol of a forgotten god"
        PlaPhiTr = [PlaPhiTr1, PlaPhiTr2, PlaPhiTr3, PlaPhiTr4, PlaPhiTr5, PlaPhiTr6]
        PlanarPhilTrinket = random.choice(PlaPhiTr)
        AlliesOrg.append(f"As a Planar Philosopher, your Sigil Faction, and thus your extra skill: {PlanarPhilSigilFaction}")
        EQP.append(PlanarPhilTrinket) 
        if PlanarPhilSigilFaction == "Athar":
            AdditionalInfo.append(f"Factions of Sigil - Your Faction, {PlanarPhilSigilFaction}, adheres to: Deities are frauds and merely channel the might of a true, higher power.")
        if PlanarPhilSigilFaction == "Bleak Cabal":
            AdditionalInfo.append(f"Factions of Sigil - Your Faction, {PlanarPhilSigilFaction}, adheres to: There is no greater truth to the multiverse. Each being must discover their own meaning.")
        if PlanarPhilSigilFaction == "Doomguard":
            AdditionalInfo.append(f"Factions of Sigil - Your Faction, {PlanarPhilSigilFaction}, adheres to: Nothing lasts forever. The purpose of everything is to crumble and decay.")
        if PlanarPhilSigilFaction == "Fated":
            AdditionalInfo.append(f"Factions of Sigil - Your Faction, {PlanarPhilSigilFaction}, adheres to: Everyone makes their own fate and is entitled to whatever they can take and hold.")
        if PlanarPhilSigilFaction == "Fraternity of Order":
            AdditionalInfo.append(f"Factions of Sigil - Your Faction, {PlanarPhilSigilFaction}, adheres to: All of existence is governed by laws, and power comes from understanding and exploiting them.")
        if PlanarPhilSigilFaction == "Hands of Havoc":
            AdditionalInfo.append(f"Factions of Sigil - Your Faction, {PlanarPhilSigilFaction}, adheres to: Those who try to impose a single order on the multiverse are doomed to fail.")
        if PlanarPhilSigilFaction == "Harmonium":
            AdditionalInfo.append(f"Factions of Sigil - Your Faction, {PlanarPhilSigilFaction}, adheres to: The multiverse will be perfect only when everything is acting in harmony, whether it wants to or not.")
        if PlanarPhilSigilFaction == "Heralds of Dust":
            AdditionalInfo.append(f"Factions of Sigil - Your Faction, {PlanarPhilSigilFaction}, adheres to: Everyone is already dead; the entirety of the multiverse is an afterlife. Undeath holds the key to the next stage of existence.")
        if PlanarPhilSigilFaction == "Mercykillers":
            AdditionalInfo.append(f"Factions of Sigil - Your Faction, {PlanarPhilSigilFaction}, adheres to: Cold, relentless justice is absolute, and no one is above it.")
        if PlanarPhilSigilFaction == "Mind's Eye":
            AdditionalInfo.append(f"Factions of Sigil - Your Faction, {PlanarPhilSigilFaction}, adheres to: The multiverse exists to be explored. It shapes us, and we shape it in turn.")
        if PlanarPhilSigilFaction == "Society of Sensation":
            AdditionalInfo.append(f"Factions of Sigil - Your Faction, {PlanarPhilSigilFaction}, adheres to: Sensation is the proof of existence. By experiencing everything, we can understand the multiverse in all its complexity.")
        if PlanarPhilSigilFaction == "Transcendent Order":
            AdditionalInfo.append(f"Factions of Sigil - Your Faction, {PlanarPhilSigilFaction}, adheres to: Thought clouds action. To fall in step with the multiverse, one must act on instinct alone.")
        AdditionalInfo.append("Feature: Conviction (see notes)")
        Notes.append("Feature: Conviction - You gain the Scion of the Outer Planes feat. In addition, members of your organization provide you free, modest lodging and food at any of their holdings or the homes of other faction members.")
    if back == "Prismari Student": 
        PriStuPT1 = "I'm the life of the party, and I expect everyone's attention when I walk into a room."
        PriStuPT2 = "Two weeks ago, I was enthralled with my latest project. Now, I think it's garbage and deserves to be destroyed."
        PriStuPT3 = "I believe everyone has the ability to express their truest selves through art, and I'm happy to quietly push them in the right direction."
        PriStuPT4 = "Everyone is a critic, and I work to win them all over."
        PriStuPT5 = "I'm beset with such an overwhelming sense of ennui regarding my art. Nothing quite captures my attention anymore."
        PriStuPT6 = "Instead of confronting my negative emotions, I channel them into explosive artistic displays."
        PriStuPT = [PriStuPT1, PriStuPT2, PriStuPT3, PriStuPT4, PriStuPT5, PriStuPT6]
        Trait = random.choice(PriStuPT)
        PriStuTr1 = "A pair of rose-tinted glasses with glittery frames"
        PriStuTr2 = "A stoppered glass bottle that, when opened, plays a brassy orchestral piece"
        PriStuTr3 = "A quartet of hovering water motes in a vial"
        PriStuTr4 = "A bandolier of watercolor paints"
        PriStuTr5 = "A tiara capped with a crystal that crackles with harmless lightning"
        PriStuTr6 = "An iridescent quill"
        PriStuTr = [PriStuTr1, PriStuTr2, PriStuTr3, PriStuTr4, PriStuTr5, PriStuTr6]
        PrismariStudentTrinket = random.choice(PriStuTr)     
        EQP.append(PrismariStudentTrinket)       
        AdditionalInfo.append("Feature: Prismari Initiate - You gain the Strixhaven Initiate feat and must choose Prismari within it.\nIn addition, if you have the Spellcasting or Pact Magic feature, the spells on the Prismari Spells table are added to the spell list of your spellcasting class.\n1st: Chromatic Orb, Thunderwave\n2nd: Flaming Sphere, Kinetic Jaunt\n3rd: Haste, Water Walk\n4th: Freedom of Movement, Wall of Fire\n5th: Cone of Cold, Conjure Elemental\nConsider customizing how your spells look when you cast them. You might wield your Prismari spells with dynamic, gestural movement—as much dance as somatic component. Even a blast of fire in your hands is a sculpted work of art; elemental forces make grand designs as you hurl spells. These forces might linger on your body or in your clothes as decorative elements after your spells are dissipated, as sparks dance in your hair and your touch leaves tracings of frost on whatever you touch.")
    if back == "Quandrix Student":  
        QuaStuPT1 = "When I find a subject I'm interested in, I won't stop studying until I know everything about it. It keeps me up at night."
        QuaStuPT2 = "I hope this all makes sense to me one day. Until then, I'm going to keep faking it."
        QuaStuPT3 = "Equations and patterns come naturally to my mind. I wish friendship came just as easily."
        QuaStuPT4 = "I believe I'm always the smartest person in the room. And I'll prove it, even if no one asks me to."
        QuaStuPT5 = "If these classes have taught me anything, it's that reality is a lie, and nothing matters. So why bother?"
        QuaStuPT6 = "Before I graduate, I want to achieve something mathematically impossible. I must leave a legacy!"
        QuaStuPT = [QuaStuPT1, QuaStuPT2, QuaStuPT3, QuaStuPT4, QuaStuPT5, QuaStuPT6]
        Trait = random.choice(QuaStuPT)
        QuaStuTr1 = "A small succulent in a dodecahedral clay pot"
        QuaStuTr2 = "A blue knit hat that looks a bit like a bottle folding in on itself"
        QuaStuTr3 = "A model hypercube carved from green crystal, showcasing the fourth dimension"
        QuaStuTr4 = "A crumpled test on the theory of gravity manipulation, with a failing grade on the front and the name of a famous Quandrix professor"
        QuaStuTr5 = "A blue tetrahedron that, when tapped twice, projects a recording of an old mathematics lecture"
        QuaStuTr6 = "A round bread roll cut so that someone could spread butter on both halves without ever lifting the knife"
        QuaStuTr = [QuaStuTr1, QuaStuTr2, QuaStuTr3, QuaStuTr4, QuaStuTr5, QuaStuTr6]
        QuandrixStudentTrinket = random.choice(QuaStuTr)  
        EQP.append(QuandrixStudentTrinket)
        AdditionalInfo.append("Feature: Quandrix Initiate - You gain the Strixhaven Initiate feat and must choose Quandrix within it.\nIn addition, if you have the Spellcasting or Pact Magic feature, the spells on the Quandrix Spells table are added to the spell list of your spellcasting class.\n1st: Entangle, Guiding Bolt\n2nd: Enlarge/Reduce, Vortex Warp\n3rd: Aura of Vitality, Haste\n4th: Control Water, Freedom of Movement\n5th: Circle of Power, Passwall\nConsider customizing how your spells look when you cast them. Your Quandrix spells might manifest amid kaleidoscopic swirls of fractal patterns, amplifying the tiniest movements of your somatic components. When your magic creates or alters creatures, it might briefly surround the targets with shimmering fractal designs or tessellated patterns.")
    if back == "Rakdos Cultist":
        RCPerf1 = "Spikewheel acrobat"
        RCPerf2 = "Lampooning satirist"
        RCPerf3 = "Fire juggler"
        RCPerf4 = "Marionette puppeteer"
        RCPerf5 = "Pain artist"
        RCPerf6 = "Noise musician"
        RCPerf7 = "Nightmare clown"
        RCPerf8 = "Master of ceremonies"
        RCPerf = [RCPerf1, RCPerf2, RCPerf3, RCPerf4, RCPerf5, RCPerf6, RCPerf7, RCPerf8]
        RakdosCultPerformance = random.choice(RCPerf)    
        RakCulC1 = "I was part of a two-person act until my former partner moved to a different troupe."
        RakCulC2 = "My sibling and I ran away from home and joined the Cult of Rakdos together. We're very close."
        RakCulC3 = "A childhood friend of mine is an attendant in Rix Maadi, the Rakdos guildhall."
        RakCulC4 = "My parents brought me into the guild and taught me my trade."
        RakCulC5 = "There's a lesser demon in the cult who thinks he owes me a favor, and who am I to argue?"
        RakCulC6 = "The master of ceremonies in my troupe is well connected with other troupes."
        RakCulC7 = "I had a romance with a pain artist in another troupe."
        RakCulC8 = "Rakdos himself has witnessed me perform."
        RakCulC = [RakCulC1, RakCulC2, RakCulC3, RakCulC4, RakCulC5, RakCulC6, RakCulC7, RakCulC8]
        RakdosCultConAlly = random.choice(RakCulC)
        RakCulC.remove(RakdosCultConAlly)
        randRakdosCultConRival = False
        while not randRakdosCultConRival:
            try:
                RakdosCultConRival = random.choice(RakCulC)
                randRakdosCultConRival = True
            except IndexError:
                RakdosCultConRival = random.choice(RakCulC)          
        RakCulNRC1 = "I know an Azorius elocutor who has a very amusing dark side."
        RakCulNRC2 = "A Boros captain really wants to 'redeem' me."
        RakCulNRC3 = "I think a member of my troupe is a Dimir agent."
        RakCulNRC4 = "I once convinced a Golgari medusa to participate in a show. We've been on good terms ever since."
        RakCulNRC5 = "I came from the Gruul and still have relatives there."
        RakCulNRC6 = "An Izzet technician provides pyrotechnics for my performances."
        RakCulNRC7 = "An Orzhov oligarch has taken an interest in my career, like a patron of the arts."
        RakCulNRC8 = "Roll an additional Rakdos contact; you can decide if the contact is an ally or a rival."
        RakCulNRC9 = "A Selesnya healer attends my performances regularly."
        RakCulNRC10 = "A Simic biomancer provides mutant monsters to add a taste of the bizarre to our shows."
        RakCulNRC = [RakCulNRC1, RakCulNRC2, RakCulNRC3, RakCulNRC4, RakCulNRC5, RakCulNRC6, RakCulNRC7, RakCulNRC8, RakCulNRC9, RakCulNRC10]
        RakdosCultNonRakCon = random.choice(RakCulNRC)        
        AdditionalInfo.append(f"Rakdos Performance: Rakdos performance styles typically fuse standard circus-style acrobatics with fire, wrought-iron spikes and hooks, and monsters.\nYour Performance: {RakdosCultPerformance}")
        AdditionalInfo.append("Feature: Fearsome Reputation (see notes)")
        Notes.append("Feature: Fearsome Reputation - People recognize you as a member of the Cult of Rakdos, and they're careful not to draw your anger or ridicule. You can get away with minor criminal offenses, such as refusing to pay for food at a restaurant or breaking down a door at a local shop, if no legal authorities witness the crime. Most people are too daunted by you to report your wrongdoing to the Azorius.")
        AlliesOrg.append("Rakdos Guild Spells\nPrerequisite: Spellcasting or Pact Magic class feature\nFor you, the spells on the Rakdos Guild Spells table are added to the spell list of your spellcasting class.\nCantrip: Fire Bolt, Vicious Mockery\n1st: Burning Hands, Dissonant Whispers, Hellish Rebuke\n2nd: Crown of Madness, Enthrall, Flaming Sphere\n3rd: Fear, Haste\n4th: Confusion, Wall of Fire\n5th: Dominate Person\nYour magic often produces a flashy spectacle, wreathing you or your targets in a mixture of harmless flame and shadowy shapes. When you manipulate an opponent's mind, a flaming symbol of Rakdos might momentarily appear like a mask over the target's face.")
        AlliesOrg.append(f"Your Rakdos Guild Contact Ally: {RakdosCultConAlly}")
        AlliesOrg.append(f"Your Rakdos Guild Contact Rival: {RakdosCultConRival}")
        AlliesOrg.append(f"Your Non-Guild Contact: {RakdosCultNonRakCon}")   
    if back == "Reformed Cultist":
        AdditionalInfo.append("Feature: Fell Teachings (see notes)")
        Notes.append("Feature: Fell Teachings - You were inundated with knowledge about one of the Betrayer Gods, and know by heart everything from their basic commandments to some of their most esoteric secrets. Choose one of the Betrayer Gods. You have advantage on Intelligence (Religion) checks to know information about their faith, including obscure secrets unknown to most worshipers.\nAdditionally, you can work with your GM to create a secret that you learned during your time in the cult. This secret might be the seed of a conspiracy, a myth of a legendary hero whose true meaning has mutated over the years, or even the location of a fabled artifact of the gods.")
    if back == "Rewarded":      
        RewPT1 = "A safe home is a foundation on which anything else can be built. (Key, Throne)"
        RewPT2 = "I was elevated to heights I could never otherwise attain, and I won't waste my fortune. (Star, Sun)"
        RewPT3 = "I try to be a source of inspiration and joy to others. Life is never as bad as you think! (Euryale, Jester)"
        RewPT4 = "Courage and boldness can carry the day when all else fails. (Comet, Knight)"
        RewPT5 = "My good fortune means I can lift others up as well. (Gem, Moon)"
        RewPT6 = "Having the right answers is the first step to solving any problem, no matter how dire. (Fates, Sage)"
        RewPT = [RewPT1, RewPT2, RewPT3, RewPT4, RewPT5, RewPT6]
        Trait = random.choice(RewPT)
        RewTr1 = "A perfumed silk scarf from an admirer"
        RewTr2 = "A crystal bead that glows like a candle in the dark"
        RewTr3 = "A letter of introduction and invitation from an influential person in a far-off city"
        RewTr4 = "A motto or symbol whose meaning eludes you, etched on a piece of your equipment"
        RewTr5 = "A crisp playing card that never seems to tear or soil, depicting the card that affected you"
        RewTr6 = "Half a medallion designed to be rejoined to its other half"
        RewTr = [RewTr1, RewTr2, RewTr3, RewTr4, RewTr5, RewTr6]
        RewardedTrinket = random.choice(RewTr) 
        EQP.append(RewardedTrinket)      
        AdditionalInfo.append("Feature: Fortune's Favor - Your unexpected good fortune is reflected by a minor boon. You gain the Lucky, Magic Initiate, or Skilled feat (your choice). Your choice of feat reflects the transformation that changed your life. An encounter with a genie who gave you three wishes might have resulted in magical powers represented by Magic Initiate. If you paid off all your family debts with a fortuitous round of three-dragon ante, you might be Lucky instead. Alternatively, you could use the Skilled feat to reflect whatever trial you endured to secure your new destiny and to model the knowledge and abilities imparted to you by whatever force transformed your life.")
    if back == "Rival Intern":
        AdditionalInfo.append("Feature: Inside Informant (see notes)")
        Notes.append("Feature: Inside Informant - You have connections to your previous employer or other groups you dealt with during your previous employment. You can communicate with your contacts, gaining information at the DM's discretion.")
    if back == "Ruined":     
        RuPT1 = "I've changed from my past, and I work to live up to my new path. (Balance, Throne)"
        RuPT2 = "Every moment is a gift I refuse to squander. (Euryale, Skull)"
        RuPT3 = "Now that I've overcome having nothing, I can survive anything. (Fool, Ruin, Talons)"
        RuPT4 = "I know enemies are set against me, and I always prepare for the worst. (Flames, Rogue)"
        RuPT5 = "I interpret every event as part of a larger pattern I just haven't worked out yet. (Puzzle, Star)"
        RuPT6 = "I must make up for so much time I've already lost. (Donjon, Void)"
        RuPT = [RuPT1, RuPT2, RuPT3, RuPT4, RuPT5, RuPT6]
        Trait = random.choice(RuPT)
        RuTr1 = "A rusted scrap of a once-beloved family heirloom"
        RuTr2 = "A land deed, but all the names and markings that once tied it to you have faded into obscurity"
        RuTr3 = "A bauble once imbued with powerful magic"
        RuTr4 = "A battered playing card with a hole pierced in it, its face depicting the card that affected you"
        RuTr5 = "A yellowed Humanoid tooth that whispers eerily when placed under a pillow"
        RuTr6 = "A keepsake from someone you were once close to but who is now your enemy"
        RuTr = [RuTr1, RuTr2, RuTr3, RuTr4, RuTr5, RuTr6]
        RuinedTrinket = random.choice(RuTr)    
        EQP.append(RuinedTrinket)
        AdditionalInfo.append("Feature: Still Standing (see notes)")
        Notes.append("Feature: Still Standing - You have weathered ruinous misfortune, and you possess hidden reserves others don't expect. You gain the Alert, Skilled, or Tough feat (your choice). Your choice of feat reflects how you've dealt with the terrible loss that changed your life forever. If you've kept your senses sharp for every opportunity and climbed your way out of misery by seizing the tiniest scrap of hope, choose Alert. If you've redoubled your efforts to reclaim what was once yours, choose Skilled. If you've stoically persevered through your misfortune, select Tough.")         
    if back == "Rune Carver":
        RS1 = "You inscribe runes in wax or clay with a fine metal needle."
        RS2 = "You whittle pieces of wood into small figurines you mark with runes."
        RS3 = "You engrave runes onto glass beads and thread them onto necklaces and bracelets."
        RS4 = "You stitch runes into the hems of clothing."
        RS5 = "You carve runes on a set of animal bones you can throw in different formations."
        RS6 = "You draw runes into candles, melting the wax to smooth over the engravings."
        RS = [RS1, RS2, RS3, RS4, RS5, RS6]
        RuneStyle = random.choice(RS)
        RCPT1 = "Is it practical to learn an ancient language that is rarely spoken? No. But is it fun? Very."
        RCPT2 = "I learned one of my ancestors was a lauded rune carver whose story was lost to time. I seek to rekindle that legacy."
        RCPT3 = "The old, traditional markings of runecraft look so boring. Why not give my runes some flair?"
        RCPT4 = "In my studies of runes, I strive to understand how great civilizations of the past fell, so I can prevent it from happening to societies of the present."
        RCPT5 = "Life may be a whirlwind of chaos, but whenever I create my runes, I feel at peace."
        RCPT6 = "My brain struggles to process words written in ink, but the feeling of carved runes makes my mind sing."
        RCPT = [RCPT1, RCPT2, RCPT3, RCPT4, RCPT5, RCPT6]
        Trait = random.choice(RCPT)        
        AdditionalInfo.append(f"Rune Styles - Each rune carver has a unique style and preferred medium for creating runes\nYour Rune Style: {RuneStyle}")
        OtherBackgroundInfo.append("With the Rune Carver background, if the DM allows you, can have the feats Skilled (feat) or Tough (feat), as well as Rune Shaper (feat).")
    if back == "Cloistered Scholar":
        AdditionalInfo.append("Feature: Library Access (see notes)")
        Notes.append("Feature: Library Access - Though others must often endure extensive interviews and significant fees to gain access to even the most common archives in your library, you have free and easy access to the majority of the library, though it might also have repositories of lore that are too valuable, magical, or secret to permit anyone immediate access.\nYou have a working knowledge of your cloister's personnel and bureaucracy, and you know how to navigate those connections with some ease.\nAdditionally, you are likely to gain preferential treatment at other libraries across the Realms, as professional courtesy shown to a fellow scholar.")
    if back == "Sage":
        S1 = "Alchemist"
        S2 = "Astronomer"
        S3 = "Discredited academic"
        S4 = "Librarian"
        S5 = "Professor"
        S6 = "Researcher"
        S7 = "Wizard's apprentice"
        S8 = "Scribe"
        SPE = [S1, S2, S3, S4, S5, S6, S7, S8]
        Specialty = random.choice(SPE)        
        AdditionalInfo.append(f"Sage Specialty: The nature of your scholary training is: {Specialty}")
        AdditionalInfo.append("Feature: Researcher (see notes)")
        Notes.append("Feature: Researcher - When you attempt to learn or recall a piece of lore, if you do not know that information, you often know where and from whom you can obtain it. Usually, this information comes from a library, scriptorium, university, or a sage or other learned person or creature. Your DM might rule that the knowledge you seek is secreted away in an almost inaccessible place, or that it simply cannot be found. Unearthing the deepest secrets of the multiverse can require an aDventure or even a whole campaign.")
    if back == "Selesnya Initiate":
        SelesInC1 = "A wise centaur trainer believed in me even though I was a terrible student."
        SelesInC2 = "A good friend has risen to become a Ledev guardian."
        SelesInC3 = "I left my former guild and joined the Selesnya along with a close friend."
        SelesInC4 = "The dryad at the head of my enclave has taken an interest in my activities."
        SelesInC5 = "A sibling is an instructor at the guild's training grounds."
        SelesInC6 = "One of my parents is a votary, tasked with protecting the temple gardens at the Vitu-Ghazi guildhall."
        SelesInC7 = "I had a romance with a well-known Selesnya healer."
        SelesInC8 = "Trostani, the head of the guild and the voice of Mat'Selesnya, once welcomed me into her presence."
        SelesInC = [SelesInC1, SelesInC2, SelesInC3, SelesInC4, SelesInC5, SelesInC6, SelesInC7, SelesInC8]
        SelesInitConAlly = random.choice(SelesInC)
        SelesInC.remove(SelesInitConAlly)
        randSelesInitConR = False
        while not randSelesInitConR:
            try:
                SelesInitConRival = random.choice(SelesInC)
                randSelesInitConR = True
            except IndexError:
                SelesInitConRival = random.choice(SelesInC)          
        SelesInNSC1 = "I left the Azorius, and a former colleague still resents me for that act."
        SelesInNSC2 = "A good friend, eager for action, left the Selesnya and joined the Boros."
        SelesInNSC3 = "I had a relationship with a guild mate who turned out to be a Dimir agent."
        SelesInNSC4 = "I know a disgruntled Golgari assassin who is ripe for recruitment."
        SelesInNSC5 = "I'm friendly with a Gruul centaur who almost joined us a few years back."
        SelesInNSC6 = "I once had a heated public argument with an Izzet chemister, and neither of us is allowed back into that restaurant."
        SelesInNSC7 = "I paid off my debt to the Orzhov Syndicate, but my good friend was not so lucky and remains indebted to that guild."
        SelesInNSC8 = "At a time of terrible grief in my life, a Rakdos performer made a mockery of my pain, leaving me with mixed feelings of sadness and humor."
        SelesInNSC9 = "Roll an additional Selesnya contact; you can decide if the contact is an ally or a rival."
        SelesInNSC10 = "I have a sibling in the Simic Combine, and we argue every time we see each other."
        SelesInNSC = [SelesInNSC1, SelesInNSC2, SelesInNSC3, SelesInNSC4, SelesInNSC5, SelesInNSC6, SelesInNSC7, SelesInNSC8, SelesInNSC9, SelesInNSC10]
        SelesInitNonSelesCon = random.choice(SelesInNSC)
        AlliesOrg.append(f"Your Seles Guild Contact Ally: {SelesInitConAlly}")
        AlliesOrg.append(f"Your Seles Guild Contact Rival: {SelesInitConRival}")
        AlliesOrg.append(f"Your Non-Guild Contact: {SelesInitNonSelesCon}")        
        AdditionalInfo.append("Feature: Conclave's Shelter (see notes)")
        Notes.append("Feature: Conclave's Shelter - As a member of the Selesnya Conclave, you can count on your guild mates to provide shelter and aid. You and your companions can find a place to hide or rest in any Selesnya enclave in the city, unless you have proven to be a danger to them. The members of the enclave will shield you from the law or anyone else searching for you, though they will not risk their lives in this effort.\nIn addition, as a guild member you can receive free healing and care at a Selesnya enclave, though you must provide any material components needed for spells.")
        AlliesOrg.append("Selesnya Guild Spells\nPrerequisite: Spellcasting or Pact Magic class feature\nFor you, the spells on the Selesnya Guild Spells table are added to the spell list of your spellcasting class.\nCantrip: Druidcraft, Friends\n1st: Animal Friendship, Charm Person\n2nd: Aid, Animal Messenger, Calm Emotions, Warding Bond\n3rd: Plant Growth, Speak With Plants\n4th: Aura of Life, Conjure Minor Elementals\n5th: Awaken, Commune With Nature\nMembers of the Selesnya Conclave refer to their magic as 'doruvati,' a Sylvan word meaning 'gift.' When you use these gifts of Mat'Selesnya, graceful swirls of green and silver light dance in the air around you, and phantasmal green leaves might waft through the air. A sensation of gentle warmth and the smell of spring flowers or autumn leaves might accompany your spells.")
    if back == "Shipwright": 
        ShipwSI1 = "Grand Designs. You are working on plans and schematics for a new, very fast ship. You must examine as many different kinds of vessels as possible to help ensure the success of your design."
        ShipwSI2 = "Solid and Sound. You patched up a war galley and prevented it from sinking. The local navy regards you as a friend."
        ShipwSI3 = "Favored. You insisted on thicker planking for a merchant vessel's hull, which saved it from sinking when it smashed against a reef. You have a standing invitation to visit the merchant's distant mansion."
        ShipwSI4 = "Master of Armaments. You specialized in designing and mounting defenses for the navy. You easily recognize and determine the quality of such items."
        ShipwSI5 = "Low Places. You have contacts in the smuggling outfits along the coast; you occasionally repair the criminals' ships in exchange for coin and favors."
        ShipwSI6 = "Mysteries of the Deep. You experienced an encounter with a possibly divine being while sailing alone. Work with your DM to determine the secret about the deep waters of the sea that this entity revealed to you."
        ShipwSI = [ShipwSI1, ShipwSI2, ShipwSI3, ShipwSI4, ShipwSI5, ShipwSI6]
        ShipwrightSeaInfluence = random.choice(ShipwSI)
        ShipwSMCon1 = "Eda Oweland"
        ShipwSMCon2 = "Eda Oweland"
        ShipwSMCon3 = "Gellan Primewater"
        ShipwSMCon4 = "Gellan Primewater"
        ShipwSMCon5 = "Anders Solmor"
        ShipwSMCon6 = "Anders Solmor"
        ShipwSMCon = [ShipwSMCon1, ShipwSMCon2, ShipwSMCon3, ShipwSMCon4, ShipwSMCon5, ShipwSMCon6]
        ShipwrightSaltwaterMarshContact = random.choice(ShipwSMCon)
        AdditionalInfo.append(f"Life At Sea - Your life at sea and in port has shaped you\nYour Sea's Influence: {ShipwrightSeaInfluence}")
        AdditionalInfo.append(f"As a Shipwright, your Saltwater Marsh Contact: {ShipwrightSaltwaterMarshContact}")
        AdditionalInfo.append("Feature: I'll Patch It! (see notes)")
        Notes.append("Feature: I'll Patch It! - Provided you have carpenter's tools and wood. you can perform repairs on a water vehicle. When you use this ability, you restore a number of hit points co the hull of a water vehicle equal to 5 x your proficiency modifier. A vehicle cannot be patched by you in this way again until after it has been pulled ashore and fully repaired.")
    if back == "Silverquill Student":
        SilvStuPT1 = "I'll say whatever I need to in order to maintain my high social status."
        SilvStuPT2 = "I prefer saying the blunt truth over a pretty lie, and I don't particularly care whose feelings I hurt."
        SilvStuPT3 = "I believe that uplifting my peers is the best way to succeed."
        SilvStuPT4 = "I've mastered the art of using humor as a defense, and I always have a charming joke ready."
        SilvStuPT5 = "I always wait before speaking, analyzing the situation for whichever angle is most advantageous to my goals."
        SilvStuPT6 = "No one knows about the all-nighters I've pulled to keep my magic looking effortless, and I'm going to keep it that way."
        SilvStuPT = [SilvStuPT1, SilvStuPT2, SilvStuPT3, SilvStuPT4, SilvStuPT5, SilvStuPT6]
        Trait = random.choice(SilvStuPT)
        SilvStuTr1 = "A black leather notebook filled with half-finished poems"
        SilvStuTr2 = "A set of flashcards detailing different colloquialisms and their meanings"
        SilvStuTr3 = "A canteen that makes any liquid drunk from it taste sweet"
        SilvStuTr4 = "A forged permission slip granting access to the special archives of Strixhaven's libraries"
        SilvStuTr5 = "A stylish silver pin that references a famous series of novels about warlocks"
        SilvStuTr6 = "A stack of small pieces of parchment, each enchanted to stick to whatever surface it's pressed against and peel off easily"
        SilvStuTr = [SilvStuTr1, SilvStuTr2, SilvStuTr3, SilvStuTr4, SilvStuTr5, SilvStuTr6]
        SilverquillInitiateTrinket = random.choice(SilvStuTr)
        EQP.append(SilverquillInitiateTrinket)
        AdditionalInfo.append("Feature: Silverquill Initiate - You gain the Strixhaven Initiate feat and must choose Silverquill within it.\nIn addition, if you have the Spellcasting or Pact Magic feature, the spells on the Silverquill Spells table are added to the spell list of your spellcasting class.\n1st: Dissonant Whispers, Silvery Barbs\n2nd: Calm Emotions, Darkness\n3rd: Beacon of Hope, Daylight\n4th: Compulsion, Confusion\n5th: Dominate Person, Rary's Telepathic Bond\nConsider customizing how your spells look when you cast them. Your Silverquill spells might be accompanied by visual effects resembling splotches of ink or radiating ripples of golden light. Any auditory effects of your spells often sound like amplified echoes of your own voice speaking the spells' verbal components—even amid the crash of lightning or a fiery eruption.")
    if back == "Simic Scientist":
        SSProj1 = "Hull Clade, focused on protection and durability"
        SSProj2 = "Fin Clade, focused on movement"
        SSProj3 = "Gyre Clade, focused on cyclical patterns and metamagic"
        SSProj4 = "Guardian Project, focused on creating guard monsters and super soldiers"
        SSProj5 = "Crypsis Project, focused on intelligence and counterintelligence"
        SSProj6 = "Independent research in a new area"
        SSProj = [SSProj1, SSProj2, SSProj3, SSProj4, SSProj5, SSProj6]
        SimisSciProject = random.choice(SSProj)
        SimSciC1 = "My research builds on my parents' work and takes it in interesting new directions."
        SimSciC2 = "If a serious problem confounds me, I can count on my mentor to provide clarity of thought."
        SimSciC3 = "A former laboratory colleague went on to work on the Guardian Project."
        SimSciC4 = "A former colleague has ventured into fields of research that are possibly immoral and almost certainly illegal."
        SimSciC5 = "A former lover is now the supervisor of a prominent clade."
        SimSciC6 = "My sibling has become an almost unrecognizable mutant."
        SimSciC7 = "An old friend has retreated into a secluded life as an ascetic deepsage, devoted to contemplating philosophical principles."
        SimSciC8 = "My former clade supervisor is now engaged in field research studying some of the largest beasts and monsters on Ravnica."
        SimSciC = [SimSciC1, SimSciC2, SimSciC3, SimSciC4, SimSciC5, SimSciC6, SimSciC7, SimSciC8]
        SimicSciConAlly = random.choice(SimSciC)      
        SimSciC.remove(SimicSciConAlly)
        randSimSciR = False
        while not randSimSciR:
            try:
                SimicSciConRival = random.choice(SimSciC)
                randSimSciR = True
            except IndexError:
                SimicSciConRival = random.choice(SimSciC)         
        SimSciNSC1 = "My older sibling is upset that I didn't follow them into the Azorius."
        SimSciNSC2 = "A Boros sergeant is always asking questions about my work, but I suspect they're genuinely curious."
        SimSciNSC3 = "A friend in my clade thinks I don't know they're a Dimir agent."
        SimSciNSC4 = "I helped a Golgari spore druid with the fertilization and growth of their fungus field."
        SimSciNSC5 = "I can't fathom what could have made my childhood friend run off and join the Gruul."
        SimSciNSC6 = "I love comparing notes with my friend in the Izzet, though our fields of research are very different."
        SimSciNSC7 = "I borrowed a lot of money from an Orzhov syndic to help finance my research."
        SimSciNSC8 = "A Rakdos ringmaster has taken an interest in my research which, come to think of it, might make a nice sideshow act."
        SimSciNSC9 = "I left the Selesnya — and a lover — behind when I joined the Simic."
        SimSciNSC10 = "Roll an additional Simic contact; you can decide if the contact is an ally or a rival."
        SimSciNSC = [SimSciNSC1, SimSciNSC2, SimSciNSC3, SimSciNSC4, SimSciNSC5, SimSciNSC6, SimSciNSC7, SimSciNSC8, SimSciNSC9, SimSciNSC10]
        SimicSciNonSimicCon = random.choice(SimSciNSC)        
        AdditionalInfo.append(f"As a Simic researcher, you are part of a clade — a diverse group of individuals combining disparate talents in pursuit of a common goal—or a researcher on a specialized, short-term project focused on addressing an immediate need.\nYour Simic Project: {SimisSciProject}")
        AlliesOrg.append(f"Your Simic Guild Contact Ally: {SimicSciConAlly}")
        AlliesOrg.append(f"Your Simic Guild Contact Rival: {SimicSciConRival}")
        AlliesOrg.append(f"Your Non-Guild Contact: {SimicSciNonSimicCon}")        
        AdditionalInfo.append("Feature: Researcher (see notes)")
        Notes.append("Feature: Researcher - When you attempt to learn or recall a magical or scientific fact, if you don't know that information, you know where and from whom you can obtain it. Usually, this information comes from a Simic laboratory, or sometimes from an Izzet facility, a library, a university, or an independent scholar or other learned person or creature. Knowing where the information can be found doesn't automatically enable you to learn it; you might need to offer bribes, favors, or other incentives to induce people to reveal their secrets.\nYour DM might rule that the knowledge you seek is secreted away in an inaccessible place, or that it simply can't be found. Unearthing the deepest secrets of the multiverse can require an adventure or even a whole campaign.")
        AdditionalInfo.append("Simic Guild Spells\nPrerequisite: Spellcasting or Pact Magic class feature\nFor you, the spells on the Simic Guild Spells table are added to the spell list of your spellcasting class.\nCantrip: Acid Splash, Druidcraft\n1st: Detect Poison and Disease, Expeditious Retreat, Jump\n2nd: Alter Self, Enhance Ability, Enlarge/Reduce\n3rd: Gaseous Form, Water Breathing, Wind Wall\n4th: Freedom of Movement, Polymorph\n5th: Creation\nWhen your magic causes physical alterations in yourself or others, the result often displays the characteristics of fish, amphibians, or other water-dwelling creatures. Blue-green eddies of magical energy sometimes accompany your spellcasting, forming spirals that reflect the mathematical perfection of nature.")
    if back == "Smuggler":
        SmuAcc1 = "Spirit of the Whale. You smuggled stolen dwarven spirits in the body of a dead whale being pulled behind a fishing boat. When you delivered the goods, the corpse suddenly exploded, sending whale meat and whiskey bottles for half a mile."
        SmuAcc2 = "Cart and Sword. You drove a cart filled with stolen art through the middle of a battlefield while singing sea shanties to confuse the combatants."
        SmuAcc3 = "The Recruit. You enlisted in another nation's navy for the purpose of smuggling stolen jewels to a distant port. You attained a minor rank before disappearing from the navy and making your way here."
        SmuAcc4 = "River of Shadows. Your riverboat accidentally slipped through the veil into the Shadowfell for several hours. While you were there, you sold some stolen dragonborn artifacts before returning to this plane and paddling home."
        SmuAcc5 = "Cold-Hearted. You agreed to transport a family escaping a war. The baby began to cry at a checkpoint, and you gave the guards all your gold to let you pass. The family never found out about this gesture."
        SmuAcc6 = "Playing Both Sides. You once smuggled crates of crossbow bolts and bundles of arrows, each destined for an opposing side in a regional war, at the same time. The buyers arrived within moments of each other but did not discover your trickery."
        SmuAcc = [SmuAcc1, SmuAcc2, SmuAcc3, SmuAcc4, SmuAcc5, SmuAcc6]
        SmugglerAccomplishment = random.choice(SmuAcc)
        AdditionalInfo.append(f"Claim To Fame - Every smuggler has that one tale that sets them apart from common criminals. By wits, sailing skill, or a silver tongue, you lived co tell the story- and you tell it often.\nYour Accomplishment: {SmugglerAccomplishment}")
        AdditionalInfo.append("Feature: Down Low (see notes)")
        Notes.append("Feature: Down Low - You are acquainted with a network of smugglers who are willing to help you out of tight situations. White in a particular town, city. or other similarly sized community (DM's discretion). You and your companions can stay for free in safe houses. Safe houses provide a poor lifestyle. While staying at a safe house, you can choose to keep your presence (and that of your companions) a secret.")
    if back == "Mercenary Veteran":
        AdditionalInfo.append("Feature: Mercenaries of the North (see notes)")
        Notes.append("Feature: Mercenaries of the North - Countless mercenary companies operate up and down the Sword Coast and throughout the North. Most are small-scale operations that employ a dozen to a hundred folk who offer security services, hunt monsters and brigands, or go to war in exchange for gold. Some organizations, such as the Zhentarim, Flaming Fist, and the nation of Mintarn have hundreds or thousands of members and can provide private armies to those with enough funds. A few organizations operating in the North are described below.\nThe Chill. The cold and mysterious Lurkwood serves as the home of numerous groups of goblinoids that have banded together into one tribe called the Chill. Unlike most of their kind, the Chill refrain s from raiding the people of the North and maintains relatively good relations so that they can hire them selves out as warriors. Few city-states in the North are willing to field an army alongside the Chill, but several are happy to quietly pay the Chill to battle the Uthgardt, ores, trolls of the Evermoors, and other threats to civilization.\nSilent Rain. Consisting solely of elves, Silent Rain is a legendary mercenary company operating out of Evereska. Caring little for gold or fame, Silent Rain agrees only to jobs that either promote elven causes or involve destroying ores, gnolls, and the like. Prospective employers must leave written word (in Elvish) near Evereska, and the Silent Rain sends a representative if interested.\nThe Bloodaxes. Founded in Sundabar nearly two centuries ago, the Bloodaxes were originally a group of dwarves outcast from their clans for crimes against the teachings of Moradin Soulforger. They began hiring out as mercenaries to whoever in the North would pay them. Since then the mercenary company has broadened its membership to other races , but every member is an exile, criminal, or misfit of some sort looking for a fresh start and a new family among the bold Bloodaxes.")
        AdditionalInfo.append("Feature: Mercenary Life (see notes)")
        Notes.append("Feature: Mercenary Life - You know the mercenary life as only someone who has experienced it can. You are able to identify mercenary companies by their emblems, and you know a little about any such company, including the names and reputations of its commanders and leaders, and who has hired them recently. You can find the taverns and festhalls where mercenaries abide in any area, as long as you speak the language. You can find mercenary work between adventures sufficient to maintain a comfortable lifestyle.")
    if back == "Knight of the Order":
        AdditionalInfo.append("Feature: Knightly Orders of Faerun (see notes)")
        Notes.append("Feature: Knightly Orders of Faerun - Many who rightfully call themselves 'knight' earn that title as part of an order in service to a deity, such as Kelemvor's Eternal Order or Mystra's Knights of the Mystic Fire. Other knightly orders serve a government, royal family, or are the elite military of a feudal state, such as the brutal Warlock Knights of Vaasa. Other knighthoods are secular and non-governmental organizations of warriors who follow a particular philosophy, or consider themselves a kind of extended family, similar to an order of monks. Although there are organizations, such as the Knights of the Shield, that use the trappings of knighthood without necessarily being warriors, most folk of Faerûn who hear the word 'knight' think of a mounted warrior in armor beholden to a code. Below are a few knightly organizations.\nKnights of the Unicorn. The Knights of the Unicorn began as a fad of romantically minded sons and daughters of patriar families in Baldur's Gate. On a lark, they took the unicorn goddess Lurue as their mascot and went on various adventures for fun. The reality of the dangers they faced eventually sank in, as did Lurue's tenets. Over time the small group grew and spread, gaining a following in places as far as Cormyr. The Knights of the Unicorn are chivalric adventurers who follow romantic ideals: life is to be relished and lived with laughter, quests should be taken on a dare, impossible dreams should be pursued for the sheer wonder of their completion, and everyone should be praised for their strengths and comforted in their weaknesses.\nKnights of Myth Drannor. Long ago, the Knights of Myth Drannor were a famous adventuring band, and Dove Falconhand, one of the famous Seven Sisters, was one of them. The band took its name to honor the great but fallen city, just as the new Knights of Myth Drannor do today. With the city once again in ruins, Dove Falconhand decided to reform the group with the primary goal of building alliances and friendship between the civilized races of the world and goodly people in order to combat evil. The Knights of Myth Drannor once again ride the roads of the Dalelands, and they've begun to spread to the lands beyond. Their members, each accepted by Dove herself, are above all valiant and honest.\nKnights of the Silver Chalice. The Knights of the Silver Chalice was formed by edict of the demigod Siamorphe in Waterdeep a century ago. Siamorphe's ethos is the nobility's right and responsibility to rule, and the demigod is incarnated as a different noble mortal in each generation. By the decree of the Siamorphe at that time, the Knights of the Silver Chalice took it upon themselves to put a proper heir on the throne of Tethyr and reestablish order in that kingdom. Since then they have grown to be the most popular knighthood in Tethyr, a nation that has hosted many knighthoods in fealty to the crown.")
        AdditionalInfo.append("Feature: Knightly Regard - You receive shelter and succor from members of your knightly order and those who are sympathetic to its aims. If your order is a religious one, you can gain aid from temples and other religious communities of your deity. Knights of civic orders can get help from the community – whether a lone settlement or a great nation that they serve, and knights of philosophical orders can find help from those they have aided in pursuit of their ideals, and those who share those ideals.\nThis help comes in the form of shelter and meals, and healing when appropriate, as well as occasionally risky assistance, such as a band of local citizens rallying to aid a sorely pressed knight in a fight, or those who support the order helping to smuggle a knight out of town when he or she is being hunted unjustly.")
    if back == "Soldier":
        S1 = "Officer"
        S2 = "Scout"
        S3 = "Infantry"
        S4 = "Cavalry"
        S5 = "Healer"
        S6 = "Quartermaster"
        S7 = "Standard bearer"
        S8 = "Support staff (cook, blacksmith, or the like)"
        SPE = [S1, S2, S3, S4, S5, S6, S7, S8]
        Specialty = random.choice(SPE)
        AdditionalInfo.append(f"Feature: Specialty - During your time as a soldier, you had a specific role to play in your unit or arm.\nThat specialty being: {Specialty}")
        AdditionalInfo.append("Feature: Military Rank (see notes)")
        Notes.append("Feature: Military Rank - You have a military rank from your career as a soldier. Soldiers loyal to your former military organization still recognize your authority and influence, and they defer to you if they are of a lower rank. You can invoke your rank to exert influence over other soldiers and requisition simple equipment or horses for temporary use. You can also usually gain access to friendly military encampments and fortresses where your rank is recognized.")
    if back == "Urchin":
        AdditionalInfo.append("Feature: City Secrets (see notes)")
        Notes.append("Feature: City Secrets - You know the secret patterns and flow to cities and can find passages through the urban sprawl that others would miss. When you are not in combat, you (and companions you lead) can travel between any two locations in the city twice as fast as your speed would normally allow.")
    if back == "Volstrucker Agent":
        VolsAgTrag1 = "Familicide. Through deceit or manipulation, the Volstrucker convinced you to slaughter your own family."
        VolsAgTrag2 = "Amnesia. You were forced to study magic so potent that it strained your mind beyond mortal limits, stealing away the memories of your past."
        VolsAgTrag3 = "Capture. You were captured and tortured by agents of the Kryn Dynasty, and barely escaped."
        VolsAgTrag4 = "Starvation. A terrible blight afflicted your rural village, and many of your friends and family members starved to death. You survived, but only barely."
        VolsAgTrag5 = "Disfigurement. One of your arcane experiments went wrong and scarred or dismembered you so gravely that others now shun you. Only the Volstrucker showed you kindness after that day."
        VolsAgTrag6 = "Vicissitude. You were once the scion of a wealthy family who lost their entire fortune in the blink of an eye."
        VolsAgTrag = [VolsAgTrag1, VolsAgTrag2, VolsAgTrag3, VolsAgTrag4, VolsAgTrag5, VolsAgTrag6]
        VolstruckerAgentTragedy = random.choice(VolsAgTrag)
        AdditionalInfo.append(f"Tragedy - Happy people aren't selected to join the Volstrucker. The Cerberus Assembly preys upon talented individuals who have been broken by tragedy-in some cases, tragedy that the Volstrucker has arranged for. A slightly broken mind is more easily reshaped and reeducated.\nYour Tragedy: {VolstruckerAgentTragedy}")
        AdditionalInfo.append("Feature: Shadow Network (see notes)")
        Notes.append("Feature: Shadow Network - You have access to the Volstrucker shadow network, which allows you to communicate with other members of the order over long distances. If you write a letter in a special arcane ink, address it to a member of the Volstrucker, and cast it into a fire, the letter will burn to cinders and materialize whole again on the person of the agent you addressed it to.\nThe ink used to send a letter across the shadow network is the same as that used by a wizard to scribe spells in a spellbook. Writing a letter in this ink costs 10 gp per page.")
    if back == "Waterdhavian Noble":
        AdditionalInfo.append("Feature: Kept in Style (see notes)")
        Notes.append("Feature: Kept in Style - While you are in Waterdeep or elsewhere in the North your house sees to your everyday needs. Your name a~d signet are sufficient to cover most of your expenses; the inns, taverns, and festhalls you frequent are glad to record your debt and send an accounting to your family's estate in Waterdeep to settle what you owe.\nThis advantage enables you to live a comfortable lifestyle without having to pay 2 gp a day for it, or reduces the cost of a wealthy or aristocratic lifestyle by that amount. You may not maintain a less affluent lifestyle and use the difference as income – the benefit is a line of credit, not an actual monetary reward.")
    if back == "Wildspacer":
        WildSpClE1 = "Beholder"
        WildSpClE2 = "Cosmic Horror"
        WildSpClE3 = "Feyr"
        WildSpClE4 = "Lunar Dragon"
        WildSpClE5 = "Mind Flayer"
        WildSpClE6 = "Neh-thalggu"
        WildSpClE7 = "Neogi"
        WildSpClE8 = "Space Clown"
        WildSpClE9 = "Vampirate"
        WildSpClE10 = "Void Scavver"
        WildSpClE = [WildSpClE1, WildSpClE2, WildSpClE3, WildSpClE4, WildSpClE5, WildSpClE6, WildSpClE7, WildSpClE8, WildSpClE9, WildSpClE10]
        WildSpacerCloseEnc = random.choice(WildSpClE)
        AdditionalInfo.append(f"Close Encounter - You had a harrowing encounter with one of Wildspace's many terrors. You escaped with your life, but the encounter left you with a scar or two, or perhaps a recurring nightmare.\nYour Close Encounter: {WildSpacerCloseEnc}")
        AdditionalInfo.append("Feature: Wildspace Adaptation - You gain the Tough feat from the Player's Handbook. In addition, you learned how to adapt to zero gravity. Being weightless doesn't give you disadvantage on any of your melee attack rolls (see 'Weightlessness' in chapter 2).")
    if back == "Wind-Touched":
        WiToAccep1 = "I am truly blessed and have power over the wind itself."
        WiToAccep2 = "I am devoted to the wind spirits, in action and title."
        WiToAccep3 = "I believe in nature and goodness."
        WiToAccep4 = "I will work tirelessly to earn the respect of those who give me this title."
        WiToAccep5 = "I accept this honor but have my doubts."
        WiToAccep6 = "I feel nothing for this title, and carry it against my will."
        WiToAccep = [WiToAccep1, WiToAccep2, WiToAccep3, WiToAccep4, WiToAccep5, WiToAccep6]
        WindTouchedAcceptance = random.choice(WiToAccep)    
        AdditionalInfo.append(f"Title and Blessing - For some birdfolk, the moniker of Wind-Touched is merely a title, a symbol of their devotion to the wind and the natural world. Others have been told since birth that they were blessed by the wind, much in the way the Amaranthine Reya was in the old tales.\nYour Acceptance: {WindTouchedAcceptance}")
        AdditionalInfo.append("Feature: Supernatural Presence (see notes)")
        Notes.append("Feature: Supernatural Presence - Whether or not you are truly Wind-Touched, there are folk all across Everden that believe that you have been divinely blessed. If you make a show of power or skill that can be attributed to the wind or air, such as feats of acrobatics or commanding unseen forces, those believers will be bolstered by your supernatural presence. They will support you and, depending on how well you have convinced them of your powers, treat you with reverence and possibly even worship.")
    if back == "Witchlight Hand":
        WitHCC1 = "Old, cantankerous Witchlight hand"
        WitHCC2 = "Young, impressionable Witchlight hand"
        WitHCC3 = "Performer (such as an acrobat, a clown, or a musician)"
        WitHCC4 = "Retired performer"
        WitHCC5 = "Seasoned animal trainer"
        WitHCC6 = "Old Blink Dog"
        WitHCC7 = "Cheery Sprite"
        WitHCC8 = "Harmless, magical wisp of light (no stat block required) that has a flying speed of 30 feet, can hover, and sheds bright light in a 5-foot radius and dim light for an additional 5 feet"
        WitHCC = [WitHCC1, WitHCC2, WitHCC3, WitHCC4, WitHCC5, WitHCC6, WitHCC7, WitHCC8]
        WitchlHandCreatComp = random.choice(WitHCC)
        AdditionalInfo.append("Feature: Carnival Fixture (see notes)")
        Notes.append("Feature: Carnival Fixture - The Witchlight Carnival provides you with free, modest lodging and food. In addition, you may wander about the carnival and partake of its many wonders at no cost to you, provided you don't disrupt its shows or cause any other trouble.")
        AdditionalInfo.append(f"Carnival Companion - Over the years, you have earned the friendship of another carnival fixture.\nYour Creature Companion: {WitchlHandCreatComp}, please use the Witchlight Hand stat block in Ch.1 of 'The Wild Beyond the Witchlight' for stats.")
    if back == "Witherbloom Student":    
        WitStuPT1 = "I love brewing up a new recipe, even if some might be repulsed by my choice of ingredients. Or the final product. Or both."
        WitStuPT2 = "My fashion sense is like my garden: withered, black, and weird."
        WitStuPT3 = "I'm going to befriend every single monster in this swamp if it's the last thing I do."
        WitStuPT4 = "Everything in this world dies eventually. The question is, what will you do with the time you have left?"
        WitStuPT5 = "I know we just met, but when you die, may I have your bones? For research."
        WitStuPT6 = "Don't interrupt me; I'm brooding."
        WitStuPT = [WitStuPT1, WitStuPT2, WitStuPT3, WitStuPT4, WitStuPT5, WitStuPT6]
        Trait = random.choice(WitStuPT)
        WitStuTr1 = "A black bird-shaped mask, trimmed with glowing green thread"
        WitStuTr2 = "A set of rabbit bones"
        WitStuTr3 = "A pair of thick knee-high waders, stained with muck and moss"
        WitStuTr4 = "A slimy green tentacle, which occasionally wriggles"
        WitStuTr5 = "A notebook containing waterproof paper"
        WitStuTr6 = "A necklace of five small vials, each filled with luminescent white liquid"
        WitStuTr = [WitStuTr1, WitStuTr2, WitStuTr3, WitStuTr4, WitStuTr5, WitStuTr6]
        WitherbloomStudentTrinket = random.choice(WitStuTr)
        EQP.append(WitherbloomStudentTrinket)
        AdditionalInfo.append("Feature: Witherbloom Initiate - You gain the Strixhaven Initiate feat and must choose Witherbloom within it.\nIn addition, if you have the Spellcasting or Pact Magic feature, the spells on the Witherbloom Spells table are added to the spell list of your spellcasting class.\n1st: Cure Wounds, Inflict Wounds\n2nd: Lesser Restoration, Wither and Bloom\n3rd: Revivify, Vampiric Touch\n4th: Blight, Death Ward\n5th: Antilife Shell, Greater Restoration\nConsider customizing how your spells look when you cast them. Your Witherbloom spells might rely on material components or a spellcasting focus drawn from the swamp environment of Witherbloom, and your spells might take on an appearance suggesting those natural elements. Spectral shapes of swamp animals or plants might form amid your spell effects.")
########################################################################################################
### Printing section ###
    if back == "Ashari":
        OtherBackgroundInfo.append("As an Ashari, you also know a language specifically based on your tribe's elemental affinity.")
    if HollowOne == "Hollow One":
        RaceNotes.append("You are a Hollow One, or a zombie, in addition to your race, meaning you have a few extra traits.")    

    Gold = str(BGL)
    AA = "A mummified goblin hand"
    AB = "A piece of crystal that faintly glows in the moonlight"
    AC = "A gold coin minted in an unknown land"
    AD = "A diary written in a language you do not know"
    AE = "A brass ring that never tarnishes"
    AF = "An old chess piece made from glass"
    AG = "A pair of knucklebone dice, each with a skull symbol on the side that would normally show six pips"
    AH = "A small idol depicting a nightmarish creature that gives you unsettling dreams when you sleep near it"
    AI = "A rope necklace from which dangles four mummified elf fingers"
    AJ = "The deed for a parcel of land in a realm unknown to you"
    AK = "A 1-ounce block made from an unknown material"
    AL = "A small cloth doll skewered with needles"
    AM = "A tooth from an unknown beast"
    AN = "An enormous scale, perhaps from a dragon"
    AO = "A bright green feather"
    AP = "An old divination card bearing your likeness"
    AQ = "A glass orb filled with moving smoke"
    AR = "A 1-pound egg with a bright red shell"
    AS = "A pipe that blows bubbles"
    AT = "A glass jar containing a weird bit of flesh floating in pickling fluid"
    AU = "A tiny gnome-crafted music box that plays a song you dimly remember from your childhood"
    AV = "A small wooden statuette of a smug halfling"
    AW = "A brass orb etched with strange runes"
    AX = "A multicolored stone disk"
    AY = "A tiny silver icon of a raven"
    AZ = "A bag containing forty-seven humanoid teeth, one of which is rotten"
    BA = "A shard of obsidian that always feels warm to the touch"
    BB = "A dragon's bony talon hanging from a plain leather necklace"
    BC = "A pair of old socks"
    BD = "A blank book whose pages refuse to hold ink, chalk, graphite, or any other substance or marking"
    BE = "A silver badge in the shape of a five-pointed star"
    BF = "A knife that belonged to a relative"
    BG = "A glass vial filled with nail clippings"
    BH = "A rectangular metal device with two tiny metal cups on one end that throws sparks when wet"
    BI = "A white, sequined glove sized for a human"
    BJ = "A vest with one hundred tiny pockets"
    BK = "A small, weightless stone block"
    BL = "A tiny sketch portrait of a goblin"
    BM = "An empty glass vial that smells of perfume when opened"
    BN = "A gemstone that looks like a lump of coal when examined by anyone but you"
    BO = "A scrap of cloth from an old banner"
    BP = "A rank insignia from a lost legionnaire"
    BQ = "A tiny silver bell without a clapper"
    BR = "A mechanical canary inside a gnome-crafted lamp"
    BS = "A tiny chest carved to look like it has numerous feet on the bottom"
    BT = "A dead sprite inside a clear glass bottle"
    BU = "A metal can that has no opening but sounds as if it is filled with liquid, sand, spiders, or broken glass (your choice)"
    BV = "A glass orb filled with water, in which swims a clockwork goldfish"
    BW = "A silver spoon with an M engraved on the handle"
    BX = "A whistle made from gold-colored wood"
    BY = "A dead scarab beetle the size of your hand"
    BZ = "Two toy soldiers, one with a missing head"
    CA = "A small box filled with different-sized buttons"
    CB = "A candle that can't be lit"
    CC = "A tiny cage with no door"
    CD = "An old key"
    CE = "An indecipherable treasure map"
    CF = "A hilt from a broken sword"
    CG = "A rabbit's foot"
    CH = "A glass eye"
    CI = "A cameo carved in the likeness of a hideous person"
    CJ = "A silver skull the size of a coin"
    CK = "An alabaster mask"
    CL = "A pyramid of sticky black incense that smells very bad"
    CM = "A nightcap that, when worn, gives you pleasant dreams"
    CN = "A single caltrop made from bone"
    CO = "A gold monocle frame without the lens"
    CP = "A 1-inch cube, each side painted a different color"
    CQ = "A crystal knob from a door"
    CR = "A small packet filled with pink dust"
    CS = "A fragment of a beautiful song, written as musical notes on two pieces of parchment"
    CT = "A silver teardrop earring made from a real teardrop"
    CU = "The shell of an egg painted with scenes of human misery in disturbing detail"
    CV = "A fan that, when unfolded, shows a sleeping cat"
    CW = "A set of bone pipes"
    CX = "A four-leaf clover pressed inside a book discussing manners and etiquette"
    CY = "A sheet of parchment upon which is drawn a complex mechanical contraption"
    CZ = "An ornate scabbard that fits no blade you have found so far"
    DA = "An invitation to a party where a murder happened"
    DB = "A bronze pentacle with an etching of a rat's head in its center"
    DC = "A purple handkerchief embroidered with the name of a powerful archmage"
    DD = "Half of a floorplan for a temple, castle, or some other structure"
    DE = "A bit of folded cloth that, when unfolded, turns into a stylish cap"
    DF = "A receipt of deposit at a bank in a far-flung city"
    DG = "A diary with seven missing pages"
    DH = "An empty silver snuffbox bearing an inscription on the surface that says 'dreams'"
    DI = "An iron holy symbol devoted to an unknown god"
    DJ = "A book that tells the story of a legendary hero's rise and fall, with the last chapter missing"
    DK = "A vial of dragon blood"
    DL = "An ancient arrow of elven design"
    DM = "A needle that never bend"
    DN = "An ornate brooch of dwarven design"
    DO = "An empty wine bottle bearing a pretty label that says, 'The Wizard of Wines Winery, Red Dragon Crush, 331422-W'"
    DP = "A mosaic tile with a multicolored, glazed surface"
    DQ = "A petrified mouse"
    DR = "A black pirate flag adorned with a dragon's skull and crossbones"
    DS = "A tiny mechanical crab or spider that moves about when it is not being observed"
    DT = "A glass jar containing lard with a label that reads, 'Griffon Grease'"
    DU = "A wooden box with a ceramic bottom that holds a living worm with a head on each end of its body"
    DV = "A metal urn containing the ashes of a hero"
    Tri = [AA, AB, AC, AD, AE, AF, AG, AH, AI, AJ, AK, AL, AM, AN, AO, AP, AQ, AR, AS, AT, AU, AV, AW, AX, AY, AZ]
    TRI = random.choice(Tri)
    Trn = [BA, BB, BB, BD, BE, BF, BG, BH, BI, BJ, BK, BL, BM, BN, BO, BP, BQ, BR, BS, BT, BU, BV, BW, BX, BY, BZ]
    TRN = random.choice(Trn)
    Trk = [CA, CB, CB, CD, CE, CF, CG, CH, CI, CJ, CK, CL, CM, CN, CO, CP, CQ, CR, CS, CT, CU, CV, CW, CX, CY, CZ]
    TRK = random.choice(Trk)
    Trt = [DA, DB, DB, DD, DE, DF, DG, DH, DI, DJ, DK, DL, DM, DN, DO, DP, DQ, DR, DS, DT, DU, DV]
    TRT = random.choice(Trt)
    Trin = [TRI, TRN, TRK, TRT]
    Trinket = random.choice(Trin)
    EQP.append(Trinket)
    Trin.remove(Trinket)
    randtrk = False
    while not randtrk:
        try:
            Trinket2 = random.choice(Trin)
            randtrk = True
        except IndexError:
            Trinket2 = random.choice(Trin)
    if ((back == "Inheritor") and ((Inheritance == Inh2 or Inheritance == Inh3))):
        EQP.append(Trinket2)
    if param == "Y":        
        print(f"Your Charisma bonuses: {Charisma}")
        print(f"Your Constitution bonuses: {Constitution}") 
        print(f"Your Dexterity bonuses: {Dexterity}")
        print(f"Your Intelligence bonuses: {Intelligence}")
        print(f"Your Strength bonuses: {Strength}")
        print(f"Your Wisdom bonuses: {Wisdom}")
        
        print("Six Scores to choose from to apply to your abilities:")
    n=0
    Sums = []
    run = True
    while run:
        Value1 = d6()
        Value2 = d6()
        Value3 = d6()
        Value4 = d6()
        value = (Value1, Value2, Value3, Value4)
        for v in value:
            if v == 1:
                v = d6()
        Value = sorted(value)
        del Value[0]
        sum = 0
        for k in range(len(Value)):
            sum += Value[k]
        Sums.append(sum)
        n += 1
        if n >= 6:
            run = False
        #Figure out how to assign each sum to a value, and figure out what each value is assigned to, then after printing all 6, make sure to THEN ask what abilityscore to assign each value to, and make sure to set the score += the value shown, not just change it to the new value
    AbilityScoresList = ["Charisma", "Constitution", "Dexterity", "Intelligence", "Strength", "Wisdom"]
    if param == "Y":
        for i, sum in enumerate(Sums, 1):
            print(f"Score {i} to apply: {sum}")        
        print("0 - Random")        
        for i, option in enumerate(AbilityScoresList, 1):
            print(f"{i} - {option}")
        absc1 = int(input("Which ability score would you like to apply the first score to? "))
        if absc1 == 0:
            AbilityScoresListRand1 = random.choice(AbilityScoresList)
            if AbilityScoresListRand1 == "Charisma":
                Charisma += Sums[0]
            if AbilityScoresListRand1 == "Constitution":
                Constitution += Sums[0]
            if AbilityScoresListRand1 == "Dexterity":
                Dexterity += Sums[0]
            if AbilityScoresListRand1 == "Intelligence":
                Intelligence += Sums[0]
            if AbilityScoresListRand1 == "Strength":
                Strength += Sums[0]
            if AbilityScoresListRand1 == "Wisdom":
                Wisdom += Sums[0]
            AbilityScoresList.remove(AbilityScoresListRand1)
        elif 1 <= absc1 <= 6:
            first_absc_choice = AbilityScoresList[absc1 - 1]
            if first_absc_choice == "Charisma":
                Charisma += Sums[0]
            if first_absc_choice == "Constitution":
                Constitution += Sums[0]
            if first_absc_choice == "Dexterity":
                Dexterity += Sums[0]
            if first_absc_choice == "Intelligence":
                Intelligence += Sums[0]
            if first_absc_choice == "Strength":
                Strength += Sums[0]
            if first_absc_choice == "Wisdom":            
                Wisdom += Sums[0]
            AbilityScoresList.remove(first_absc_choice)
        print("0 - Random")        
        for i, option in enumerate(AbilityScoresList, 1):
            print(f"{i} - {option}")
        absc2 = int(input("Which ability score would you like to apply the second score to? "))
        if absc2 == 0:
            AbilityScoresListRand2 = random.choice(AbilityScoresList)
            if AbilityScoresListRand2 == "Charisma":
                Charisma += Sums[1]
            if AbilityScoresListRand2 == "Constitution":
                Constitution += Sums[1]
            if AbilityScoresListRand2 == "Dexterity":
                Dexterity += Sums[1]
            if AbilityScoresListRand2 == "Intelligence":
                Intelligence += Sums[1]
            if AbilityScoresListRand2 == "Strength":
                Strength += Sums[1]
            if AbilityScoresListRand2 == "Wisdom":
                Wisdom += Sums[1]
            AbilityScoresList.remove(AbilityScoresListRand2)
        elif 1 <= absc2 <= 5:
            second_absc_choice = AbilityScoresList[absc2 - 1]
            if second_absc_choice == "Charisma":
                Charisma += Sums[1]
            if second_absc_choice == "Constitution":
                Constitution += Sums[1]
            if second_absc_choice == "Dexterity":
                Dexterity += Sums[1]
            if second_absc_choice == "Intelligence":
                Intelligence += Sums[1]
            if second_absc_choice == "Strength":
                Strength += Sums[1]
            if second_absc_choice == "Wisdom":            
                Wisdom += Sums[1]
            AbilityScoresList.remove(second_absc_choice)        
        print("0 - Random")        
        for i, option in enumerate(AbilityScoresList, 1):
            print(f"{i} - {option}")
        absc3 = int(input("Which ability score would you like to apply the third score to? "))
        if absc3 == 0:
            AbilityScoresListRand3 = random.choice(AbilityScoresList)
            if AbilityScoresListRand3 == "Charisma":
                Charisma += Sums[2]
            if AbilityScoresListRand3 == "Constitution":
                Constitution += Sums[2]
            if AbilityScoresListRand3 == "Dexterity":
                Dexterity += Sums[2]
            if AbilityScoresListRand3 == "Intelligence":
                Intelligence += Sums[2]
            if AbilityScoresListRand3 == "Strength":
                Strength += Sums[2]
            if AbilityScoresListRand3 == "Wisdom":
                Wisdom += Sums[2]
            AbilityScoresList.remove(AbilityScoresListRand3)
        elif 1 <= absc3 <= 4:
            third_absc_choice = AbilityScoresList[absc3 - 1]
            if third_absc_choice == "Charisma":
                Charisma += Sums[2]
            if third_absc_choice == "Constitution":
                Constitution += Sums[2]
            if third_absc_choice == "Dexterity":
                Dexterity += Sums[2]
            if third_absc_choice == "Intelligence":
                Intelligence += Sums[2]
            if third_absc_choice == "Strength":
                Strength += Sums[2]
            if third_absc_choice == "Wisdom":            
                Wisdom += Sums[2]
            AbilityScoresList.remove(third_absc_choice)                    
        print("0 - Random")        
        for i, option in enumerate(AbilityScoresList, 1):
            print(f"{i} - {option}")
        absc4 = int(input("Which ability score would you like to apply the fourth score to? "))
        if absc4 == 0:
            AbilityScoresListRand4 = random.choice(AbilityScoresList)
            if AbilityScoresListRand4 == "Charisma":
                Charisma += Sums[3]
            if AbilityScoresListRand4 == "Constitution":
                Constitution += Sums[3]
            if AbilityScoresListRand4 == "Dexterity":
                Dexterity += Sums[3]
            if AbilityScoresListRand4 == "Intelligence":
                Intelligence += Sums[3]
            if AbilityScoresListRand4 == "Strength":
                Strength += Sums[3]
            if AbilityScoresListRand4 == "Wisdom":
                Wisdom += Sums[3]
            AbilityScoresList.remove(AbilityScoresListRand4)
        elif 1 <= absc4 <= 3:
            fourth_absc_choice = AbilityScoresList[absc4 - 1]
            if fourth_absc_choice == "Charisma":
                Charisma += Sums[3]
            if fourth_absc_choice == "Constitution":
                Constitution += Sums[3]
            if fourth_absc_choice == "Dexterity":
                Dexterity += Sums[3]
            if fourth_absc_choice == "Intelligence":
                Intelligence += Sums[3]
            if fourth_absc_choice == "Strength":
                Strength += Sums[3]
            if fourth_absc_choice == "Wisdom":            
                Wisdom += Sums[3]
            AbilityScoresList.remove(fourth_absc_choice)        
        print("0 - Random")        
        for i, option in enumerate(AbilityScoresList, 1):
            print(f"{i} - {option}")
        absc5 = int(input("Which ability score would you like to apply the fifth score to? "))
        if absc5 == 0:
            AbilityScoresListRand5 = random.choice(AbilityScoresList)
            if AbilityScoresListRand5 == "Charisma":
                Charisma += Sums[4]
            if AbilityScoresListRand5 == "Constitution":
                Constitution += Sums[4]
            if AbilityScoresListRand5 == "Dexterity":
                Dexterity += Sums[4]
            if AbilityScoresListRand5 == "Intelligence":
                Intelligence += Sums[4]
            if AbilityScoresListRand5 == "Strength":
                Strength += Sums[4]
            if AbilityScoresListRand5 == "Wisdom":
                Wisdom += Sums[4]
            AbilityScoresList.remove(AbilityScoresListRand5)
        elif 1 <= absc5 <= 2:
            fifth_absc_choice = AbilityScoresList[absc5 - 1]
            if fifth_absc_choice == "Charisma":
                Charisma += Sums[4]
            if fifth_absc_choice == "Constitution":
                Constitution += Sums[4]
            if fifth_absc_choice == "Dexterity":
                Dexterity += Sums[4]
            if fifth_absc_choice == "Intelligence":
                Intelligence += Sums[4]
            if fifth_absc_choice == "Strength":
                Strength += Sums[4]
            if fifth_absc_choice == "Wisdom":            
                Wisdom += Sums[4]
            AbilityScoresList.remove(fifth_absc_choice)        
        last_absc_choice = AbilityScoresList[0]
        if last_absc_choice == "Charisma":
            Charisma += Sums[5]
        if last_absc_choice == "Constitution":
            Constitution += Sums[5]
        if last_absc_choice == "Dexterity":
            Dexterity += Sums[5]
        if last_absc_choice == "Intelligence":
            Intelligence += Sums[5]
        if last_absc_choice == "Strength":
            Strength += Sums[5]
        if last_absc_choice == "Wisdom":            
            Wisdom += Sums[5]
    if param == "N":
            AbilityScoresListRand1 = random.choice(AbilityScoresList)
            if AbilityScoresListRand1 == "Charisma":
                Charisma += Sums[0]
            if AbilityScoresListRand1 == "Constitution":
                Constitution += Sums[0]
            if AbilityScoresListRand1 == "Dexterity":
                Dexterity += Sums[0]
            if AbilityScoresListRand1 == "Intelligence":
                Intelligence += Sums[0]
            if AbilityScoresListRand1 == "Strength":
                Strength += Sums[0]
            if AbilityScoresListRand1 == "Wisdom":
                Wisdom += Sums[0]
            AbilityScoresList.remove(AbilityScoresListRand1)
            AbilityScoresListRand2 = random.choice(AbilityScoresList)
            if AbilityScoresListRand2 == "Charisma":
                Charisma += Sums[1]
            if AbilityScoresListRand2 == "Constitution":
                Constitution += Sums[1]
            if AbilityScoresListRand2 == "Dexterity":
                Dexterity += Sums[1]
            if AbilityScoresListRand2 == "Intelligence":
                Intelligence += Sums[1]
            if AbilityScoresListRand2 == "Strength":
                Strength += Sums[1]
            if AbilityScoresListRand2 == "Wisdom":
                Wisdom += Sums[1]
            AbilityScoresList.remove(AbilityScoresListRand2)           
            AbilityScoresListRand3 = random.choice(AbilityScoresList)
            if AbilityScoresListRand3 == "Charisma":
                Charisma += Sums[2]
            if AbilityScoresListRand3 == "Constitution":
                Constitution += Sums[2]
            if AbilityScoresListRand3 == "Dexterity":
                Dexterity += Sums[2]
            if AbilityScoresListRand3 == "Intelligence":
                Intelligence += Sums[2]
            if AbilityScoresListRand3 == "Strength":
                Strength += Sums[2]
            if AbilityScoresListRand3 == "Wisdom":
                Wisdom += Sums[2]
            AbilityScoresList.remove(AbilityScoresListRand3)   
            AbilityScoresListRand4 = random.choice(AbilityScoresList)
            if AbilityScoresListRand4 == "Charisma":
                Charisma += Sums[3]
            if AbilityScoresListRand4 == "Constitution":
                Constitution += Sums[3]
            if AbilityScoresListRand4 == "Dexterity":
                Dexterity += Sums[3]
            if AbilityScoresListRand4 == "Intelligence":
                Intelligence += Sums[3]
            if AbilityScoresListRand4 == "Strength":
                Strength += Sums[3]
            if AbilityScoresListRand4 == "Wisdom":
                Wisdom += Sums[3]
            AbilityScoresList.remove(AbilityScoresListRand4)   
            AbilityScoresListRand5 = random.choice(AbilityScoresList)
            if AbilityScoresListRand5 == "Charisma":
                Charisma += Sums[4]
            if AbilityScoresListRand5 == "Constitution":
                Constitution += Sums[4]
            if AbilityScoresListRand5 == "Dexterity":
                Dexterity += Sums[4]
            if AbilityScoresListRand5 == "Intelligence":
                Intelligence += Sums[4]
            if AbilityScoresListRand5 == "Strength":
                Strength += Sums[4]
            if AbilityScoresListRand5 == "Wisdom":
                Wisdom += Sums[4]
            AbilityScoresList.remove(AbilityScoresListRand5)    
            AbilityScoresListRand6 = random.choice(AbilityScoresList)
            if AbilityScoresListRand6 == "Charisma":
                Charisma += Sums[5]
            if AbilityScoresListRand6 == "Constitution":
                Constitution += Sums[5]
            if AbilityScoresListRand6 == "Dexterity":
                Dexterity += Sums[5]
            if AbilityScoresListRand6 == "Intelligence":
                Intelligence += Sums[5]
            if AbilityScoresListRand6 == "Strength":
                Strength += Sums[5]
            if AbilityScoresListRand6 == "Wisdom":
                Wisdom += Sums[5]

    ChaMod = math.floor((Charisma-10)/2)
    ConMod = math.floor((Constitution-10)/2)
    DexMod = math.floor((Dexterity-10)/2)
    IntMod = math.floor((Intelligence-10)/2)
    StrMod = math.floor((Strength-10)/2)
    WisMod = math.floor((Wisdom-10)/2)
    ProfBonus = math.ceil(plLvl/4)+1
    Acrobatics = "Acrobatics"
    AnimalHandling = "Animal Handling"
    Arcana = "Arcana"
    Athletics = "Athletics"
    Deception = "Deception"
    History = "History"
    Insight = "Insight"
    Intimidation = "Intimidation"
    Investigation = "Investigation"
    Medicine = "Medicine"
    Nature = "Nature"
    Perception = "Perception"
    Performance = "Performance"
    Persuasion = "Persuasion"
    Religion = "Religion"
    SleightofHand = "Sleight of Hand"
    Stealth = "Stealth"
    Survival = "Survival"
    FeatTrait = OtherBackgroundInfo + RaceNotes    
    add_info_str = '\n'.join(f'- {item}' for item in AdditionalInfo)
    allies_str = '\n'.join(f'- {item}' for item in AlliesOrg)
    classlevel_str = "/".join(f"{item}" for item in Class)
    if subrace == "Chromatic Dragonborn":
        subrace = f"{color} + {subrace}"
    if subrace == "Gem Dragonborn":
        subrace = f"{gem} + {subrace}"
    if subrace == "Metallic Dragonborn":
        subrace = f"{metal} + {subrace}"
    if subrace == "Eladrin":
        subrace = f"{season} + {subrace}"   
    data = {
        'ClassLevel':classlevel_str + ' ' + str(plLvl),
        'Background':back,
        'PlayerName':playername,
        'CharacterName':charactername + f'({Gender})',
        'CharacterName 2':charactername + f'({Gender})',
        'Race ':subrace,
        'STR':str(Strength),
        'ProfBonus':str(ProfBonus),
        'AC':'10',
        'Initiative': str(DexMod),
        'Speed': str(walkingspeed),
        'PersonalityTraits ':Trait,
        'STRmod':str(StrMod),
        'DEX':str(Dexterity),
        'Ideals':Ideal,
        'DEXmod ':str(DexMod),
        'Bonds':Bond,
        'CON':str(Constitution),
        'CONmod':str(ConMod),
        'Flaws':Flaw,
        'INT':str(Intelligence),
        'INTmod':str(IntMod),        
        'WIS':str(Wisdom),        
        'WISmod':str(WisMod),
        'CHA':str(Charisma),        
        'CHamod':str(ChaMod),
        'GP':str(BGL),
        'Height':str(Height) + ' inches',
        'Weight':str(Weight) + ' pounds',
        'Allies':allies_str,
        'Feat+Traits':add_info_str,
        }
    dndchargen_characterbuilder(param, plLvl, playername, charactername, race, Class, subclass, submulticlass, BeachballFlag, BGL, EQP, SkillsProf, PlProf, PlLang, SLANG, Notes, data, skills_dict, FeatTrait)

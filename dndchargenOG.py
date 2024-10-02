import random

para = input("Set parameters? Y/N ")
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
Gen = ["Male", "Female"]
if param == "Y":
    print("0 - Random")
    print("1 - Male")
    print("2 - Female")
    gend = input("Sex? ")
    if gend == "1":
        Gender = "Male"
    if gend == "2":
        Gender = "Female"
    if gend == "0":
        Gender = random.choice(Gen)
if param == "N":
    Gender = random.choice(Gen)
sex = Gender
Dra = ["Black Scale Dragonborn", "Blue Scale Dragonborn", "Brass Scale Dragonborn", "Bronze Scale Dragonborn", "Copper Scale Dragonborn", "Gold Scale Dragonborn", "Green Scale Dragonborn", "Red Scale Dragonborn", "Silver Scale Dragonborn", "White Scale Dragonborn"]
Drag = random.choice(Dra)
Dwf = ["Mountain Dwarf", "Hill Dwarf"]
Dwar = random.choice(Dwf)
El = ["Dark Elf", "Ground Elf", "High Elf", "Wood Elf"]
Elf = random.choice(El)
Ge = ["Air Genasi", "Earth Genasi", "Fire Genasi", "Water Genasi"]
Genasi = random.choice(Ge)
Gn = ["Desert Gnome", "Forest Gnome", "Rock Gnome", "Svirfneblin Gnome"]
Gnome = random.choice(Gn)
Hal = ["Lightfoot Halfling", "Stout Halfling"]
Half = random.choice(Hal)
Hum = ["Human", "Variant Human"]
Human = random.choice(Hum)
rac = ["Aarakocra", Drag, Dwar, Elf, Genasi, Gnome, "Goliath", "Half-Elf", Half, "Half-Orc", Human, "Tiefling"]
if param == "Y":
    print("0 - Random")
    print("1 - Aarakocra")
    print("2 - Dragonborn")
    print("3 - Dwarf")
    print("4 - Elf")
    print("5 - Genasi")
    print("6 - Gnome")
    print("7 - Goliath")
    print("8 - Half-Elf")
    print("9 - Halflling")
    print("10 - Half-Orc")
    print("11 - Human")
    print("12 - Tiefling")

    rce = input("Race? ")
    if rce == "1":
        race = "Aarakocra"
    if rce == "2":
        race = Drag
    if rce == "3":
        race = Dwar
    if rce == "4":
        race = Elf
    if rce == "5":
        race = Genasi
    if rce == "6":
        race = Gnome
    if rce == "7":
        race = "Goliath"
    if rce == "8":
        race = "Half-Elf"
    if rce == "9":
        race = Half
    if rce == "10":
        race = "Half-Orc"
    if rce == "11":
        race = Human
    if rce == "12":
        race = "Tiefling"
    if rce == "0":
        race = random.choice(rac)
if param == "N":
    race = random.choice(rac)
Aara = " Aarakocra,"
Drac = " Draconic,"
Dwarvi = " Dwarvish,"
Elvi = " Elvish,"
Gian = " Giant,"
Gnom = " Gnomish,"
Gobl = " Goblin,"
Hafl = " Hafling,"
Orc = " Orc,"
Aura = " Auran,"
Infe = " Infernal,"
Prim = " Primordial,"
SLANG = [Aara, Dwarvi, Elvi, Gian, Gobl, Hafl, Orc]
Rlang2 = random.choice(SLANG)
if race == "Aarakocra":
    Hmo1 = random.randint(1, 4)
    Hmo2 = random.randint(1, 4)
    Hmod = Hmo1 + Hmo2
    Hbase = 58
    Wmo1 = random.randint(1, 10)
    Wmo2 = random.randint(1, 10)
    Wbase = 80
    Rlang = Aara + Aura
    Hilang = ""
if race == Drag:
    Hmo1 = random.randint(1, 10)
    Hmo2 = random.randint(1, 10)
    Hmod = Hmo1 + Hmo2
    Hbase = 66
    Wmo1 = random.randint(1, 6)
    Wmo2 = random.randint(1, 6)
    Wbase = 175
    Rlang = Drac
    Hilang = ""
if race == Dwar:
    if Dwar == "Mountain Dwarf":
        Hmo1 = random.randint(1, 4)
        Hmo2 = random.randint(1, 4)
        Hmod = Hmo1 + Hmo2
        Hbase = 48
        Wmo1 = random.randint(1, 6)
        Wmo2 = random.randint(1, 6)
        Wbase = 115
    if Dwar == "Hill Dwarf":
        Hmo1 = random.randint(1, 4)
        Hmo2 = random.randint(1, 4)
        Hbase = 44
        Wmo1 = random.randint(1, 6)
        Wmo2 = random.randint(1, 6)
        Wbase = 115
    Rlang = Dwarvi
    Hilang = ""
if race == Elf:
    if Elf == "Dark Elf":
        Hmo1 = random.randint(1, 6)
        Hmo2 = random.randint(1, 6)
        Hbase = 44
        Wmo1 = random.randint(1, 6)
        Wmo2 = random.randint(1, 6)
        Wbase = 75
        Hilang = ""
    if Elf == "Ground Elf":
        Hmo1 = random.randint(1, 4)
        Hmo2 = random.randint(1, 4)
        Hbase = 60
        Wmo1 = random.randint(1, 4)
        Wmo2 = random.randint(1, 4)
        Wbase = 100
        Hilang = ""
    if Elf == "High Elf":
        Hmo1 = random.randint(1, 10)
        Hmo2 = random.randint(1, 10)
        Hbase = 90
        Wmo1 = random.randint(1, 4)
        Wmo2 = random.randint(1, 4)
        Wbase = 100
        Hilang = Rlang2
    if Elf == "Wood Elf":
        Hmo1 = random.randint(1, 10)
        Hmo2 = random.randint(1, 10)
        Hbase = 90
        Wmo1 = random.randint(1, 4)
        Wmo2 = random.randint(1, 4)
        Wbase = 100
        Hilang = ""
    Rlang = Elvi
if race == Genasi:
    Hmo1 = random.randint(1, 10)
    Hmo2 = random.randint(1, 10)
    Hbase = 56
    Wmo1 = random.randint(1, 4)
    Wmo2 = random.randint(1, 4)
    Wbase = 110
    Rlang = Prim
    Hilang = ""
if race == Gnome:
    Hmo1 = random.randint(1, 4)
    Hmo2 = random.randint(1, 4)
    Hbase = 31
    Wmo1 = 1
    Wmo2 = 0
    Wbase = 35
    Rlang = Gnom
    Hilang = ""
if race == "Goliath":
    Hmo1 = random.randint(1, 6)
    Hmo2 = random.randint(1, 6)
    Hbase = 84
    Wmo1 = random.randint(1, 4)
    Wmo2 = random.randint(1, 4)
    Wbase = 140
    Rlang = Gian
    Hilang = ""
if race == "Half-Elf":
    Hmo1 = random.randint(1, 8)
    Hmo2 = random.randint(1, 8)
    Hbase = 57
    Wmo1 = random.randint(1, 4)
    Wmo2 = random.randint(1, 4)
    Wbase = 110
    Rlang = Elvi
    Hilang = ""
if race == Half:
    Hmo1 = random.randint(1, 6)
    Hmo2 = random.randint(1, 6)
    Hbase = 28
    Wmo1 = 1
    Wmo2 = 0
    Wbase = 35
    Rlang = Hafl
    Hilang = ""
if race == "Half-Orc":
    Hmo1 = random.randint(1, 10)
    Hmo2 = random.randint(1, 10)
    Hbase = 58
    Wmo1 = random.randint(1, 6)
    Wmo2 = random.randint(1, 6)
    Wbase = 140
    Rlang = Orc
    Hilang = ""
if race == Human:
    Hmo1 = random.randint(1, 10)
    Hmo2 = random.randint(1, 10)
    Hbase = 56
    Wmo1 = random.randint(1, 4)
    Wmo2 = random.randint(1, 4)
    Wbase = 110
    Rlang = Rlang2
    Hilang = ""
if race == "Tiefling":
    Hmo1 = random.randint(1, 8)
    Hmo2 = random.randint(1, 8)
    Hbase = 57
    Wmo1 = random.randint(1, 4)
    Wmo2 = random.randint(1, 4)
    Wbase = 110
    Rlang = Infe
    Hilang = ""
if Rlang in SLANG:
    SLANG.remove(Rlang)
if Hilang in SLANG:
    SLANG.remove(Hilang)
Randl = random.choice(SLANG)
SLANG.remove(Randl)
Rand2 = random.choice(SLANG)
Randl2 = str(Rand2)
Hmod = Hmo1 + Hmo2
Wmod = Wmo1 + Wmo2
tl = Hmod + Hbase
Wemod = Wmod*Hmod
hy = Wbase + Wemod
Height = str(tl)
Weight = str(hy)


Cri = ["Criminal", "Spy (Criminal Variant)"]
Criminal = random.choice(Cri)
Ent = ["Entertainer", "Gladiator (Entertainer Variant)"]
Entertainer = random.choice(Ent)
GA = ["Guild Artisan","Guild Merchant (Guild Artisan Variant)"]
Gui = random.choice(GA)
No = ["Noble", "Knight (Noble Variant)"]
Nob = random.choice(No)
SA = ["Sailor", "Pirate (Sailor Variant)"]
Sai = random.choice(SA)

Background = ["Acolyte", "Charlatan", Criminal, Entertainer, "Folk Hero", Gui, "Hermit", Nob, "Outlander", "Sage", Sai, "Soldier", "Urchin"]
Arti = ["Alchemist Speciliast Artificer", "Armorist Speciliast Artificer", "Artilierist Speciliast Artificer", "Battle Smith Speciliast Artificer"]
Artificer = random.choice (Arti)
Barb = ["Path of the Ancestral Guardian Barbarian", "Path of the Battleranger Barbarian", "Path of the Berserker Barbarian", "Path of the Storm Herold Barbarian", "Path of the Totem Warrior Barbarian", "Path of the Zelot Barbarian"]
Barbarian = random.choice(Barb)
Bar = ["College of Glamor Bard", "College of Lore Bard", "College of Satire Bard", "College of Sword Bard", "College of Valor Bard", "College of Whispers Bards"]
Bard = random.choice(Bar)
Cle = ["Death Domain Cleric", 'Forge Domain Cleric', "Grave Domain Cleric", "Knowledge Domain Cleric", "Life Domain Cleric", "Light Domain Cleric", "Nature Domain Cleric", "Order Domain Cleric", "Tempest Domain Cleric", "Trickery Domain Cleric", "War Domain Cleric", "Zeal Domain Cleric"]
Cleric = random.choice(Cle)
Dru = ["Circle of Dreams Druid", "Circle of Land Druid", "Circle of the Moon Druid", "Circle of the Sheppard Druid"]
Druid = random.choice(Dru)
Fig = ["Arcane Archer Archetype Fighter", "Battle Master Archetype Fighter", "Cavalier Archetype Fighter", "Champion Archetype Fighter", "Eldrich Knight Archetype Fighter", "Samurai Archetype Fighter"]
Fighter = random.choice(Fig)
Mon = ["Way of the Drunken Warrior Monk", "Way of the Four Elements Monk", "Way of the Kensei Monk", "Way of the Open Hand Monk", "Way of the Shadow Monk", "Way of the Sun Soul Monk"]
Monk = random.choice(Mon)
Pal= ["Oath of the Ancients Paladin", "Oath of Conquest Paladin", "Oath of the Crown Paladin", "Oath of Devotion Paladin", "Oath of Redemption Paladin", "Oath of Vengeance Paladin"]
Paladin = random.choice(Pal)
Ran = ["Beast Master Archetype Ranger", "Gloom Stalker Archetype Ranger", "Horizon Walker Archetype Ranger", "Hunter Archetype Ranger", "Monster Slayer Archetype Ranger", "Shooting Star Archetype Ranger"]
Ranger = random.choice(Ran)
Rog = ["Arcane Trickster Archetype Rogue", "Assassin Archetype Rogue", "Inquisitive Archetype Rogue", "Mastermind Archetype Rogue", "Mountebank Archetype Rogue", "Scout Archetype Rogue", "Swashbuckler Archetype Rogue", "Thief Archetype Rogue"]
Rogue = random.choice(Rog)
Sor = ["Draconic Bloodline Origin Sorcerer", "Divine Soul Origin Sorcerer", "Phoenix Origin Sorcerer", "Sea Origin Sorcerer", "Shadow Origin Sorcerer", "Stone Origin Sorcerer", "Storm Origin Sorcerer", "Wild Magic Origin Sorcerer"]
Sorcerer = random.choice(Sor)
War = ["Ancient Dragon Patron Warlock", "Archfey Patron Warlock", "Celestial Patron Warlock", "Fiend Patron Warlock", "Mysterious Feline Patron Warlock", "Great Old One Patron Warlock", "Hexblade Patron Warlock", "Queen of Spiders Patron Warlock", "Raven Queen Patron Warlock", "Serpent Patron Warlock"]
Warlock = random.choice(War)
Wiz = ["Abjuration Arcane Tradition Wizard", "Conjuration Arcane Tradition Wizard", "Divination Arcane Tradition Wizard", "Evocation Arcane Tradition Wizard", "Illusion Arcane Tradition Wizard", "Necromancy Arcane Tradition Wizard", "Transmutation Arcane Tradition Wizard", "War Arcane Tradition Wizard"]
Wizard = random.choice(Wiz)
Clas = [Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard]
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
        Class = Artificer
    if cla == "2":
        Class = Barbarian
    if cla == "3":
        Class = Bard
    if cla == "4":
        Class = Cleric
    if cla == "5":
        Class = Druid
    if cla == "6":
        Class = Fighter
    if cla == "7":
        Class = Monk
    if cla == "8":
        Class = Paladin
    if cla == "9":
        Class = Ranger
    if cla == "10":
        Class = Rogue
    if cla == "11":
        Class = Sorcerer
    if cla == "12":
        Class = Warlock
    if cla == "13":
        Class = Wizard
    if cla == "0":
        Class = random.choice(Clas)    
if param == "N":
    Class = random.choice(Clas)
if param == "Y":
    print("0 - random")
    print("1 - Acolyte")
    print("2 - Charlatan")
    print("3 - Criminal")
    print("4 - Entertainer")
    print("5 - Folk Hero")
    print("6 - Guild Artisan")
    print("7 - Hermit")
    print("8 - Noble")
    print("9 - Outlander")
    print("10 - Sage")
    print("11 - Sailor")
    print("12 - Soldier")
    print("13 - Urchin")
    bkg = input("Background? ")
    if bkg == "1":
        back = "Acolyte"
    if bkg == "2":
        back = "Charlatan"
    if bkg == "3":
        back = Criminal
    if bkg == "4":
        back = Entertainer
    if bkg == "5":
        back = "Folk Hero"
    if bkg == "6":
        back = Gui
    if bkg == "7":
        back = "Hermit"
    if bkg == "8":
        back = Nob
    if bkg == "9":
        back = "Outlander"
    if bkg == "10":
        back = "Sage"
    if bkg == "11":
        back = Sai
    if bkg == "12":
        back = "Soldier"
    if bkg == "13":
        back = "Urchin"
    if bkg == "0":
        back = random.choice(Background)
if param == "N":
    back = random.choice(Background)
print("You are a " + Gender + " " + race)
print ("Your height is " + Height + " inches")
print ("Your weight is " + Weight + " pounds")
print ("Your Class is " + Class)
print ("Your background is " + back)

if back == "Acolyte":
    P1 = "I Idolize a particular hero of my faith, and constantly refer to that person’s deeds and example."
    P2 = "I can find common ground between the fiercest enemies, empathizing with them and always working towards peace."
    P3 = "I see omens in every event and action. The gods try to speak to us, we just need to listen."
    P4 = "Nothing can shake my optimistic attitude."
    P5 = "I quote (or misquote) sacred texts and proverbs in almost every situation."
    P6 = "I am tolerant of other faiths and respect the worship of other gods."
    P7 = "I have enjoyed fine food, drink, and high society among my temple’s elite. Rough living grates on me."
    P8 = "I have spent so long in the temple that I have little practical experience dealing with people in the outside world."
    PTR = [P1,P2, P3, P4, P5, P6, P7, P8]
    Trait = random.choice(PTR)
    I1 = "Tradition - The ancient traditions of worship and sacrifice must be upheld."
    I2 = "Charity - I always try to help those in need, no matter what the personal cost."
    I3 = "Change - We must help to bring about the changes the gods are constantly working in the world."
    I4 = "Power - I hope to one day rise to top of my faith’s religious hierarchy."
    I5 = "Faith - I trust that my deity will guide my actions. I have faith that if I work hard, things will go well."
    I6 = "Aspiration - I seek to prove myself worthy of my god’s favor, by matching my actions against his or her teachings."
    IDE = [I1, I2, I3, I4, I5, I6]
    Ideal = random.choice(IDE)
    B1 = "I would die to recover an ancient relic of my faith that was lost long ago."
    B2 = "I will someday get revenge on the corrupt temple hierarchy who branded me a heretic."
    B3 = "I owe my life to the priest who took me in when my parents died."
    B4 = "Everything I do is for the common people."
    B5 = "I will do anything to protect the temple where I served."
    B6 = "I seek to preserve a sacred text that my enemies considered heretical and seek to destroy."
    BND = [B1, B2, B3, B4, B5, B6]
    Bond = random.choice(BND)
    F1 = "I judge others harshly, and myself even more severely."
    F2 = "I put too much trust in those who wield power with my temple's hierarchy."
    F3 = "My piety sometimes leads me to blindly trust those that profess faith in my god."
    F4 = "I am inflexible in my thinking."
    F5 = "I am suspicious of strangers and expect the worst of them."
    F6 = "Once I pick a goal, I become obsessed with it to the detriment of everything else in my life."
    FLA = [F1, F2, F3, F4, F5, F6]
    Flaw = random.choice(FLA)
    BGL = 15
    print ("You personality trait: " +  Trait )
    print ("Your ideal: " + Ideal)
    print ("Your bond: " + Bond)
    print ("Your flaw: " + Flaw)
    print("You speak Common," , Rlang , Hilang , Randl, Randl2)
if back == "Charlatan":
    S1 = "I cheat at games of chance."
    S2 = "I shave coins or forge documents."
    S3 = "I insinuate myself into people is lives to prey on their weaknesses, and secure their fortunes."
    S4 = "I put on new identities like clothes."
    S5 = "I run sleight-of-hand cons on street corners."
    S6 = "I convince people that worthless junk is worth their hard-earned money."
    SCM = [S1, S2, S3, S4, S5, S6]
    Scam = random.choice(SCM)
    P1 = "I fall in and out of love easily, and am always pursuing someone."
    P2 = "I have a joke for every occasion, especially occasions where humor is inappropriate."
    P3 = "Flattery is my preferred trick for getting what I want."
    P4 = "I am a born gambler who cannot resist taking a risk for potential payout."
    P5 = "I lie about almost everything, even when there is no good reason to."
    P6 = "Sarcasm and insults are my weapons of choice."
    P7 = "I keep multiple holy symbols on me and invoke whatever deity might come in useful at any given time."
    P8 = "I pocket anything I see that might have some value."
    PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
    Trait = random.choice(PTR)
    I1 = "Independence - I am a free spirit, no one tells me what to do."
    I2 = "Fairness - I never target people who can not afford to lose a few coins."
    I3 = "Charity - I distribute the money I acquire to the people who really need it."
    I4 = "Creativity - I never run the same con twice."
    I5 = "Friendship - Material goods come and go. Bonds of friendship last forever."
    I6 = "Aspiration - I am determined to make something of myself."
    IDE = [I1, I2, I3, I4, I5, I6]
    Ideal = random.choice(IDE)
    B1 = "I fleeced the wrong person and must work to ensure that this individual never crosses paths with me or those I care about."
    B2 = "I owe everything to my mentor, a horrible person who is probably rotting in jail somewhere."
    B3 = "Somewhere out there, I have a child who does not know me. I am making the world better for him or her."
    B4 = "I come from a noble family and one day I will reclaim my lands and title from those who stole them from me."
    B5 = "A powerful person killed someone I loved. Someday soon, I will have my revenge."
    B6 = "I swindled and ruined a person who did not deserve it. I seek to atone for my misdeeds but might never be able to forgive myself. "
    BND = [B1, B2, B3, B4, B5, B6]
    Bond = random.choice(BND)
    F1 = "I cannot resist a pretty face."
    F2 = "I am always in debt. I spend my ill-gotten gains on decadent luxuries faster than I bring them in."
    F3 = "I am convinced that no one could ever fool me the way I fool others."
    F4 = "I am too greedy for my own good. I cannot resist taking a risk if there’s money involved."
    F5 = "I cannot resist swindling people who are more powerful than me."
    F6 = "I hate to admit and will hate myself for it, but I will run and hide to preserve my own hide if the going gets tough."
    FLA = [F1, F2, F3, F4, F5, F6]
    Flaw = random.choice(FLA)
    BGL = 15
    print ("Your favored scam: " + Scam)
    print("You personality trait: " + Trait)
    print("Your ideal: " + Ideal)
    print("Your bond: " + Bond)
    print("Your flaw: " + Flaw)
    print("You speak Common," + Rlang + Hilang)
if back == Criminal:
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
    P1 = "I always have a plan for what to do when things go wrong."
    P2 = "I am always calm, no matter what the situation. I never raise my voice or let my emotions control me."
    P3 = "The first thing I do in a new place is note the locations of everything valuable, or where such things could be hidden."
    P4 = "I would rather make a new friend than a new enemy."
    P5 = "I am incredibly slow to trust. Those who seem the fairest often have the most to hide."
    P6 = "I do not pay attention to the risks in a situation. Never tell me the odds."
    P7 = "The best way to get me to do something is to tell me I cannot do it."
    P8 = "I blow up at the slightest insult."
    PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
    Trait = random.choice(PTR)
    I1 = "Honor - I do not steal from others in the trade."
    I2 = "Freedom - Chains are meant to be broken, as are those who would forge them."
    I3 = "Charity - I steal from the wealthy so that I can help people in need."
    I4 = "Greed -  I will do whatever it takes to become wealthy."
    I5 = "People - I am loyal to my friends, not to any ideals, and everyone else can take a trip down the Styx for all I care. "
    I6 = "Redemption - There is a spark of good in everyone. "
    IDE = [I1, I2, I3, I4, I5, I6]
    Ideal = random.choice(IDE)
    B1 = "I am trying to pay off an old debt I owe to a generous benefactor."
    B2 = "My ill-gotten gains go to support my family."
    B3 = "Something important was taken from me, and I aim to steal it back."
    B4 = "I will become the greatest thief that ever lived."
    B5 = "I am guilty of a terrible crime. I hope I can redeem myself for it."
    B6 = "Someone I loved died because of a mistake I made. That will never happen again."
    BND = [B1, B2, B3, B4, B5, B6]
    Bond = random.choice(BND)
    F1 = "When I see something valuable, I can not think about anything but how to steal it."
    F2 = "When faced with a choice between money and my friends, I usually choose the money."
    F3 = "If there is a plan, I will forget it. If I do not forget it, I will ignore it."
    F4 = "I have a 'tell' that reveals when I am lying."
    F5 = "I turn tail and run when things look bad."
    F6 = "An innocent person is in prison for a crime that I committed. I am okay with that."
    FLA = [F1, F2, F3, F4, F5, F6]
    Flaw = random.choice(FLA)
    BGL = 15
    print ("Your criminal speciality: " + Specialty)
    print("You personality trait: " + Trait)
    print("Your ideal: " + Ideal)
    print("Your bond: " + Bond)
    print("Your flaw: " + Flaw)
    print ("You speak Common," + Rlang + Hilang)
if back == Entertainer:
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
    P1 = "I know a story relevant to almost every situation."
    P2 = "Whenever I come to a new place, I collect local rumors and spread gossip."
    P3 = "I'm a hopeless romantic, always searching for that 'special someone'."
    P4 = "Nobody stays angry at me or around me for long, since I can defuse any amount of tension."
    P5 = "I love a good insult, even one directed at me."
    P6 = "I get bitter if I'm not the center of attention."
    P7 = "I'll settle for nothing less than perfection."
    P8 = "I change my mood or my mind as quickly as I change key in a song."
    PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
    Trait = random.choice(PTR)
    I1 = "Beauty - When I perform, I make the world better than it was."
    I2 = "Tradition - The stories, legends, and songs of the past must never be forgotten, for they teach us who we are."
    I3 = "Creativity - The world is in need of new ideas and bold action."
    I4 = "Greed - I'm only in it for the money and fame."
    I5 = "People - I like seeing the smiles on people's faces when I perform. That's all that matters. "
    I6 = "Honesty - Art should reflect the soul; it should come from within and reveal who we really are. "
    IDE = [I1, I2, I3, I4, I5, I6]
    Ideal = random.choice(IDE)
    B1 = "My instrument is my most treasured possession, and it reminds me of someone I love."
    B2 = "Someone stole my precious instrument, and someday I'll get it back."
    B3 = "I want to be famous, whatever it takes."
    B4 = "I idolize a hero of the old tales and measure my deeds against that person's."
    B5 = "I will do anything to prove myself superior to my hated rival."
    B6 = "I would do anything for the other members of my old troupe."
    BND = [B1, B2, B3, B4, B5, B6]
    Bond = random.choice(BND)
    F1 = "I'll do anything to win fame and renown."
    F2 = "I'm a sucker for a pretty face."
    F3 = "A scandal prevents me from ever going home again. That kind of trouble seems to follow me around."
    F4 = "I once satirized a noble who still wants my head. It was a mistake that I will likely repeat."
    F5 = "I have trouble keeping my true feelings hidden. My sharp tongue lands me in trouble."
    F6 = "Despite my best efforts, I am unreliable to my friends."
    FLA = [F1, F2, F3, F4, F5, F6]
    Flaw = random.choice(FLA)
    BGL = 15
    print ("Your entertainer routine: " + Routine)
    print("You personality trait: " + Trait)
    print("Your ideal: " + Ideal)
    print("Your bond: " + Bond)
    print("Your flaw: " + Flaw)
    print("You speak Common," + Rlang + Hilang)
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
    P1 = "I judge people by their actions, not their words."
    P2 = "If someone is in trouble, I am always ready to lend help."
    P3 = "When I set my mind to something, I follow through no matter what gets in my way."
    P4 = "I have a strong sense of fair play and always try to find the most equitable solution to arguments."
    P5 = "I am confident in my own abilities and do what I can to instill confidence in others."
    P6 = "Thinking is for other people. I prefer action."
    P7 = "I misuse long words in an attempt to sound smarter."
    P8 = "I get bored easily. When am I going to get on with my destiny?"
    PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
    Trait = random.choice(PTR)
    I1 = "Respect - People deserve to be treated with dignity and respect. "
    I2 = "Fairness - No one should get preferential treatment before the law, and no one is above the law. "
    I3 = "Freedom - Tyrants must not be allowed to oppress the people. "
    I4 = "Might - If I become strong, I can take what I want, what I deserve."
    I5 = "Sincerity - There is no good in pretending to be something I am not. "
    I6 = "Destiny - Nothing and no one can steer me away from my higher calling. "
    IDE = [I1, I2, I3, I4, I5, I6]
    Ideal = random.choice(IDE)
    B1 = "I have a family, but I have no idea where they are. One day, I hope to see them again."
    B2 = "I worked the land, I love the land, and I will protect the land."
    B3 = "A proud noble once gave me a horrible beating, and I will take my revenge on any bully I encounter."
    B4 = "My tools are symbols of my past life, and I carry them so that I will never forget my roots."
    B5 = "I protect those who cannot protect themselves."
    B6 = "I wish my childhood sweetheart had come with me to pursue my destiny."
    BND = [B1, B2, B3, B4, B5, B6]
    Bond = random.choice(BND)
    F1 = "The tyrant who rules my land will stop at nothing to see me killed."
    F2 = "I am convinced of the significance of my destiny, and blind to my shortcomings and the risk of failure."
    F3 = "The people who knew me when I was young know my shameful secret, so I can never go home again."
    F4 = "I have a weakness for the vices of the city, especially hard drink."
    F5 = "Secretly, I believe that things would be better if I were a tyrant lording over the land."
    F6 = "I have trouble trusting in my allies."
    FLA = [F1, F2, F3, F4, F5, F6]
    Flaw = random.choice(FLA)
    BGL = 10
    print ("Your defining event: " + Event)
    print("You personality trait: " + Trait)
    print("Your ideal: " + Ideal)
    print("Your bond: " + Bond)
    print("Your flaw: " + Flaw)
    print("You speak Common," + Rlang + Hilang)
if back == Gui:
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
    P1 = "I believe that anything worth doing is worth doing right. I ca not help it – I am a perfectionist."
    P2 = "I'm a snob who looks down on those who can't appreciate fine art."
    P3 = "I always want to know how things work and what makes people tick."
    P4 = "I'm full of witty aphorisms and have a proverb for every occasion."
    P5 = "I'm rude to people who lack my commitment to hard work and fair play."
    P6 = "I like to talk at length about my profession."
    P7 = "I don't part with my money easily and will haggle tirelessly to get the best deal possible."
    P8 = "I'm well known for my work, and I want to make sure everyone appreciates it. I'm always taken aback when people haven't heard of me."
    PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
    Trait = random.choice(PTR)
    I1 = "I'll do anything to get my hands on something rare or priceless."
    I2 = "I'm quick to assume that someone is trying to cheat me."
    I3 = "No one must ever learn that I once stole money from guild coffers."
    I4 = "I am never satisfied with what I have – I always want more."
    I5 = "I would kill to acquire a noble title."
    I6 = "I'm terribly jealous of anyone who can outshine my handiwork. Everywhere I go, I'm surrounded by rivals."
    IDE = [I1, I2, I3, I4, I5, I6]
    Ideal = random.choice(IDE)
    B1 = "Community - It is the duty of all civilized people to strengthen the bonds of community and the security of civilization."
    B2 = "Generosity - My talents were given to me so that I could use them to benefit the world. "
    B3 = "Freedom - Everyone should be free to pursue his or her own livelihood. "
    B4 = "Greed - I'm only in it for the money. "
    B5 = "People - I'm committed to the people I care about, not to ideals. "
    B6 = "Aspiration - I work hard to be the best there is at my craft."
    BND = [B1, B2, B3, B4, B5, B6]
    Bond = random.choice(BND)
    F1 = "The workshop where I learned my trade is the most important place in the world to me."
    F2 = "I created a great work for someone, and then found them unworthy to receive it. I'm still looking for someone worthy."
    F3 = "I owe my guild a great debt for forging me into the person I am today."
    F4 = "I pursue wealth to secure someone's love."
    F5 = "One day I will return to my guild and prove that I am the greatest artisan of them all."
    F6 = "I will get revenge on the evil forces that destroyed my place of business and ruined my livelihood."
    FLA = [F1, F2, F3, F4, F5, F6]
    Flaw = random.choice(FLA)
    BGL = 15
    print("Your Guild Business: " + Business)
    print("You personality trait: " + Trait)
    print("Your ideal: " + Ideal)
    print("Your bond: " + Bond)
    print("Your flaw: " + Flaw)
    print("You speak Common," , Rlang , Randl,  Randl2 , Hilang)
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
    P1 = "I have been isolated for so long that I speak rarely, preferring gestures and also the occasional grunt."
    P2 = "I am utterly serene, even in the face of disaster."
    P3 = "The leader of my community had something wise to say on every topic, and I am eager to share that wisdom."
    P4 = "I feel tremendous empathy for all who suffer."
    P5 = "I am oblivious to etiquette and social expectations."
    P6 = "I connect everything that happens to me to a grand, cosmic plan."
    P7 = "I often get lost in my own thoughts and contemplation, becoming oblivious to my surroundings."
    P8 = "I am working on a grand philosophical theory and love sharing my ideas."
    PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
    Trait = random.choice(PTR)
    I1 = "Greater Good.- My gifts are meant to be shared with all, not used for my own benefit. "
    I2 = "Logic - Emotions must not cloud our sense of what is right and true, or our logical thinking. "
    I3 = "Free Thinking - Inquiry and curiosity are the pillars of progress. "
    I4 = "Power - Solitude and contemplation are paths toward mystical or magical power."
    I5 = "Live and Let Live - Meddling in the affairs of others only causes trouble."
    I6 = "Self-Knowledge-  If you know yourself, there is nothing left to know."
    IDE = [I1, I2, I3, I4, I5, I6]
    Ideal = random.choice(IDE)
    B1 = "Nothing is more important than the other members of my hermitage, order, or association."
    B2 = "I entered seclusion to hide from the ones who might still be hunting me. I must someday confront them."
    B3 = "I am still seeking the enlightenment I pursued in my seclusion, and it still eludes me."
    B4 = "I entered seclusion because I loved someone I could not have."
    B5 = "Should my discovery come to light, it could bring ruin to the world."
    B6 = "My isolation gave me great insight into a great evil that only I can destroy."
    BND = [B1, B2, B3, B4, B5, B6]
    Bond = random.choice(BND)
    F1 = "Now that I've returned to the world, I enjoy its delights a little too much"
    F2 = "I harbor dark, bloodthirsty thoughts that my isolation and meditation failed to quell."
    F3 = "I am dogmatic in my thoughts and philosophy."
    F4 = "I let my need to win arguments overshadow friendships and harmony."
    F5 = "I would risk too much to uncover a lost bit of knowledge."
    F6 = "I like keeping secrets and will not share them with anyone."
    FLA = [F1, F2, F3, F4, F5, F6]
    Flaw = random.choice(FLA)
    BGL = 5
    print ("Your life of seclusion: " + Seclusion)
    print("You personality trait: " + Trait)
    print("Your ideal: " + Ideal)
    print("Your bond: " + Bond)
    print("Your flaw: " + Flaw)
    print("You speak Common," + Rlang + Hilang)
if back == Nob:
    P1 = "My eloquent flattery makes everyone I talk to feel like the most wonderful and important person in the world."
    P2 = "The common folk love me for my kindness and generosity."
    P3 = "No one could doubt by looking at my regal bearing that I am a cut above the unwashed masses."
    P4 = "I take great pains to always look my best and follow the latest fashions."
    P5 = "I do not like to get my hands dirty, and I will not be caught dead in unsuitable accommodations."
    P6 = "Despite my noble birth, I do not place myself above other folk. We all have the same blood."
    P7 = "My favor, once lost, is lost forever."
    P8 = "If you do me an injury, I will crush you, ruin your name, and salt your fields."
    PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
    Trait = random.choice(PTR)
    I1 = "Respect - Respect is due to me because of my position, but all people regardless of station deserve to be treated with dignity."
    I2 = "Responsibility - It is my duty to respect the authority of those above me, just as those below me must respect mine."
    I3 = "Independence - I must prove that I can handle myself without the coddling of my family. "
    I4 = "Power - If I can attain more power, no one will tell me what to do. "
    I5 = "Family - Blood runs thicker than water. "
    I6 = "Noble Obligation -  It is my duty to protect and care for the people beneath me. "
    IDE = [I1, I2, I3, I4, I5, I6]
    Ideal = random.choice(IDE)
    B1 = "I will face any challenge to win the approval of my family."
    B2 = "My house’s alliance with another noble family must be sustained at all costs."
    B3 = "Nothing is more important than the other members of my family."
    B4 = "I am in love with the heir of a family that my family despises."
    B5 = "My loyalty to my sovereign is unwavering."
    B6 = "The common folk must see me as a hero of the people."
    BND = [B1, B2, B3, B4, B5, B6]
    Bond = random.choice(BND)
    F1 = "I secretly believe that everyone is beneath me."
    F2 = "I hide a truly scandalous secret that could ruin my family forever."
    F3 = "I too often hear veiled insults and threats in every word addressed to me, and I am quick to anger."
    F4 = "I have an insatiable desire for carnal pleasures."
    F5 = "In fact, the world does revolve around me."
    F6 = "By my words and actions, I often bring shame to my family."
    FLA = [F1, F2, F3, F4, F5, F6]
    Flaw = random.choice(FLA)
    BGL = 25
    print("You personality trait: " + Trait)
    print("Your ideal: " + Ideal)
    print("Your bond: " + Bond)
    print("Your flaw: " + Flaw)
    print("You speak Common," + Rlang + Randl + Hilang)
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
    P1 = "I am driven by a wanderlust that led me away from home."
    P2 = "I watch over my friends as if they were a litter of newborn pups."
    P3 = "I once ran twenty-five miles without stopping to warn  my clan of an approaching orc horde. I would do it again if I had to."
    P4 = "I have a lesson for every situation, drawn from observing nature."
    P5 = "I place no stock in wealthy or well-mannered folk. Money and manners will not save you from a hungry owlbear"
    P6 = "I am always picking things up, absently fiddling with them, and sometimes accidentally breaking them."
    P7 = "I feel far more comfortable around animals than people."
    P8 = "I was, in fact, raised by wolves."
    PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
    Trait = random.choice(PTR)
    I1 = "Change - Life is like the seasons, in constant change, and we must change with it."
    I2 = "Greater Good - It is each person’s responsibility to make the most happiness for the whole tribe."
    I3 = "Honor - If I dishonor myself, I dishonor my whole clan."
    I4 = "Might -  The strongest are meant to rule."
    I5 = "Nature - The natural world is more important than all the constructs of civilization."
    I6 = "Glory - I must earn glory in battle, for myself and my clan."
    IDE = [I1, I2, I3, I4, I5, I6]
    Ideal = random.choice(IDE)
    B1 = "My family, clan, or tribe is the most important thing in my life, even when they are far from me."
    B2 = "An injury to the unspoiled wilderness of my home is an injury to me."
    B3 = "I will bring terrible wrath down on the evildoers who destroyed my homeland."
    B4 = "I am the last of my tribe, and it is up to me to ensure their names enter legend."
    B5 = "I suffer awful visions of a coming disaster and will do anything to prevent it."
    B6 = "It is my duty to provide children to sustain my tribe."
    BND = [B1, B2, B3, B4, B5, B6]
    Bond = random.choice(BND)
    F1 = "I am too enamored of ale, wine, and other intoxicants."
    F2 = "There is no room for caution in a life lived to the fullest."
    F3 = "I remember every insult I’ve received and nurse a silent resentment toward anyone who hass ever wronged me."
    F4 = "I am slow to trust members of other races, tribes, and societies."
    F5 = "Violence is my answer to almost any challenge."
    F6 = "Do not expect me to save those who can’t save themselves. It is nature’s way that the strong thrive and the weak perish."
    FLA = [F1, F2, F3, F4, F5, F6]
    Flaw = random.choice(FLA)
    BGL = 10
    print ("Your Outlander origin: " + Origin)
    print("Your personality trait: " + Trait)
    print("Your ideal: " + Ideal)
    print("Your bond: " + Bond)
    print("Your flaw: " + Flaw)
    print("You speak Common," + Rlang + Randl + Hilang)
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
    P1 = "I use polysyllabic words that convey the impression of great erudition."
    P2 = "I have read every book in the world's greatest libraries, or I like to boast that I have."
    P3 = "I'm used to helping out those who aren't as smart as I am, and I patiently explain anything and everything to others."
    P4 = "There's nothing I like more than a good mystery."
    P5 = "I'm willing to listen to every side of an argument before I make my own judgment."
    P6 = "I… speak… slowly… when talking… to idiots,… which… almost… everyone… is… compared… to me."
    P7 = "I am horribly, horribly awkward in social situations."
    P8 = "I'm convinced that people are always trying to steal my secrets."
    PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
    Trait = random.choice(PTR)
    I1 = "Knowledge - The path to power and self-improvement is through knowledge."
    I2 = "Beauty - What is beautiful points us beyond itself toward what is true."
    I3 = "Logic - Emotions must not cloud our logical thinking."
    I4 = "No Limits - Nothing should fetter the infinite possibility inherent in all existence. "
    I5 = "Power - Knowledge is the path to power and domination. "
    I6 = "Self-Improvement - The goal of a life of study is the betterment of oneself. "
    IDE = [I1, I2, I3, I4, I5, I6]
    Ideal = random.choice(IDE)
    B1 = "It is my duty to protect my students."
    B2 = "I have an ancient text that holds terrible secrets that must not fall into the wrong hands."
    B3 = "I work to preserve a library, university, scriptorium, or monastery."
    B4 = "My life's work is a series of tomes related to a specific field of lore."
    B5 = "I've been searching my whole life for the answer to a certain question."
    B6 = "I sold my soul for knowledge. I hope to do great deeds and win it back."
    BND = [B1, B2, B3, B4, B5, B6]
    Bond = random.choice(BND)
    F1 = "I am easily distracted by the promise of information."
    F2 = "Most people scream and run when they see a demon. I stop and take notes on its anatomy."
    F3 = "Unlocking an ancient mystery is worth the price of a civilization."
    F4 = "I overlook obvious solutions in favor of complicated ones."
    F5 = "I speak without really thinking through my words, invariably insulting others."
    F6 = "I can't keep a secret to save my life, or anyone else's."
    FLA = [F1, F2, F3, F4, F5, F6]
    Flaw = random.choice(FLA)
    BGL = 10
    print ("Your Sage specialty: " + Specialty)
    print("You personality trait: " + Trait)
    print("Your ideal: " + Ideal)
    print("Your bond: " + Bond)
    print("Your flaw: " + Flaw)
    print("You speak Common," , Rlang , Randl,  Randl2 , Hilang)
if back == Sai:
    P1 = "My friends know they can rely on me, no matter what."
    P2 = "I work hard so that I can play hard when the work is done."
    P3 = "I enjoy sailing into new ports and making new friends over a flagon of ale."
    P4 = "I stretch the truth for the sake of a good story."
    P5 = "To me, a tavern brawl is a nice way to get to know a new city."
    P6 = "I never pass up a friendly wager."
    P7 = "My language is as foul as an otyugh nest."
    P8 = "I like a job well done, especially if I can convince someone else to do it."
    PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
    Trait = random.choice(PTR)
    I1 = "Respect - The thing that keeps a ship together is mutual respect between captain and crew"
    I2 = "Fairness -  We all do the work, so we all share in the rewards."
    I3 = "Freedom - The sea is freedom-the freedom to go anywhere and do anything."
    I4 = "Mastery -  I'm a predator, and the other ships on the sea are my prey."
    I5 = "People - I'm committed to my crewmates, not to ideals."
    I6 = "Aspiration - Someday I'll own my own ship and chart my own destiny.)"
    IDE = [I1, I2, I3, I4, I5, I6]
    Ideal = random.choice(IDE)
    B1 = "I'm loyal to my captain first, everything else second."
    B2 = "The ship is most important, crewmates and captains come and go."
    B3 = "I'll always remember my first ship."
    B4 = "In a harbor town, I have a paramour whose eyes nearly stole me from the sea."
    B5 = "I was cheated out of my fair share of the profits, and I want to get my due."
    B6 = "Ruthless pirates murdered my captain and crewmates, plundered our ship, and left me to die. Vengeance will be mine."
    BND = [B1, B2, B3, B4, B5, B6]
    Bond = random.choice(BND)
    F1 = "I follow orders, even if I think they're wrong."
    F2 = "I'll say anything to avoid having to do extra work."
    F3 = "Once someone questions my courage, I never back down no matter how dangerous the situation."
    F4 = "Once I start drinking, it's hard for me to stop."
    F5 = "I can't help but pocket loose coins and other trinkets I come across."
    F6 = "My pride will probably lead to my destruction."
    FLA = [F1, F2, F3, F4, F5, F6]
    Flaw = random.choice(FLA)
    BGL = 10
    print("You personality trait: " + Trait)
    print("Your ideal: " + Ideal)
    print("Your bond: " + Bond)
    print("Your flaw: " + Flaw)
    print("You speak Common," + Rlang + Hilang)
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
    P1 = "I am always polite and respectful."
    P2 = "I am haunted by memories of war. I can't get the images of violence out of my mind."
    P3 = "I have lost too many friends and I am slow to make a new one."
    P4 = "I am full of inspiring and cautionary tales from my military experience which is relevant to almost every combat situation."
    P5 = "I can stare down a hell hound without flinching."
    P6 = "I enjoy being strong and I like breaking things."
    P7 = "I have a crude sense of humor."
    P8 = "I face problems head-on. A simple, direct solution is the best path to success."
    PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
    Trait = random.choice(PTR)
    I1 = "Greater Good - Our lot is to lay down our lives in defense of others."
    I2 = "Responsibility - I do what I must and obey just authority."
    I3 = "Independence - When people follow orders blindly, they embrace a kind of tyranny."
    I4 = "Might -  In life as in war, the stronger force wins."
    I5 = "Live and Let Live - Ideals are not worth killing over or going to war for."
    I6 = "Nation - My city, nation, or people are all that matter."
    IDE = [I1, I2, I3, I4, I5, I6]
    Ideal = random.choice(IDE)
    B1 = "I would still lay down my life for the people I served with."
    B2 = "Someone saved my life on the battlefield. To this day, I will never leave a friend behind."
    B3 = "My honor is my life."
    B4 = "I will never forget the crushing defeat my company suffered or the enemies who dealt it."
    B5 = "Those who fight beside me are those worth dying for."
    B6 = "I fight for those who cannot fight for themselves."
    BND = [B1, B2, B3, B4, B5, B6]
    Bond = random.choice(BND)
    F1 = "The monstrous enemy which we faced in battle still leaves me quivering with fear."
    F2 = "I have little respect for anyone who is not a proven warrior."
    F3 = "I made a terrible mistake in battle that cost many lives, and I would do anything to keep that mistake secret."
    F4 = "My hatred of my enemies is blind and unreasoning."
    F5 = "I obey the law, even if the law causes misery."
    F6 = "I would rather eat my armor than admit when I’m wrong."
    FLA = [F1, F2, F3, F4, F5, F6]
    Flaw = random.choice(FLA)
    BGL = 10
    print("You personality trait: " + Trait)
    print("Your ideal: " + Ideal)
    print("Your bond: " + Bond)
    print("Your flaw: " + Flaw)
    print("You speak Common," + Rlang + Hilang)
if back == "Urchin":
    P1 = "I hide scraps of food and trinkets away in my pockets."
    P2 = "I ask a lot of questions."
    P3 = "I like to squeeze into small places where no one else can get to me."
    P4 = "I sleep with my back to a wall or tree, with everything I own wrapped in a bundle in my arms."
    P5 = "I eat like a pig and have bad manners."
    P6 = "I think anyone who's nice to me is hiding evil intent."
    P7 = "I don't like to bathe."
    P8 = "I bluntly say what other people are hinting at or hiding."
    PTR = [P1, P2, P3, P4, P5, P6, P7, P8]
    Trait = random.choice(PTR)
    I1 = "Respect - All people, rich or poor, deserve respect."
    I2 = "Community: We have to take care of each other, because no one else is going to do it."
    I3 = "Change - The low are lifted up, and the high and mighty are brought down. Change is the nature of things."
    I4 = "Retribution - The rich need to be shown what life and death are like in the gutters."
    I5 = "People - I help the people who help me-that's what keeps us alive."
    I6 = "Aspiration - I'm going to prove that I'm worthy of a better life."
    IDE = [I1, I2, I3, I4, I5, I6]
    Ideal = random.choice(IDE)
    B1 = "My town or city is my home, and I'll fight to defend it."
    B2 = "I sponsor an orphanage to keep others from enduring what I was forced to endure."
    B3 = "I owe my survival to another urchin who taught me to live on the streets."
    B4 = "I owe a debt I can never repay to the person who took pity on me."
    B5 = "I escaped my life of poverty by robbing an important person, and I'm wanted for it."
    B6 = "No one else should have to endure the hardships I've been through."
    BND = [B1, B2, B3, B4, B5, B6]
    Bond = random.choice(BND)
    F1 = "If I'm outnumbered, I will run away from a fight."
    F2 = "Gold seems like a lot of money to me, and I'll do just about anything for more of it."
    F3 = "I will never fully trust anyone other than myself."
    F4 = "I'd rather kill someone in their sleep then fight fair."
    F5 = "It's not stealing if I need it more than someone else."
    F6 = "People who can't take care of themselves get what they deserve."
    FLA = [F1, F2, F3, F4, F5, F6]
    Flaw = random.choice(FLA)
    BGL = 10
    print("You personality trait: " + Trait)
    print("Your ideal: " + Ideal)
    print("Your bond: " + Bond)
    print("Your flaw: " + Flaw)
    print("You speak Common," + Rlang + Hilang)

Gold = str(BGL)
print ("Your starting gold: " + Gold)
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
print ("Your trinket: " + Trinket)
print("")
print("stats:")
n=0
m=0
run = True
while run:
    Value1 = random.randint (1, 6)
    Value2 = random.randint (1, 6)
    Value3 = random.randint (1, 6)
    Value4 = random.randint (1, 6)
    value = (Value1, Value2, Value3, Value4)
    Value = sorted(value)
    del Value[0]
    sum = 0
    for k in range(len(Value)):
        sum += Value[k]
    print (sum)
    n += 1
    if n >= 6:
        run = False



input()
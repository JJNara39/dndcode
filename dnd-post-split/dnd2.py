import random
from dndchargen_race import *
from dndchargen_bkg import *
from dndchargen_class import *
#from dndchargen_character_builder import *
from fractions import Fraction

def dndCharGen(param, chLvl, charactername, playername):
    skills_dict = {
        "AcroNum" : 0,
        "AnHaNum" : 0,
        "ArcaNum" : 0,
        "AthlNum" : 0,
        "DeceNum" : 0,
        "HistNum" : 0,
        "InsiNum" : 0,
        "IntiNum" : 0,
        "InveNum" : 0,
        "MediNum" : 0,
        "NatuNum" : 0,
        "PercNum" : 0,
        "PerfNum" : 0,
        "PersNum" : 0,
        "ReliNum" : 0,
        "SloHNum" : 0,
        "SteaNum" : 0,
        "SurvNum" : 0
    }
    Charisma = 0
    Constitution = 0
    Dexterity = 0
    Intelligence = 0
    Strength = 0
    Wisdom =  0
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
    ARTISANTOOLS = [AlchSupp, BrewSupp, CallSupp, CarpTools, CartTools, CobbTools, CooksUten, GlasTools, JeweTools, LthrwrkTools, MasnTools, PaintSupp, PottTools, SmthTools, TinkTools, WeavTools, WdcrvTools]
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
    DisgKit = "Disguise Kit"
    ForgKit = "Forgery Kit"
    HerbKit = "Herbalism Kit"
    NavTools = "Navigator's Tools"
    PoisKit = "Poisoner's Kit"
    ThievKit = "Thieves' Tools"
    Kits = [DisgKit, ForgKit, HerbKit, NavTools, PoisKit, ThievKit]
    VehLand = "Vehicles (Land)"
    VehSea = "Vehicles (Sea)"
    VehSpace = "Vehicles (Space)"
    VehProf = [VehLand, VehSea, VehSpace]
    ToolProficiencies = [ARTISANTOOLS, GamingSets, MusicalInstruments, Kits]
    AntimatterRifle = "Antimatter Rifle"
    AutomaticPistol = "Automatic Pistol"
    AutomaticRifle = "Automatic Rifle"
    HuntingRifle = "Hunting Rifle"
    LaserPistol = "Laser Pistol"
    LaserRifle = "Laser Rifle"
    Musket = "Musket"
    Pistol = "Pistol"
    Revolver = "Revolver"
    Shotgun = "Shotgun"
    Firearms = [AntimatterRifle, AutomaticPistol, AutomaticRifle, HuntingRifle, LaserPistol, LaserRifle, Musket, Pistol, Revolver, Shotgun]
    Club = "Club"
    Dagger = "Dagger"
    Dart = "Dart"
    Greatclub = "Greatclub"
    Handaxe = "Handaxe"
    Javelin = "Javelin"
    LightCrossbow = "Light Crossbow"
    LightHammer = "Light Hammer"
    Mace = "Mace"
    Quarterstaff = "Quarterstaff"
    Shortbow = "Shortbow"
    Sickle = "Sickle"
    Sling = "Sling"
    Spear = "Spear"
    Yklwa = "Yklwa"
    SimpleWeapons = [Club, Dagger, Dart, Greatclub, Handaxe, Javelin, LightCrossbow, LightHammer, Mace, Quarterstaff, Shortbow, Sickle, Sling, Spear, Yklwa]
    Battleaxe = "Battleaxe"
    DoubleBladedScimitar = "Double-Bladed Scimitar"
    Flail = "Flail"
    Glaive = "Glaive"
    Greataxe = "Greataxe"
    Greatsword = "Greatsword"
    Halberd = "Halberd"
    Lance = "Lance"
    Longsword = "Longsword"
    Maul = "Maul"
    Morningstar = "Morningstar"
    Pike = "Pike"
    Rapier = "Rapier"
    Scimitar = "Scimitar"
    Shortsword = "Shortsword"
    Trident = "Trident"
    WarPick = "War Pick"
    Warhammer = "Warhammer"
    Whip = "Whip"
    Blowgun = "Blowgun"
    Crossbow = "Crossbow"
    HandCrossbow = "Hand Crossbow"
    Longbow = "Longbow"
    Net = "Net"
    MartialWeapons = [
            Battleaxe, DoubleBladedScimitar, Flail, Glaive, Greataxe, Greatsword, Halberd, Lance, Longsword, Maul, Morningstar, Pike, Rapier, Scimitar,
            Shortsword, Trident, WarPick, Warhammer, Whip, Blowgun, Crossbow, HandCrossbow, Longbow, Net
        ]
    Leather = "Leather"
    StuddedLeather = "Studded Leather"
    Padded = "Padded"
    LightArmor = [Leather, StuddedLeather, Padded]
    Breastplate = "Breastplate"
    ChainShirt = "Chain Shirt"
    HalfPlate = "Half Plate"
    Hide = "Hide"
    ScaleMail = "Scale Mail"
    SpikedArmor ="Spiked Armor"
    MediumArmor = [Breastplate, ChainShirt, HalfPlate, Hide, ScaleMail, SpikedArmor]
    ChainMail = "Chain Mail"
    RingMail = "Ring Mail"
    Plate = "Plate"
    Splint = "Splint"
    HeavyArmor = [ChainMail, RingMail, Plate, Splint]
    Shield = "Shield"   
    SLANG = []
    RaceNotes = []
    PlProf = []
    PlLang = []    
    ClassNotes = []
    Gender = ""
    HollowOne = ""
    race = ""
    subrace = ""
    Class = ""
    subclass = ""
    Lineage = ""
    Height = 0
    Weight = 0
    walkingspeed = 0
    CreatureType = ""
    DamageResistance = ""
    Aara = "Aarakocra"
    Abys = "Abyssal"
    Aqua = "Aquan"
    Aura = "Auran"
    Bird = "Birdfolk"
    Cele = "Celestial"
    Cerva = "Cervan"
    Comm = "Common"
    Drac = "Draconic"
    Dwarvi = "Dwarvish"
    DpSp = "Deep Speech"
    Elvi = "Elvish"
    Gian = "Giant"
    GithL = "Gith"
    Gnom = "Gnomish"
    Gobl = "Goblin"
    Grun = "Grung"
    Hafl = "Hafling"
    Hedg = "Hedge"
    Infe = "Infernal"
    Jerb = "Jerbeen"
    Krau = "Kraul"
    Leon = "Leonin"
    Loxo = "Loxodon"
    Mapa = "Mapach"
    Mino = "Minotaur"
    Orc = "Orc"
    Quo = "Quori"
    Prim = "Primordial"
    Sylv = "Sylvan"
    Unde = "Undercommon"
    Veda = "Vedalken"
    Vulp = "Vulpin"
    TCant = "Thieves Cant"
    SLANG = [Aara, Abys, Aqua, Aura, Bird, Cele, Cerva, Comm, DpSp, Drac, Dwarvi, Elvi, Gian, GithL, Gnom, Gobl, Grun, Hafl, Hedg, Infe, Jerb, Krau, Leon, Loxo, Mapa, Mino, Orc, Quo, Prim, Sylv, Unde, Veda, Vulp]
    CharacterGen = ["Race", "Class", "Background"]
    if param == "Y":
        print("0 - Random")
        print("1 - Race")
        print("2 - Class")
        print("3 - Background")
        chargen1 = int(input("Which aspect of your character do you want to define first? "))
        if chargen1 == 0:
            CharacterGenRand1 = random.choice(CharacterGen)
            if CharacterGenRand1 == "Race":
                Gender, HollowOne, race, subrace, Lineage, Height, Weight, walkingspeed, CreatureType, DamageResistance, PlLang, SLANG, PlProf, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom, RaceNotes = dndCharGenRace(param, PlLang, SLANG, PlProf, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
            if CharacterGenRand1 == "Class":
                Class, subclass, ClassNotes = dndchargen_class(param)
            if CharacterGenRand1 == "Background":
                back, Trait, Ideal, Bond, Flaw, BGL, PlLang, SLANG, PlProf, skills_dict = dndCharGenBkg(param, PlLang, SLANG, PlProf, skills_dict)     
            CharacterGen.remove(CharacterGenRand1)
        elif 1 <= chargen1 <= 3:
            first_choice = CharacterGen[chargen1 - 1]
            if first_choice == "Race":
                Gender, HollowOne, race, subrace, Lineage, Height, Weight, walkingspeed, CreatureType, DamageResistance, PlLang, SLANG, PlProf, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom, RaceNotes = dndCharGenRace(param, PlLang, SLANG, PlProf, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
            if first_choice == "Class":
                Class, subclass, ClassNotes = dndchargen_class(param)
            if first_choice == "Background":
                back, Trait, Ideal, Bond, Flaw, BGL, PlLang, SLANG, PlProf, skills_dict = dndCharGenBkg(param, PlLang, SLANG, PlProf, skills_dict)     
            CharacterGen.remove(first_choice)
        print("0 - Random")        
        for i, option in enumerate(CharacterGen, 1):
            print(f"{i} - {option}")
        chargen2 = int(input("Which aspect of your character do you want to define next? "))
        if chargen2 == 0:
            CharacterGenRand2 = random.choice(CharacterGen)
            if CharacterGenRand2 == "Race":
                Gender, HollowOne, race, subrace, Lineage, Height, Weight, walkingspeed, CreatureType, DamageResistance, PlLang, SLANG, PlProf, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom, RaceNotes = dndCharGenRace(param, PlLang, SLANG, PlProf, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
            if CharacterGenRand2 == "Class":
                Class, subclass, ClassNotes = dndchargen_class(param)
            if CharacterGenRand2 == "Background":
                back, Trait, Ideal, Bond, Flaw, BGL, PlLang, SLANG, PlProf, skills_dict = dndCharGenBkg(param, PlLang, SLANG, PlProf, skills_dict)     
            CharacterGen.remove(CharacterGenRand2)
        elif 1 <= chargen2 <= len(CharacterGen):
            second_choice = CharacterGen[chargen2 - 1]
            if second_choice == "Race":
                Gender, HollowOne, race, subrace, Lineage, Height, Weight, walkingspeed, CreatureType, DamageResistance, PlLang, SLANG, PlProf, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom, RaceNotes = dndCharGenRace(param, PlLang, SLANG, PlProf, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
            if second_choice == "Class":
                Class, subclass, ClassNotes = dndchargen_class(param)
            if second_choice == "Background":
                back, Trait, Ideal, Bond, Flaw, BGL, PlLang, SLANG, PlProf, skills_dict = dndCharGenBkg(param, PlLang, SLANG, PlProf, skills_dict)     
            CharacterGen.remove(second_choice)
        last_choice = CharacterGen[0]
        if last_choice == "Race":
            Gender, HollowOne, race, subrace, Lineage, Height, Weight, walkingspeed, CreatureType, DamageResistance, PlLang, SLANG, PlProf, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom, RaceNotes = dndCharGenRace(param, PlLang, SLANG, PlProf, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
        if last_choice == "Class":
            Class, subclass, ClassNotes = dndchargen_class(param)
        if last_choice == "Background":
            back, Trait, Ideal, Bond, Flaw, BGL, PlLang, SLANG, PlProf, skills_dict = dndCharGenBkg(param, PlLang, SLANG, PlProf, skills_dict)     
    if param == "N":
        CharacterGenRand1 = random.choice(CharacterGen)
        if CharacterGenRand1 == "Race":
            Gender, HollowOne, race, subrace, Lineage, Height, Weight, walkingspeed, CreatureType, DamageResistance, PlLang, SLANG, PlProf, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom, RaceNotes = dndCharGenRace(param, PlLang, SLANG, PlProf, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
        if CharacterGenRand1 == "Class":
            Class, subclass, ClassNotes = dndchargen_class(param)
        if CharacterGenRand1 == "Background":
            back, Trait, Ideal, Bond, Flaw, BGL, PlLang, SLANG, PlProf, skills_dict = dndCharGenBkg(param, PlLang, SLANG, PlProf, skills_dict)     
        CharacterGen.remove(CharacterGenRand1)
        CharacterGenRand2 = random.choice(CharacterGen)
        if CharacterGenRand2 == "Race":
            Gender, HollowOne, race, subrace, Lineage, Height, Weight, walkingspeed, CreatureType, DamageResistance, PlLang, SLANG, PlProf, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom, RaceNotes = dndCharGenRace(param, PlLang, SLANG, PlProf, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
        if CharacterGenRand2 == "Class":
            Class, subclass, ClassNotes = dndchargen_class(param)
        if CharacterGenRand2 == "Background":
            back, Trait, Ideal, Bond, Flaw, BGL, PlLang, SLANG, PlProf, skills_dict = dndCharGenBkg(param, PlLang, SLANG, PlProf, skills_dict)     
        CharacterGen.remove(CharacterGenRand2)
        CharacterGenRand3 = random.choice(CharacterGen)
        if CharacterGenRand3 == "Race":
            Gender, HollowOne, race, subrace, Lineage, Height, Weight, walkingspeed, CreatureType, DamageResistance, PlLang, SLANG, PlProf, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom, RaceNotes = dndCharGenRace(param, PlLang, SLANG, PlProf, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
        if CharacterGenRand3 == "Class":
            Class, subclass, ClassNotes = dndchargen_class(param)
        if CharacterGenRand3 == "Background":       
            back, Trait, Ideal, Bond, Flaw, BGL, PlLang, SLANG, PlProf, skills_dict = dndCharGenBkg(param, PlLang, SLANG, PlProf, skills_dict)     
    summation(param, playername, charactername, chLvl, Gender, race, subrace, Height, Weight, RaceNotes, Class, subclass, ClassNotes, HollowOne, Lineage, PlLang, PlProf, back, Trait, Ideal, Bond, Flaw, BGL, PlProf, skills_dict, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)



#Dice are in dndchargen


DMorPlay = int(input("Are you a 1 - DM or 2 - Player? "))
party = int(input("How many characters will your party have? ")) #This can be used later when I implement CR encounters, it will function on party size
chLvlList = []
numMon = 1 #Lets just say for now there is one monster per encounter

##########################################################################################
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
    
###########################################################################################
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
            chLvl = int(input("What level is character {}? ".format(p+1)))
            chLvlList.append(chLvl)
            para = input("Set parameters on character {}? Y/N ".format(p+1))
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
            charactername = input("What is this character's name? ")
            dndCharGen(param, chLvl, charactername, playername)
            
        properPL = sum(chLvlList) / party
        #encounterCR = int(properPL) * party * (1/4) #Instead of making this fraction that auto reduces, lets instead plug the numerator and denominator in an let it do its thing
        eCRMixednum = int(properPL) * party
        eCRMixedden = 4 #The initial scenario was a lvl 1 character could handle a CR of 1/4
        eCRMixed = mixedFraction(eCRMixednum,eCRMixedden)
        #eCRMixed = mixedFraction(encounterCR) #Going to plug numerator and denominator into our mixedFraction function instead
        print("With a party size of {} and a total party level of {}, The Total Encounter CR to work with is {}".format(party, sum(chLvlList), eCRMixed))

    if eYN == "N":
        for p in range(party):
            #Add in a level check for classes, if the level is 3+, the subclass is available.
            chLvl = int(input("What level is character {}? ".format(p+1)))
            chLvlList.append(chLvl)            
            para = input("Set parameters on character {}? Y/N ".format(p+1))
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
            dndCharGen(param, chLvl)
else:
    for p in range(party):
        chLvl = int(input(f"What level is the character {p+1}? "))
        chLvlList.append(chLvl)   
    #Add in a level check for classes, if the level is 3+, the subclass is available.
        para = input(f"Set parameters on character {p+1}? Y/N ")
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
        dndCharGen(param, chLvl)    

'''
#This block of code is to make sure dndCharGen works
for i in range(500):
    print(f"For character {i}:")
    para = "N"
    dndCharGen(para)
'''

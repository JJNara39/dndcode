import random
from dndchargen_languagesskills import *
from dndchargen_summation import *

def d2():
    result = random.randint(1,2)
    return result
def d4():
    result = random.randint(1,4)
    return result
def d6():
    result = random.randint(1,6)
    return result
def d8():
    result = random.randint(1,8)
    return result
def d10():
    result = random.randint(1,10)
    return result
def d12():
    result = random.randint(1,12)
    return result
def d20():
    result = random.randint(1,20)
    return result
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

def dndCharGenRace(param, plLvl, PlLang, SLANG, PlProf, Notes, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom):
    walkingspeed = 0
    CreatureType = ""
    DamageResistance = ""
    Height = 0
    Weight = 0    
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
    if param == "N":
        Gender = random.choice(Gen)
    HolOne = ["Hollow One", "Not Hollow One"] 
    if param == "Y":
        HlwOne = input("Do you want to be a Hollow One (Zombie)? Y/N ")
        if HlwOne == "Y":
            HollowOne = "Hollow One"
        if HlwOne == "y":
            HollowOne = "Hollow One"
        if HlwOne == "Yes":
            HollowOne = "Hollow One"
        if HlwOne == "yes":
            HollowOne = "Hollow One"
        if HlwOne == "Ye":
            HollowOne = "Hollow One"
        if HlwOne == "ye":
            HollowOne = "Hollow One"
        if HlwOne == "N":
            HollowOne = "Not Hollow One"
        if HlwOne == "n":
            HollowOne = "Not Hollow One"
        if HlwOne == "No":
            HollowOne = "Not Hollow One"
        if HlwOne == "no":
            HollowOne = "Not Hollow One"
    if param == "N":
        HollowOne = random.choice(HolOne)

    Aas = ["Fallen Aasimar", "Protector Aasimar", "Scourge Aasimar"]
    Cer = ["Grove Cervan", "Pronghorn Cervan"]
    Corg = ["Cardigan Corginian", "Pembroke Corginian"]
    Cor = ["Dusk Corvum", "Kindled Corvum"]
    Dra = ["Black Scale Dragonborn", "Blue Scale Dragonborn", "Brass Scale Dragonborn", "Bronze Scale Dragonborn", "Chromatic Dragonborn", "Copper Scale Dragonborn", "Draconblood Dragonborn", "Gem Dragonborn", "Gold Scale Dragonborn", "Green Scale Dragonborn", "Metallic Dragonborn", "Red Scale Dragonborn", "Ravenite Dragonborn", "Silver Scale Dragonborn", "White Scale Dragonborn"]
    Dwf = ["Duergar", "Hill Dwarf", "Mountain Dwarf"]
    El = ["Astral Elf", "Dark Elf", "Eladrin", "High Elf", "Sea Elf", "Shadar-kai", "Wood Elf"]
    Gal = ["Bright Gallus", "Huden Gallus"]
    Ge = ["Air Genasi", "Earth Genasi", "Fire Genasi", "Water Genasi"]
    Git = ["Githyanki", "Githzerai"]
    Gn = ["Forest Gnome", "Rock Gnome", "Svirfneblin (Deep) Gnome"]
    Hal = ["Ghostwise Halfling", "Lightfoot Halfling", "Stout Halfling"]
    HE = ["Half-Elf: Aquatic Elf Descent", "Half-Elf: Drow Descent", "Half-Elf: Moon Elf Descent", "Half-Elf: Sun Elf Descent", "Half-Elf: Wood Elf Descent"]
    Hum = ["Human", "Variant Human"]
    Lum = ["Sable Luma, Sera Luma"]
    Rap = ["Maran Raptor (Bird)", "Mistral Raptor (Bird)"]
    Shark = ["Blue Sharkin", "Basking Sharkin", "Bull Sharkin", "Cookie Cutter Sharkin", "Goblin Sharkin", "Hammerhead Sharkin", "Leopard Sharkin", "Mako Sharkin", "Nurse Sharkin", "Thresher Sharkin", "Tiger Sharkin", "Whale Sharkin", "Great White Sharkin", "Cladoselache", "Cretoxyrhina", "Edestus", "Helicoprion", "Hybodus", "Megalodon", "Ptychodus", "Scapanorhynchus", "Stethacanthus", "Xenacanthus"]
    Shi = ["Beasthide Shifter", "Longtooth Shifter", "Swiftstride Shifter", "Wildhunt Shifter"]
    Stri = ["Stout Strig", "Swift Strig"]
    Tie = ["Asmodeus Subject Tiefling", "Baalzebul Subject Tiefling", "Dispater Subject Tiefling", "Fierna Subject Tiefling", "Glasya Subject Tiefling", "Levistus Subject Tiefling", "Mammon Subject Tiefling", "Mephistopheles Subject Tiefling", "Zariel Subject Tiefling"]
    rac = ["Aarakocra", "Aasimar", "Autognome", "Bugbear", "Centaur", "Cervan", "Changeling", "Corginian", "Corvum", "Dhampir", "Disembodied", "Dragonborn", "Dwarf", "Elf", "Fairy", "Firbolg", "Gallus", "Genasi", "Giff", "Gith", "Gnome", "Goblin", "Goliath", "Grung", "Hadozee", "HalfElf", "Halfling", "Half-Orc", "Harengon", "Hedge", "Hexblood", "Human", "Hobgoblin", "Jerbeen", "Kalashtar", "Kender", "Kenku", "Kobold", "Leonin", "Lizardfolk", "Locathah", "Loxodon", "Luma", "Mapach", "Minotaur", "Orc", "Owlin", "Plasmoid", "Raptor (Bird)", "Reborn", "Satyr", "Sharkin", "Shifter", "Simic Hybrid", "Strig", "Tabaxi", "Thri-Kreen", "Tiefling", "Tortle", "Triton", "Vedalken", "Verdan", "Vulpin", "Warforged", "Wechselkind", "Yuan-ti"]
    subrace = ""
    if param == "Y":
        print("0 - Random")
        print("1 - Aarakocra")
        print("2 - Aasimar")
        print("3 - Autognome")
        print("4 - Bugbear")
        print("5 - Centaur")
        print("6 - Cervan (Deer-Folk)")
        print("7 - Changeling")
        print("8 - Corginian")
        print("9 - Corvum (Crow-Folk)")
        print("10 - Dhampir")
        print("11 - Disembodied (Celestial-Person)")
        print("12 - Dragonborn")
        print("13 - Dwarf")
        print("14 - Elf")
        print("15 - Fairy")
        print("16 - Firbolg (Small Giant-folk)")
        print("17 - Gallus (Chicken-Folk)")
        print("18 - Genasi")
        print("19 - Giff (Hippo-Person)")
        print("20 - Gith (Demon Drow)")
        print("21 - Gnome")
        print("22 - Goblin")
        print("23 - Goliath")
        print("24 - Grung")
        print("25 - Hadozee (Lemur-Person)")
        print("26 - Half-Elf")
        print("27 - Halfling")
        print("28 - Half-Orc")
        print("29 - Harengon (Rabbit-Person)")
        print("30 - Hedge (Hedgehog-Folk)")
        print("31 - Hexblood (Witch/Warlock-Person)")
        print("32 - Hobgoblin")
        print("33 - Human")
        print("34 - Jerbeen (Mouse-Folk)")
        print("35 - Kalashtar (Compound of Humans and Spirits)")
        print("36 - Kender (Innocent/Mystical Humans)")
        print("37 - Kenku")
        print("38 - Kobold")
        print("39 - Leonin (Lion-Person)")
        print("40 - Lizardfolk")
        print("41 - Locathah (Fish-Folk)")
        print("42 - Loxodon (Elephant-Person)")
        print("43 - Luma (Dove-Folk)")
        print("44 - Mapach (Raccoon-Folk)")
        print("45 - Minotaur")
        print("46 - Orc")
        print("47 - Owlin")
        print("48 - Plasmoid (Slime-Person)")
        print("49 - Raptor (Hawk-Folk)")
        print("50 - Reborn (Truly Revived; sentient Zombie)")
        print("51 - Satyr")
        print("52 - Sharkin")
        print("53 - Shifter (Lycanthrope-People)")
        print("54 - Simic Hybrid (Mix between humans/elves/vedalken)")
        print("55 - Strig (Owl-Folk)")
        print("56 - Tabaxi (Cat-folk)")
        print("57 - Thri-Kreen (Cricket-Person)")
        print("58 - Tiefling")
        print("59 - Tortle")
        print("60 - Triton (Noble-ish Sea-folk)")
        print("61 - Vedalken (Blue imperfect beings striving for perfection)")
        print("62 - Verdan (VERY-humanoid Goblin-folk)")
        print("63 - Vulpin (Fox-Folk)")
        print("64 - Warforged")
        print("65 - Wechselkind (Puppet-Folk)")
        print("66 - Yuan-ti (Abyssal-Dragonoids)")
        rce = input("Race? ")
        if rce == "1":
            race = "Aarakocra"
        if rce == "2":
            race = "Aasimar"
            print("0 - Random")
            print("1 - Fallen Aasimar")
            print("2 - Protector Aasimar")
            print("3 - Scourge Aasimar")            
            subr = int(input("Which subrace would you like? "))
            if subr == 1:
                subrace = "Fallen Aasimar"
            if subr == 2:
                subrace = "Protector Aasimar"
            if subr == 3:
                subrace = "Scourge Aasimar"
            if subr == 0:
                subrace = random.choice(Aas)
        if rce == "3":
            race = "Autognome"
        if rce == "4":
            race = "Bugbear"
        if rce == "5":
            race = "Centaur"
        if rce == "6":
            race = "Cervan"
            print("0 - Random")
            print("1 - Grove Cervan")
            print("2 - Pronghorn Cervan")            
            subr = int(input("Which subrace would you like? "))
            if subr == 1:
                subrace = "Grove Cervan"
            if subr == 2:
                subrace = "Pronghorn Cervan"
            if subr == 0:
                subrace = random.choice(Cer)                        
        if rce == "7":
            race = "Changeling"
        if rce == "8":
            race = "Corginian"
            print("0 - Random")
            print("1 - Cardigan Corginian")
            print("2 - Pembroke Corginian")
            subr = int(input("Which subrace would you like? "))
            if subr == 1:
                subrace = "Cardigan Corginian"
            if subr == 2:
                subrace = "Pembroke Corginian"
            if subr == 0:
                subrace = random.choice(Corg)            
        if rce == "9":
            race = "Corvum"
            print("0 - Random")
            print("1 - Dusk Corvum")
            print("2 - Kindled Corvum")
            subr = int(input("Which subrace would you like? "))
            if subr == 1:
                subrace = "Dusk Corvum"
            if subr == 2:
                subrace = "Kindled Corvum"  
            if subr == 0:
                subrace = random.choice(Cor)   
        if rce == "10":
            race = "Dhampir"                                        
        if rce == "10":
            race = "Disembodied"                        
        if rce == "11":
            race = "Dragonborn"
            print("0 - Random")
            print("1 - Black Scale Dragonborn")
            print("2 - Blue Scale Dragonborn")
            print("3 - Brass Scale Dragonborn")
            print("4 - Bronze Scale Dragonborn")
            print("5 - Chromatic Dragonborn")
            print("6 - Copper Scale Dragonborn")
            print("7 - Draconblood Dragonborn")
            print("8 - Gem Dragonborn")
            print("9 - Green Scale Dragonborn")
            print("10 - Metallic Dragonborn")
            print("11 - Red Scale Dragonborn")
            print("12 - Ravenite Dragonborn")
            print("13 - Silver Scale Dragonborn")
            print("14 - White Scale Dragonborn")
            subr = int(input("Which subrace would you like? "))
            if subr == 1:
                subrace = "Black Scale Dragonborn"
            if subr == 2:
                subrace = "Blue Scale Dragonborn"  
            if subr == 3:
                subrace = "Brass Scale Dragonborn"
            if subr == 4:
                subrace = "Bronze Scale Dragonborn"
            if subr == 5:
                subrace = "Chromatic Dragonborn"
                colors = ["Black", "Blue", "Green", "Red", "White"]
                print("0 - Random")
                for i, clr in enumerate(colors, 1):
                    print(f"{i} - {clr}")
                clrint = int(input("What color chromatic dragon are you? "))
                if clrint == 1:
                    color = "Black"
                if clrint == 2:
                    color = "Blue"
                if clrint == 3:
                    color = "Green"
                if clrint == 4:
                    color = "Red"
                if clrint == 5:
                    color = "White"
                if clrint == 0:
                    color = random.choice(colors)
            if subr == 6:
                subrace = "Copper Scale Dragonborn"
            if subr == 7:
                subrace = "Draconblood Dragonborn"
            if subr == 8:
                subrace = "Gem Dragonborn"
                gems = ["Amethyst", "Crystal", "Emerald", "Sapphire", "Topaz"]
                for i, gm in enumerate(gems, 1):
                    print(f"{i} - {gm}")           
                gemint = int(input("What color chromatic dragon are you? "))
                if gemint == 1:
                    gem = "Amethyst"
                if gemint == 2:
                    gem = "Crystal"
                if gemint == 3:
                    gem = "Emerald"
                if gemint == 4:
                    gem = "Sapphire"
                if gemint == 5:
                    gem = "Topaz"
                if gemint == 0:
                    gem = random.choice(gems)                     
            if subr == 9:
                subrace = "Gold Scale Dragonborn"
            if subr == 10:
                subrace = "Green Scale Dragonborn"
            if subr == 11:
                subrace = "Metallic Dragonborn"
                metals = ["Brass", "Bronze", "Copper", "Gold", "Silver"]
                for i, mtl in enumerate(metals, 1):
                    print(f"{i} - {mtl}")           
                metalint = int(input("What color chromatic dragon are you? "))
                if metalint == 1:
                    metal = "Brass"
                if metalint == 2:
                    metal = "Bronze"
                if metalint == 3:
                    metal = "Copper"
                if metalint == 4:
                    metal = "Gold"
                if metalint == 5:
                    metal = "Silver"
                if metalint == 0:
                    metal = random.choice(metals) 
            if subr == 11:
                subrace  = "Red Scale Dragonborn"
            if subr == 12:
                subrace = "Ravenite Dragonborn"
            if subr == 13:
                subrace = "Silver Scale Dragonborn"
            if subr == 14:
                subrace = "White Scale Dragonborn"
            if subr == 0:
                subrace = random.choice(Dra)  
        if rce == "12":
            race = "Dwarf"
            print("0 - Random")
            print("1 - Duergar")
            print("2 - Hill Dwarf")
            print("3 - Mountain Dwarf")
            subr = int(input("Which subrace would you like? "))                  
            if subr == 1:
                subrace = "Duergar"
            if subr == 2:
                subrace = "Hill Dwarf"
            if subr == 3:
                subrace = "Mountain Dwarf"
            if subr == 0:
                subrace = random.choice(Dwf)                
        if rce == "13":
            race = "Elf"
            print("0 - Random")
            print("1 - Astral Elf")
            print("2 - Dark Elf")
            print("3 - Eladrin")
            print("4 - High Elf") 
            print("5 - Sea Elf") 
            print("6 - Shadar-kai")           
            print("7 - Wood Elf")   
            subr = int(input("Which subrace would you like? "))  
            if subr == 1:
                subrace = "Astral Elf"
            if subr == 2:
                subrace = "Dark Elf"
            if subr == 3:
                subrace = "Eladrin"
            if subr == 4:
                subrace = "High Elf"
            if subr == 5:
                subrace = "Sea Elf"
            if subr == 6:
                subrace = "Shadar-kai"
            if subr == 7:
                subrace = "Wood Elf"
            if subr == 0:
                subrace = random.choice(El)                                                                                                                                            
        if rce == "14":
            race = "Fairy"                    
        if rce == "15":
            race = "Firbolg"
        if rce == "16":
            race = "Gallus" 
            print("0 - Random") 
            print("1 - Bright Gallus") 
            print("2 - Huden Gallus")   
            subr = int(input("Which subrace would you like? "))            
            if subr == 1:
                subrace = "Bright Gallus"      
            if subr == 2:
                subrace = "Huden Gallus"                       
            if subr == 0:
                subrace = random.choice(Gal)
        if rce == "17":
            race = "Genasi"
            print("0 - Random") 
            print("1 - Air Genasi") 
            print("2 - Earth Genasi") 
            print("3 - Fire Genasi") 
            print("4 - Water Genasi")             
            subr = int(input("Which subrace would you like? ")) 
            if subr == 1:
                subrace = "Air Genasi"
            if subr == 2:
                subrace = "Earth Genasi"
            if subr == 3:
                subrace = "Fire Genasi"
            if subr == 4:
                subrace = "Water Genasi"
            if subr == 0:
                subrace = random.choice(Ge)
        if rce == "18":
            race = "Giff"
        if rce == "19":
            race = "Gith"
            print("0 - random")
            print("1 - Githyanki")
            print("2 - Githzerai")
            subr = int(input("Which subrace would you like? ")) 
            if subr == 1:
                subrace = "Githyanki"
            if subr == 2:
                subrace = "Githzerai"
            if subr == 0:
                subrace = random.choice(Git)
        if rce == "20":
            race = "Gnome"
            print("0 - Random")
            print("1 - Forest Gnome")
            print("2 - Rock Gnome")
            print("3 - Svirfneblin (Deep) Gnome")
            subr = int(input("Which subrace would you like? "))   
            if subr == 1:
                subrace = "Forest Gnome"
            if subr == 2:
                subrace = "Rock Gnome"
            if subr == 3:
                subrace = "Svirfneblin (Deep) Gnome"
            if subr == 0:                      
                subrace = random.choice(Gn)
        if rce == "21":
            race = "Goblin"
        if rce == "22":
            race = "Goliath"
        if rce == "23":
            race = "Grung"            
        if rce == "24":
            race = "Hadozee"
        if rce == "25":
            race = "HalfElf"
            print("0 - Random")
            print("1 - Half-Elf: Aquatic Elf Descent")
            print("2 - Half-Elf: Drow Descent")
            print("3 - Half-Elf: Moon Elf Descent")
            print("4 - Half-Elf: Sun Elf Descent")
            print("5 - Half-Elf: Wood Elf Descent")            
            subr = int(input("Which subrace would you like? "))             
            if subr == 1:
                subrace = "Half-Elf: Aquatic Elf Descent"
            if subr == 2:
                subrace = "Half-Elf: Drow Descent"
            if subr == 3:
                subrace = "Half-Elf: Moon Elf Descent"
            if subr == 4:
                subrace = "Half-Elf: Sun Elf Descent"
            if subr == 5:
                subrace = "Half-Elf: Wood Elf Descent"
            if subr == 0:   
                subrace = random.choice(HE)    
        if rce == "26":
            race = "Halfling"
            print("0 - Random")
            print("1 - Ghostwise Halfling")
            print("2 - Lightfoot Halfling")
            print("3 - Stout Halfling")            
            subr = int(input("Which subrace would you like? "))  
            if subr == 1:
                subrace = "Ghostwise Halfling"
            if subr == 2:
                subrace = "Lightfoot Halfling"
            if subr == 3:
                subrace = "Stout Halfling"
            if subr == 0:
                subrace = random.choice(Hal)                       
        if rce == "27":
            race = "Half-Orc"
        if rce == "28":
            race = "Harengon"
        if rce == "29":
            race = "Hedge"             
        if rce == "30":
            race = "Hobgoblin"
        if rce == "31":
            race = "Hexblood"            
        if rce == "31":
            race = "Human"
            print("0 - Random")
            print("1 - Human")
            print("2 - Variant Human")  
            subr = int(input("Which subrace would you like? "))      
            if subr == 1:
                subrace = "Human"
            if subr == 2:
                subrace = "Variant Human"
            if subr == 0: 
                subrace = random.choice(Hum)                            
        if rce == "32":
            race = "Jerbeen"
        if rce == "33":
            race = "Kalashtar"
        if rce == "34":
            race = "Kender"
        if rce == "35":
            race = "Kenku"
        if rce == "36":
            race = "Kobold"
        if rce == "37":
            race = "Leonin"            
        if rce == "38":
            race = "Lizardfolk"
        if rce == "39":
            race = "Locathah"            
        if rce == "40":
            race = "Loxodon"
        if rce == "41":
            race = "Luma"  
            print("0 - Random")
            print("1 - Sable Luma")
            print("2 - Sera Luma")  
            subr = int(input("Which subrace would you like? "))    
            if subr == 1:
                subrace = "Sable Luma"
            if subr == 2:
                subrace = "Sera Luma"
            if subr == 0:  
                subrace = random.choice(Lum)                             
        if rce == "42":
            race = "Mapach"                      
        if rce == "43":
            race = "Minotaur"            
        if rce == "44":
            race = "Orc"
        if rce == "45":
            race = "Owlin"               
        if rce == "46":
            race = "Plasmoid"
        if rce == "47":
            race = "Raptor (Bird)"
            print("0 - Random")
            print("1 - Maran Raptor (Bird)")
            print("2 - Mistral Raptor (Bird)")  
            subr = int(input("Which subrace would you like? "))    
            if subr == 1:
                subrace = "Maran Raptor (Bird)"
            if subr == 2:
                subrace = "Mistral Raptor (Bird)"
            if subr == 0:  
                subrace = random.choice(Rap)                             
        if rce == "50":
            race = "Reborn"        
        if rce == "48":
            race = "Satyr"
        if rce == "49":
            race = "Sharkin"  
            print("0 - Random")
            print("1 - Blue Sharkin")
            print("2 - Basking Sharkin")
            print("3 - Bull Sharkin")
            print("4 - Cookie Cutter Sharkin")
            print("5 - Goblin Sharkin")  
            print("6 - Hammerhead Sharkin")
            print("7 - Leopard Sharkin")
            print("8 - Mako Sharkin")
            print("9 - Nurse Sharkin")
            print("10 - Thresher Sharkin")
            print("11 - Tiger Sharkin")   
            print("12 - Whale Sharkin")
            print("13 - Great White Sharkin")
            print("14 - Cladoselache")
            print("15 - Cretoxyrhina")
            print("16 - Edestus")
            print("17 - Helicoprion")   
            print("18 - Hybodus")
            print("19 - Megalodon")
            print("20 - Ptychodus")
            print("21 - Scapanorhynchus")
            print("22 - Stethacanthus")
            print("23 - Xenacanthus")    
            subr = int(input("Which subrace would you like? "))   
            if subr == 1:
                subrace = "Blue Sharkin"
            if subr == 2:
                subrace = "Basking Sharkin"
            if subr == 3:
                subrace = "Bull Sharkin"
            if subr == 4:
                subrace = "Cookie Cutter Sharkin"
            if subr == 5:
                subrace = "Goblin Sharkin"  
            if subr == 6:
                subrace = "Hammerhead Sharkin"
            if subr == 7:
                subrace = "Leopard Sharkin"
            if subr == 8:
                subrace = "Mako Sharkin"
            if subr == 9:
                subrace = "Nurse Sharkin"
            if subr == 10:
                subrace = "Thresher Sharkin"
            if subr == 11:
                subrace = "Tiger Sharkin"   
            if subr == 12:
                subrace = "Whale Sharkin"
            if subr == 13:
                subrace = "Great White Sharkin"
            if subr == 14:
                subrace = "Cladoselache"
            if subr == 15:
                subrace = "Cretoxyrhina"
            if subr == 16:
                subrace = "Edestus"
            if subr == 17:
                subrace = "Helicoprion"   
            if subr == 18:
                subrace = "Hybodus"
            if subr == 19:
                subrace = "Megalodon"
            if subr == 20:
                subrace = "Ptychodus"
            if subr == 21:
                subrace = "Scapanorhynchus"
            if subr == 22:
                subrace = "Stethacanthus"
            if subr == 23:
                subrace = "Xenacanthus"                                                                    
            if subr == 0:
                subrace = random.choice(Shark)
        if rce == "50":
            race = "Shifter"
            print("0 - Random")
            print("1 - Beasthide Shifter")
            print("2 - Longtooth Shifter")
            print("3 - Swiftstride Shifter")
            print("4 - Wildhunt Shifter")   
            subr = int(input("Which subrace would you like? "))  
            if subr == 1:
                subrace = "Beasthide Shifter"
            if subr == 2:
                subrace = "Longtooth Shifter"
            if subr == 3:
                subrace = "Swiftstride Shifter"
            if subr == 4:
                subrace = "Wildhunt Shifter"
            if subr == 0: 
                subrace = random.choice(Shi)                                
        if rce == "51":
            race = "Simic Hybrid"                                         
        if rce == "52":
            race = "Strig"   
            print("0 - Random")
            print("1 - Stout Strig")
            print("2 - Swift Strig")  
            subr = int(input("Which subrace would you like? "))    
            if subr == 1:
                subrace = "Stout Strig"
            if subr == 2:
                subrace = "Swift Strig"
            if subr == 0:
                subrace = random.choice(Stri)                                            
        if rce == "53":
            race = "Tabaxi"    
        if rce == "54":
            race = "Thri-Kreen"           
        if rce == "55":
            race = "Tiefling"
            print("0 - Random")
            print("1 - Baalzebul Subject Tiefling")
            print("2 - Dispater Subject Tiefling") 
            print("3 - Fierna Subject Tiefling")
            print("4 - Glasya Subject Tiefling")
            print("5 - Levistus Subject Tiefling") 
            print("6 - Mammon Subject Tiefling")
            print("7 - Mephistopheles Subject Tiefling")
            print("8 - Zariel Subject Tiefling") 
            print("9 - Asmodeus Subject Tiefling")  
            subr = int(input("Which subrace would you like? "))   
            if subr == 1:
                subrace = "Baalzebul Subject Tiefling"
            if subr == 2:
                subrace = "Dispater Subject Tiefling" 
            if subr == 3:
                subrace = "Fierna Subject Tiefling"
            if subr == 4:
                subrace = "Glasya Subject Tiefling"
            if subr == 5:
                subrace = "Levistus Subject Tiefling" 
            if subr == 6:
                subrace = "Mammon Subject Tiefling"
            if subr == 7:
                subrace = "Mephistopheles Subject Tiefling"
            if subr == 8:
                subrace = "Zariel Subject Tiefling" 
            if subr == 9:
                subrace = "Asmodeus Subject Tiefling"                                                                  
            if subr == 0:
                subrace = random.choice(Tie)
        if rce == "56":
            race = "Tortle"            
        if rce == "57":
            race = "Triton"
        if rce == "58":
            race = "Vedalken"   
        if rce == "59":
            race = "Verdan"
        if rce == "60":
            race = "Vulpin"               
        if rce == "61":
            race = "Warforged"
        if rce == "62":
            race = "Wechselkind"               
        if rce == "63":
            race = "Yuan-ti"
        if rce == "0":
            race = random.choice(rac)
            if race == "Aasimar":
                subrace = random.choice(Aas)
            if race == "Cervan":
                subrace = random.choice(Cer)
            if race == "Corginian":
                subrace = random.choice(Corg)
            if race == "Corvum":
                subrace = random.choice(Cor)
            if race == "Dragonborn":
                subrace = random.choice(Dra)   
                colors = ["Black", "Blue", "Green", "Red", "White"] 
                gems = ["Amethyst", "Crystal", "Emerald", "Sapphire", "Topaz"]
                metals = ["Brass", "Bronze", "Copper", "Gold", "Silver"]
                if subrace == "Chromatic Dragonborn":
                    color = random.choice(colors)
                if subrace == "Gem Dragonborn":
                    gem = random.choice(gems)
                if subrace == "Metallic Dragonborn":
                    metal = random.choice(metals)
            if race == "Dwarf":
                subrace = random.choice(Dwf)
            if race == "Elf":
                subrace = random.choice(El) 
            if race == "Gallus":
                subrace = random.choice(Gal)
            if race == "Genasi":
                subrace = random.choice(Ge)
            if race == "Gith":
                subrace = random.choice(Git)
            if race == "Gnome":
                subrace = random.choice(Gn)
            if race == "Halfling":
                subrace = random.choice(Hal)
            if race == "HalfElf":
                subrace = random.choice(HE)
            if race == "Human":
                subrace = random.choice(Hum)
            if race == "Luma":
                subrace = random.choice(Lum)
            if race == "Raptor (Bird)":
                subrace = random.choice(Rap)
            if race == "Sharkin":
                subrace = random.choice(Shark)
            if race == "Shifter":
                subrace = random.choice(Shi)
            if race == "Strig":
                subrace = random.choice(Stri)
            if race == "Tiefling":
                subrace = random.choice(Tie)      
    if param == "N":
        race = random.choice(rac)
        if race == "Aasimar":
            subrace = random.choice(Aas)
        if race == "Cervan":
            subrace = random.choice(Cer)
        if race == "Corginian":
            subrace = random.choice(Corg)
        if race == "Corvum":
            subrace = random.choice(Cor)
        if race == "Dragonborn":
            subrace = random.choice(Dra)
            colors = ["Black", "Blue", "Green", "Red", "White"] 
            gems = ["Amethyst", "Crystal", "Emerald", "Sapphire", "Topaz"]
            metals = ["Brass", "Bronze", "Copper", "Gold", "Silver"]
            if subrace == "Chromatic Dragonborn":
                color = random.choice(colors)
            if subrace == "Gem Dragonborn":
                gem = random.choice(gems)
            if subrace == "Metallic Dragonborn":
                metal = random.choice(metals)
        if race == "Dwarf":
            subrace = random.choice(Dwf)
        if race == "Elf":
            subrace = random.choice(El)        
        if race == "Gallus":
            subrace = random.choice(Gal)
        if race == "Genasi":
            subrace = random.choice(Ge)
        if race == "Gith":
            subrace = random.choice(Git)
        if race == "Gnome":
            subrace = random.choice(Gn)
        if race == "Halfling":
            subrace = random.choice(Hal)
        if race == "HalfElf":
            subrace = random.choice(HE)
        if race == "Human":
            subrace = random.choice(Hum)
        if race == "Luma":
            subrace = random.choice(Lum)
        if race == "Raptor (Bird)":
            subrace = random.choice(Rap)
        if race == "Sharkin":
            subrace = random.choice(Shark)
        if race == "Shifter":
            subrace = random.choice(Shi)
        if race == "Strig":
            subrace = random.choice(Stri)
        if race == "Tiefling":
            subrace = random.choice(Tie)
    Line = ["Dhampir", "Hexblood", "Reborn", "No lineage"]
    if param == "Y":
        if ((race != "Dhampir") and (race != "Hexblood") and (race != "Reborn")):
            Lin = input("Would you like a Ravenloft-Styled lineage to add to your race? Y/N  ")
            if Lin == "Y":
                linea = "Y"
            if Lin == "y":
                linea = "Y"
            if Lin == "Yes":
                linea = "Y"
            if Lin == "yes":
                linea = "Y"
            if Lin == "Ye":
                linea = "Y"
            if Lin == "ye":
                linea = "Y"
            if Lin == "N":
                linea = "N"
            if Lin == "n":
                linea = "N"
            if Lin == "No":
                linea = "N"
            if Lin == "no":
                linea == "N"
        if linea == "Y":
            LINE = ["Dhampir, Hexblood, Reborn"]          
            print("0 - Random")
            print("1 - Dhampir")
            print("2 - Hexblood")
            print("3 - Reborn")
            lineag = input("Which Ravenloft-Styled would you like to add to your race? ")           
            if Lin == "1":
                Lineage = "Dhampir"
            if Lin == "2":
                Lineage = "Hexblood"
            if Lin == "3":
                Lineage = "Reborn"
            if Lin == "4":
                Lineage = "No lineage"
            if Lin == "0":
                Lineage = random.choice(LINE)
        if linea == "N":
            Lineage = "No lineage"
    if param == "N":
        if ((race != "Dhampir") and (race != "Hexblood") and (race != "Reborn")):
            Lineage = random.choice(Line)       

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
    UAur = "You can also understand Auran, though you cannot speak it naturally"
    RaceNotes = []
    RacialBkg = []
    PlProf = []
    PlLang = []
    if ((race == "Corvum") or (race == "Gallus") or (race == "Luma") or (race == "Raptor (Bird)") or (race == "Strig") or (race == "Cervan") or (race == "Hedge") or (race == "Jerbeen") or (race == "Mapach") or (race == "Vulpin")):
        SLANG.remove(Bird)
    else:
        SLANG.remove(Comm)
    ProfBonus = math.ceil(plLvl/4)+1
    Darkvision = "Darkvision: You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
    if race == "Aarakocra":
        Hmo1 = d4()
        Hmo2 = d4()
        Hmod = Hmo1 + Hmo2
        Hbase = 58
        Wmo1 = d10()
        Wmo2 = d10()
        Wmod = Wmo1 + Wmo2
        Wbase = 80
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Aara)
        PlLang.append(Aura)
        SLANG.remove(Aara)
        SLANG.remove(Aura)
        Dexterity += 2
        Wisdom += 1
        walkspeed = 25
        CreatureType = "Avian Humanoid"
        RaceNotes.append("Flight: You have a flying speed of 50 feet. To use this speed, you can't be wearing medium or heavy armor.")
        RaceNotes.append("Talons: You are proficient with your unarmed strikes, which deal 1d4 slashing damage on a hit.")
    if race == "Aasimar":
        Hmo1 = d12()
        Hmo2 = d12()
        Hmo3 = d12()
        Hmod = Hmo1 + Hmo2 + Hmo3
        Hbase = 56
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Cele)
        SLANG.remove(Cele)
        Charisma += 2
        walkspeed = 30
        CreatureType = "Humanoid"
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("Celestial Resistance: You have resistance to necrotic damage and radiant damage.")
        RaceNotes.append("Healing Hands (see notes)")
        Notes.append("Healing Hands: As an action, you can touch a creature and cause it to regain a number of hit points equal to your level. Once you use this trait, you can't use it again until you finish a long rest.")
        RaceNotes.append("Light Bearer: You know the Light cantrip. Charisma is your spellcasting ability for it.")
        if subrace == "Protector Aasimar":
            Wisdom += 1
            if plLvl >= 3:
                RaceNotes.append("Radiant Soul (see notes)")
                Notes.append("Radiant Soul: You can use your action to unleash the divine energy within yourself, causing your eyes to glimmer and two luminous, incorporeal wings to sprout from your back.\nYour transformation lasts for 1 minute or until you end it as a bonus action. During it, you have a flying speed of 30 feet, and once on each of your turns, you can deal extra radiant damage to one target when you deal damage to it with an attack or a spell. The extra radiant damage equals your level.\nOnce you use this trait, you can't use it again until you finish a long rest.")
        if subrace == "Scourge Aasimar":
            Constitution += 1
            if plLvl >= 3:
                RaceNotes.append("Radiant Consumption (see notes)")
                Notes.append("Radiant Consumption: You can use your action to unleash the divine energy within yourself, causing a searing light to radiate from you, pour out of your eyes and mouth, and threaten to char you.\nYour transformation lasts for 1 minute or until you end it as a bonus action. During it, you shed bright light in a 10-foot radius and dim light for an additional 10 feet, and at the end of each of your turns, you and each creature within 10 feet of you take radiant damage equal to half your level (rounded up). In addition, once on each of your turns, you can deal extra radiant damage to one target when you deal damage to it with an attack or a spell. The extra radiant damage equals your level.\nOnce you use this trait, you can't use it again until you finish a long rest.")
        if subrace == "Fallen Aasimar":
            Strength += 1
            if plLvl >= 3:
                RaceNotes.append("Necrotic Shroud (see notes)")
                Notes.append("Necrotic Shroud: You can use your action to unleash the divine energy within yourself, causing your eyes to turn into pools of darkness and two skeletal, ghostly, flightless wings to sprout from your back. The instant you transform, other creatures within 10 feet of you that can see you must succeed on a Charisma saving throw (DC 8 + your proficiency bonus + your Charisma modifier) or become frightened of you until the end of your next turn.\nYour transformation lasts for 1 minute or until you end it as a bonus action. During it, once on each of your turns, you can deal extra necrotic damage to one target when you deal damage to it with an attack or a spell. The extra necrotic damage equals your level.\nOnce you use this trait, you can't use it again until you finish a long rest.")
    if race == "Autognome":
        Hmo1 = d4()
        Hmo2 = d4()
        Hmod = Hmo1 + Hmo2
        Hbase = 31
        Wmo1 = 1
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 35
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        SLANG.remove(Gnom)
        PlLang.append(Comm)
        PlLang.append(Gnom)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = abilityscores(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
        walkspeed = 30
        RaceNotes.append("Armored Casing: You are encased in thin metal or some other durable material. While you aren't wearing armor, your base Armor Class is 13 + your Dexterity modifier.")
        RaceNotes.append("Built for Success (see notes)")
        Notes.append(f"Built for Success: You can add a d4 to one attack roll, ability check, or saving throw you make, and you can do so after seeing the d20 roll but before the effects of the roll are resolved. You can use this trait {ProfBonus} times, and you regain all expended uses when you finish a long rest.")
        RaceNotes.append("Healing Machine (see notes)")
        Notes.append("Healing Machine: If the Mending spell is cast on you, you can spend a Hit Die, roll it, and regain a number of hit points equal to the roll plus your Constitution modifier (minimum of 1 hit point).\nIn addition, your creator designed you to benefit from several spells that preserve life but that normally don't affect Constructs: Cure Wounds, Healing Word, Mass Cure Wounds, Mass Healing Word, and Spare the Dying.")
        RaceNotes.append("Mechanical Nature (see notes)")
        Notes.append("Mechanical Nature: You have resistance to poison damage and immunity to disease, and you have advantage on saving throws against being paralyzed or poisoned. You don't need to eat, drink, or breathe.")
        RaceNotes.append("Sentry's Rest (see notes)")
        Notes.append("Sentry's Rest: When you take a long rest, you spend at least 6 hours in an inactive, motionless state, instead of sleeping. In this state, you appear inert, but you remain conscious.")
        PlProf = arttool2(param, PlProf)
        CreatureType = "Construct"
    if race == "Bugbear":
        Hmo1 = d12()
        Hmo2 = d12()
        Hmod = Hmo1 + Hmo2
        Hbase = 72
        Wmo1 = d6()
        Wmo2 = d6()
        Wmod = Wmo1 + Wmo2
        Wbase = 200
        PlLang.append(Comm)
        PlLang.append(Gobl)
        SLANG.remove(Gobl)
        Strength += 2
        Dexterity += 1
        CreatureType = "Goblinoid"
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("Long-Limbed: When you make a melee attack on your turn, your reach for it is 5 feet greater than normal.")
        RaceNotes.append("Powerful Build: You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.")
        PlProf.append(Stealth)
        RaceNotes.append("Surprise Attack (see notes)")
        Notes.append("Surprise Attack: If you surprise a creature and hit it with an attack on your first turn in combat, the attack deals an extra 2d6 damage to it. You can use this trait only once per combat." )
    if race == "Centaur":
        Hmo1 = d10()
        Hmo2 = 0
        Hmod = Hmo1 + Hmo2
        Hbase = 72
        Wmo1 = d12()
        Wmo2 = d12()
        Wmod = Wmo1 + Wmo2
        Wbase = 600
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        SLANG.remove(Sylv)
        PlLang.append(Comm)
        PlLang.append(Sylv)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        CreatureType = "Fey"
        RaceNotes.append("Charge (see notes)")
        Notes.append("Charge: If you move at least 30 feet straight toward a target and then hit it with a melee weapon attack on the same turn, you can immediately follow that attack with a bonus action, making one attack against the target with your hooves.")
        RaceNotes.append("Hooves (see notes)")
        Notes.append("Hooves: Your hooves are natural melee weapons, which you can use to make unarmed strikes. If you hit with them, you deal bludgeoning damage equal to 1d4 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.")
        RaceNotes.append("Equine Build (see notes)")
        Notes.append("Equine Build: You count as one size larger when determining your carrying capacity and the weight you can push or drag.\nIn addition, any climb that requires hands and feet is especially difficult for you because of your equine legs. When you make such a climb, each foot of movement costs you 4 extra feet, instead of the normal 1 extra foot.")
        PlProf = fourskillprof(param, PlProf, AnimalHandling, Medicine, Nature, Survival)
    if race == "Cervan":
        Constitution += 2
        CreatureType = "Humanoid"
        RaceNotes.append("Practical (see notes)")
        Notes.append("Practical: Cervans are eminently practical and like to spend their time learning useful skills for life in their woodland villages. You gain proficiency in one of the following skills: Athletics, Medicine, Nature, or Survival.")
        RaceNotes.append("Surge of Vigor (see notes)")
        Notes.append("Surge of Vigor: All cervans possess a great tenacity and will to survive, which allows them to bounce back from even the most devastating blows. If an attack deals over half of your current remaining hit points in damage, (even if your hit points are reduced to 0 by the attack) you immediately regain hit points equal to 1d12 + your Constitution Modifier.\nYou can’t use this feature again until you have completed a long rest.")
        if subrace == "Grove Cervan":
            Hmo1 = d10()
            Hmo2 = d10()
            Hmod = Hmo1 + Hmo2
            Hbase = 56
            Wmo1 = d4()
            Wmo2 = 0
            Wmod = Wmo1 + Wmo2
            Wbase = 110
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            Height = str(tl)
            Weight = str(hy)
            PlLang.append(Bird)
            PlLang.append(Cerva)
            SLANG.remove(Cerva)
            Dexterity += 1
            walkspeed = 35
            RaceNotes.append("Standing Leap: Your base long jump is 30 feet, and your base high jump is 15 feet, with or without a running start.")
            RaceNotes.append("Nimble Step: Opportunity attacks made against you are rolled with disadvantage.")      
        if subrace == "Pronghorn Cervan":
            Hmo1 = d10()
            Hmo2 = d10()
            Hmod = Hmo1 + Hmo2
            Hbase = 73
            Wmo1 = d4()
            Wmo2 = d4()
            Wmod = Wmo1 + Wmo2
            Wbase = 120
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            Height = str(tl)
            Weight = str(hy)
            PlLang.append(Bird)
            PlLang.append(Cerva)
            SLANG.remove(Cerva)
            Strength += 1
            RaceNotes.append("Robust Build: Your carrying capacity is doubled, as is the weight you can push, drag, or lift.")
            RaceNotes.append("Antlers (see notes)")
            Notes.append("Antlers: You have a set of large, strong antlers that can be used to make devastating charge attacks. You can use your unarmed strike to gore opponents, dealing 1d6 + your Strength Modifier piercing damage on a hit.\nAdditionally, if you move at least 20 feet in a straight line towards an opponent, you can spend a bonus action to charge them, dealing an extra 1d6 points of piercing damage. If the target of your charge is Large or smaller, they must make a Strength saving throw against a DC of your Proficiency Bonus + 8 + your Strength Modifier. On failure, the target is pushed 10 feet away from you into a space of your choice.")
    if race == "Changeling":
        Hmo1 = d12()
        Hmo2 = d12()
        Hmo3 = d12()
        Hmod = Hmo1 + Hmo2 + Hmo3
        Hbase = 43
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 25
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        Charisma += 2
        Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = singleabilityscore(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
        walkspeed = 30
        CreatureType = "Humanoid"
        RaceNotes.append("Shapechanger (see notes)")
        Notes.append("Shapechanger: As an action, you can change your appearance and your voice. You determine the specifics of the changes, including your coloration, hair length, and sex. You can also adjust your height and weight, but not so much that your size changes. You can make yourself appear as a member of another race, though none of your game statistics change. You can't duplicate the appearance of a creature you've never seen, and you must adopt a form that has the same basic arrangement of limbs that you have. Your clothing and equipment aren't changed by this trait.\nYou stay in the new form until you use an action to revert to your true form or until you die.")
        PlProf = fourskillprof(param, PlProf, Deception, Insight, Intimidation, Persuasion)
    if race == "Corginian":
        Hmo1 = d4()
        Hmo2 = d4()
        Hmod = Hmo1 + Hmo2
        Hbase = 36
        Wmo1 = 1
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 40
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        Charisma += 2
        Wisdom += 1
        walkspeed = 25
        CreatureType = "Fey"
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("Nimble: You can move through the space of any creature that is of a size larger than yours.")
        RaceNotes.append("Slippery: You have advantage on Strength (Athletics) and Dexterity (Acrobatics) checks made to escape a grapple.")
        RaceNotes.append("Strong Jaws (see notes)")
        Notes.append("Strong Jaws: Your jaws are natural weapons, which you can use to make unarmed strikes. If you attack with them, you deal piercing damage equal to 1d4 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.")
        if subrace == "Cardigan Corginian":
            RaceNotes.append("Keen Smell: Cardigan Corginians have sharp, observant snouts. You have advantage on Intelligence (Investigation) and Wisdom (Perception) checks involving smell.")                        
        if subrace == "Pembroke Corginian":
            RaceNotes.append("Keen Hearing: Pembroke Corginians have sharp, observant ears. You have advantage on Intelligence (Investigation) and Wisdom (Perception) checks involving hearing.")
    if race == "Corvum":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 52
        Wmo1 = d4()
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 70
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Bird)
        PlLang.append(UAur)
        Intelligence += 2
        walkspeed = 30
        CreatureType = "Avian Humanoid"
        RaceNotes.append("Glide (see notes)")
        Notes.append("Glide: Using your feathered arms, you can slow your fall, and glide short distances. When falling you can use your reaction to spread your arms, stiffen your wing feathers, and slow your descent. While doing so, you continue to fall gently at a speed of 60 feet per round, taking no fall damage when you land. If you would fall at least 10 feet in this way, you may fly up to your movement speed in one direction you choose, although you cannot choose to move upwards, landing in the space you finish your movement. You cannot glide while carrying heavy weapons or wielding a shield (though you may drop any held items as part of your reaction to spread your arms). You cannot glide while wearing heavy armor, or if you are encumbered.")
        RaceNotes.append("Talons (see notes)")
        Notes.append("Talons: Your sharp claws aid you in unarmed combat and while climbing. Your damage for an unarmed strike is 1d4 piercing damage. Additionally, you have advantage on Strength (Athletics) checks made to climb any surface your talons could reasonably grip.")
        PlProf = fourskillprof(param, PlProf, Arcana, History, Nature, Religion)
        RaceNotes.append("Appraising Eye (see notes)")
        Notes.append("Appraising Eye: You have an almost supernatural ability to appraise objects. By spending an action examining any object, you can determine any magical properties the item has, how they might be used or activated, as well as a fair estimation of market price. Using this skill strains the eyes, and you must complete a long or short rest before you can use it again.")
        if subrace == "Dusk Corvum":
            Dexterity += 1
            RaceNotes.append("Skulker: You have advantage on Dexterity (Stealth) checks made in dim light or darkness.")
            PlProf.append(Insight)
        if subrace == "Kindled Corvum":
            Charisma += 1
            RaceNotes.append("Convincing (see notes)")
            Notes.append("Convincing: Kindled corvums have a way with words, and are accomplished at saying what someone wants or needs to hear. You have proficiency in either the Deception or Persuasion skill. Additionally, you have advantage on all Charisma checks made to convince someone of your exceptional knowledge on any topic related to the skill you selected with your learned trait (Arcana, History, Nature, or Religion).")
            KindledCorvumProf = ["Languages", "Tools"]
            KindledCorvumProfRand = random.choice(KindledCorvumProf)
            if param == "Y":
                print("0 - Random")
                print("1 - One language of your choice")
                print("2 - One Tool of your choice")
                kcprof = int(input("Choose whether to gain proficiency in a language or a tool. "))
                if kcprof == 1:
                    PlLang, SLANG = languagegen(param, PlLang, SLANG)
                if kcprof == 2:
                    PlProf = artisantools(param, PlProf)
                if kcprof == 0:
                    if KindledCorvumProfRand == "Languages":
                        PlLang, SLANG = languagegen(param, PlLang, SLANG)
                    if KindledCorvumProfRand == "Tools":
                        PlProf = artisantools(param, PlProf)
            if param == "N":
                if KindledCorvumProfRand == "Languages":
                    PlLang, SLANG = languagegen(param, PlLang, SLANG)
                if KindledCorvumProfRand == "Tools":
                    PlProf = artisantools(param, PlProf)
            RaceNotes.append("Sharp Mind: You are able to accurately recall with perfect clarity anything you have seen or heard within the past month.")
    if race == "Dhampir":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = abilityscores(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
        CreatureType = "Humanoid"
        walkspeed = 35
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("Deathless Nature: You don’t need to breathe.")
        RaceNotes.append("Spider Climb (see notes)")
        Notes.append("Spider Climb: You have a climbing speed equal to your walking speed. In addition, at 3rd level, you can move up, down, and across vertical surfaces and upside down along ceilings, while leaving your hands free.")
        RaceNotes.append("Vampiric Bite (see notes)")
        Notes.append(f"Vampiric Bite: Your fanged bite is a natural weapon, which counts as a simple melee weapon with which you are proficient. You add your Constitution modifier, instead of your Strength modifier, to the attack and damage rolls when you attack with this bite. It deals 1d4 piercing damage on a hit. While you are missing half or more of your hit points, you have advantage on attack rolls you make with this bite. When you attack with this bite and hit a creature that isn’t a Construct or an Undead, you can empower yourself in one of the following ways of your choice: You regain hit points equal to the piercing damage dealt by the bite. You gain a bonus to the next ability check or attack roll you make; the bonus equals the piercing damage dealt by the bite. You can empower yourself with this bite {ProfBonus} times, and you regain all expended uses when you finish a long rest.")
    if race == "Disembodied":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        Intelligence += 1
        Dexterity += 1
        walkspeed = 30
        CreatureType = "Humanoid"
        RaceNotes.append("Fade Away (see notes)")
        Notes.append("Fade Away: On your turn, as an action, you can fade from the Material Realm and disappear into the ethereal plane. While you remain faded away, you cannot interact with the Material Plane, and effects on the Material Plane cannot interact with you, including spells and creatures. However, you can move and hear as normal, and see everything in shades of grey.\nThis effect lasts for 1 minute, or until you use a bonus action to end it. When the effect ends, you reappear in the Material Plane, in the closest unoccupied space you disappeared from. Once you use this feature, you cannot use it again until you complete a long rest.")
        RaceNotes.append("Planar Outcast(1) (see notes). More options are available at higher levels.")
        Notes.append("Planar Outcast(1): You may cast the Feather Fall spell once per day, targeting yourself only. Intelligence is your spellcasting ability for this spell. More options are available at higher levels.")
        if plLvl >= 3:
            RaceNotes.append("Planar Outcast(2) (see notes)")
            Notes.append("Planar Outcast(2): You may cast the Blur spell once per day. Intelligence is your spellcasting ability for this spell.")
        if plLvl >= 5:
            RaceNotes.append("Planar Outcast(3) (see notes)")
            Notes.append("Planar Outcast(3): You may cast the Blink spell once per day. Intelligence is your spellcasting ability for this spell.")
        PlProf.append(Arcana)
    if race == "Dragonborn":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 66
        Wmo1 = d6()
        Wmo2 = d6()
        Wmod = Wmo1 + Wmo2
        Wbase = 175
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Drac)
        SLANG.remove(Drac)
        CreatureType = "Dragonoid"
        if subrace == "Black Scale Dragonborn":
            Strength += 2
            Charisma += 1
            walkspeed = 30 
            DamageResistance = "Acid Damage"
            RaceNotes.append(f"Damage Resistance: {DamageResistance}")
            BWDT = "Acid Damage"
            RaceNotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "5 by 30 ft. line (Dex. save)"
            RaceNotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((plLvl >= 1) & (plLvl < 6)):
                BreathWeaponDMG = "2d6"
            if ((plLvl >= 6) & (plLvl < 11)):
                BreathWeaponDMG = "3d6"
            if ((plLvl >= 11) & (plLvl < 16)):
                BreathWeaponDMG = "4d6"
            if plLvl >= 16:
                BreathWeaponDMG = "5d6"  
            Notes.append(f"Breath Weapon: You can use your action to exhale destructive energy. The size of this breath weapon is {BreathWeaponSize} and deals {BWDT}. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw (described in the last sentence). The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {BreathWeaponDMG} damage on a failed save, and half as much damage on a successful one. After you use your breath weapon, you can’t use it again until you complete a short or long rest.")            
        if subrace == "Blue Scale Dragonborn":
            Strength += 2
            Charisma += 1
            walkspeed = 30            
            DamageResistance = "Lightning Damage"
            RaceNotes.append(f"Damage Resistance: {DamageResistance}")
            BWDT = "Lightning Damage"
            RaceNotes.append("Breath Weapon (see notes)")
            BreathWeaponSize  = "5 by 30 ft. line (Dex. save)"
            RaceNotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((plLvl >= 1) & (plLvl < 6)):
                BreathWeaponDMG = "2d6"
            if ((plLvl >= 6) & (plLvl < 11)):
                BreathWeaponDMG = "3d6"
            if ((plLvl >= 11) & (plLvl < 16)):
                BreathWeaponDMG = "4d6"
            if plLvl >= 16:
                BreathWeaponDMG = "5d6"  
            Notes.append(f"Breath Weapon: You can use your action to exhale destructive energy. The size of this breath weapon is {BreathWeaponSize} and deals {BWDT}. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw (described in the last sentence). The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {BreathWeaponDMG} damage on a failed save, and half as much damage on a successful one. After you use your breath weapon, you can’t use it again until you complete a short or long rest.")            
        if subrace == "Brass Scale Dragonborn":
            Strength += 2
            Charisma += 1
            walkspeed = 30            
            DamageResistance = "Fire Damage"
            RaceNotes.append(f"Damage Resistance: {DamageResistance}")
            BWDT = "Fire Damage"
            RaceNotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "5 by 30 ft. line (Dex. save)"
            RaceNotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((plLvl >= 1) & (plLvl < 6)):
                BreathWeaponDMG = "2d6"
            if ((plLvl >= 6) & (plLvl < 11)):
                BreathWeaponDMG = "3d6"
            if ((plLvl >= 11) & (plLvl < 16)):
                BreathWeaponDMG = "4d6"
            if plLvl >= 16:
                BreathWeaponDMG = "5d6"  
            Notes.append(f"Breath Weapon: You can use your action to exhale destructive energy. The size of this breath weapon is {BreathWeaponSize} and deals {BWDT}. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw (described in the last sentence). The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {BreathWeaponDMG} damage on a failed save, and half as much damage on a successful one. After you use your breath weapon, you can’t use it again until you complete a short or long rest.")
        if subrace == "Bronze Scale Dragonborn":
            Strength += 2
            Charisma += 1
            walkspeed = 30            
            DamageResistance = "Lightning Damage"
            RaceNotes.append(f"Damage Resistance: {DamageResistance}")
            BWDT = "Lightning Damage"
            RaceNotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "5 by 30 ft. line (Dex. save)"
            RaceNotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((plLvl >= 1) & (plLvl < 6)):
                BreathWeaponDMG = "2d6"
            if ((plLvl >= 6) & (plLvl < 11)):
                BreathWeaponDMG = "3d6"
            if ((plLvl >= 11) & (plLvl < 16)):
                BreathWeaponDMG = "4d6"
            if plLvl >= 16:
                BreathWeaponDMG = "5d6"  
            Notes.append(f"Breath Weapon: You can use your action to exhale destructive energy. The size of this breath weapon is {BreathWeaponSize} and deals {BWDT}. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw (described in the last sentence). The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {BreathWeaponDMG} damage on a failed save, and half as much damage on a successful one. After you use your breath weapon, you can’t use it again until you complete a short or long rest.")
        if subrace == "Chromatic Dragonborn":
            Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = abilityscores(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
            walkingspeed = 30
            Notes.append("Chromatic Dragonborn: If need be, please see Fizban's Treasury of Dragons (tm) for more details about Chromatic Dragonborn.") 
            if color == "Black":
                DamageResistance = "Acid Damage"
                BWDT = "Acid Damage"
            if color == "Blue":
                DamageResistance = "Lightning Damage"
                BWDT = "Lightning Damage"
            if color == "Green":
                DamageResistance = "Poison Damage"
                BWDT = "Poison Damage"
            if color == "Red":
                DamageResistance = "Fire Damage"
                BWDT = "Fire Damage"
            if color == "White":
                DamageResistance = "Cold Damage"
                BWDT = "Cold Damage"                 
            RaceNotes.append(f"Damage Resistance: {DamageResistance}")                                           
            RaceNotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "5 by 30 ft. line (Dex. save)"
            RaceNotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((plLvl >= 1) & (plLvl < 5)):
                BreathWeaponDMG = "1d10"
            if ((plLvl >= 5) & (plLvl < 11)):
                BreathWeaponDMG = "2d10"
            if ((plLvl >= 11) & (plLvl < 17)):
                BreathWeaponDMG = "3d10"
            if plLvl >= 17:
                BreathWeaponDMG = "4d10"                                
            Notes.append(f"Breath Weapon: When you take the Attack action on your turn, you can replace one of your attacks with an exhalation of magical energy in a 30-foot line that is 5 feet wide. Each creature in that area must make a Dexterity saving throw (DC = 8 + your Constitution modifier + your proficiency bonus). On a failed save, the creature takes {BreathWeaponDMG} {BWDT}. On a successful save, it takes half as much damage.\nYou can use your Breath Weapon {ProfBonus} times, and you regain all expended uses when you finish a long rest.")
            if plLvl >= 5:
                Notes.append("As an action, you can channel your draconic energy to protect yourself. For 1 minute, you become immune to the damage type associated with your Chromatic Ancestry (color). Once you use this trait, you can't do so again until you finish a long rest.")
        if subrace == "Copper Scale Dragonborn":
            Strength += 2
            Charisma += 1
            walkspeed = 30            
            DamageResistance = "Acid Damage"
            RaceNotes.append(f"Damage Resistance: {DamageResistance}")
            BWDT = "Acid Damage"
            RaceNotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "5 by 30 ft. line (Dex. save)"
            RaceNotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((plLvl >= 1) & (plLvl < 6)):
                BreathWeaponDMG = "2d6"
            if ((plLvl >= 6) & (plLvl < 11)):
                BreathWeaponDMG = "3d6"
            if ((plLvl >= 11) & (plLvl < 16)):
                BreathWeaponDMG = "4d6"
            if plLvl >= 16:
                BreathWeaponDMG = "5d6"  
            Notes.append(f"Breath Weapon: You can use your action to exhale destructive energy. The size of this breath weapon is {BreathWeaponSize} and deals {BWDT}. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw (described in the last sentence). The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {BreathWeaponDMG} damage on a failed save, and half as much damage on a successful one. After you use your breath weapon, you can’t use it again until you complete a short or long rest.")
        if subrace == "Draconblood Dragonborn":
            Intelligence += 2
            Charisma += 1
            walkspeed = 30
            RaceNotes.append("Darkvision (see notes)") 
            Notes.append(Darkvision)
            RaceNotes.append("Forceful Presence (see notes)")
            Notes.append("Forceful Presence: You can use your understanding of creative diplomacy or intimidation to guide a conversation in your favor. When you make a Charisma (Intimidation or Persuasion) check, you can do so with advantage. Once you use this trait, you can't do so again until you finish a short or long rest.")
        if subrace == "Gem Dragonborn":
            Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = abilityscores(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
            walkingspeed = 30
            Notes.append("Gem Dragonborn: If need be, please see Fizban's Treasury of Dragons (tm) for more details about Gem Dragonborn.")
            if gem == "Amethyst":
                DamageResistance = "Force Damage"
                BWDT = "Force Damage"
            if gem == "Crystal":
                DamageResistance = "Radiant Damage"
                BWDT = "Radiant Damage"
            if gem == "Emerald":
                DamageResistance = "Psychic Damage"
                BWDT = "Psychic Damage"
            if gem == "Sapphire":
                DamageResistance = "Thunder Damage"
                BWDT = "Thunder Damage"
            if gem == "Topaz":
                DamageResistance = "Necrotic Damage"
                BWDT = "Necrotic Damage"   
            RaceNotes.append(f"Draconic Resistance - You have resistance to: {DamageResistance}")
            RaceNotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "5 by 30 ft. line (Dex. save)"
            RaceNotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((plLvl >= 1) & (plLvl < 5)):
                BreathWeaponDMG = "1d10"
            if ((plLvl >= 5) & (plLvl < 11)):
                BreathWeaponDMG = "2d10"
            if ((plLvl >= 11) & (plLvl < 17)):
                BreathWeaponDMG = "3d10"
            if plLvl >= 17:
                BreathWeaponDMG = "4d10"                                
            Notes.append(f"Breath Weapon: When you take the Attack action on your turn, you can replace one of your attacks with an exhalation of magical energy in a 30-foot line that is 5 feet wide. Each creature in that area must make a Dexterity saving throw (DC = 8 + your Constitution modifier + your proficiency bonus). On a failed save, the creature takes {BreathWeaponDMG} {BWDT}. On a successful save, it takes half as much damage.\nYou can use your Breath Weapon {ProfBonus} times, and you regain all expended uses when you finish a long rest.")
            RaceNotes.append("Psionic Mind (see notes)")
            Notes.append("Psionic Mind: You can send telepathic messages to any creature you can see within 30 feet of you. You don't need to share a language with the creature for it to understand these messages, but it must be able to understand at least one language to comprehend them.")
            if plLvl >= 5:
                RaceNotes.append("Gem Flight (see notes)")
                Notes.append("Gem Flight: You can use a bonus action to manifest spectral wings on your body. These wings last for 1 minute. For the duration, you gain a flying speed equal to your walking speed and can hover. Once you use this trait, you can't do so again until you finish a long rest.")
        if subrace == "Gold Scale Dragonborn":
            Strength += 2
            Charisma += 1
            walkspeed = 30            
            DamageResistance = "Fire Damage"
            RaceNotes.append(f"Damage Resistance: {DamageResistance}")
            BWDT = "Fire Damage"
            RaceNotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "5 by 30 ft. line (Dex. save)"
            RaceNotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((plLvl >= 1) & (plLvl < 6)):
                BreathWeaponDMG = "2d6"
            if ((plLvl >= 6) & (plLvl < 11)):
                BreathWeaponDMG = "3d6"
            if ((plLvl >= 11) & (plLvl < 16)):
                BreathWeaponDMG = "4d6"
            if plLvl >= 16:
                BreathWeaponDMG = "5d6"  
            Notes.append(f"Breath Weapon: You can use your action to exhale destructive energy. The size of this breath weapon is {BreathWeaponSize} and deals {BWDT}. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw (described in the last sentence). The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {BreathWeaponDMG} damage on a failed save, and half as much damage on a successful one. After you use your breath weapon, you can’t use it again until you complete a short or long rest.")
        if subrace == "Green Scale Dragonborn":
            Strength += 2
            Charisma += 1
            walkspeed = 30
            DamageResistance = "Poison Damage"
            RaceNotes.append(f"Damage Resistance: {DamageResistance}")
            BWDT = "Poison Damage"
            RaceNotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "15 ft. cone (Con. save)"
            RaceNotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((plLvl >= 1) & (plLvl < 6)):
                BreathWeaponDMG = "2d6"
            if ((plLvl >= 6) & (plLvl < 11)):
                BreathWeaponDMG = "3d6"
            if ((plLvl >= 11) & (plLvl < 16)):
                BreathWeaponDMG = "4d6"
            if plLvl >= 16:
                BreathWeaponDMG = "5d6"  
            Notes.append(f"Breath Weapon: You can use your action to exhale destructive energy. The size of this breath weapon is {BreathWeaponSize} and deals {BWDT}. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw (described in the last sentence). The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {BreathWeaponDMG} damage on a failed save, and half as much damage on a successful one. After you use your breath weapon, you can’t use it again until you complete a short or long rest.")
        if subrace == "Metallic Dragonborn":
            Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = abilityscores(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
            walkingspeed = 30
            Notes.append("Metallic Dragonborn: If need be, please see Fizban's Treasury of Dragons (tm) for more details about Metallic Dragonborn.")
            if metal == "Brass":
                DamageResistance = "Fire Damage"
                BWDT = "Fire Damage"
            if metal == "Bronze":
                DamageResistance = "Lightning Damage"
                BWDT = "Lightning Damage"
            if metal == "Copper":
                DamageResistance = "Acid Damage"
                BWDT = "Acid Damage"
            if metal == "Gold":
                DamageResistance = "Fire Damage"
                BWDT = "Fire Damage"
            if metal == "Silver":
                DamageResistance = "Cold Damage"
                BWDT = "Cold Damage" 
            RaceNotes.append(f"Damage Resistance: {DamageResistance}")
            RaceNotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "15 ft. cone (Con. save)"
            RaceNotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((plLvl >= 1) & (plLvl < 5)):
                BreathWeaponDMG = "1d10"
            if ((plLvl >= 5) & (plLvl < 11)):
                BreathWeaponDMG = "2d10"
            if ((plLvl >= 11) & (plLvl < 17)):
                BreathWeaponDMG = "3d10"
            if plLvl >= 17:
                BreathWeaponDMG = "4d10"                                
            Notes.append(f"Breath Weapon: When you take the Attack action on your turn, you can replace one of your attacks with an exhalation of magical energy in a 30-foot line that is 5 feet wide. Each creature in that area must make a Dexterity saving throw (DC = 8 + your Constitution modifier + your proficiency bonus). On a failed save, the creature takes {BreathWeaponDMG} {BWDT}. On a successful save, it takes half as much damage.\nYou can use your Breath Weapon {ProfBonus} times, and you regain all expended uses when you finish a long rest.")
            if plLvl >= 5:
                RaceNotes.append("Metallic Breath Weapon (see notes)")
                Notes.append("Metallic Breath Weapon: You gain a second breath weapon. When you take the Attack action on your turn, you can replace one of your attacks with an exhalation in a 15-foot cone. The save DC for this breath is 8 + your Constitution modifier + your proficiency bonus. Whenever you use this trait, choose one:\nEnervating Breath - Each creature in the cone must succeed on a Constitution saving throw or become incapacitated until the start of your next turn.\nRepulsion Breath - Each creature in the cone must succeed on a Strength saving throw or be pushed 20 feet away from you and be knocked prone.\nOnce you use your Metallic Breath Weapon, you can't do so again until you finish a long rest.")
        if subrace == "Red Scale Dragonborn":
            Strength += 2
            Charisma += 1
            walkspeed = 30            
            DamageResistance = "Fire Damage"
            RaceNotes.append(f"Damage Resistance: {DamageResistance}")
            BWDT = "Fire Damage"
            RaceNotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "15 ft. cone (Con. save)"
            RaceNotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((plLvl >= 1) & (plLvl < 6)):
                BreathWeaponDMG = "2d6"
            if ((plLvl >= 6) & (plLvl < 11)):
                BreathWeaponDMG = "3d6"
            if ((plLvl >= 11) & (plLvl < 16)):
                BreathWeaponDMG = "4d6"
            if plLvl >= 16:
                BreathWeaponDMG = "5d6"  
            Notes.append(f"Breath Weapon: You can use your action to exhale destructive energy. The size of this breath weapon is {BreathWeaponSize} and deals {BWDT}. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw (described in the last sentence). The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {BreathWeaponDMG} damage on a failed save, and half as much damage on a successful one. After you use your breath weapon, you can’t use it again until you complete a short or long rest.")
        if subrace == "Ravenite Dragonborn":
            Strength += 2
            Constitution += 1
            RaceNotes.append("Darkvision (see notes)")
            Notes.append(Darkvision)
            RaceNotes.append("Vengeful Assault (see notes)")
            Notes.append("Vengeful Assault: When you take damage from a creature in range of a weapon you are wielding, you can use your reaction to make an attack with the weapon against that creature. Once you use this trait, you can't do so again until you finish a short or long rest.")
        if subrace == "Silver Scale Dragonborn":
            Strength += 2
            Charisma += 1
            walkspeed = 30            
            DamageResistance = "Cold Damage"
            RaceNotes.append(f"Damage Resistance: {DamageResistance}")
            BWDT = "Cold Damage"
            RaceNotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "15 ft. cone (Con. save)"
            RaceNotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((plLvl >= 1) & (plLvl < 6)):
                BreathWeaponDMG = "2d6"
            if ((plLvl >= 6) & (plLvl < 11)):
                BreathWeaponDMG = "3d6"
            if ((plLvl >= 11) & (plLvl < 16)):
                BreathWeaponDMG = "4d6"
            if plLvl >= 16:
                BreathWeaponDMG = "5d6"  
            Notes.append(f"Breath Weapon: You can use your action to exhale destructive energy. The size of this breath weapon is {BreathWeaponSize} and deals {BWDT}. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw (described in the last sentence). The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {BreathWeaponDMG} damage on a failed save, and half as much damage on a successful one. After you use your breath weapon, you can’t use it again until you complete a short or long rest.")
        if subrace == "White Scale Dragonborn":
            Strength += 2
            Charisma += 1
            walkspeed = 30            
            DamageResistance = "Cold Damage"
            RaceNotes.append(f"Damage Resistance: {DamageResistance}")
            BWDT = "Cold Damage"
            RaceNotes.append("Breath Weapon (see notes)")
            BreathWeaponSize = "15 ft. cone (Con. save)"
            RaceNotes.append(f"Breath Weapon Size and Damage Type: {BreathWeaponSize}, {BWDT}")
            if ((plLvl >= 1) & (plLvl < 6)):
                BreathWeaponDMG = "2d6"
            if ((plLvl >= 6) & (plLvl < 11)):
                BreathWeaponDMG = "3d6"
            if ((plLvl >= 11) & (plLvl < 16)):
                BreathWeaponDMG = "4d6"
            if plLvl >= 16:
                BreathWeaponDMG = "5d6"  
            Notes.append(f"Breath Weapon: You can use your action to exhale destructive energy. The size of this breath weapon is {BreathWeaponSize} and deals {BWDT}. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw (described in the last sentence). The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes {BreathWeaponDMG} damage on a failed save, and half as much damage on a successful one. After you use your breath weapon, you can’t use it again until you complete a short or long rest.")
    if race == "Dwarf":
        Constitution += 2
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("Dwarven Resilience: You have advantage on saving throws against poison, and you have resistance against poison Damage")
        PlProf.append(Battleaxe)
        PlProf.append(Handaxe)
        PlProf.append(LightHammer)
        PlProf.append(Warhammer)
        PlProf = threetoolprof(param, PlProf, SmthTools, BrewSupp, MasnTools)
        RaceNotes.append("Stonecunning (see notes)")
        Notes.append(f"Stonecunning: Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, or {2*ProfBonus}, instead of your normal proficiency bonus.")
        walkingspeed = 25
        CreatureType = "Humanoid"
        RaceNotes.append("Speed: Your speed is not reduced by wearing heavy armor.") 
        if subrace == "Duergar":
            Hmo1 = d4()
            Hmo2 = d4()
            Hmod = Hmo1 + Hmo2
            Hbase = 48
            Wmo1 = d6()
            Wmo2 = d6()
            Wmod = Wmo1 + Wmo2
            Wbase = 115
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            Height = str(tl)
            Weight = str(hy)
            PlLang.append(Comm)
            PlLang.append(Dwarvi)
            SLANG.remove(Dwarvi)            
            Strength += 1
            RaceNotes.remove(Darkvision)
            RaceNotes.append("Superior Darkvision (see notes)")
            Notes.append("Superior Darkvision: You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.")
            RaceNotes.append("Duergar Resilience: You have advantage on saving throws against illusions and against being charmed or paralyzed.")
            RaceNotes.append("Duergar Magic(1) (see notes). More options are available at higher levels.")
            Notes.append("Duergar Magic(1): You can cast the Enlarge/Reduce spell on yourself once with this trait, using only the spell's enlarge option. You don't need material components for this spell, and you can't cast it while you're in direct sunlight, although sunlight has no effect on it once cast. You regain the ability to cast this spell with this trait when you finish a long rest. Intelligence is your spellcasting ability for this spell.")
            if plLvl >= 5:
                RaceNotes.append("Duergar Magic(2) (see notes)")
                Notes.append("Duergar Magic(2): You can cast the Invisibility spell on yourself once with this trait. You don't need material components for this spell, and you can't cast it while you're in direct sunlight, although sunlight has no effect on it once cast. You regain the ability to cast this spell with this trait when you finish a long rest. Intelligence is your spellcasting ability for this spell.")
            RaceNotes.append("Sunlight Sensitivity (see notes)")
            Notes.append("Sunlight Sensitivity: You have disadvantage on Attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight.")
        if subrace == "Hill Dwarf":
            Hmo1 = d4()
            Hmo2 = d4()
            Hmod = Hmo1 + Hmo2
            Hbase = 46
            Wmo1 = d6()
            Wmo2 = d6()
            Wmod = Wmo1 + Wmo2
            Wbase = 115    
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            Height = str(tl)
            Weight = str(hy)               
            PlLang.append(Comm)
            PlLang.append(Dwarvi)
            SLANG.remove(Dwarvi)
            Wisdom += 1
            RaceNotes.append("Dwarven Toughness: Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.")
        if subrace == "Mountain Dwarf":
            Hmo1 = d4()
            Hmo2 = d4()
            Hmod = Hmo1 + Hmo2
            Hbase = 46
            Wmo1 = d6()
            Wmo2 = d6()
            Wmod = Wmo1 + Wmo2
            Wbase = 115  
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            Height = str(tl)
            Weight = str(hy)                
            PlLang.append(Comm)
            PlLang.append(Dwarvi)
            SLANG.remove(Dwarvi)
            Strength += 2
            PlProf.append(LightArmor)
            PlProf.append(MediumArmor) 
    if race == "Elf":
        walkingspeed = 30
        CreatureType = "Humanoid"
        Dexterity += 2
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        PlProf.append(Perception)
        RaceNotes.append("Fey Ancestry: You have advantage on saving throws against being charmed, and magic can’t put you to sleep.")
        if subrace == "Astral Elf":
            Hmo1 = d6()
            Hmo2 = d6()
            Hmod = Hmo1 + Hmo2
            Hbase = 44
            Wmo1 = d6()
            Wmo2 = d6()
            Wmod = Wmo1 + Wmo2
            Wbase = 75
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            Height = str(tl)
            Weight = str(hy)
            SLANG.remove(Elvi)
            PlLang.append(Comm)
            PlLang.append(Elvi)
            PlLang, SLANG = languagegen(param, PlLang, SLANG)
            Dexterity -= 2
            Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = abilityscores(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
            RaceNotes.append("Astral Fire (see notes)")
            Notes.append("Astral Fire: You know one of the following cantrips of your choice: dancing lights, light, or sacred flame. Intelligence, Wisdom, or Charisma is your spellcasting ability for it (choose when you select this race).")           
            RaceNotes.append("Starlight Step (see Notes)")
            Notes.append(f"Starlight Step - As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. You can use this trait {ProfBonus} times, and you regain all expended uses when you finish a long rest.")
            RaceNotes.append("Astral Trance (see notes)")
            Notes.append("Astral Trance - You don't need to sleep, and magic can't put you to sleep. You can finish a long rest in 4 hours if you spend those hours in a trancelike meditation, during which you remain conscious.\nWhenever you finish this trance, you gain proficiency in one skill of your choice and with one weapon or tool of your choice, selected from the Player's Handbook. You mystically acquire these proficiencies by drawing them from shared elven memory and the experiences of entities on the Astral Plane, and you retain them until you finish your next long rest.")
        if subrace == "Dark Elf":
            Hmo1 = d6()
            Hmo2 = d6()
            Hmod = Hmo1 + Hmo2
            Hbase = 44
            Wmo1 = d6()
            Wmo2 = d6()
            Wmod = Wmo1 + Wmo2
            Wbase = 75
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            Height = str(tl)
            Weight = str(hy)
            PlLang.append(Comm)
            PlLang.append(Elvi)
            SLANG.remove(Elvi)           
            Charisma += 1
            RaceNotes.remove(Darkvision)
            RaceNotes.append("Superior Darkvision (see notes)")
            Notes.append("Superior Darkvision: You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.")
            RaceNotes.append("Sunlight Sensitivity (see notes)")
            Notes.append("Sunlight Sensitivity: You have disadvantage on Attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight.")            
            RaceNotes.append("Drow Magic(1) (see notes). More options are available at higher levels.")
            Notes.append("Drow Magic(1): You know the Dancing Lights cantrip. More options are available at higher levels.")
            if plLvl >= 3:
                RaceNotes.append("Drow Magic(2) (see notes).")
                Notes.append("Drow Magic(2): You can cast the Faerie Fire spell once per day; you must finish a long rest in order to cast the spell again using this trait. Charisma is your spellcasting ability for this spell.")
            if plLvl >= 5:
                RaceNotes.append("Drow Magic(3) (see notes).")
                Notes.append("Drow Magic(3): You can also cast the Darkness spell once per day; you must finish a long rest in order to cast the spell again using this trait. Charisma is your spellcasting ability for this spell.")                             
            RaceNotes.append("Trance (see notes)")
            Notes.append("Trance: Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is “trance.”) While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.")                
            PlProf.append(Rapier)
            PlProf.append(Shortsword)
            PlProf.append(HandCrossbow)
        if subrace == "Eladrin":
            Hmo1 = d12()
            Hmo2 = d12()
            Hmod = Hmo1 + Hmo2
            Hbase = 54
            Wmo1 = d4()
            Wmo2 = 0
            Wmod = Wmo1 + Wmo2
            Wbase = 90
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            Height = str(tl)
            Weight = str(hy)
            SLANG.remove(Elvi)
            PlLang.append(Comm)
            PlLang.append(Elvi)
            PlLang, SLANG = languagegen(param, PlLang, SLANG)
            Charisma += 1
            RaceNotes.append("Trance (see notes)")
            Notes.append("Trance: Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is “trance.”) While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.")    
        if subrace == "High Elf": 
            Hmo1 = d10()
            Hmo2 = d10()
            Hmod = Hmo1 + Hmo2
            Hbase = 90
            Wmo1 = d4()
            Wmo2 = d4()
            Wmod = Wmo1 + Wmo2
            Wbase = 100
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            Height = str(tl)
            Weight = str(hy)
            SLANG.remove(Elvi)
            PlLang.append(Comm)
            PlLang.append(Elvi)
            PlLang, SLANG = languagegen(param, PlLang, SLANG)            
            Intelligence += 1
            PlProf.append(Longsword)
            PlProf.append(Shortsword)
            PlProf.append(Shortbow)
            PlProf.append(Longbow)
            RaceNotes.append("Wizard Cantrip (see notes)")
            Notes.append("Wizard Cantrip: You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it.")
            RaceNotes.append("Trance (see notes)")
            Notes.append("Trance: Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is “trance.”) While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.")            
        if subrace == "Sea Elf":
            Hmo1 = d8()
            Hmo2 = d8()
            Hmod = Hmo1 + Hmo2
            Hbase = 54
            Wmo1 = d4()
            Wmo2 = 0
            Wmod = Wmo1 + Wmo2
            Wbase = 90
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            Height = str(tl)
            Weight = str(hy)
            SLANG.remove(Elvi)
            PlLang.append(Comm)
            PlLang.append(Elvi)
            PlLang.append(Aqua)
            SLANG.remove(Aqua)
            Constitution += 1
            PlProf.append(Spear)
            PlProf.append(Trident)
            PlProf.append(LightCrossbow)
            PlProf.append(Net)
            RaceNotes.append("Child of the Sea: You have a swimming speed of 30 feet, and you can breathe air and water.")
            RaceNotes.append("Friend of the Sea: Using gestures and sounds, you can communicate simple ideas with any beast that has an innate swimming speed.")
            RaceNotes.append("Trance (see notes)")
            Notes.append("Trance: Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is “trance.”) While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.")
        if subrace == "Shadar-kai":
            Hmo1 = d8()
            Hmo2 = d8()
            Hmod = Hmo1 + Hmo2
            Hbase = 56
            Wmo1 = d4()
            Wmo2 = 0
            Wmod = Wmo1 + Wmo2
            Wbase = 90
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            Height = str(tl)
            Weight = str(hy)
            PlLang.append(Comm)
            PlLang.append(Elvi)
            SLANG.remove(Elvi)
            Constitution += 1
            DamageResistance = "Necrotic Damage"
            RaceNotes.append(f"Damage Resistance: {DamageResistance}")
            RaceNotes.append("Blessing of the Raven Queen(1) (see notes). More options are available at higher levels.")
            Notes.append("Blessing of the Raven Queen(1): As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. Once you use this trait, you can't do so again until you finish a long rest.")
            if plLvl >= 3:
                RaceNotes.append("Blessing of the Raven Queen(2) (see notes)")
                Notes.append("Blessing of the Raven Queen(2): You also gain resistance to all damage when you teleport using this trait. The resistance lasts until the start of your next turn. During that time, you appear ghostly and translucent.")
            RaceNotes.append("Trance (see notes)")
            Notes.append("Trance: Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is “trance.”) While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.")
        if subrace == "Wood Elf":
            Hmo1 = d10()
            Hmo2 = d10()
            Hmod = Hmo1 + Hmo2
            Hbase = 90
            Wmo1 = d4()
            Wmo2 = d4()
            Wmod = Wmo1 + Wmo2
            Wbase = 100
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            Height = str(tl)
            Weight = str(hy)
            PlLang.append(Comm)
            PlLang.append(Elvi)
            SLANG.remove(Elvi)
            Wisdom += 1
            PlProf.append(Longsword)
            PlProf.append(Shortsword)
            PlProf.append(Shortbow)
            PlProf.append(Longbow)            
            walkingspeed = 35
            RaceNotes.append("Mask of the Wild: You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.")
            RaceNotes.append("Trance (see notes)")
            Notes.append("Trance: Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is “trance.”) While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.")            
    if race == "Fairy":
        Hmo1 = d4()
        Hmo2 = d4()
        Hmod = Hmo1 + Hmo2
        Hbase = 21
        Wmo1 = 1
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 20
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = abilityscores(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
        CreatureType = "Fey"
        walkingspeed = 30
        RaceNotes.append("Flight: Because of your wings, you have a flying speed equal to your walking speed. You can't use this flying speed if you're wearing medium or heavy armor.")
        RaceNotes.append("Fairy Magic(1) (see notes). More options are available at higher levels.")
        Notes.append("Fairy Magic(1): You know the Druidcraft cantrip. More options are available at higher levels.")
        if plLvl >= 3:
            RaceNotes.append("Fairy Magic(2) (see notes)")
            Notes.append("Fairy Magic(2): You can cast the Faerie Fire spell with this trait. Once you cast Faerie Fire with this trait, you can't cast that spell with it again until you finish a long rest. You can also cast this spell using any spell slots you have of the appropriate level. Intelligence, Wisdom, or Charisma is your spellcasting ability for this spell when you cast it with this trait (choose when you select this race).")
        if plLvl >= 5:
            RaceNotes.append("Fairy Magic(3) (see notes)")
            Notes.append("Fairy Magic(3): You can also cast the Enlarge/Reduce spell with this trait. Once you cast Enlarge/Reduce with this trait, you can't cast that spell with it again until you finish a long rest. You can also cast this spell using any spell slots you have of the appropriate level. Intelligence, Wisdom, or Charisma is your spellcasting ability for this spell when you cast it with this trait (choose when you select this race).")
    if race == "Firbolg":
        Hmo1 = d12()
        Hmo2 = d12()
        Hmod = Hmo1 + Hmo2
        Hbase = 74
        Wmo1 = d6()
        Wmo2 = d6()
        Wmod = Wmo1 + Wmo2
        Wbase = 175
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Elvi)
        PlLang.append(Gian)
        SLANG.remove(Elvi)
        SLANG.remove(Gian)
        Strength += 1
        Wisdom += 2
        walkingspeed = 30
        CreatureType = "Fey"
        RaceNotes.append("Firbolg Magic (see notes)")
        Notes.append("Firbolg Magic: You can cast Detect Magic and Disguise Self with this trait, using Wisdom as your spellcasting ability for them. Once you cast either spell, you can't cast it again with this trait until you finish a short or long rest. When you use this version of Disguise Self, you can seem up to 3 feet shorter than normal, allowing you to more easily blend in with humans and elves.")
        RaceNotes.append("Hidden Step (see notes)")
        Notes.append("Hidden Step: As a bonus action, you can magically turn invisible until the start of your next turn or until you attack, make a damage roll, or force someone to make a saving throw. Once you use this trait, you can't use it again until you finish a short or long rest.")
        RaceNotes.append("Powerful Build: You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.")
        RaceNotes.append("Speech of Beast and Leaf (see notes)")
        Notes.append("Speech of Beast and Leaf: You have the ability to communicate in a limited manner with beasts and plants. They can understand the meaning of your words, though you have no special ability to understand them in return. You have advantage on all Charisma checks you make to influence them.")
    if race == "Gallus":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmo3 = d10()
        Hmod = Hmo1 + Hmo2 + Hmo3
        Hbase = 40
        Wmo1 = d4()
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 55
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Bird)
        PlLang.append(UAur)
        Wisdom += 2
        walkingspeed = 30
        CreatureType = "Avian Humanoid"
        RaceNotes.append("Glide (see notes)")
        Notes.append("Glide: Using your feathered arms, you can slow your fall, and glide short distances. When falling you can use your reaction to spread your arms, stiffen your wing feathers, and slow your descent. While doing so, you continue to fall gently at a speed of 60 feet per round, taking no fall damage when you land. If you would fall at least 10 feet in this way, you may fly up to your movement speed in one direction you choose, although you cannot choose to move upwards, landing in the space you finish your movement. You cannot glide while carrying heavy weapons or wielding a shield (though you may drop any held items as part of your reaction to spread your arms). You cannot glide while wearing heavy armor, or if you are encumbered.")
        RaceNotes.append("Wing Flap (see notes)")
        Notes.append("Wing Flap: As a bonus action, you can use your powerful feathered arms to propel yourself upward a distance equal to half your movement speed. You can use it in conjunction with a regular jump, but not while gliding.")
        RaceNotes.append("Communal (see notes)")
        Notes.append(f"Communal: Whenever you make an Intelligence (History) check related to the history of your race, culture, or community, you are considered proficient in the History skill and add double your proficiency bonus to the check, or {2*ProfBonus}, instead of your normal proficiency bonus.")
        PlProf.extend(SimpleWeapons)
        PlProf = threetoolprof(param, PlProf, BrewSupp, CarpTools, SmthTools)
        if subrace == "Bright Gallus":
            Charisma += 1
            RaceNotes.append("Inspiring (see notes)")
            Notes.append("Inspiring: By spending an action and giving words of advice or encouragement, you can inspire an ally who is able to see and hear you. The ally can roll a d4 and add the number rolled to their next ability check, attack roll, or saving throw.")
            PlProf.append(Insight)
        if subrace == "Huden Gallus":
            Dexterity += 1
            RaceNotes.append("Seedspeech (see notes)")
            Notes.append("Seedspeech: Your connection to the Great Rhythm is such that you can speak with the greenery of the forest itself. Through speech and touch you can communicate simple ideas to living plants. You are able to interpret their responses in simple language. Plants in the Wood do not experience the world in terms of sight, but most can feel differences in temperature, describe things that have touched them, as well as hear vibrations that happened around them (including speech).")
            PlProf.append(Nature)
    if race == "Genasi":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Prim)
        SLANG.remove(Prim)
        CreatureType = "Humanoid"
        Constitution += 2
        walkingspeed = 30
        if subrace == "Air Genasi":
            Dexterity += 1
            RaceNotes.append("Unending Breath: You can hold your breath indefinitely while you're not incapacitated.")
            RaceNotes.append("Mingle with the Wind (see notes)")
            Notes.append("Mingle with the Wind: You can cast the Levitate spell once with this trait, requiring no material components, and you regain the ability to cast it this way when you finish a long rest. Constitution is your spellcasting ability for this spell.")
        if subrace == "Earth Genasi":
            Strength += 1
            RaceNotes.append("Earth Walk: You can move across difficult terrain made of earth or stone without expending extra movement.")
            RaceNotes.append("Merge With Stone (see notes)")
            Notes.append("Merge With Stone: You can cast the Pass Without Trace spell once with this trait, requiring no material components, and you regain the ability to cast it this way when you finish a long rest. Constitution is your spellcasting ability for this spell.")
        if subrace == "Fire Genasi":
            Intelligence += 1
            RaceNotes.append("Darkvision (see notes)")
            Notes.append(Darkvision)
            DamageResistance = "Fire Damage"
            RaceNotes.append(f"Damage Resistance: {DamageResistance}")
            RaceNotes.append("Reach to the Blaze(1) (see notes). More options are available at higher levels.")
            Notes.append("Reach to the Blaze(1): You know the Produce Flame cantrip. Constitution is your spellcasting ability for this spell.")
            if plLvl >= 3:
                RaceNotes.append("Reach to the Blaze(2) (see notes)")
                Notes.append("Reach to the Blaze(2): You can cast the Burning Hands spell once with this trait as a 1st-level spell, and you regain the ability to cast it this way when you finish a long rest. Constitution is your spellcasting ability for this spell.")
        if subrace == "Water Genasi":
            Wisdom += 1
            DamageResistance = "Acid Damage"
            RaceNotes.append(f"Damage Resistance: {DamageResistance}")
            RaceNotes.append("Amphibious: You can breathe air and water.")
            RaceNotes.append("Swim: You have a swimming speed of 30 feet.")
            RaceNotes.append("Call to the Wave(1) (see notes). More options are available at higher levels.")
            Notes.append("Call to the Wave(1): You know the Shape Water cantrip. Constitution is your spellcasting ability for is spell.")
            if plLvl >= 3:
                RaceNotes.append("Call to the Wave(2) (see notes)")
                Notes.append("Call to the Wave(2): You can cast the Create or Destroy Water spell once with this trait as a 2nd-level spell, and you regain the ability to cast it this way when you finish a long rest. Constitution is your spellcasting ability for is spell.")
    if race == "Giff":
        Hmo1 = d12()
        Hmo2 = d12()
        Hmod = Hmo1 + Hmo2
        Hbase = 74
        Wmo1 = d6()
        Wmo2 = d6()
        Wmod = Wmo1 + Wmo2
        Wbase = 175
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = abilityscores(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
        CreatureType = "Humanoid"
        walkingspeed = 30
        RaceNotes.append("Swim: Your swimming speed is the same as your walking speed")
        RaceNotes.append("Astral Spark (see notes)")
        Notes.append(f"Astral Spark: Your psychic connection to the Astral Plane enables you to mystically access a spark of divine power, which you can channel through your weapons. When you hit a target with a simple or martial weapon, you can cause the target to take an extra {ProfBonus} force damage.\nYou can use this trait {ProfBonus} times, but you can use it no more than once per turn. You regain all expended uses when you finish a long rest.")
        PlProf.extend(Firearms)
        RaceNotes.append("Firearms Mastery - You have a mystical connection to firearms that traces back to the gods of the giff, who delighted in such weapons. You have proficiency with all firearms (already in proficiencies) and ignore the loading property of any firearm. In addition, attacking at long range with a firearm doesn't impose disadvantage on your attack roll.")
        RaceNotes.append("Hippo Build (see notes)")
        Notes.append("Hippo Build: You have advantage on Strength-based ability checks and Strength saving throws. In addition, you count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.")
    if race == "Gith":
        walkingspeed = 30
        CreatureType = "Humanoid"
        Intelligence += 1
        if subrace == "Githyanki":
            Hmo1 = d12()
            Hmo2 = d12()
            Hmod = Hmo1 + Hmo2
            Hbase = 60
            Wmo1 = d4()
            Wmo2 = d4()
            Wmod = Wmo1 + Wmo2
            Wbase = 100
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            Height = str(tl)
            Weight = str(hy)
            PlLang.append(Comm)
            PlLang.append(GithL)
            SLANG.remove(GithL)
            Strength += 2
            PlLang, SLANG = languagegen(param, PlLang, SLANG)
            PlProf = toolskillprof(param, PlProf)
            RaceNotes.append("Githyanki Psionics(1) (see notes). More options are available at higher levels.")
            Notes.append("Githyanki Psionics(1): You know the Mage Hand cantrip, and the hand is invisible when you cast the cantrip with this trait.\nIntelligence is your spellcasting ability for this spell. When you cast it with this trait, it doesn't require components.")
            if plLvl >= 3:
                RaceNotes.append("Githyanki Psionics(2) (see notes)")
                Notes.append("Githyanki Psionics(2): You can cast Jump once with this trait, and you regain the ability to do so when you finish a long rest.\nIntelligence is your spellcasting ability for this spell. When you cast it with this trait, it doesn't require components.")
            if plLvl >= 5:
                RaceNotes.append("Githyanki Psionics(3) (see notes)")
                Notes.append("Githyanki Psionics(3): You can cast the Misty Step spell once with this trait, and you regain the ability to do so when you finish a long rest.\nIntelligence is your spellcasting ability for this spell. When you cast it with this trait, it doesn't require components.")
            PlProf.extend(LightArmor)
            PlProf.extend(MediumArmor)
            PlProf.append(Shortsword)
            PlProf.append(Longsword)
            PlProf.append(Greatsword)
        if subrace == "Githzerai":
            Hmo1 = d12()
            Hmo2 = d12()
            Hmod = Hmo1 + Hmo2
            Hbase = 59
            Wmo1 = d4()
            Wmo2 = 0
            Wmod = Wmo1 + Wmo2
            Wbase = 90
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            Height = str(tl)
            Weight = str(hy)
            PlLang.append(Comm)
            PlLang.append(GithL)
            SLANG.remove(GithL)
            Wisdom += 2
            RaceNotes.append("Mental Discipline (see notes)")
            Notes.append("Mental Discipline: You have advantage on saving throws against the charmed and frightened conditions. Under the tutelage of monastic masters, githzerai learn to govern their own minds.")
            RaceNotes.append("Githzerai Psionics(1) (see notes). More options available at higher levels.")
            Notes.append("Githzerai Psionics(1): You know the Mage Hand cantrip, and the hand is invisible when you cast the cantrip with this trait.\nWisdom is your spellcasting ability for this spell. When you cast it with this trait, it doesn't require components.")
            if plLvl >= 3:
                RaceNotes.append("Githzerai Psionics(2) (see notes)")
                Notes.append("Githzerai Psionics(2): You can cast Shield once with this trait, and you regain the ability to do so when you finish a long rest.\nWisdom is your spellcasting ability for this spell. When you cast it with this trait, it doesn't require components.")
            if plLvl >= 5:
                RaceNotes.append("Githzerai Psionics(3) (see notes)")
                Notes.append("Githzerai Psionics(3): You can cast the Detect Thoughts spell once with this trait, and you regain the ability to do so when you finish a long rest.\nWisdom is your spellcasting ability for this spell. When you cast it with this trait, it doesn't require components.")
    if race == "Gnome":
        Hmo1 = d4()
        Hmo2 = d4()
        Hmod = Hmo1 + Hmo2
        Hbase = 31
        Wmo1 = 1
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 35
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Gnom)
        SLANG.remove(Gnom)
        CreatureType = "Humanoid"
        Intelligence += 2
        walkingspeed = 25
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("Proficent in Intelligence(Saving Throw) against magic")
        RaceNotes.append("Proficent in Wisdom(Saving Throw) against magic")
        RaceNotes.append("Proficent in Charisma(Saving Throw) against magic")
        if subrace == "Forest Gnome":
            Dexterity += 1
            RaceNotes.append("Natural Illusionist: You know the Minor Illusion cantrip. Intelligence is your spellcasting modifier for it.")
            RaceNotes.append("Speak with Small Beasts: Through sound and gestures, you may communicate simple ideas with Small or smaller beasts.")
        if subrace == "Rock Gnome":
            Constitution += 1
            RaceNotes.append("Artificer's Lore (see notes)")
            Notes.append(f"Artificer's Lore: Whenever you make an Intelligence (History) check related to magic items, alchemical objects, or technological devices, you can add twice your proficiency bonus, or {2*ProfBonus}, instead of any proficiency bonus you normally apply.")
            RaceNotes.append("Tinker (see notes)")
            Notes.append("Tinker - You have proficiency with artisan’s tools (tinker’s tools). Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it; at that time, you can reclaim the materials used to create it. You can have up to three such devices active at a time.\nWhen you create a device, choose one of the following options:\nClockwork Toy. This toy is a clockwork animal, monster, or person, such as a frog, mouse, bird, dragon, or soldier. When placed on the ground, the toy moves 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents.\nFire Starter. The device produces a miniature flame, which you can use to light a candle, torch, or campfire. Using the device requires your action.\nMusic Box - When opened, this music box plays a single song at a moderate volume. The box stops playing when it reaches the song’s end or when it is closed.")
        if subrace == "Svirfneblin (Deep) Gnome":
            SLANG.remove(Unde)
            PlLang.append(Unde)
            Dexterity += 1
            RaceNotes.append("Superior Darkvision: Your darkvision has a radius of 120 feet.")
            RaceNotes.append("Stone Camouflage: You have advantage on Dexterity (stealth) checks to hide in rocky terrain.")
    if race == "Goblin":
        Hmo1 = d4()
        Hmo2 = d4()
        Hmod = Hmo1 + Hmo2
        Hbase = 41
        Wmo1 = 1
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 35
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Gobl)
        SLANG.remove(Gobl)
        CreatureType = "Goblinoid"
        Dexterity += 2
        Constitution += 1
        walkingspeed = 30
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("Fury of the Small (see notes)")
        Notes.append(f"Fury of the Small: When you damage a creature with an attack or a spell and the creature's size is larger than yours, you can cause the attack or spell to deal extra damage to the creature. The extra damage equals your player level, {plLvl}. Once you use this trait, you can't use it again until you finish a short or long rest.")
        RaceNotes.append("Nimble Escape: You can take the Disengage or Hide action as a bonus action on each of your turns.")
    if race == "Goliath":
        Hmo1 = d6()
        Hmo2 = d6()
        Hmod = Hmo1 + Hmo2
        Hbase = 84
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 140
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Gian)
        SLANG.remove(Gian)
        CreatureType = "Humanoid"
        Strength += 2
        Constitution += 1
        walkingspeed = 30
        PlProf.append(Athletics)
        RaceNotes.append("Stone's Endurance (see notes)")
        Notes.append("Stone's Endurance: You can focus yourself to occasionally shrug off injury. When you take damage, you can use your reaction to roll a d12. Add your Constitution modifier to the number rolled, and reduce the damage by that total. After you use this trait, you can't use it again until you finish a short or long rest.")
        RaceNotes.append("Powerful Build: You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.")
        RaceNotes.append("Mountain Born (see notes)")
        Notes.append("Mountain Born: You're acclimated to high altitude, including elevations above 20,000 feet. You're also naturally adapted to cold climates, as described in chapter 5 of the Dungeon Master's Guide.")
    if race == "Grung":
        Hmo1 = d6()
        Hmo2 = d6()
        Hmod = Hmo1 + Hmo2
        Hbase = 30
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 30
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Grun)
        SLANG.remove(Grun)
        Dexterity += 2
        Constitution += 1
        PlProf.append(Perception)
        walkingspeed = 25
        CreatureType = "Humanoid"
        RaceNotes.append("Your climbing speed is equal to your walking speed.")
        RaceNotes.append("Amphibious: You can breathe air and water.")
        RaceNotes.append("Poison Immunity: You’re immune to poison damage and the poisoned condition.")
        RaceNotes.append("Poisonous Skin (see notes)")
        Notes.append("Poisonous Skin: Any creature that grapples you or otherwise comes into direct contact with your skin must succeed on a DC 12 Constitution saving throw or become poisoned for 1 minute. A poisoned creature no longer in direct contact with you can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.\nYou can also apply this poison to any piercing weapon as part of an attack with that weapon, though when you hit the poison reacts differently. The target must succeed on a DC 12 Constitution saving throw or take 2d4 poison damage.")
        RaceNotes.append("Standing Leap: Your long jump is up to 25 feet and your high jump is up to 15 feet, with or without a running start.")
        RaceNotes.append("Water Dependency (see notes)")
        Notes.append("Water Dependency: If you fail to immerse yourself in water for at least 1 hour during a day, you suffer one level of exhaustion at the end of that day. You can only recover from this exhaustion through magic or by immersing yourself in water for at least 1 hour.")
    if race == "Hadozee":
        Hmo1 = d8()
        Hmo2 = d8()
        Hmod = Hmo1 + Hmo2
        Hbase = 57
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = abilityscores(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
        CreatureType = "Humanoid"
        walkingspeed = 30
        RaceNotes.append("Your Climbing speed is the same as your walking speed")
        RaceNotes.append("Dexterous Feet: As a bonus action, you can use your feet to manipulate an object, open or close a door or container, or pick up or set down a Tiny object.")
        RaceNotes.append("Glide (see notes)")
        Notes.append("Glide: If you are not incapacitated or wearing heavy armor, you can extend your skin membranes and glide. When you do so, you can perform the following aerial maneuvers:\nYou can move up to 5 feet horizontally for every 1 foot you descend in the air, at no movement cost to you.\nWhen you would take damage from a fall, you can use your reaction to reduce the fall's damage to 0.")
        RaceNotes.append("Hadozee Resilience (see notes)")
        Notes.append(f"Hadozee Resilience: The magic that runs in your veins heightens your natural defenses. When you take damage, you can use your reaction to roll a d6. Add your proficiency bonus to the number rolled, ({ProfBonus}), and reduce the damage you take by an amount equal to that total (minimum of 0 damage).\nYou can use this trait {ProfBonus} times. You regain all expended uses when you finish a long rest.")
    if race == "HalfElf":
        Hmo1 = d8()
        Hmo2 = d8()
        Hmod = Hmo1 + Hmo2
        Hbase = 57
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        SLANG.remove(Elvi)
        PlLang.append(Comm)
        PlLang.append(Elvi)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        Charisma += 2
        Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = singleabilityscore(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
        Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = singleabilityscore(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
        walkingspeed = 30
        CreatureType = "Humanoid"
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("Fey Ancestry: You have advantage on saving throws against being charmed, and magic can’t put you to sleep.")
        PlProf = skillprof2(param, PlProf)
        if subrace == "Half-Elf: Aquatic Elf Descent":
            RaceNotes.append("Swim: You gain a swimming speed of 30 ft.")
        if subrace == "Half-Elf: Drow Descent":
            RaceNotes.append("Drow Magic(1) (see notes). More options are available at higher levels.")
            Notes.append("Drow Magic(1): You know the Dancing Lights cantrip. More options are available at higher levels.")
            if plLvl >= 3:
                RaceNotes.append("Drow Magic(2) (see notes)")
                Notes.append("Drow Magic(2): You can cast the Faerie Fire spell once per day; you must finish a long rest in order to cast the spell again using this trait. Charisma is your spellcasting ability for this spell.")
            if plLvl >= 5:
                RaceNotes.append("Drow Magic(3) (see notes)")
                Notes.append("Drow Magic(3): You can also cast the Darkness spell once per day; you must finish a long rest in order to cast the spell again using this trait. Charisma is your spellcasting ability for this spell.")
        if (subrace == "Half-Elf: Moon Elf Descent") or (subrace == "Half-Elf: Sun Elf Descent"):
            VariantFeatures = ["Proficiencies", "Cantrip"]
            VariantFeatureRand = random.choice(VariantFeatures)
            if param == "Y":
                print("0 - Random")
                print("1 - Longsword, Shortsword, Shortbow, and Longbow Proficiency")
                print("2 - Wizard Cantrip")
                varfeat = int(input("Which variant feature would you prefer? "))
                if varfeat == 1:
                    PlProf.append(Longsword)
                    PlProf.append(Shortsword)
                    PlProf.append(Shortbow)
                    PlProf.append(Longbow)
                if varfeat == 2:
                    RaceNotes.append("Wizard Cantrip (see notes)")
                    Notes.append("Wizard Cantrip: You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it.")
                if varfeat == 0:
                    if VariantFeatureRand == "Proficiencies":
                        PlProf.append(Longsword)
                        PlProf.append(Shortsword)
                        PlProf.append(Shortbow)
                        PlProf.append(Longbow)
                    if VariantFeatureRand == "Cantrip":
                        RaceNotes.append("Wizard Cantrip")
                        Notes.append("Wizard Cantrip: You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it.")
            if param == "N":
                if VariantFeatureRand == "Proficiencies":
                    PlProf.append(Longsword)
                    PlProf.append(Shortsword)
                    PlProf.append(Shortbow)
                    PlProf.append(Longbow)
                if VariantFeatureRand == "Cantrip":
                    RaceNotes.append("Wizard Cantrip (see notes)")
                    Notes.append("Wizard Cantrip: You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it.")               
        if subrace == "Half-Elf: Wood Elf Descent":
            VariantFeatures = ["Proficiencies", "Fleet of Foot", "Mask of the Wild"]
            VariantFeatureRand = random.choice(VariantFeatures)
            if param == "Y":
                print("0 - Random")
                print("1 - Longsword, Shortsword, Shortbow, and Longbow Proficiency")
                print("2 - Fleet of Foot: WalkSpeed = 35 ft")
                print("3 - Mask of the Wild: You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.")
                varfeat = int(input("Which variant feature would you prefer? "))
                if varfeat == 1:
                    PlProf.append(Longsword)
                    PlProf.append(Shortsword)
                    PlProf.append(Shortbow)
                    PlProf.append(Longbow)
                if varfeat == 2:
                    walkingspeed = 35
                if varfeat == 3:
                    RaceNotes.append("Mask of the Wild (see notes)")
                    Notes.append("Mask of the Wild: You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.")
                if varfeat == 0:
                    if VariantFeatureRand == "Proficiencies":
                        PlProf.append(Longsword)
                        PlProf.append(Shortsword)
                        PlProf.append(Shortbow)
                        PlProf.append(Longbow)
                    if VariantFeatureRand == "Fleet of Foot":
                        walkingspeed = 35  
                    if VariantFeatureRand == "Mask of the Wild":  
                        RaceNotes.append("Mask of the Wild (see notes)")
                        Notes.append("Mask of the Wild: You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.")
            if param == "N":
                if VariantFeatureRand == "Proficiencies":
                    PlProf.append(Longsword)
                    PlProf.append(Shortsword)
                    PlProf.append(Shortbow)
                    PlProf.append(Longbow)
                if VariantFeatureRand == "Fleet of Foot":
                    walkingspeed = 35  
                if VariantFeatureRand == "Mask of the Wild":  
                    RaceNotes.append("Mask of the Wild (see notes)")
                    Notes.append("Mask of the Wild: You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.")       
    if race == "Halfling":
        Hmo1 = d6()
        Hmo2 = d6()
        Hmod = Hmo1 + Hmo2
        Hbase = 28
        Wmo1 = 1
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 35
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Hafl)
        SLANG.remove(Hafl)
        Dexterity += 2
        walkingspeed = 25
        CreatureType = "Humanoid"
        RaceNotes.append("Lucky: When you roll a 1 on the d20 for an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll.")
        RaceNotes.append("Brave: You have advantage on saving throws against being frightened.")
        RaceNotes.append("Halfling Nimbleness: You can move through the space of any creature that is of a size larger than yours.")
        if subrace == "Ghostwise Halfling":
            Wisdom += 1
            RaceNotes.append("Silent Speech (see notes)")
            Notes.append("Silent Speech: You can speak telepathically to any creature within 30 feet of you. The creature understands you only if the two of you share a language. You can speak telepathically in this way to one creature at a time.")
        if subrace == "Lightfoot Halfling":
            Charisma += 1
            RaceNotes.append("Naturally Stealthy: You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you.")
        if subrace == "Stout Halfling":
            Constitution += 1
            RaceNotes.append("Stout Resilience: You have advantage on saving throws against poison, and you have resistance against poison damage.")
    if race == "Half-Orc":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 58
        Wmo1 = d6()
        Wmo2 = d6()
        Wmod = Wmo1 + Wmo2
        Wbase = 140
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Orc)
        SLANG.remove(Orc)
        Strength += 2
        Constitution += 1
        walkingspeed = 30
        CreatureType = "Humanoid"
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        PlProf.append(Intimidation)
        RaceNotes.append("Relentless Endurance (see notes)")
        Notes.append("Relentless Endurance: When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can’t use this feature again until you finish a long rest.")
        RaceNotes.append("Savage Attacks (see notes)")
        Notes.append("Savage Attacks: When you score a critical hit with a melee weapon attack, you can roll one of the weapon’s damage dice one additional time and add it to the extra damage of the critical hit.")
    if race == "Harengon":
        Hmo1 = d12()
        Hmo2 = d12()
        Hmo3 = d12()
        Hmo4 = d12()
        Hmod = Hmo1 + Hmo2 + Hmo3 + Hmo4
        Hbase = 42
        Wmo1 = d6()
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 25
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = abilityscores(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
        CreatureType = "Humanoid"
        walkingspeed = 30
        RaceNotes.append(f"Hare-Trigger: You can add your proficiency bonus, {ProfBonus}, to your initiative rolls.")
        PlProf.append(Perception)
        RaceNotes.append("Lucky Footwork (see notes)")
        Notes.append("Lucky Footwork: When you fail a Dexterity saving throw, you can use your reaction to roll a d4 and add it to the save, potentially turning the failure into a success. You can't use this reaction if you're prone or your speed is 0.")
        RaceNotes.append("Rabbit Hop (see notes)")
        Notes.append(f"Rabbit Hop: As a bonus action, you can jump a number of feet equal to five times your proficiency bonus, or {5*ProfBonus} feet, without provoking opportunity attacks. You can use this trait only if your speed is greater than 0. You can use it {ProfBonus} times, and you regain all expended uses when you finish a long rest.")
    if race == "Hedge":
        Hmo1 = d6()
        Hmo2 = d6()
        Hmod = Hmo1 + Hmo2
        Hbase = 35
        Wmo1 = d4()
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 30
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Bird)
        PlLang.append(Hedg)
        SLANG.remove(Hedg)
        Charisma += 2
        Wisdom += 1
        walkingspeed = 25
        CreatureType = "Humanoid"
        RaceNotes.append("Natural Burrowers (see notes)")
        Notes.append("Natural Burrowers: You have a burrowing speed of 15 feet. You are capable of burrowing through soil, but are unable to dig through anything more substantial with just your clawed hands.")
        RaceNotes.append("Spiny Quills (see notes)")
        Notes.append("Spiny Quills: The backs of hedges are covered with spiny quills, which makes it impossible for hedges to wear armor. These quills provide exceptional protection, therefore you have a base armor class of 14 + your Dexterity modifier. Even though you can’t wear armor, you can still benefit from the armor class bonus provided by shields so long as you are proficient with them.")
        RaceNotes.append("Curl Up (see notes)")
        Notes.append("Curl Up: You can use your action to curl up, exposing attackers to a wall of your toughened quills. While curled up you cannot move, attack, or cast spells with somatic components, and your base armor class becomes 19. You cannot benefit from any Dexterity bonus to armor class while curled up, but you can still use shields.\nAny creature that misses you with a melee attack while you are curled up takes 2d4 points of piercing damage from your sharp quills. If a creature hits you while you are curled up, you are knocked prone in your space at the end of the turn. You may uncurl yourself at any point during your turn.")
        RaceNotes.append("Forest Magic (see notes)")
        Notes.append("Forest Magic: You have a deep connection to the magic of the Wood. You know the Druidcraft cantrip. Additionally, you can cast Animal Messenger as a 2nd level spell once with this trait, and regain the ability to do so after a short or long rest. Charisma is your spellcasting ability for these spells.")
        RaceNotes.append("Speak With Bugs (see notes)")
        Notes.append("Speak With Bugs: Through sounds and gestures, you can communicate simple ideas with creatures of the beast subtype that represent insects, spiders, worms, and other creepy crawlies, regardless of their size.")
    if race == "Hexblood":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = abilityscores(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
        CreatureType = "Fey"
        walkingspeed = 30
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("Eerie Token (see notes)")
        RaceNotes.append("Eerie Token: As a bonus action, you can harmlessly remove a lock of your hair, one of your nails, or one of your teeth. This token is imbued with magic until you finish a long rest. While the token is imbued in this way, you can take these actions:\nTelepathic Message - As an action, you can send a telepathic message to the creature holding or carrying the token, as long as you are within 10 miles of it. The message can contain up to twenty-five words.\nRemote Viewing - If you are within 10 miles of the token, you can enter a trance as an action. The trance lasts for 1 minute, but it ends early if you dismiss it (no action required) or are incapacitated. During this trance, you can see and hear from the token as if you were located where it is. While you are using your senses at the token’s location, you are blinded and deafened in regard to your own surroundings. When the trance ends, the token is harmlessly destroyed.\nOnce you create a token using this feature, you can’t do so again until you finish a long rest, at which point your missing part regrows.")
        RaceNotes.append("Hex Magic (see notes)")
        RaceNotes.append("Hex Magic: You can cast the Disguise Self and Hex spells with this trait. Once you cast either of these spells with this trait, you can’t cast that spell with it again until you finish a long rest. You can also cast these spells using any spell slots you have.\nIntelligence, Wisdom, or Charisma is your spellcasting ability for these spells (choose the ability when you gain this lineage).")    
    if race == "Hobgoblin":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Gobl)
        SLANG.remove(Gobl)
        Constitution += 2
        Intelligence += 1
        walkingspeed = 30
        CreatureType = "Goblinoid"
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        PlProf = martwepprof2(param, PlProf)
        PlProf.extend(LightArmor)
        RaceNotes.append("Saving Face (see notes)")
        Notes.append("Saving Face: Hobgoblins are careful not to show weakness in front of their allies, for fear of losing status. If you miss with an attack roll or fail an ability check or a saving throw, you can gain a bonus to the roll equal to the number of allies you can see within 30 feet of you (maximum bonus of +5). Once you use this trait, you can't use it again until you finish a short or long rest.")
    if race == "Human":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        walkingspeed = 30
        CreatureType = "Humanoid"
        if subrace == "Human":
            Charisma += 1
            Constitution += 1
            Dexterity += 1
            Intelligence += 1
            Strength += 1
            Wisdom += 1        
        if subrace == "Variant Human":
            Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = singleabilityscore(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
            Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = singleabilityscore(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
            PlProf = skillprof(param, PlProf)
            RaceNotes.append("Feat: You gain one feat of your choice.")  
    if race == "Jerbeen":
        Hmo1 = d4()
        Hmo2 = d4()
        Hmod = Hmo1 + Hmo2
        Hbase = 28
        Wmo1 = d2()
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 20
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Bird)
        PlLang.append(Jerb)
        SLANG.remove(Jerb)
        Dexterity += 2
        Charisma += 1
        walkingspeed = 30
        CreatureType = "Humanoid"
        RaceNotes.append("Standing Leap: Your base long jump is 30 feet, and your base high jump is 15 feet, with or without a running start.")
        RaceNotes.append("Nimbleness: You can move through the space of any creature that is of a size larger than yours.")
        RaceNotes.append("Take Heart (see notes)")
        Notes.append("Take Heart: You have advantage on Strength saving throws and saving throws against being frightened as long as you are within 5 feet of an ally who isn’t frightened or incapacitated that you can both see and hear.")
        RaceNotes.append("Team Tactics: You can use the Help action as a bonus action.")
    if race == "Kalashtar":
        Hmo1 = d6()
        Hmo2 = d6()
        Hmod = Hmo1 + Hmo2
        Hbase = 64
        Wmo1 = d6()
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        SLANG.remove(Quo)
        PlLang.append(Comm)
        PlLang.append(Quo)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        CreatureType = "Humanoid"
        Wisdom += 2
        Charisma += 1
        walkingspeed = 30
        DamageResistance = "Psychic Damage"
        RaceNotes.append(f"Damage Resistance: {DamageResistance}")
        RaceNotes.append("Dual Mind: You have advantage on all Wisdom saving throws.")
        RaceNotes.append("Mind Link (see notes)")
        Notes.append("Mind Link: You can speak telepathically to any creature you can see, provided the creature is within a number of feet of you equal to 10 times your level. You don't need to share a language with the creature for it to understand your telepathic utterances, but the creature must be able to understand at least one language.\nWhen you're using this trait to speak telepathically to a creature, you can use your action to give that creature the ability to speak telepathically with you for 1 hour or until you end this effect as an action. To use this ability, the creature must be able to see you and must be within this trait's range. You can give this ability to only one creature at a time; giving it to a creature takes it away from another creature who has it.")
        RaceNotes.append("Severed from Dreams (see notes)")
        Notes.append("Severed from Dreams: Kalashtar sleep, but they don't connect to the plane of dreams as other creatures do. Instead, their minds draw from the memories of their otherworldly spirit while they sleep. As such, you are immune to spells and other magical effects that require you to dream, like Dream, but not to spells and other magical effects that put you to sleep, like Sleep.")
    if race == "Kender":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = abilityscores(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
        CreatureType = "Humanoid"
        walkingspeed = 30
        PlProf = fiveskillprof(param, PlProf, Insight, Investigation, SleightofHand, Stealth, Survival)
        RaceNotes.append("Fearless (see notes)")
        Notes.append("Fearless: You have advantage on saving throws you make to avoid or end the frightened condition on yourself. When you fail a saving throw to avoid or end the frightened condition on yourself, you can choose to succeed instead. Once you succeed on a saving throw in this way, you can't do so again until you finish a long rest.")
        RaceNotes.append("Taunt (see notes)")
        Notes.append("Taunt: You have an extraordinary ability to fluster creatures. As a bonus action, you can unleash a string of provoking words at a creature within 60 feet of yourself that can hear and understand you. The target must succeed on a Wisdom saving throw, or it has disadvantage on attack rolls against targets other than you until the start of your next turn. The DC equals 8 + your proficiency bonus + your Intelligence, Wisdom, or Charisma modifier (choose when you select this race).\nYou can use this bonus action a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.")
    if race == "Kenku":
        Hmo1 = d8()
        Hmo2 = d8()
        Hmod = Hmo1 + Hmo2
        Hbase = 52
        Wmo1 = d6()
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 50
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Aura)
        SLANG.remove(Aura)
        Dexterity += 2
        Wisdom += 1
        walkingspeed = 30
        CreatureType = "Avian Humanoid"
        RaceNotes.append("Expert Forgery (see notes)")
        Notes.append("Expert Forgery: You can duplicate other creatures' handwriting and craftwork. You have advantage on all checks made to produce forgeries or duplicates of existing objects.")
        PlProf = fourskillprof(param, PlProf, Acrobatics, Deception, Stealth, SleightofHand)
        PlProf = fourskillprof(param, PlProf, Acrobatics, Deception, Stealth, SleightofHand)
        RaceNotes.append("Mimicry (see notes)")
        Notes.append("Mimicry: You can mimic sounds you have heard, including voices. A creature that hears the sounds can tell they are imitations with a successful Insight check opposed by your Deception check.")
        PlLang.append("In addition to the languages you know, you can only speak using your Mimicry trait.")
    if race == "Kobold":
        Hmo1 = d4()
        Hmo2 = d4()
        Hmod = Hmo1 + Hmo2
        Hbase = 25
        Wmo1 = 1
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 25
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Drac)
        SLANG.remove(Drac)
        CreatureType = "Humanoid"
        Strength -= 2
        Dexterity += 2
        walkingspeed = 30
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("Grovel, Cower, and Beg (see notes)")
        Notes.append("Grovel, Cower, and Beg: As an action on your turn, you can cower pathetically to distract nearby foes. Until the end of your next turn, your allies gain advantage on attack rolls against enemies within 10 feet of you that you can see. Once you use this trait, you can't use it again until you finish a short or long rest.")
        RaceNotes.append("Pack Tactics: You have advantage on an attack roll against a creature if at least one of your allies is within 5 feet of the creature and the ally isn't incapacitated.")
        RaceNotes.append("Sunlight Sensitivity (see notes)")
        Notes.append("Sunlight Sensitivity: You have disadvantage on attack rolls and on Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight.")
    if race == "Leonin":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 66
        Wmo1 = d6()
        Wmo2 = d6()
        Wmod = Wmo1 + Wmo2
        Wbase = 180
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Leon)
        SLANG.remove(Leon)
        CreatureType = "Humanoid"
        Constitution += 2
        Strength += 1
        walkingspeed = 35
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("Claws (see notes)")
        Notes.append("Claws: Your claws are natural weapons, which you can use to make unarmed strikes. If you hit with them, you can deal slashing damage equal to 1d4 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.")
        PlProf = fourskillprof(param, PlProf, Athletics, Intimidation, Perception, Survival)
        RaceNotes.append("Daunting Roar (see notes)")
        Notes.append("Daunting Roar: As a bonus action, you can let out an especially menacing roar. Creatures of your choice within 10 feet of you that can hear you must succeed on a Wisdom saving throw or become frightened of you until the end of your next turn. The DC of the save equals 8 + your proficiency bonus + your Constitution modifier. Once you use this trait, you can't use it again until you finish a short or long rest.")
    if race == "Lizardfolk":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 57
        Wmo1 = d6()
        Wmo2 = d6()
        Wmod = Wmo1 + Wmo2
        Wbase = 120
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Drac)
        SLANG.remove(Drac)
        CreatureType = "Humanoid"
        Constitution += 2
        Wisdom += 1
        walkingspeed = 30
        RaceNotes.append("Your swim speed is the same as your walking speed.")
        RaceNotes.append("Bite (see notes)")
        Notes.append("Bite: Your fanged maw is a natural weapon, which you can use to make unarmed strikes. If you hit with it, you deal piercing damage equal to 1d6 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.")
        RaceNotes.append("Cunning Artisan (see notes)")
        Notes.append("Cunning Artisan: As part of a short rest, you can harvest bone and hide from a slain beast, construct, dragon, monstrosity, or plant creature of size small or larger to create one of the following items: a shield, a club, a javelin, or 1d4 darts or blowgun needles. To use this trait, you need a blade, such as a dagger, or appropriate artisan's tools, such as leatherworker's tools.")
        RaceNotes.append("Hold Breath: You can hold your breath for up to 15 minutes at a time.")
        PlProf = fiveskillprof(param, PlProf, AnimalHandling, Nature, Perception, Stealth, Survival)
        PlProf = fiveskillprof(param, PlProf, AnimalHandling, Nature, Perception, Stealth, Survival) 
        RaceNotes.append("Natural Armor (see notes)")
        Notes.append("Natural Armor: You have tough, scaly skin. When you aren't wearing armor, your AC is 13 + your Dexterity modifier. You can use your natural armor to determine your AC if the armor you wear would leave you with a lower AC. A shield's benefits apply as normal while you use your natural armor.")
        RaceNotes.append("Hungry Jaws (see notes)")
        Notes.append("Hungry Jaws: In battle, you can throw yourself into a vicious feeding frenzy. As a bonus action, you can make a special attack with your bite. If the attack hits, it deals its normal damage, and you gain temporary hit points equal to your Constitution modifier (minimum of 1), and you can't use this trait again until you finish a short or long rest.")
    if race == "Locathah":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Aqua)
        SLANG.remove(Aqua)
        CreatureType = "Humanoid"
        Strength += 2
        Dexterity += 1
        RaceNotes.append("Natural Armor (see notes)")
        Notes.append("Natural Armor: You have tough, scaly skin. When you aren’t wearing armor, your AC is 12 + your Dexterity modifier. You can use your natural armor to determine your AC if the armor you wear would leave you with a lower AC. A shield’s benefits apply as normal while you use your natural armor.")
        PlProf.append(Athletics)
        PlProf.append(Perception)
        RaceNotes.append("Leviathan Will: You have advantage on saving throws against being charmed, frightened, paralyzed, poisoned, stunned, or put to sleep.")
        RaceNotes.append("Limited Amphibiousness: You can breathe air and water, but you need to be submerged at least once every 4 hours to avoid suffocating.")
        walkingspeed = 30
        RaceNotes.append("Your swim speed is the same as your walking speed.")
    if race == "Loxodon":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 79
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 295
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Loxo)
        SLANG.remove(Loxo)
        CreatureType = "Humanoid"
        Constitution += 2
        Wisdom += 1
        walkingspeed = 30
        RaceNotes.append("Powerful Build: You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.")
        RaceNotes.append("Loxodon Serenity: You have advantage on saving throws against being charmed or frightened.")
        RaceNotes.append("Natural Armor (see notes)")
        Notes.append("Natural Armor: You have thick, leathery skin. When you aren't wearing armor, your AC is 12 + your Constitution modifier. You can use your natural armor to determine your AC if the armor you wear would leave you with a lower AC. A shield's benefits apply as normal while you use your natural armor.")
        RaceNotes.append("Trunk (see notes)")
        Notes.append("Trunk: You can grasp things with your trunk, and you can use it as a snorkel. It has a reach of 5 feet, and it can lift a number of pounds equal to five times your Strength score. You can use it to do the following simple tasks: lift, drop, hold, push, or pull an object or a creature; open or close a door or a container; grapple someone; or make an unarmed strike. Your DM might allow other simple tasks to be added to that list of options.\nYour trunk can't wield weapons or shields or do anything that requires manual precision, such as using tools or magic items or performing the somatic components of a spell.")
        RaceNotes.append("Keen Smell: Thanks to your sensitive trunk, you have advantage on Perception, Survival, and Investigation checks that involve smell.")
    if race == "Luma":
        Hmo1 = d4()
        Hmo2 = d4()
        Hmod = Hmo1 + Hmo2
        Hbase = 32
        Wmo1 = 1
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 25
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Bird)
        PlLang.append(UAur)
        CreatureType = "Avian Humanoid"
        Charisma += 2
        walkingspeed = 25
        RaceNotes.append("Glide (see notes)")
        Notes.append("Glide: Using your feathered arms, you can slow your fall, and glide short distances. When falling you can use your reaction to spread your arms, stiffen your wing feathers, and slow your descent. While doing so, you continue to fall gently at a speed of 60 feet per round, taking no fall damage when you land. If you would fall at least 10 feet in this way, you may fly up to your movement speed in one direction you choose, although you cannot choose to move upwards, landing in the space you finish your movement. You cannot glide while carrying heavy weapons or wielding a shield (though you may drop any held items as part of your reaction to spread your arms). You cannot glide while wearing heavy armor, or if you are encumbered.")
        RaceNotes.append("Wing Flap (see notes)")
        Notes.append("Wing Flap: As a bonus action, you can use your powerful feathered arms to propel yourself upward a distance equal to half your movement speed. You can use it in conjunction with a regular jump, but not while gliding.")
        RaceNotes.append("Touched/Sorcerer Cantrip (see notes)")
        Notes.append("Touched: You know one cantrip from the sorcerer spell list. Charisma is your spellcasting ability for this cantrip.")
        RaceNotes.append("Fated (see notes)")
        Notes.append("Fated: Whether by luck or a guiding presence, you always seem to find your way. You can choose to reroll any attack, skill check, or saving throw. You can decide to do this after your roll, but only before the outcome of the roll has been determined. You can’t use this feature again until you have completed a long rest.")
        if subrace == "Sable Luma":
            Constitution += 1
            RaceNotes.append("Hard to Read (see notes)")
            Notes.append("Hard to Read: Your innate eccentricities make it hard for other folk to figure you out. When someone performs a Wisdom (Insight) check against you, they have disadvantage on their roll. Additionally, you gain advantage on Charisma (Deception) checks made against creatures that are not lumas.")
            RaceNotes.append("Resilience: You have advantage on saving throws against poison.")
            DamageResistance = "Poison Damage"
            RaceNotes.append(f"Damage Resistance: {DamageResistance}")
        if subrace == "Sera Luma":
            Wisdom += 1
            PlProf.append(Performance)
            RaceNotes.append("Songbird (see notes)")
            Notes.append("Songbird: When you perform, you can demonstrate the innate and mystical power of your Charisma. You may cast the charm person spell once per long rest. This spell does not require any somatic components to cast. Charisma is your spellcasting ability for this spell.")
    if race == "Mapach":
        Hmo1 = d6()
        Hmo2 = d6()
        Hmod = Hmo1 + Hmo2
        Hbase = 47
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 85
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Bird)
        PlLang.append(Mapa)
        SLANG.remove(Mapa)
        Wisdom += 2
        Constitution += 1
        walkingspeed = 30
        CreatureType = "Humanoid"
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("In addition to Darkvision, Mapachs are most comfortable under the cloak of night.")
        RaceNotes.append("Expert Climbers: You have a climb speed of 20 feet.")
        DamageResistance = "Poison Damage"
        RaceNotes.append(f"Damage Resistance: {DamageResistance}")
        RaceNotes.append("Resilience: You have advantage on saving throws against poison.")
        RaceNotes.append("Scroungecraft (see notes)")
        Notes.append("Scroungecraft: You are proficient with tinker’s tools. Additionally, you have the ability to construct crude but functional versions of common items using materials present in your surroundings. You may spend 10 minutes to craft these materials into any tool or piece of adventuring gear worth 30 gold pieces or less. The item will be completely functional, even capable of passing for a disguise (if you crafted an article of clothing). Tools, along with any other item that would logically break on its first use (caltrops, arrows), will become useless afterward. Scroungecrafted items will otherwise last 1 hour before falling apart.\nDepending on the materials available, a Game Master (GM) may rule that you cannot craft an item in this way. For example, a vial of acid might be easy to make if you happen to be near a nest of acidic beetle larvae, or bark can be bound into a makeshift flask, but it would be difficult to create a passable facsimile of silken robes from a pile of leaves.\nShould you have access to the proper materials, you can spend 8 hours converting an item you have scroungecrafted in this way into a permanent version, so long as you start this process before the item falls apart. Items crafted in such a way will function exactly as a normal version of the item, and if you have proficiency in the tools used to craft them, they can even look professionally-crafted. Otherwise, they retain a rather rough, cobbled-together appearance. You can also use scroungecraft to repair broken equipment, provided you have the materials on hand. Though, how long your repairs hold together is up to the GM.")
        RaceNotes.append("Skulker: You have advantage on Stealth checks made in dim light and darkness.")
    if race == "Minotaur":
        Hmo1 = d8()
        Hmo2 = d8()
        Hmod = Hmo1 + Hmo2
        Hbase = 64
        Wmo1 = d6()
        Wmo2 = d6()
        Wmod = Wmo1 + Wmo2
        Wbase = 175
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        SLANG.remove(Mino)
        PlLang.append(Comm)
        PlLang.append(Mino)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        CreatureType = "Humanoid"
        Strength += 2
        Constitution += 1
        walkingspeed = 30
        RaceNotes.append("Horns (see notes)")
        Notes.append("Horns: Your horns are natural melee weapons, which you can use to make unarmed strikes. If you hit with them, you deal piercing damage equal to 1d6 +your Strength modifier. instead of the bludgeoning damage normal for an unarmed strike.")
        RaceNotes.append("Goring Rush: Immediately after you use the Dash action on your turn and move at least 20 feet, you can make one melee attack with your horns as a bonus action.")
        RaceNotes.append("Hammering Horns (see notes)")
        Notes.append("Hammering Horns: Immediately after you hit a creature with a melee attack as part of the Attack action on your turn, you can use a bonus action to attempt to shove that target with your horns. The target must be no more than one size larger than you and within 5 feet of you. Unless it succeeds on a Strength saving throw against a DC equal to 8 + your proficiency bonus+ your Strength modifier, you push it up to 10 feet away from you.")
        PlProf = twoskillprof(param, PlProf, Intimidation, Persuasion)
    if race == "Orc":
        Hmo1 = d8()
        Hmo2 = d8()
        Hmod = Hmo1 + Hmo2
        Hbase = 64
        Wmo1 = d6()
        Wmo2 = d6()
        Wmod = Wmo1 + Wmo2
        Wbase = 175
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Orc)
        SLANG.remove(Orc)
        CreatureType = "Humanoid"
        Strength += 2
        Constitution += 1
        Intelligence -= 2
        walkingspeed = 30
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("Aggressive (see notes)")
        Notes.append("Aggressive: As a bonus action, you can move up to your movement speed toward a hostile creature you can see or hear. You must end this move closer to the enemy than you started.")
        PlProf.append(Intimidation)
        RaceNotes.append("Powerful Build: You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.")
    if race == "Owlin":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        CreatureType = "Humanoid"
        Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = abilityscores(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
        walkingspeed = 30
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("Flight: Thanks to your wings, you have a flying speed equal to your walking speed. You can't use this flying speed if you're wearing medium or heavy armor.")
        PlProf.append(Stealth)
    if race == "Plasmoid":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = abilityscores(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
        CreatureType = "Ooze"
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("Amorphous (see notes)")
        Notes.append("Amorphous: You can squeeze through a space as narrow as 1 inch wide, provided you are wearing and carrying nothing. You have advantage on ability checks you make to initiate or escape a grapple.")
        RaceNotes.append("Hold Breath: You can hold your breath for 1 hour.")
        DamageResistance = "Acid Damage and Poison Damage"
        RaceNotes.append(f"Damage Resistance: {DamageResistance}")
        RaceNotes.append("You have advantage on saving throws against being poisoned.")
        RaceNotes.append("Shape Self (see notes)")
        Notes.append("Shape Self: As an action, you can reshape your body to give yourself a head, one or two arms, one or two legs, and makeshift hands and feet, or you can revert to a limbless blob. While you have a humanlike shape, you can wear clothing and armor made for a Humanoid of your size.\nAs a bonus action, you can extrude a pseudopod that is up to 6 inches wide and 10 feet long or reabsorb it into your body. As part of the same bonus action, you can use this pseudopod to manipulate an object, open or close a door or container, or pick up or set down a Tiny object. The pseudopod contains no sensory organs and can't attack, activate magic items, or lift more than 10 pounds.")
    if race == "Raptor (Bird)":
        Hmo1 = d6()
        Hmo2 = d6()
        Hmod = Hmo1 + Hmo2
        Hbase = 35
        Wmo1 = 1
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 25
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Bird)
        PlLang.append(UAur)
        Dexterity += 2
        walkingspeed = 25
        CreatureType = "Avian Humanoid"
        RaceNotes.append("Glide (see notes)")
        Notes.append("Glide: Using your feathered arms, you can slow your fall, and glide short distances. When falling you can use your reaction to spread your arms, stiffen your wing feathers, and slow your descent. While doing so, you continue to fall gently at a speed of 60 feet per round, taking no fall damage when you land. If you would fall at least 10 feet in this way, you may fly up to your movement speed in one direction you choose, although you cannot choose to move upwards, landing in the space you finish your movement. You cannot glide while carrying heavy weapons or wielding a shield (though you may drop any held items as part of your reaction to spread your arms). You cannot glide while wearing heavy armor, or if you are encumbered.")
        RaceNotes.append("Talons (see notes)")
        RaceNotes.append("Talons: Your sharp claws aid you in unarmed combat andwhile climbing. Your damage for an unarmed strike is 1d4 piercing damage. Additionally, you have advantage on Strength (Athletics) checks made to climb any surface your talons could reasonably grip.")
        PlProf.append(Perception)
        PlProf.append(Longbow)
        PlProf.append(Shortbow)
        PlProf.append(Spear)
        RaceNotes.append("Your familiarity with the longbow means that it is not considered a heavy weapon for you.")
        if subrace == "Maran Raptor (Bird)":
            Intelligence += 1
            RaceNotes.append("Swimmer: You have a swimming speed of 25 feet.")
            RaceNotes.append("Patient: When you react with a readied action, you have advantage on the first attack roll, skill check, or ability check you make as a part of that action.")
        if subrace == "Mistral Raptor (Bird)":
            Wisdom += 1
            PlProf.append(Acrobatics)
            RaceNotes.append("Aerial Defense: Creatures that attack you while you are falling, gliding, or jumping have disadvantage on their attack roll.")
    if race == "Reborn":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = abilityscores(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
        CreatureType = "Humanoid"
        walkingspeed = 30
        RaceNotes.append("Deathless Nature (see notes)")
        Notes.append("Deathless Nature: You have escaped death, a fact represented by the following benefits:\nYou have advantage on saving throws against disease and being poisoned, and you have resistance to poison damage.\nYou have advantage on death saving throws.\nYou don’t need to eat, drink, or breathe.\nYou don’t need to sleep, and magic can’t put you to sleep. You can finish a long rest in 4 hours if you spend those hours in an inactive, motionless state, during which you retain consciousness.")
        RaceNotes.append("Knowledge from a Past Life (see notes)")
        Notes.append(f"Knowledge from a Past Life: You temporarily remember glimpses of the past, perhaps faded memories from ages ago or a previous life. When you make an ability check that uses a skill, you can roll a d6 immediately after seeing the number on the d20 and add the number on the d6 to the check. You can use this feature {ProfBonus} times, and you regain all expended uses when you finish a long rest.")    
    if race == "Satyr":
        Hmo1 = d8()
        Hmo2 = d8()
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        SLANG.remove(Sylv)
        PlLang.append(Comm)
        PlLang.append(Sylv)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        Charisma += 2
        Dexterity += 1
        CreatureType = "Fey"
        walkingspeed = 35
        RaceNotes.append("Ram: You can use your head and horns to make unarmed strikes. If you hit with them, you deal bludgeoning damage equal to 1d4 + your Strength modifier.")
        RaceNotes.append("Magic Resistance: You have advantage on saving throws against spells and other magical effects.")
        RaceNotes.append("Mirthful Leaps (see notes)")
        Notes.append("Mirthful Leaps: Whenever you make a long or high jump, you can roll a d8 and add the number rolled to the number of feet you cover, even when making a standing jump. This extra distance costs movement as normal.")
        PlProf.append(Performance)
        PlProf.append(Persuasion)
        PlProf = musicalinstr(param, PlProf)
    if race == "Sharkin":
        Hmo1 = d4()
        Hmo2 = d4()
        Hmod = Hmo1 + Hmo2 + 2
        Hbase = 71
        Wmo1 = d4()
        Wmo2 = d4() + 3
        Wmod = Wmo1 + Wmo2
        Wbase = 160
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        SLANG.remove(Aqua)
        PlLang.append(Comm)
        PlLang.append(Aqua)
        CreatureType = "Humanoid"
        Constitution += 1
        Strength += 2
        walkingspeed = 30
        RaceNotes.append("Your swimming speed is 60 feet")
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("Amphibious: You can breath air and water.")
        RaceNotes.append("Fearless: Everyone has a disadvantage on Intimidation checks on you.")
        if subrace == "Blue Sharkin":
            RaceNotes.append("Graceful Swimmer: Your swimming speed increases to 90 feet.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Basking Sharkin":
            RaceNotes.append("Tough Hide: You gain a +1 bonus to your AC.")
            DamageResistance = "Non-Magical Piercing Damage and Poison Damage"
            RaceNotes.append(f"Damage Resistance: {DamageResistance}")
            RaceNotes.append("Huge Liver: You have advantage on saving throws against being poisoned.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Bull Sharkin":
            RaceNotes.append("Oceanic Rage (see notes)")
            Notes.append("Oceanic Rage: You may enter a rage as a bonus action. While raging, you gain a +2 to damage rolls at 1st level, +3 at 9th, and +4 at 16th. You have advantage on Strength Checks and Strength saving throws. You have resistance to bludgeoning, piercing, and slashing damage. If you are able to cast spells, you can't cast them or concentrate on them while raging. Your rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven't attacked a hostile creature since your last turn or taken damage since then. You can end your rage as a bonus action, and once you have raged you cannot do so again until you finish a long rest.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Cookie Cutter Sharkin":
            RaceNotes.append("Photophores: You chest and stomach can emit 5 feet of dim light in the dark, while underwater you have advantage on Stealth checks.")
            PlProf.append(Stealth)
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Goblin Sharkin":
            PlProf.append(Investigation)
            RaceNotes.append("Ampullae of Lorenzini: You have advantage on Perception and Investigation checks.")
            RaceNotes.remove(Darkvision)
            RaceNotes.append("Superior Darkvision (see notes)")
            Notes.append("Superior Darkvision: You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Hammerhead Sharkin":
            PlProf.append(Investigation)
            RaceNotes.append("Ampullae of Lorenzini: You have advantage on Perception and Investigation checks.")
            RaceNotes.append("Lateral Vision: You gain a +2 bonus to your passive Perception.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Leopard Sharkin":
            RaceNotes.append("Nictitating Membrane: You are able to see in murky environments and you have advantage on saving throws against being blinded.")
            RaceNotes.append("Oxygen Efficient: Your short and long rest times are cut in half.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Mako Sharkin":
            DamageResistance = "Cold Damage"
            RaceNotes.append(f"Damage Resistance: {DamageResistance}")
            RaceNotes.append("Speedy Swimmer: Your swimming speed increases to 120 feet.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Nurse Sharkin":
            PlProf.append(Investigation)
            RaceNotes.append("Ampullae of Lorenzini: You have advantage on Perception and Investigation checks.")
            RaceNotes.remove(Darkvision)
            RaceNotes.append("Modified Darkvision: You have darkvision up to 90ft. You see dim light as if it were bright light, and you see darkness as if it were dim light.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Thresher Sharkin":
            DamageResistance = "Cold Damage"
            RaceNotes.append(f"Damage Resistance: {DamageResistance}")
            RaceNotes.append("Whiplash (see notes)")
            Notes.append(f"Whiplash: As a bonus action, your tail can be used to strike a creature, potentially stunning it. The creature must make Constitution saving throw against a DC equal to 8 + your Constitution modifier + your proficiency bonus. On a failed save it becomes stunned until the end of its next turn. On a successful save, it does not get stunned. You can use this trait {ProfBonus} times, and you regain all expended uses when you finish a long rest.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Tiger Sharkin":
            RaceNotes.remove(Darkvision)
            RaceNotes.append("Modified Darkvision: You have darkvision up to 90ft. You see dim light as if it were bright light, and you see darkness as if it were dim light.")
            RaceNotes.append("Shell Crusher: You gain a +2 to attack and damage rolls against armored creatures.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Whale Sharkin":
            DamageResistance = "Non-magical bludgeoning damage."
            RaceNotes.append(f"Damage Resistance: {DamageResistance}")
            RaceNotes.append("Whale Toughness: Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Great White Sharkin":
            RaceNotes.append("Blood Frenzy (see notes)")
            Notes.append(f"Blood Frenzy: With the ability to smell blood from a range of 3 miles, the smell of it can excite your hunger for battle. When you make an attack against a creature that doesn't have all its hit points, you can choose to make the attack with advantage. You can use this trait {ProfBonus} times, and you regain all expended uses when you finish a long rest.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Cladoselache":
            PlProf.append(Investigation)
            RaceNotes.append("Ampullae of Lorenzini: You have advantage on Perception and Investigation checks.")
            RaceNotes.append("Speedy Swimmer: Your swimming speed increases to 90 feet.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Cretoxyrhina":
            PlProf.append(Investigation)
            RaceNotes.append("Ampullae of Lorenzini: You have advantage on Perception and Investigation checks.")
            RaceNotes.append("Blood Frenzy (see notes)")
            Notes.append(f"Blood Frenzy: With the ability to smell blood from a range of 3 miles, the smell of it can excite your hunger for battle. When you make an attack against a creature that doesn't have all its hit points, you can choose to make the attack with advantage. You can use this trait {ProfBonus} times, and you regain all expended uses when you finish a long rest.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Edestus":
            PlProf.append(Investigation)
            RaceNotes.append("Ampullae of Lorenzini: You have advantage on Perception and Investigation checks.")
            RaceNotes.append("Razored Teeth: You gain a +2 bonus to attack and damage rolls against unarmored creatures.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Helicoprion":
            PlProf.append(Investigation)
            RaceNotes.append("Ampullae of Lorenzini: You have advantage on Perception and Investigation checks.")
            RaceNotes.append("Hacksaw Jaw: You gain an extra 1d4 slashing damage bonus, against creatures that don't have all their hit points.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Hybodus":
            RaceNotes.append("Dorsal Stinger (see notes)")
            DorsalStingerDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                DorsalStingerDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                DorsalStingerDmg = "3d6"
            if plLvl >= 20:
                DorsalStingerDmg = "4d6"
            Notes.append(f"Dorsal Stinger: As a bonus action, you may pierce your foe. Your fins have stingers that does {DorsalStingerDmg} piercing damage.")
            RaceNotes.append("Stream Burst: Whilst swimming in a body of water, you can use a bonus action to perform the dash action.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Megalodon":
            PlProf.append(Investigation)
            RaceNotes.append("Ampullae of Lorenzini: You have advantage on Perception and Investigation checks.")
            RaceNotes.append("Blood Frenzy (see notes)")
            Notes.append(f"Blood Frenzy: With the ability to smell blood from a range of 3 miles, the smell of it can excite your hunger for battle. When you make an attack against a creature that doesn't have all its hit points, you can choose to make the attack with advantage. You can use this trait {ProfBonus} times, and you regain all expended uses when you finish a long rest.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Ptychodus":
            RaceNotes.append("Shell Crusher: You gain a +2 to attack and damage rolls against armored creatures.")
            RaceNotes.append("Stream Burst: Whilst swimming in a body of water, you can use a bonus action to perform the dash action.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Scapanorhynchus":
            PlProf.append(Investigation)
            RaceNotes.append("Ampullae of Lorenzini: You have advantage on Perception and Investigation checks.")
            RaceNotes.remove(Darkvision)
            RaceNotes.append("Superior Darkvision (see notes)")
            Notes.append("Superior Darkvision: You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Stethacanthus":
            RaceNotes.append("Dorsal Stinger (see notes)")   
            DorsalStingerDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                DorsalStingerDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                DorsalStingerDmg = "3d6"
            if plLvl >= 20:
                DorsalStingerDmg = "4d6"
            Notes.append(f"Dorsal Stinger: As a bonus action, you may pierce your foe. Your fins have stingers that does {DorsalStingerDmg} piercing damage.")
            RaceNotes.remove(Darkvision)
            RaceNotes.append("Superior Darkvision (see notes)")
            Notes.append("Superior Darkvision: You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
        if subrace == "Xenacanthus":      
            RaceNotes.append("Graceful Swimmer: Your swimming speed increases to 90 feet.")
            RaceNotes.append("Vicious Bite (see notes)")
            ViciousBiteDmg = "1d6"
            if ((plLvl >= 5) & (plLvl < 10)):
                ViciousBiteDmg = "2d6"
            if ((plLvl >= 10) & (plLvl < 20)):
                ViciousBiteDmg = "3d6"
            if plLvl >= 20:
                ViciousBiteDmg = "4d6"
            Notes.append(f"Vicious Bite: When you take the Attack action on your turn, you can replace one of your attacks with a vicious bite attack. This is a natural weapon attack with which you are proficient with and uses your Strength modifier for its attack rolls. This bite does {ViciousBiteDmg} piercing damage.")
    if race == "Shifter":
        walkingspeed = 30
        CreatureType = "Humanoid"
        RaceNotes.append("Darkvision (see notes)") 
        RaceNotes.append(Darkvision)   
        RaceNotes.append("Shifting (see notes)")
        Notes.append("Shifting: As a bonus action, you can assume a more bestial appearance. This transformation lasts for 1 minute, until you die, or until you revert to your normal appearance as a bonus action. When you shift, you gain temporary hit points equal to your level + your Constitution modifier (minimum of 1 temporary hit point). You also gain additional benefits that depend on your shifter subrace, described below. Once you shift, you can't do so again until you finish a short or long rest.")
        if subrace == "Beasthide Shifter":
            Hmo1 = d4()
            Hmo2 = d4()
            Hmod = Hmo1 + Hmo2
            Hbase = 62
            Wmo1 = d4()
            Wmo2 = d4()
            Wmod = Wmo1 + Wmo2
            Wbase = 130
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            Height = str(tl)
            Weight = str(hy)
            PlLang.append(Comm)
            PlLang, SLANG = languagegen(param, PlLang, SLANG) 
            Constitution += 2
            Strength += 1
            PlProf.append(Athletics)
            RaceNotes.append("Shifting Feature: Whenever you shift, you gain 1d6 additional temporary hit points. While shifted, you have a + 1 bonus to your Armor Class.")
        if subrace == "Longtooth Shifter":
            Hmo1 = d8()
            Hmo2 = d8()            
            Hmod = Hmo1 + Hmo2
            Hbase = 54
            Wmo1 = d4()
            Wmo2 = d4()
            Wmod = Wmo1 + Wmo2
            Wbase = 90
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            Height = str(tl)
            Weight = str(hy)
            PlLang.append(Comm)
            PlLang, SLANG = languagegen(param, PlLang, SLANG) 
            Strength += 2
            Dexterity += 1
            PlProf.append(Intimidation)
            RaceNotes.append("Shifting Feature (see notes)")
            Notes.append("Shifting Feature: While shifted, you can use your elongated fangs to make an unarmed strike as a bonus action. If you hit with your fangs, you can deal piercing damage equal to 1d6 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.")
        if subrace == "Swiftstride Shifter":
            Hmo1 = d6()
            Hmo2 = d6()        
            Hmod = Hmo1 + Hmo2
            Hbase = 58
            Wmo1 = d4()
            Wmo2 = d4()
            Wmod = Wmo1 + Wmo2
            Wbase = 110   
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            Height = str(tl)
            Weight = str(hy)        
            PlLang.append(Comm)
            PlLang, SLANG = languagegen(param, PlLang, SLANG)
            Dexterity += 2
            Charisma += 1
            PlProf.append(Acrobatics)
            RaceNotes.append("Shifting Feature: While shifted, your walking speed increases by 10 feet. Additionally, you can move up to 10 feet as a reaction when a creature ends its turn within 5 feet of you. This reactive movement doesn't provoke opportunity attacks.")
        if subrace == "Wildhunt Shifter":    
            Hmo1 = d10()
            Hmo2 = d10()
            Hmod = Hmo1 + Hmo2
            Hbase = 50
            Wmo1 = d4()
            Wmo2 = d4()
            Wmod = Wmo1 + Wmo2
            Wbase = 70
            tl = Hmod + Hbase
            Wemod = Wmod*Hmod
            hy = Wbase + Wemod
            Height = str(tl)
            Weight = str(hy)
            PlLang.append(Comm)
            PlLang, SLANG = languagegen(param, PlLang, SLANG)
            Wisdom += 2
            Dexterity += 1
            PlProf.append(Survival)
            RaceNotes.append("Shifting Feature (see notes)")
            Notes.append("Shifting Feature: While shifted, you have advantage on Wisdom checks, and no creature within 30 feet of you can make an attack roll with advantage against you, unless you're incapacitated.")
    if race == "Simic Hybrid":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        SimHybLang = [Elvi, Veda]
        if param == "Y":
            print("0 - Random")
            print("1 - Elvish")
            print("2 - Vedalken")
            shlang = int(input("Choose your symic hybrid language. "))
            if shlang == 1:
                PlLang.append(Comm)
                PlLang.append(Elvi)
            if shlang == 2:
                PlLang.append(Comm)
                PlLang.append(Veda)
            if shlang == 0:
                SimicHybridLang = random.choice(SimHybLang)
                PlLang.append(Comm)
                PlLang.append(SimicHybridLang)
                SLANG.remove(SimicHybridLang)
        if param == "N":
            SimicHybridLang = random.choice(SimHybLang)
            PlLang.append(Comm)
            PlLang.append(SimicHybridLang)
            SLANG.remove(SimicHybridLang)
        CreatureType = "Humanoid"
        Constitution += 2
        Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = singleabilityscore(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
        walkingspeed = 30
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("Animal Enhancement(1) (see notes)")
        Notes.append("Animal Enhancement(1): Your body has been altered to incorporate certain animal characteristics. You choose one animal enhancement now and a second enhancement at 5th level.\nAt 1st level, choose one of the following options:\nManta Glide - You have ray-like fins that you can use as wings to slow your fall or allow you to glide. When you fall and aren't incapacitated, you can subtract up to 100 feet from the fall when calculating falling damage, and you can move up to 2 feet horizontally for every 1 foot you descend. \nNimble Climber - You have a climbing speed equal to your walking speed.\nUnderwater Adaptation - You can breathe air and water, and you have a swimming speed equal to your walking speed.")
        if plLvl >= 5:
            RaceNotes.append("Animal Enhancement(2) (see notes)")
            AnimalEnhDMG = "2d10"
            if ((plLvl >= 11) & (plLvl < 17)):
                AnimalEnhDMG = "3d10"
            if plLvl > 17:
                AnimalEnhDMG = "4d10"
            Notes.append(f"Animal Enhancement(2): Your body evolves further, developing new characteristics. Choose one of the options you didn't take at 1st level, or one of the following options:\nGrappling Appendage - You have two special appendages growing alongside your arms. Choose whether they're both claws or tentacles. As an action, you can use one of them to try to grapple a creature. Each one is also a natural weapon, which you can use to make an unarmed strike. If you hit with it, the target takes bludgeoning damage equal to 1d6 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike. Immediately after hitting, you can try to grapple the target as a bonus action. These appendages can't precisely manipulate anything and can't wield weapons, magic items, or other specialized equipment.\mCarapace - Your skin in places is covered by a thick shell. You gain a +1 bonus to AC when you're not wearing heavy armor.\mAcid Spit - As an action, you can spray acid from glands in your mouth, targeting one creature or object you can see within 30 feet of you. The target takes {AnimalEnhDMG} acid damage unless it succeeds on a Dexterity saving throw against a DC equal to 8 + your Constitution modifier + your proficiency bonus. You can use this trait a number of times equal to your Constitution modifier (minimum of once), and you regain all expended uses of it when you finish a long rest.")
    if race == "Strig":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 46
        Wmo1 = d6()
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 80
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Bird)
        PlLang.append(UAur)
        CreatureType = "Avian Humanoid"  
        Strength += 2
        walkingspeed = 30
        RaceNotes.append("Glide (see notes)")
        Notes.append("Glide: Using your feathered arms, you can slow your fall, and glide short distances. When falling you can use your reaction to spread your arms, stiffen your wing feathers, and slow your descent. While doing so, you continue to fall gently at a speed of 60 feet per round, taking no fall damage when you land. If you would fall at least 10 feet in this way, you may fly up to your movement speed in one direction you choose, although you cannot choose to move upwards, landing in the space you finish your movement. You cannot glide while carrying heavy weapons or wielding a shield (though you may drop any held items as part of your reaction to spread your arms). You cannot glide while wearing heavy armor, or if you are encumbered.")
        RaceNotes.append("Talons (see notes)")
        Notes.append("Talons: Your sharp claws aid you in unarmed combat and while climbing. Your damage for an unarmed strike is 1d4 piercing damage. Additionally, you have advantage on Strength (Athletics) checks made to climb any surface your talons could reasonably grip.")
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("Patterned Feathers: You have advantage on Dexterity (Stealth) checks when you attempt to hide in a forest.")
        if subrace == "Stout Strig":
            Constitution += 1
            PlProf.append(Intimidation)
            RaceNotes.append("Brawler: When you successfully attack a target with your talons, you can choose to grapple that target as a bonus action.")
        if subrace == "Swift Strig":
            Dexterity += 1
            walkingspeed = 35
            PlProf.append(Survival)
    if race == "Tabaxi":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 58
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 90
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        Dexterity += 2
        Charisma += 1
        walkingspeed = 30
        CreatureType = "Humanoid"
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("Feline Agility (see notes)")
        Notes.append("Feline Agility: Your reflexes and agility allow you to move with a burst of speed. When you move on your turn in combat, you can double your speed until the end of the turn. Once you use this trait, you can't use it again until you move 0 feet on one of your turns.")
        RaceNotes.append("Cat's Claws (see notes)")
        Notes.append("Cat's Claws: Because of your claws, you have a climbing speed of 20 feet. In addition, your claws are natural weapons, which you can use to make unarmed strikes. If you hit with them, you deal slashing damage equal to 1d4 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.")
        PlProf.append(Perception)
        PlProf.append(Stealth)
    if race == "Tiefling":
        Hmo1 = d8()
        Hmo2 = d8()
        Hmod = Hmo1 + Hmo2
        Hbase = 57
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Infe)
        SLANG.remove(Infe)
        CreatureType = "Humanoid"
        Charisma += 2
        walkingspeed = 30
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        DamageResistance = "Fire Damage"
        RaceNotes.append(f"Damage Resistance: {DamageResistance}")
        if subrace == "Asmodeus Subject Tiefling":
            Intelligence += 1
            RaceNotes.append("Infernal Legacy(1) (see notes). More options are available at higher levels.")
            Notes.append("Infernal Legacy(1): You know the Thaumaturgy cantrip. Charisma is your spellcasting ability for this spell. More options are available at higher levels.")
            if plLvl >= 3:
                RaceNotes.append("Infernal Legacy(2) (see notes)")
                Notes.append("Infernal Legacy(2): You can cast the Hellish Rebuke spell as a 2nd-level spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for this spell.")
            if plLvl >= 5:
                RaceNotes.append("Infernal Legacy(3) (see notes)")
                Notes.append("Infernal Legacy(3): You can cast the Darkness spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for this spell.")
        if subrace == "Baalzebul Subject Tiefling":
            Intelligence += 1
            RaceNotes.append("Legacy of Maladomini(1) (see notes). More options are available at higher levels.")
            Notes.append("Legacy of Maladomini(1): You know the Thaumaturgy cantrip. Charisma is your spellcasting ability for this spell.")
            if plLvl >= 3:
                RaceNotes.append("Legacy of Maladomini(2) (see notes)")
                Notes.append("Legacy of Maladomini(2): You can cast the Ray of Sickness spell once as a 2nd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
            if plLvl >= 5:
                RaceNotes.append("Legacy of Maladomini(3) (see notes)")
                Notes.append("Legacy of Maladomini(3): You can also cast the Crown of Madness spell once. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
        if subrace == "Dispater Subject Tiefling":
            Dexterity += 1
            RaceNotes.append("Legacy of Dis(1) (see notes). More options are available at higher levels.")
            Notes.append("Legacy of Dis(1): You know the Thaumaturgy cantrip. Charisma is your spellcasting ability for this spell.")
            if plLvl >= 3:
                RaceNotes.append("Legacy of Dis(2) (see notes)")
                Notes.append("Legacy of Dis(2): You can cast the Disguise Self spell once as a 2nd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
            if plLvl >= 5:
                RaceNotes.append("Legacy of Dis(3) (see notes)")            
                Notes.append("Legacy of Dis(3): You can also cast the Detect Thoughts spell once. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
        if subrace == "Fierna Subject Tiefling":
            Wisdom += 1
            RaceNotes.append("Legacy of Phlegethos(1) (see notes). More options are available at higher levels.")
            Notes.append("Legacy of Phlegethos(1): You know the Friends cantrip. Charisma is your spellcasting ability for this spell.")
            if plLvl >= 3:
                RaceNotes.append("Legacy of Phlegethos(2) (see notes)")
                Notes.append("Legacy of Phlegethos(2): You can cast the Charm Person spell once as a 2nd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
            if plLvl >= 5:
                RaceNotes.append("Legacy of Phlegethos(3) (see notes)")        
                Notes.append("Legacy of Phlegethos(3): You can also cast the Suggestion spell once. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
        if subrace == "Glasya Subject Tiefling":
            Dexterity += 1
            RaceNotes.append("Legacy of Malbolge(1) (see notes). More options are available at higher levels.")
            Notes.append("Legacy of Malbolge(1): You know the Minor Illusion cantrip. Charisma is your spellcasting ability for this spell.")
            if plLvl >= 3:
                RaceNotes.append("Legacy of Malbolge(2) (see notes)")
                Notes.append("Legacy of Malbolge(2): You can cast the Disguise Self spell once as a 2nd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
            if plLvl >= 5:
                RaceNotes.append("Legacy of Malbolge(3) (see notes)")        
                Notes.append("Legacy of Malbolge(3): You can also cast the Invisibility spell once as a 3rd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
        if subrace == "Levistus Subject Tiefling":
            Constitution += 1
            RaceNotes.append("Legacy of Stygia(1) (see notes). More options are available at higher levels.")
            Notes.append("Legacy of Stygia(1): You know the Ray of Frost cantrip. Charisma is your spellcasting ability for this spell.")
            if plLvl >= 3:
                RaceNotes.append("Legacy of Stygia(2) (see notes)")
                Notes.append("Legacy of Stygia(2): You can cast the Armor of Agathys spell once as a 2nd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
            if plLvl >= 5:
                RaceNotes.append("Legacy of Stygia(3) (see notes)")        
                Notes.append("Legacy of Stygia(3): You can also cast the Darkness spell once. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
        if subrace == "Mammon Subject Tiefling":
            Intelligence += 1
            RaceNotes.append("Legacy of Minauros(1) (see notes). More options are available at higher levels.")
            Notes.append("Legacy of Minauros(1): You know the Mage Hand cantrip. Charisma is your spellcasting ability for this spell.")
            if plLvl >= 3:
                RaceNotes.append("Legacy of Minauros(2) (see notes)")
                Notes.append("Legacy of Minauros(2): You can cast the Tenser's Floating Disk spell once as a 2nd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
            if plLvl >= 5:
                RaceNotes.append("Legacy of Minauros(3) (see notes)")        
                Notes.append("Legacy of Minauros(3): You can also cast the Arcane Lock spell once. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
        if subrace == "Mephistopheles Subject Tiefling":
            Intelligence += 1
            RaceNotes.append("Legacy of Cania(1) (see notes). More options are available at higher levels.")
            Notes.append("Legacy of Cania(1): You know the Mage Hand cantrip. Charisma is your spellcasting ability for this spell.")
            if plLvl >= 3:
                RaceNotes.append("Legacy of Cania(2) (see notes)")
                Notes.append("Legacy of Cania(2): You can cast the Burning Hands spell once as a 2nd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
            if plLvl >= 5:
                RaceNotes.append("Legacy of Cania(3) (see notes)")        
                Notes.append("Legacy of Cania(3): You can also cast the Flame Blade spell once as a 3rd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
        if subrace == "Zariel Subject Tiefling":
            Strength += 1
            RaceNotes.append("Legacy of Avernus(1) (see notes). More options are available at higher levels.")
            Notes.append("Legacy of Avernus(1): You know the Thaumaturgy cantrip. Charisma is your spellcasting ability for this spell.")
            if plLvl >= 3:
                RaceNotes.append("Legacy of Avernus(2) (see notes)")
                Notes.append("Legacy of Avernus(2): You can cast the Searing Smite spell once as a 2nd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
            if plLvl >= 5:
                RaceNotes.append("Legacy of Avernus(3) (see notes)")    
                Notes.append("Legacy of Avernus(3): You can also cast the Branding Smite spell once as a 3rd-level spell. You must finish a long rest to cast this spell again with this trait. Charisma is your spellcasting ability for this spell.")
    if race == "Thri-Kreen":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = abilityscores(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
        CreatureType = "Monstrosity"
        walkingspeed = 35
        RaceNotes.append("Chameleon Carapace (see notes)")
        Notes.append("Chameleon Carapace: While you aren't wearing armor, your carapace gives you a base Armor Class of 13 + your Dexterity modifier.\nAs an action, you can change the color of your carapace to match the color and texture of your surroundings, giving you advantage on Dexterity (Stealth) checks made to hide in those surroundings.")
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("Secondary Arms (see notes)")
        Notes.append("Secondary Arms: You have two slightly smaller secondary arms below your primary pair of arms. The secondary arms can manipulate an object, open or close a door or container, pick up or set down a Tiny object, or wield a weapon that has the light property.")
        RaceNotes.append("Sleepless (see notes)")
        Notes.append("Sleepless: You do not require sleep and can remain conscious during a long rest, though you must still refrain from strenuous activity to gain the benefit of the rest.")
        RaceNotes.append("Thri-kreen Telepathy (see notes)")
        Notes.append("Thri-kreen Telepathy: Without the assistance of magic, you can't speak the non-thri-kreen languages you know. Instead you use telepathy to convey your thoughts. You have the magical ability to transmit your thoughts mentally to willing creatures you can see within 120 feet of yourself. A contacted creature doesn't need to share a language with you to understand your thoughts, but it must be able to understand at least one language. Your telepathic link to a creature is broken if you and the creature move more than 120 feet apart, if either of you is incapacitated, or if either of you mentally breaks the contact (no action required).")
    if race == "Tortle":
        Hmo1 = d12()
        Hmo2 = d12()
        Hmo3 = d12()
        Hmod = Hmo1 + Hmo2 + Hmo3
        Hbase = 43
        Wmo1 = d6()
        Wmo2 = d6()
        Wmod = Wmo1 + Wmo2
        Wbase = 310
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        SLANG.remove(Aqua)
        PlLang.append(Comm)
        PlLang.append(Aqua)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        Strength += 2
        Wisdom += 1
        walkingspeed = 30
        CreatureType = "Humanoid"
        RaceNotes.append("Claws (see notes)")
        Notes.append("Claws: Your claws are natural weapons, which you can use to make unarmed strikes. If you hit with them, you deal slashing damage equal to 1d4 + your Strength modifier, instead of bludgeoning damage normal for an unarmed strike.")
        RaceNotes.append("Hold Breath (see notes)")
        Notes.append("Hold Breath: You can hold your breath for up to 1 hour at a time. Tortles aren't natural swimmers, but they can remain underwater for some time before needing to come up for air.")
        RaceNotes.append("Natural Armor (see notes)")
        Notes.append("Natural Armor: Due to your shell and the shape of your body, you are ill-suited to wearing armor. Your shell provides ample protection, however; it gives you a base AC of 17 (your Dexterity modifier doesn't affect this number). You gain no benefit from wearing armor, but if you are using a shield, you can apply the shield's bonus as normal.")
        RaceNotes.append("Shell Defense (see notes)")
        Notes.append("Shell Defense: You can withdraw into your shell as an action. until you emerge, you gain a +4 bonus to AC, and you have advantage on Strength and Constitution saving throws. While in your shell, you are prone, your speed is 0 and can't increase, you have disadvantage on Dexterity saving throws, you can't take reactions, and the only action you can take is a bonus action to emerge from your shell.")
        PlProf.append(Survival)
    if race == "Triton":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 54
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 90
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Prim)
        SLANG.remove(Prim)
        Strength += 1
        Constitution += 1
        Charisma += 1
        walkingspeed = 30
        CreatureType = "Humanoid"
        RaceNotes.append("You have a swimming speed of 30 feet.")
        RaceNotes.append("Amphibious: You can breathe air and water.")
        RaceNotes.append("Control Air and Water (see notes)")
        Notes.append("Control Air and Water: A child of the sea, you can call on the magic of elemental air and water. You can cast Fog Cloud with this trait. Starting at 3rd level, you can cast Gust of Wind with it, and starting at 5th level, you can also cast Wall of Water with it. Once you cast a spell with this trait, you can't cast that spell with it again until you finish a long rest. Charisma is your spellcasting ability for these spells.")
        RaceNotes.append("Emissary of the Sea (see notes)")
        Notes.append("Emissary of the Sea: Aquatic beasts have an extraordinary affinity with your people. You can communicate simple ideas with beasts that can breathe water. They can understand the meaning of your words, though you have no special ability to understand them in return.")
        DamageResistance = "Cold Damage"
        RaceNotes.append(f"Damage Resistance: {DamageResistance}")
        RaceNotes.append("Guardians of the Depths: You ignore any of the drawbacks caused by a deep, underwater environment.")
    if race == "Vedalken":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 64
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)        
        SLANG.remove(Veda)
        PlLang.append(Comm)
        PlLang.append(Veda)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        CreatureType = "Humanoid"
        Intelligence += 2
        Wisdom += 1
        walkingspeed = 30
        RaceNotes.append("Vedalken Dispassion: You have advantage on all Intelligence, Wisdom, and Charisma saving throws.")
        PlProf = vedsixskillprof(param, PlProf, Arcana, History, Investigation, Medicine, Performance, SleightofHand)
        PlProf = vedartisantools(param, PlProf)
        RaceNotes.append("Partially Amphibious (see notes)")
        Notes.append("Partially Amphibious: By absorbing oxygen through your skin, you can breathe underwater for up to 1 hour. Once you've reached that limit, you can't use this trait again until you finish a long rest.")
    if race == "Verdan":
        Hmo1 = d4()
        Hmo2 = d4()
        Hmod = Hmo1 + Hmo2
        Hbase = 41
        Wmo1 = 1
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 35
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)        
        SLANG.remove(Gobl)
        PlLang.append(Comm)
        PlLang.append(Gobl)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        Constitution += 1
        Charisma += 2
        walkingspeed = 30
        CreatureType = "Humanoid"
        RaceNotes.append("Black Blood Healing (see notes)")
        Notes.append("Black Blood Healing: The black blood that is a sign of your people's connection to That-Which-Endures boosts your natural healing. When you roll a 1 or 2 on any Hit Die you spend at the end of a short rest, you can reroll the die and must use the new roll.")
        RaceNotes.append("Limited Telepathy (see notes)")
        Notes.append("Limited Telepathy: You can telepathically speak to any creature you can see within 30 feet of you. You don't need to share a language with the creature for it to understand your telepathy, but it must be able to understand at least one language. This process of communication is slow and limited, allowing you to transmit and receive only simple ideas and straightforward concepts.")
        PlProf.append(Persuasion)
        RaceNotes.append("Telepathic Insight: Your mind's connection to the world around you strengthens your will. You have advantage on all Wisdom and Charisma saving throws.")
    if race == "Vulpin":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 50
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 80
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)        
        PlLang.append(Bird)
        PlLang.append(Vulp)
        SLANG.remove(Vulp)
        Intelligence += 2
        Charisma += 1
        walkingspeed = 30
        CreatureType = "Humanoid"
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("Bite (see notes)")
        Notes.append("Bite: You have sharp fangs that enable you to make natural bite attacks. You can choose to bite as an unarmed strike that deals 1d6 points of piercing damage, which can be calculated using either your Strength or Dexterity modifier for both the attack roll and damage bonus.")
        RaceNotes.append("Evasive: You add your Intelligence modifier as a bonus on all Dexterity saving throws.")
        RaceNotes.append("Bewitching Guile(1) (see notes). More options are available at higher levels.")
        Notes.append("Bewitching Guile(1): You can cast Charm Person as a 1st level spell with this trait, and regain the ability to do so when you finish a long rest. Intelligence is your spellcasting ability for this spell.")
        if plLvl >= 3:
            RaceNotes.append("Bewitching Guile(2) (see notes)")
            Notes.append("Bewitching Guile(2): You can cast Ambush Prey as a 2nd level spell with this trait, and regain the ability to do so when you finish a long rest. Intelligence is your spellcasting ability for this spell.")
        if plLvl >= 5:
            RaceNotes.append("Bewitching Guile(3) (see notes)")
            Notes.append("Bewitching Guile(3): You can cast Fear with this trait, and regain the ability to do so when you finish a long rest. Intelligence is your spellcasting ability for this spell.")
    if race == "Warforged":
        Hmo1 = d6()
        Hmo2 = d6()
        Hmod = Hmo1 + Hmo2
        Hbase = 60
        Wmo1 = 4
        Wmo2 = 0
        Wmod = Wmo1 + Wmo2
        Wbase = 270
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)        
        PlLang.append(Comm)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        CreatureType = "Construct"
        Constitution += 2
        Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom = singleabilityscore(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom)
        walkingspeed = 30
        RaceNotes.append("Constructed Resilience (see notes)")
        Notes.append("Constructed Resilience: You were created to have remarkable fortitude, represented by the following benefits:\nYou have advantage on saving throws against being poisoned, and you have resistance to poison damage.\nYou don't need to eat, drink, or breathe.\nYou are immune to disease.\nYou don't need to sleep, and magic can't put you to sleep.")
        RaceNotes.append("Sentry's Rest (see notes)")
        Notes.append("Sentry's Rest: When you take a long rest, you must spend at least six hours in an inactive, motionless state, rather than sleeping. In this state, you appear inert, but it doesn't render you unconscious, and you can see and hear as normal.")
        RaceNotes.append("Integrated Protection (see notes)")
        Notes.append("Integrated Protection: Your body has built-in defensive layers, which can be enhanced with armor:\nYou gain a +1 bonus to Armor Class.\nYou can don only armor with which you have proficiency. To don armor, you must incorporate it into your body over the course of 1 hour, during which you remain in contact with the armor. To doff armor, you must spend 1 hour removing it. You can rest while donning or doffing armor in this way.\nWhile you live, your armor can't be removed from your body against your will.")
        PlProf = skillprof(param, PlProf)
        PlProf = artisantools(param, PlProf)
    if race == "Wechselkind":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)        
        SLANG.remove(Sylv)
        PlLang.append(Sylv)
        PlLang, SLANG = languagegen(param, PlLang, SLANG)
        CreatureType = "Fey"
        Constitution += 2
        Charisma += 1
        walkingspeed = 25
        DamageResistance = "Poison Damage"
        RaceNotes.append(f"Damage Resistance: {DamageResistance}")
        RaceNotes.append("Artificial Form (see notes)")
        Notes.append("Artificial Form: As a constructed creature, your body functions differently than a normal person.\nYou have advantage on saving throws against being poisoned, and you have resistance to poison damage.\nYou are immune to disease. You don’t need to eat, drink, sleep, or breathe. You are still considered humanoid.")
        RaceNotes.append("Faerie Glamour (see notes)")
        Notes.append("Faerie Glamour: When the faerie leaves a wechselkind in place of a mortal child, they cover it with a glamour to make it appear identical to the child that was stolen. Over time this glamour fades, but a wechselkind can still call upon it in times of need.\nYou may cast the Disguise Self spell once with this trait, but only to take on the appearance of the child you were intended to replace, and you regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for this spell.")
        RaceNotes.append("Childish Agility: You can move through the space of any creature that is of a size larger than yours.")
        PlProf.append(Acrobatics)
    if race == "Yuan-ti":
        Hmo1 = d10()
        Hmo2 = d10()
        Hmod = Hmo1 + Hmo2
        Hbase = 56
        Wmo1 = d4()
        Wmo2 = d4()
        Wmod = Wmo1 + Wmo2
        Wbase = 110
        tl = Hmod + Hbase
        Wemod = Wmod*Hmod
        hy = Wbase + Wemod
        Height = str(tl)
        Weight = str(hy)
        PlLang.append(Comm)
        PlLang.append(Abys)
        PlLang.append(Drac)
        SLANG.remove(Abys)
        SLANG.remove(Drac)
        CreatureType = "Humanoid"
        Intelligence += 1
        Charisma += 2
        walkingspeed = 30
        RaceNotes.append("Darkvision (see notes)")
        Notes.append(Darkvision)
        RaceNotes.append("Innate Spellcasting (see notes)")
        Notes.append("Innate Spellcasting: You know the Poison Spray cantrip. You can cast Animal Friendship an unlimited number of times with this trait, but you can target only snakes with it. Starting at 3rd level, you can also cast Suggestion with this trait. Once you cast it, you can't do so again until you finish a long rest. Charisma is your spellcasting ability for these spells.")
        RaceNotes.append("Magic Resistance: You have advantage on saving throws against spells and other magical effects.")
        DamageResistance = "Immunity to Poison Damage"
        RaceNotes.append(f"Damage Resistance: {DamageResistance}")
        RaceNotes.append("You are immune to the poisoned condition.")
    RaceNotes.append(f"Creature Type: {CreatureType}")

    return Gender, HollowOne, race, subrace, Lineage, Height, Weight, walkingspeed, PlLang, SLANG, PlProf, Notes, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom, RaceNotes

import random
import math
from dndchargen_languagesskills import *

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

#Define a function called hpcalc that determines your hp, given your level, and what dice you give it
def hpcalc(chlvl, dicefunc):
    result = 0
    for i in range(chlvl):
        result += dicefunc()
    return result

ChaST = "Charisma(ST)"
ConST = "Constitution(ST)"
DexST = "Dexterity(ST)"
IntST = "Intelligence(ST)"
StrST = "Strength(ST)"
WisST = "Wisdom(ST)"
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
Shield = "Shield" 
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
ThievKit = "Thieves' Tools"

def dndchargen_characterbuilder(param, plLvl, Class, subclass, BGL, EQP, SkillsProf, PlProf, data):
    ClassNotes = []
    ProfBonus = int(data['ProfBonus'])
    ChaMod = int(data['CHaMod'])
    ConMod = int(data['CONmod'])
    DexMod = int(data['DEXmod'])
    IntMod = int(data['INTmod'])
    StrMod = int(data['STRmod'])
    WisMod = int(data['WISmod'])
    if (plLvl >= 4) & (plLvl <= 8):
        ClassNotes.append("You can increase one score by 2, two by one, or a feat. As normal, you can't increase an ability score above 20 using this feature.")
    if (plLvl >= 8 & (plLvl <= 12)):
        ClassNotes.append("You can increase one score by 2, two by one, or a feat. As normal, you can't increase an ability score above 20 using this feature.")    
    if Class == "Artificer":
        if param == "Y":
            artlvl = int(input(f"Given your player level of {plLvl}, What is your Artificer level? "))   
        if param == "N":
            artlvl = plLvl
        hitdice = f"{artlvl}d8"
        if artlvl == 1:
            hitpoints = 8 + ConMod
        else:
            hitpoints = 8 + ConMod + hpcalc(artlvl, d8)
        PlProf.extend(LightArmor)
        PlProf.extend(MediumArmor)
        PlProf.append(Shield)
        PlProf.extend(SimpleWeapons)
        PlProf.append(ThievKit)
        PlProf.append(TinkTools)
        PlProf = artisantools(param, PlProf)
        SkillsProf.append(ConST)
        SkillsProf.append(IntST)
        SkillsProf = twoskillsfromlist(param, SkillsProf, Arcana, History, Investigation, Medicine, Nature, Perception, SleightofHand)
        ArtChoices = ["Starting Equipment", "Gold"]
        ArtChoices2 = ["Studded Leather Armor", "Scale Mail"]
        if param == "Y":
            print("0 - Random")
            print("1 - Starting Equipment")
            print("2 - Gold")
            sego = int(input("Would you like the starting equipment or gold(5d4 x 10gp, must forgo starting equipment from background)? "))
            if sego == 1:
                EQP = twosimpleweapons(param, EQP)
                EQP.append("A Light Crossbow and 20 bolts")
                print("0 - Random")
                print("1 - Studded Leather Armor")
                print("2 - Scale Mail")
                artchoice3 = int(input("Would you like 1 - Studded Leather Armor, or 2 - Scale Mail? "))
                if artchoice3 == 1:
                    EQP.append("Studded Leather Armor")
                if artchoice3 == 2:
                    EQP.append("Scale Mail")
                if artchoice3 == 0:
                    RandArtChoice2 = random.choice(ArtChoices2)
                    EQP.append(RandArtChoice2)
                EQP.append(ThievKit)
                EQP.append("A Dungeoneer's Pack")
            if sego == 2:
                EQP.clear()
                BGL = BGL + d4() + d4() + d4() + d4() + d4()
            if sego == 0:
                RandArtChoice = random.choice(ArtChoices)
                if RandArtChoice == "Starting Equipment":    
                    EQP = twosimpleweapons(param, EQP)
                    EQP.append("A Light Crossbow and 20 bolts")
                    RandArtChoice2 = random.choice(ArtChoices2)
                    EQP.append(RandArtChoice2)
                    EQP.append(ThievKit)
                    EQP.append("A Dungeoneer's Pack")
                if RandArtChoice == "Gold":
                    EQP.clear()
                    BGL = BGL + d4() + d4() + d4() + d4() + d4()
        if param == "N":
            RandArtChoice = random.choice(ArtChoices)
            if RandArtChoice == "Starting Equipment":    
                EQP = twosimpleweapons(param, EQP)
                EQP.append("A Light Crossbow and 20 bolts")
                RandArtChoice2 = random.choice(ArtChoices2)
                EQP.append(RandArtChoice2)
                EQP.append(ThievKit)
                EQP.append("A Dungeoneer's Pack")
            if RandArtChoice == "Gold":
                EQP.clear()
                BGL = BGL + d4() + d4() + d4() + d4() + d4()
        PlProf.extend(Firearms)
        
        ClassNotes.append("Magical Tinkering - At 1st level, you learn how to invest a spark of magic into mundane objects. To use this ability, you must have tinker's tools or other artisan's tools in hand. You then touch a Tiny nonmagical object as an action and give it one of the following magical properties of your choice:\n - The object sheds bright light in a 5-foot radius and dim light for an additional 5 feet \n - Whenever tapped by a creature, the object emits a recorded message that can be heard up to 10 feet away \n - You utter the message when you bestow this property on the object, and the recording can be no more than 6 seconds long \n - The object continuously emits your choice of an odor or a nonverbal sound (wind, waves, chirping, or the like). The chosen phenomenon is perceivable up to 10 feet away \n - A static visual effect appears on one of the object's surfaces. This effect can be a picture, up to 25 words of text, lines and shapes, or a mixture of these elements, as you like. \n The chosen property lasts indefinitely. As an action, you can touch the object and end the property early. \n You can bestow magic on multiple objects, touching one object each time you use this feature, though a single object can only bear one property at a time. The maximum number of objects you can affect with this feature at one time is equal to your Intelligence modifier (minimum of one object). If you try to exceed your maximum, the oldest property immediately ends, and then the new property applies.")
        SpellcastingClass = "Artificer"
        SpellcastingAbility = "Int"
        SpellsaveDC = 8 + ProfBonus + IntMod
        SpellAttackMod = ProfBonus + IntMod
        if artlvl >= 2:
            ClassNotes.append("Infuse Item - You have the ability to imbue mundane items with certain magical infusions. The magic items you create with this feature are effectively prototypes of permanent items. You learn additional infusions of your choice when you reach certain levels in this class. Whenever you gain a level in this class, you can replace one of the artificer infusions you learned with a new one.")
            InfusionNumber = 4
            ClassNotes.append(f"You have {InfusionNumber} infusions")
            ClassNotes.append("Infusing an Item - Whenever you finish a long rest, you can touch a nonmagical object and imbue it with one of your artificer infusions, turning it into a magic item. An infusion works on only certain kinds of objects, as specified in the infusion's description. If the item requires attunement, you can attune yourself to it the instant you infuse the item. If you decide to attune to the item later, you must do so using the normal process for attunement (see 'Attunement' in chapter 7 of the Dungeon Master's Guide). Your infusion remains in an item indefinitely, but when you die, the infusion vanishes after a number of days have passed equal to your Intelligence modifier (minimum of 1 day). The infusion also vanishes if you give up your knowledge of the infusion for another one. You can infuse more than one nonmagical object at the end of a long rest; the maximum number of objects appears in the Infused Items column of the Artificer table. You must touch each of the objects, and each of your infusions can be in only one object at a time. Moreover, no object can bear more than one of your infusions at a time. If you try to exceed your maximum number of infusions, the oldest infusion immediately ends, and then the new infusion applies.")
        if artlvl >= 3:
            ClassNotes.append("The Right Tool For The Job - At 3rd level, you learn how to produce exactly the tool you need: with tinker's tools in hand, you can magically create one set of artisan's tools in an unoccupied space within 5 feet of you. This creation requires 1 hour of uninterrupted work, which can coincide with a short or long rest. Though the product of magic, the tools are nonmagical, and they vanish when you use this feature again.")
        if subclass == "Alchemist Speciliast Artificer":
        if subclass == "Armorer Speciliast Artificer":
        if subclass == "Artilierist Speciliast Artificer":
        if subclass == "Battle Smith Speciliast Artificer":        
    if Class == "Barbarian":
        if param == "Y":
            barblvl = int(input(f"Given your player level of {plLvl}, what is your Barbarian level? "))        
        if subclass == "Path of the Ancestral Guardian Barbarian":
        if subclass == "Path of the Battlerager Barbarian":
        if subclass == "Path of the Beast Barbarian":
            BPBO1 = "One of your parents is a lycanthrope, and you've inherited some of their curse."
            BPBO2 = "You are descended from an archdruid and inherited the ability to partially change shape."
            BPBO3 = "A fey spirit gifted you with the ability to adopt different bestial aspects."
            BPBO4 = "An ancient animal spirit dwells within you, allowing you to walk this path."
            BPBO = [BPBO1, BPBO2, BPBO3, BPBO4]
            BarbPathBeastOrigin = random.choice(BPBO)
            ClassNotes.append(f"As a Path of the Beast Barbarian, the Origin of the Beast is: {BarbPathBeastOrigin}")                  
        if subclass == "Path of the Berserker Barbarian":
        if subclass == "Path of the Giant Barbarian":
        if subclass == "Path of the Juggernaut Barbarian":
        if subclass == "Path of the Storm Herald Barbarian":
        if subclass == "Path of the Totem Warrior Barbarian":
        if subclass == "Path of the Zealot Barbarian":
        if subclass == "Path of the Wild Magic Barbarian":        
    if Class == "Bard":
        if param == "Y":
            bardlvl = int(input(f"Given your player level of {plLvl}, what is your Bard level? "))        
        if subclass == "College of Creation Bard":
        if subclass == "College of Eloquence Bard":
        if subclass == "College of Glamour Bard":
        if subclass == "College of Lore Bard":
        if subclass == "College of the Road Bard":
        if subclass == "College of Satire Bard":
        if subclass == "College of Spirits Bard":
        if subclass == "College of Swords Bard":
        if subclass == "College of Tragedy Bard":
        if subclass == "College of Valor Bard":
        if subclass == "College of Whispers Bards":        
    if Class == "Cleric":
        if param == "Y":
            clerlvl = int(input(f"Given your player level of {plLvl}, what is your Cleric level? "))        
        if subclass == "Arcana Domain Cleric":
        if subclass == "Blood Domain Cleric":
        if subclass == "Commmunity Domain Cleric":
        if subclass == "Death Domain Cleric":
        if subclass == "Forge Domain Cleric":
        if subclass == "Grave Domain Cleric":
        if subclass == "Knowledge Domain Cleric":
        if subclass == "Life Domain Cleric":
        if subclass == "Light Domain Cleric":
        if subclass == "Moon Domain Cleric":
        if subclass == "Nature Domain Cleric":
        if subclass == "Night Domain Cleric":
        if subclass == "Order Domain Cleric":
        if subclass == "Peace Domain Cleric":
        if subclass == "Tempest Domain Cleric":
        if subclass == "Trickery Domain Cleric":
        if subclass == "Twilight Domain Cleric":
        if subclass == "War Domain Cleric":
        if subclass == "Zeal Domain Cleric":        
    if Class == "Druid":
        if param == "Y":
            drulvl = int(input(f"Given your player level of {plLvl}, what is your Druid level? "))        
        if subclass == "Circle of the Blighted Druid":
        if subclass == "Circle of Dreams Druid":
        if subclass == "Circle of the Land Druid":
        if subclass == "Circle of the Moon Druid":
        if subclass == "Circle of the Sheppard Druid":
        if subclass == "Circle of Spores Druid":
        if subclass == "Circle of the Stars Druid":
        if subclass == "Circle of Wildfire Druid":        
    if Class == "Fighter":
        if param == "Y":
            figlvl = int(input(f"Given your player level of {plLvl}, what is your Fighter level? "))        
        if subclass == "Arcane Archer Archetype Fighter":
        if subclass == "Battle Master Archetype Fighter":
        if subclass == "Cavalier Archetype Fighter":
        if subclass == "Champion Archetype Fighter":
        if subclass == "Echo Knight Archetype Fighter":
        if subclass == "Eldrich Knight Archetype Fighter":
        if subclass == "Psi Warrior Archetype Fighter":
        if subclass == "Purple Dragon Knight Archetype Fighter":
        if subclass == "Rune Knight Archetype Fighter":
        if subclass == "Samurai Archetype Fighter":
        if subclass == "Scofflaw Archetype Fighter":        
    if Class == "Monk":
        if param == "Y":
            monklvl = int(input(f"Given your player level of {plLvl}, what is your Monk level? "))        
        if subclass == "Way of the Ascendant Dragon Monk":
            ADO1 = "You honed your abilities by aligning your spirit with a dragon's world-altering power."
            ADO2 = "A dragon personally took an active role in shaping your inner energy."
            ADO3 = "You studied at a monastery that traces its teachings back centuries or more to a single dragon's instruction, or one that is devoted to a dragon god."
            ADO4 = "You spent long stretches meditating in the region around an ancient dragon's lair, absorbing that lair's ambient magic."
            ADO5 = "You found a scroll written in Draconic that contained inspiring new techniques."
            ADO6 = "After a dream featuring a five-handed dragonborn, you awoke with the mystical breath of dragons."
            ADO = [ADO1, ADO2, ADO3, ADO4, ADO5, ADO6]
            AscenDragOrigin = random.choice(ADO)
            ClassNotes.append(f"As a Way of the Ascendant Dragon Monk, your Ascendant Origin: {AscenDragOrigin}")              
        if subclass == "Way of the Astral Self Monk":
        if subclass == "Way of the Cobalt Soul Monk":
        if subclass == "Way of the Drunken Master Monk":
        if subclass == "Way of the Four Elements Monk":
        if subclass == "Way of the Kensei Monk":
        if subclass == "Way of the Long Death Monk":
        if subclass == "Way of Mercy Monk":
        if subclass == "Way of the Open Hand Monk":
        if subclass == "Way of the Shadow Monk":
        if subclass == "Way of the Sun Soul Monk":        
    if Class == "Paladin":
        if param == "Y":
            pallvl = int(input(f"Given your player level of {plLvl}, what is your Paladin level? "))        
        if subclass == "Oath of the Ancients Paladin":
        if subclass == "Oath of Conquest Paladin":
        if subclass == "Oath of the Crown Paladin":
        if subclass == "Oath of Devotion Paladin":
        if subclass == "Oath of Glory Paladin":
        if subclass == "Oath of the Open Sea Paladin":
        if subclass == "Oath of Redemption Paladin":
        if subclass == "Oath of the Watchers Paladin":
        if subclass == "Oath of Vengeance Paladin":
        if subclass == "Oathbreaker Paladin":        
    if Class == "Ranger":
        if param == "Y":
            ranlvl = int(input(f"Given your player level of {plLvl}, what is your Ranger level? "))        
        if subclass == "Beast Master Archetype Ranger":
        if subclass == "Drakewarden Ranger":
            DWO1 = "You studied a dragon's scale or claw, or a trinket from a dragon's hoard, creating your bond through that token's lingering draconic magic."
            DWO2 = "A secret order of rangers who collect and guard draconic lore taught you their ways."
            DWO3 = "A dragon gave you a geode or gemstone to care for. To your surprise, the drake hatched from that stone."
            DWO4 = "You ingested a few drops of dragon blood, forever infusing your nature magic with draconic power."
            DWO5 = "An ancient Draconic inscription on a standing stone empowered you when you read it aloud."
            DWO6 = "You had a vivid dream of a mysterious figure accompanied by seven yellow canaries, who warned you of impending doom. When you awoke, your drake was there, watching you."
            DWO = [DWO1, DWO2, DWO3, DWO4, DWO5, DWO6]
            DrakewardenOrigin = random.choice(DWO)
            ClassNotes.append(f"As a Drakewarden Ranger, your Drakewarden Origin: {DrakewardenOrigin}")               
        if subclass == "Fey Wanderer Archetype Ranger":
        if subclass == "Gloom Stalker Archetype Ranger":
        if subclass == "Horizon Walker Archetype Ranger":
        if subclass == "Hunter Archetype Ranger":
        if subclass == "Monster Slayer Archetype Ranger":
        if subclass == "Shooting Star Archetype Ranger":
        if subclass == "Swarmkeeper Archetype Ranger":        
    if Class == "Rogue":
        if param == "Y":
            roglvl = int(input(f"Given your player level of {plLvl}, what is your Rogue level? "))        
        if subclass == "Arcane Trickster Archetype Rogue":
        if subclass == "Assassin Archetype Rogue":
        if subclass == "Inquisitive Archetype Rogue":
        if subclass == "Mastermind Archetype Rogue":
        if subclass == "Mountebank Archetype Rogue":
        if subclass == "Phantom Archetype Rogue":
        if subclass == "Scout Archetype Rogue":
        if subclass == "Soulknife Archetype Rogue":
        if subclass == "Swashbuckler Archetype Rogue":
        if subclass == "Thief Archetype Rogue":        
    if Class == "Sorcerer":
        if param == "Y":
            sorclvl = int(input(f"Given your player level of {plLvl}, what is your Sorcerer level? "))        
        if subclass == "Aberrant Mind Origin Sorcerer":
            AbSO1 = "You were exposed to the Far Realm's warping influence. You are confinced that a tentacle is now growing on you, but no one else can see it."
            AbSO2 = "A psychic wind from the Astral Plane carried psionic energy to you. When you use your powers, faint motes of light sparkle around you."
            AbSO3 = "You once suffered the dominating powers of an aboleth, leaving a psychic splinter in your mind."
            AbSO4 = "You were implanted with a mind flayer tadpole, but the ceremorphosis never completed. And now its psionic power is yours. When you use it, your flesh shines with a strange mucus."
            AbSO5 = "As a child, you had an imaginary friend that looked like a flumph or a strange platypus-like creature. One day, it gifted you with psionic powers, which have ended up being not so imaginary."
            AbSO6 = "Your nightmares whisper the truth to you: your psionic powers are not your own. You draw them from your parasitic twin."
            AbSO = [AbSO1, AbSO2, AbSO3, AbSO4, AbSO5, AbSO6]
            AberrantOrigin = random.choice(AbSO)
            ClassNotes.append(f"As an Aberrant Mind Origin Sorcerer, the Aberrant Origin is {AberrantOrigin}")             
        if subclass == "Clockwork Soul Origin Sorcerer":
        if subclass == "Divine Soul Origin Sorcerer":
        if subclass == "Draconic Bloodline Origin Sorcerer":
        if subclass == "Lunar Magic Origin Sorcerer":
        if subclass == "Phoenix Origin Sorcerer":
        if subclass == "Runechild Origin Sorcerer":
        if subclass == "Sea Origin Sorcerer":
        if subclass == "Shadow Origin Sorcerer":
        if subclass == "Stone Origin Sorcerer":
        if subclass == "Storm Origin Sorcerer":  
        if subclass == "Wild Magic Origin Sorcerer":                  
    if Class == "Warlock":   
        if param == "Y":
            warlvl = int(input(f"Given your player level of {plLvl}, what is your Warlock level? "))          
        if subclass == "Ancient Dragon Patron Warlock":
        if subclass == "Archfey Patron Warlock":
        if subclass == "Celestial Patron Warlock":
        if subclass == "The Fathomless Patron Warlock":
        if subclass == "Fiend Patron Warlock":
        if subclass == "The Genie Patron Warlock":
            GenK1 = "Dao, or Earth Genie"
            GenK2 = "Djinni, or Air Genie"
            GenK3 = "Efreeti, or Fire Genie"
            GenK4 = "Marid, or Water Genie"
            GenK = [GenK1, GenK2, GenK3, GenK4]
            GenieKind = random.choice(GenK)
            ClassNotes.append(f"As a Genie Patron Warlock, your Genie is a(n): {GenieKind}")                  
        if subclass == "Great Old One Patron Warlock":
        if subclass == "Hexblade Patron Warlock":
        if subclass == "Mysterious Feline Patron Warlock":
        if subclass == "Queen of Spiders Patron Warlock":
        if subclass == "Raven Queen Patron Warlock":
        if subclass == "Serpent Patron Warlock":         
    if Class == "Wizard":
        if param == "Y":
            wizlvl = int(input(f"Given your player level of {plLvl}, what is your Wizard level? "))        
        if subclass == "Undead Patron Warlock":
        if subclass == "Undying Patron Warlock":
        if subclass == "Abjuration Arcane Tradition Wizard":
        if subclass == "Bladesinging Arcane Tradition Wizard":
        if subclass == "Blood Magic Arcane Tradition Wizard":
        if subclass == "Chronurgy Magic Wizard":
        if subclass == "Conjuration Arcane Tradition Wizard":
        if subclass == "Divination Arcane Tradition Wizard":
        if subclass == "Enchantment Arcane Tradition Wizard":
        if subclass == "Evocation Arcane Tradition Wizard":
        if subclass == "Graviturgy Magic Wizard":
        if subclass == "Illusion Arcane Tradition Wizard":
        if subclass == "Necromancy Arcane Tradition Wizard":
        if subclass == "Order of Scribes Arcane Tradition Wizard":
        if subclass == "Transmutation Arcane Tradition Wizard":
        if subclass == "War Arcane Tradition Wizard":






    return Class, subclass, ClassNotes
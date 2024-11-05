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
ChainMail = "Chain Mail"
RingMail = "Ring Mail"
Plate = "Plate"
Splint = "Splint"
HeavyArmor = [ChainMail, RingMail, Plate, Splint]
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

def dndchargen_characterbuilder(param, plLvl, Class, subclass, submulticlass, BGL, EQP, SkillsProf, PlProf, Notes, data):
    poollevel = plLvl
    ClassNotes = []
    ClassLvl = []
    SpellcastingClass = []
    SpellcastingAbility = []
    SpellsaveDC = []
    SpellAttackMod = []
    hitdice = []
    hitpoints = 0

    ProfBonus = int(data['ProfBonus'])
    ChaMod = int(data['CHamod'])
    ConMod = int(data['CONmod'])
    DexMod = int(data['DEXmod '])
    IntMod = int(data['INTmod'])
    StrMod = int(data['STRmod'])
    WisMod = int(data['WISmod'])
    if plLvl >= 4:
        ClassNotes.append("You can increase one score by 2, two by one, or a feat. As normal, you can't increase an ability score above 20 using this feature.")
    if plLvl >= 8:
        ClassNotes.append("You can increase one score by 2, two by one, or a feat. As normal, you can't increase an ability score above 20 using this feature.")    
    if plLvl >= 12:
        ClassNotes.append("You can increase one score by 2, two by one, or a feat. As normal, you can't increase an ability score above 20 using this feature.")    
    if plLvl >= 16:
        ClassNotes.append("You can increase one score by 2, two by one, or a feat. As normal, you can't increase an ability score above 20 using this feature.")        
    if plLvl >= 19:
        ClassNotes.append("You can increase one score by 2, two by one, or a feat. As normal, you can't increase an ability score above 20 using this feature.")    
    for i in range(len(Class)):
        if Class[i] == "Artificer":
            if ((param == "N") or (submulticlass == "N")):
                artlvl = plLvl
                ClassLvl.append(artlvl)            
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:
                    artlvl = int(input(f"Given your pool of levels of {poollevel}, What is your Artificer level? "))
                    if artlvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")
                poollevel = poollevel - artlvl
                ClassLvl.append(artlvl)
            if artlvl >= 1:
                hitdice.append(f"{artlvl}d8 for {Class[i]}")
                if artlvl == 1:
                    hitpoints += (8 + ConMod)
                else:
                    hitpoints += (8 + ConMod + hpcalc(artlvl, d8))
                PlProf.extend(LightArmor)
                PlProf.extend(MediumArmor)
                PlProf.append(Shield)
                PlProf.extend(SimpleWeapons)
                PlProf.append(ThievKit)
                PlProf.append(TinkTools)
                PlProf = artisantools(param, PlProf)
                SkillsProf.append(ConST)
                SkillsProf.append(IntST)
                ArtSkillsList = [Arcana, History, Investigation, Medicine, Nature, Perception, SleightofHand]
                SkillsProf = twoskillsfromlist(param, SkillsProf, ArtSkillsList)
                ArtChoices = ["Starting Equipment", "Gold"]
                ArtChoices2 = ["Studded Leather Armor", "Scale Mail"]
                if i == 0:
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
                ClassNotes.append("Magical Tinkering (see notes)")
                Notes.append("Magical Tinkering - You learn how to invest a spark of magic into mundane objects. To use this ability, you must have tinker's tools or other artisan's tools in hand. You then touch a Tiny nonmagical object as an action and give it one of the following magical properties of your choice:\n - The object sheds bright light in a 5-foot radius and dim light for an additional 5 feet \n - Whenever tapped by a creature, the object emits a recorded message that can be heard up to 10 feet away \n - You utter the message when you bestow this property on the object, and the recording can be no more than 6 seconds long \n - The object continuously emits your choice of an odor or a nonverbal sound (wind, waves, chirping, or the like). The chosen phenomenon is perceivable up to 10 feet away \n - A static visual effect appears on one of the object's surfaces. This effect can be a picture, up to 25 words of text, lines and shapes, or a mixture of these elements, as you like. \n The chosen property lasts indefinitely. As an action, you can touch the object and end the property early. \n You can bestow magic on multiple objects, touching one object each time you use this feature, though a single object can only bear one property at a time. The maximum number of objects you can affect with this feature at one time is equal to your Intelligence modifier (minimum of one object). If you try to exceed your maximum, the oldest property immediately ends, and then the new property applies.")
                SpellcastingClass.append("Artificer")
                SpellcastingAbility.append("Int")
                SpellsaveDC.append(8 + ProfBonus + IntMod)
                SpellAttackMod.append(ProfBonus + IntMod)
                ArtCantripsKnown = 2
                ArtSpellSlot1 = 0
                ArtSpellSlot2 = 0
                ArtSpellSlot3 = 0
                ArtSpellSlot4 = 0
                ArtSpellSlot5 = 0
            if artlvl >= 2:
                ClassNotes.append("Infuse Item (see notes)")
                Notes.append("Infuse Item - You have the ability to imbue mundane items with certain magical infusions. The magic items you create with this feature are effectively prototypes of permanent items. You learn additional infusions of your choice when you reach certain levels in this class.\nWhenever you gain a level in this class, you can replace one of the artificer infusions you learned with a new one.")
                InfusionNumber = 4
                InfusedItem = 2
                ClassNotes.append("Infusing an Item (see notes)")
                Notes.append("Infusing an Item - Whenever you finish a long rest, you can touch a nonmagical object and imbue it with one of your artificer infusions, turning it into a magic item. An infusion works on only certain kinds of objects, as specified in the infusion's description. If the item requires attunement, you can attune yourself to it the instant you infuse the item. If you decide to attune to the item later, you must do so using the normal process for attunement (see 'Attunement' in chapter 7 of the Dungeon Master's Guide).\nYour infusion remains in an item indefinitely, but when you die, the infusion vanishes after a number of days have passed equal to your Intelligence modifier (minimum of 1 day). The infusion also vanishes if you give up your knowledge of the infusion for another one.\nYou can infuse more than one nonmagical object at the end of a long rest; the maximum number of objects appears in the Infused Items column of the Artificer table. You must touch each of the objects, and each of your infusions can be in only one object at a time. Moreover, no object can bear more than one of your infusions at a time. If you try to exceed your maximum number of infusions, the oldest infusion immediately ends, and then the new infusion applies.")
                ArtSpellSlot1 = 2
            if artlvl >= 3:
                ClassNotes.append("The Right Tool For The Job (see notes)")
                Notes.append("The Right Tool For The Job - You learn how to produce exactly the tool you need: with tinker's tools in hand, you can magically create one set of artisan's tools in an unoccupied space within 5 feet of you. This creation requires 1 hour of uninterrupted work, which can coincide with a short or long rest. Though the product of magic, the tools are nonmagical, and they vanish when you use this feature again.")
                Arti = ["Alchemist Specialist Artificer", "Armorer Specialist Artificer", "Artilierist Specialist Artificer", "Battle Smith Specialist Artificer"]
                if subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Alchemist Specialist Artificer")
                        print("2 - Armorer Specialist Artificer")
                        print("3 - Artilierist Specialist Artificer")
                        print("4 - Battle Smith Specialist Artificer")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 1:
                            subclass[i] = "Alchemist Specialist Artificer"
                        if subc == 2:
                            subclass[i] = "Armorer Specialist Artificer"
                        if subc == 3:
                            subclass[i] = "Artilierist Specialist Artificer"
                        if subc == 4:
                            subclass[i] = "Battle Smith Specialist Artificer"
                        if subc == 0:
                            subclass[i] = random.choice(Arti)
                    if param == "N":
                        subclass[i] = random.choice(Arti)
                if subclass[i] == "Alchemist Specialist Artificer":
                    if AlchSupp in PlProf:
                        print(f"You already know {AlchSupp}, please select a different tool to be proficient in.")
                        PlProf = artisantools(param, PlProf)
                    else:
                        PlProf.append(AlchSupp)
                    ClassNotes.append("Alchemist Spells (see notes)")
                    Notes.append("Alchemist Spells - You always have certain spells prepared after you reach particular levels in this class, as shown in the Alchemist Spells table. These spells count as artificer spells for you, but they don't count against the number of artificer spells you prepare.\n3rd Artificer Level: Healing Word, Ray of Sickness\n5th Artificer Level: Flaming Sphere, Melf's Acid Arrow\n9th Artificer Level: Gaseous Form, Mass Healing Word\n13th Artificer Level: Blight, Death Ward\n17th Artificer Level: Cloudkill, Raise Dead")
                    ClassNotes.append("Experimental Elixer (see notes)")
                    Notes.append("Experimental Elixer - Whenever you finish a long rest, you can magically produce an experimental elixir in an empty flask you touch. Roll on the Experimental Elixir table for the elixir's effect, which is triggered when someone drinks the elixir. As an action, a creature can drink the elixir or administer it to an incapacitated creature.\nCreating an experimental elixir requires you to have alchemist supplies on your person, and any elixir you create with this feature lasts until it is drunk or until the end of your next long rest.\nWhen you reach certain levels in this class, you can make more elixirs at the end of a long rest, roll for each elixir's effect separately. Each elixir requires its own flask.\nYou can create additional experimental elixirs by expending a spell slot of 1st level or higher for each one. When you do so, you use your action to create the elixir in an empty flask you touch, and you choose the elixir's effect from the Experimental Elixir table.")
                    ArtElixers = 1
                    if artlvl >= 5:
                        ClassNotes.append("Alchemical Savant (see notes)")
                        Notes.append("Alchemical Savant - You develop masterful command of magical chemicals, enhancing the healing and damage you create through them. Whenever you cast a spell using your alchemist's supplies as the spellcasting focus, you gain a bonus to one roll of the spell. That roll must restore hit points or be a damage roll that deals acid, fire, necrotic, or poison damage, and the bonus equals your Intelligence modifier (minimum of +1).")
                    if artlvl >= 6:
                        ArtElixers = 2
                    if artlvl >= 9:
                        ClassNotes.append("Restorative Reagents (see notes)")
                        Notes.append("Restorative Reagents - You can incorporate restorative reagents into some of your works:\nWhenever a creature drinks an experimental elixir you created, the creature gains temporary hit points equal to 2d6 + your Intelligence modifier (minimum of 1 temporary hit point).\nYou can cast Lesser Restoration without expending a spell slot and without preparing the spell, provided you use alchemist's supplies as the spellcasting focus.\nYou can do so a number of times equal to your Intelligence modifier (minimum of once), and you regain all expended uses when you finish a long rest.")
                    if artlvl >= 15:
                        ArtElixers = 3
                        ClassNotes.append("Chemical Mastery (see notes)")
                        Notes.append("Chemical Mastery - You have been exposed to so many chemicals that they pose little risk to you, and you can use them to quickly end certain ailments:\nYou gain resistance to acid damage and poison damage, and you are immune to the poisoned condition.\nYou can cast Greater Restoration and Heal without expending a spell slot, without preparing the spell, and without material components, provided you use alchemist's supplies as the spellcasting focus.\nOnce you cast either spell with this feature, you can't cast that spell with it again until you finish a long rest.")
                    ClassNotes.append(f"You can produce {ArtElixers} elixer(s), rolling on the Experimental Elixer table.")
                if subclass[i] == "Armorer Specialist Artificer":
                    PlProf.extend(HeavyArmor)
                    if SmthTools in PlProf:
                        print(f"You already know {SmthTools}, please select a different tool to be proficient in.")
                        PlProf = artisantools(param, PlProf)
                    else:
                        PlProf.append(SmthTools)
                    ClassNotes.append("Armorer Spells (see notes")
                    Notes.append("Armorer Spells - You always have certain spells prepared after you reach particular levels in this class, as shown in the Armorer Spells table. These spells count as artificer spells for you, but they don't count against the number of artificer spells you prepare.\n3rd Artificer Level: Magic Missile, Thunderwave\n5th Artificer Level: Mirror Image, Shatter\n9th Artificer Level: Hypnotic Pattern, Lightning Bolt\n13th Artificer Level: Fire Shield, Greater Invisibility\n17th Artificer Level: Passwall, Wall of Force")
                    ClassNotes.append("Arcane Armor (see notes)")
                    Notes.append("Your metallurgical pursuits have led to you making armor a conduit for your magic. As an action, you can turn a suit of armor you are wearing into Arcane Armor, provided you have smith's tools in hand.\nYou gain the following benefits while wearing this armor:\nIf the armor normally has a Strength requirement, the arcane armor lacks this requirement for you.\nYou can use the arcane armor as a spellcasting focus for your artificer spells.\nThe armor attaches to you and can't be removed against your will. It also expands to cover your entire body, although you can retract or deploy the helmet as a bonus action. The armor replaces any missing limbs, functioning identically to a limb it replaces.\nYou can doff or don the armor as an action.\nThe armor continues to be Arcane Armor until you don another suit of armor or you die.")
                    ClassNotes.append("Armor Model (see notes)")
                    Notes.append("Armor Model - You can customize your Arcane Armor. When you do so, choose one of the following armor models: Guardian or Infiltrator. The model you choose gives you special benefits while you wear it.\nEach model includes a special weapon. When you attack with that weapon, you can add your Intelligence modifier, instead of Strength or Dexterity, to the attack and damage rolls.\nYou can change the armor's model whenever you finish a short or long rest, provided you have smith's tools in hand.\nGuardian:\nYou design your armor to be in the front line of conflict. It has the following features:\nThunder Gauntlets. Each of the armor's gauntlets counts as a simple melee weapon while you aren't holding anything in it, and it deals 1d8 thunder damage on a hit. A creature hit by the gauntlet has disadvantage on attack rolls against targets other than you until the start of your next turn, as the armor magically emits a distracting pulse when the creature attacks someone else.\nDefensive Field. As a bonus action, you can gain temporary hit points equal to your level in this class, replacing any temporary hit points you already have. You lose these temporary hit points if you doff the armor. You can use this bonus action a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.\nInfiltrator:\nYou customize your armor for subtle undertakings. It has the following features:\nLightning Launcher. A gemlike node appears on one of your armored fists or on the chest (your choice). It counts as a simple ranged weapon, with a normal range of 90 feet and a long range of 300 feet. and it deals 1d6 lightning damage on a hit. Once on each of your turns when you hit a creature with it, you can deal an extra 1d6 lightning damage to that target.\nPowered Steps. Your walking speed increases by 5 feet.\nDampening Field. You have advantage on Dexterity (Stealth) checks. If the armor normally imposes disadvantage on such checks, the advantage and disadvantage cancel each other, as normal.")
                    if artlvl >= 5:
                        ClassNotes.append("Extra Attack - You can attack twice, rather than once, whenever you take the Attack action on your turn.")
                    if artlvl >= 9:
                        ClassNotes.append("Armor Modifications (see notes)")
                        Notes.append("Armor Modifications - You learn how to use your artificer infusions to specially modify your Arcane Armor. That armor now counts as separate items for the purposes of your Infuse Items feature: armor (the chest piece), boots, helmet, and the armor's special weapon. Each of those items can bear one of your infusions, and the infusions transfer over if you change your armor's model with the Armor Model feature. In addition, the maximum number of items you can infuse at once increases by 2, but those extra items must be part of your Arcane Armor.")
                    if artlvl >= 15:
                        ClassNotes.append("Perfected Armor - Your Arcane Armor gains additional benefits based on its model. (see notes)")
                        Notes.append("Perfected Armor - Your Arcane Armor gains additional benefits based on its model, as shown below.\nGuardian. When a Huge or smaller creature you can see ends its turn within 30 feet of you, you can use your reaction to magically force the creature to make a Strength saving throw against your spell save DC, pulling the creature up to 30 feet toward you to an unoccupied space. If you pull the target to a space within 5 feet of you, you can make a melee weapon attack against it as part of this reaction. You can use this reaction a number of times equal to your proficiency bonus, and you regain all expended uses of it when you finish a long rest.\nInfiltrator. Any creature that takes lightning damage from your Lightning Launcher glimmers with magical light until the start of your next turn. The glimmering creature sheds dim light in a 5-foot radius, and it has disadvantage on attack rolls against you, as the light jolts it if it attacks you. In addition, the next attack roll against it has advantage, and if that attack hits, the target takes an extra 1d6 lightning damage.")
                if subclass[i] == "Artilierist Specialist Artificer":
                    if WdcrvTools in PlProf:
                        print(f"You already know {WdcrvTools}, please select a different tool to be proficient in.")
                        PlProf = artisantools(param, PlProf)
                    else:
                        PlProf.append(WdcrvTools)
                    ClassNotes.append("Artilierist Spells (see notes")
                    Notes.append("Artilierist Spells - You always have certain spells prepared after you reach particular levels in this class, as shown in the Artillerist Spells table. These spells count as artificer spells for you, but they don't count against the number of artificer spells you prepare.\n3rd Artificer Level: Shield, Thunderwave\n5th Artificer Level: Scorching Ray, Shatter\n9th Artificer Level: Fireball, Wind Wall\n13th Artificer Level: Ice Storm, Wall of Fire\n17th Artificer Level: Cone of Cold, Wall of Force")
                    ClassNotes.append("Eldritch Cannon (see notes)")
                    Notes.append("Eldritch Cannon - You learn how to create a magical cannon. Using woodcarver's tools or smith's tools, you can take an action to magically create a Small or Tiny eldritch cannon in an unoccupied space on a horizontal surface within 5 feet of you. A Small eldritch cannon occupies its space, and a Tiny one can be held in one hand.\nOnce you create a cannon, you can't do so again until you finish a long rest or until you expend a spell slot of 1st level or higher. You can have only one cannon at a time and can't create one while your cannon is present.\nThe cannon is a magical object. Regardless of size, the cannon has an AC of 18 and a number of hit points equal to five times your artificer level. It is immune to poison damage, psychic damage, and all conditions. If it is forced to make an ability check or a saving throw, treat all its ability scores as 10 (+0). If the Mending spell is cast on it, it regains 2d6 hit points. It disappears if it is reduced to 0 hit points or after 1 hour. You can dismiss it early as an action.\nWhen you create the cannon, you determine its appearance and whether it has legs. You also decide which type it is, choosing from the options on the Eldritch Cannons table. On each of your turns, you can take a bonus action to cause the cannon to activate if you are within 60 feet of it. As part of the same bonus action, you can direct the cannon to walk or climb up to 15 feet to an unoccupied space, provided it has legs.\nFlamethrower: The cannon exhales fire in an adjacent 15-foot cone that you designate. Each creature in that area must make a Dexterity saving throw against your spell save DC, taking 2d8 fire damage on a failed save or half as much damage on a successful one. The fire ignites any flammable objects in the area that aren't being worn or carried.\nForce Ballista: Make a ranged spell attack, originating from the cannon, at one creature or object within 120 feet of it. On a hit, the target takes 2d8 force damage, and if the target is a creature, it is pushed up to 5 feet away from the cannon.\nProtector: The cannon emits a burst of positive energy that grants itself and each creature of your choice with in 10 feet of it a number of temporary hit points equal to 1d8 + your Intelligence modifier (minimum of +1).")
                    if plLvl >= 5:
                        ClassNotes.append("Arcane Firearm (see notes)")
                        Notes.append("Arcane Firearm - You know how to turn a wand, staff, or rod into an arcane firearm, a conduit for your destructive spells. When you finish a long rest, you can use woodcarver's tools to carve special sigils into a wand, staff, or rod and thereby turn it into your arcane firearm. The sigils disappear from the object if you later carve them on a different item. The sigils otherwise last indefinitely.\nYou can use your arcane firearm as a spellcasting focus for your artificer spells. When you cast an artificer spell through the firearm, roll a d8, and you gain a bonus to one of the spell's damage rolls equal to the number rolled.")
                    if plLvl >= 9:
                        ClassNotes.append("Explosive Cannon (see notes)")
                        Notes.append("Explosive Cannon - Every eldritch cannon you create is more destructive:\nThe cannon's damage rolls all increase by 1d8.\nAs an action, you can command the cannon to detonate if you are within 60 feet of it. Doing so destroys the cannon and forces each creature within 20 feet of it to make a Dexterity saving throw against your spell save DC, taking 3d8 force damage on a failed save or half as much damage on a successful one.")
                    if plLvl >= 15:
                        ClassNotes.append("Fortified Position (see notes)")
                        Notes.append("Fortified Position - You're a master at forming well-defended emplacements using Eldritch Cannon:\nYou and your allies have half cover while within 10 feet of a cannon you create with Eldritch Cannon, as a result of a shimmering field of magical protection that the cannon emits.\nYou can now have two cannons at the same time. You can create two with the same action (but not the same spell slot), and you can activate both of them with the same bonus action. You determine whether the cannons are identical to each other or different. You can't create a third cannon while you have two.")
                if subclass[i] == "Battle Smith Specialist Artificer":        
                    if SmthTools in PlProf:
                        print(f"You already know {SmthTools}, please select a different tool to be proficient in.")
                        PlProf = artisantools(param, PlProf)
                    else:
                        PlProf.append(SmthTools)
                    ClassNotes.append("Battle Smith Spells (see notes")
                    Notes.append("Battle Smith Spells - You always have certain spells prepared after you reach particular levels in this class, as shown in the Battle Smith Spells table. These spells count as artificer spells for you, but they don't count against the number of artificer spells you prepare.\n3rd Artificer Level: Heroism, Shield\n5th Artificer Level: Branding Smite, Warding Bond\n9th Artificer Level: Aura of Vitality, Conjure Barrage\n13th Artificer Level: Aura of Purity, Fire Shield\n17th Artificer Level: Banishing Smite, Mass Cure Wounds")
                    PlProf.extend(MartialWeapons)
                    ClassNotes.append("Battle Ready (see notes)")
                    Notes.append("Battle Ready - Your combat training and your experiments with magic have paid off in two ways:\nYou gain proficiency with martial weapons (already in Proficiences).\nWhen you attack with a magic weapon, you can use your Intelligence modifier, instead of Strength or Dexterity modifier, for the attack and damage rolls.")
                    ClassNotes.append("Steel Defender (see notes)")
                    Notes.append("Steel Defender - Your tinkering has borne you a faithful companion, a Steel Defender. It is friendly to you and your companions, and it obeys your commands. See this creature's game statistics in the steel defender stat block. You determine the creature's appearance and whether it has two legs or four; your choice has no effect on its game statistics.\nIn combat, the steel defender shares your initiative count, but it takes its turn immediately after yours. It can move and use its reaction on its own, but the only action it takes on its turn is the Dodge action, unless you take a bonus action on your turn to command it to take one of the actions in its stat block or the Dash, Disengage, Help, Hide, or Search action.\nIf the mending spell is cast on it, it regains 2d6 hit points. If it has died within the last hour, you can use your smith's tools as an action to revive it, provided you are within 5 feet of it and you expend a spell slot of 1st level or higher. The steel defender returns to life after 1 minute with all its hit points restored.\nAt the end of a long rest, you can create a new steel defender if you have your smith's tools with you. If you already have a steel defender from this feature, the first one immediately perishes.")
                    if artlvl >= 5:
                        ClassNotes.append("Extra Attack - You can attack twice, rather than once, whenever you take the Attack action on your turn.")
                    if artlvl >= 9:
                        ClassNotes.append("Arcane Jolt (see notes)")
                        Notes.append("Arcane Jolt - You learn new ways to channel arcane energy to harm or heal. When either you hit a target with a magic weapon attack or your steel defender hits a target, you can channel magical energy through the strike to create one of the following effects:\nThe target takes an extra 2d6 force damage.\nChoose one creature or object you can see within 30 feet of the target. Healing energy flows into the chosen recipient, restoring 2d6 hit points to it. You can use this energy a number of times equal to your Intelligence modifier (minimum of once), but you can do so no more than once on a turn. You regain all expended uses when you finish a long rest.")
                    if artlvl >= 15:
                        ClassNotes.append("Improved Defender (see notes)")
                        Notes.append("Improved Defender - Your Arcane jolt and Steel Defender become more powerful:\nThe extra damage and the healing of your Arcane jolt both increase to 4d6.\nYour steel defender gains a +2 bonus to Armor Class.\nWhenever your steel defender uses its Deflect Attack, the attacker takes force damage equal to 1d4 + your Intelligence modifier.")
                ArtSpellSlot1 = 3
            if artlvl >= 5:
                ArtSpellSlot1 = 4
                ArtSpellSlot2 = 2
            if artlvl >= 6:
                ClassNotes.append("Tool Expertise - Your proficiency bonus is doubled for any ability check you make that uses your proficiency with a tool.")
                InfusionNumber = 6
                InfusedItem = 3
            if artlvl >= 7:
                ClassNotes.append("Flash Of Genius (see notes)")
                Notes.append("Flash Of Genius - You gain the ability to come up with solutions under pressure. When you or another creature you can see within 30 feet of you makes an ability check or a saving throw, you can use your reaction to add your Intelligence modifier to the roll.\nYou can use this feature a number of times equal to your Intelligence modifier (minimum of once). You regain all expended uses when you finish a long rest.")
                ArtSpellSlot2 = 3
            if artlvl >= 9:
                ArtSpellSlot3 = 2
            if artlvl >= 10:
                ClassNotes.append("Magic Item Adept - You achieve a profound understanding of how to use and make magic items:\nYou can attune to up to four magic items at once.\nIf you craft a magic item with a rarity of common or uncommon, it takes you a quarter of the normal time, and it costs you half as much of the usual gold.")
                InfusionNumber = 8
                InfusedItem = 4
                ArtCantripsKnown = 3
            if artlvl >= 11:
                ClassNotes.append("Spell-Storing Item (see notes)")
                Notes.append("Spell-Storing Item - You learn how to store a spell in an object. Whenever you finish a long rest, you can touch one simple or martial weapon or one item that you can use as a spellcasting focus, and you store a spell in it, choosing a 1st- or 2nd-level spell from the artificer spell list that requires 1 action to cast (you needn't have it prepared).\nWhile holding the object, a creature can take an action to produce the spell's effect from it, using your spellcasting ability modifier. If the spell requires concentration, the creature must concentrate. The spell stays in the object until it's been used a number of times equal to twice your Intelligence modifier (minimum of twice) or until you use this feature again to store a spell in an object.")
                ArtSpellSlot3 = 3
            if artlvl >= 14:
                ClassNotes.append("Magic Item Savant - Your skill with magic items deepens more: You can attune to up to five magic items at once. You ignore all class, race, spell, and level requirements on attuning to or using a magic item.")
                InfusionNumber = 10
                InfusedItem = 5
                ArtCantripsKnown = 4
            if artlvl >= 15:
                ArtSpellSlot4 = 2
            if artlvl >= 17:
                ArtSpellSlot4 = 3
                ArtSpellSlot5 = 1
            if artlvl >= 18:
                ClassNotes.append("Magic Item Master - You can attune to up to six magic items at once.")
                InfusionNumber = 12
                InfusedItem = 6
            if artlvl >= 19:
                ArtSpellSlot5 = 2
            if artlvl == 20:
                ClassNotes.append("Soul Of Artifice (see notes)")
                Notes.append("Soul Of Artifice - You develop a mystical connection to your magic items, which you can draw on for protection:\nYou gain a +1 bonus to all saving throws per magic item you are currently attuned to.\nIf you're reduced to 0 hit points but not killed outright, you can use your reaction to end one of your artificer infusions, causing you to drop to 1 hit point instead of 0.")
            ClassNotes.append(f"You know {InfusionNumber} infusions and can infuse {InfusedItem} items.")
            ClassNotes.append(f"Spells known: \nArtificer Cantrips: {ArtCantripsKnown}\nArtificer 1st Level Spell Slots: {ArtSpellSlot1}\nArtificer 2nd Level Spell Slots: {ArtSpellSlot2}\nArtificer 3rd Level Spell Slots: {ArtSpellSlot3}\nArtificer 4th Level Spell Slots: {ArtSpellSlot4}\nArtificer 5th Level Spell Slots: {ArtSpellSlot5}")
            #See if I can f-string anything
        if Class[i] == "Barbarian":
            if ((param == "N") or (submulticlass == "N")):
                barblvl = plLvl
                ClassLvl.append(barblvl)              
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    barblvl = int(input(f"Given your pool of levels of {poollevel}, what is your Barbarian level? "))   
                    if barblvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                    
                poollevel = poollevel - barblvl
                ClassLvl.append(barblvl)
            if barblvl >= 1:
                hitdice.append(f"{barblvl}d12 for {Class[i]}")
                if barblvl == 1:
                    hitpoints += (12 + ConMod)
                else:
                    hitpoints += (12 + ConMod + hpcalc(barblvl, d12))
                PlProf.extend(LightArmor)
                PlProf.extend(MediumArmor)
                PlProf.append(Shield)
                PlProf.extend(SimpleWeapons)
                PlProf.extend(MartialWeapons)
                SkillsProf.append(StrST)
                SkillsProf.append(ConST)
                BarbSkillsList = [AnimalHandling, Athletics, Intimidation, Nature, Perception, Survival]
                SkillsProf = twoskillsfromlist(param, SkillsProf, BarbSkillsList)
                StartEquip1 = ["Greataxe", "Martial Melee Weapon"]
                if param == "Y":
                    print("0 - Random")
                    print("1 - Greataxe")
                    print("2 - Martial Melee Weapon")
                    se1 = int(input("What would you like your first choice for starting equipment to be? "))
                    if se1 == 0:
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "Greataxe":
                            EQP.append(Greataxe)
                        if SE1rand == "Martial Melee Weapon":
                            EQP.append(random.choice(MartialWeapons))
                    if se1 == 1:
                        EQP.append(Greataxe)
                    if se1 == 2:
                        print("0 - Random")
                        for i, mw in enumerate(MartialWeapons, 1):
                            print(f"{i} - {mw}")
                        se1mw = int(input("Which martial weapon would you like to add to your inventory? "))
                        if se1mw == 0:
                            EQP.append(random.choice(MartialWeapons))
                        elif 1 <= se1mw <= len(MartialWeapons):
                            EQP.append(MartialWeapons[se1mw-1])
                    
                if param == "N":
                    SE1rand = random.choice(StartEquip1)
                    if SE1rand == "Greataxe":
                        EQP.append(Greataxe)
                    if SE1rand == "Martial Melee Weapon":
                        EQP.append(random.choice(MartialWeapons))


            if barblvl >= 3:
                Barb = ["Path of the Ancestral Guardian Barbarian", "Path of the Battlerager Barbarian", "Path of the Beast Barbarian", "Path of the Berserker Barbarian", "Path of the Giant Barbarian", "Path of the Juggernaut Barbarian", "Path of the Storm Herald Barbarian", "Path of the Totem Warrior Barbarian", "Path of the Zealot Barbarian", "Path of the Wild Magic Barbarian"]            
                if subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Path of the Ancestral Guardian Barbarian")
                        print("2 - Path of the Battlerager Barbarian")
                        print("3 - Path of the Beast Barbarian")
                        print("4 - Path of the Berserker Barbarian")
                        print("5 - Path of the Giant Barbarian")
                        print("6 - Path of the Juggernaut Barbarian")
                        print("7 - Path of the Storm Herald Barbarian")
                        print("8 - Path of the Totem Warrior Barbarian")
                        print("9 - Path of the Wild Magic Barbarian")
                        print("10 - Path of the Zealot Barbarian")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 1:
                            subclass[i] = "Path of the Ancestral Guardian Barbarian"
                        if subc == 2:
                            subclass[i] = "Path of the Battlerager Barbarian"
                        if subc == 3:
                            subclass[i] = "Path of the Beast Barbarian"
                        if subc == 4:
                            subclass[i] = "Path of the Berserker Barbarian"
                        if subc == 5:
                            subclass[i] = "Path of the Giant Barbarian"
                        if subc == 6:
                            subclass[i] = "Path of the Juggernaut Barbarian"   
                        if subc == 7:
                            subclass[i] = "Path of the Storm Herald Barbarian"   
                        if subc == 8:
                            subclass[i] = "Path of the Totem Warrior Barbarian"  
                        if subc == 9:
                            subclass[i] = "Path of the Wild Magic Barbarian"
                        if subc == 10:
                            subclass[i] = "Path of the Zealot Barbarian"
                        if subc == 0:
                            subclass[i] = random.choice(Barb)
                    if param == "N":
                        subclass[i] = random.choice(Barb)                                   
                if subclass[i] == "Path of the Ancestral Guardian Barbarian":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Path of the Battlerager Barbarian":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Path of the Beast Barbarian":
                    BPBO1 = "One of your parents is a lycanthrope, and you've inherited some of their curse."
                    BPBO2 = "You are descended from an archdruid and inherited the ability to partially change shape."
                    BPBO3 = "A fey spirit gifted you with the ability to adopt different bestial aspects."
                    BPBO4 = "An ancient animal spirit dwells within you, allowing you to walk this path."
                    BPBO = [BPBO1, BPBO2, BPBO3, BPBO4]
                    BarbPathBeastOrigin = random.choice(BPBO)
                    ClassNotes.append(f"As a Path of the Beast Barbarian, the Origin of the Beast is: {BarbPathBeastOrigin}")                  
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Path of the Berserker Barbarian":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Path of the Giant Barbarian":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Path of the Juggernaut Barbarian":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Path of the Storm Herald Barbarian":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Path of the Totem Warrior Barbarian":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Path of the Zealot Barbarian":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Path of the Wild Magic Barbarian":        
                    print(f"Your subclass is {subclass[i]}")
        if Class[i] == "Bard":
            if ((param == "N") or (submulticlass == "N")):
                bardlvl = plLvl
                ClassLvl.append(bardlvl)             
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    bardlvl = int(input(f"Given your pool of levels of {poollevel}, what is your Bard level? "))      
                    if bardlvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                
                poollevel = poollevel - bardlvl
                ClassLvl.append(bardlvl)              
            if bardlvl >= 3:
                Bar = ["College of Creation Bard", "College of Eloquence Bard", "College of Glamour Bard", "College of Lore Bard", "College of the Road Bard", "College of Satire Bard", "College of Spirits Bard", "College of Swords Bard", "College of Tragedy Bard", "College of Valor Bard", "College of Whispers Bards"]
                if subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        print("1 - College of Creation Bard")
                        print("2 - College of Eloquence Bard")
                        print("3 - College of Glamour Bard")
                        print("4 - College of Lore Bard")
                        print("5 - College of the Road Bard")
                        print("6 - College of Satire Bard")
                        print("7 - College of Spirits Bard")
                        print("8 - College of Swords Bard")
                        print("9 - College of Tragedy Bard")
                        print("10 - College of Valor Bard")
                        print("11 - College of Whispers Bard")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 1:
                            subclass[i] = "College of Creation Bard"
                        if subc == 2:
                            subclass[i] = "College of Eloquence Bard"
                        if subc == 3:
                            subclass[i] = "College of Glamour Bard"
                        if subc == 4:
                            subclass[i] = "College of Lore Bard"
                        if subc == 5:
                            subclass[i] = "College of the Road Bard"
                        if subc == 6:
                            subclass[i] = "College of Satire Bard"
                        if subc == 7:
                            subclass[i] = "College of Spirits Bard"             
                        if subc == 8:
                            subclass[i] = "College of Swords Bard"
                        if subc == 9:
                            subclass[i] = "College of Tragedy Bard"
                        if subc == 10:
                            subclass[i] = "College of Valor Bard"
                        if subc == 11:
                            subclass[i] = "College of Whispers Bard"                                                                                                                            
                        if subc == 0:
                            subclass[i] = random.choice(Bar)
                    if param == "N":
                        subclass[i] = random.choice(Bar)                             
                if subclass[i] == "College of Creation Bard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "College of Eloquence Bard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "College of Glamour Bard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "College of Lore Bard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "College of the Road Bard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "College of Satire Bard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "College of Spirits Bard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "College of Swords Bard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "College of Tragedy Bard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "College of Valor Bard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "College of Whispers Bards":        
                    print(f"Your subclass is {subclass[i]}")
        if Class[i] == "Cleric":
            if ((param == "N") or (submulticlass == "N")):
                clerlvl = plLvl
                ClassLvl.append(clerlvl) 
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    clerlvl = int(input(f"Given your pool of levels of {poollevel}, what is your Cleric level? "))    
                    if clerlvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                
                poollevel = poollevel - clerlvl
                ClassLvl.append(clerlvl)
            if clerlvl >= 3:
                Cle = ["Arcana Domain Cleric", "Blood Domain Cleric", "Commmunity Domain Cleric", "Death Domain Cleric", 'Forge Domain Cleric', "Grave Domain Cleric", "Knowledge Domain Cleric", "Life Domain Cleric", "Light Domain Cleric", "Moon Domain Cleric", "Nature Domain Cleric", "Night Domain Cleric", "Order Domain Cleric", "Peace Domain Cleric", "Tempest Domain Cleric", "Trickery Domain Cleric", "Twilight Domain Cleric", "War Domain Cleric", "Zeal Domain Cleric"]
                if subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Arcana Domain Cleric")
                        print("2 - Blood Domain Cleric")
                        print("3 - Commmunity Domain Cleric")
                        print("4 - Death Domain Cleric")
                        print("5 - Forge Domain Cleric")
                        print("6 - Grave Domain Cleric")
                        print("7 - Knowledge Domain Cleric")
                        print("8 - Life Domain Cleric")
                        print("9 - Light Domain Cleric")
                        print("10 - Moon Domain Cleric")
                        print("11 - Nature Domain Cleric")
                        print("12 - Night Domain Cleric")
                        print("13 - Order Domain Cleric")
                        print("14 - Peace Domain Cleric")
                        print("15 - Tempest Domain Cleric")
                        print("16 - Trickery Domain Cleric")
                        print("17 - Twilight Domain Cleric")
                        print("18 - War Domain Cleric")
                        print("19 - Zeal Domain Cleric")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 1:
                            subclass[i] = "Arcana Domain Cleric"
                        if subc == 2:
                            subclass[i] = "Blood Domain Cleric"
                        if subc == 3:
                            subclass[i] = "Commmunity Domain Cleric"
                        if subc == 4:
                            subclass[i] = "Death Domain Cleric"
                        if subc == 5:
                            subclass[i] = "Forge Domain Cleric"
                        if subc == 6:
                            subclass[i] = "Grave Domain Cleric"
                        if subc == 7:
                            subclass[i] = "Knowledge Domain Cleric"
                        if subc == 8:
                            subclass[i] = "Life Domain Cleric"
                        if subc == 9:
                            subclass[i] = "Light Domain Cleric"
                        if subc == 10:
                            subclass[i] = "Moon Domain Cleric"
                        if subc == 11:
                            subclass[i] = "Nature Domain Cleric"
                        if subc == 12:
                            subclass[i] = "Night Domain Cleric"
                        if subc == 13:
                            subclass[i] = "Order Domain Cleric"
                        if subc == 14:
                            subclass[i] = "Peace Domain Cleric"
                        if subc == 15:
                            subclass[i] = "Tempest Domain Cleric"
                        if subc == 16:
                            subclass[i] = "Trickery Domain Cleric"
                        if subc == 17:
                            subclass[i] = "Twilight Domain Cleric"
                        if subc == 18:
                            subclass[i] = "War Domain Cleric"
                        if subc == 19:
                            subclass[i] = "Zeal Domain Cleric"                
                        if subc == 0:
                            subclass[i] = random.choice(Cle) 
                    if param == "N":
                        subclass[i] = random.choice(Cle)                             
                if subclass[i] == "Arcana Domain Cleric":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Blood Domain Cleric":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Commmunity Domain Cleric":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Death Domain Cleric":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Forge Domain Cleric":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Grave Domain Cleric":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Knowledge Domain Cleric":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Life Domain Cleric":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Light Domain Cleric":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Moon Domain Cleric":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Nature Domain Cleric":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Night Domain Cleric":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Order Domain Cleric":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Peace Domain Cleric":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Tempest Domain Cleric":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Trickery Domain Cleric":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Twilight Domain Cleric":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "War Domain Cleric":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Zeal Domain Cleric":        
                    print(f"Your subclass is {subclass[i]}")
        if Class[i] == "Druid":
            if ((param == "N") or (submulticlass == "N")):
                drulvl = plLvl
                ClassLvl.append(drulvl) 
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    drulvl = int(input(f"Given your pool of levels of {poollevel}, what is your Druid level? "))      
                    if drulvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                
                poollevel = poollevel - drulvl
                ClassLvl.append(drulvl)
            if drulvl >= 3:
                Dru = ["Circle of the Blighted Druid", "Circle of Dreams Druid", "Circle of the Land Druid", "Circle of the Moon Druid", "Circle of the Sheppard Druid", "Circle of Spores Druid", "Circle of the Stars Druid", "Circle of Wildfire Druid"]  
                if subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Circle of the Blighted Druid")
                        print("2 - Circle of Dreams Druid")
                        print("3 - Circle of the Land Druid")
                        print("4 - Circle of the Moon Druid")
                        print("5 - Circle of the Sheppard Druid")
                        print("6 - Circle of Spores Druid")
                        print("7 - Circle of the Stars Druid")
                        print("8 - Circle of Wildfire Druid")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 1:
                            subclass[i] = "Circle of the Blighted Druid"
                        if subc == 2:
                            subclass[i] = "Circle of Dreams Druid"
                        if subc == 3:
                            subclass[i] = "Circle of the Land Druid"
                        if subc == 4:
                            subclass[i] = "Circle of the Moon Druid"    
                        if subc == 5:
                            subclass[i] = "Circle of the Sheppard Druid"
                        if subc == 6:
                            subclass[i] = "Circle of Spores Druid"
                        if subc == 7:
                            subclass[i] = "Circle of the Stars Druid" 
                        if subc == 8:
                            subclass[i] = "Circle of Wildfire Druid"
                        if subc == 0:
                            subclass[i] = random.choice(Dru)
                    if param == "N":
                        subclass[i] = random.choice(Dru)                               
                if subclass[i] == "Circle of the Blighted Druid":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Circle of Dreams Druid":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Circle of the Land Druid":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Circle of the Moon Druid":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Circle of the Sheppard Druid":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Circle of Spores Druid":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Circle of the Stars Druid":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Circle of Wildfire Druid":        
                    print(f"Your subclass is {subclass[i]}")
        if Class[i] == "Fighter":
            if ((param == "N") or (submulticlass == "N")):
                figlvl = plLvl
                ClassLvl.append(figlvl)   
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    figlvl = int(input(f"Given your pool of levels of {poollevel}, what is your Fighter level? "))       
                    if figlvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                    
                poollevel = poollevel - figlvl
                ClassLvl.append(figlvl)
            if figlvl >= 3:
                Fig = ["Arcane Archer Archetype Fighter", "Battle Master Archetype Fighter", "Cavalier Archetype Fighter", "Champion Archetype Fighter", "Echo Knight Archetype Fighter", "Eldrich Knight Archetype Fighter", "Psi Warrior Archetype Fighter", "Purple Dragon Knight Archetype Fighter", "Rune Knight Archetype Fighter", "Samurai Archetype Fighter", "Scofflaw Archetype Fighter"]
                if subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Arcane Archer Archetype Fighter")
                        print("2 - Battle Master Archetype Fighter")
                        print("3 - Cavalier Archetype Fighter")
                        print("4 - Champion Archetype Fighter")
                        print("5 - Echo Knight Archetype Fighter")
                        print("6 - Eldrich Knight Archetype Fighter")
                        print("7 - Psi Warrior Archetype Fighter")
                        print("8 - Purple Dragon Knight Archetype Fighter")
                        print("9 - Rune Knight Archetype Fighter")
                        print("10 - Samurai Archetype Fighter")
                        print("11 - Scofflaw Archetype Fighter")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 1:
                            subclass[i] = "Arcane Archer Archetype Fighter"
                        if subc == 2:
                            subclass[i] = "Battle Master Archetype Fighter"
                        if subc == 3:
                            subclass[i] = "Cavalier Archetype Fighter"
                        if subc == 4:
                            subclass[i] = "Champion Archetype Fighter"  
                        if subc == 5:
                            subclass[i] = "Echo Knight Archetype Fighter"
                        if subc == 6:
                            subclass[i] = "Eldrich Knight Archetype Fighter"
                        if subc == 7:
                            subclass[i] = "Psi Warrior Archetype Fighter"
                        if subc == 8:
                            subclass[i] = "Purple Dragon Knight Archetype Fighter"  
                        if subc == 9:
                            subclass[i] = "Rune Knight Archetype Fighter"
                        if subc == 10:
                            subclass[i] = "Samurai Archetype Fighter"
                        if subc == 11:
                            subclass[i] = "Scofflaw Archetype Fighter"       
                        if subc == 0:
                            subclass[i] = random.choice(Fig)          
                    if param == "N":
                        subclass[i] = random.choice(Fig)                    
                if subclass[i] == "Arcane Archer Archetype Fighter":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Battle Master Archetype Fighter":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Cavalier Archetype Fighter":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Champion Archetype Fighter":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Echo Knight Archetype Fighter":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Eldrich Knight Archetype Fighter":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Psi Warrior Archetype Fighter":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Purple Dragon Knight Archetype Fighter":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Rune Knight Archetype Fighter":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Samurai Archetype Fighter":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Scofflaw Archetype Fighter":        
                    print(f"Your subclass is {subclass[i]}")
        if Class[i] == "Monk":
            if ((param == "N") or (submulticlass == "N")):
                monklvl = plLvl
                ClassLvl.append(monklvl) 
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    monklvl = int(input(f"Given your pool of levels of {poollevel}, what is your Monk level? "))    
                    if monklvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                
                poollevel = poollevel - monklvl
                ClassLvl.append(monklvl)
            if monklvl >= 3:
                Mon = ["Way of the Ascendant Dragon Monk", "Way of the Astral Self Monk", "Way of the Cobalt Soul Monk", "Way of the Drunken Master Monk", "Way of the Four Elements Monk", "Way of the Kensei Monk", "Way of the Long Death Monk", "Way of Mercy Monk", "Way of the Open Hand Monk", "Way of the Shadow Monk", "Way of the Sun Soul Monk"]
                if subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Way of the Ascendant Dragon Monk")
                        print("2 - Way of the Astral Self Monk")
                        print("3 - Way of the Cobalt Soul Monk")
                        print("4 - Way of the Drunken Master Monk")
                        print("5 - Way of the Four Elements Monk")
                        print("6 - Way of the Kensei Monk")
                        print("7 - Way of the Long Death Monk")
                        print("8 - Way of Mercy Monk")
                        print("9 - Way of the Open Hand Monk")
                        print("10 - Way of the Shadow Monk")
                        print("11 - Way of the Sun Soul Monk")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 1:
                            subclass[i] = "Way of the Ascendant Dragon Monk"
                        if subc == 2:
                            subclass[i] = "Way of the Astral Self Monk"
                        if subc == 3:
                            subclass[i] = "Way of the Cobalt Soul Monk"
                        if subc == 4:
                            subclass[i] = "Way of the Drunken Master Monk"     
                        if subc == 5:
                            subclass[i] = "Way of the Four Elements Monk"
                        if subc == 6:
                            subclass[i] = "Way of the Kensei Monk"
                        if subc == 7:
                            subclass[i] = "Way of the Long Death Monk"
                        if subc == 8:
                            subclass[i] = "Way of Mercy Monk"
                        if subc == 9:
                            subclass[i] = "Way of the Open Hand Monk"
                        if subc == 10:
                            subclass[i] = "Way of the Shadow Monk"
                        if subc == 11:
                            subclass[i] = "Way of the Sun Soul Monk"            
                        if subc == 0:
                            subclass[i] = random.choice(Mon)
                    if param == "N":
                        subclass[i] = random.choice(Mon)                               
                if subclass[i] == "Way of the Ascendant Dragon Monk":
                    ADO1 = "You honed your abilities by aligning your spirit with a dragon's world-altering power."
                    ADO2 = "A dragon personally took an active role in shaping your inner energy."
                    ADO3 = "You studied at a monastery that traces its teachings back centuries or more to a single dragon's instruction, or one that is devoted to a dragon god."
                    ADO4 = "You spent long stretches meditating in the region around an ancient dragon's lair, absorbing that lair's ambient magic."
                    ADO5 = "You found a scroll written in Draconic that contained inspiring new techniques."
                    ADO6 = "After a dream featuring a five-handed dragonborn, you awoke with the mystical breath of dragons."
                    ADO = [ADO1, ADO2, ADO3, ADO4, ADO5, ADO6]
                    AscenDragOrigin = random.choice(ADO)
                    ClassNotes.append(f"As a Way of the Ascendant Dragon Monk, your Ascendant Origin: {AscenDragOrigin}")              
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Way of the Astral Self Monk":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Way of the Cobalt Soul Monk":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Way of the Drunken Master Monk":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Way of the Four Elements Monk":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Way of the Kensei Monk":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Way of the Long Death Monk":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Way of Mercy Monk":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Way of the Open Hand Monk":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Way of the Shadow Monk":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Way of the Sun Soul Monk":        
                    print(f"Your subclass is {subclass[i]}")
        if Class[i] == "Paladin":
            if ((param == "N") or (submulticlass == "N")):
                pallvl = plLvl
                ClassLvl.append(pallvl) 
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    pallvl = int(input(f"Given your pool of levels of {poollevel}, what is your Paladin level? "))      
                    if pallvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                
                poollevel = poollevel - pallvl
                ClassLvl.append(pallvl)
            if pallvl >= 3:
                Pal= ["Oath of the Ancients Paladin", "Oath of Conquest Paladin", "Oath of the Crown Paladin", "Oath of Devotion Paladin", "Oath of Glory Paladin", "Oath of the Open Sea Paladin", "Oath of Redemption Paladin", "Oath of the Watchers Paladin", "Oath of Vengeance Paladin", "Oathbreaker Paladin"]
                if subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Oath of the Ancients Paladin")
                        print("2 - Oath of Conquest Paladin")
                        print("3 - Oath of the Crown Paladin")
                        print("4 - Oath of Devotion Paladin")
                        print("5 - Oath of Glory Paladin")
                        print("6 - Oath of the Open Sea Paladin")
                        print("7 - Oath of Redemption Paladin")
                        print("8 - Oath of the Watchers Paladin")
                        print("9 - Oath of Vengeance Paladin")
                        print("10 - Oathbreaker Paladin")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 1:
                            subclass[i] = "Oath of the Ancients Paladin"
                        if subc == 2:
                            subclass[i] = "Oath of Conquest Paladin"
                        if subc == 3:
                            subclass[i] = "Oath of the Crown Paladin"
                        if subc == 4:
                            subclass[i] = "Oath of Devotion Paladin"
                        if subc == 5:
                            subclass[i] = "Oath of Glory Paladin"
                        if subc == 6:
                            subclass[i] = "Oath of the Open Sea Paladin"
                        if subc == 7:
                            subclass[i] = "Oath of Redemption Paladin"
                        if subc == 8:
                            subclass[i] = "Oath of the Watchers Paladin"  
                        if subc == 9:
                            subclass[i] = "Oath of Vengeance Paladin"
                        if subc == 10:
                            subclass[i] = "Oathbreaker Paladin"
                        if subc == 0:
                            subclass[i] = random.choice(Pal)
                    if param == "N":
                        subclass[i] = random.choice(Pal)                     
                if subclass[i] == "Oath of the Ancients Paladin":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Oath of Conquest Paladin":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Oath of the Crown Paladin":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Oath of Devotion Paladin":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Oath of Glory Paladin":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Oath of the Open Sea Paladin":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Oath of Redemption Paladin":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Oath of the Watchers Paladin":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Oath of Vengeance Paladin":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Oathbreaker Paladin":        
                    print(f"Your subclass is {subclass[i]}")
        if Class[i] == "Ranger":
            if ((param == "N") or (submulticlass == "N")):
                ranlvl = plLvl
                ClassLvl.append(ranlvl)
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    ranlvl = int(input(f"Given your pool of levels of {poollevel}, what is your Ranger level? "))  
                    if ranlvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                
                poollevel = poollevel - ranlvl
                ClassLvl.append(ranlvl)
            if ranlvl >= 3:
                Ran = ["Beast Master Archetype Ranger", "Drakewarden Ranger", "Fey Wanderer Archetype Ranger", "Gloom Stalker Archetype Ranger", "Horizon Walker Archetype Ranger", "Hunter Archetype Ranger", "Monster Slayer Archetype Ranger", "Shooting Star Archetype Ranger", "Swarmkeeper Archetype Ranger"]
                if subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Beast Master Archetype Ranger")
                        print("2 - Drakewarden Ranger")
                        print("3 - Fey Wanderer Archetype Ranger")
                        print("4 - Gloom Stalker Archetype Ranger")
                        print("5 - Horizon Walker Archetype Ranger")
                        print("6 - Hunter Archetype Ranger")
                        print("7 - Monster Slayer Archetype Ranger")
                        print("8 - Shooting Star Archetype Ranger")
                        print("9 - Swarmkeeper Archetype Ranger")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 1:
                            subclass[i] = "Beast Master Archetype Ranger"
                        if subc == 2:
                            subclass[i] = "Drakewarden Ranger"
                        if subc == 3:
                            subclass[i] = "Fey Wanderer Archetype Ranger"
                        if subc == 4:
                            subclass[i] = "Gloom Stalker Archetype Ranger"    
                        if subc == 5:
                            subclass[i] = "Horizon Walker Archetype Ranger"
                        if subc == 6:
                            subclass[i] = "Hunter Archetype Ranger"
                        if subc == 7:
                            subclass[i] = "Monster Slayer Archetype Ranger"   
                        if subc == 8:
                            subclass[i] = "Shooting Star Archetype Ranger"   
                        if subc == 9:
                            subclass[i] = "Swarmkeeper Archetype Ranger"
                        if subc == 0:
                            subclass[i] = random.choice(Ran)  
                    if param == "N":
                        subclass[i] = random.choice(Ran)                          
                if subclass[i] == "Beast Master Archetype Ranger":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Drakewarden Ranger":
                    DWO1 = "You studied a dragon's scale or claw, or a trinket from a dragon's hoard, creating your bond through that token's lingering draconic magic."
                    DWO2 = "A secret order of rangers who collect and guard draconic lore taught you their ways."
                    DWO3 = "A dragon gave you a geode or gemstone to care for. To your surprise, the drake hatched from that stone."
                    DWO4 = "You ingested a few drops of dragon blood, forever infusing your nature magic with draconic power."
                    DWO5 = "An ancient Draconic inscription on a standing stone empowered you when you read it aloud."
                    DWO6 = "You had a vivid dream of a mysterious figure accompanied by seven yellow canaries, who warned you of impending doom. When you awoke, your drake was there, watching you."
                    DWO = [DWO1, DWO2, DWO3, DWO4, DWO5, DWO6]
                    DrakewardenOrigin = random.choice(DWO)
                    ClassNotes.append(f"As a Drakewarden Ranger, your Drakewarden Origin: {DrakewardenOrigin}")       
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Fey Wanderer Archetype Ranger":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Gloom Stalker Archetype Ranger":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Horizon Walker Archetype Ranger":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Hunter Archetype Ranger":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Monster Slayer Archetype Ranger":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Shooting Star Archetype Ranger":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Swarmkeeper Archetype Ranger": 
                    print(f"Your subclass is {subclass[i]}")                       
        if Class[i] == "Rogue":
            if ((param == "N") or (submulticlass == "N")):
                roglvl = plLvl
                ClassLvl.append(roglvl)
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    roglvl = int(input(f"Given your pool of levels of {poollevel}, what is your Rogue level? "))   
                    if roglvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                
                poollevel = poollevel - roglvl
                ClassLvl.append(roglvl)
            if roglvl >= 3:
                Rog = ["Arcane Trickster Archetype Rogue", "Assassin Archetype Rogue", "Inquisitive Archetype Rogue", "Mastermind Archetype Rogue", "Mountebank Archetype Rogue", "Phantom Archetype Rogue", "Scout Archetype Rogue", "Soulknife Archetype Rogue", "Swashbuckler Archetype Rogue", "Thief Archetype Rogue"]
                if subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Arcane Trickster Archetype Rogue")
                        print("2 - Assassin Archetype Rogue")
                        print("3 - Inquisitive Archetype Rogue")
                        print("4 - Mastermind Archetype Rogue")
                        print("5 - Mountebank Archetype Rogue")
                        print("6 - Phantom Archetype Rogue")
                        print("7 - Scout Archetype Rogue")
                        print("8 - Soulknife Archetype Rogue")
                        print("9 - Swashbuckler Archetype Rogue")
                        print("10 - Thief Archetype Rogue")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 1:
                            subclass[i] = "Arcane Trickster Archetype Rogue"
                        if subc == 2:
                            subclass[i] = "Assassin Archetype Rogue"
                        if subc == 3:
                            subclass[i] = "Inquisitive Archetype Rogue"
                        if subc == 4:
                            subclass[i] = "Mastermind Archetype Rogue"  
                        if subc == 5:
                            subclass[i] = "Mountebank Archetype Rogue"
                        if subc == 6:
                            subclass[i] = "Phantom Archetype Rogue"
                        if subc == 7:
                            subclass[i] = "Scout Archetype Rogue"
                        if subc == 8:
                            subclass[i] = "Soulknife Archetype Rogue"   
                        if subc == 9:
                            subclass[i] = "Swashbuckler Archetype Rogue"   
                        if subc == 10:
                            subclass[i] = "Thief Archetype Rogue"     
                        if subc == 0:
                            subclass[i] = random.choice(Rog)
                    if param == "N":
                        subclass[i] = random.choice(Rog)                               
                if subclass[i] == "Arcane Trickster Archetype Rogue":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Assassin Archetype Rogue":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Inquisitive Archetype Rogue":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Mastermind Archetype Rogue":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Mountebank Archetype Rogue":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Phantom Archetype Rogue":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Scout Archetype Rogue":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Soulknife Archetype Rogue":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Swashbuckler Archetype Rogue":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Thief Archetype Rogue":        
                    print(f"Your subclass is {subclass[i]}")
        if Class[i] == "Sorcerer":
            if ((param == "N") or (submulticlass == "N")):
                sorclvl = plLvl
                ClassLvl.append(sorclvl)              
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    sorclvl = int(input(f"Given your pool of levels of {poollevel}, what is your Sorcerer level? "))  
                    if sorclvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                
                poollevel = poollevel - sorclvl
                ClassLvl.append(sorclvl)
            if sorclvl >= 3:
                Sor = ["Aberrant Mind Origin Sorcerer", "Clockwork Soul Origin Sorcerer", "Divine Soul Origin Sorcerer", "Draconic Bloodline Origin Sorcerer", "Lunar Magic Origin Sorcerer", "Phoenix Origin Sorcerer", "Runechild Origin Sorcerer", "Sea Origin Sorcerer", "Shadow Origin Sorcerer", "Stone Origin Sorcerer", "Storm Origin Sorcerer", "Wild Magic Origin Sorcerer"]
                if subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Aberrant Mind Origin Sorcerer")
                        print("2 - Clockwork Soul Origin Sorcerer")
                        print("3 - Divine Soul Origin Sorcerer")
                        print("4 - Draconic Bloodline Origin Sorcerer")
                        print("5 - Lunar Magic Origin Sorcerer")
                        print("6 - Phoenix Origin Sorcerer")
                        print("7 - Runechild Origin Sorcerer")
                        print("8 - Sea Origin Sorcerer")
                        print("9 - Shadow Origin Sorcerer")
                        print("10 - Stone Origin Sorcerer")
                        print("11 - Storm Origin Sorcerer")
                        print("12 - Wild Magic Origin Sorcerer")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 1:
                            subclass[i] = "Aberrant Mind Origin Sorcerer"
                        if subc == 2:
                            subclass[i] = "Clockwork Soul Origin Sorcerer"
                        if subc == 3:
                            subclass[i] = "Divine Soul Origin Sorcerer"
                        if subc == 4:
                            subclass[i] = "Draconic Bloodline Origin Sorcerer"     
                        if subc == 5:
                            subclass[i] = "Lunar Magic Origin Sorcerer"
                        if subc == 6:
                            subclass[i] = "Phoenix Origin Sorcerer"
                        if subc == 7:
                            subclass[i] = "Runechild Origin Sorcerer"
                        if subc == 8:
                            subclass[i] = "Sea Origin Sorcerer"
                        if subc == 9:
                            subclass[i] = "Shadow Origin Sorcerer"
                        if subc == 10:
                            subclass[i] = "Stone Origin Sorcerer"
                        if subc == 11:
                            subclass[i] = "Storm Origin Sorcerer"
                        if subc == 12:
                            subclass[i] = "Wild Magic Origin Sorcerer"        
                        if subc == 0:
                            subclass[i] = random.choice(Sor)
                    if param == "N":
                        subclass[i] = random.choice(Sor)                                 
                if subclass[i] == "Aberrant Mind Origin Sorcerer":
                    AbSO1 = "You were exposed to the Far Realm's warping influence. You are confinced that a tentacle is now growing on you, but no one else can see it."
                    AbSO2 = "A psychic wind from the Astral Plane carried psionic energy to you. When you use your powers, faint motes of light sparkle around you."
                    AbSO3 = "You once suffered the dominating powers of an aboleth, leaving a psychic splinter in your mind."
                    AbSO4 = "You were implanted with a mind flayer tadpole, but the ceremorphosis never completed. And now its psionic power is yours. When you use it, your flesh shines with a strange mucus."
                    AbSO5 = "As a child, you had an imaginary friend that looked like a flumph or a strange platypus-like creature. One day, it gifted you with psionic powers, which have ended up being not so imaginary."
                    AbSO6 = "Your nightmares whisper the truth to you: your psionic powers are not your own. You draw them from your parasitic twin."
                    AbSO = [AbSO1, AbSO2, AbSO3, AbSO4, AbSO5, AbSO6]
                    AberrantOrigin = random.choice(AbSO)
                    ClassNotes.append(f"As an Aberrant Mind Origin Sorcerer, the Aberrant Origin is {AberrantOrigin}")     
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Clockwork Soul Origin Sorcerer":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Divine Soul Origin Sorcerer":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Draconic Bloodline Origin Sorcerer":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Lunar Magic Origin Sorcerer":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Phoenix Origin Sorcerer":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Runechild Origin Sorcerer":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Sea Origin Sorcerer":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Shadow Origin Sorcerer":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Stone Origin Sorcerer":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Storm Origin Sorcerer":  
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Wild Magic Origin Sorcerer":                  
                    print(f"Your subclass is {subclass[i]}")
        if Class[i] == "Warlock":   
            if ((param == "N") or (submulticlass == "N")):
                warlvl = plLvl
                ClassLvl.append(warlvl) 
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    warlvl = int(input(f"Given your pool of levels of {poollevel}, what is your Warlock level? "))    
                    if warlvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                
                poollevel = poollevel - warlvl
                ClassLvl.append(warlvl)
            if warlvl >= 3:
                War = ["Ancient Dragon Patron Warlock", "Archfey Patron Warlock", "Celestial Patron Warlock", "The Fathomless Patron Warlock", "Fiend Patron Warlock", "The Genie Patron Warlock", "Great Old One Patron Warlock", "Hexblade Patron Warlock", "Mysterious Feline Patron Warlock", "Queen of Spiders Patron Warlock", "Raven Queen Patron Warlock", "Serpent Patron Warlock", "Undead Patron Warlock", "Undying Patron Warlock"]    
                if subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Ancient Dragon Patron Warlock")
                        print("2 - Archfey Patron Warlock")
                        print("3 - Celestial Patron Warlock")
                        print("4 - The Fathomless Patron Warlock")
                        print("5 - Fiend Patron Warlock")
                        print("6 - The Genie Patron Warlock")
                        print("7 - Great Old One Patron Warlock")
                        print("8 - Hexblade Patron Warlock")
                        print("9 - Mysterious Feline Patron Warlock")
                        print("10 - Queen of Spiders Patron Warlock")
                        print("11 - Raven Queen Patron Warlock")
                        print("12 - Serpent Patron Warlock")
                        print("13 - Undead Patron Warlock")
                        print("14 - Undying Patron Warlock")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 1:
                            subclass[i] = "Ancient Dragon Patron Warlock"
                        if subc == 2:
                            subclass[i] = "Archfey Patron Warlock"
                        if subc == 3:
                            subclass[i] = "Celestial Patron Warlock"
                        if subc == 4:
                            subclass[i] = "The Fathomless Patron Warlock"   
                        if subc == 5:
                            subclass[i] = "Fiend Patron Warlock"
                        if subc == 6:
                            subclass[i] = "The Genie Patron Warlock"
                        if subc == 7:
                            subclass[i] = "Great Old One Patron Warlock"
                        if subc == 8:
                            subclass[i] = "Hexblade Patron Warlock"
                        if subc == 9:
                            subclass[i] = "Mysterious Feline Patron Warlock"   
                        if subc == 10:
                            subclass[i] = "Queen of Spiders Patron Warlock"
                        if subc == 11:
                            subclass[i] = "Raven Queen Patron Warlock"
                        if subc == 12:
                            subclass[i] = "Serpent Patron Warlock"
                        if subc == 13:
                            subclass[i] = "Undead Patron Warlock"
                        if subc == 14:
                            subclass[i] = "Undying Patron Warlock"                                                                                                
                        if subc == 0:
                            subclass[i] = random.choice(War)
                    if param == "N":
                        subclass[i] = random.choice(War)                              
                if subclass[i] == "Ancient Dragon Patron Warlock":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Archfey Patron Warlock":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Celestial Patron Warlock":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "The Fathomless Patron Warlock":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Fiend Patron Warlock":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "The Genie Patron Warlock":
                    GenK1 = "Dao, or Earth Genie"
                    GenK2 = "Djinni, or Air Genie"
                    GenK3 = "Efreeti, or Fire Genie"
                    GenK4 = "Marid, or Water Genie"
                    GenK = [GenK1, GenK2, GenK3, GenK4]
                    GenieKind = random.choice(GenK)
                    ClassNotes.append(f"As a Genie Patron Warlock, your Genie is a(n): {GenieKind}")                  
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Great Old One Patron Warlock":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Hexblade Patron Warlock":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Mysterious Feline Patron Warlock":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Queen of Spiders Patron Warlock":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Raven Queen Patron Warlock":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Serpent Patron Warlock":    
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Undead Patron Warlock":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Undying Patron Warlock":                 
                    print(f"Your subclass is {subclass[i]}")
        if Class[i] == "Wizard":
            if ((param == "N") or (submulticlass == "N")):
                wizlvl = plLvl
                ClassLvl.append(wizlvl)  
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    wizlvl = int(input(f"Given your pool of levels of {poollevel}, what is your Wizard level? "))  
                    if wizlvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                
                poollevel = poollevel - wizlvl
                ClassLvl.append(wizlvl)                       
            if wizlvl >= 3:
                Wiz = ["Abjuration Arcane Tradition Wizard", "Bladesinging Arcane Tradition Wizard", "Blood Magic Arcane Tradition Wizard", "Chronurgy Magic Wizard", "Conjuration Arcane Tradition Wizard", "Divination Arcane Tradition Wizard", "Enchantment Arcane Tradition Wizard", "Evocation Arcane Tradition Wizard", "Graviturgy Magic Wizard", "Illusion Arcane Tradition Wizard", "Necromancy Arcane Tradition Wizard", "Order of Scribes Arcane Tradition Wizard", "Transmutation Arcane Tradition Wizard", "War Arcane Tradition Wizard"]
                if subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Abjuration Arcane Tradition Wizard")
                        print("2 - Bladesinging Arcane Tradition Wizard")
                        print("3 - Blood Magic Arcane Tradition Wizard")
                        print("4 - Chronurgy Magic Arcane Tradition Wizard")
                        print("5 - Conjuration Arcane Tradition Wizard")
                        print("6 - Divination Arcane Tradition Wizard")
                        print("7 - Enchantment Arcane Tradition Wizard")
                        print("8 - Evocation Arcane Tradition Wizard")
                        print("9 - Graviturgy Magic Arcane Tradition Wizard")
                        print("10 - Illusion Arcane Tradition Wizard")
                        print("11 - Necromancy Arcane Tradition Wizard")
                        print("12 - Order of Scribes Arcane Tradition Wizard")
                        print("13 - Transmutation Arcane Tradition Wizard")
                        print("14 - War Arcane Tradition Wizard")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 1:
                            subclass[i] = "Abjuration Arcane Tradition Wizard"
                        if subc == 2:
                            subclass[i] = "Bladesinging Arcane Tradition Wizard"
                        if subc == 3:
                            subclass[i] = "Blood Magic Arcane Tradition Wizard"
                        if subc == 4:
                            subclass[i] = "Chronurgy Magic Arcane Tradition Wizard"  
                        if subc == 5:
                            subclass[i] = "Conjuration Arcane Tradition Wizard"
                        if subc == 6:
                            subclass[i] = "Divination Arcane Tradition Wizard"
                        if subc == 7:
                            subclass[i] = "Enchantment Arcane Tradition Wizard"
                        if subc == 8:
                            subclass[i] = "Evocation Arcane Tradition Wizard" 
                        if subc == 9:
                            subclass[i] = "Graviturgy Magic Arcane Tradition Wizard"   
                        if subc == 10:
                            subclass[i] = "Illusion Arcane Tradition Wizard"
                        if subc == 11:
                            subclass[i] = "Necromancy Arcane Tradition Wizard"
                        if subc == 12:
                            subclass[i] = "Order of Scribes Arcane Tradition Wizard"                                                               
                        if subc == 13:
                            subclass[i] = "Transmutation Arcane Tradition Wizard"
                        if subc == 14:
                            subclass[i] = "War Arcane Tradition Wizard"                                       
                        if subc == 0:
                            subclass[i] = random.choice(Wiz)
                    if param == "N":
                        subclass[i] = random.choice(Wiz)                              
                if subclass[i] == "Abjuration Arcane Tradition Wizard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Bladesinging Arcane Tradition Wizard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Blood Magic Arcane Tradition Wizard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Chronurgy Magic Wizard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Conjuration Arcane Tradition Wizard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Divination Arcane Tradition Wizard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Enchantment Arcane Tradition Wizard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Evocation Arcane Tradition Wizard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Graviturgy Magic Wizard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Illusion Arcane Tradition Wizard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Necromancy Arcane Tradition Wizard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Order of Scribes Arcane Tradition Wizard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "Transmutation Arcane Tradition Wizard":
                    print(f"Your subclass is {subclass[i]}")
                if subclass[i] == "War Arcane Tradition Wizard":
                    print(f"Your subclass is {subclass[i]}")

#When finally reporting everything, make sure to include the Color/Gem/Metal for Certain Dragonborn, or Season for the Eladrin Subrace of Elves

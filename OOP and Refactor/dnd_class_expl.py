#When converting notes to a dictionary, start by replacing all player.notes.append( into player.notes[
#Double check what classes give what tool proficiencies
#Code in What it means to be the ravenloft races / hollow one
#This file will have a name similar to "update" while everything that occurs once (equipment) will be moved to dnd_class_gen
import random
import math
from dnd_languagesskills import *
import dnd_tools


def dice(sides):
    # Rolls a dice with dicenum sides
    result = random.randint(1, sides)
    return result



#Define a function called hpcalc that determines your hp, given your level, and what dice you give it
def hpcalc(chlvl, dicefunc, sides):
    result = 0
    for i in range(chlvl):
        result += dicefunc(sides)  # Call the function with the sides
    return result

def dndchargen_characterbuilder(param, player):
    poollevel = player.level
    MartialWeapons = list(dnd_tools.martial_weapons.keys())
    MartialWeaponsNames = [wep["Name"] for wep in dnd_tools.martial_weapons.values()]
    mw_keys_to_remove = ["Blowgun", "HandCrossbow", "HeavyCrossbow", "Longbow", "Net"]
    MartialMeleeWeapons = [key for key in MartialWeapons if key not in mw_keys_to_remove]
    MartialMeleeWeaponsNames = [key["Name"] for key in dnd_tools.martial_weapons.values() if key not in mw_keys_to_remove]
    SimpleWeapons = list(dnd_tools.simple_weapons.keys())
    SimpleWeaponsNames = [wep["Name"] for wep in dnd_tools.simple_weapons.values()]
    sw_keys_to_remove = ["LightCrossbow", "Dart", "Shortbow", "Sling"]
    SimpleMeleeWeapons = [key for key in SimpleWeapons if key not in sw_keys_to_remove]
    SimpleMeleeWeaponsNames = [key["Name"] for key in dnd_tools.simple_weapons.values() if key not in sw_keys_to_remove]
    MusicalInstr = list(dnd_tools.musical_instr.keys())
    MusicalInstrNames = [mi["Name"] for mi in dnd_tools.musical_instr.values()]
    mi_key_to_remove = ["Lute"]
    MusicalInstrWOLute = [key for key in MusicalInstr if key not in mi_key_to_remove]
    MusicalInstrWOLuteNames = [key["Name"] for key in dnd_tools.musical_instr.values() if key not in mi_key_to_remove]
    AllWeapons = MartialWeapons + SimpleWeapons
    ohw_keys = ["Club", "Dagger", "Handaxe", "Javelin", "LightHammer", "Mace", "Quarterstaff", "Sickle", "Spear", 
                        "Battleaxe", "Flail", "Lance", "Longsword", "Morningstar", "Rapier", "Scimitar", "Shortsword", 
                        "Trident", "WarPick", "Warhammer", "Whip"
                    ]
    OneHandedWeapons = [key for key in AllWeapons if key in ohw_keys]
    OneHandedWeaponsNames = [
        dnd_tools.simple_weapons[key]["Name"] if key in dnd_tools.simple_weapons 
        else dnd_tools.martial_weapons[key]["Name"] 
        for key in OneHandedWeapons
    ]
    if player.level >= 4:
        player.classnotes.append("You can increase one score by 2, two by one, or a feat. As normal, you can't increase an ability score above 20 using this feature.")
    if player.level >= 8:
        player.classnotes.append("You can increase one score by 2, two by one, or a feat. As normal, you can't increase an ability score above 20 using this feature.")    
    if player.level >= 12:
        player.classnotes.append("You can increase one score by 2, two by one, or a feat. As normal, you can't increase an ability score above 20 using this feature.")    
    if player.level >= 16:
        player.classnotes.append("You can increase one score by 2, two by one, or a feat. As normal, you can't increase an ability score above 20 using this feature.")        
    if player.level >= 19:
        player.classnotes.append("You can increase one score by 2, two by one, or a feat. As normal, you can't increase an ability score above 20 using this feature.")    
    print(f"Your classes are {player.Class}")
    for i in range(len(player.Class)):
        print(f"i is {i}")
        if player.Class[i] == "Artificer":
            if ((param == "N") or (player.singlemulticlass == "N")):
                artlvl = player.level
                player.classlvl.append(artlvl)            
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:
                    artlvl = int(input(f"Given your pool of levels of {poollevel}, What is your Artificer level? "))
                    if artlvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")
                poollevel = poollevel - artlvl
                player.classlvl.append(artlvl)
            if artlvl >= 1:
                player.hitdice.append(f"{artlvl}d8 for {player.Class[i]}")
                if artlvl == 1:
                    player.hitpoints += (8 + player.ConMod)
                else:
                    player.hitpoints += (8 + player.ConMod + hpcalc(artlvl, dice, 8))
                if i == 0:
                    profs = ["Light Armor", "Medium Armor", "Shield", "Simple Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    player.proficiencies.append(dnd_tools.kits["ThievKit"]["Name"])
                    player.proficiencies.append(dnd_tools.artisan_tools["TinkTools"]["Name"])                                                
                    player.proficiencies = artisantools(param, player.proficiencies)
                    player.skills.append(dnd_tools.saving_throws["ConST"])
                    player.skills.append(dnd_tools.saving_throws["IntST"])
                    ArtSkillsList = [
                        dnd_tools.skills["Arcana"], 
                        dnd_tools.skills["History"], 
                        dnd_tools.skills["Investigation"], 
                        dnd_tools.skills["Medicine"], 
                        dnd_tools.skills["Nature"], 
                        dnd_tools.skills["Perception"], 
                        dnd_tools.skills["SleightofHand"]
                        ]
                    player.skills = twoskillsfromlist(param, player.skills, ArtSkillsList)
                    ArtChoices = ["Starting Equipment", "Gold"]
                    ArtChoices2 = ["Studded Leather Armor", "Scale Mail"]
                    if param == "Y":
                        print("0 - Random")
                        for idx, artch in enumerate(ArtChoices,1):
                            print(f"{idx} - {artch}")
                        sego = int(input("Would you like the starting equipment or gold(5d4 x 10gp, must forgo starting equipment from background, Artificer Only)? "))
                        if sego == 1:
                            player.equipment = twosimpleweapons(param, player.equipment)
                            player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                            player.equipment.append("20 Bolts")
                            print("0 - Random")
                            for idx, artch2 in enumerate(ArtChoices2,1):
                                print(f"{idx} - {artch2}")                            
                            artchoice3 = int(input("Which armor would you like to add to your equipment? "))
                            if artchoice3 == 1:
                                player.equipment.append(dnd_tools.light_armor["StuddedLeather"].copy())
                            if artchoice3 == 2:
                                player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                            if artchoice3 == 0:
                                RandArtChoice2 = random.choice(ArtChoices2)
                                if RandArtChoice2 == "Studded Leather Armor":
                                    player.equipment.append(dnd_tools.light_armor["StuddedLeather"].copy())
                                if RandArtChoice2 == "Scale Mail":
                                    player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                            player.equipment.append(dnd_tools.kits["ThievKit"].copy())
                            player.equipment.extend(dnd_tools.packs["DungeoneersPack"]["contents"])
                        if sego == 2:
                            player.gold = player.gold + dice(4) + dice(4) + dice(4) + dice(4) + dice(4)
                        if sego == 0:
                            RandArtChoice = random.choice(ArtChoices)
                            if RandArtChoice == "Starting Equipment":    
                                player.equipment = twosimpleweapons(param, player.equipment)
                                player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                                player.equipment.append("20 Bolts")
                                RandArtChoice2 = random.choice(ArtChoices2)
                                if RandArtChoice2 == "Studded Leather Armor":
                                    player.equipment.append(dnd_tools.light_armor["StuddedLeather"].copy())
                                if RandArtChoice2 == "Scale Mail":
                                    player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                                player.equipment.append(dnd_tools.kits["ThievKit"].copy())
                                player.equipment.extend(dnd_tools.packs["DungeoneersPack"]["contents"])
                            if RandArtChoice == "Gold":
                                player.gold = player.gold + dice(4) + dice(4) + dice(4) + dice(4) + dice(4)
                    if param == "N":
                        RandArtChoice = random.choice(ArtChoices)
                        if RandArtChoice == "Starting Equipment":    
                            player.equipment = twosimpleweapons(param, player.equipment)
                            player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                            player.equipment.append("20 Bolts")
                            RandArtChoice2 = random.choice(ArtChoices2)
                            if RandArtChoice2 == "Studded Leather Armor":
                                player.equipment.append(dnd_tools.light_armor["StuddedLeather"].copy())
                            if RandArtChoice2 == "Scale Mail":
                                player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                            player.equipment.append(dnd_tools.kits["ThievKit"].copy())
                            player.equipment.extend(dnd_tools.packs["DungeoneersPack"]["contents"])
                        if RandArtChoice == "Gold":
                            player.gold = player.gold + dice(4) + dice(4) + dice(4) + dice(4) + dice(4)
                else:
                    profs = ["Light Armor", "Medium Armor", "Shield"]
                    for prof in profs:                                                                     
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    player.proficiencies.append(dnd_tools.artisan_tools("ThievKit")["Name"]) 
                    player.proficiencies.append(dnd_tools.artisan_tools("TinkTools")["Name"])                         
                profs = ["Firearms"]
                for prof in profs:
                    if prof not in player.proficiencies:
                        player.proficiencies.append(prof)
                player.classnotes.append("Magical Tinkering (see notes)")
                player.notes.append(f"Magical Tinkering - You learn how to invest a spark of magic into mundane objects. To use this ability, you must have tinker's tools or other artisan's tools in hand. You then touch a Tiny nonmagical object as an action and give it one of the following magical properties of your choice:\n - The object sheds bright light in a 5-foot radius and dim light for an additional 5 feet \n - Whenever tapped by a creature, the object emits a recorded message that can be heard up to 10 feet away \n - You utter the message when you bestow this property on the object, and the recording can be no more than 6 seconds long \n - The object continuously emits your choice of an odor or a nonverbal sound (wind, waves, chirping, or the like). The chosen phenomenon is perceivable up to 10 feet away \n - A static visual effect appears on one of the object's surfaces. This effect can be a picture, up to 25 words of text, lines and shapes, or a mixture of these elements, as you like. \n The chosen property lasts indefinitely. As an action, you can touch the object and end the property early. \n You can bestow magic on multiple objects, touching one object each time you use this feature, though a single object can only bear one property at a time. The maximum number of objects you can affect with this feature at one time is equal to your Intelligence modifier, or {player.IntMod} objects, minimum of one object. If you try to exceed your maximum, the oldest property immediately ends, and then the new property applies.")
                player.spellcastingclass.append("Artificer")
                player.spellcastingability.append("Int")
                player.spellsavedc.append(8 + player.profbonus + player.IntMod)
                player.spellattackmod.append(player.profbonus + player.IntMod)
                ArtCantripsKnown = 2
                ArtSpellSlot1 = 0
                ArtSpellSlot2 = 0
                ArtSpellSlot3 = 0
                ArtSpellSlot4 = 0
                ArtSpellSlot5 = 0
            if artlvl >= 2:
                player.classnotes.append("Infuse Item (see notes)")
                player.notes.append("Infuse Item - You have the ability to imbue mundane items with certain magical infusions. The magic items you create with this feature are effectively prototypes of permanent items. You learn additional infusions of your choice when you reach certain levels in this class.\nWhenever you gain a level in this class, you can replace one of the artificer infusions you learned with a new one.")
                InfusionNumber = 4
                InfusedItem = 2
                player.classnotes.append("Infusing an Item (see notes)")
                player.notes.append(f"Infusing an Item - Whenever you finish a long rest, you can touch a nonmagical object and imbue it with one of your artificer infusions, turning it into a magic item. An infusion works on only certain kinds of objects, as specified in the infusion's description. If the item requires attunement, you can attune yourself to it the instant you infuse the item. If you decide to attune to the item later, you must do so using the normal process for attunement (see 'Attunement' in chapter 7 of the Dungeon Master's Guide).\nYour infusion remains in an item indefinitely, but when you die, the infusion vanishes after a number of days have passed equal to your Intelligence modifier, or {player.IntMod} days, minimum of 1 day. The infusion also vanishes if you give up your knowledge of the infusion for another one.\nYou can infuse more than one nonmagical object at the end of a long rest; the maximum number of objects appears in the Infused Items column of the Artificer table. You must touch each of the objects, and each of your infusions can be in only one object at a time. Moreover, no object can bear more than one of your infusions at a time. If you try to exceed your maximum number of infusions, the oldest infusion immediately ends, and then the new infusion applies.")
                ArtSpellSlot1 = 2
            if artlvl >= 3:
                player.classnotes.append("The Right Tool For The Job (see notes)")
                player.notes.append("The Right Tool For The Job - You learn how to produce exactly the tool you need: with tinker's tools in hand, you can magically create one set of artisan's tools in an unoccupied space within 5 feet of you. This creation requires 1 hour of uninterrupted work, which can coincide with a short or long rest. Though the product of magic, the tools are nonmagical, and they vanish when you use this feature again.")
                Arti = ["Alchemist Specialist Artificer", "Armorer Specialist Artificer", "Artilierist Specialist Artificer", "Battle Smith Specialist Artificer"]
                
                print(f"Subclasses are: {player.subclass}")
                if player.subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        for idx, subcl in enumerate(Arti, 1):
                            print(f"{idx} - {subcl}")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 0:
                            player.subclass[i] = random.choice(Arti)
                        elif 1 <= subc <= len(Arti):
                            player.subclass[i] = Arti[subc - 1]
                    if param == "N":
                        player.subclass[i] = random.choice(Arti)
                if player.subclass[i] == "Alchemist Specialist Artificer":
                    if dnd_tools.artisan_tools["AlchSupp"]["Name"] in player.proficiencies:
                        if param == "Y":
                            print(f"You already know {dnd_tools.artisan_tools["AlchSupp"]["Name"]}, please select a different tool to be proficient in.")
                        player.proficiencies = artisantools(param, player.proficiencies)
                    else:
                        player.proficiencies.append(dnd_tools.artisan_tools["AlchSupp"]["Name"])
                    player.classnotes.append("Alchemist Spells (see notes)")
                    player.notes.append("Alchemist Spells - You always have certain spells prepared after you reach particular levels in this class, as shown in the Alchemist Spells table. These spells count as artificer spells for you, but they don't count against the number of artificer spells you prepare.\n3rd Artificer Level: Healing Word, Ray of Sickness\n5th Artificer Level: Flaming Sphere, Melf's Acid Arrow\n9th Artificer Level: Gaseous Form, Mass Healing Word\n13th Artificer Level: Blight, Death Ward\n17th Artificer Level: Cloudkill, Raise Dead")
                    player.classnotes.append("Experimental Elixer (see notes)")
                    player.notes.append("Experimental Elixer - Whenever you finish a long rest, you can magically produce an experimental elixir in an empty flask you touch. Roll on the Experimental Elixir table for the elixir's effect, which is triggered when someone drinks the elixir. As an action, a creature can drink the elixir or administer it to an incapacitated creature.\nCreating an experimental elixir requires you to have alchemist supplies on your person, and any elixir you create with this feature lasts until it is drunk or until the end of your next long rest.\nWhen you reach certain levels in this class, you can make more elixirs at the end of a long rest, roll for each elixir's effect separately. Each elixir requires its own flask.\nYou can create additional experimental elixirs by expending a spell slot of 1st level or higher for each one. When you do so, you use your action to create the elixir in an empty flask you touch, and you choose the elixir's effect from the Experimental Elixir table.")
                    ArtElixers = 1
                    if artlvl >= 5:
                        player.classnotes.append("Alchemical Savant (see notes)")
                        player.notes.append(f"Alchemical Savant - You develop masterful command of magical chemicals, enhancing the healing and damage you create through them. Whenever you cast a spell using your alchemist's supplies as the spellcasting focus, you gain a bonus to one roll of the spell. That roll must restore hit points or be a damage roll that deals acid, fire, necrotic, or poison damage, and the bonus equals your Intelligence modifier, or bonus of {player.IntMod}, minimum of +1.")
                    if artlvl >= 6:
                        ArtElixers = 2
                    if artlvl >= 9:
                        player.classnotes.append("Restorative Reagents (see notes)")
                        player.notes.append(f"Restorative Reagents - You can incorporate restorative reagents into some of your works:\nWhenever a creature drinks an experimental elixir you created, the creature gains temporary hit points equal to 2d6 + your Intelligence modifier, or 2d6 + {player.IntMod} temporary hit points, minimum of 1 temporary hit point.\nYou can cast Lesser Restoration without expending a spell slot and without preparing the spell, provided you use alchemist's supplies as the spellcasting focus.\nYou can do so a number of times equal to your Intelligence modifier, or {player.IntMod} times, minimum of once, and you regain all expended uses when you finish a long rest.")
                    if artlvl >= 15:
                        ArtElixers = 3
                        player.classnotes.append("Chemical Mastery (see notes)")
                        player.notes.append("Chemical Mastery - You have been exposed to so many chemicals that they pose little risk to you, and you can use them to quickly end certain ailments:\nYou gain resistance to acid damage and poison damage, and you are immune to the poisoned condition.\nYou can cast Greater Restoration and Heal without expending a spell slot, without preparing the spell, and without material components, provided you use alchemist's supplies as the spellcasting focus.\nOnce you cast either spell with this feature, you can't cast that spell with it again until you finish a long rest.")
                    player.classnotes.append(f"You can produce {ArtElixers} elixer(s), rolling on the Experimental Elixer table.")
                if player.subclass[i] == "Armorer Specialist Artificer":
                    profs = ["Heavy Armor"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    if "Smith's Tools" in player.proficiencies:
                        if param == "Y":
                            print("You already know Smith's Tools, please select a different tool to be proficient in.")
                        player.proficiencies = artisantools(param, player.proficiencies)
                    else:
                        player.proficiencies.append(dnd_tools.artisan_tools["SmthTools"]["Name"])
                    player.classnotes.append("Armorer Spells (see notes")
                    player.notes.append("Armorer Spells - You always have certain spells prepared after you reach particular levels in this class, as shown in the Armorer Spells table. These spells count as artificer spells for you, but they don't count against the number of artificer spells you prepare.\n3rd Artificer Level: Magic Missile, Thunderwave\n5th Artificer Level: Mirror Image, Shatter\n9th Artificer Level: Hypnotic Pattern, Lightning Bolt\n13th Artificer Level: Fire Shield, Greater Invisibility\n17th Artificer Level: Passwall, Wall of Force")
                    player.classnotes.append("Arcane Armor (see notes)")
                    player.notes.append("Your metallurgical pursuits have led to you making armor a conduit for your magic. As an action, you can turn a suit of armor you are wearing into Arcane Armor, provided you have smith's tools in hand.\nYou gain the following benefits while wearing this armor:\nIf the armor normally has a Strength requirement, the arcane armor lacks this requirement for you.\nYou can use the arcane armor as a spellcasting focus for your artificer spells.\nThe armor attaches to you and can't be removed against your will. It also expands to cover your entire body, although you can retract or deploy the helmet as a bonus action. The armor replaces any missing limbs, functioning identically to a limb it replaces.\nYou can doff or don the armor as an action.\nThe armor continues to be Arcane Armor until you don another suit of armor or you die.")
                    player.classnotes.append("Armor Model (see notes)")
                    player.notes.append(f"Armor Model - You can customize your Arcane Armor. When you do so, choose one of the following armor models: Guardian or Infiltrator. The model you choose gives you special benefits while you wear it.\nEach model includes a special weapon. When you attack with that weapon, you can add your Intelligence modifier, or {player.IntMod}, instead of Strength or Dexterity, to the attack and damage rolls.\nYou can change the armor's model whenever you finish a short or long rest, provided you have smith's tools in hand.\nGuardian:\nYou design your armor to be in the front line of conflict. It has the following features:\nThunder Gauntlets. Each of the armor's gauntlets counts as a simple melee weapon while you aren't holding anything in it, and it deals 1d8 thunder damage on a hit. A creature hit by the gauntlet has disadvantage on attack rolls against targets other than you until the start of your next turn, as the armor magically emits a distracting pulse when the creature attacks someone else.\nDefensive Field. As a bonus action, you can gain temporary hit points equal to your level in this class, replacing any temporary hit points you already have. You lose these temporary hit points if you doff the armor. You can use this bonus action a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.\nInfiltrator:\nYou customize your armor for subtle undertakings. It has the following features:\nLightning Launcher. A gemlike node appears on one of your armored fists or on the chest (your choice). It counts as a simple ranged weapon, with a normal range of 90 feet and a long range of 300 feet. and it deals 1d6 lightning damage on a hit. Once on each of your turns when you hit a creature with it, you can deal an extra 1d6 lightning damage to that target.\nPowered Steps. Your walking speed increases by 5 feet.\nDampening Field. You have advantage on Dexterity (Stealth) checks. If the armor normally imposes disadvantage on such checks, the advantage and disadvantage cancel each other, as normal.")
                    if artlvl >= 5:
                        player.classnotes.append("Extra Attack - You can attack twice, rather than once, whenever you take the Attack action on your turn.")
                    if artlvl >= 9:
                        player.classnotes.append("Armor Modifications (see notes)")
                        player.notes.append("Armor Modifications - You learn how to use your artificer infusions to specially modify your Arcane Armor. That armor now counts as separate items for the purposes of your Infuse Items feature: armor (the chest piece), boots, helmet, and the armor's special weapon. Each of those items can bear one of your infusions, and the infusions transfer over if you change your armor's model with the Armor Model feature. In addition, the maximum number of items you can infuse at once increases by 2, but those extra items must be part of your Arcane Armor.")
                    if artlvl >= 15:
                        player.classnotes.append("Perfected Armor - Your Arcane Armor gains additional benefits based on its model. (see notes)")
                        player.notes.append(f"Perfected Armor - Your Arcane Armor gains additional benefits based on its model, as shown below.\nGuardian. When a Huge or smaller creature you can see ends its turn within 30 feet of you, you can use your reaction to magically force the creature to make a Strength saving throw against your spell save DC, or against {player.spellsavedc[i]}, pulling the creature up to 30 feet toward you to an unoccupied space. If you pull the target to a space within 5 feet of you, you can make a melee weapon attack against it as part of this reaction. You can use this reaction a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses of it when you finish a long rest.\nInfiltrator. Any creature that takes lightning damage from your Lightning Launcher glimmers with magical light until the start of your next turn. The glimmering creature sheds dim light in a 5-foot radius, and it has disadvantage on attack rolls against you, as the light jolts it if it attacks you. In addition, the next attack roll against it has advantage, and if that attack hits, the target takes an extra 1d6 lightning damage.")
                if player.subclass[i] == "Artilierist Specialist Artificer":
                    if "Woodcarver's Tools" in player.proficiencies:
                        if param == "Y":
                            print("You already know Woodcarver's Tools, please select a different tool to be proficient in.")
                        player.proficiencies = artisantools(param, player.proficiencies)
                    else:
                        player.proficiencies.append("Woodcarver's Tools")
                    player.classnotes.append("Artilierist Spells (see notes")
                    player.notes.append("Artilierist Spells - You always have certain spells prepared after you reach particular levels in this class, as shown in the Artillerist Spells table. These spells count as artificer spells for you, but they don't count against the number of artificer spells you prepare.\n3rd Artificer Level: Shield, Thunderwave\n5th Artificer Level: Scorching Ray, Shatter\n9th Artificer Level: Fireball, Wind Wall\n13th Artificer Level: Ice Storm, Wall of Fire\n17th Artificer Level: Cone of Cold, Wall of Force")
                    player.classnotes.append("Eldritch Cannon (see notes)")
                    player.notes.append(f"Eldritch Cannon - You learn how to create a magical cannon. Using woodcarver's tools or smith's tools, you can take an action to magically create a Small or Tiny eldritch cannon in an unoccupied space on a horizontal surface within 5 feet of you. A Small eldritch cannon occupies its space, and a Tiny one can be held in one hand.\nOnce you create a cannon, you can't do so again until you finish a long rest or until you expend a spell slot of 1st level or higher. You can have only one cannon at a time and can't create one while your cannon is present.\nThe cannon is a magical object. Regardless of size, the cannon has an AC of 18 and a number of hit points equal to five times your Artificer level, or {5*artlvl} Hit Points. It is immune to poison damage, psychic damage, and all conditions. If it is forced to make an ability check or a saving throw, treat all its ability scores as 10 (+0). If the Mending spell is cast on it, it regains 2d6 hit points. It disappears if it is reduced to 0 hit points or after 1 hour. You can dismiss it early as an action.\nWhen you create the cannon, you determine its appearance and whether it has legs. You also decide which type it is, choosing from the options on the Eldritch Cannons table. On each of your turns, you can take a bonus action to cause the cannon to activate if you are within 60 feet of it. As part of the same bonus action, you can direct the cannon to walk or climb up to 15 feet to an unoccupied space, provided it has legs.\nFlamethrower: The cannon exhales fire in an adjacent 15-foot cone that you designate. Each creature in that area must make a Dexterity saving throw against your spell save DC, or against {player.spellsavedc[i]}, taking 2d8 fire damage on a failed save or half as much damage on a successful one. The fire ignites any flammable objects in the area that aren't being worn or carried.\nForce Ballista: Make a ranged spell attack, originating from the cannon, at one creature or object within 120 feet of it. On a hit, the target takes 2d8 force damage, and if the target is a creature, it is pushed up to 5 feet away from the cannon.\nProtector: The cannon emits a burst of positive energy that grants itself and each creature of your choice with in 10 feet of it a number of temporary hit points equal to 1d8 + your Intelligence modifier, or 1d8 + {player.IntMod} temporary hitpoints, minimum of +1.")
                    if artlvl >= 5:
                        player.classnotes.append("Arcane Firearm (see notes)")
                        player.notes.append("Arcane Firearm - You know how to turn a wand, staff, or rod into an arcane firearm, a conduit for your destructive spells. When you finish a long rest, you can use woodcarver's tools to carve special sigils into a wand, staff, or rod and thereby turn it into your arcane firearm. The sigils disappear from the object if you later carve them on a different item. The sigils otherwise last indefinitely.\nYou can use your arcane firearm as a spellcasting focus for your artificer spells. When you cast an artificer spell through the firearm, roll a d8, and you gain a bonus to one of the spell's damage rolls equal to the number rolled.")
                    if artlvl >= 9:
                        player.classnotes.append("Explosive Cannon (see notes)")
                        player.notes.append(f"Explosive Cannon - Every eldritch cannon you create is more destructive:\nThe cannon's damage rolls all increase by 1d8.\nAs an action, you can command the cannon to detonate if you are within 60 feet of it. Doing so destroys the cannon and forces each creature within 20 feet of it to make a Dexterity saving throw against your spell save DC, or against {player.spellsavedc[i]}, taking 3d8 force damage on a failed save or half as much damage on a successful one.")
                    if artlvl >= 15:
                        player.classnotes.append("Fortified Position (see notes)")
                        player.notes.append("Fortified Position - You're a master at forming well-defended emplacements using Eldritch Cannon:\nYou and your allies have half cover while within 10 feet of a cannon you create with Eldritch Cannon, as a result of a shimmering field of magical protection that the cannon emits.\nYou can now have two cannons at the same time. You can create two with the same action (but not the same spell slot), and you can activate both of them with the same bonus action. You determine whether the cannons are identical to each other or different. You can't create a third cannon while you have two.")
                if player.subclass[i] == "Battle Smith Specialist Artificer":        
                    if "Smith's Tools" in player.proficiencies:
                        if param == "Y":
                            print("You already know Smith's Tools, please select a different tool to be proficient in.")
                        player.proficiencies = artisantools(param, player.proficiencies)
                    else:
                        player.proficiencies.append(dnd_tools.artisan_tools["SmthTools"]["Name"])
                    player.classnotes.append("Battle Smith Spells (see notes")
                    player.notes.append("Battle Smith Spells - You always have certain spells prepared after you reach particular levels in this class, as shown in the Battle Smith Spells table. These spells count as artificer spells for you, but they don't count against the number of artificer spells you prepare.\n3rd Artificer Level: Heroism, Shield\n5th Artificer Level: Branding Smite, Warding Bond\n9th Artificer Level: Aura of Vitality, Conjure Barrage\n13th Artificer Level: Aura of Purity, Fire Shield\n17th Artificer Level: Banishing Smite, Mass Cure Wounds")
                    profs = ["Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)  
                    player.classnotes.append("Battle Ready (see notes)")
                    player.notes.append(f"Battle Ready - Your combat training and your experiments with magic have paid off in two ways:\nYou gain proficiency with martial weapons (already in Proficiences).\nWhen you attack with a magic weapon, you can use your Intelligence modifier, or {player.IntMod}, instead of Strength or Dexterity modifier, for the attack and damage rolls.")
                    player.classnotes.append("Steel Defender (see notes)")
                    player.notes.append("Steel Defender - Your tinkering has borne you a faithful companion, a Steel Defender. It is friendly to you and your companions, and it obeys your commands. See this creature's game statistics in the steel defender stat block. You determine the creature's appearance and whether it has two legs or four; your choice has no effect on its game statistics.\nIn combat, the steel defender shares your initiative count, but it takes its turn immediately after yours. It can move and use its reaction on its own, but the only action it takes on its turn is the Dodge action, unless you take a bonus action on your turn to command it to take one of the actions in its stat block or the Dash, Disengage, Help, Hide, or Search action.\nIf the mending spell is cast on it, it regains 2d6 hit points. If it has died within the last hour, you can use your smith's tools as an action to revive it, provided you are within 5 feet of it and you expend a spell slot of 1st level or higher. The steel defender returns to life after 1 minute with all its hit points restored.\nAt the end of a long rest, you can create a new steel defender if you have your smith's tools with you. If you already have a steel defender from this feature, the first one immediately perishes.")
                    if artlvl >= 5:
                        player.classnotes.append("Extra Attack - You can attack twice, rather than once, whenever you take the Attack action on your turn.")
                    if artlvl >= 9:
                        player.classnotes.append("Arcane Jolt (see notes)")
                        player.notes.append(f"Arcane Jolt - You learn new ways to channel arcane energy to harm or heal. When either you hit a target with a magic weapon attack or your steel defender hits a target, you can channel magical energy through the strike to create one of the following effects:\nThe target takes an extra 2d6 force damage.\nChoose one creature or object you can see within 30 feet of the target. Healing energy flows into the chosen recipient, restoring 2d6 hit points to it. You can use this energy a number of times equal to your Intelligence modifier, or {player.IntMod} times, minimum of once, but you can do so no more than once on a turn. You regain all expended uses when you finish a long rest.")
                    if artlvl >= 15:
                        player.classnotes.append("Improved Defender (see notes)")
                        player.notes.append(f"Improved Defender - Your Arcane jolt and Steel Defender become more powerful:\nThe extra damage and the healing of your Arcane jolt both increase to 4d6.\nYour steel defender gains a +2 bonus to Armor Class.\nWhenever your steel defender uses its Deflect Attack, the attacker takes force damage equal to 1d4 + your Intelligence modifier, or 1d4 + {player.IntMod} force damage.")
                ArtSpellSlot1 = 3
            if artlvl >= 5:
                ArtSpellSlot1 = 4
                ArtSpellSlot2 = 2
            if artlvl >= 6:
                player.classnotes.append("Tool Expertise - Your Proficiency Bonus is doubled for any ability check you make that uses your proficiency with a tool.")
                InfusionNumber = 6
                InfusedItem = 3
            if artlvl >= 7:
                player.classnotes.append("Flash Of Genius (see notes)")
                player.notes.append(f"Flash Of Genius - You gain the ability to come up with solutions under pressure. When you or another creature you can see within 30 feet of you makes an ability check or a saving throw, you can use your reaction to add your Intelligence modifier, or {player.IntMod}, to the roll.\nYou can use this feature a number of times equal to your Intelligence modifier, or {player.IntMod} times, minimum of once. You regain all expended uses when you finish a long rest.")
                ArtSpellSlot2 = 3
            if artlvl >= 9:
                ArtSpellSlot3 = 2
            if artlvl >= 10:
                player.classnotes.append("Magic Item Adept - You achieve a profound understanding of how to use and make magic items:\nYou can attune to up to four magic items at once.\nIf you craft a magic item with a rarity of common or uncommon, it takes you a quarter of the normal time, and it costs you half as much of the usual gold.")
                InfusionNumber = 8
                InfusedItem = 4
                ArtCantripsKnown = 3
            if artlvl >= 11:
                player.classnotes.append("Spell-Storing Item (see notes)")
                player.notes.append(f"Spell-Storing Item - You learn how to store a spell in an object. Whenever you finish a long rest, you can touch one simple or martial weapon or one item that you can use as a spellcasting focus, and you store a spell in it, choosing a 1st- or 2nd-level spell from the artificer spell list that requires 1 action to cast (you needn't have it prepared).\nWhile holding the object, a creature can take an action to produce the spell's effect from it, using your spellcasting ability modifier. If the spell requires concentration, the creature must concentrate. The spell stays in the object until it's been used a number of times equal to twice your Intelligence modifier, or {2*player.IntMod} times, minimum of twice or until you use this feature again to store a spell in an object.")
                ArtSpellSlot3 = 3
            if artlvl >= 14:
                player.classnotes.append("Magic Item Savant - Your skill with magic items deepens more: You can attune to up to five magic items at once. You ignore all class, race, spell, and level requirements on attuning to or using a magic item.")
                InfusionNumber = 10
                InfusedItem = 5
                ArtCantripsKnown = 4
            if artlvl >= 15:
                ArtSpellSlot4 = 2
            if artlvl >= 17:
                ArtSpellSlot4 = 3
                ArtSpellSlot5 = 1
            if artlvl >= 18:
                player.classnotes.append("Magic Item Master - You can attune to up to six magic items at once.")
                InfusionNumber = 12
                InfusedItem = 6
            if artlvl >= 19:
                ArtSpellSlot5 = 2
            if artlvl == 20:
                player.classnotes.append("Soul Of Artifice (see notes)")
                player.notes.append("Soul Of Artifice - You develop a mystical connection to your magic items, which you can draw on for protection:\nYou gain a +1 bonus to all saving throws per magic item you are currently attuned to.\nIf you're reduced to 0 hit points but not killed outright, you can use your reaction to end one of your artificer infusions, causing you to drop to 1 hit point instead of 0.")
            player.classnotes.append(f"You know {InfusionNumber} infusions and can infuse {InfusedItem} items.")
            player.notes.append(f"You have {ArtCantripsKnown} cantrips available to you.")
            if ArtSpellSlot1 != 0:
                player.notes.append(f"The number of first level spell slots you have as a Artificer is: {ArtSpellSlot1}.")
            if ArtSpellSlot2 != 0:
                player.notes.append(f"The number of second level spell slots you have as a Artificer is: {ArtSpellSlot2}.")
            if ArtSpellSlot3 != 0:                
                player.notes.append(f"The number of third level spell slots you have as a Artificer is: {ArtSpellSlot3}.")
            if ArtSpellSlot4 != 0:
                player.notes.append(f"The number of fourth level spell slots you have as a Artificer is: {ArtSpellSlot4}.")
            if ArtSpellSlot5 != 0:
                player.notes.append(f"The number of fifth level spell slots you have as a Artificer is: {ArtSpellSlot5}.")            
            #See if I can f-string anything
        if player.Class[i] == "Barbarian":
            print(f"i is still {i}")
            if ((param == "N") or (player.singlemulticlass == "N")):
                barblvl = player.level
                player.classlvl.append(barblvl)              
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    barblvl = int(input(f"Given your pool of levels of {poollevel}, what is your Barbarian level? "))   
                    if barblvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                    
                poollevel = poollevel - barblvl
                player.classlvl.append(barblvl)
            if barblvl >= 1:
                player.hitdice.append(f"{barblvl}d12 for {player.Class[i]}")
                if barblvl == 1:
                    player.hitpoints += (12 + player.ConMod)
                else:
                    player.hitpoints += (12 + player.ConMod + hpcalc(barblvl, dice, 12))
                if i == 0:
                    profs = ["Light Armor", "Medium Armor", "Shield", "Simple Weapons", "Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    player.skills.append(dnd_tools.saving_throws["StrST"])
                    player.skills.append(dnd_tools.saving_throws["ConST"])
                    BarbSkillsList = [
                        dnd_tools.skills["AnimalHandling"], 
                        dnd_tools.skills["Athletics"], 
                        dnd_tools.skills["Intimidation"], 
                        dnd_tools.skills["Nature"], 
                        dnd_tools.skills["Perception"], 
                        dnd_tools.skills["Survival"]
                        ]
                    player.skills = twoskillsfromlist(param, player.skills, BarbSkillsList)
                    StartEquip1 = ["Greataxe", "Martial Melee Weapon"]
                    StartEquip2 = ["Two Handaxes", "Any Simple Weapon"]
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Greataxe")
                        print("2 - Martial Melee Weapon")
                        se1 = int(input("What would you like your first choice for starting equipment to be? "))
                        if se1 == 0:
                            SE1rand = random.choice(StartEquip1)
                            if SE1rand == "Greataxe":
                                player.equipment.append(dnd_tools.martial_weapons["Greataxe"].copy())
                            if SE1rand == "Martial Melee Weapon":
                                MartWepRandKey = random.choice(MartialMeleeWeapons)
                                player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey].copy())
                        if se1 == 1:
                            player.equipment.append(dnd_tools.martial_weapons["Greataxe"].copy())
                        if se1 == 2:
                            print("0 - Random")
                            for j, mmw in enumerate(MartialMeleeWeaponsNames, 1):
                                print(f"{j} - {mmw}")
                            se1mmw = int(input("Which martial melee weapon would you like to add to your inventory? "))
                            if se1mmw == 0:
                                MartWepRandKey = random.choice(MartialMeleeWeapons)
                                player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey].copy())
                            elif 1 <= se1mmw <= len(MartialMeleeWeapons):
                                MartWepKey = MartialMeleeWeapons[se1mmw-1]
                                player.equipment.append(dnd_tools.martial_weapons[MartWepKey].copy())
                        print("0 - Random")
                        print("1 - Two Handaxes")
                        print("2 - Any Simple Weapon")
                        se2 = int(input("What would you like your second choice for starting equipment to be? "))
                        if se2 == 0:
                            SE2rand = random.choice(StartEquip2)
                            if SE2rand == "Two Handaxes":
                                player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                                player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                            if SE2rand == "Any Simple Weapon":
                                SimpRandKey = random.choice(SimpleWeapons)
                                player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                        if se2 == 1:
                            player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                            player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                        if se2 == 2:
                            print("0 - Random")
                            for j, sw in enumerate(SimpleWeaponsNames, 1):
                                print(f"{j} - {sw}")
                            se2sw = int(input("Which simple weapon would you like to add to your inventory? "))
                            if se2sw == 0:
                                SimpRandKey = random.choice(SimpleWeapons)
                                player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                            elif 1 <= se2sw <= len(SimpleWeapons):
                                SimpKey = SimpleWeapons[se2sw-1]
                                player.equipment.append(dnd_tools.simple_weapons[SimpKey].copy())
                        player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])
                        for idx in range(1,4):
                            player.equipment.append(dnd_tools.simple_weapons["Javelin"].copy())
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "Greataxe":
                            player.equipment.append(dnd_tools.martial_weapons["Greataxe"].copy())
                        if SE1rand == "Martial Melee Weapon":
                            MartWepRandKey = random.choice(MartialMeleeWeapons)
                            player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey].copy())
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "Two Handaxes":
                            player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                            player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                        if SE2rand == "Any Simple Weapon":
                            SimpRandKey = random.choice(SimpleWeapons)
                            player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                        player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])
                        for idx in range(1,4):
                            player.equipment.append(dnd_tools.simple_weapons["Javelin"].copy())
                else:
                    profs = ["Shield", "Simple Weapons", "Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)                                                                    
                print(f"Barblevel is {barblvl}")
                Rages = "2"
                RageDmg = 2
                if barblvl >= 3:
                    Rages = "3"
                if barblvl >= 6:
                    Rages = "4"
                if barblvl >= 9:
                    RageDmg = 3
                if barblvl >= 12:
                    Rages = "5"
                if barblvl >= 16:
                    RageDmg = 4
                if barblvl >= 17:
                    Rages = "6"
                if barblvl == 20:
                    Rages = "Unlimited"
                player.classnotes.append("Rage (see notes)")
                player.notes.append(f"Rage - In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action.\nWhile raging, you gain the following benefits if you aren’t wearing heavy armor:\nYou have advantage on Strength checks and Strength saving throws.\nWhen you make a melee weapon attack using Strength, you gain a +{RageDmg} to your damage roll.\nYou have resistance to bludgeoning, piercing, and slashing damage.\nIf you are able to cast spells, you can’t cast them or concentrate on them while raging.\nYour rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven’t attacked a hostile creature since your last turn or taken damage since then. You can also end your rage on your turn as a bonus action.\nOnce you have raged {Rages} times, you must finish a long rest before you can rage again.")
                player.classnotes.append(f"Unarmored Defense - While you are not wearing any armor, your Armor Class equals 10 + your Dexterity modifier + your Constitution modifier, or AC {10 + player.DexMod + player.ConMod}. You can use a shield and still gain this benefit.")
            if barblvl >= 2:
                player.classnotes.append("Reckless Attack (see notes)")
                player.notes.append("Reckless Attack - You can throw aside all concern for defense to attack with fierce desperation. When you make your first attack on your turn, you can decide to attack recklessly. Doing so gives you advantage on melee weapon attack rolls using Strength during this turn, but attack rolls against you have advantage until your next turn.")
                player.classnotes.append("Danger Sense (see notes)")
                player.notes.append("Danger Sense - You gain an uncanny sense of when things nearby aren’t as they should be, giving you an edge when you dodge away from danger.\nYou have advantage on Dexterity saving throws against effects that you can see, such as traps and spells. To gain this benefit, you can’t be blinded, deafened, or incapacitated.")
            if barblvl >= 3:
                Barb = ["Path of the Ancestral Guardian Barbarian", "Path of the Battlerager Barbarian", "Path of the Beast Barbarian", "Path of the Berserker Barbarian", "Path of the Giant Barbarian", "Path of the Juggernaut Barbarian", "Path of the Storm Herald Barbarian", "Path of the Totem Warrior Barbarian", "Path of the Zealot Barbarian", "Path of the Wild Magic Barbarian"]            
                print(f"Subclasses are: {player.subclass}")
                print(f"At this point, i should still be {i}")
                if player.subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        for idx, subcl in enumerate(Barb, 1):
                            print(f"{idx} - {subcl}")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 0:
                            player.subclass[i] = random.choice(Barb)
                        elif 1 <= subc <= len(Barb):
                            player.subclass[i] = Barb[subc - 1]
                    if param == "N":
                        player.subclass[i] = random.choice(Barb)         
                if player.subclass[i] == "Path of the Ancestral Guardian Barbarian":
                    player.classnotes.append("Ancestral Protectors (see notes)")
                    player.notes.append("Ancestral Protectors - Spectral warriors appear when you enter your rage. While you’re raging, the first creature you hit with an attack on your turn becomes the target of the warriors, which hinder its attacks. Until the start of your next turn, that target has disadvantage on any attack roll that isn't against you, and when the target hits a creature other than you with an attack, that creature has resistance to the damage of the target’s attacks.")
                    if barblvl >= 6:
                        SpiritShieldReduction = "2d6"
                        if barblvl >= 10:
                            SpiritShieldReduction = "3d6"
                        if barblvl >= 14:
                            SpiritShieldReduction = "4d6"
                        player.classnotes.append("Spirit Shield (see notes)")
                        player.notes.append(f"Spirit Shield - The guardian spirits that aid you can provide supernatural protection to those you defend. If you are raging and a creature you can see within 30 feet of you takes damage, you can use your reaction to reduce that damage by {SpiritShieldReduction}.")
                    if barblvl >= 10:
                        player.classnotes.append("Consult the Spirits (see notes)")
                        player.notes.append("Consult the Spirits - You gain the ability to consult with your ancestral spirits. When you do so, you cast the Augury or Clairvoyance spell, without using a spell slot or material components. Rather than creating a spherical sensor, this use of Clairvoyance invisibly summons one of your ancestral spirits to the chosen location. Wisdom is your spellcasting ability for these spells.\nAfter you cast either spell in this way, you can’t use this feature again until you finish a short or long rest.")
                    if barblvl >= 14:
                        player.classnotes.append("Vengeful Ancestors - Your ancestral spirits grow powerful enough to retaliate. When you use your Spirit Shield to reduce the damage of an attack, the attacker takes an amount of force damage that your Spirit Shield prevents.")
                if player.subclass[i] == "Path of the Battlerager Barbarian":
                    player.classnotes.append("Battlerager Armor (see notes)")
                    player.notes.append(f"Battlerager Armor - You gain the ability to use spiked armor as a weapon.\nWhile you are wearing Spiked Armor and are raging, you can use a bonus action to make one melee weapon attack with your armor spikes against a target within 5 feet of you. If the attack hits, the spikes deal 1d4 piercing damage. You use your Strength modifier, or {player.StrMod}, for the attack and damage rolls.\nAdditionally, when you use the Attack action to grapple a creature, the target takes 3 piercing damage if your grapple check succeeds.")
                    if barblvl >= 6:
                        player.classnotes.append("Reckless Abandon (see notes)")
                        player.notes.append(f"Reckless Abandon - When you use Reckless Attack while raging, you also gain temporary hit points equal to your Constitution modifier, or {player.ConMod} temporary hit points, minimum of 1. They vanish if any of them are left when your rage ends.")
                    if barblvl >= 10:
                        player.classnotes.append("Battlerager Charge - You can take the Dash action as a bonus action while you are raging.")
                    if barblvl >= 14:
                        player.classnotes.append("Spiked Retribution - When a creature within 5 feet of you hits you with a melee attack, the attacker takes 3 piercing damage if you are raging, aren't incapacitated, and are wearing spiked armor.")
                if player.subclass[i] == "Path of the Beast Barbarian":
                    BPBO1 = "One of your parents is a lycanthrope, and you've inherited some of their curse."
                    BPBO2 = "You are descended from an archdruid and inherited the ability to partially change shape."
                    BPBO3 = "A fey spirit gifted you with the ability to adopt different bestial aspects."
                    BPBO4 = "An ancient animal spirit dwells within you, allowing you to walk this path."
                    BPBO = [BPBO1, BPBO2, BPBO3, BPBO4]
                    BarbPathBeastOrigin = random.choice(BPBO)
                    player.classnotes.append(f"As a Path of the Beast Barbarian, the Origin of the Beast is: {BarbPathBeastOrigin}")                  
                    player.classnotes.append("Form of the Beast (see notes)")
                    player.notes.append(f"Form of the Beast - When you enter your rage, you can transform, revealing the bestial power within you. Until the rage ends, you manifest a natural weapon. It counts as a simple melee weapon for you, and you add your Strength modifier, or {player.StrMod}, to the attack and damage roll when you attack with it, as normal.\nYou choose the weapon's form each time you rage:\nBite - Your mouth transforms into a bestial muzzle or great mandibles (your choice). It deals 1d8 piercing damage on a hit. Once on each of your turns when you damage a creature with this bite, you regain a number of hit points equal to your Proficiency Bonus, or {player.profbonus} hit points, provided you have less than half your hit points when you hit.\nClaws - Each of your hands transforms into a claw, which you can use as a weapon if it's empty. It deals 1d6 slashing damage on a hit. Once on each of your turns when you attack with a claw using the Attack action, you can make one additional claw attack as part of the same action.\nTail - You grow a lashing, spiny tail, which deals 1d8 piercing damage on a hit and has the reach property. If a creature you can see within 10 feet of you hits you with an attack roll, you can use your reaction to swipe your tail and roll a d8, applying a bonus to your AC equal to the number rolled, potentially causing the attack to miss you.")
                    if barblvl >= 6:
                        player.classnotes.append("Bestial Soul (see notes)")
                        player.notes.append("Bestial Soul - The feral power within you increases, causing the natural weapons of your Form of the Beast to count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage.\nYou can also alter your form to help you adapt to your surroundings. When you finish a short or long rest, choose one of the following benefits, which lasts until you finish your next short or long rest:\n- You gain a swimming speed equal to your walking speed, and you can breathe underwater.\n- You gain a climbing speed equal to your walking speed, and you can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.\n- When you jump, you can make a Strength (Athletics) check and extend your jump by a number of feet equal to the check's total. You can make this special check only once per turn.")
                    if barblvl >= 10:
                        player.classnotes.append("Infectious Fury (see notes)")
                        player.notes.append(f"Infectious Fury - When you hit a creature with your natural weapons while you are raging, the beast within you can curse your target with rabid fury. The target must succeed on a Wisdom saving throw, DC of 8 + your Constitution modifier + your Proficiency Bonus, or DC of {8 + player.ConMod + player.profbonus}, or suffer one of the following effects (your choice):\n- The target must use its reaction to make a melee attack against another creature of your choice that you can see.\n- The target takes 2d12 psychic damage.\nYou can use this feature a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
                    if barblvl >= 14:
                        player.classnotes.append("Call the Hunt (see notes)")
                        player.notes.append(f"Call the Hunt - The beast within you grows so powerful that you can spread its ferocity to others and gain resilience from them joining your hunt. When you enter your rage, you can choose a number of other willing creatures you can see within 30 feet of you equal to your Constitution modifier, or {player.ConMod} creatures, minimum of one creature. You gain 5 temporary hit points for each creature that accepts this feature. Until the rage ends, the chosen creatures can each use the following benefit once on each of their turns: when the creature hits a target with an attack roll and deals damage to it, the creature can roll a d6 and gain a bonus to the damage equal to the number rolled.\nYou can use this feature a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
                if player.subclass[i] == "Path of the Berserker Barbarian":
                    player.classnotes.append("Frenzy - You can go into a frenzy when you rage. If you do so, for the duration of your rage you can make a single melee weapon attack as a bonus action on each of your turns after this one. When your rage ends, you suffer one level of exhaustion.")
                    if barblvl >= 6:
                        player.classnotes.append("Mindless Rage - You can't be charmed or frightened while raging. If you are charmed or frightened when you enter your rage, the effect is suspended for the duration of the rage.")
                    if barblvl >= 10:
                        player.classnotes.append(f"Intimidating Presence - You can use your action to frighten someone with your menacing presence. When you do so, choose one creature that you can see within 30 feet of you. If the creature can see or hear you, it must succeed on a Wisdom saving throw, DC of 8 + your Proficiency Bonus + your Charisma modifier, or DC {8 + player.profbonus + player.ChaMod}, or be frightened of you until the end of your next turn. On subsequent turns, you can use your action to extend the duration of this effect on the frightened creature until the end of your next turn. This effect ends if the creature ends its turn out of line of sight or more than 60 feet away from you.\nIf the creature succeeds on its saving throw, you can't use this feature on that creature again for 24 hours.")
                    if barblvl >= 14:
                        player.classnotes.append("Retaliation - When you take damage from a creature that is within 5 feet of you, you can use your reaction to make a melee weapon attack against that creature.")
                if player.subclass[i] == "Path of the Giant Barbarian":
                    player.classnotes.append("Giant Power - You learn to speak, read, and write Giant or one other language of your choice if you already know Giant. Additionally, you learn a cantrip of your choice: either Druidcraft or Thaumaturgy. Wisdom is your spellcasting ability for this spell.")
                    player.classnotes.append("Giant's Havoc (see notes)")
                    player.notes.append("Giant's Havoc - Your rages pull strength from the primal might of giants, transforming you into a hulking force of destruction. While raging, you gain the following benefits:\n- Crushing Throw: When you make a successful ranged attack with a thrown weapon using Strength, you can add your Rage Damage bonus to the attack's damage roll.\n- Giant Stature: Your reach increases by 5 feet, and if you are smaller than Large, you become Large, along with anything you are wearing. If there isn't enough room for you to increase your size, your size doesn't change.")
                    if barblvl >= 6:
                        player.classnotes.append("Elemental Cleaver (see notes)")
                        player.notes.append("Elemental Cleaver - Your bond with the elemental might of giants grows, and you learn to infuse weapons with primordial energy.\nWhen you enter your rage, you can choose one weapon that you are holding and infuse it with one of the following damage types: acid, cold, fire, thunder, or lightning. While you wield the infused weapon during your rage, the weapon's damage type changes to the chosen type, it deals an extra 1d6 damage of the chosen type when it hits, and it gains the thrown property, with a normal range of 20 feet and a long range of 60 feet. If you throw the weapon, it reappears in your hand the instant after it hits or misses a target. The infused weapon's benefits are suppressed while a creature other than you wields it.\nWhile raging and holding the infused weapon, you can use a bonus action to change the infused weapon's current damage type to another one from the damage type options above.")
                    if barblvl >= 10:
                        player.classnotes.append("Mighty Impel (see notes)")
                        player.notes.append(f"Mighty Impel - Your connection to giant strength allows you to hurl both allies and enemies on the battlefield. As a bonus action while raging, you can choose one Medium or smaller creature within your reach and move it to an unoccupied space you can see within 30 feet of yourself. An unwilling creature must succeed on a Strength saving throw, DC of 8 + your Proficiency Bonus + your Strength modifier, or DC {8 + player.profbonus + player.StrMod}, to avoid the effect.\nIf, at the end of this movement, the thrown creature isn't on a surface or liquid that can support it, the creature falls, taking damage as normal and landing prone.")
                    if barblvl >= 14:
                        player.classnotes.append("Demiurgic Colossus (see notes)")
                        player.notes.append("Demiurgic Colossus - The primordial power of your rage intensifies. When you rage, your reach increases by 10 feet, your size can increase to Large or Huge (your choice), and you can use your Mighty Impel to move creatures that are Large or smaller.\nIn addition, the extra damage dealt by your Elemental Cleaver feature increases to 2d6.")
                if player.subclass[i] == "Path of the Juggernaut Barbarian":
                    player.classnotes.append("Thunderous Blows(1) (see notes)")
                    player.notes.append(f"Thunderous Blows(1) - Your rage instills you with the strength to shove and smash your way through your foes, making any battlefield your domain. When you hit a creature with a melee attack while you're raging, you can push that creature up to 5 feet away from you in a direction of your choice. A creature that is Huge or larger makes a Strength saving throw with a DC of 8 + your Proficiency Bonus + your Strength modifier, or DC {8 + player.profbonus + player.StrMod}. On a success, the creature is not pushed.")
                    player.classnotes.append("Spirit of the Mountain - You harness your fury to anchor your feet to the ground, becoming a bulwark of strength. While you are raging, you can't be knocked prone or moved along the ground against your will.")
                    if barblvl >= 6:
                        player.classnotes.append("Demolishing Might - Your melee weapon attacks deal an extra 1d8 damage to constructs, and deal double damage to objects and structures.")
                        player.classnotes.append("Resolute Stance (see notes)")
                        player.notes.append("Resolute Stance - You can temporarily refocus your combat ability to make yourself a bulwark of defense. At the start of your turn (no action required), you can assume a defensive stance that lasts until the start of your next turn. While in this stance, you can't be grappled, attack rolls against you have disadvantage, and your weapon attacks are made with disadvantage.")
                    if barblvl >= 10:
                        player.classnotes.append("Thunderous Blows(2) (see notes)")
                        player.notes.append("Thunderous Blows(2) - You can push a creature up to 10 feet when you hit it with a melee attack while you're raging.")
                        player.classnotes.append("Hurricane Strike (see notes)")
                        player.notes.append(f"Hurricane Strike - Your blows can hurl foes through the air and into the attacks of your allies. As a reaction when you push a creature at least 5 feet, you can then leap into an unoccupied space next to the creature. If you do so, the creature must succeed on a Strength saving throw with a DC equal to 8 + your Proficiency Bonus + your Strength modifier, or DC {8 + player.profbonus + player.StrMod}, or be knocked prone. This leap costs no movement and does not provoke opportunity attacks.\nAdditionally, whenever you push a creature into a space within 5 feet of one of your allies, the ally can use its reaction to make a melee weapon attack against that creature.")
                    if barblvl >= 14:
                        player.classnotes.append("Unstoppable (see notes)")
                        player.notes.append("Unstoppable - Your fury in battle makes you unstoppable. While you're raging, your speed cannot be reduced, and you are immune to the frightened, paralyzed, prone, and stunned conditions.\nIf you are frightened, paralyzed, or stunned, you can still use a bonus action to enter a rage (even if you can't otherwise take actions). You aren't affected by any of these conditions while you're raging.")
                if player.subclass[i] == "Path of the Storm Herald Barbarian":
                    player.classnotes.append("Storm Aura (see notes)")
                    player.notes.append(f"Storm Aura - You emanate a stormy, magical aura while you rage. The aura extends 10 feet from you in every direction, but not through total cover.\nYour aura has an effect that activates when you enter your rage, and you can activate the effect again on each of your turns as a bonus action. Choose desert, sea, or tundra. Your aura's effect depends on that chosen environment, as detailed below. You can change your environment choice whenever you gain a level in this class.\nIf your aura's effects require a saving throw, the DC equals 8 + your Proficiency Bonus + your Constitution modifier, or DC {8 + player.profbonus + player.ConMod}.\nDesert - When this effect is activated, all other creatures in your aura take 2 fire damage each. The damage increases when you reach certain levels in this class, increasing to 3 at 5th level, 4 at 10th level, 5 at 15th level, and 6 at 20th level.\nSea - When this effect is activated, you can choose one other creature you can see in your aura. The target must make a Dexterity saving throw. The target takes 1d6 lightning damage on a failed save, or half as much damage on a successful one. The damage increases when you reach certain levels in this class, increasing to 2d6 at 10th level, 3d6 at 15th level, and 4d6 at 20th level.\nTundra - When this effect is activated, each creature of your choice in your aura gains 2 temporary hit points, as icy spirits inure it to suffering. The temporary hit points increase when you reach certain levels in this class, increasing to 3 at 5th level, 4 at 10th level, 5 at 15th level, and 6 at 20th level.")
                    if barblvl >= 6:
                        player.classnotes.append("Storm Soul (see notes)")
                        player.notes.append("Storm Soul - The storm grants you benefits even when your aura isn't active. The benefits are based on the environment you chose for your Storm Aura.\nDesert - You gain resistance to fire damage, and you don’t suffer the effects of extreme heat, as described in the Dungeon Master's Guide. Moreover, as an action, you can touch a flammable object that isn't being worn or carried by anyone else and set it on fire.\nSea - You gain resistance to lightning damage, and you can breathe underwater. You also gain a swimming speed of 30 feet.\nTundra - You gain resistance to cold damage, and you don’t suffer the effects of extreme cold, as described in the Dungeon Master's Guide. Moreover, as an action, you can touch water and turn a 5-foot cube of it into ice, which melts after 1 minute. This action fails if a creature is in the cube.")
                    if barblvl >= 10:
                        player.classnotes.append("Shielding Storm - You learn to use your mastery of the storm to protect others. Each creature of your choice has the damage resistance you gained from the Storm Soul feature while the creature is in your Storm Aura.")
                    if barblvl >= 14:
                        player.classnotes.append("Raging Storm (see notes)")
                        player.notes.append(f"Raging Storm - The power of the storm you channel grows mightier, lashing out at your foes. The effect is based on the environment you chose for your Storm Aura.\nDesert - Immediately after a creature in your aura hits you with an attack, you can use your reaction to force that creature to make a Dexterity saving throw. On a failed save, the creature takes fire damage equal to your Barbarian level, or {barblvl} fire damage.\nSea - When you hit a creature in your aura with an attack, you can use your reaction to force that creature to make a Strength saving throw. On a failed save, the creature is knocked prone, as if struck by a wave.\nTundra - Whenever the effect of your Storm Aura is activated, you can choose one creature you can see in the aura. That creature must succeed on a Strength saving throw, or its speed is reduced to 0 until the start of your next turn, as magical frost covers it.")
                if player.subclass[i] == "Path of the Totem Warrior Barbarian":
                    player.classnotes.append("Spirit Seeker - Yours is a path that seeks attunement with the natural world, giving you a kinship with beasts. You gain the ability to cast the Beast Sense and Speak with Animals spells, but only as rituals.")
                    player.classnotes.append("Totem Spirit (see notes)")
                    player.notes.append("Totem Spirit - When you adopt this path, you choose a totem spirit and gain its feature. You must make or acquire a physical totem object – an amulet or similar adornment – that incorporates fur or feathers, claws, teeth, or bones of the totem animal. At your option, you also gain minor physical attributes that are reminiscent of your totem spirit. For example, if you have a bear totem spirit, you might be unusually hairy and thick-skinned, or if your totem is the eagle, your eyes turn bright yellow.\nYour totem animal might be an animal related to those listed here but more appropriate to your homeland. For example, you could choose a hawk or vulture in place of an eagle.\nBear - While raging, you have resistance to all damage except psychic damage. The spirit of the bear makes you tough enough to stand up to any punishment.\nEagle - While you're raging and aren't wearing heavy armor, other creatures have disadvantage on opportunity attack rolls against you, and you can use the Dash action as a bonus action on your turn. The spirit of the eagle makes you into a predator who can weave through the fray with ease.\nElk - While you're raging and aren't wearing heavy armor, your walking speed increases by 15 feet. The spirit of the elk makes you extraordinarily swift.\nTiger - While raging, you can add 10 feet to your long jump distance and 3 feet to your high jump distance. The spirit of the tiger empowers your leaps.\nWolf - While you're raging, your friends have advantage on melee attack rolls against any creature within 5 feet of you that is hostile to you. The spirit of the wolf makes you a leader of hunters.")
                    if barblvl >= 6:
                        player.classnotes.append("Aspect of the Beast (see notes)")
                        player.notes.append("Aspect of the Beast - You gain a magical benefit based on the totem animal of your choice. You can choose the same animal you selected at 3rd level or a different one.\nBear - You gain the might of a bear. Your carrying capacity (including maximum load and maximum lift) is doubled, and you have advantage on Strength checks made to push, pull, lift, or break objects.\nEagle - You gain the eyesight of an eagle. You can see up to 1 mile away with no difficulty, able to discern even fine details as though looking at something no more than 100 feet away from you. Additionally, dim light doesn't impose disadvantage on your Wisdom (Perception) checks.\nElk - Whether mounted or on foot, your travel pace is doubled, as is the travel pace of up to ten companions while they're within 60 feet of you and you're not incapacitated. The elk spirit helps you roam far and fast.\nTiger - You gain proficiency in two skills from the following list: Athletics, Acrobatics, Stealth, and Survival. The cat spirit hones your survival instincts.\nWolf - You gain the hunting sensibilities of a wolf. You can track other creatures while traveling at a fast pace, and you can move stealthily while traveling at a normal pace.")
                    if barblvl >= 10:
                        player.classnotes.append("Spirit Walker - You can cast the Commune with Nature spell, but only as a ritual. When you do so, a spiritual version of one of the animals you chose for Totem Spirit or Aspect of the Beast appears to you to convey the information you seek.")
                    if barblvl >= 14:
                        player.classnotes.append("Totemic Attunement (see notes)")
                        player.notes.append(f"Totemic Attunement - You gain a magical benefit based on a totem animal of your choice. You can choose the same animal you selected previously or a different one.\nBear - While you're raging, any creature within 5 feet of you that's hostile to you has disadvantage on attack rolls against targets other than you or another character with this feature. An enemy is immune to this effect if it can't see or hear you or if it can't be frightened.\nEagle - While raging, you have a flying speed equal to your current walking speed. This benefit works only in short bursts; you fall if you end your turn in the air and nothing else is holding you aloft.\nElk - While raging, you can use a bonus action during your move to pass through the space of a Large or smaller creature. That creature must succeed on a Strength saving throw, the DC equal to 8 + your Strength modifier + your Proficiency Bonus, or DC of {8 + player.StrMod + player.profbonus}, or be knocked prone and take bludgeoning damage equal to 1d12 + your Strength modifier, or 1d12 + {player.StrMod} bludgeoning damage.\nTiger - While you're raging, if you move at least 20 feet in a straight line toward a Large or smaller target right before making a melee weapon attack against it, you can use a bonus action to make an additional melee weapon attack against it.\nWolf - While you're raging, you can use a bonus action on your turn to knock a Large or smaller creature prone when you hit it with melee weapon attack.")
                if player.subclass[i] == "Path of the Zealot Barbarian":
                    player.classnotes.append(f"Divine Fury - You can channel divine fury into your weapon strikes. While you're raging, the first creature you hit on each of your turns with a weapon attack takes extra damage equal to 1d6 + half your Barbarian level, or 1d6 + {math.floor(barblvl/2)} extra damage. The extra damage is necrotic or radiant; you choose the type of damage when you gain this feature.")
                    player.classnotes.append("Warrior of the Gods - Your soul is marked for endless battle. If a spell, such as Raise Dead, has the sole effect of restoring you to life (but not undeath), the caster doesn't need material components to cast the spell on you.")
                    if barblvl >= 6:
                        player.classnotes.append("Fanatical Focus - The divine power that fuels your rage can protect you. If you fail a saving throw while raging, you can reroll it, and you must use the new roll. You can use this ability only once per rage.")
                    if barblvl >= 10:
                        player.classnotes.append("Zealous Presence (see notes)")
                        player.notes.append("Zealous Presence - You learn to channel divine power to inspire zealotry in others. As a bonus action, you unleash a battle cry infused with divine energy. Up to ten other creatures of your choice within 60 feet of you that can hear you gain advantage on attack rolls and saving throws until the start of your next turn.\nOnce you use this feature, you can’t use it again until you finish a long rest.")
                    if barblvl >= 14:
                        player.classnotes.append("Rage Beyond Death (see notes)")
                        player.notes.append("Rage Beyond Death - The divine power that fuels your rage allows you to shrug off fatal blows.\nWhile you're raging, having 0 hit points doesn’t knock you unconscious. You still must make death saving throws, and you suffer the normal effects of taking damage while at 0 hit points. However, if you would die due to failing death saving throws, you don’t die until your rage ends, and you die then only if you still have 0 hit points.")
                if player.subclass[i] == "Path of the Wild Magic Barbarian":     
                    player.classnotes.append("Magic Awareness (see notes)")
                    player.classnotes.append(f"Magic Awareness - As an action, you can open your awareness to the presence of concentrated magic. Until the end of your next turn, you know the location of any spell or magic item within 60 feet of you that isn't behind total cover. When you sense a spell, you learn which school of magic it belongs to.\nYou can use this feature a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
                    WM1 = "Shadowy tendrils lash around you. Each creature of your choice that you can see within 30 feet of you must succeed on a Constitution saving throw or take 1d12 necrotic damage. You also gain 1d12 temporary hit points."
                    WM2 = "You teleport up to 30 feet to an unoccupied space you can see. Until your rage ends, you can use this effect again on each of your turns as a bonus action."
                    WM3 = "An intangible spirit, which looks like a Flumph or a Pixie (your choice), appears within 5 feet of one creature of your choice that you can see within 30 feet of you. At the end of the current turn, the spirit explodes, and each creature within 5 feet of it must succeed on a Dexterity saving throw or take 1d6 force damage. Until your rage ends, you can use this effect again, summoning another spirit, on each of your turns as a bonus action."
                    WM4 = "Magic infuses one weapon of your choice that you are holding. Until your rage ends, the weapon's damage type changes to force, and it gains the light and thrown properties, with a normal range of 20 feet and a long range of 60 feet. If the weapon leaves your hand, the weapon reappears in your hand at the end of the current turn."
                    WM5 = "Whenever a creature hits you with an attack roll before your rage ends, that creature takes 1d6 force damage, as magic lashes out in retribution."
                    WM6 = "Until your rage ends, you are surrounded by multicolored, protective lights; you gain a + 1 bonus to AC, and while within 10 feet of you, your allies gain the same bonus."
                    WM7 = "Flowers and vines temporarily grow around you; until your rage ends, the ground within 15 feet of you is difficult terrain for your enemies."
                    WM8 = "A bolt of light shoots from your chest. Another creature of your choice that you can see within 30 feet of you rust succeed on a Constitution Saving throw or take 1d6 radiant damage and be blinded until the start of your next turn. Until your rage ends, you can use this effect again on each of your turns as a bonus action."
                    WM = [WM1, WM2, WM3, WM4, WM5, WM6, WM7, WM8]
                    WildMagic = random.choice(WM)
                    player.notes.append("Wild Surge (see notes)")
                    player.notes.append(f"Wild Surge - The magical energy roiling inside you sometimes erupts from you. When you enter your rage, the Magical Effect produces is {WildMagic}\nIf the effect requires a saving throw, the DC equals 8 + your Proficiency Bonus + your Constitution modifier, or DC {8 + player.profbonus + player.ConMod}.")   
                    if barblvl >= 6:
                        player.classnotes.append(f"Bolstering Magic (see notes)")
                        player.notes.append(f"Bolstering Magic - You can harness your wild magic to bolster yourself or a companion. As an action, you can touch one creature (which can be yourself) and confer one of the following benefits of your choice to that creature:\n- For 10 minutes, the creature can roll a d3 whenever making an attack roll or an ability check and add the number rolled to the d20 roll.\n- Roll a d3. The creature regains one expended spell slot, the level of which equals the number rolled or lower (the creature's choice). Once a creature receives this benefit, that creature can't receive it again until after a long rest.\nYou can take this action a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
                    if barblvl >= 10:
                        player.classnotes.append("Unstable Backlash - When you are imperiled during your rage, the magic within you can lash out; immediately after you take damage or fail a saving throw while raging, you can use your reaction to roll on the Wild Magic table and immediately produce the effect rolled. This effect replaces your current Wild Magic effect.")
                    if barblvl >= 14:
                        player.classnotes.append("Controlled Surge - Whenever you roll on the Wild Magic table, you can roll the die twice and choose which of the two effects to unleash. If you roll the same number on both dice, you can ignore the number and choose any effect on the table.")
                player.skills = oneskillfromlist(param, player.skills, BarbSkillsList)
            if barblvl >= 5:
                player.classnotes.append("Extra Attack - You can attack twice, instead of once, whenever you take the Attack action on your turn.")
                player.classnotes.append("Fast Movement - Your speed increases by 10 feet while you aren’t wearing heavy armor.")
            if barblvl >= 7:
                player.classnotes.append("Feral Instinct (see notes)")
                player.notes.append("Feral Instinct - Your instincts are so honed that you have advantage on initiative rolls.\nAdditionally, if you are surprised at the beginning of combat and aren’t incapacitated, you can act normally on your first turn, but only if you enter your rage before doing anything else on that turn.")
                player.classnotes.append("Instinctive Pounce - As part of the bonus action you take to enter your rage, you can move up to half your speed.")
            if barblvl >= 9:
                BrutalWeaponDice = 1
                if barblvl >= 13:
                    BrutalWeaponDice = 2
                if barblvl >= 17:
                    BrutalWeaponDice = 3
                player.classnotes.append(f"Brutal Critical - You can roll {BrutalWeaponDice} additional weapon damage die when determining the extra damage for a critical hit with a melee attack.")
            if barblvl >= 10:
                player.skills = oneskillfromlist(param, player.skills, BarbSkillsList)
            if barblvl >= 11:
                player.classnotes.append("Relentless Rage (see notes)")
                player.notes.append("Relentless Rage - Your rage can keep you fighting despite grievous wounds. If you drop to 0 hit points while you’re raging and don’t die outright, you can make a DC 10 Constitution saving throw. If you succeed, you drop to 1 hit point instead.\nEach time you use this feature after the first, the DC increases by 5. When you finish a short or long rest, the DC resets to 10.")
            if barblvl >= 15:
                player.classnotes.append("Persistent Rage - Your rage is so fierce that it ends early only if you fall unconscious or if you choose to end it.")
            if barblvl >= 18:
                player.classnotes.append("Indomitable Might - If your total for a Strength check is less than your Strength score, you can use that score in place of the total.")
            if barblvl == 20:
                player.classnotes.append("Primal Champion - You embody the power of the wilds. Your Strength and Constitution scores increase by 4. Your maximum for those scores is now 24.")
        if player.Class[i] == "Bard":
            if ((param == "N") or (player.singlemulticlass == "N")):
                bardlvl = player.level
                player.classlvl.append(bardlvl)             
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    bardlvl = int(input(f"Given your pool of levels of {poollevel}, what is your Bard level? "))      
                    if bardlvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                
                poollevel = poollevel - bardlvl
                player.classlvl.append(bardlvl) 
            if bardlvl >= 1:
                player.hitdice.append(f"{bardlvl}d8 for {player.Class[i]}")
                if bardlvl == 1:
                    player.hitpoints += (8 + player.ConMod)
                else:
                    player.hitpoints += (8 + player.ConMod + hpcalc(bardlvl, dice, 8))            
                if i == 0:
                    profs = ["Light Armor", "Simple Weapons", 
                             dnd_tools.martial_weapons["HandCrossbow"]["Name"], 
                             dnd_tools.martial_weapons["Longsword"]["Name"], 
                             dnd_tools.martial_weapons["Rapier"]["Name"],
                             dnd_tools.martial_weapons["Shortsword"]["Name"]
                             ]                    
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    player.proficiencies = musicalinstr(param, player.proficiencies)
                    player.proficiencies = musicalinstr(param, player.proficiencies)
                    player.proficiencies = musicalinstr(param, player.proficiencies)
                    player.skills.append(dnd_tools.saving_throws["DexST"])
                    player.skills.append(dnd_tools.saving_throws["ChaST"])
                    player.skills = skillprof3(param, player.skills)  
                    StartEquip1 = ["Rapier", "Longsword", "Any Simple Weapon"]
                    StartEquip2 = ["Diplomat's Pack", "Entertainer's Pack"]     
                    StartEquip3 = ["Lute", "Any Other Musical Instrument"]                                   
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Rapier")
                        print("2 - Longsword")
                        print("3 - Any Simple Weapon")
                        se1 = int(input("What would you like your first choice for starting equipment to be? "))
                        if se1 == 0:
                            SE1rand = random.choice(StartEquip1)
                            if SE1rand == "Rapier":
                                player.equipment.append(dnd_tools.martial_weapons["Rapier"].copy())
                            if SE1rand == "Longsword":
                                player.equipment.append(dnd_tools.martial_weapons["Longsword"].copy())
                            if SE1rand == "Any Simple Weapon":
                                SimpRandKey = random.choice(SimpleWeapons)
                                player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                        if se1 == 1:
                            player.equipment.append(dnd_tools.martial_weapons["Rapier"].copy())
                        if se1 == 2:
                            player.equipment.append(dnd_tools.martial_weapons["Longsword"].copy())
                        if se1 == 3:
                            print("0 - Random")
                            for j, sw in enumerate(SimpleWeaponsNames, 1):
                                print(f"{j} - {sw}")
                            se1sw = int(input("Which simple weapon would you like to add to your inventory? "))
                            if se1sw == 0:
                                SimpRandKey = random.choice(SimpleWeapons)
                                player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                            elif 1 <= se1sw <= len(SimpleWeapons):
                                SimpKey = SimpleWeapons[se1sw-1]
                                player.equipment.append(dnd_tools.simple_weapons[SimpKey].copy())
                        print("0 - Random")
                        print("1 - Diplomat's Pack")
                        print("2 - Entertainer's Pack")
                        se2 = int(input("What would you like your second choice for starting equipment to be? "))
                        if se2 == 0:
                            SE2rand = random.choice(StartEquip2)
                            if SE2rand == "Diplomat's Pack":
                                player.equipment.extend(dnd_tools.packs["DiplomatsPack"]["contents"])
                            if SE2rand == "Entertainer's Pack":
                                player.equipment.extend(dnd_tools.packs["EntertainersPack"]["contents"])
                        if se2 == 1:
                            player.equipment.extend(dnd_tools.packs["DiplomatsPack"]["contents"])
                        if se2 == 2:
                            player.equipment.extend(dnd_tools.packs["EntertainersPack"]["contents"])
                        print("0 - Random")
                        print("1 - Lute")
                        print("2 - Any Other Musical Instrument")
                        se3 = int(input("What would you like your third choice for starting equipment to be? "))
                        if se3 == 0:
                            SE3rand = random.choice(StartEquip3)
                            if SE3rand == "Lute":
                                player.equipment.append(dnd_tools.musical_instr["Lute"].copy())
                            if SE2rand == "Any Other Musical Instrument":
                                MIWOLRandKey = random.choice(MusicalInstrWOLute)
                                player.equipment.append(dnd_tools.musical_instr[MIWOLRandKey].copy())
                        if se3 == 1:
                            player.equipment.append(dnd_tools.musical_instr["Lute"].copy())
                        if se3 == 2:
                            print("0 - Random")
                            for j, miwl in enumerate(MusicalInstrWOLuteNames, 1):
                                print(f"{j} - {miwl}")
                            se3mi = int(input("Which Musical Instrument, minus the Lute, would you like to add to your inventory? "))
                            if se3mi == 0:
                                MIWOLRandKey = random.choice(MusicalInstrWOLute)
                                player.equipment.append(dnd_tools.musical_instr[MIWOLRandKey].copy())
                            elif 1 <= se3mi <= len(SimpleWeapons):
                                MIWOLKey = MusicalInstrWOLute[se3mi-1]
                                player.equipment.append(dnd_tools.musical_instr[MIWOLKey].copy())
                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "Rapier":
                            player.equipment.append(dnd_tools.martial_weapons["Rapier"].copy())
                        if SE1rand == "Longsword":
                            player.equipment.append(dnd_tools.martial_weapons["Longsword"].copy())
                        if SE1rand == "Any Simple Weapon":
                            SimpRandKey = random.choice(SimpleWeapons)
                            player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "Diplomat's Pack":
                            player.equipment.extend(dnd_tools.packs["DiplomatsPack"]["contents"])
                        if SE2rand == "Entertainer's Pack":
                            player.equipment.extend(dnd_tools.packs["EntertainersPack"]["contents"])
                        SE3rand = random.choice(StartEquip3)
                        if SE3rand == "Lute":
                            player.equipment.append(dnd_tools.musical_instr["Lute"].copy())
                        if SE2rand == "Any Other Musical Instrument":
                            MIWOLRandKey = random.choice(MusicalInstrWOLute)
                            player.equipment.append(dnd_tools.musical_instr[MIWOLRandKey].copy())                           
                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())    
                else:
                    profs = ["Light Armor"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    player.skills = skillprof(param, player.skills)   
                    player.proficiencies = musicalinstr(param, player.proficiencies)                                                                                                      
                player.spellcastingclass.append("Bard")
                player.spellcastingability.append("Cha")
                player.spellsavedc.append(8 + player.profbonus + player.ChaMod)
                player.spellattackmod.append(player.profbonus + player.ChaMod)
                BardCantripsKnown = 2
                BardSpellsKnown = 4
                BardSpellSlot1 = 2
                BardSpellSlot2 = 0
                BardSpellSlot3 = 0
                BardSpellSlot4 = 0
                BardSpellSlot5 = 0
                BardSpellSlot6 = 0
                BardSpellSlot7 = 0
                BardSpellSlot8 = 0
                BardSpellSlot9 = 0
                SpellCastingFocus = "Musical Instrument"    
                BardicInspiration = "d6"
                if ((bardlvl >= 5) and (bardlvl < 10)):
                    BardicInspiration = "d8"
                if ((bardlvl > 10) and (bardlvl < 15)):
                    BardicInspiration = "d10"
                if bardlvl >= 15:
                    BardicInspiration = "d12"
            player.classnotes.append("Bardic Inspiration (see notes)")
            player.notes.append(f"Bardic Inspiration - You can inspire others through stirring words or music. To do so, you use a bonus action on your turn to choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one Bardic Inspiration die, a {BardicInspiration}.\nOnce within the next 10 minutes, the creature can roll the die and add the number rolled to one ability check, attack roll, or saving throw it makes. The creature can wait until after it rolls the d20 before deciding to use the Bardic Inspiration die, but must decide before the DM says whether the roll succeeds or fails. Once the Bardic Inspiration die is rolled, it is lost. A creature can have only one Bardic Inspiration die at a time.\nYou can use this feature a number of times equal to your Charisma modifier, or {player.ChaMod} times, a minimum of once. You regain any expended uses when you finish a long rest.\nYour Bardic Inspiration die changes when you reach certain levels in this class.")            
            if bardlvl >= 2:
                player.classnotes.append(f"Jack of All Trades - You can add half your Proficiency Bonus, rounded down, or {math.floor(player.profbonus/2)}, to any ability check you make that doesn’t already include your Proficiency Bonus.")
                SongRest = "1d6"
                if ((bardlvl >= 9) and (bardlvl < 13)):
                    SongRest = "1d8"
                if ((bardlvl >= 13) and (bardlvl < 17)):
                    SongRest = "1d10"
                if (bardlvl >= 17):
                    SongRest = "1d12"
                player.classnotes.append("Song of Rest (see notes)")
                player.notes.append(f"Song of Rest - You can use soothing music or oration to help revitalize your wounded allies during a short rest. If you or any friendly creatures who can hear your performance regain hit points at the end of the short rest by spending one or more Hit Dice, each of those creatures regains an extra {SongRest} hit points.\nThe extra hit points increase when you reach certain levels in this class.")
                player.classnotes.append("Magical Inspiration - If a creature has a Bardic Inspiration die from you and casts a spell that restores hit points or deals damage, the creature can roll that die and choose a target affected by the spell. Add the number rolled as a bonus to the hit points regained or the damage dealt. The Bardic Inspiration die is then lost.")
                BardSpellsKnown = 5
                BardSpellSlot1 = 3
            if bardlvl >= 3:
                Bar = ["College of Creation Bard", "College of Eloquence Bard", "College of Glamour Bard", "College of Lore Bard", "College of the Road Bard", "College of Spirits Bard", "College of Swords Bard", "College of Tragedy Bard", "College of Valor Bard", "College of Whispers Bards"]
                

                if player.subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        for idx, subcl in enumerate(Bar, 1):
                            print(f"{idx} - {subcl}")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 0:
                            player.subclass[i] = random.choice(Bar)
                        elif 1 <= subc <= len(Bar):
                            player.subclass[i] = Bar[subc - 1]
                    if param == "N":
                        player.subclass[i] = random.choice(Bar)                               
                if player.subclass[i] == "College of Creation Bard":
                    player.classnotes.append("Mote of Potential (see notes)")
                    player.notes.append(f"Mote of Potential - Whenever you give a creature a Bardic Inspiration die, you can utter a note from the Song of Creation to create a Tiny mote of potential, which orbits within 5 feet of that creature. The mote is intangible and invulnerable, and it lasts until the Bardic Inspiration die is lost. The mote looks like a musical note, a star, a flower, or another symbol of art or life that you choose.\nWhen the creature uses the Bardic Inspiration die, the mote provides an additional effect based on whether the die benefits an ability check, an attack roll, or a saving throw, as detailed below:\nAbility Check - When the creature rolls the Bardic Inspiration die to add it to an ability check, the creature can roll the Bardic Inspiration die again and choose which roll to use, as the mote pops and emits colorful, harmless sparks for a moment.\nAttack Roll - Immediately after the creature rolls the Bardic Inspiration die to add it to an attack roll against a target, the mote thunderously shatters. The target and each creature of your choice that you can see within 5 feet of it must succeed on a Constitution saving throw against your spell save DC, or against {player.spellsavedc[i]}, or take thunder damage equal to the number rolled on the Bardic Inspiration die.\nSaving Throw - Immediately after the creature rolls the Bardic Inspiration die and adds it to a saving throw, the mote vanishes with the sound of soft music, causing the creature to gain temporary hit points equal to the number rolled on the Bardic Inspiration die plus your Charisma modifier, or {player.ChaMod} temporary hit points, minimum of 1 temporary hit point.")
                    PerfCreation = "Medium"
                    if ((bardlvl >= 6) and (bardlvl < 14)):
                        PerfCreation = "Large"
                    if bardlvl >= 14:
                        PerfCreation = "Huge"
                    player.classnotes.append("Performance of Creation (see notes)")
                    player.notes.append(f"Performance of Creation - You can channel the magic of the Song of Creation to create one nonmagical item of your choice in an unoccupied space within 10 feet of you. The item must appear on a surface or in a liquid that can support it. The gp value of the item can't be more than 20 times your Bard level, or maximum {bardlvl*20} gp, and the item must be {PerfCreation} or smaller. The item glimmers softly, and a creature can faintly hear music when touching it. The created item disappears after a number of hours equal to your Proficiency Bonus, or {player.profbonus} hours. For examples of items you can create, see the equipment chapter of the Player's Handbook.\nOnce you create an item with this feature, you can't do so again until you finish a long rest, unless you expend a spell slot of 2nd level or higher to use this feature again. You can have only one item created by this feature at a time; if you use this action and already have an item from this feature, the first one immediately vanishes.\nThe size of the item you can create with this feature increases as you level up.")
                    if bardlvl >= 6:
                        player.classnotes.append("Animating Performance (see notes)")
                        player.notes.append("Animating Performance - As an action, you can target a Large or smaller nonmagical item you can see within 30 feet of you and animate it. The animate item uses the Dancing Item stat block, which uses your Proficiency Bonus (PB). The item is friendly to you and your companions and obeys your commands. It lives for 1 hour, until it is reduced to 0 hit points, or until you die.\nIn combat, the item shares your initiative count, but it takes its turn immediately after yours. It can move and use its reaction on its own, but the only action it takes on its turn is the Dodge action, unless you take a bonus action on your turn to command it to take another action. That action can be one in its stat block or some other action. If you are incapacitated, the item can take any action of its choice, not just Dodge.\nWhen you use your Bardic Inspiration feature, you can command the item as part of the same bonus action you use for Bardic Inspiration.\nOnce you animate an item with this feature, you can't do so again until you finish a long rest, unless you expend a spell slot of 3rd level or higher to use this feature again. You can have only one item animated by this feature at a time; if you use this action and already have a dancing item from this feature, the first one immediately becomes inanimate.")
                    if bardlvl >= 14:
                        player.classnotes.append("Creation Crescendo (see notes)")
                        player.notes.append(f"Creation Crescendo - When you use your Performance of Creation feature, you can create more than one item at once (minimum of two items), specifically a number of items equal to your Charisma modifier, or {player.ChaMod} items. If you create an item that would exceed that number, you choose which of the previously created items disappears. Only one of these items can be of the maximum size you can create; the rest must be Small or Tiny.\nYou are no longer limited by gp value when creating items with Performance of Creation.")
                if player.subclass[i] == "College of Eloquence Bard":
                    player.classnotes.append("Silver Tongue - You are a master at saying the right thing at the right time. When you make a Charisma (Persuasion) or Charisma (Deception) check, you can treat a d20 roll of 9 or lower as a 10.")
                    player.classnotes.append("Unsettling Words (see notes)")
                    player.notes.append("Unsettling Words - You can spin words laced with magic that unsettle a creature and cause it to doubt itself. As a bonus action, you can expend one use of your Bardic Inspiration and choose one creature you can see within 60 feet of you. Roll the Bardic Inspiration die. The creature must subtract the number rolled from the next saving throw it makes before the start of your next turn.")
                    if bardlvl >= 6:
                        player.classnotes.append("Unfailing Inspiration - Your inspiring words are so persuasive that others feel driven to succeed. When a creature adds one of your Bardic Inspiration dice to its ability check, attack roll, or saving throw and the roll fails, the creature can keep the Bardic Inspiration die.")
                        player.classnotes.append("Universal Speech (see notes)")
                        player.notes.append(f"Universal Speech - You have gained the ability to make your speech intelligible to any creature. As an action, choose one or more creatures within 60 feet of you, up to a number equal to your Charisma modifier, or up to {player.ChaMod} creatures, minimum of one creature. The chosen creatures can magically understand you, regardless of the language you speak, for 1 hour.\nOnce you use this feature, you can't use it again until you finish a long rest, unless you expend a spell slot to use it again.")
                    if bardlvl >= 14:
                        player.classnotes.append("Infectious Inspiration (see notes)")
                        player.notes.append(f"Infectious Inspiration - \nWhen you successfully inspire someone, the power of your eloquence can now spread to someone else. When a creature within 60 feet of you adds one of your Bardic Inspiration dice to its ability check, attack roll, or saving throw and the roll succeeds, you can use your reaction to encourage a different creature (other than yourself) that can hear you within 60 feet of you, giving it a Bardic Inspiration die without expending any of your Bardic Inspiration uses.\nYou can use this reaction a number of times equal to your Charisma modifier, or {player.ChaMod} times, minimum of once, and you regain all expended uses when you finish a long rest.")
                if player.subclass[i] == "College of Glamour Bard":
                    CGBTempHP = 5
                    if ((bardlvl >= 5) and bardlvl < 10):
                        CGBTempHP = 8
                    if ((bardlvl >= 10) and (bardlvl < 15)):
                        CGBTempHP = 11
                    if bardlvl >= 15:
                        CGBTempHP = 14
                    player.classnotes.append("Mantle of Inspiration (see notes)")
                    player.notes.append(f"Mantle of Inspiration - You gain the ability to weave a song of fey magic that imbues your allies with vigor and speed.\nAs a bonus action, you can expend one use of your Bardic Inspiration to grant yourself a wondrous appearance. When you do so, choose a number of creatures you can see and who can see you within 60 feet of you, up to a number equal to your Charisma modifier, or up to {player.ChaMod} creatures, minimum of one. Each of them gains {CGBTempHP} temporary hit points. When a creature gains these temporary hit points, it can immediately use its reaction to move up to its speed, without provoking opportunity attacks.\nThe number of temporary hit points increases when you reach certain levels in this class.")
                    player.classnotes.append("Enthralling Performance (see notes)")
                    player.notes.append(f"Enthralling Performance - You can charge your performance with seductive, fey magic.\nIf you perform for at least 1 minute, you can attempt to inspire wonder in your audience by singing, reciting a poem, or dancing. At the end of the performance, choose a number of humanoids within 60 feet of you who watched and listened to all of it, up to a number equal to your Charisma modifier, or {player.ChaMod} humanoids, minimum of one. Each target must succeed on a Wisdom saving throw against your spell save DC, or against {player.spellsavedc[i]}, or be charmed by you. While charmed in this way, the target idolizes you, it speaks glowingly of you to anyone who speaks to it, and it hinders anyone who opposes you, avoiding violence unless it was already inclined to fight on your behalf. This effect ends on a target after 1 hour, if it takes any damage, if you attack it, or if it witnesses you attacking or damaging any of its allies.\nIf a target succeeds on its saving throw, the target has no hint that you tried to charm it.\nOnce you use this feature, you can’t use it again until you finish a short or long rest.")
                    if bardlvl >= 6:
                        player.classnotes.append("Mantle of Majesty (see notes)")
                        player.notes.append("Mantle of Majesty - You gain the ability to cloak yourself in a fey magic that makes others want to serve you. As a bonus action, you cast Command, without expending a spell slot, and you take on an appearance of unearthly beauty for 1 minute or until your concentration ends (as if you were concentrating on a spell). During this time, you can cast Command as a bonus action on each of your turns, without expending a spell slot.\nAny creature charmed by you automatically fails its saving throw against the Command you cast with this feature.\nOnce you use this feature, you can’t use it again until you finish a long rest.")
                    if bardlvl >= 14:
                        player.classnotes.append("Unbreakable Majesty (see notes)")
                        player.notes.append(f"Unbreakable Majesty - Your appearance permanently gains an otherworldly aspect that makes you look more lovely and fierce.\nIn addition, as a bonus action, you can assume a magically majestic presence for 1 minute or until you are incapacitated. For the duration, whenever any creature tries to attack you for the first time on a turn, the attacker must make a Charisma saving throw against your spell save DC, or against {player.spellsavedc[i]}. On a failed save, it can't attack you on this turn, and it must choose a new target for its attack or the attack is wasted. On a successful save, it can attack you on this turn, but it has disadvantage on any saving throw it makes against your spells on your next turn.\nOnce you assume this majestic presence, you can't do so again until you finish a short or long rest.")
                if player.subclass[i] == "College of Lore Bard":
                    player.classnotes.append("Bonus Proficiencies - You gain proficiency with three skills of your choice (not added).")
                    player.classnotes.append("Cutting Words (see notes)")
                    player.notes.append("Cutting Words - You learn how to use your wit to distract, confuse, and otherwise sap the confidence and competence of others. When a creature that you can see within 60 feet of you makes an attack roll, an ability check, or a damage roll, you can use your reaction to expend one of your uses of Bardic Inspiration, rolling a Bardic Inspiration die and subtracting the number rolled from the creature's roll. You can choose to use this feature after the creature makes its roll, but before the DM determines whether the attack roll or ability check succeeds or fails, or before the creature deals its damage. The creature is immune if it can't hear you or if it's immune to being charmed.")
                    if bardlvl >= 6:
                        player.classnotes.append("Additional Magical Secrets - You learn two spells of your choice from any class. A spell you choose must be of a level you can cast, as shown on the Bard table, or a cantrip. The chosen spells count as bard spells for you but don't count against the number of bard spells you know.")
                    if bardlvl >= 14:
                        player.classnotes.append("Peerless Skill - When you make an ability check, you can expend one use of Bardic Inspiration. Roll a Bardic Inspiration die and add the number rolled to your ability check. You can choose to do so after you roll the die for the ability check, but before the DM tells you whether you succeed or fail.")
                if player.subclass[i] == "College of the Road Bard":
                    player.classnotes.append("Bonus Proficiencies (see notes)")
                    player.notes.append("Bonus Proficiencies - You gain a few useful proficiencies picked up from your time on the road. Choose three of the following options (each option can only be selected once, this has not been automatically added):\nYou gain proficiency with a Gaming Set of your choice\nYou gain proficiency with a martial weapon of your choice\nYou gain proficiency with Herbalism Kits\nYou gain proficiency with Thieves' Tools\nYou gain proficiency with a skill of your choice\nYou learn two languages of your choice")
                    player.classnotes.append("Wanderer’s Lore (see notes)")
                    player.notes.append("Wanderer’s Lore - You can share any useful tidbits of information you have come across in your travels to help others to see problems from a new angle. When a creature has a Bardic Inspiration die granted by you, they may make a single Arcana, History, Nature, or Religion check with advantage. The creature may choose whether or not to add the Bardic Inspiration die to this roll.")
                    player.classnotes.append("Traveler’s Tricks(1) (see notes)")
                    player.notes.append("Traveler’s Tricks(1) - You already have several memorable experiences from your life on the road. You learn two Traveler’s Tricks of your choice (see Traveler’s Trick Options).\nThese Traveler’s Tricks represent skills, techniques, and useful pieces of knowledge picked up along the way. Each one requires you to expend a use of your Bardic Inspiration, and takes a bonus action to use unless otherwise specified.\nAt higher levels you learn additional Traveler’s Tricks.")
                    if bardlvl >= 6:
                        player.classnotes.append("Traveler’s Tricks(2) (see notes)")
                        player.notes.append("Traveler’s Tricks(2) - You already have several memorable experiences from your life on the road. You learn an additional Traveler’s Trick of your choice (see Traveler’s Trick Options).\nThese Traveler’s Tricks represent skills, techniques, and useful pieces of knowledge picked up along the way. Each one requires you to expend a use of your Bardic Inspiration, and takes a bonus action to use unless otherwise specified.\nAt higher levels you learn additional Traveler’s Tricks.")                        
                        player.classnotes.append("Improved Tricks - Your Traveler’s Tricks become stronger. By practicing the tricks you know, and encountering stronger adventurers who share their knowledge with you, your mastery over your tricks increases.")
                    if bardlvl >= 14:
                        player.classnotes.append("Traveler’s Tricks(3) (see notes)")
                        player.notes.append("Traveler’s Tricks(3) - You already have several memorable experiences from your life on the road. You learn an additional Traveler’s Tricks of your choice (see Traveler’s Trick Options).\nThese Traveler’s Tricks represent skills, techniques, and useful pieces of knowledge picked up along the way. Each one requires you to expend a use of your Bardic Inspiration, and takes a bonus action to use unless otherwise specified.\nAt higher levels you learn additional Traveler’s Tricks.")
                        player.classnotes.append("Improved Tricks - Your Traveler’s Tricks become stronger. By practicing the tricks you know, and encountering stronger adventurers who share their knowledge with you, your mastery over your tricks increases.")
                if player.subclass[i] == "College of Spirits Bard":
                    player.classnotes.append("Guiding Whispers - You can reach out to spirits to guide you and others. You learn the Guidance cantrip, which doesn’t count against the number of bard cantrips you know. For you, it has a range of 60 feet when you cast it.")
                    player.classnotes.append("Spiritual Focus - You employ tools that aid you in channeling spirits, be they historical figures or fictional archetypes. You can use the following objects as a spellcasting focus for your bard spells: a candle, crystal ball, skull, spirit board, or tarokka deck.")
                    if bardlvl >= 6:
                        player.classnotes.append("When you cast a bard spell that deals damage or restores hit points through the Spiritual Focus, roll a d6, and you gain a bonus to one damage or healing roll of the spell equal to the number rolled.")
                    player.classnotes.append("Tales from Beyond (see notes)")
                    player.notes.append(f"Tales from Beyond - You reach out to spirits who tell their tales through you. While you are holding your Spiritual Focus, you can use a bonus action to expend one use of your Bardic Inspiration and roll on the Spirit Tales table using your Bardic Inspiration die to determine the tale the spirits direct you to tell. You retain the tale in mind until you bestow the tale’s effect or you finish a short or long rest.\nYou can use an action to choose one creature you can see within 30 feet of you (this can be you) to be the target of the tale’s effect. Once you do so, you can’t bestow the tale’s effect again until you roll it again.\nYou can retain only one of these tales in mind at a time, and rolling on the Spirit Tales table immediately ends the effect of the previous tale.\nIf the tale requires a saving throw, the DC equals your spell save DC, or against {player.spellsavedc[i]}.")
                    if bardlvl >= 6:
                        player.classnotes.append("Spirit Session (see notes)")
                        player.notes.append(f"Spirit Session - Spirits provide you with supernatural insights. You can conduct an hour-long ritual channeling spirits (which can be done during a short or long rest) using your Spiritual Focus. You can conduct the ritual with a number of willing creatures equal to your Proficiency Bonus, or {player.profbonus} creatures, including yourself. At the end of the ritual, you temporarily learn one spell of your choice from any class.\nThe spell you choose must be of a level equal to the number of creatures that conducted the ritual or less, the spell must be of a level you can cast, and it must be in the school of divination or necromancy. The chosen spell counts as a bard spell for you but doesn’t count against the number of bard spells you know.\nOnce you perform the ritual, you can’t do so again until you start a long rest, and you know the chosen spell until you start a long rest.")
                    if bardlvl >= 14:
                        player.classnotes.append("Mystical Connection - You now have the ability to nudge the spirits of Tales from Beyond toward certain tales. Whenever you roll on the Spirit Tales table, you can roll the die twice and choose which of the two effects to bestow. If you roll the same number on both dice, you can ignore the number and choose any effect on the table.")
                        player.classnotes.append("Spirit Tales (see notes)")
                        player.notes.append("Spirit Tales - Storytellers, like bards of the College of Spirits, often give voice to tales inspired by some greater theme or body of work. When determining what stories you tell, consider what unites them. Do they all feature characters from a specific group, like archetypes from the tarokka deck, figures from constellations, childhood imaginary friends, or characters in a particular storybook? Or are your inspirations more general, incorporating historic champions, mythological heroes, or urban legends? Use the tales you tell to define your niche as a storytelling adventurer.")
                if player.subclass[i] == "College of Swords Bard":
                    profs = ["Medium Armor", "Scimitar"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    player.classnotes.append("Bonus Proficiencies - You gain proficiency with medium armor and the scimitar (added to proficiencies).\nIf you’re proficient with a simple or martial melee weapon, you can use it as a spellcasting focus for your bard spells.")
                    player.classnotes.append("Fighting Style (see notes)")
                    player.notes.append("Fighting Style - You adopt a particular style of fighting as your specialty. Choose one of the following options. You can't take a Fighting Style option more than once, even if you later get to choose again.\nDueling - When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.\nTwo-Weapon Fighting - When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.")
                    player.classnotes.append("Blade Flourish (see notes)")
                    player.notes.append("Blade Flourish - You learn to conduct impressive displays of martial prowess and speed.\nWhenever you take the Attack action on your turn, your walking speed increases by 10 feet until the end of the turn, and if a weapon attack that you make as part of this action hits a creature, you can use one of the following Blade Flourish options of your choice. You can use only one Blade Flourish option per turn.\nDefensive Flourish - You can expend one use of your Bardic Inspiration to cause the weapon to deal extra damage to the target you hit. The damage equals the number you roll on the Bardic Inspiration die. You also add the number rolled to your AC until the start of your next turn.\nSlashing Flourish - You can expend one use of your Bardic Inspiration to cause the weapon to deal extra damage to the target you hit and to any other creature of your choice that you can see within 5 feet of you. The damage equals the number you roll on the Bardic Inspiration die.\nMobile Flourish - You can expend one use of your Bardic Inspiration to cause the weapon to deal extra damage to the target you hit. The damage equals the number you roll on the Bardic Inspiration die. You can also push the target up to 5 feet away from you, plus a number of feet equal to the number you roll on that die. You can then immediately use your reaction to move up to your walking speed to an unoccupied space within 5 feet of the target.")
                    if bardlvl >= 6:
                        player.classnotes.append("Extra Attack - You can attack twice, instead of once, whenever you take the Attack action on your turn.")
                    if bardlvl >= 14:
                        player.classnotes.append("Master's Flourish - Whenever you use a Blade Flourish option, you can roll a d6 and use it instead of expending a Bardic Inspiration die.")
                if player.subclass[i] == "College of Tragedy Bard":                    
                    player.classnotes.append("Poetry in Misery - You learn to harness the beauty in failure, finding inspiration in even the direst twists of fate. Whenever you or an ally within 30 feet of you rolls a 1 on the d20 for an attack roll, an ability check, or a saving throw, you can use your reaction to soliloquize and regain one expended use of your Bardic Inspiration feature.")
                    player.classnotes.append("Sorrowful Fate (see notes)")
                    player.notes.append("Sorrowful Fate - You exploit a foe's peril to instill deep feelings of sorrow and doom. When you or an ally you can see forces a creature to make a saving throw, you can expend one use of your Bardic Inspiration to change the type of saving throw to a Charisma save instead.\nIf the target fails this save, roll a Bardic Inspiration die. The target takes psychic damage equal to the result, and is plagued with regret for 1 minute. If the target is reduced to 0 hit points during this time and can speak, they are magically compelled to utter darkly poetic final words before succumbing to their injuries.\nOnce you use this feature, you can't use it again until you finish a short or long rest.")
                    if bardlvl >= 6:
                        player.classnotes.append("Tale of Hubris(1) (see notes)")
                        player.notes.append("Tale of Hubris(1) - You learn to weave a magical narrative that draws out the fatal arrogance of your foes. When a creature scores a critical hit against you or an ally within 60 feet of you that you can see, you can use your reaction and expend one use of your Bardic Inspiration to target the attacking creature and evoke the story of their downfall. For 1 minute or until the target suffers a critical hit, any weapon attack against the target scores a critical hit on a roll of 18–20.")
                        player.classnotes.append("Impending Misfortune (see notes)")
                        player.notes.append("Impending Misfortune - Your words can twist the power of fate to create triumph from the promise of future despair. When you make an attack roll or a saving throw, you can gain a +10 bonus to the roll, but the next attack roll or saving throw you make takes a −10 penalty. If not used, this penalty disappears when you finish a short or long rest.\nYou can't use this feature again until you finish a short or long rest, or until you are reduced to 0 hit points.")
                    if bardlvl >= 14:
                        player.classnotes.append("Tale of Hubris(2) (see notes)")
                        player.notes.append("Tale of Hubris(2) - The critical hit range of this feature increases to 17–20.")
                        player.classnotes.append("Nimbus of Pathos (see notes)")
                        player.notes.append("Nimbus of Pathos - You can touch a willing creature as an action and empower it with tragic heroism. For 1 minute, the creature is surrounded by mournful music and ghostly singing, granting it the following benefits and drawbacks:\n-The creature has a +4 bonus to AC.\n-It has advantage on attack rolls and saving throws.\n-When the creature hits a target with a weapon attack or spell attack, that target takes an extra 1d10 radiant damage.\n- Any weapon attack against the creature scores a critical hit on a roll of 18–20.\nWhen this effect ends, the creature immediately drops to 0 hit points and is dying. Once you use this feature, you can't use it again until you finish a long rest.")
                if player.subclass[i] == "College of Valor Bard":
                    profs = ["Medium Armor", "Shield", "Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof) 
                    player.classnotes.append("Combat Inspiration (see notes)")
                    player.notes.append("Combat Inspiration - You learn to inspire others in battle. A creature that has a Bardic Inspiration die from you can roll that die and add the number rolled to a weapon damage roll it just made. Alternatively, when an attack roll is made against the creature, it can use its reaction to roll the Bardic Inspiration die and add the number rolled to its AC against that attack, after seeing the roll but before knowing whether it hits or misses.")                                                  
                    if bardlvl >= 6:
                        player.classnotes.append("Extra Attack - You can attack twice, instead of once, whenever you take the Attack action on your turn.")
                    if bardlvl >= 14:
                        player.classnotes.append("Battle Magic - You have mastered the art of weaving spellcasting and weapon use into a single harmonious act. When you use your action to cast a bard spell, you can make one weapon attack as a bonus action.")
                if player.subclass[i] == "College of Whispers Bards":        
                    PsychicBladeDmg = "2d6"
                    if ((bardlvl >= 5) and (bardlvl < 10)):
                        PsychicBladeDmg = "3d6"
                    if ((bardlvl >= 10) and (bardlvl < 15)):
                        PsychicBladeDmg = "5d6"
                    if bardlvl >= 15:
                        PsychicBladeDmg = "8d6"
                    player.classnotes.append("Psychic Blades (see notes)")
                    player.notes.append(f"Psychic Blades - When you join the College of Whispers at 3rd level, you gain the ability to make your weapon attacks magically toxic to a creature's mind.\nWhen you hit a creature with a weapon attack, you can expend one use of your Bardic Inspiration to deal an additional {PsychicBladeDmg} psychic damage to that target. You can do so only once per round on your turn.\nThe psychic damage increases when you reach certain levels in this class.")
                    player.classnotes.append("Words of Terror (see notes)")
                    player.notes.append(f"Words of Terror - You learn to infuse innocent-seeming words with an insidious magic that can inspire terror.\nIf you speak to a humanoid alone for at least 1 minute, you can attempt to seed paranoia and fear into its mind. At the end of the conversation, the target must succeed on a Wisdom saving throw against your spell save DC, or against {player.spellsavedc[i]}, or be frightened of you or another creature of your choice. The target is frightened in this way for 1 hour, until it is attacked or damaged, or until it witnesses its allies being attacked or damaged.\nIf the target succeeds on its saving throw, the target has no hint that you tried to frighten it.\nOnce you use this feature, you can’t use it again until you finish a short rest or long rest.")
                    if bardlvl >= 6:
                        player.classnotes.append("Mantle of Whispers (see notes)")
                        player.notes.append("Mantle of Whispers - You gain the ability to adopt a humanoid's persona. When a humanoid dies within 30 feet of you, you can magically capture its shadow using your reaction. You retain this shadow until you use it or you finish a long rest.\nYou can use the shadow as an action. When you do so, it vanishes, magically transforming into a disguise that appears on you. You now look like the dead person, but healthy and alive. This disguise lasts for 1 hour or until you end it as a bonus action.\nWhile you're in the disguise, you gain access to all information that the humanoid would freely share with a casual acquaintance. Such information includes general details on its background and personal life, but doesn't include secrets. The information is enough that you can pass yourself off as the person by drawing on its memories.\nAnother creature can see through this disguise by succeeding on a Wisdom (Insight) check contested by your Charisma (Deception) check. You gain a +5 bonus to your check.\nOnce you capture a shadow with this feature, you can't capture another one with it until you finish a short or long rest.")
                    if bardlvl >= 14:
                        player.classnotes.append("Shadow Lore (see notes)")
                        player.notes.append(f"Shadow Lore - You gain the ability to weave dark magic into your words and tap into a creature’s deepest fears.\nAs an action, you magically whisper a phrase that only one creature of your choice within 30 feet of you can hear. The target must make a Wisdom saving throw against your spell save DC, or against {player.spellsavedc[i]}. It automatically succeeds if it doesn’t share a language with you or if it can’t hear you. On a successful saving throw, your whisper sounds like unintelligible mumbling and has no effect.\nIf the target fails its saving throw, it is charmed by you for the next 8 hours or until you or your allies attack or damage it. It interprets the whispers as a description of its most mortifying secret.\nWhile you gain no knowledge of this secret, the target is convinced you know it. While charmed in this way, the creature obeys your commands for fear that you will reveal its secret. It won’t risk its life for you or fight for you, unless it was already inclined to do so. It grants you favors and gifts it would offer to a close friend.\nWhen the effect ends, the creature has no understanding of why it held you in such fear.\nOnce you use this feature, you can’t use it again until you finish a long rest.")
            player.classnotes.append("Expertise - Choose two of your skill proficiencies. Your Proficiency Bonus is doubled for any ability check you make that uses either of the chosen proficiencies.")
            BardSpellsKnown = 6
            BardSpellSlot1 = 4
            BardSpellSlot2 = 2
            if bardlvl >= 4:
                player.classnotes.append("Bardic Versatility (see notes)")
                player.notes.append("Bardic Versatility - Whenever you reach a level in this class that grants the Ability Score Improvement feature, you can do one of the following, representing a change in focus as you use your skills and magic:\nReplace one of the skills you chose for the Expertise feature with one of your other skill proficiencies that isn't benefiting from Expertise.\nReplace one cantrip you learned from this class's Spellcasting feature with another cantrip from the bard spell list.")
                BardCantripsKnown = 3
                BardSpellsKnown = 7
                BardSpellSlot2 = 3
            if bardlvl >= 5:
                player.classnotes.append("Font of Inspiration - You regain all of your expended uses of Bardic Inspiration when you finish a short or long rest.")
                BardSpellsKnown = 8
                BardSpellSlot3 = 2               
            if bardlvl >= 6:
                player.classnotes.append("Countercharm (see notes)")
                player.notes.append("Countercharm - You gain the ability to use musical notes or words of power to disrupt mind-influencing effects. As an action, you can start a performance that lasts until the end of your next turn. During that time, you and any friendly creatures within 30 feet of you have advantage on saving throws against being frightened or charmed. A creature must be able to hear you to gain this benefit. The performance ends early if you are incapacitated or silenced or if you voluntarily end it (no action required).")
                BardSpellsKnown = 9
                BardSpellSlot3 = 3
            if bardlvl >= 7:
                BardSpellsKnown = 10
                BardSpellSlot4 = 1              
            if bardlvl >= 8:
                BardSpellsKnown = 11
                BardSpellSlot4 = 2          
            if bardlvl >= 9:      
                BardSpellsKnown = 12
                BardSpellSlot4 = 3
                BardSpellSlot5 = 1                     
            if bardlvl >= 10:
                player.classnotes.append("Expertise - Choose two more of your skill proficiencies. Your Proficiency Bonus is doubled for any ability check you make that uses either of the chosen proficiencies.")
                player.classnotes.append("Magical Secrets(1) (see notes)")
                player.notes.append("Magical Secrets(1) - You have plundered magical knowledge from a wide spectrum of disciplines. Choose two spells from any classes, including this one. A spell you choose must be of a level you can cast, as shown on the Bard table, or a cantrip.\nThe chosen spells count as bard spells for you and are included in the number in the Spells Known column of the Bard table.\nYou learn additional spells at higher levels.")
                BardCantripsKnown = 4
                BardSpellsKnown = 14
                BardSpellSlot5 = 2  
            if bardlvl >= 11:
                BardSpellsKnown = 15
                BardSpellSlot6 = 1
            if bardlvl >= 13:
                BardSpellsKnown = 16
                BardSpellSlot2 = 3 
                BardSpellSlot3 = 3
                BardSpellSlot4 = 3
                BardSpellSlot5 = 2  
                BardSpellSlot6 = 1  
                BardSpellSlot7 = 1                                        
            if bardlvl >= 14:
                player.classnotes.append("Magical Secrets(2) (see notes)")
                player.notes.append("Magical Secrets(2) - You have plundered magical knowledge from a wide spectrum of disciplines. Choose two more spells from any classes, including this one. A spell you choose must be of a level you can cast, as shown on the Bard table, or a cantrip.\nThe chosen spells count as bard spells for you and are included in the number in the Spells Known column of the Bard table.\nYou learn additional spells at higher levels.")
                BardSpellsKnown = 18 
                BardSpellSlot7 = 1 
            if bardlvl >= 15:
                BardSpellsKnown = 19 
                BardSpellSlot8 = 1                  
            if bardlvl >= 17:
                BardSpellsKnown = 20
                BardSpellSlot9 = 1 
            if bardlvl >= 18:
                player.classnotes.append("Magical Secrets(3) (see notes)")
                player.notes.append("Magical Secrets(3) - You have plundered magical knowledge from a wide spectrum of disciplines. Choose two more spells from any classes, including this one. A spell you choose must be of a level you can cast, as shown on the Bard table, or a cantrip.\nThe chosen spells count as bard spells for you and are included in the number in the Spells Known column of the Bard table.\nYou learn additional spells at higher levels.")
                BardSpellsKnown = 22
                BardSpellSlot5 = 3  
            if bardlvl >= 19:
                BardSpellSlot6 = 2                         
            if bardlvl == 20:
                player.classnotes.append("Superior Inspiration - When you roll initiative and have no uses of Bardic Inspiration left, you regain one use.")
                BardSpellSlot7 = 2
            player.notes.append(f"You have {BardCantripsKnown} cantrips available to you.")
            player.notes.append(f"You know {BardSpellsKnown} spells.")
            player.notes.append(f"The number of first level spell slots you have as a Bard is: {BardSpellSlot1}.")
            if BardSpellSlot2 != 0:
                player.notes.append(f"The number of second level spell slots you have as a Bard is: {BardSpellSlot2}.")
            if BardSpellSlot3 != 0:                
                player.notes.append(f"The number of third level spell slots you have as a Bard is: {BardSpellSlot3}.")
            if BardSpellSlot4 != 0:
                player.notes.append(f"The number of fourth level spell slots you have as a Bard is: {BardSpellSlot4}.")
            if BardSpellSlot5 != 0:
                player.notes.append(f"The number of fifth level spell slots you have as a Bard is: {BardSpellSlot5}.")
            if BardSpellSlot6 != 0:
                player.notes.append(f"The number of sixth level spell slots you have as a Bard is: {BardSpellSlot6}.")
            if BardSpellSlot7 != 0:
                player.notes.append(f"The number of seventh level spell slots you have as a Bard is: {BardSpellSlot7}.")
            if BardSpellSlot8 != 0:
                player.notes.append(f"The number of eighth level spell slots you have as a Bard is: {BardSpellSlot8}.")
            if BardSpellSlot9 != 0:
                player.notes.append(f"The number of ninth level spell slots you have as a Bard is: {BardSpellSlot9}.")
        if player.Class[i] == "Cleric":
            if ((param == "N") or (player.singlemulticlass == "N")):
                clerlvl = player.level
                player.classlvl.append(clerlvl) 
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    clerlvl = int(input(f"Given your pool of levels of {poollevel}, what is your Cleric level? "))    
                    if clerlvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                
                poollevel = poollevel - clerlvl
                player.classlvl.append(clerlvl)
            if clerlvl >= 1:
                player.hitdice.append(f"{clerlvl}d8 for {player.Class[i]}")
                if clerlvl == 1:
                    player.hitpoints += (8 + player.ConMod)
                else:
                    player.hitpoints += (8 + player.ConMod + hpcalc(clerlvl, dice, 8))   
                if i == 0:    
                    profs = ["Light Armor", "Medium Armor", "Shield"]         
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    player.skills.append(dnd_tools.saving_throws["WisST"])
                    player.skills.append(dnd_tools.saving_throws["ChaST"])
                    SkillsList = [
                        dnd_tools.skills["History"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Medicine"], 
                        dnd_tools.skills["Persuasion"], 
                        dnd_tools.skills["Religion"]
                        ]
                    player.skills = twoskillsfromlist(param, player.skills, SkillsList)   
                    StartEquip1 = ["Mace", "Warhammer (if proficient)"]
                    StartEquip2 = ["Scale Mail", "Leather Armor", "Chain Mail (if proficient)"]     
                    StartEquip3 = ["Light Crossbow w/ 20 Bolts", "Any Simple Weapon"]
                    StartEquip4 = ["Priest's Pack", "Explorer's Pack"]    
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Mace")
                        print("2 - Warhammer (if proficient)")
                        se1 = int(input("What would you like your first choice for starting equipment to be? "))
                        if se1 == 0:
                            SE1rand = random.choice(StartEquip1)
                            if SE1rand == "Mace":
                                player.equipment.append(dnd_tools.simple_weapons["Mace"].copy())
                            if SE1rand == "Warhammer (if proficient)":
                                if "Warhammer" in player.proficiencies:
                                    player.equipment.append(dnd_tools.martial_weapons["Warhammer"].copy())
                                else:
                                    player.equipment.append(dnd_tools.simple_weapons["Mace"].copy())
                        if se1 == 1:
                            player.equipment.append(dnd_tools.simple_weapons["Mace"].copy())
                        if se1 == 2:
                            if "Warhammer" in player.proficiencies:
                                player.equipment.append(dnd_tools.martial_weapons["Warhammer"].copy())
                            else:
                                player.equipment.append(dnd_tools.simple_weapons["Mace"].copy())
                        print("0 - Random")
                        print("1 - Scale Mail")
                        print("2 - Leather Armor")
                        print("3 - Chain Mail (if proficient)")
                        se2 = int(input("What would you like your second choice for starting equipment to be? "))
                        if se2 == 0:
                            SE2rand = random.choice(StartEquip2)
                            if SE2rand == "Scale Mail":
                                player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                            if SE2rand == "Leather Armor":
                                player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                            if SE2rand == "Chain Mail (if proficient)":
                                se2while = False
                                while not se2while:
                                    if ("Chain Mail" in player.proficiencies) or ("Heavy Armor" in player.proficiencies):
                                        player.equipment.append(dnd_tools.heavy_armor["ChainMail"].copy())
                                        se2while = True
                                    else:
                                        SE2rand = random.choice(StartEquip2)
                                        if SE2rand != "Chain Mail (if proficient)":
                                            if SE2rand == "Scale Mail":
                                                player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                                            if SE2rand == "Leather Armor":
                                                player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                                            se2while = True                                  
                        if se2 == 1:
                            player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                        if se2 == 2:
                            player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        if se2 == 3:
                            if ("Chain Mail" in player.proficiencies) or ("Heavy Armor" in player.proficiencies):
                                player.equipment.append(dnd_tools.heavy_armor["ChainMail"].copy())
                            else:
                                print("0 - Random")
                                print("1 - Scale Mail")
                                print("2 - Leather Armor")
                                se2 = int(input("You are not proficient in Chain Mail, please make a different choice. "))
                                if se2 == 0:
                                    SE2rand = random.choice(StartEquip2)
                                    if SE2rand == "Scale Mail":
                                        player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                                    if SE2rand == "Leather Armor":
                                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())      
                                if se2 == 1:
                                    player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                                if se2 == 2:
                                    player.equipment.append(dnd_tools.light_armor["Leather"].copy())                                                                                 
                        print("0 - Random")
                        print("1 - Light Crossbow w/ 20 Bolts")
                        print("2 - Any Simple Weapon")
                        se3 = int(input("What would you like your third choice for starting equipment to be? "))
                        if se3 == 0:
                            SE3rand = random.choice(StartEquip3)
                            if SE3rand == "Light Crossbow w/ 20 Bolts":
                                player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                                player.equipment.append("20 Bolts")
                            if SE3rand == "Any Simple Weapon":    
                                SimpKeyRand = random.choice(SimpleWeapons)                        
                                player.equipment.append(dnd_tools.simple_weapons[SimpKeyRand].copy())
                        if se3 == 1:
                            player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                            player.equipment.append("20 Bolts")
                        if se3 == 2:
                            print("0 - Random")
                            for j, sw in enumerate(SimpleWeaponsNames, 1):
                                print(f"{j} - {sw}")
                            se3sw = int(input("Which simple weapon would you like to add to your inventory? "))
                            if se3sw == 0:
                                SimpKeyRand = random.choice(SimpleWeapons)                        
                                player.equipment.append(dnd_tools.simple_weapons[SimpKeyRand].copy())
                            elif 1 <= se3sw <= len(SimpleWeapons):
                                SimpKey = SimpleWeapons[se3sw-1]
                                player.equipment.append(dnd_tools.simple_weapons[SimpKey].copy())                            
                        print("0 - Random")
                        print("1 - Priest's Pack")
                        print("2 - Explorer's Pack")
                        se4 = int(input("What would you like your fourth choice for starting equipment to be? "))                        
                        if se4 == 0:
                            SE4rand = random.choice(StartEquip4)
                            if SE4rand == "Priest's Pack":
                                player.equipment.extend(dnd_tools.packs["PriestsPack"]["contents"])
                            if SE4rand == "Explorer's Pack":
                                player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])
                        if se4 == 1:
                            player.equipment.extend(dnd_tools.packs["PriestsPack"]["contents"])
                        if se4 == 2:
                            player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])
                        player.equipment.append(dnd_tools.shields["Shield"].copy())
                        player.equipment.append("A Holy Symbol")
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "Mace":
                            player.equipment.append(dnd_tools.simple_weapons["Mace"].copy())
                        if SE1rand == "Warhammer (if proficient)":
                            if "Warhammer" in player.proficiencies:
                                player.equipment.append(dnd_tools.martial_weapons["Warhammer"].copy())
                            else:
                                player.equipment.append(dnd_tools.simple_weapons["Mace"].copy())           
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "Scale Mail":
                            player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                        if SE2rand == "Leather Armor":
                            player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        if SE2rand == "Chain Mail (if proficient)":
                            se2while = False
                            while not se2while:
                                if ("Chain Mail" in player.proficiencies) or ("Heavy Armor" in player.proficiencies):
                                    player.equipment.append(dnd_tools.heavy_armor["ChainMail"].copy())
                                    se2while = True
                                else:
                                    SE2rand = random.choice(StartEquip2)
                                    if SE2rand != "Chain Mail (if proficient)":
                                        if SE2rand == "Scale Mail":
                                            player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                                        if SE2rand == "Leather Armor":
                                            player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                                        se2while = True           
                        SE3rand = random.choice(StartEquip3)
                        if SE3rand == "Light Crossbow w/ 20 Bolts":
                            player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                            player.equipment.append("20 Bolts")
                        if SE3rand == "Any Simple Weapon":    
                            SimpKeyRand = random.choice(SimpleWeapons)                        
                            player.equipment.append(dnd_tools.simple_weapons[SimpKeyRand].copy())                                                               
                        SE4rand = random.choice(StartEquip4)
                        if SE4rand == "Priest's Pack":
                            player.equipment.extend(dnd_tools.packs["PriestsPack"]["contents"])
                        if SE4rand == "Explorer's Pack":
                            player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])                           
                        player.equipment.append(dnd_tools.shields["Shield"].copy())
                        player.equipment.append("A Holy Symbol")       
                else:
                    profs = ["Light Armor", "Medium Armor", "Shield"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof) 
                player.spellcastingclass.append("Cleric")
                player.spellcastingability.append("Wis")
                player.spellsavedc.append(8 + player.profbonus + player.WisMod)
                player.spellattackmod.append(player.profbonus + player.WisMod)
                ClericCantripsKnown = 3
                ClericSpellSlot1 = 2
                ClericSpellSlot2 = 0
                ClericSpellSlot3 = 0
                ClericSpellSlot4 = 0
                ClericSpellSlot5 = 0
                ClericSpellSlot6 = 0
                ClericSpellSlot7 = 0
                ClericSpellSlot8 = 0
                ClericSpellSlot9 = 0 
                Cle = ["Arcana Domain Cleric", "Blood Domain Cleric", "Commmunity Domain Cleric", "Death Domain Cleric", 'Forge Domain Cleric', "Grave Domain Cleric", "Knowledge Domain Cleric", "Life Domain Cleric", "Light Domain Cleric", "Moon Domain Cleric", "Nature Domain Cleric", "Night Domain Cleric", "Order Domain Cleric", "Peace Domain Cleric", "Tempest Domain Cleric", "Trickery Domain Cleric", "Twilight Domain Cleric", "War Domain Cleric"]
                

                if player.subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        for idx, subcl in enumerate(Cle, 1):
                            print(f"{idx} - {subcl}")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 0:
                            player.subclass[i] = random.choice(Cle)
                        elif 1 <= subc <= len(Cle):
                            player.subclass[i] = Cle[subc - 1]
                    if param == "N":
                        player.subclass[i] = random.choice(Cle)                          
                if player.subclass[i] == "Arcana Domain Cleric":
                    ClericArcanaDomainSpells = []
                    if clerlvl >= 1:
                        ClericArcanaDomainSpells.append("Detect Magic")
                        ClericArcanaDomainSpells.append("Magic Missile")
                    if clerlvl >= 3:
                        ClericArcanaDomainSpells.append("Magic Weapon")
                        ClericArcanaDomainSpells.append("Nystul's Magic Aura")
                    if clerlvl >= 5:
                        ClericArcanaDomainSpells.append("Dispel Magic")
                        ClericArcanaDomainSpells.append("Magic Circle")
                    if clerlvl >= 7:
                        ClericArcanaDomainSpells.append("Arcane Eye")
                        ClericArcanaDomainSpells.append("Leomund's Secret Chest")
                    if clerlvl >= 9:
                        ClericArcanaDomainSpells.append("Planar Binding")
                        ClericArcanaDomainSpells.append("Teleportation Circle")     
                    clericdomain_str = ", ".join(f"{spell}" for spell in ClericArcanaDomainSpells)         
                    player.classnotes.append("Domain Spells (see notes)")
                    player.notes.append(f"Domain Spells - Each domain has a list of spells — its domain spells — that you gain certain Cleric levels. Currently your Domain Spells are: {clericdomain_str}. Once you gain a domain spell, you always have it prepared, and it doesn’t count against the number of spells you can prepare each day.\nIf you have a domain spell that doesn’t appear on the cleric spell list, the spell is nonetheless a cleric spell for you.") 
                    player.skills.append(dnd_tools.skills["Arcana"])                                                                                 
                    player.classnotes.append("Arcane Initiate - You gain two cantrips of your choice from the wizard spell list. For you, these cantrips count as Cleric cantrips.")
                    if clerlvl >= 2:
                        if ((clerlvl >= 5) and (clerlvl < 8)):
                            ArcaneBanishment = "1/2 or lower"
                        if ((clerlvl >= 8) and (clerlvl < 11)):
                            ArcaneBanishment = "1 or lower"
                        if ((clerlvl >= 11) and (clerlvl < 14)):
                            ArcaneBanishment = "2 or lower"   
                        if ((clerlvl >= 14) and (clerlvl < 17)):
                            ArcaneBanishment = "3 or lower" 
                        if clerlvl >= 17:
                            ArcaneBanishment = "4 or lower"                                                                                
                        player.classnotes.append("Channel Divinity: Arcane Abjuration (see notes)")                
                        player.notes.append(f"Channel Divinity: Arcane Abjuration - You can use your Channel Divinity to abjure otherworldly creatures.\nAs an action, you present your holy symbol, and one celestial, elemental, fey, or fiend of your choice that is within 30 feet of you must make a Wisdom saving throw, provided that the creature can see or hear you. If the creature fails its saving throw, it is turned for 1 minute or until it takes any damage.\nA turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly end its move in a space within 30 feet of you. It also can't take reactions. For its action, it can only use the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action.\nAfter you reach 5th level, when a creature fails its saving throw against your Arcane Abjuration feature, the creature is banished for 1 minute (as in the Banishment spell, no concentration required) if it isn't on its plane of origin and its challenge rating is {ArcaneBanishment}.")
                        if clerlvl >= 6:
                            player.classnotes.append("Spell Breaker - When you restore hit points to an ally with a spell of 1st level or higher, you can also end one spell of your choice on that creature. The level of the spell you end must be equal to or lower than the level of the spell slot you use to cast the healing spell.")
                        if clerlvl >= 8:
                            player.classnotes.append(f"Potent Spellcasting - You add your Wisdom modifier, or {player.WisMod}, to the damage you deal with any cleric cantrip.")
                        if clerlvl >= 17:
                            player.classnotes.append("Arcane Mastery - You choose four spells from the wizard spell list, one from each of the following levels: 6th, 7th, 8th, and 9th. You add them to your list of domain spells. Like your other domain spells, they are always prepared and count as cleric spells for you.")
                if player.subclass[i] == "Blood Domain Cleric":
                    ClericBloodDomainSpells = []
                    if clerlvl >= 1:
                        ClericBloodDomainSpells.append("False Life")
                        ClericBloodDomainSpells.append("Sleep")
                    if clerlvl >= 3:
                        ClericBloodDomainSpells.append("Hold Person")
                        ClericBloodDomainSpells.append("Ray of Enfeeblement")
                    if clerlvl >= 5:
                        ClericBloodDomainSpells.append("Haste")
                        ClericBloodDomainSpells.append("Slow")
                    if clerlvl >= 7:
                        ClericBloodDomainSpells.append("Blight")
                        ClericBloodDomainSpells.append("Stoneskin")
                    if clerlvl >= 9:
                        ClericBloodDomainSpells.append("Dominate Person")
                        ClericBloodDomainSpells.append("Hold Monster") 
                    clericdomain_str = ", ".join(f"{spell}" for spell in ClericBloodDomainSpells)       

                    profs = ["Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)  
                    player.classnotes.append("Bloodletting Focus (see notes)")
                    player.notes.append("Bloodletting Focus - Your divine magic draws the blood from magically inflicted wounds, worsening the agony of your foes. When you cast a damage-dealing spell of 1st level or higher whose duration is instantaneous, any creature with blood that takes damage from the spell takes extra necrotic damage equal to 2 + the spell's level.")
                    if clerlvl >= 2:
                        player.classnotes.append("Channel Divinity: Crimson Bond (see notes)")
                        player.notes.append(f"Channel Divinity: Crimson Bond - You can use your Channel Divinity to form a supernatural bond with a creature you can see, or with a creature for which you possess a blood sample. This bond lasts for 1 hour or until your concentration is broken (as if concentrating on a spell).\nWhile the bond is in effect, you can use an action to learn the target's approximate distance and direction from you, as well as its current hit points and any conditions affecting it, as long as the target is within 10 miles of you. Alternatively, you can use your action to attempt to connect with the target's senses. You take 2d6 necrotic damage and the target makes a Constitution saving throw against your spell save DC, or against {player.spellsavedc[i]}. On a successful save, the bond ends. On a failure, you can choose to either see or hear through the target's senses for a number of minutes equal to your Wisdom modifier, or {player.WisMod} minutes, minimum 1 minute. During this time, you are blinded or deafened (respectively) with regard to your own senses. When the connection ends, the bond is lost.\nRegardless of the outcome, the target feels a wave of unease pass over it when it makes this save.")
                    if clerlvl >= 6:
                        player.classnotes.append("Channel Divinity: Blood Puppet(1) (see notes)")
                        player.notes.append(f"Channel Divinity: Blood Puppet(1) - You can use your Channel Divinity to briefly control a creature's actions—whether that creature is living or dead. As an action, you target a Large or smaller creature or corpse within 60 feet of you that has blood. A creature you target must succeed on a Wisdom saving throw against your spell save DC, or against {player.spellsavedc[i]}, or become charmed by you. An unconscious creature automatically fails its saving throw, and isn't incapacitated while you control its actions. A corpse targeted by this effect gains a semblance of life that you control.\nOn the affected creature or animated corpse's turn, you can command it (no action required) to move up to half its speed and use its action to do one of the following:\n- Interact with an object\n- Make a single attack\n- Do nothing\nAn animated corpse or an unconscious creature takes its turn immediately after yours, but can't move or take actions unless you command it to do so. Its statistics are the same as when it was alive or conscious.\nAn affected living creature makes a new saving throw at the end of each of its turns, ending the effect on itself on a success. For any target, your control lasts for 1 minute or until your concentration is broken (as if concentrating on a spell).")
                        player.classnotes.append("Sanguine Recall (see notes)")
                        player.notes.append(f"Sanguine Recall - You can sacrifice a portion of your own vitality to recover expended spell slots as an action. The spell slots can have a combined level equal to or less than half your Cleric level (rounded up), or less than or equal to {math.ceil(clerlvl/2)}, and none of the slots can be 6th level or higher. You take 1d8 necrotic damage for each spell slot level recovered, which can't be reduced in any way. You can't use this feature again until you finish a long rest.\nFor example, if you're an 8th-level cleric, you can recover up to four levels of spell slots—a single 4th-level slot, two 2nd-level slots, a 3rd-level slot and a 1st-level slot, or four 1st-level slots. You then take 4d8 necrotic damage.")
                    if clerlvl >= 8:
                        ClericDivineStrike = "1d8"
                        if clerlvl >= 14:
                            ClericDivineStrike = "2d8"
                            player.classnotes.append(f"Divine Strike - You gain the ability to cause the physical wounds you deal out to bleed profusely. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {ClericDivineStrike} necrotic damage to the target.")
                    if clerlvl >= 17:
                        player.classnotes.append("Channel Divinity: Blood Puppet(2) - You can use this feature to target a Huge or smaller creature or corpse.")
                        player.classnotes.append("Vascular Corruption Aura (see notes)")
                        player.notes.append("Vascular Corruption Aura - You can use your action to emit a deathly aura of necrotic energy that causes the veins of nearby foes to burst and bleed. For 1 minute, any hostile creature with blood that moves within 30 feet of you for the first time on a turn or starts its turn there takes 3d6 necrotic damage. If a hostile creature with blood regains hit points while in the aura, it regains only half as many hit points as expected.\nOnce you use this feature, you can't use it again until you finish a long rest.")
                if player.subclass[i] == "Commmunity Domain Cleric":
                    ClericCommunityDomainSpells = []
                    if clerlvl >= 1:
                        ClericCommunityDomainSpells.append("Bless")
                        ClericCommunityDomainSpells.append("Goodberry")
                    if clerlvl >= 3:
                        ClericCommunityDomainSpells.append("Aid")
                        ClericCommunityDomainSpells.append("Heroism")
                    if clerlvl >= 5:
                        ClericCommunityDomainSpells.append("Beacon of Hope")
                        ClericCommunityDomainSpells.append("Spirit Guardians")
                    if clerlvl >= 7:
                        ClericCommunityDomainSpells.append("Banishment")
                        ClericCommunityDomainSpells.append("Faithful Hound")
                    if clerlvl >= 9:
                        ClericCommunityDomainSpells.append("Mass Cure Wounds")
                        ClericCommunityDomainSpells.append("Telepathic Bond") 
                    clericdomain_str = ", ".join(f"{spell}" for spell in ClericCommunityDomainSpells)    

                    profs = ["Cooking Utensils"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof) 
                    player.classnotes.append("Blessing of the Hearth (see notes)")
                    player.notes.append("Blessing of the Hearth - You gain the ability to conjure a small flagstone hearth with a simple iron cooking pot whenever you rest. This hearth helps warm you and your companions, and can be used to prepare hearty and nutritious meals on the road. If you or any friendly creatures you make camp with would regain hit points at the end of a short rest by spending one or more hit dice, each of those creatures may choose to re-roll one of their resting dice, taking the higher roll between the two.")
                    if clerlvl >= 2:
                        player.classnotes.append("Channel Divinity: Magnificent Feast (see notes)")
                        player.notes.append(f"Channel Divinity: Magnificent Feast - You may use your Channel Divinity to conjure a magical feast for the rough road ahead. By spending 10 minutes, you may create a number of delicious, well-prepared, yet simple food items equal to your Wisdom modifier, or {player.WisMod} food items, minimum of 1. These food items will last up to 8 hours or until the end of a rest, and will never spoil. Eating food created in this way takes an action, providing whomever eats it with healing equal to 2d4 + your Cleric level, or 2d4 + {clerlvl} healing, and can remove either the frightened or poisoned condition from that creature (chosen by the creature when consumed).")
                    if clerlvl >= 6:
                        player.classnotes.append("Channel Divinity: Community Watch (see notes)")
                        player.notes.append(f"Channel Divinity: Community Watch - You can use your Channel Divinity to instill a feeling of vigilant protection in you and your allies. You grant yourself and a number of allies, up to your Wisdom modifier, or {player.WisMod} allies, minimum of 1, a boon from your deity. Allies must be able to see you and be within 30 feet to receive the boon. Once per round, a creature benefitting from this boon can roll a d6, adding the result to a skill check, saving throw, or attack roll. This effect lasts for a number of rounds equal to your Wisdom modifier, or {player.WisMod} rounds, minimum of 1 round. A creature can only benefit from this effect if it can see at least one of its allies.")
                    if clerlvl >= 8:
                        ClericDivineStrike = "1d8"
                        if clerlvl >= 14:
                            ClericDivineStrike = "2d8"
                        player.classnotes.append("Divine Strike (see notes)")
                        player.notes.append(f"Divine Strike - You gain the ability to infuse your weapon with the power to punish wrongdoing. Once on each of your turns, when you hit a creature with a weapon attack, you can cause the attack to deal an extra {ClericDivineStrike} psychic damage to the target. Visions of the evil they have wrought upon others flash before their eyes. You choose whether any foe reduced to 0 hit points by this attack remains stable or dies.")
                    if clerlvl >= 17:
                        player.classnotes.append("Paragon of the People (see notes)")
                        player.notes.append("Paragon of the People - Your Community Watch grants an additional d6 to each affected ally. It also grants immunity to fear for the duration of the effect. Additionally, your Magnificent Feast produces twice as many foodstuffs, each of which can, when consumed, remove a single curse or disease affecting the target (including attunement to a cursed item).")
                if player.subclass[i] == "Death Domain Cleric":
                    ClericDeathDomainSpells = []
                    if clerlvl >= 1:
                        ClericDeathDomainSpells.append("False Life")
                        ClericDeathDomainSpells.append("Ray of Sickness")
                    if clerlvl >= 3:
                        ClericDeathDomainSpells.append("Blindness/Deafness")
                        ClericDeathDomainSpells.append("Ray of Enfeeblement")
                    if clerlvl >= 5:
                        ClericDeathDomainSpells.append("Animate Dead")
                        ClericDeathDomainSpells.append("Vampiric Touch")
                    if clerlvl >= 7:
                        ClericDeathDomainSpells.append("Blight")
                        ClericDeathDomainSpells.append("Death Ward")
                    if clerlvl >= 9:
                        ClericDeathDomainSpells.append("Antilife Shell")
                        ClericDeathDomainSpells.append("Cloudkill") 
                    clericdomain_str = ", ".join(f"{spell}" for spell in ClericDeathDomainSpells)      

                    profs = ["Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)  
                    player.classnotes.append("Reaper - You learn one necromancy cantrip of your choice from any spell list. When you cast a necromancy cantrip that normally targets only one creature, the spell can instead target two creatures within range and within 5 feet of each other.")
                    if clerlvl >= 2:
                        player.classnotes.append(f"Channel Divinity: Touch of Death - You can use Channel Divinity to destroy another creature's life force by touch. When you hit a creature with a melee attack, you can use Channel Divinity to deal extra necrotic damage to the target. The damage equals {5 + (2*clerlvl)}.")
                    if clerlvl >= 6:
                        player.classnotes.append("Inescapable Destruction - Your ability to channel negative energy becomes more potent. Necrotic damage dealt by your cleric spells and Channel Divinity options ignores resistance to necrotic damage.")
                    if clerlvl >= 8:
                        ClericDivineStrike = "1d8"
                        if clerlvl >= 14:
                            ClericDivineStrike = "2d8"
                        player.classnotes.append(f"Divine Strike - You gain the ability to infuse your weapon strikes with necrotic energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an a {ClericDivineStrike} necrotic damage to the target.")
                    if clerlvl >= 17:
                        player.classnotes.append("Improved Reaper - When you cast a necromancy spell of 1st through 5th level that targets only one creature, the spell can instead target two creatures within range and within 5 feet of each other. If the spell consumes its material components, you must provide them for each target.")
                if player.subclass[i] == "Forge Domain Cleric":
                    ClericForgeDomainSpells = []
                    if clerlvl >= 1:
                        ClericForgeDomainSpells.append("Identify")
                        ClericForgeDomainSpells.append("Searing Smite")
                    if clerlvl >= 3:
                        ClericForgeDomainSpells.append("Heat Metal")
                        ClericForgeDomainSpells.append("Magic Weapon")                        
                    if clerlvl >= 5:
                        ClericForgeDomainSpells.append("Elemental Weapon")
                        ClericForgeDomainSpells.append("Protection from Energy")
                    if clerlvl >= 7:
                        ClericForgeDomainSpells.append("Fabricate")
                        ClericForgeDomainSpells.append("Wall of Fire")
                    if clerlvl >= 9:
                        ClericForgeDomainSpells.append("Animate Objects")
                        ClericForgeDomainSpells.append("Creation") 
                    clericdomain_str = ", ".join(f"{spell}" for spell in ClericForgeDomainSpells)   

                    profs = ["Heavy Armor", "Smith's Tools"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    player.classnotes.append("Blessing of the Forge (see notes)")
                    player.notes.append("Blessing of the Forge - You gain the ability to imbue magic into a weapon or armor. At the end of a long rest, you can touch one nonmagical object that is a suit of armor or a simple or martial weapon. Until the end of your next long rest or until you die, the object becomes a magic item, granting a +1 bonus to AC if it’s armor or a +1 bonus to attack and damage rolls if it’s a weapon.\nOnce you use this feature, you can’t use it again until you finish a long rest.")
                    if clerlvl >= 2:
                        player.classnotes.append("Channel Divinity: Artisan's Blessing (see notes)")
                        player.notes.append("Channel Divinity: Artisan's Blessing - You can use your Channel Divinity to create simple items.\nYou conduct an hour-long ritual that crafts a nonmagical item that must include some metal: a simple or martial weapon, a suit of armor, ten pieces of ammunition, a set of tools, or another metal object. The creation is completed at the end of the hour, coalescing in an unoccupied space of your choice on a surface within 5 feet of you.\nThe thing you create can be something that is worth no more than 100 gp. As part of this ritual, you must lay out metal, which can include coins, with a value equal to the creation. The metal irretrievably coalesces and transforms into the creation at the ritual’s end, magically forming even nonmetal parts of the creation.\nThe ritual can create a duplicate of a nonmagical item that contains metal, such as a key, if you possess the original during the ritual.")
                    if clerlvl >= 6:
                        player.classnotes.append("Soul of the Forge - Your mastery of the forge grants you special abilities:\n- You gain resistance to fire damage.\n- While wearing heavy armor, you gain a +1 bonus to AC.")
                    if clerlvl >= 8:
                        ClericDivineStrike = "1d8"
                        if clerlvl >= 14:
                            ClericDivineStrike = "2d8"
                        player.classnotes.append(f"Divine Strike - You gain the ability to infuse your weapon strikes with the fiery power of the forge. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {ClericDivineStrike} fire damage to the target.")
                    if clerlvl >= 17:
                        player.classnotes.append("Saint of Forge and Fire - Your blessed affinity with fire and metal becomes more powerful:\n- You gain immunity to fire damage.\n- While wearing heavy armor, you have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks.")                            
                if player.subclass[i] == "Grave Domain Cleric":
                    ClericGraveDomainSpells = []
                    if clerlvl >= 1:
                        ClericGraveDomainSpells.append("Bane")
                        ClericGraveDomainSpells.append("False Life")
                    if clerlvl >= 3:
                        ClericGraveDomainSpells.append("Gentle Repose")
                        ClericGraveDomainSpells.append("Ray of Enfeeblement")
                    if clerlvl >= 5:
                        ClericGraveDomainSpells.append("Revivify")
                        ClericGraveDomainSpells.append("Vampiric Touch")
                    if clerlvl >= 7:
                        ClericGraveDomainSpells.append("Blight")
                        ClericGraveDomainSpells.append("Death Ward")
                    if clerlvl >= 9:
                        ClericGraveDomainSpells.append("Antilife Shell")
                        ClericGraveDomainSpells.append("Raise Dead")                 
                    clericdomain_str = ", ".join(f"{spell}" for spell in ClericGraveDomainSpells)    
                    player.classnotes.append("Domain Spells (see notes)")
                    player.notes.append(f"Domain Spells - Each domain has a list of spells — its domain spells — that you gain certain Cleric levels. Currently your Domain Spells are: {clericdomain_str}. Once you gain a domain spell, you always have it prepared, and it doesn’t count against the number of spells you can prepare each day.\nIf you have a domain spell that doesn’t appear on the cleric spell list, the spell is nonetheless a cleric spell for you.")                    
                    player.classnotes.append("Circle of Mortality (see notes)")
                    player.notes.append("Circle of Mortality - You gain the ability to manipulate the line between life and death. When you would normally roll one or more dice to restore hit points with a spell to a creature at 0 hit points, you instead use the highest number possible for each die.\nIn addition, you learn the Spare the Dying cantrip, which doesn't count against the number of cleric cantrips you know. For you, it has a range of 30 feet, and you can cast it as a bonus action.")
                    player.classnotes.append("Eyes of the Grave (see notes)")
                    player.notes.append(f"Eyes of the Grave - You gain the ability to occasionally sense the presence of the undead, whose existence is an insult to the natural cycle of life. As an action, you can open your awareness to magically detect undead. Until the end of your next turn, you know the location of any undead within 60 feet of you that isn't behind total cover and that isn't protected from divination magic. This sense doesn't tell you anything about a creature's capabilities or identity.\nYou can use this feature a number of times equal to your Wisdom modifier, or {player.WisMod} times, minimum of once. You regain all expended uses when you finish a long rest.")
                    if clerlvl >= 2:
                        player.classnotes.append("Channel Divinity: Path to the Grave (see notes)")
                        player.notes.append("Channel Divinity: Path to the Grave - You can use your Channel Divinity to mark another creature’s life force for termination.\nAs an action, you choose one creature you can see within 30 feet of you, cursing it until the end of your next turn. The next time you or an ally of yours hits the cursed creature with an attack, the creature has vulnerability to all of that attack's damage, and then the curse ends.")
                    if clerlvl >= 6:
                        player.classnotes.append("Sentinel at Death's Door (see notes)")
                        player.notes.append(f"Sentinel at Death's Door - You gain the ability to impede death’s progress. As a reaction when you or an ally that you can see within 30 feet of you suffers a critical hit, you can turn that attack into a normal hit. Any effects triggered by a critical hit are canceled.\nYou can use this feature a number of times equal to your Wisdom modifier, or {player.WisMod} times, minimum of once. You regain all expended uses when you finish a long rest.")
                    if clerlvl >= 8:
                        player.classnotes.append(f"Potent Spellcasting - You add your Wisdom modifier, or {player.WisMod}, to the damage you deal with any cleric cantrip.")
                    if clerlvl >= 17:
                        player.classnotes.append("Keeper of Souls (see notes)")        
                        player.notes.append("Keeper of Souls - You can seize a trace of vitality from a parting soul and use it to heal the living. When an enemy you can see dies within 30 feet of you, you or one ally of your choice that is within 30 feet of you regains hit points equal to the enemy’s number of Hit Dice. You can use this feature only if you aren't incapacitated. Once you use it, you can't do so again until the start of your next turn.")             
                if player.subclass[i] == "Knowledge Domain Cleric":
                    ClericKnowledgeDomainSpells = []
                    if clerlvl >= 1:
                        ClericKnowledgeDomainSpells.append("Command")
                        ClericKnowledgeDomainSpells.append("Identify")
                    if clerlvl >= 3:
                        ClericKnowledgeDomainSpells.append("Augury")
                        ClericKnowledgeDomainSpells.append("Suggestion")
                    if clerlvl >= 5:
                        ClericKnowledgeDomainSpells.append("Nondetection")
                        ClericKnowledgeDomainSpells.append("Speak with Dead")
                    if clerlvl >= 7:
                        ClericKnowledgeDomainSpells.append("Arcane Eye")
                        ClericKnowledgeDomainSpells.append("Confusion")
                    if clerlvl >= 9:
                        ClericKnowledgeDomainSpells.append("Legend Lore")
                        ClericKnowledgeDomainSpells.append("Scrying") 
                    clericdomain_str = ", ".join(f"{spell}" for spell in ClericKnowledgeDomainSpells)    
                    player.classnotes.append("Domain Spells (see notes)")
                    player.notes.append(f"Domain Spells - Each domain has a list of spells — its domain spells — that you gain certain Cleric levels. Currently your Domain Spells are: {clericdomain_str}. Once you gain a domain spell, you always have it prepared, and it doesn’t count against the number of spells you can prepare each day.\nIf you have a domain spell that doesn’t appear on the cleric spell list, the spell is nonetheless a cleric spell for you.")                    
                    player.languages, player.slang = languagegen(param, player.languages, player.slang)
                    player.languages, player.slang = languagegen(param, player.languages, player.slang)
                    player.classnotes.append("Blessings of Knowledge - Your Proficiency Bonus is doubled for any ability check you make that uses either of those skills.")
                    if clerlvl >= 2:
                        player.classnotes.append("Channel Divinity: Knowledge of the Ages - You can use your Channel Divinity to tap into a divine well of knowledge. As an action, you choose one skill or tool. For 10 minutes, you have proficiency with the chosen skill or tool.")
                    if clerlvl >= 6:
                        player.classnotes.append("Channel Divinity: Read Thoughts (see notes)")
                        player.notes.append("Channel Divinity: Read Thoughts - You can use your Channel Divinity to read a creature's thoughts. You can then use your access to the creature's mind to command it.\nAs an action, choose one creature that you can see within 60 feet of you. That creature must make a Wisdom saving throw. If the creature succeeds on the saving throw, you can't use this feature on it again until you finish a long rest.\nIf the creature fails its save, you can read its surface thoughts (those foremost in its mind, reflecting its current emotions and what it ie actively thinking about) when it is within 60 feet of you. This effect lasts for 1 minute.\nDuring that time, you can use your action to end this effect and cast the Suggestion spell on the creature without expending a spell slot. The target automatically fails its saving throw against the spell.")
                    if clerlvl >= 8:
                        player.classnotes.append(f"Potent Spellcasting - You add your Wisdom modifier, or {player.WisMod}, to the damage you deal with any cleric cantrip.")
                    if clerlvl >= 17:
                        player.classnotes.append("Visions of the Past (see notes)")        
                        player.notes.append("Visions of the Past - You can call up visions of the past that relate to an object you hold or your immediate surroundings. You spend at least 1 minute in meditation and prayer, then receive dreamlike, shadowy glimpses of recent events. You can meditate in this way for a number of minutes equal to your Wisdom score and must maintain concentration during that time, as if you were casting a spell.\nOnce you use this feature, you can't use it again until you finish a short or long rest.\nObject Reading - Holding an object as you meditate, you can see visions of the object's previous owner. After meditating for 1 minute, you learn how the owner acquired and lost the object, as well as the most recent significant event involving the object and that owner. If the object was owned by another creature in the recent past (within a number of days equal to your Wisdom score), you can spend 1 additional minute for each owner to learn the same information about that creature.\nArea Reading - As you meditate, you see visions of recent events in your immediate vicinity (a room, street, tunnel, clearing, or the like, up to a 50-foot cube), going back a number of days equal to your Wisdom score. For each minute you meditate, you learn about one significant event, beginning with the most recent. Significant events typically involve powerful emotions, such as battles and betrayals, marriages and murders, births and funerals. However, they might also include more mundane events that are nevertheless important in your current situation.")                   
                if player.subclass[i] == "Life Domain Cleric":
                    ClericLifeDomainSpells = []
                    if clerlvl >= 1:
                        ClericLifeDomainSpells.append("Bless")
                        ClericLifeDomainSpells.append("Cure Wounds")
                    if clerlvl >= 3:
                        ClericLifeDomainSpells.append("Lesser Restoration")
                        ClericLifeDomainSpells.append("Spiritual Weapon")
                    if clerlvl >= 5:
                        ClericLifeDomainSpells.append("Beacon of Hope")
                        ClericLifeDomainSpells.append("Revivify")
                    if clerlvl >= 7:
                        ClericLifeDomainSpells.append("Death Ward")
                        ClericLifeDomainSpells.append("Guardian of Faith")
                    if clerlvl >= 9:
                        ClericLifeDomainSpells.append("Mass Cure Wounds")
                        ClericLifeDomainSpells.append("Raise Dead") 
                    clericdomain_str = ", ".join(f"{spell}" for spell in ClericLifeDomainSpells)   

                    profs = ["Heavy Armor"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    player.classnotes.append("Disciple of Life - Your healing spells are more effective. Whenever you use a spell of 1st level or higher to restore hit points to a creature, the creature regains additional hit points equal to 2 + the spell's level.")
                    if clerlvl >= 2:
                        player.classnotes.append("Channel Divinity: Preserve Life (see notes)")
                        player.notes.append(f"Channel Divinity: Preserve Life - You can use your Channel Divinity to heal the badly injured.\nAs an action, you present your holy symbol and evoke healing energy that can restore a number of hit points equal to five times your Cleric level, or {5*clerlvl} hit points. Choose any creatures within 30 feet of you, and divide those hit points among them. This feature can restore a creature to no more than half of its hit point maximum. You can't use this feature on an undead or a construct.")
                    if clerlvl >= 6:
                        player.classnotes.append("Blessed Healer - The healing spells you cast on others heal you as well. When you cast a spell of 1st level or higher that restores hit points to a creature other than you, you regain hit points equal to 2 + the spell's level.")
                    if clerlvl >= 8:
                        ClericDivineStrike = "1d8"
                        if clerlvl >= 14:
                            ClericDivineStrike = "2d8"
                        player.classnotes.append(f"Divine Strike - You gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {ClericDivineStrike} radiant damage to the target.")
                    if clerlvl >= 17:
                        player.classnotes.append("Supreme Healing - When you would normally roll one or more dice to restore hit points with a spell, you instead use the highest number possible for each die. For example, instead of restoring 2d6 hit points to a creature, you restore 12.")        
                if player.subclass[i] == "Light Domain Cleric":
                    ClericLightDomainSpells = []
                    if clerlvl >= 1:
                        ClericLightDomainSpells.append("Burning Hands")
                        ClericLightDomainSpells.append("Faerie Fire")
                    if clerlvl >= 3:
                        ClericLightDomainSpells.append("Flaming Sphere")
                        ClericLightDomainSpells.append("Scorching Ray")
                    if clerlvl >= 5:
                        ClericLightDomainSpells.append("Daylight")
                        ClericLightDomainSpells.append("Fireball")
                    if clerlvl >= 7:
                        ClericLightDomainSpells.append("Guardian of Faith")
                        ClericLightDomainSpells.append("Wall of Fire")
                    if clerlvl >= 9:
                        ClericLightDomainSpells.append("Flame Strike")
                        ClericLightDomainSpells.append("Scrying") 
                    clericdomain_str = ", ".join(f"{spell}" for spell in ClericLightDomainSpells)    

                    player.classnotes.append("Bonus Cantrip - You gain the Light cantrip if you don't already know it.")
                    player.classnotes.append("Warding Flare (see notes)")
                    player.notes.append(f"Warding Flare - You can interpose divine light between yourself and an attacking enemy. When you are attacked by a creature within 30 feet of you that you can see, you can use your reaction to impose disadvantage on the attack roll, causing light to flare before the attacker before it hits or misses. An attacker that can't be blinded is immune to this feature.\nYou can use this feature a number of times equal to your Wisdom modifier, or {player.WisMod} times, a minimum of once. You regain all expended uses when you finish a long rest.")
                    if clerlvl >= 2:
                        player.classnotes.append("Channel Divinity: Radiance of the Dawn (see notes)")
                        player.notes.append(f"Channel Divinity: Radiance of the Dawn - You can use your Channel Divinity to harness sunlight, banishing darkness and dealing radiant damage to your foes.\nAs an action, you present your holy symbol, and any magical darkness within 30 feet of you is dispelled. Additionally, each hostile creature within 30 feet of you must make a Constitution saving throw. A creature takes radiant damage equal to 2d10 + your Cleric level, or 2d10 + {clerlvl} radiant damage, on a failed saving throw, and half as much damage on a successful one. A creature that has total cover from you is not affected.")
                    if clerlvl >= 6:
                        player.classnotes.append("Improved Flare - You can also use your Warding Flare feature when a creature that you can see within 30 feet of you attacks a creature other than you.")
                    if clerlvl >= 8:
                        player.classnotes.append(f"Potent Spellcasting - You can add your Wisdom modifier, or {player.WisMod}, when you deal with any cleric cantrip.")
                    if clerlvl >= 17:
                        player.classnotes.append("Corona of Light (see notes)")      
                        player.notes.append("Corona of Light - You can use your action to activate an aura of sunlight that lasts for 1 minute or until you dismiss it using another action. You emit bright light in a 60-foot radius and dim light 30 feet beyond that. Your enemies in the bright light have disadvantage on saving throws against any spell that deals fire or radiant damage.")                 
                if player.subclass[i] == "Moon Domain Cleric":
                    ClericMoonDomainSpells = []
                    if clerlvl >= 1:
                        ClericMoonDomainSpells.append("Faerie Fire")
                        ClericMoonDomainSpells.append("Silent Image")
                    if clerlvl >= 3:
                        ClericMoonDomainSpells.append("Invisibility")
                        ClericMoonDomainSpells.append("Moonbeam")
                    if clerlvl >= 5:
                        ClericMoonDomainSpells.append("Hypnotic Pattern")
                        ClericMoonDomainSpells.append("Major Image")
                    if clerlvl >= 7:
                        ClericMoonDomainSpells.append("Greater Invisibility")
                        ClericMoonDomainSpells.append("Hallucinatory Terrain")
                    if clerlvl >= 9:
                        ClericMoonDomainSpells.append("Dream")
                        ClericMoonDomainSpells.append("Passwall") 
                    clericdomain_str = ", ".join(f"{spell}" for spell in ClericMoonDomainSpells)   
                    player.classnotes.append("Domain Spells (see notes)")
                    player.notes.append(f"Domain Spells - Each domain has a list of spells — its domain spells — that you gain certain Cleric levels. Currently your Domain Spells are: {clericdomain_str}. Once you gain a domain spell, you always have it prepared, and it doesn’t count against the number of spells you can prepare each day.\nIf you have a domain spell that doesn’t appear on the cleric spell list, the spell is nonetheless a cleric spell for you.")                     
                    player.classnotes.append("Clarity of Catha (see notes)")
                    player.notes.append(f"Clarity of Catha - When you choose this domain at 1st level, you learn to shine light upon the mind's most dire moments, shielding those you protect. When a creature within 30 feet of you that you can see makes a Wisdom saving throw, you can use your reaction to grant that creature advantage on the save.\nYou can use this feature a number of times equal to your Proficiency Bonus, or {player.profbonus} times, regaining all expended uses when you finish a long rest.")
                    if clerlvl >= 2:
                        player.classnotes.append("Channel Divinity: Blessing of the Full Moon (see notes)")
                        player.notes.append("Channel Divinity: Blessing of the Full Moon - You can use your Channel Divinity to infuse your allies with bestial power. As an action, you instill a willing creature of your choice within 30 feet of you that you can see with one of the following blessings of your choice:\nBlessing of the Watchful Moon - For 1 hour, the blessed creature's speed increases by 10 feet, and it has advantage on Wisdom (Perception or Survival) checks involving smell or made to track a creature.\nBlessing of the Blood-Drenched Moon - For 10 minutes, the blessed creature has advantage on attack rolls against a target if at least one of the blessed creature's allies is within 5 feet of the target and the ally isn't incapacitated.")
                    if clerlvl >= 6:
                        player.classnotes.append("Channel Divinity: Mind of Two Moons (see notes)")
                        player.notes.append("Channel Divinity: Mind of Two Moons - You can use your Channel Divinity to invoke the twofold arcana of Exandria's moons. By expending one use of Channel Divinity, you can cast a second concentration spell while already concentrating on a first spell, as long as both spells are on your list of Moon Domain spells. If you need to make a Constitution saving throw to maintain your concentration on both spells, you make the save with disadvantage. On a failure, you lose concentration on both spells.")
                    if clerlvl >= 8:
                        player.classnotes.append(f"Empowered Cantrips - Your cleric cantrips deal extra damage equal to your Wisdom modifier, or {player.WisMod} extra damage, minimum of 1.")
                    if clerlvl >= 17:
                        player.classnotes.append("Eclipse of Ill Omen (see notes)")      
                        player.notes.append("Eclipse of Ill Omen - You can call upon the vermillion moon Ruidus to flare in the sky above you, eclipsing all other light. Its power surrounds you even where the sky can't be seen, and even on other planes. As a bonus action, you can manifest an area of reddish, dim light in a 60-foot radius around you. In addition to the normal effects of dim light, creatures in the area make saving throws with disadvantage. When you create this eclipse, you can choose any number of creatures that are unaffected by it.\nThis eclipse lasts while you concentrate (as if concentrating on a spell) for up to 1 minute. Concentrating on this feature counts as concentrating on a Moon Domain spell for the purpose of your Mind of Two Moons feature.\nAdditionally, once per turn when you deal radiant damage to any creatures in this area of dim light, you can curse one of those creatures until the eclipse ends (no action required). A creature cursed in this way has its speed halved and can't regain hit points.\nOnce you use this feature, you can't use it again until you finish a long rest.")                         
                if player.subclass[i] == "Nature Domain Cleric":
                    ClericNatureDomainSpells = []
                    if clerlvl >= 1:
                        ClericNatureDomainSpells.append("Animal Friendship")
                        ClericNatureDomainSpells.append("Speak with Animals")
                    if clerlvl >= 3:
                        ClericNatureDomainSpells.append("Barkskin")
                        ClericNatureDomainSpells.append("Spike Growth")
                    if clerlvl >= 5:
                        ClericNatureDomainSpells.append("Plant Growth")
                        ClericNatureDomainSpells.append("Wind Wall")
                    if clerlvl >= 7:
                        ClericNatureDomainSpells.append("Dominate Beast")
                        ClericNatureDomainSpells.append("Grasping Vine")
                    if clerlvl >= 9:
                        ClericNatureDomainSpells.append("Insect Plague")
                        ClericNatureDomainSpells.append("Tree Stride") 
                    clericdomain_str = ", ".join(f"{spell}" for spell in ClericNatureDomainSpells)    
                    player.classnotes.append("Domain Spells (see notes)")
                    player.notes.append(f"Domain Spells - Each domain has a list of spells — its domain spells — that you gain certain Cleric levels. Currently your Domain Spells are: {clericdomain_str}. Once you gain a domain spell, you always have it prepared, and it doesn’t count against the number of spells you can prepare each day.\nIf you have a domain spell that doesn’t appear on the cleric spell list, the spell is nonetheless a cleric spell for you.")                    
                    SkillsList = [
                        dnd_tools.skills["AnimalHandling"], 
                        dnd_tools.skills["Nature"], 
                        dnd_tools.skills["Survival"]
                        ]
                    player.skills = oneskillfromlist(param, player.skills, SkillsList)
                    profs = ["Heavy Armor"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)               
                    player.classnotes.append("Acolyte of Nature - You learn one cantrip of your choice from the druid spell list.")
                    if clerlvl >= 2:
                        player.classnotes.append("Channel Divinity: Charm Animals and Plants (see notes)")
                        player.notes.append("Channel Divinity: Charm Animals and Plants - You can use your Channel Divinity to charm animals and plants.\nAs an action, you present your holy symbol and invoke the name of your deity. Each beast or plant creature that can see you within 30 feet of you must make a Wisdom saving throw. If the creature fails its saving throw, it is charmed by you for 1 minute or until it takes damage. While it is charmed by you, it is friendly to you and other creatures you designate.")
                    if clerlvl >= 6:
                        player.classnotes.append("Dampen Elements - When you or a creature within 30 feet of you takes acid, cold, fire, lightning, or thunder damage, you can use your reaction to grant resistance to the creature against that instance of the damage.")
                    if clerlvl >= 8:
                        ClericDivineStrike = "1d8"
                        if clerlvl >= 14:
                            ClericDivineStrike = "2d8"
                        player.classnotes.append(f"Divine Strike - You gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {ClericDivineStrike} cold, fire, or lightning damage (your choice) to the target.")
                    if clerlvl >= 17:
                        player.classnotes.append("Master of Nature - You gain the ability to command animals and plant creatures. While creatures are charmed by your Charm Animals and Plants feature, you can take a bonus action on your turn to verbally command what each of those creatures will do on its next turn.")                     
                if player.subclass[i] == "Night Domain Cleric":
                    ClericNightDomainSpells = []
                    if clerlvl >= 1:
                        ClericNightDomainSpells.append("Sleep")
                        ClericNightDomainSpells.append("Veil of Dusk")
                    if clerlvl >= 3:
                        ClericNightDomainSpells.append("Darkness")
                        ClericNightDomainSpells.append("Moonbeam")
                    if clerlvl >= 5:
                        ClericNightDomainSpells.append("Nondetection")
                        ClericNightDomainSpells.append("Globe of Twilight")
                    if clerlvl >= 7:
                        ClericNightDomainSpells.append("Divination")
                        ClericNightDomainSpells.append("Stellar Bodies")
                    if clerlvl >= 9:
                        ClericNightDomainSpells.append("Dream")
                        ClericNightDomainSpells.append("Seeming") 
                    clericdomain_str = ", ".join(f"{spell}" for spell in ClericNightDomainSpells)  

                    player.classnotes.append("Eye of Twilight(1) (see notes)")
                    player.notes.append("Eye of Twilight(1) - A divine blessing grants you the ability to see more clearly in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in magical or nonmagical darkness as if it were only dim light. You can’t discern color in the darkness, only shades of gray.")
                    player.classnotes.append("Ward of Shadows (see notes)")
                    player.notes.append(f"Ward of Shadows - You can create a ward of divine shadows to conceal yourself from an attacking enemy. When attacked by a creature you can see within 30 feet of you, you can use your reaction to impose disadvantage on the attack roll, as shadows envelop your form. An attacker that can’t be blinded is immune to this feature.\nYou can use this feature a number of times equal to your Wisdom modifier, or {player.WisMod} times, a minimum of once; and regain all expended uses when you finish a long rest.")
                    if clerlvl >= 2:
                        player.classnotes.append("Channel Divinity: Invocation of Night (see notes)")
                        player.notes.append(f"Channel Divinity: Invocation of Night - You can use your Channel Divinity to harness the powers of night, clouding the vision of your foes in a shroud of darkness.\nAs an action, you present your holy symbol causing any source of mundane or magical light within 30 feet of you to be extinguished. Additionally, each hostile creature within 30 feet of you must make a Constitution saving throw. A creature who fails the saving throw is blinded for a number of rounds equal to your Cleric level, or {clerlvl} rounds. A creature blinded in this way gets a new saving throw at the end of each of its turns to remove the effect. A creature that has total cover from you is not affected.")
                    if clerlvl >= 6:
                        player.classnotes.append("Eye of Twilight(2) (see notes)")
                        player.notes.append("Eye of Twilight(2) - You can see in dim light within 120 feet of you as if it were bright light, and in magical or nonmagical darkness as if it were dim light. You can’t discern color in the darkness, only shades of gray.")                            
                        player.classnotes.append("Improved Ward - You can use your Ward of Shadows feature whenever a creature you can see within 30 feet of you attacks a creature besides yourself.")
                    if clerlvl >= 8:
                        player.classnotes.append("Veil of Dreams (see notes)")
                        player.notes.append(f"Veil of Dreams - You gain mastery over magical sleep. When you cast the sleep spell, add your Cleric level, or {clerlvl} to the dice you roll to determine how many hit points of creatures the spell can affect.\nYou may choose the order in which creatures within the spell’s area are affected. If the first target chosen has too many hit points to be affected, the spell will instead target the next creature you have chosen that the spell could affect before affecting other targets.\nAdditionally, any creature you put to sleep cannot be woken until the start of your next turn. Otherwise, the sleep spell acts as normal.")
                        player.classnotes.append("Eyes of Twilight(2): Improved Darkvision - You can see normally in darkness, both magical and nonmagical within 120 feet.") 
                    if clerlvl >= 17:
                        player.classnotes.append("Creature of the Night (see notes)")      
                        player.notes.append("Creature of the Night - You can use your action to activate a supernatural aura of deep night. It lasts for 1 minute, or until you dismiss it using another action. You emit heavily obscuring darkness in a 30-foot radius and lightly obscuring shadows 50 feet beyond that. The darkness and shadows overlap and smother existing sources of light. Only light produced by a 9th level spell or similarly powerful effect can negate the darkness and shadows.\nEnemies within the shadows constantly feel the presence of hungry predators watching them, and become frightened as long as they remain inside the affected area. Enemies in the darkness are both blinded and frightened for as long as they remain within its area.")   
                        player.classnotes.append("Eye of Twilight(3) (see notes)")
                        player.notes.append(f"Eye of Twilight(3) - Your eyes are able to see the truth hiding within darkness. You gain the ability to call upon the powers of your deity to grant yourself truesight within 120 feet of you for a number of minutes equal to your Wisdom modifier, or {player.WisMod} minutes, a minimum of 1 minute. Your truesight only functions while in conditions of magical or nonmagical darkness. Once you have used this feature, you cannot use it again until you have completed a long rest.")                      
                if player.subclass[i] == "Order Domain Cleric":
                    ClericOrderDomainSpells = []
                    if clerlvl >= 1:
                        ClericOrderDomainSpells.append("Command")
                        ClericOrderDomainSpells.append("Heroism")
                    if clerlvl >= 3:
                        ClericOrderDomainSpells.append("Hold Person")
                        ClericOrderDomainSpells.append("Zone of Truth")
                    if clerlvl >= 5:
                        ClericOrderDomainSpells.append("Mass Healing Word")
                        ClericOrderDomainSpells.append("Slow")
                    if clerlvl >= 7:
                        ClericOrderDomainSpells.append("Compulsion")
                        ClericOrderDomainSpells.append("Locate Creature")
                    if clerlvl >= 9:
                        ClericOrderDomainSpells.append("Commune")
                        ClericOrderDomainSpells.append("Dominate Person") 
                    clericdomain_str = ", ".join(f"{spell}" for spell in ClericOrderDomainSpells)   

                    profs = ["Heavy Armor"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)  
                    SkillsList = [
                        dnd_tools.skills["Intimidation"], 
                        dnd_tools.skills["Persuasion"]
                        ]
                    player.skills = oneskillfromlist(param, player.skills, SkillsList)                    
                    player.classnotes.append("Voice of Authority (see notes)")
                    player.notes.append("Voice of Authority - You can invoke the power of law to drive an ally to attack. If you cast a spell with a spell slot of 1st level or higher and target an ally with the spell, that ally can use their reaction immediately after the spell to make one weapon attack against a creature of your choice that you can see.\nIf the spell targets more than one ally, you choose the ally who can make the attack.")
                    if clerlvl >= 2:
                        player.classnotes.append("Channel Divinity: Order's Demand (see notes)")
                        player.notes.append("Channel Divinity: Order's Demand - You can use your Channel Divinity to exert an intimidating presence over others.\nAs an action, you present your holy symbol, and each creature of your choice that can see or hear you within 30 feet of you must succeed on a Wisdom saving throw or be charmed by you until the end of your next turn or until the charmed creature takes any damage. You can also cause any of the charmed creatures to drop what they are holding when they fail the saving throw.")
                    if clerlvl >= 6:
                        player.classnotes.append("Embodiment of the Law (see notes)")
                        player.notes.append(f"Embodiment of the Law - You become remarkably adept at channeling magical energy to compel others.\nIf you cast a spell of the enchantment school using a spell slot of 1st level or higher, you can change the spell's casting time to 1 bonus action for this casting, provided the spell's casting time is normally 1 action.\nYou can use this feature a number of times equal to your Wisdom modifier, or {player.WisMod} times, minimum of once; and you regain all expended uses of it when you finish a long rest.")
                    if clerlvl >= 8:
                        ClericDivineStrike = "1d8"
                        if clerlvl >= 14:
                            ClericDivineStrike = "2d8"
                        player.classnotes.append(f"Divine Strike - You gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {ClericDivineStrike} psychic damage to the target.")
                    if clerlvl >= 17:
                        player.classnotes.append("Order's Wrath (see notes)")                       
                        player.notes.append("Order's Wrath - Enemies you designate for destruction wilt under the combined efforts of you and your allies. If you deal your Divine Strike damage to a creature on your turn, you can curse that creature until the start of your next turn. The next time one of your allies hits the cursed creature with an attack, the target also takes 2d8 psychic damage, and the curse ends. You can curse a creature in this way only once per turn.")
                if player.subclass[i] == "Peace Domain Cleric":
                    ClericPeaceDomainSpells = []
                    if clerlvl >= 1:
                        ClericPeaceDomainSpells.append("Heroism")
                        ClericPeaceDomainSpells.append("Sanctuary")
                    if clerlvl >= 3:
                        ClericPeaceDomainSpells.append("Aid")
                        ClericPeaceDomainSpells.append("Warding Bond")
                    if clerlvl >= 5:
                        ClericPeaceDomainSpells.append("Beacon of Hope")
                        ClericPeaceDomainSpells.append("Sending")
                    if clerlvl >= 7:
                        ClericPeaceDomainSpells.append("Aura of Purity")
                        ClericPeaceDomainSpells.append("Otiluke's Resilient Sphere")
                    if clerlvl >= 9:
                        ClericPeaceDomainSpells.append("Greater Restoration")
                        ClericPeaceDomainSpells.append("Rary's Telepathic Bond") 
                    clericdomain_str = ", ".join(f"{spell}" for spell in ClericPeaceDomainSpells)      

                    SkillsList = [
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Performance"], 
                        dnd_tools.skills["Persuasion"]
                        ]
                    player.skills = oneskillfromlist(param, player.skills, SkillsList)                    
                    player.classnotes.append("Emboldening Bond (see notes)")
                    player.notes.append(f"Emboldening Bond - You can forge an empowering bond among people who are at peace with one another. As an action, you choose a number of willing creatures within 30 feet of you (this can include yourself) equal to your Proficiency Bonus, or {player.profbonus} creatures. You create a magical bond among them for 10 minutes or until you use this feature again. While any bonded creature is within 30 feet of another, the creature can roll a d4 and add the number rolled to an attack roll, an ability check, or a saving throw it makes. Each creature can add the d4 no more than once per turn.\nYou can use this feature a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
                    if clerlvl >= 2:
                        player.classnotes.append("Channel Divinity: Balm of Peace (see notes)")
                        player.notes.append(f"Channel Divinity: Balm of Peace - You can use your Channel Divinity to make your very presence a soothing balm. As an action, you can move up to your speed, without provoking opportunity attacks, and when you move within 5 feet of any other creature during this action, you can restore a number of hit points to that creature equal to 2d6 + your Wisdom modifier, or 2d6 + {player.WisMod} hit points, minimum of 1 hit point. A creature can receive this healing only once whenever you take this action.")
                    if clerlvl >= 6:
                        player.classnotes.append("Protective Bond (see notes)")
                        player.notes.append("Protective Bond - The bond you forge between people helps them protect each other. When a creature affected by your Emboldening Bond feature is about to take damage, a second bonded creature within 30 feet of the first can use its reaction to teleport to an unoccupied space within 5 feet of the first creature. The second creature then takes all the damage instead.")
                    if clerlvl >= 8:
                        player.classnotes.append(f"Potent Spellcasting - You add your Wisdom modifier, or {player.WisMod}, to the damage you deal with any Cleric Cantrip.")
                    if clerlvl >= 17:
                        player.classnotes.append("Expansive Bond (see notes)")      
                        player.notes.append("Expansive Bond - The benefits of your Emboldening Bond and Protective Bond features now work when the creatures are within 60 feet of each other. Moreover, when a creature uses Protective Bond to take someone else's damage, the creature has resistance to that damage.")                                             
                if player.subclass[i] == "Tempest Domain Cleric":
                    ClericTempestDomainSpells = []
                    if clerlvl >= 1:
                        ClericTempestDomainSpells.append("Fog Cloud")
                        ClericTempestDomainSpells.append("Thunderwave")
                    if clerlvl >= 3:
                        ClericTempestDomainSpells.append("Gust of Wind")
                        ClericTempestDomainSpells.append("Shatter")
                    if clerlvl >= 5:
                        ClericTempestDomainSpells.append("Call Lightning")
                        ClericTempestDomainSpells.append("Sleet Storm")
                    if clerlvl >= 7:
                        ClericTempestDomainSpells.append("Control Water")
                        ClericTempestDomainSpells.append("Ice Storm")
                    if clerlvl >= 9:
                        ClericTempestDomainSpells.append("Destructive Wave")
                        ClericTempestDomainSpells.append("Insect Plague") 
                    clericdomain_str = ", ".join(f"{spell}" for spell in ClericTempestDomainSpells) 
                    player.classnotes.append("Domain Spells (see notes)")
                    player.notes.append(f"Domain Spells - Each domain has a list of spells — its domain spells — that you gain certain Cleric levels. Currently your Domain Spells are: {clericdomain_str}. Once you gain a domain spell, you always have it prepared, and it doesn’t count against the number of spells you can prepare each day.\nIf you have a domain spell that doesn’t appear on the cleric spell list, the spell is nonetheless a cleric spell for you.")                       
                    profs = ["Heavy Armor", "Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    player.classnotes.append("Wrath of the Storm (see notes)")
                    player.notes.append(f"Wrath of the Storm - You can thunderously rebuke attackers. When a creature within 5 feet of you that you can see hits you with an attack, you can use your reaction to cause the creature to make a Dexterity saving throw. The creature takes 2d8 lightning or thunder damage (your choice) on a failed saving throw, and half as much damage on a successful one.\nYou can use this featurea number of times equal to your Wisdom modifier, or {player.WisMod} times, a minimum of once. You regain all expended uses when you finish a long rest.")
                    if clerlvl >= 2:
                        player.classnotes.append("Channel Divinity: Destructive Wrath - You can use your Channel Divinity to wield the power of the storm with unchecked ferocity.\nWhen you roll lightning or thunder damage, you can use your Channel Divinity to deal maximum damage, instead of rolling.")
                    if clerlvl >= 6:
                        player.classnotes.append("Thunderous Strike - When you deal lightning damage to a Large or smaller creature, you can also push it up to 10 feet away from you.")
                    if clerlvl >= 8:
                        ClericDivineStrike = "1d8"
                        if clerlvl >= 14:
                            ClericDivineStrike = "2d8"
                        player.classnotes.append(f"Divine Strike - You gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {ClericDivineStrike} thunder damage to the target.")
                    if clerlvl >= 17:
                        player.classnotes.append("Stormborn - You have a flying speed equal to your current walking speed whenever you are not underground or indoors.")                                          
                if player.subclass[i] == "Trickery Domain Cleric":
                    ClericTrickeryDomainSpells = []
                    if clerlvl >= 1:
                        ClericTrickeryDomainSpells.append("Charm Person")
                        ClericTrickeryDomainSpells.append("Disguise Self")
                    if clerlvl >= 3:
                        ClericTrickeryDomainSpells.append("Mirror Image")
                        ClericTrickeryDomainSpells.append("Pass without Trace")
                    if clerlvl >= 5:
                        ClericTrickeryDomainSpells.append("Blink")
                        ClericTrickeryDomainSpells.append("Dispel Magic")                        
                    if clerlvl >= 7:
                        ClericTrickeryDomainSpells.append("Dimension Door")
                        ClericTrickeryDomainSpells.append("Polymorph")
                    if clerlvl >= 9:
                        ClericTrickeryDomainSpells.append("Dominate Person")
                        ClericTrickeryDomainSpells.append("Modify Memory") 
                    clericdomain_str = ", ".join(f"{spell}" for spell in ClericTrickeryDomainSpells)   
                    player.classnotes.append("Domain Spells (see notes)")
                    player.notes.append(f"Domain Spells - Each domain has a list of spells — its domain spells — that you gain certain Cleric levels. Currently your Domain Spells are: {clericdomain_str}. Once you gain a domain spell, you always have it prepared, and it doesn’t count against the number of spells you can prepare each day.\nIf you have a domain spell that doesn’t appear on the cleric spell list, the spell is nonetheless a cleric spell for you.")                     
                    player.classnotes.append("Blessing of the Trickster - You can use your action to touch a willing creature other than yourself to give it advantage on Dexterity (Stealth) checks. This blessing lasts for 1 hour or until you use this feature again.")
                    if clerlvl >= 2:
                        player.classnotes.append("Channel Divinity: Invoke Duplicity (see notes)")
                        player.notes.append("Channel Divinity: Invoke Duplicity - You can use your Channel Divinity to create an illusory duplicate of yourself.\nAs an action, you create a perfect illusion of yourself that lasts for 1 minute, or until you lose your concentration (as if you were concentrating on a spell). The illusion appears in an unoccupied space that you can see within 30 feet of you. As a bonus action on your turn, you can move the illusion up to 30 feet to a space you can see, but it must remain within 120 feet of you.\nFor the duration, you can cast spells as though you were in the illusion's space, but you must use your own senses. Additionally, when both you and your illusion are within 5 feet of a creature that can see the illusion, you have advantage on attack rolls against that creature, given how distracting the illusion is to the target.")
                    if clerlvl >= 6:
                        player.classnotes.append("Channel Divinity: Cloak of Shadows - You can use your Channel Divinity to vanish.\nAs an action, you become invisible until the end of your next turn. You become visible if you attack or cast a spell.")
                    if clerlvl >= 8:
                        ClericDivineStrike = "1d8"
                        if clerlvl >= 14:
                            ClericDivineStrike = "2d8"
                        player.classnotes.append(f"Divine Strike - You gain the ability to infuse your weapon strikes with poison – a gift from your deity. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {ClericDivineStrike} poison damage to the target.")
                    if clerlvl >= 17:
                        player.classnotes.append("Improved Duplicity - You can create up to four duplicates of yourself, instead of one, when you use Invoke Duplicity. As a bonus action on your turn, you can move any number of them up to 30 feet, to a maximum range of 120 feet.")                       
                if player.subclass[i] == "Twilight Domain Cleric":
                    ClericTwilightDomainSpells = []
                    if clerlvl >= 1:
                        ClericTwilightDomainSpells.append("Faerie Fire")
                        ClericTwilightDomainSpells.append("Sleep")
                    if clerlvl >= 3:
                        ClericTwilightDomainSpells.append("Moonbeam")
                        ClericTwilightDomainSpells.append("See Invisibility")
                    if clerlvl >= 5:
                        ClericTwilightDomainSpells.append("Aura of Vitality")
                        ClericTwilightDomainSpells.append("Leomund's Tiny Hut")
                    if clerlvl >= 7:
                        ClericTwilightDomainSpells.append("Aura of Life")
                        ClericTwilightDomainSpells.append("Greater Invisibility")
                    if clerlvl >= 9:
                        ClericTwilightDomainSpells.append("Circle of Power")
                        ClericTwilightDomainSpells.append("Mislead") 
                    clericdomain_str = ", ".join(f"{spell}" for spell in ClericTwilightDomainSpells)     
                    player.classnotes.append("Domain Spells (see notes)")
                    player.notes.append(f"Domain Spells - Each domain has a list of spells — its domain spells — that you gain certain Cleric levels. Currently your Domain Spells are: {clericdomain_str}. Once you gain a domain spell, you always have it prepared, and it doesn’t count against the number of spells you can prepare each day.\nIf you have a domain spell that doesn’t appear on the cleric spell list, the spell is nonetheless a cleric spell for you.")                   
                    profs = ["Heavy Armor", "Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)                          
                    player.classnotes.append("Eyes of Night (see notes)")
                    player.notes.append(f"Eyes of Night - You can see through the deepest gloom. You have darkvision out to a range of 300 feet. In that radius, you can see in dim light as if it were bright light and in darkness as if it were dim light.\nAs an action, you can magically share the darkvision of this feature with willing creatures you can see within 10 feet of you, up to a number of creatures equal to your Wisdom modifier, or {player.WisMod} creatures, minimum of one creature. The shared darkvision lasts for 1 hour. Once you share it, you can't do so again until you finish a long rest, unless you expend a spell slot of any level to share it again.")
                    player.classnotes.append("Vigilant Blessing - The night has taught you to be vigilant. As an action, you give one creature you touch (including possibly yourself) advantage on the next initiative roll the creature makes. This benefit ends immediately after the roll or if you use this feature again.")
                    if clerlvl >= 2:
                        player.classnotes.append("Channel Divinity: Twilight Sanctuary (see notes)")
                        player.notes.append(f"Channel Divinity: Twilight Sanctuary - You can use your Channel Divinity to refresh your allies with soothing twilight.\nAs an action, you present your holy symbol, and a sphere of twilight emanates from you. The sphere is centered on you, has a 30-foot radius, and is filled with dim light. The sphere moves with you, and it lasts for 1 minute or until you are incapacitated or die. Whenever a creature (including you) ends its turn in the sphere, you can grant that creature one of these benefits:\n- You grant it temporary hit points equal to 1d6 plus your Cleric level, or {clerlvl} temporary hit points.\n- You end one effect on it causing it to be charmed or frightened.")
                    if clerlvl >= 6:
                        player.classnotes.append("Steps of Night (see notes)")
                        player.notes.append(f"Steps of Night - You can draw on the mystical power of night to rise into the air. As a bonus action when you are in dim light or darkness, you can magically give yourself a flying speed equal to your walking speed for 1 minute. You can use this bonus action a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
                    if clerlvl >= 8:
                        ClericDivineStrike = "1d8"
                        if clerlvl >= 14:
                            ClericDivineStrike = "2d8"
                        player.classnotes.append(f"Divine Strike - You gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {ClericDivineStrike} radiant damage.")
                    if clerlvl >= 17:
                        player.classnotes.append("Twilight Shroud - The twilight that you summon offers a protective embrace: you and your allies have half cover while in the sphere created by your Twilight Sanctuary.")                      
                if player.subclass[i] == "War Domain Cleric":
                    ClericWarDomainSpells = []
                    if clerlvl >= 1:
                        ClericWarDomainSpells.append("Divine Favor")
                        ClericWarDomainSpells.append("Shield of Faith")
                    if clerlvl >= 3:
                        ClericWarDomainSpells.append("Magic Weapon")
                        ClericWarDomainSpells.append("Spiritual Weapon")
                    if clerlvl >= 5:
                        ClericWarDomainSpells.append("Crusader's Mantle")
                        ClericWarDomainSpells.append("Spirit Guardians")
                    if clerlvl >= 7:
                        ClericWarDomainSpells.append("Freedom of Movement")
                        ClericWarDomainSpells.append("Stoneskin")
                    if clerlvl >= 9:
                        ClericWarDomainSpells.append("Flame Strike")
                        ClericWarDomainSpells.append("Hold Monster") 
                    clericdomain_str = ", ".join(f"{spell}" for spell in ClericWarDomainSpells)
                    player.classnotes.append("Domain Spells (see notes)")
                    player.notes.append(f"Domain Spells - Each domain has a list of spells — its domain spells — that you gain certain Cleric levels. Currently your Domain Spells are: {clericdomain_str}. Once you gain a domain spell, you always have it prepared, and it doesn’t count against the number of spells you can prepare each day.\nIf you have a domain spell that doesn’t appear on the cleric spell list, the spell is nonetheless a cleric spell for you.")                    
                    profs = ["Heavy Armor", "Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)                        
                    player.classnotes.append(f"War Preist - Your god delivers bolts of inspiration to you while you are engaged in battle. When you use the Attack action, you can make one weapon attack as a bonus action.\nYou can use this feature a number of times equal to your Wisdom modifier, or {player.WisMod} times, a minimum of once. You regain all expended uses when you finish a long rest.")
                    if clerlvl >= 2:
                        player.classnotes.append("Channel Divinity: Guided Strike (see notes)")
                        player.notes.append("Channel Divinity: Guided Strike - You can use your Channel Divinity to strike with supernatural accuracy. When you make an attack roll, you can use your Channel Divinity to gain a +10 bonus to the roll. You make this choice after you see the roll, but before the DM says whether the attack hits or misses.")
                    if clerlvl >= 6:
                        player.classnotes.append("Channel Divinity: War God's Blessing (see notes)")
                        player.notes.append("Channel Divinity: War God's Blessing - When a creature within 30 feet of you makes an attack roll, you can use your reaction to grant that creature a +10 bonus to the roll, using your Channel Divinity. You make this choice after you see the roll, but before the DM says whether the attack hits or misses.")
                    if clerlvl >= 8:
                        ClericDivineStrike = "1d8"
                        if clerlvl >= 14:
                            ClericDivineStrike = "2d8"
                        player.classnotes.append(f"Divine Strike - You gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {ClericDivineStrike} damage of the same type dealt by the weapon to the target.")
                    if clerlvl >= 17:
                        player.classnotes.append("Avatar of Battle - You gain resistance to bludgeoning, piercing, and slashing damage from nonmagical weapons.")                     
                ClericSpellSlot1 = 4
                ClericSpellSlot2 = 2
            if clerlvl >= 4:
                ClericCantripsKnown = 4
                ClericSpellSlot2 = 3
                player.classnotes.append("Cantrip Versatility (see notes)")
                player.notes.append("Cantrip Versatility - Whenever you reach a level in this class that grants the Ability Score Improvement feature, you can replace one cantrip you learned from this class's Spellcasting feature with another cantrip from the cleric spell list.")                
            if clerlvl >= 5:
                ClericSpellSlot3 = 2
                if ((clerlvl >= 5) and (clerlvl < 8)):
                    DestroyUndeadCR = "1/2 or lower"
                if ((clerlvl >= 8) and (clerlvl < 11)):
                    DestroyUndeadCR = "1 or lower"
                if ((clerlvl >= 11) and (clerlvl < 14)):
                    DestroyUndeadCR = "2 or lower"
                if ((clerlvl >= 14) and (clerlvl < 17)):
                    DestroyUndeadCR = "3 or lower"                    
                if clerlvl >= 17:
                    DestroyUndeadCR = "4 or lower"
                player.classnotes.append(f"Destroy Undead - When an undead fails its saving throw against your Turn Undead feature, the creature is instantly destroyed if its challenge rating is {DestroyUndeadCR}.")
            if clerlvl >= 6:
                ClericSpellSlot3 = 3
            if clerlvl >= 7:
                ClericSpellSlot4 = 1
            if clerlvl >= 8:
                ClericSpellSlot4 = 2
                player.classnotes.append("Blessed Strikes (see notes)")
                player.notes.append("Blessed Strikes - You are blessed with divine might in battle. When a creature takes damage from one of your cantrips or weapon attacks, you can also deal 1d8 radiant damage to that creature. Once you deal this damage, you can't use this feature again until the start of your next turn. If you have the Divine Strike or Potent Spellcasting Features, this replaces it.")
            if clerlvl >= 9:
                ClericSpellSlot4 = 3
                ClericSpellSlot5 = 1
            if clerlvl >= 10:
                ClericCantripsKnown = 5
                ClericSpellSlot5 = 2
                player.classnotes.append("Divine Intervention(1) (see notes)")
                player.notes.append(f"Divine Intervention(1) - You can call on your deity to intervene on your behalf when your need is great.\nImploring your deity’s aid requires you to use your action. Describe the assistance you seek, and roll percentile dice. If you roll a number equal to or lower than your Cleric level, or lower than {clerlvl}, your deity intervenes. The DM chooses the nature of the intervention; the effect of any cleric spell or cleric domain spell would be appropriate.\nIf your deity intervenes, you can’t use this feature again for 7 days. Otherwise, you can use it again after you finish a long rest.")
            if clerlvl >= 11:
                ClericSpellSlot6 = 1
            if clerlvl >= 13:
                ClericSpellSlot7 = 1
            if clerlvl >= 15:
                ClericSpellSlot8 = 1
            if clerlvl >= 17:
                ClericSpellSlot9 = 1
            if clerlvl >= 18:
                ClericSpellSlot5 = 3
            if clerlvl >= 19:
                ClericSpellSlot6 = 2
            if clerlvl == 20:
                ClericSpellSlot7 = 2
                player.classnotes.append("Divine Intervention(2) (see notes)")
                player.notes.append("Divine Intervention(2) - Your call for intervention succeeds automatically, no roll required.")
            player.notes.append(f"You have {ClericCantripsKnown} cantrips available to you.")
            player.notes.append(f"The number of first level spell slots you have as a Cleric is: {ClericSpellSlot1}.")
            if ClericSpellSlot2 != 0:
                player.notes.append(f"The number of second level spell slots you have as a Cleric is: {ClericSpellSlot2}.")
            if ClericSpellSlot3 != 0:                
                player.notes.append(f"The number of third level spell slots you have as a Cleric is: {ClericSpellSlot3}.")
            if ClericSpellSlot4 != 0:
                player.notes.append(f"The number of fourth level spell slots you have as a Cleric is: {ClericSpellSlot4}.")
            if ClericSpellSlot5 != 0:
                player.notes.append(f"The number of fifth level spell slots you have as a Cleric is: {ClericSpellSlot5}.")
            if ClericSpellSlot6 != 0:
                player.notes.append(f"The number of sixth level spell slots you have as a Cleric is: {ClericSpellSlot6}.")
            if ClericSpellSlot7 != 0:
                player.notes.append(f"The number of seventh level spell slots you have as a Cleric is: {ClericSpellSlot7}.")
            if ClericSpellSlot8 != 0:
                player.notes.append(f"The number of eighth level spell slots you have as a Cleric is: {ClericSpellSlot8}.")
            if ClericSpellSlot9 != 0:
                player.notes.append(f"The number of ninth level spell slots you have as a Cleric is: {ClericSpellSlot9}.")  
            if clerlvl >= 2:      
                ChannelDivinity = 1
                player.classnotes.append("Channel Divinity (see notes)")
                if ((clerlvl >= 6) and (clerlvl < 18)):
                    ChannelDivinity = 2
                if clerlvl >= 18:
                    ChannelDivinity = 3
                player.notes.append(f"Channel Divinity - You gain the ability to channel divine energy directly from your deity, using that energy to fuel magical effects. You start with two such effects: Turn Undead and an effect determined by your domain. Some domains grant you additional effects as you advance in levels, as noted in the domain description.When you use your Channel Divinity, you choose which effect to create. You must then finish a short or long rest to use your Channel Divinity again.\nSome Channel Divinity effects require saving throws. When you use such an effect from this class, the DC equals your cleric spell save DC, or against {player.spellsavedc[i]}.\nYou can use Channel Divinity {ChannelDivinity} times between rests. When you finish a short or long rest, you regain your expended uses.")                                                   
                player.notes.append("Channel Divinity: Turn Undead - As an action, you present your holy symbol and speak a prayer censuring the undead. Each undead that can see or hear you within 30 feet of you must make a Wisdom saving throw. If the creature fails its saving throw, it is turned for 1 minute or until it takes any damage.\nA turned creature must spend its turns trying to move as far away from you as it can, and it can’t willingly move to a space within 30 feet of you. It also can’t take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there’s nowhere to move, the creature can use the Dodge action.")
                player.notes.append(f"Channel Divinity: Harness Divine Power - You can expend a use of your Channel Divinity to fuel your spells. As a bonus action, you touch your holy symbol, utter a prayer, and regain one expended spell slot, the level of which can be half your Proficiency Bonus, rounded up, or level of {math.ceil(player.profbonus/2)}.")                              
        if player.Class[i] == "Druid":
            if ((param == "N") or (player.singlemulticlass == "N")):
                drulvl = player.level
                player.classlvl.append(drulvl) 
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    drulvl = int(input(f"Given your pool of levels of {poollevel}, what is your Druid level? "))      
                    if drulvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                
                poollevel = poollevel - drulvl
                player.classlvl.append(drulvl)
            if drulvl >= 1:
                player.hitdice.append(f"{drulvl}d8 for {player.Class[i]}")
                if drulvl == 1:
                    player.hitpoints += (8 + player.ConMod)
                else:
                    player.hitpoints += (8 + player.ConMod + hpcalc(drulvl, dice, 8))  
                if i == 0:
                    profs = ["Light Armor", "Medium Armor", "Shield"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    player.classnotes.append("Druids will not wear armor or use shields made of metal")
                    firstprofs = [
                        dnd_tools.simple_weapons["Club"]["Name"],
                        dnd_tools.simple_weapons["Dagger"]["Name"],
                        dnd_tools.simple_weapons["Dart"]["Name"],
                        dnd_tools.simple_weapons["Javelin"]["Name"],
                        dnd_tools.simple_weapons["Mace"]["Name"],
                        dnd_tools.simple_weapons["Quarterstaff"]["Name"],
                        dnd_tools.martial_weapons["Scimitar"]["Name"],
                        dnd_tools.simple_weapons["Sickle"]["Name"],
                        dnd_tools.simple_weapons["Sling"]["Name"],
                        dnd_tools.simple_weapons["Spear"]["Name"],
                        dnd_tools.kits["HerbKit"]["Name"]      
                        ]    
                    for fprof in firstprofs:
                        if fprof not in player.proficiencies:
                            player.proficiencies.append(fprof)
                    player.skills.append(dnd_tools.saving_throws["WisST"])
                    player.skills.append(dnd_tools.saving_throws["IntST"])
                    SkillsList = [
                        dnd_tools.skills["Arcana"], 
                        dnd_tools.skills["AnimalHandling"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Medicine"], 
                        dnd_tools.skills["Nature"], 
                        dnd_tools.skills["Perception"], 
                        dnd_tools.skills["Religion"], 
                        dnd_tools.skills["Survival"]
                        ]
                    player.skills = twoskillsfromlist(param, player.skills, SkillsList)  
                    StartEquip1 = ["Wooden Shield", "Any Simple Weapon"]
                    StartEquip2 = ["Scimitar", "Any Simple Melee Weapon"]
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Wooden Shield")
                        print("2 - Any Simple Weapon")
                        se1 = int(input("What would you like your first choice for starting equipment to be? "))
                        if se1 == 0:
                            SE1rand = random.choice(StartEquip1)
                            if SE1rand == "Wooden Shield":
                                player.equipment.append(dnd_tools.shields["Wooden Shield"].copy())
                            if SE1rand == "Any Simple Weapon":
                                SimpRandKey = random.choice(SimpleWeapons)
                                player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                        if se1 == 1:
                            player.equipment.append(dnd_tools.shields["Wooden Shield"].copy())
                        if se1 == 2:
                            print("0 - Random")
                            for j, sw in enumerate(SimpleWeaponsNames, 1):
                                print(f"{j} - {sw}")
                            se1sw = int(input("Which simple weapon would you like to add to your inventory? "))
                            if se1sw == 0:
                                SimpRandKey = random.choice(SimpleWeapons)
                                player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                            elif 1 <= se1sw <= len(SimpleWeapons):
                                SimpKey = SimpleWeapons[se1sw-1]
                                player.equipment.append(dnd_tools.simple_weapons[SimpKey].copy()) 
                        print("0 - Random")
                        print("1 - Scimitar")
                        print("2 - Any Simple Melee Weapon")
                        se2 = int(input("What would you like your second choice for starting equipment to be? "))
                        if se2 == 0:
                            SE2rand = random.choice(StartEquip2)
                            if SE2rand == "Scimitar":
                                 player.equipment.append(dnd_tools.martial_weapons["Scimitar"].copy())
                            if SE2rand == "Any Simple Melee Weapon":
                                SimpRandMKey = random.choice(SimpleMeleeWeapons)
                                player.equipment.append(dnd_tools.simple_weapons[SimpRandMKey].copy())
                        if se2 == 1:
                             player.equipment.append(dnd_tools.martial_weapons["Scimitar"].copy())
                        if se2 == 2:
                            print("0 - Random")
                            for j, smw in enumerate(SimpleMeleeWeaponsNames, 1):
                                print(f"{j} - {smw}")
                            se2smw = int(input("Which simple melee weapon would you like to add to your inventory? "))
                            if se2smw == 0:
                                SimpRandMKey = random.choice(SimpleMeleeWeapons)
                                player.equipment.append(dnd_tools.simple_weapons[SimpRandMKey].copy())
                            elif 1 <= se2smw <= len(SimpleMeleeWeaponsNames):
                                SimpMKey = SimpleMeleeWeapons[se2sw-1]
                                player.equipment.append(dnd_tools.simple_weapons[SimpMKey].copy()) 
                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])
                        player.equipment.append("Druidic Focus")
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "Wooden Shield":
                            player.equipment.append(dnd_tools.shields["Wooden Shield"].copy())
                        if SE1rand == "Any Simple Weapon":
                            SimpRandKey = random.choice(SimpleWeapons)
                            player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "Scimitar":
                             player.equipment.append(dnd_tools.martial_weapons["Scimitar"].copy())
                        if SE2rand == "Any Simple Melee Weapon":
                            SimpRandMKey = random.choice(SimpleMeleeWeapons)
                            player.equipment.append(dnd_tools.simple_weapons[SimpRandMKey].copy())
                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])
                        player.equipment.append("Druidic Focus")
                else:
                    profs = ["Light Armor", "Medium Armor", "Shield"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)   
                player.spellcastingclass.append("Druid")
                player.spellcastingability.append("Wis")
                player.spellsavedc.append(8 + player.profbonus + player.WisMod)
                player.spellattackmod.append(player.profbonus + player.WisMod)
                DruidCantripsKnown = 2
                DruidSpellSlot1 = 2
                DruidSpellSlot2 = 0
                DruidSpellSlot3 = 0
                DruidSpellSlot4 = 0
                DruidSpellSlot5 = 0
                DruidSpellSlot6 = 0
                DruidSpellSlot7 = 0
                DruidSpellSlot8 = 0
                DruidSpellSlot9 = 0   
            player.classnotes.append("Druidic (see notes)")
            player.notes.append("Druidic - You know Druidic, the secret language of druids. You can speak the language and use it to leave hidden messages. You and others who know this language automatically spot such a message. Others spot the message’s presence with a successful DC 15 Wisdom (Perception) check but can’t decipher it without magic.")
            if drulvl >= 2: 
                DruidSpellSlot1 = 3 
                player.classnotes.append("Wild Shape (see notes)")
                player.classnotes.append("Wild Companion (see notes)")
                WildShapeCR = "1/4"
                WildShapeLimitations = "No flying or swimming speed"
                if ((drulvl >= 4) and (drulvl < 8)):
                    WildShapeCR = "1/2"
                    WildShapeLimitations = "No Flying Speed"
                if ((drulvl >= 8)):
                    WildShapeCR = "1"
                    WildShapeLimitations = "No Limitations"
                player.notes.append(f"Wild Shape - You can use your action to magically assume the shape of a beast that you have seen before. You can use this feature twice. You regain expended uses when you finish a short or long rest.\nYour Druid level determines the beasts you can transform into, the Max CR is {WildShapeCR} and the Limitations on it, if any, are {WildShapeLimitations}.\nYou can stay in a beast shape for a number of hours equal to half your Druid level (rounded down), or {math.floor(drulvl/2)} hourd. You then revert to your normal form unless you expend another use of this feature. You can revert to your normal form earlier by using a bonus action on your turn. You automatically revert if you fall unconscious, drop to 0 hit points, or die.\nWhile you are transformed, the following rules apply:\nYour game statistics are replaced by the statistics of the beast, but you retain your alignment, personality, and Intelligence, Wisdom, and Charisma scores. You also retain all of your skill and saving throw proficiencies, in addition to gaining those of the creature. If the creature has the same proficiency as you and the bonus in its stat block is higher than yours, use the creature’s bonus instead of yours. If the creature has any legendary or lair actions, you can’t use them.\n- When you transform, you assume the beast’s hit points and Hit Dice. When you revert to your normal form, you return to the number of hit points you had before you transformed. However, if you revert as a result of dropping to 0 hit points, any excess damage carries over to your normal form. For example, if you take 10 damage in animal form and have only 1 hit point left, you revert and take 9 damage. As long as the excess damage doesn’t reduce your normal form to 0 hit points, you aren’t knocked unconscious.\n- You can’t cast spells, and your ability to speak or take any action that requires hands is limited * to the capabilities of your beast form. Transforming doesn’t break your concentration on a spell you’ve already cast, however, or prevent you from taking actions that are part of a spell, such as call lightning, that you’ve already cast.\n- You retain the benefit of any features from your class, race, or other source and can use them if the new form is physically capable of doing so. However, you can’t use any of your special senses, such as darkvision, unless your new form also has that sense.\n- You choose whether your equipment falls to the ground in your space, merges into your new form, or is worn by it. Worn equipment functions as normal, but the DM decides whether it is practical for the new form to wear a piece of equipment, based on the creature’s shape and size. Your equipment doesn’t change size or shape to match the new form, and any equipment that the new form can’t wear must either fall to the ground or merge with it. Equipment that merges with the form has no effect until you leave the form.")
                player.notes.append(f"Wild Companion - You gain the ability to summon a spirit that assumes an animal form: as an action, you can expend a use of your Wild Shape feature to cast the Find Familiar spell, without material components.\nWhen you cast the spell in this way, the familiar is a fey instead of a beast, and the familiar disappears after a number of hours equal to half your Druid level, rounded down, or {math.floor(drulvl / 2)} hours. This beast follows the same rules as Wild Shape, in that the Max CR is {WildShapeCR} and if it is limited, it is limited by {WildShapeLimitations}.")
            if drulvl >= 2:
                Dru = ["Circle of the Blighted Druid", "Circle of Dreams Druid", "Circle of the Land Druid", "Circle of the Moon Druid", "Circle of the Sheppard Druid", "Circle of Spores Druid", "Circle of the Stars Druid", "Circle of Wildfire Druid"]  
                

                if player.subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        for idx, subcl in enumerate(Dru, 1):
                            print(f"{idx} - {subcl}")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 0:
                            player.subclass[i] = random.choice(Dru)
                        elif 1 <= subc <= len(Dru):
                            player.subclass[i] = Dru[subc - 1]
                    if param == "N":
                        player.subclass[i] = random.choice(Dru)                                   
                if player.subclass[i] == "Circle of the Blighted Druid":
                    player.classnotes.append("Defile Ground(1) (see notes)")
                    player.notes.append("Defile Ground(1) - You can use a bonus action to corrupt a patch of land or an area of water in a 10-foot radius centered on a point within 60 feet of you. This corruption lasts for 1 minute. The corrupted area is difficult terrain for creatures that are hostile to you. Additionally, when a creature in the area takes damage from an attack or spell for the first time on a turn, it takes an extra 1d4 necrotic damage. You can move this patch of corruption up to 30 feet as a bonus action. Flying creatures are unaffected by the corruption.\nOnce you use this feature, you can’t use it again until you finish a short or long rest.")
                    player.classnotes.append("Blighted Shape (see notes)")
                    player.notes.append("Blighted Shape - Your physical form begins to show effects of the corruption you wield, tracing blackened veins across your skin, producing gnarled, bony protrusions, or other eerie phenomena. You gain proficiency in the Charisma (Intimidation) skill.\nAdditionally, while you are transformed by your Wild Shape feature, you gain a +2 bonus to AC as gnarled spines protrude from your body. Your beast form also gains darkvision with a radius of 60 feet, or an additional 60 feet of darkvision if it already has that sense.")                    
                    if drulvl >= 6:
                        player.classnotes.append("Call of the Shadowseeds (see notes)")
                        player.notes.append(f"Call of the Shadowseeds - You learn to summon the feral children of the forest from the life force of your enemies. When a creature that is not undead or a construct takes damage within the area of your Defile Ground feature, you can use your reaction to summon a blighted sapling in an unoccupied space within 5 feet of the creature. You can direct the sapling to make an attack against any creature within 5 feet of it as a part of this reaction. The sapling then acts on your initiative, obeying your verbal commands.\nThe blighted sapling remains in your service until it's reduced to 0 hit points, until the end of your next long rest, or until you summon another sapling, at which point it crumbles into foul-smelling mulch. You can use this feature a number of times equal to your Proficiency Bonus, or {player.profbonus} times, regaining all expended uses when you finish a long rest.\nThe stats for this sapling are available in the 'Tal'Dorei Campaign Setting Reborn' sourcebook.")
                    if drulvl >= 10:
                        DefileGroundDmg = "1d6"
                        if ((drulvl >= 10) and (drulvl < 14)):
                            DefileGroundDmg = "1d8"
                        player.classnotes.append("Defile Ground(2) (see notes)")
                        player.notes.append(f"Defile Ground(2) - The area of your defiled ground increases to a 20-foot radius. Additionally, the extra damage dealt by your defiled ground increases to {DefileGroundDmg}.\nOnce you use this feature, you can’t use it again until you finish a short or long rest.")
                        player.classnotes.append("Foul Conjuration (see notes)")
                        player.notes.append(f"Foul Conjuration - The creatures you conjure are malformed and bloated with toxins. Any beast, fey, or plant (including your blighted sapling) summoned or created by your spells or class features gains the following traits:\nBlighted Resilience. The creature has immunity to necrotic and poison damage and to the poisoned condition.\nToxic Demise - When the creature is reduced to 0 hit points, it explodes in a burst of toxic mulch or fetid viscera. Each creature within 5 feet of the exploding creature must succeed on a Constitution saving throw against your spell save DC, or against {player.spellsavedc[i]}, or take necrotic damage based on the creature's challenge rating (see the attatched note for Toxic Demise Damage). As an action, you can also cause a summoned creature to explode, immediately killing it.")
                        player.notes.append(f"Toxic Demise Damage - if the CR of the Creature is 1/4 or lower, the damage is 1d4 necrotic damage.\nIf the CR is 1/2, the damage is 1d6 necrotic damage.\nIf the CR is 1 or higher, the damage is a number of d8s of necrotic damage equal to the creature's challenge rating.\nIf there is no challenge rating, the damage is a number of d6s of necrotic damage equal to your Proficiency Bonus, or {player.profbonus}d6.")
                    if drulvl >= 14:
                        player.classnotes.append("Incarnation of Corruption (see notes)")
                        player.notes.append(f"Incarnation of Corruption - Your physical form begins to take on the tainted traits of the land you are bonded to. Your skin grows ashen, and your eyes darken or turn completely white. Spines and jagged spurs emerge from your body, granting you resistance to necrotic damage and a +2 bonus to AC.\nAdditionally, whenever you start your turn within the radius of the corruption created by your Defile Ground feature, you can use a bonus action to gain temporary hit points equal to your Proficiency Bonus, or {player.profbonus} temporary hit points.")
                if player.subclass[i] == "Circle of Dreams Druid":
                    player.classnotes.append("Balm of the Summer Court (see notes)")
                    player.notes.append(f"Balm of the Summer Court - You become imbued with the blessings of the Summer Court. You are a font of energy that offers respite from injuries. You have a pool of fey energy represented by a number of d6s equal to your Druid level, or {drulvl}d6.\nAs a bonus action, you can choose an ally you can see within 120 feet of you and spend a number of those dice equal to half your Druid level, or {math.ceil(drulvl/2)} dice, or less. Roll the spent dice and add them together. The target regains a number of hit points equal to the total. The target also gains 1 temporary hit point per die spent.\nYou regain the expended dice when you finish a long rest.")
                    if drulvl >= 6:
                        player.classnotes.append("Hearth of Moonlight and Shadow (see notes)")
                        player.notes.append("Hearth of Moonlight and Shadow - Home can be wherever you are. During a short or long rest, you can invoke the shadowy power of the Gloaming Court to help guard your respite. At the start of the rest, you touch a point in space, and an invisible, 30-foot-radius sphere of magic appears, centered on that point. Total cover blocks the sphere.\nWhile within the sphere, you and your allies gain a +5 bonus to Dexterity (Stealth) and Wisdom (Perception) checks, and any light from open flames in the sphere (a campfire, torches, or the like) isn't visible outside it.\nThe sphere vanishes at the end of the rest or when you leave the sphere.")
                    if drulvl >= 10:
                        player.classnotes.append("Hidden Paths (see notes)")
                        player.notes.append(f"Hidden Paths - You can use the hidden, magical pathways that some fey use to traverse space in a blink of an eye. As a bonus action on your turn, you can teleport up to 60 feet to an unoccupied space you can see. Alternatively, you can use your action to teleport one willing creature you touch up to 30 feet to an unoccupied space you can see.\nYou can use this feature a number of times equal to your Wisdom modifier, or {player.WisMod} times, a minimum of once; and you regain all expended uses of it when you finish a long rest.")
                    if drulvl >= 14:
                        player.classnotes.append("Walker in Dreams (see notes)")
                        player.notes.append("Walker in Dreams - The magic of the Feywild grants you the ability to travel mentally or physically through dreamlands.\nWhen you finish a short rest, you can cast one of the following spells, without expending a spell slot or requiring material components: Dream (with you as the messenger), Scrying, or Teleportation Circle.\nThis use of Teleportation Circle is special. Rather than opening a portal to a permanent teleportation circle, it opens a portal to the last location where you finished a long rest on your current plane of existence. If you haven't taken a long rest on your current plane, the spell fails but isn't wasted.\nOnce you use this feature, you can't use it again until you finish a long rest.")
                if player.subclass[i] == "Circle of the Land Druid":
                    DruidCircleLandsSpells = []
                    Land = ["Arctic", "Coast", "Desert", "Forest", "Grassland", "Mountain", "Swamp", "Underdark"]
                    if param == "Y":
                        print("0 - Random")
                        for i, land in enumerate(Land, 1):
                            print(f"{i} - {land}")
                        landinput = int(input("Choose a land to connect with, it will influence your choice of Circle Spells. "))
                        if landinput == 0:
                            LandChoice = random.choice(Land)
                        elif 1 <= landinput <= len(Land):
                            LandChoice = Land[landinput-1] 
                    if param == "N":
                        LandChoice = random.choice(Land)
                    if LandChoice == "Arctic":
                        if drulvl >= 3:
                            DruidCircleLandsSpells.append("Hold Person")
                            DruidCircleLandsSpells.append("Spike Growth")
                        if drulvl >= 5:
                            DruidCircleLandsSpells.append("Sleet Storm")
                            DruidCircleLandsSpells.append("Slow")
                        if drulvl >= 7:
                            DruidCircleLandsSpells.append("Freedom of Movement")
                            DruidCircleLandsSpells.append("Ice Storm")
                        if drulvl >= 9:
                            DruidCircleLandsSpells.append("Commune with Nature")
                            DruidCircleLandsSpells.append("Cone of Cold")                          
                    if LandChoice == "Coast":
                        if drulvl >= 3:
                            DruidCircleLandsSpells.append("Mirror Image")
                            DruidCircleLandsSpells.append("Misty Step")
                        if drulvl >= 5:
                            DruidCircleLandsSpells.append("Water Breathing")
                            DruidCircleLandsSpells.append("Water Walk")
                        if drulvl >= 7:
                            DruidCircleLandsSpells.append("Control Water")
                            DruidCircleLandsSpells.append("Freedom of Movement")
                        if drulvl >= 9:
                            DruidCircleLandsSpells.append("Conjure Elemental")
                            DruidCircleLandsSpells.append("Scrying")                               
                    if LandChoice == "Desert":
                        if drulvl >= 3:
                            DruidCircleLandsSpells.append("Blur")
                            DruidCircleLandsSpells.append("Silence")
                        if drulvl >= 5:
                            DruidCircleLandsSpells.append("Create Food and Water")
                            DruidCircleLandsSpells.append("Protection from Energy")
                        if drulvl >= 7:
                            DruidCircleLandsSpells.append("Blight")
                            DruidCircleLandsSpells.append("Hallucinatory Terrain")
                        if drulvl >= 9:
                            DruidCircleLandsSpells.append("Insect Plague")
                            DruidCircleLandsSpells.append("Wall of Stone")                               
                    if LandChoice == "Forest":                    
                        if drulvl >= 3:
                            DruidCircleLandsSpells.append("Barkskin")
                            DruidCircleLandsSpells.append("Spider Climb")
                        if drulvl >= 5:
                            DruidCircleLandsSpells.append("Call Lightning")
                            DruidCircleLandsSpells.append("Plant Growth")
                        if drulvl >= 7:
                            DruidCircleLandsSpells.append("Divination")
                            DruidCircleLandsSpells.append("Freedom of Movement")
                        if drulvl >= 9:
                            DruidCircleLandsSpells.append("Commune with Nature")
                            DruidCircleLandsSpells.append("Tree Stride")                           
                    if LandChoice == "Grassland":
                        if drulvl >= 3:
                            DruidCircleLandsSpells.append("Invisibility")
                            DruidCircleLandsSpells.append("Pass Without Trace")
                        if drulvl >= 5:
                            DruidCircleLandsSpells.append("Daylight")
                            DruidCircleLandsSpells.append("Haste")
                        if drulvl >= 7:
                            DruidCircleLandsSpells.append("Divination")
                            DruidCircleLandsSpells.append("Freedom of Movement")
                        if drulvl >= 9:
                            DruidCircleLandsSpells.append("Dream")
                            DruidCircleLandsSpells.append("Insect Plague")                             
                    if LandChoice == "Mountain":
                        if drulvl >= 3:
                            DruidCircleLandsSpells.append("Spider Climb")
                            DruidCircleLandsSpells.append("Spike Growth")
                        if drulvl >= 5:
                            DruidCircleLandsSpells.append("Lightning Bolt")
                            DruidCircleLandsSpells.append("Meld into Stone")
                        if drulvl >= 7:
                            DruidCircleLandsSpells.append("Stone Shape")
                            DruidCircleLandsSpells.append("Stoneskin")
                        if drulvl >= 9:
                            DruidCircleLandsSpells.append("Passwall")
                            DruidCircleLandsSpells.append("Wall of Stone")                             
                    if LandChoice == "Swamp":
                        if drulvl >= 3:
                            DruidCircleLandsSpells.append("Darkness")
                            DruidCircleLandsSpells.append("Melf's Acid Arrow")
                        if drulvl >= 5:
                            DruidCircleLandsSpells.append("Water Walk")
                            DruidCircleLandsSpells.append("Stinking Cloud")
                        if drulvl >= 7:
                            DruidCircleLandsSpells.append("Freedom of Movement")
                            DruidCircleLandsSpells.append("Locate Creature")
                        if drulvl >= 9:
                            DruidCircleLandsSpells.append("Insect Plague")
                            DruidCircleLandsSpells.append("Scrying")                                             
                    if LandChoice == "Underdark":
                        if drulvl >= 3:
                            DruidCircleLandsSpells.append("Spider Climb")
                            DruidCircleLandsSpells.append("Web")                            
                        if drulvl >= 5:
                            DruidCircleLandsSpells.append("Gaseous Form")
                            DruidCircleLandsSpells.append("Stinking Cloud")                            
                        if drulvl >= 7:
                            DruidCircleLandsSpells.append("Greater Invisibility")
                            DruidCircleLandsSpells.append("Stone Shape")                            
                        if drulvl >= 9:  
                            DruidCircleLandsSpells.append("Cloudkill")
                            DruidCircleLandsSpells.append("Insect Plague")                                                  
                    player.classnotes.append("Bonus Cantrip - You learn one additional druid cantrip of your choice.")
                    player.classnotes.append("Natural Recovery (see notes)")
                    player.notes.append(f"Natural Recovery - You can regain some of your magical energy by sitting in meditation and communing with nature. During a short rest, you choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your Druid level (rounded up) or {math.ceil(drulvl/2)}, and none of the slots can be 6th level or higher. You can't use this feature again until you finish a long rest.\nFor example, when you are a 4th-level druid, you can recover up to two levels worth of spell slots. You can recover either a 2nd-level slot or two 1st-level slots.")
                    druid_circle_spells = ", ".join(f"{spell}" for spell in DruidCircleLandsSpells)
                    player.classnotes.append("Circle Spells (see notes)")
                    player.notes.append(f"Circle Spells - Your mystical connection to the land infuses you with the ability to cast certain spells. You gain access to different spells based on your Druid Proficiency Bonus and your spells acquired change based on the land you chose. Your current list of spells are: {druid_circle_spells}\nOnce you gain access to a circle spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you gain access to a spell that doesn't appear on the druid spell list, the spell is nonetheless a druid spell for you.")
                    if drulvl >= 6:
                        player.classnotes.append("Land's Stride (see notes)")
                        player.notes.append("Land's Stride - Moving through nonmagical difficult terrain costs you no extra movement. You can also pass through nonmagical plants without being slowed by them and without taking damage from them if they have thorns, spines, or a similar hazard.\nIn addition, you have advantage on saving throws against plants that are magically created or manipulated to impede movement, such as those created by the Entangle spell.")
                    if drulvl >= 10:
                        player.classnotes.append("Nature's Ward - You can't be charmed or frightened by elementals or fey, and you are immune to poison and disease.")
                    if drulvl >= 14:
                        player.classnotes.append("Nature's Sanctuary (see notes)")
                        player.notes.append(f"Nature's Sanctuary - Creatures of the natural world sense your connection to nature and become hesitant to attack you. When a beast or plant creature attacks you, that creature must make a Wisdom saving throw against your druid spell save DC, or against {player.spellsavedc[i]}. On a failed save, the creature must choose a different target, or the attack automatically misses. On a successful save, the creature is immune to this effect for 24 hours.\nThe creature is aware of this effect before it makes its attack against you.")
                if player.subclass[i] == "Circle of the Moon Druid":
                    player.classnotes.append("Combat Wild Shape - You gain the ability to use Wild Shape on your turn as a bonus action, rather than as an action.\nAdditionally, while you are transformed by Wild Shape, you can use a bonus action to expend one spell slot to regain 1d8 hit points per level of the spell slot expended.")
                    player.classnotes.append("Circle Forms(1) - The rites of your circle grant you the ability to transform into more dangerous animal forms. You can use your Wild Shape to transform into a beast with a challenge rating as high as 1. You ignore the Max. CR column of the Beast Shapes table, but must abide by the other limitations there.")
                    if drulvl >= 6:
                        player.classnotes.append("Circle Forms(2) - You can transform into a beast with a challenge rating as high as your Druid level divided by 3, rounded down.")
                        player.classnotes.append("Primal Strike - Your attacks in beast form count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage.")
                    if drulvl >= 10:
                        player.classnotes.append("Elemental Wild Shape - You can expend two uses of Wild Shape at the same time to transform into an Air Elemental, an Earth Elemental, a Fire Elemental, or a Water Elemental.")
                    if drulvl >= 14:
                        player.classnotes.append("Thousand Forms - You have learned to use magic to alter your physical form in more subtle ways. You can cast the Alter Self spell at will.")
                if player.subclass[i] == "Circle of the Sheppard Druid":
                    if dnd_tools.languages["Sylv"] not in player.languages:
                        player.languages.append(dnd_tools.languages["Sylv"])
                    player.classnotes.append("Speech of the Woods (see notes)")
                    player.notes.append("Speech of the Woods - You gain the ability to converse with beasts and many fey.\nBeasts can understand your speech, and you gain the ability to decipher their noises and motions. Most beasts lack the intelligence to convey or understand sophisticated concepts, but a friendly beast could relay what it has seen or heard in the recent past. This ability doesn’t grant you any special friendship with beasts, though you can combine this ability with gifts to curry favor with them as you would with any nonplayer character.")
                    player.classnotes.append("Spirit Totem (see notes)")
                    player.notes.append(f"Spirit Totem - You gain the ability to call forth nature spirits and use them to influence the world around you.\nAs a bonus action, you can magically summon an incorporeal spirit to a point you can see within 60 feet of you. The spirit creates an aura in a 30-foot radius around that point. It counts as neither a creature nor an object, though it has the spectral appearance of the creature it represents. As a bonus action, you can move the spirit up to 60 feet to a point you can see.\nThe spirit persists for 1 minute. Once you use this feature, you can’t use it again until you finish a short or long rest.\nThe effect of the spirit’s aura depends on the type of spirit you summon from the options below.\nBear Spirit - The bear spirit grants you and your allies its might and endurance. Each creature of your choice in the aura when the spirit appears gains temporary hit points equal to 5 + your Druid level, or {5 + drulvl} temporary hit points. In addition, you and your allies gain advantage on Strength checks and Strength saving throws while in the aura.\nHawk Spirit - The hawk spirit is a consummate hunter, aiding you and your allies with its keen sight. When a creature makes an attack roll against a target in the spirit’s aura, you can use your reaction to grant advantage to that attack roll. In addition, you and your allies have advantage on Wisdom (Perception) checks while in the aura.\nUnicorn Spirit - The unicorn spirit lends its protection to those nearby. You and your allies gain advantage on all ability checks made to detect creatures in the spirit’s aura. In addition, if you cast a spell using a spell slot that restores hit points to any creature inside or outside the aura, each creature of your choice in the aura also regains hit points equal to your Druid level, or {drulvl} hit points.")
                    if drulvl >= 6:
                        player.classnotes.append("Mighty Summoner - Beasts and fey that you conjure are more resilient than normal. Any beast or fey summoned or created by a spell that you cast gains two benefits:\n- The creature appears with more hit points than normal: 2 extra hit points per Hit Die it has.\n- The damage from its natural weapons is considered magical for the purpose of overcoming immunity and resistance to nonmagical attacks and damage.")
                    if drulvl >= 10:
                        player.classnotes.append(f"Guardian Spirit - Your Spirit Totem safeguards the beasts and fey that you call forth with your magic. When a beast or fey that you summoned or created with a spell ends its turn in your Spirit Totem aura, that creature regains a number of hit points equal to half your Druid level, rounded down, or {math.floor(drulvl/2)} hit points.")
                    if drulvl >= 14:
                        player.classnotes.append("Faithful Summons (see notes)")
                        player.notes.append("Faithful Summons - The nature spirits you commune with protect you when you are the most defenseless. If you are reduced to 0 hit points or are incapacitated against your will, you can immediately gain the benefits of Conjure Animals as if it were cast with a 9th-level spell slot. It summons four beasts of your choice that are challenge rating 2 or lower. The conjured beasts appear within 20 feet of you. If they receive no commands from you, they protect you from harm and attack your foes. The spell lasts for 1 hour, requiring no concentration, or until you dismiss it (no action required).\nOnce you use this feature, you can’t use it again until you finish a long rest.")
                if player.subclass[i] == "Circle of Spores Druid":
                    DruidCircleSporesSpells = []
                    if drulvl >= 3:
                        DruidCircleSporesSpells.append("Blindness/Deafness")
                        DruidCircleSporesSpells.append("Gentle Repose")
                    if drulvl >= 5:
                        DruidCircleSporesSpells.append("Animate Dead")
                        DruidCircleSporesSpells.append("Gaseous Form")
                    if drulvl >= 7:
                        DruidCircleSporesSpells.append("Blight")
                        DruidCircleSporesSpells.append("Confusion")
                    if drulvl >= 9:
                        DruidCircleSporesSpells.append("Cloudkill")
                        DruidCircleSporesSpells.append("Contagion") 
                    druidcircle_str = ", ".join(f"{spell}" for spell in DruidCircleSporesSpells)                      
                    HaloSporesDmg = "1d4"
                    if drulvl >= 6:
                        HaloSporesDmg = "1d6"
                    if drulvl >= 10:
                        HaloSporesDmg = "1d8"
                    if drulvl >= 14:
                        HaloSporesDmg = "1d10"
                    player.classnotes.append("Halo of Spores (see notes)")
                    player.notes.append(f"Halo of Spores - You are surrounded by invisible, necrotic spores that are harmless until you unleash them on a creature nearby. When a creature you can see moves into a space within 10 feet of you or starts its turn there, you can use your reaction to deal {HaloSporesDmg} necrotic damage to that creature unless it succeeds on a Constitution saving throw against your spell save DC, or against {player.spellsavedc[i]}.")
                    player.classnotes.append("Symbiotic Entity (see notes)")
                    player.notes.append(f"Symbiotic Entity - You gain the ability to channel magic into your spores. As an action, you can expend a use of your Wild Shape feature to awaken those spores, rather than transforming into a beast form, and you gain five times your Druid level temporary hitpoints, or {5*drulvl} temporary hit points. While this feature is active, you gain the following benefits:\n- When you deal your Halo of Spores damage, roll the damage die a second time and add it to the total.\n- Your melee weapon attacks deal an extra 1d6 poison damage to any target they hit.\nThese benefits last for 10 minutes, until you lose all these temporary hit points, or until you use your Wild Shape again.")
                    if drulvl >= 6:
                        player.classnotes.append("Fungal Infestation (see notes)")
                        player.notes.append("Fungal Infestation - Your spores gain the ability to infest a humanoid corpse and animate it.\nIf a beast or humanoid that is Small or Medium dies within 10 feet of you, you can use your reaction to animate it, causing it to stand up immediately with 1 hit point. The creature uses the zombie statistics. It remains animate for 1 hour, after which time it collapses and dies.\nIn combat, the zombie's turn is immediately after yours. It obeys your mental commands, and the only action it can take is the Attack action, making one melee attack.")
                    if drulvl >= 10:
                        player.classnotes.append("Spreading Spores (see notes)")
                        player.notes.append(f"Spreading Spores - You gain the ability to seed an area with deadly spores. As a bonus action while your Symbiotic Entity feature is active, you can hurl spores up to 30 feet away, where they swirl in a 10-foot cube for 1 minute. The spores disappear early if you use this feature again, if you dismiss them as a bonus action, or if your Symbiotic Entity feature is no longer active.\nWhenever a creature moves into the cube or starts its turn there, that creature takes your Halo of Spores damage, unless the creature succeeds on a Constitution saving throw against your spell save DC, or against {player.spellsavedc[i]}. A creature can take this damage no more than once per turn.\nWhile the cube of spores persists, you can't use your Halo of Spores reaction.")
                    if drulvl >= 14:
                        player.classnotes.append("Fungal Body - The fungal spores in your body alter you: you can’t be blinded, deafened, frightened, or poisoned, and any critical hit against you counts as a normal hit, unless you are incapacitated.")    
                    if drulvl >= 2:
                        player.classnotes.append("Circle Spells (see notes)")
                        player.notes.append(f"Circle Spells - Your symbiotic link to fungus and your ability to tap into the cycle of life and death grants you access to certain spells. You learn the Chill Touch cantrip. Currently the spells you know from this are: {druidcircle_str}.\nOnce you gain access to one of these spells, you always have it prepared, and it doesn’t count against the number of spells you can prepare each day. If you gain access to a spell that doesn’t appear on the druid spell list, the spell is nonetheless a druid spell for you.")
                if player.subclass[i] == "Circle of the Stars Druid":
                    SM1 = "A scroll covered with depictions of constellations"
                    SM2 = "A stone tablet with fine holes drilled through it"
                    SM3 = "A speckled owlbear hide, tooled with raised marks"
                    SM4 = "A collection of maps bound in an ebony cover"
                    SM5 = "A crystal that projects starry patterns when placed before a light"
                    SM6 = "Glass disks that depict constellations"
                    SM = [SM1, SM2, SM3, SM4, SM5, SM6]
                    StarMap = random.choice(SM)
                    player.classnotes.append("Star Map (see notes)")
                    player.notes.append(f"Star Map - You've created a star chart as part of your heavenly studies. It is a Tiny object and can serve as a spellcasting focus for your druid spells. The form of this Star Map is: {StarMap}.\nWhile holding this map, you have these benefits:\n- You know the Guidance cantrip.\n- You have the Guiding Bolt spell prepared. It counts as a druid spell for you, and it doesn't count against the number of spells you can have prepared.\n- You can cast Guiding Bolt without expending a spell slot. You can do so a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.\nIf you lose the map, you can perform a 1-hour ceremony to magically create a replacement. This ceremony can be performed during a short or long rest, and it destroys the previous map.")
                    player.classnotes.append("Starry Form (see notes)")
                    player.notes.append(f"Starry Form - As a bonus action, you can expend a use of your Wild Shape feature to take on a starry form, rather than transforming into a beast.\nWhile in your starry form, you retain your game statistics, but your body becomes luminous; your joints glimmer like stars, and glowing lines connect them as on a star chart. This form sheds bright light in a 10-foot radius and dim light for an additional 10 feet. The form lasts for 10 minutes. It ends early if you dismiss it (no action required), are incapacitated, die, or use this feature again.\nWhenever you assume your starry form, choose which of the following constellations glimmers on your body; your choice gives you certain benefits while in the form:\nArcher - A constellation of an archer appears on you. When you activate this form, and as a bonus action on your subsequent turns while it lasts, you can make a ranged spell attack, hurling a luminous arrow that targets one creature within 60 feet of you. On a hit, the attack deals radiant damage equal to 1d8 + your Wisdom modifier, or 1d8 + {player.WisMod} radiant damage.\nChalice - A constellation of a life-giving goblet appears on you. Whenever you cast a spell using a spell slot that restores hit points to a creature, you or another creature within 30 feet of you can regain hit points equal to 1d8 + your Wisdom modifier, or 1d8 + {player.WisMod} hit points.\nDragon - A constellation of a wise dragon appears on you. When you make an Intelligence or a Wisdom check or a Constitution saving throw to maintain concentration on a spell, you can treat a roll of 9 or lower on the d20 as a 10.")
                    if drulvl >= 6:
                        player.classnotes.append("Cosmic Omen (see notes)")
                        player.notes.append(f"Cosmic Omen - Whenever you finish a long rest, you can consult your Star Map for omens. When you do so, roll a die. Until you finish your next long rest, you gain access to a special reaction based on whether you rolled an even or an odd number on the die:\nWeal (even) - Whenever a creature you can see within 30 feet of you is about to make an attack roll, a saving throw, or an ability check, you can use your reaction to roll a d6 and add the number rolled to the total.\nWoe (odd) - Whenever a creature you can see within 30 feet of you is about to make an attack roll, a saving throw, or an ability check, you can use your reaction to roll a d6 and subtract the number rolled from the total.\nYou can use this reaction a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
                    if drulvl >= 10:
                        player.classnotes.append("Twinkling Constellations (see notes)")
                        player.notes.append("Twinkling Constellations - The constellations of your Starry Form improve. The 1d8 of the Archer and the Chalice becomes 2d8, and while the Dragon is active, you have a flying speed of 20 feet and can hover.\nMoreover, at the start of each of your turns while in your Starry Form, you can change which constellation glimmers on your body.")
                    if drulvl >= 14:
                        player.classnotes.append("Full of Stars - While in your Starry Form, you become partially incorporeal, giving you resistance to bludgeoning, piercing, and slashing damage.")
                if player.subclass[i] == "Circle of Wildfire Druid":        
                    DruidCircleWildfireSpells = []
                    if drulvl >= 2:
                        DruidCircleWildfireSpells.append("Burning Hands")
                        DruidCircleWildfireSpells.append("Cure Wounds")
                    if drulvl >= 3:
                        DruidCircleWildfireSpells.append("Flaming Sphere")
                        DruidCircleWildfireSpells.append("Scorching Ray")
                    if drulvl >= 5:
                        DruidCircleWildfireSpells.append("Plant Growth")
                        DruidCircleWildfireSpells.append("Revivify")
                    if drulvl >= 7:
                        DruidCircleWildfireSpells.append("Aura of Life")
                        DruidCircleWildfireSpells.append("Fire Shield")
                    if drulvl >= 9:
                        DruidCircleWildfireSpells.append("Flame Strike")
                        DruidCircleWildfireSpells.append("Mass Cure Wounds") 
                    druidcircle_str = ", ".join(f"{spell}" for spell in DruidCircleWildfireSpells)                      
                    player.classnotes.append("Summon Wildfire Spirit (see notes)")
                    player.notes.append(f"Summon Wildfire Spirit - You can summon the primal spirit bound to your soul. As an action, you can expend one use of your Wild Shape feature to summon your Wildfire Spirit, rather than assuming a beast form.\nThe spirit appears in an unoccupied space of your choice that you can see within 30 feet of you. Each creature within 10 feet of the spirit (other than you) when it appears must succeed on a Dexterity saving throw against your spell save DC, or against {player.spellsavedc[i]}, or take 2d6 fire damage.\nThe spirit is friendly to you and your companions and obeys your commands. See this creature's game statistics in the Wildfire Spirit stat block, which uses your Proficiency Bonus (PB) in several places. You determine the spirit's appearance. Some spirits take the form of a humanoid figure made of gnarled branches covered in flame, while others look like beasts wreathed in fire.\nIn combat, the spirit shares your initiative count, but it takes its turn immediately after yours. The only action it takes on its turn is the Dodge action, unless you take a bonus action on your turn to command it to take another action. That action can be one in its stat block or some other action. If you are incapacitated, the spirit can take any action of its choice, not just Dodge.\nThe spirit manifests for 1 hour, until it is reduced to 0 hit points, until you use this feature to summon the spirit again, or until you die.")
                    if drulvl >= 6:
                        player.classnotes.append("Enhanced Bond (see notes)")
                        player.notes.append("Enhanced Bond - The bond with your wildfire spirit enhances your destructive and restorative spells. Whenever you cast a spell that deals fire damage or restores hit points while your wildfire spirit is summoned, roll a d8, and you gain a bonus equal to the number rolled to one damage or healing roll of the spell.\nIn addition, when you cast a spell with a range other than self, the spell can originate from you or your Wildfire Spirit.")
                    if drulvl >= 10:
                        player.classnotes.append("Cauterizing Flames (see notes)")
                        player.notes.append(f"Cauterizing Flames - You gain the ability to turn death into magical flames that can heal or incinerate. When a Small or larger creature dies within 30 feet of you or your wildfire spirit, a harmless spectral flame springs forth in the dead creature's space and flickers there for 1 minute. When a creature you can see enters that space, you can use your reaction to extinguish the spectral flame there and either heal the creature or deal fire damage to it. The healing or damage equals 2d10 + your Wisdom modifier, or 2d10 + {player.WisMod} healing/damage.\nYou can use this reaction a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
                    if drulvl >= 14:
                        player.classnotes.append("Blazing Revival - The bond with your Wildfire Spirit can save you from death. If the spirit is within 120 feet of you when you are reduced to 0 hit points and thereby fall unconscious, you can cause the spirit to drop to 0 hit points. You then regain half your hit points and immediately rise to your feet.\nOnce you use this feature, you can't use it again until you finish a long rest.")    
                    if drulvl >= 2:
                        player.classnotes.append("Circle Spells (see notes)")
                        player.notes.append(f"Circle Spells - You have formed a bond with a wildfire spirit, a primal being of creation and destruction. Your link with this spirit grants you access to some spells when you reach certain levels in this class, which are currently {druidcircle_str}.\nOnce you gain access to one of these spells, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you gain access to a spell that doesn't appear on the druid spell list, the spell is nonetheless a druid spell for you.")
                DruidSpellSlot1 = 4
                DruidSpellSlot2 = 2
            if drulvl >= 4:
                DruidCantripsKnown = 3
                DruidSpellSlot2 = 3
                player.classnotes.append("Cantrip Versatility (see notes)")
                player.notes.append("Cantrip Versatility - Whenever you reach a level in this class that grants the Ability Score Improvement feature, you can replace one cantrip you learned from this class's Spellcasting feature with another cantrip from the druid spell list.")
            if drulvl >= 5:
                DruidSpellSlot3 = 2
            if drulvl >= 6:
                DruidSpellSlot3 = 3
            if drulvl >= 7:
                DruidSpellSlot4 = 1
            if drulvl >= 8:
                DruidSpellSlot4 = 2
            if drulvl >= 9:
                DruidSpellSlot4 = 3
                DruidSpellSlot5 = 1
            if drulvl >= 10:
                DruidCantripsKnown = 4
                DruidSpellSlot5 = 2
            if drulvl >= 11:
                DruidSpellSlot6 = 1
            if drulvl >= 13:
                DruidSpellSlot7 = 1
            if drulvl >= 15:
                DruidSpellSlot8 = 1
            if drulvl >= 17:
                DruidSpellSlot9 = 1
            if drulvl >= 18:
                DruidSpellSlot5 = 3
                player.classnotes.append("Timeless Body - The primal magic that you wield causes you to age more slowly. For every 10 years that pass, your body ages only 1 year.")
                player.classnotes.append("Beast Spells (see notes)")
                player.notes.append("Beast Spells - You can cast many of your druid spells in any shape you assume using Wild Shape. You can perform the somatic and verbal components of a druid spell while in a beast shape, but you aren’t able to provide material components.")
            if drulvl >= 19:
                DruidSpellSlot6 = 2
            if drulvl == 20:
                DruidSpellSlot7 = 2
                player.classnotes.append("Archdruid (see notes)")
                player.notes.append("Archdruid - You can use your Wild Shape an unlimited number of times.\nAdditionally, you can ignore the verbal and somatic components of your druid spells, as well as any material components that lack a cost and aren’t consumed by a spell. You gain this benefit in both your normal shape and your beast shape from Wild Shape.")                
            player.notes.append(f"You have {DruidCantripsKnown} cantrips available to you.")
            player.notes.append(f"The number of first level spell slots you have as a Druid is: {DruidSpellSlot1}.")
            if DruidSpellSlot2 != 0:
                player.notes.append(f"The number of second level spell slots you have as a Druid is: {DruidSpellSlot2}.")
            if DruidSpellSlot3 != 0:                
                player.notes.append(f"The number of third level spell slots you have as a Druid is: {DruidSpellSlot3}.")
            if DruidSpellSlot4 != 0:
                player.notes.append(f"The number of fourth level spell slots you have as a Druid is: {DruidSpellSlot4}.")
            if DruidSpellSlot5 != 0:
                player.notes.append(f"The number of fifth level spell slots you have as a Druid is: {DruidSpellSlot5}.")
            if DruidSpellSlot6 != 0:
                player.notes.append(f"The number of sixth level spell slots you have as a Druid is: {DruidSpellSlot6}.")
            if DruidSpellSlot7 != 0:
                player.notes.append(f"The number of seventh level spell slots you have as a Druid is: {DruidSpellSlot7}.")
            if DruidSpellSlot8 != 0:
                player.notes.append(f"The number of eighth level spell slots you have as a Druid is: {DruidSpellSlot8}.")
            if DruidSpellSlot9 != 0:
                player.notes.append(f"The number of ninth level spell slots you have as a Druid is: {DruidSpellSlot9}.")                
        if player.Class[i] == "Fighter":
            if ((param == "N") or (player.singlemulticlass == "N")):
                figlvl = player.level
                player.classlvl.append(figlvl)   
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    figlvl = int(input(f"Given your pool of levels of {poollevel}, what is your Fighter level? "))       
                    if figlvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                    
                poollevel = poollevel - figlvl
                player.classlvl.append(figlvl)
            if figlvl >= 1:
                player.hitdice.append(f"{figlvl}d10 for {player.Class[i]}")
                if figlvl == 1:
                    player.hitpoints += (10 + player.ConMod)
                else:
                    player.hitpoints += (10 + player.ConMod + hpcalc(figlvl, dice, 10))
                if i == 0:       
                    profs = ["Light Armor", "Medium Armor", "Heavy Armor", "Shield", "Simple Weapons", "Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)                                
                    player.skills.append(dnd_tools.saving_throws["StrST"])
                    player.skills.append(dnd_tools.saving_throws["ConST"])
                    SkillsList = [
                        dnd_tools.skills["Acrobatics"], 
                        dnd_tools.skills["AnimalHandling"], 
                        dnd_tools.skills["Athletics"], 
                        dnd_tools.skills["History"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Intimidation"], 
                        dnd_tools.skills["Perception"], 
                        dnd_tools.skills["Survival"]
                        ]
                    player.skills = twoskillsfromlist(param, player.skills, SkillsList)  
                    StartEquip1 = ["Chain Mail", "Leather Armor, Longbow and 20 Arrows"]
                    StartEquip2 = ["Martial Weapon and Shield", "Two Martial Weapons"]
                    StartEquip3 = ["Light Crossbow and 20 Bolts", "Two Handaxes"]
                    StartEquip4 = ["Dungeoneer's Pack", "Explorer's Pack"]
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Chain Mail")
                        print("2 - Leather Armor, Longbow and 20 Arrows")
                        se1 = int(input("What would you like your first choice for starting equipment to be? "))
                        if se1 == 0:
                            SE1rand = random.choice(StartEquip1)
                            if SE1rand == "Chain Mail":
                                player.equipment.append(dnd_tools.heavy_armor["ChainMail"].copy())
                            if SE1rand == "Leather Armor, Longbow and 20 Arrows":
                                player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                                player.equipment.append(dnd_tools.martial_weapons["Longbow"].copy())
                                player.equipment.append("20 Arrows")
                        if se1 == 1:
                            player.equipment.append(dnd_tools.heavy_armor["ChainMail"].copy())
                        if se1 == 2:
                            player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                            player.equipment.append(dnd_tools.martial_weapons["Longbow"].copy())
                            player.equipment.append("20 Arrows")
                        print("0 - Random")
                        print("1 - Martial Weapon and Shield")
                        print("2 - Two Martial Weapons")
                        se2 = int(input("What would you like your second choice for starting equipment to be? "))
                        if se2 == 0:
                            SE2rand = random.choice(StartEquip2)
                            if SE2rand == "Martial Weapon and Shield":
                                player.equipment.append(random.choice(MartialWeapons))
                                player.equipment.append(dnd_tools.shields["Shield"].copy())
                            if SE2rand == "Two Martial Weapons":
                                MartWepRandKey1 = random.choice(MartialWeapons)
                                player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey1].copy())
                                MartWepRandKey2 = random.choice(MartialWeapons)
                                player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey2].copy())
                        if se2 == 1:
                            print("0 - Random")
                            for j, mw in enumerate(MartialWeaponsNames, 1):
                                print(f"{j} - {mw}")
                            se2mw = int(input("Which martial weapon would you like to add to your inventory? "))
                            if se2mw == 0:
                                MartWepRandKey = random.choice(MartialWeapons)
                                player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey].copy())
                            elif 1 <= se2mw <= len(MartialWeapons):
                                MartWepKey = MartialMeleeWeapons[se2mw-1]
                                player.equipment.append(dnd_tools.martial_weapons[MartWepKey].copy())
                            player.equipment.append(dnd_tools.shields["Shield"].copy())
                        if se2 == 2:
                            print("0 - Random")
                            for j, mw1 in enumerate(MartialWeaponsNames, 1):
                                print(f"{j} - {mw1}")
                            se2mw1 = int(input("Choose your first martial weapon to add to your inventory? "))
                            if se2mw1 == 0:
                                MartWepRandKey1 = random.choice(MartialWeapons)
                                player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey1].copy())
                            elif 1 <= se2mw1 <= len(MartialWeapons):
                                MartWepKey1 = MartialMeleeWeapons[se2mw1-1]
                                player.equipment.append(dnd_tools.martial_weapons[MartWepKey1].copy())                              
                            print("0 - Random")
                            for j, mw in enumerate(MartialWeaponsNames, 1):
                                print(f"{j} - {mw}")
                            se2mw2 = int(input("Choose your second martial weapon to add to your inventory? "))
                            if se2mw2 == 0:
                                MartWepRandKey2 = random.choice(MartialWeapons)
                                player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey2].copy())
                            elif 1 <= se2mw2 <= len(MartialWeapons):
                                MartWepKey2 = MartialMeleeWeapons[se2mw2-1]
                                player.equipment.append(dnd_tools.martial_weapons[MartWepKey2].copy())                              
                        print("0 - Random")
                        print("1 - Light Crossbow and 20 Bolts")
                        print("2 - Two Handaxes")       
                        se3 = int(input("What would you like your third choice for starting equipment to be? "))
                        if se3 == 0:
                            SE3rand = random.choice(StartEquip3)
                            if SE3rand == "Light Crossbow and 20 Bolts":
                                player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                                player.equipment.append("20 Bolts")
                            if SE3rand == "Two Handaxes":
                                player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                                player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                        if se3 == 1:
                            player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                            player.equipment.append("20 Bolts")
                        if se3 == 2: 
                            player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                            player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy()) 
                        print("0 - Random")
                        print("1 - Dungeoneer's Pack")
                        print("2 - Explorer's Pack")       
                        se4 = int(input("What would you like your fourth choice for starting equipment to be? "))                       
                        if se4 == 0:
                            SE4rand = random.choice(StartEquip4)
                            if SE4rand == "Dungeoneer's Pack":
                                player.equipment.extend(dnd_tools.packs["DungeoneersPack"]["contents"])
                            if SE4rand == "Explorer's Pack":
                                player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])
                        if se4 == 1:
                            player.equipment.extend(dnd_tools.packs["DungeoneersPack"]["contents"])
                        if se4 == 2:
                            player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "Chain Mail":
                            player.equipment.append(dnd_tools.heavy_armor["ChainMail"].copy())
                        if SE1rand == "Leather Armor, Longbow and 20 Arrows":
                            player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                            player.equipment.append(dnd_tools.martial_weapons["Longbow"].copy())
                            player.equipment.append("20 Arrows")
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "Martial Weapon and Shield":
                            MartWepRandKey = random.choice(MartialWeapons)
                            player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey].copy())
                            player.equipment.append(dnd_tools.shields["Shield"].copy())
                        if SE2rand == "Two Martial Weapons":
                            MartWepRandKey1 = random.choice(MartialWeapons)
                            player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey1].copy())
                            MartWepRandKey2 = random.choice(MartialWeapons)
                            player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey2].copy())
                        SE3rand = random.choice(StartEquip3)
                        if SE3rand == "Light Crossbow and 20 Bolts":
                            player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                            player.equipment.append("20 Bolts")
                        if SE3rand == "Two Handaxes":
                            player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                            player.equipment.append(dnd_tools.simple_weapons["Handaxe"].copy())
                        SE4rand = random.choice(StartEquip4)
                        if SE4rand == "Dungeoneer's Pack":
                            player.equipment.extend(dnd_tools.packs["DungeoneersPack"]["contents"])
                        if SE4rand == "Explorer's Pack":
                            player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"]) 
                else:
                    profs = ["Light Armor", "Medium Armor", "Shield", "Simple Weapons", "Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)                                                                             
            player.classnotes.append("Fighting Style (see notes)")
            player.notes.append(f"Fighting Style - You adopt a particular style of fighting as your specialty. Choose one of the following options. You can’t take a Fighting Style option more than once, even if you later get to choose again.\n- Archery - You gain a +2 bonus to attack rolls you make with ranged weapons.\n- Blind Fighting - You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you.\n- Defense - While you are wearing armor, you gain a +1 bonus to AC.\n- Dueling - When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.\n- Great Weapon Fighting - When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit.\n- Interception - When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by 1d10 + your Proficiency Bonus, or reduction by 1d10 + {player.profbonus}, to a minimum of 0 damage. You must be wielding a shield or a simple or martial weapon to use this reaction.\n- Protection - When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.\n- Superior Technique - You learn one maneuver of your choice from among those available to the Battle Master archetype. If a maneuver you use requires your target to make a saving throw to resist the maneuver's effects, the saving throw DC equals 8 + your Proficiency Bonus, {8 + player.profbonus}, + your Strength or Dexterity modifier (your choice). You gain one superiority die, which is a d6 (this die is added to any superiority dice you have from another source). This die is used to fuel your maneuvers. A superiority die is expended when you use it. You regain your expended superiority dice when you finish a short or long rest.\n- Thrown Weapon Fighting - You can draw a weapon that has the thrown property as part of the attack you make with the weapon. In addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll.\n- Two-Weapon Fighting - When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.\n- Unarmed Fighting - Your unarmed strikes can deal bludgeoning damage equal to 1d6 + your Strength modifier, or 1d6 + {player.StrMod} bludgeoning damage, on a hit. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8. At the start of each of your turns, you can deal 1d4 bludgeoning damage to one creature grappled by you.")
            player.classnotes.append("Second Wind (see notes)")
            player.notes.append(f"Second Wind - You have a limited well of stamina that you can draw on to protect yourself from harm. On your turn, you can use a bonus action to regain hit points equal to 1d10 + your Fighter level, or 1d10 + {figlvl} hit points. Once you use this feature, you must finish a short or long rest before you can use it again.")
            if figlvl >= 2:
                player.classnotes.append("Action Surge(1) - You can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action.\nOnce you use this feature, you must finish a short or long rest before you can use it again.")
                if figlvl >= 17:
                    player.classnotes.append("Action Surge(2) - You can use it twice before a rest, but only once on the same turn.")
            if figlvl >= 3:
                Fig = ["Arcane Archer Archetype Fighter", "Battle Master Archetype Fighter", "Cavalier Archetype Fighter", "Champion Archetype Fighter", "Echo Knight Archetype Fighter", "Eldrich Knight Archetype Fighter", "Psi Warrior Archetype Fighter", "Purple Dragon Knight Archetype Fighter", "Rune Knight Archetype Fighter", "Samurai Archetype Fighter", "Scofflaw Archetype Fighter"]
                
                print(f"Subclasses are: {player.subclass}")
                if player.subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        for idx, subcl in enumerate(Fig, 1):
                            print(f"{idx} - {subcl}")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 0:
                            player.subclass[i] = random.choice(Fig)
                        elif 1 <= subc <= len(Fig):
                            player.subclass[i] = Fig[subc - 1]
                    if param == "N":
                        player.subclass[i] = random.choice(Fig)                       
                if player.subclass[i] == "Arcane Archer Archetype Fighter":
                    player.classnotes.append("Arcane Archer Lore - You learn magical theory or some of the secrets of nature – typical for practitioners of of this elven martial tradition. You choose to gain proficiency in either the Arcana or the Nature skill, and you choose to learn either the Prestidigitation or Druidcraft cantrip.")
                    player.classnotes.append("Arcane Shot (see notes)")
                    player.notes.append("Arcane Shot - You learn to unleash special magical effects with some of your shots. When you gain this feature, you learn two Arcane Shot options of your choice (see the Fighter Arcane Archer Arcane Shot table).\nOnce per turn when you fire an arrow from a shortbow or longbow as part of the Attack action, you can apply one of your Arcane Shot options to that arrow. You decide to use the option when the arrow hits, unless the option doesn’t involve an attack roll. You have two uses of this ability, and you regain all expended uses of it when you finish a short or long rest.\nYou gain an additional Arcane Shot option of your choice when you reach certain levels in this class: 7th, 10th, 15th, and 18th level. Each option also improves when you become an 18th-level fighter.")
                    if figlvl >= 7:
                        player.classnotes.append("Magic Arrow (see notes)")
                        player.notes.append("Magic Arrow - You gain the ability to infuse arrows with magic. Whenever you fire a nonmagical arrow from a shortbow or longbow, you can make it magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage. The magic fades from the arrow immediately after it hits or misses its target.")
                        player.classnotes.append("Curving Shot - You learn how to direct an errant arrow toward a new target. When you make an attack roll with a magic arrow and miss, you can use a bonus action to reroll the attack roll against a different target within 60 feet of the original target.")
                    if figlvl >= 15:
                        player.classnotes.append("Ever-Ready Shot - Your magical archery is available whenever battle starts. If you roll initiative and have no uses of Arcane Shot remaining, you regain one use of it.")
                if player.subclass[i] == "Battle Master Archetype Fighter":
                    SuperiorityDie = "four"
                    if ((figlvl >= 7) and (figlvl < 15)):
                        SuperiorityDie = "five"
                    if figlvl >= 15:
                        SuperiorityDie = "six"
                    player.classnotes.append("Combat Superiority (see notes)")
                    player.notes.append(f"Combat Superiority - You learn maneuvers that are fueled by special dice called superiority dice.\nManeuvers - You learn three maneuvers (from Maneuvers table) of your choice. Many maneuvers enhance an attack in some way. You can use only one maneuver per attack. You learn two additional maneuvers of your choice at 7th, 10th, and 15th level. Each time you learn new maneuvers, you can also replace one maneuver you know with a different one.\nSuperiority Dice - You have {SuperiorityDie} superiority dice, which are d8s. A superiority die is expended when you use it. You regain all of your expended superiority dice when you finish a short or long rest.\nSaving Throws - Some of your maneuvers require your target to make a saving throw to resist the maneuver's effects. The saving throw DC is calculated as follows:\nManeuver save DC = 8 + your Proficiency Bonus, or {8 + player.profbonus}, + your Strength or Dexterity modifier (your choice)")
                    player.proficiencies = artisantools(param, player.proficiencies)                    
                    if figlvl >= 7:
                        player.classnotes.append("Know Your Enemy (see notes)")
                        player.notes.append("Know Your Enemy - If you spend at least 1 minute observing or interacting with another creature outside combat, you can learn certain information about its capabilities compared to your own. The DM tells you if the creature is your equal, superior, or inferior in regard to two of the following characteristics of your choice:\n- Strength score\n- Dexterity score\n- Constitution score\n- Armor Class\n- Current hit points\n- Total class levels, if any\n- Fighter class levels, if any")
                        player.classnotes.append("")
                    if figlvl >= 10:
                        SuperiorityDieValue = "d10"
                        if figlvl >= 18:
                            SuperiorityDieValue = "d12"
                        player.classnotes.append(f"Improved Combat Superiority - Your superiority dice turn into {SuperiorityDieValue}s.")
                    if figlvl >= 15:
                        player.classnotes.append("Relentless - When you roll initiative and have no superiority dice remaining, you regain 1 superiority die.")
                if player.subclass[i] == "Cavalier Archetype Fighter":
                    CavFig = ["Skills", "Language"]
                    if param == "Y":                        
                        print("0 - Random")
                        print("1 - Skill Proficiecy in Animal Handling, History, Insight, Performance, Persuasion")
                        print("2 - One Language of your choice")
                        cavfiginput = int(input("Choose what you would like your bonus, due to this class, to be. "))
                        if cavfiginput == 0:
                            CavFigChoice = random.choice(CavFig)
                        elif 1 <= cavfiginput <= len(CavFig):
                            CavFigChoice = CavFig[cavfiginput-1]
                        if CavFigChoice == "Skills":
                            SkillsList = [
                                dnd_tools.skills["AnimalHandling"], 
                                dnd_tools.skills["History"], 
                                dnd_tools.skills["Insight"], 
                                dnd_tools.skills["Performance"], 
                                dnd_tools.skills["Persuasion"]
                                ]
                            player.skills = oneskillfromlist(param, player.skills, SkillsList)
                        if CavFigChoice == "Language":
                            player.languages, player.slang = languagegen(param, player.languages, player.slang)
                    if param == "N":
                        CavFigChoice = random.choice(CavFig)
                        if CavFigChoice == "Skills":
                            SkillsList = [
                                dnd_tools.skills["AnimalHandling"], 
                                dnd_tools.skills["History"], 
                                dnd_tools.skills["Insight"], 
                                dnd_tools.skills["Performance"], 
                                dnd_tools.skills["Persuasion"]
                                ]
                            player.skills = oneskillfromlist(param, player.skills, SkillsList)
                        if CavFigChoice == "Language":
                            player.languages, player.slang = languagegen(param, player.languages, player.slang)                        
                    player.classnotes.append("Born to the Saddle (see notes)")
                    player.notes.append("Born to the Saddle - Your mastery as a rider becomes apparent. You have advantage on saving throws made to avoid falling off your mount. If you fall off your mount and descend no more than 10 feet, you can land on your feet if you’re not incapacitated.\nFinally, mounting or dismounting a creature costs you only 5 feet of movement, rather than half your speed.")
                    player.classnotes.append("Unwavering Mark (see notes)")
                    player.notes.append(f"Unwavering Mark - You can menace your foes, foiling their attacks and punishing them for harming others. When you hit a creature with a melee weapon attack, you can mark the creature until the end of your next turn. This effect ends early if you are incapacitated or you die, or if someone else marks the creature.\nWhile it is within 5 feet of you, a creature marked by you has disadvantage on any attack roll that doesn't target you.\nIn addition, if a creature marked by you deals damage to anyone other than you, you can make a special melee weapon attack against the marked creature as a bonus action on your next turn. You have advantage on the attack roll, and if it hits, the attack's weapon deals extra damage to the target equal to half your Fighter level, or {math.ceil(figlvl/2)} extra damage.\nRegardless of the number of creatures you mark, you can make this special attack a number of times equal to your Strength modifier, or {player.StrMod} times, a minimum of once, and you regain all expended uses of it when you finish a long rest.")               
                    if figlvl >= 7:
                        player.classnotes.append("Warding Maneuver (see notes)")
                        player.notes.append(f"Warding Maneuver - You learn to fend off strikes directed at you, your mount, or other creatures nearby. If you or a creature you can see within 5 feet of you is hit by an attack, you can roll 1d8 as a reaction if you're wielding a melee weapon or a shield. Roll the die, and add the number rolled to the target's AC against that attack. If the attack still hits, the target has resistance against the attack's damage.\nYou can use this feature a number of times equal to your Constitution modifier, or {player.ConMod} times, a minimum of once, and you regain all expended uses of it when you finish a long rest.")
                    if figlvl >= 10:
                        player.classnotes.append("Hold the Line - You become a master of locking down your enemies. Creatures provoke an opportunity attack from you when they move 5 feet or more while within your reach, and if you hit a creature with an opportunity attack, the target's speed is reduced to 0 until the end of the current turn.")
                    if figlvl >= 15:
                        player.classnotes.append("Ferocious Charger (see notes)")
                        player.notes.append(f"Ferocious Charger - You can run down your foes, whether you're mounted or not. If you move at least 10 feet in a straight line right before attacking a creature and you hit it with the attack, that target must succeed on a Strength saving throw, DC of 8 + your Proficiency Bonus + your Strength modifier, or DC {8 + player.profbonus + player.StrMod}, or be knocked prone. You can use this feature only once on each of your turns.")
                    if figlvl >= 18:
                        player.classnotes.append("Vigilant Defender (see notes)")
                        player.notes.append("Vigilant Defender - You respond to danger with extraordinary vigilance. In combat, you get a special reaction that you can take once on every creature's turn, except your turn. You can use this special reaction only to make an opportunity attack, and you can't use it on the same turn that you take your normal reaction.")
                if player.subclass[i] == "Champion Archetype Fighter":
                    player.classnotes.append("Improved Critical - Your weapon attacks score a critical hit on a roll of 19 or 20.")
                    if figlvl >= 7:
                        player.classnotes.append(f"Remarkable Athlete - You can add half your Proficiency Bonus, or {math.ceil(player.profbonus/2)} to any Strength, Dexterity, or Constitution check you make that doesn't already use your Proficiency Bonus.\nIn addition, when you make a running long jump, the distance you can cover increases by a number of feet equal to your Strength modifier, or {player.StrMod} feet.")
                    if figlvl >= 10:
                        player.classnotes.append("Additional Fighting Style - You can choose a second option from the Fighting Style class feature.")
                    if figlvl >= 15:
                        player.classnotes.append("Superior Critical - Your weapon attacks score a critical hit on a roll of 18-20.")
                    if figlvl >= 18:
                        player.classnotes.append(f"Survivor - You attain the pinnacle of resilience in battle. At the start of each of your turns, you regain hit points equal to 5 + your Constitution modifier, or {5 + player.ConMod} hit points, if you have no more than half of your hit points left. You don't gain this benefit if you have 0 hit points.")
                if player.subclass[i] == "Echo Knight Archetype Fighter":
                    player.classnotes.append("Manifest Echo (see notes)")
                    player.notes.append(f"Manifest Echo - You can use a bonus action to magically manifest an echo of yourself in an unoccupied space you can see within 15 feet of you. This echo is a magical, translucent, gray image of you that lasts until it is destroyed, until you dismiss it as a bonus action, until you manifest another echo, or until you're incapacitated.\nYour echo has AC of 14 + your Proficiency Bonus, or AC {14 + player.profbonus}, 1 hit point, and immunity to all conditions. If it has to make a saving throw, it uses your saving throw bonus for the roll. It is the same size as you, and it occupies its space. On your turn, you can mentally command the echo to move up to 30 feet in any direction (no action required). If your echo is ever more than 30 feet from you at the end of your turn, it is destroyed. You can use the echo in the following ways:\n- As a bonus action, you can teleport, magically swapping places with your echo at a cost of 15 feet of your movement, regardless of the distance between the two of you.\n- When you take the Attack action on your turn, any attack you make with that action can originate from your space or the echo's space. You make this choice for each attack.\n- When a creature that you can see within 5 feet of your echo moves at least 5 feet away from it, you can use your reaction to make an opportunity attack against that creature as if you were in the echo's space.")
                    player.classnotes.append("Unleash Incarnation (see notes)")
                    player.notes.append(f"Unleash Incarnation - You can heighten your echo's fury. Whenever you take the Attack action, you can make one additional melee attack from the echo's position.\nYou can use this feature a number of times equal to your Constitution modifier, or {player.ConMod} times, a minimum of once. You regain all expended uses when you finish a long rest.")
                    if figlvl >= 7:
                        player.classnotes.append("Echo Avatar (see notes)")
                        player.notes.append(f"Echo Avatar - You can temporarily transfer your consciousness to your echo. As an action, you can see through your echo's eyes and hear through its ears. During this time, you are deafened and blinded. You can sustain this effect for up to 10 minutes, and you can end it at any time (requires no action). While your echo is being used in this way, it can be up to 1 ,000 feet away from you without being destroyed.")    
                    if figlvl >= 10:
                        player.classnotes.append("Shadow Martyr (see notes)")
                        player.notes.append("Shadow Martyr - You can make your echo throw itself in front of an attack directed at another creature that you can see. Before the attack roll is made, you can use your reaction to teleport the echo to an unoccupied space within 5 feet of the targeted creature. The attack roll that triggered the reaction is instead made against your echo.\nOnce you use this feature, you can't use it again until you finish a short or long rest.")
                    if figlvl >= 15:                                                                  
                        player.classnotes.append("Reclaim Potential (see notes)")
                        player.notes.append(f"Reclaim Potential - You've learned to absorb the fleeting magic of your echo. When an echo of yours is destroyed by taking damage, you can gain a number of temporary hit points equal to 2d6 + your Constitution modifier, or 2d6 + {player.ConMod} temporary hitpoints, provided you don't already have temporary hit points.\nYou can use this feature a number of times equal to your Constitution modifier, or {player.ConMod} times, a minimum of once. You regain all expended uses when you finish a long rest.")  
                    if figlvl >= 18:
                        player.classnotes.append("Legion Of One (see notes)")
                        player.notes.append("Legion Of One - You can use a bonus action to create two echoes with your Manifest Echo feature, and these echoes can coexist. If you try to create a third echo, the previous two echoes are destroyed. Anything you can do from one echo's position can be done from the other's instead.\nIn addition, when you roll initiative and have no uses of your Unleash Incarnation feature left, you regain one use of that feature.")                                                  
                if player.subclass[i] == "Eldrich Knight Archetype Fighter":
                    EKCantrips = 2
                    EKSpellsKnown = 3
                    EKSpellSlot1 = 2
                    EKSpellSlot2 = 0
                    EKSpellSlot3 = 0
                    EKSpellSlot4 = 0
                    player.classnotes.append("Weapon Bond (see notes)")
                    player.notes.append("Weapon Bond - You learn a ritual that creates a magical bond between yourself and one weapon. You perform the ritual over the course of 1 hour, which can be done during a short rest. The weapon must be within your reach throughout the ritual, at the conclusion of which you touch the weapon and forge the bond.\nOnce you have bonded a weapon to yourself, you can't be disarmed of that weapon unless you are incapacitated. If it is on the same plane of existence, you can summon that weapon as a bonus action on your turn, causing it to teleport instantly to your hand.\nYou can have up to two bonded weapons, but can summon only one at a time with your bonus action. If you attempt to bond with a third weapon, you must break the bond with one of the other two.")                     
                    if figlvl >= 4:
                        EKSpellsKnown = 4
                        EKSpellSlot1 = 3
                    if figlvl >= 7:
                        EKSpellsKnown = 5
                        EKSpellSlot1 = 4
                        EKSpellSlot2 = 2
                        player.classnotes.append("War Magic - When you use your action to cast a cantrip, you can make one weapon attack as a bonus action.")
                    if figlvl >= 8:
                        EKSpellsKnown = 6
                    if figlvl >= 10:
                        EKCantrips = 3
                        EKSpellsKnown = 7
                        EKSpellSlot2 = 3
                        player.classnotes.append("Eldritch Strike - You learn how to make your weapon strikes undercut a creature's resistance to your spells. When you hit a creature with a weapon attack, that creature has disadvantage on the next saving throw it makes against a spell you cast before the end of your next turn.")
                    if figlvl >= 11:
                        EKSpellsKnown = 8
                    if figlvl >= 13:
                        EKSpellsKnown = 9
                        EKSpellSlot3 = 2                        
                    if figlvl >= 14:
                        EKSpellsKnown = 10
                    if figlvl >= 15:
                        player.classnotes.append("Arcane Charge - You gain the ability to teleport up to 30 feet to an unoccupied space you can see when you use your Action Surge. You can teleport before or after the additional action.")
                    if figlvl >= 16:
                        EKSpellsKnown = 11
                        EKSpellSlot3 = 3
                    if figlvl >= 18:
                        player.classnotes.append("Improved War Magic - When you use your action to cast a spell, you can make one weapon attack as a bonus action.")
                    if figlvl >= 19:
                        EKSpellsKnown = 12
                        EKSpellSlot4 = 1
                    if figlvl >= 20:
                        EKSpellsKnown = 13
                    player.spellcastingclass.append("EldKngt Fig")
                    player.spellcastingability.append("Int")
                    player.spellsavedc.append(8 + player.profbonus + player.IntMod)
                    player.spellattackmod.append(player.profbonus + player.IntMod)      
                    player.notes.append(f"You have {EKCantrips} cantrips available to you.")
                    player.notes.append(f"The number of first level spell slots you have as an Eldritch Knight Fighter is {EKSpellSlot1}.")
                    if EKSpellSlot2 != 0:
                        player.notes.append(f"The number of second level spell slots you have as an Eldritch Knight Fighter is: {EKSpellSlot2}.")
                    if EKSpellSlot3 != 0:                
                        player.notes.append(f"The number of third level spell slots you have as an Eldritch Knight Fighter is: {EKSpellSlot3}.")
                    if EKSpellSlot4 != 0:
                        player.notes.append(f"The number of fourth level spell slots you have as an Eldritch Knight Fighter is: {EKSpellSlot4}.")                                                         
                if player.subclass[i] == "Psi Warrior Archetype Fighter":
                    PsionicEnergyDice = "d6"
                    if figlvl >= 5:
                        PsionicEnergyDice = "d8"
                    if figlvl >= 11:
                        PsionicEnergyDice = "d10"
                    if figlvl >= 17:
                        PsionicEnergyDice = "d12"
                    player.classnotes.append("Psionic Power (see notes)")
                    player.notes.append(f"Psionic Power - You harbor a wellspring of psionic energy within yourself. This energy is represented by your Psionic Energy dice, which are each a {PsionicEnergyDice}. You have a number of these dice equal to twice your Proficiency Bonus, or {2*player.profbonus} dice, and they fuel various psionic powers you have, which are detailed below.\nSome of your powers expend the Psionic Energy die they use, as specified in a power's description, and you can't use a power if it requires you to use a die when your dice are all expended. You regain all your expended Psionic Energy dice when you finish a long rest. In addition, as a bonus action, you can regain one expended Psionic Energy die, but you can't do so again until you finish a short or long rest.\nThe powers below use your Psionic Energy dice.\nProtective Field - When you or another creature you can see within 30 feet of you takes damage, you can use your reaction to expend one Psionic Energy die, roll the die, and reduce the damage taken by the number rolled plus your Intelligence modifier, or reduction of {player.IntMod}, minimum reduction of 1, as you create a momentary shield of telekinetic force.\nPsionic Strike - You can propel your weapons with psionic force. Once on each of your turns, immediately after you hit a target within 30 feet of you with an attack and deal damage to it with a weapon, you can expend one Psionic Energy die, rolling it and dealing force damage to the target equal to the number rolled plus your Intelligence modifier, or plus {player.IntMod} force damage.\nTelekinetic Movement - You can move an object or a creature with your mind. As an action, you target one loose object that is Large or smaller or one willing creature, other than yourself. If you can see the target and it is within 30 feet of you, you can move it up to 30 feet to an unoccupied space you can see. Alternatively, if it is a Tiny object, you can move it to or from your hand. Either way, you can move the target horizontally, vertically, or both.\nOnce you take this action, you can't do so again until you finish a short or long rest, unless you expend a Psionic Energy die to take it again.")
                    if figlvl >= 7:
                        player.classnotes.append("Telekinetic Adept (see notes)")
                        player.notes.append(f"Telekinetic Adept - You have mastered new ways to use your telekinetic abilities, detailed below.\nPsi-Powered Leap -  As a bonus action, you can propel your body with your mind. You gain a flying speed equal to twice your walking speed until the end of the current turn. Once you take this bonus action, you can't do so again until you finish a short or long rest, unless you expend a Psionic Energy die to take it again.\nTelekinetic Thrust -  When you deal damage to a target with your Psionic Strike, you can force the target to make a Strength saving throw against a DC equal to 8 + your Proficiency Bonus + your Intelligence modifier, or DC {8 + player.profbonus + player.IntMod}. If the save fails, you can knock the target prone or move it up to 10 feet in any direction horizontally.")         
                    if figlvl >= 10:
                        player.classnotes.append("Guarded Mind - The psionic energy flowing through you has bolstered your mind. You have resistance to psychic damage. Moreover, if you start your turn charmed or frightened, you can expend a Psionic Energy die and end every effect on yourself subjecting you to those conditions.")
                    if figlvl >= 15:
                        player.classnotes.append("Bulwark of Force (see notes)")
                        player.notes.append(f"Bulwark of Force - You can shield yourself and others with telekinetic force. As a bonus action, you can choose creatures, which can include you, that you can see within 30 feet of you, up to a number of creatures equal to your Intelligence modifier, or {player.IntMod} creatures, minimum of one creature. Each of the chosen creatures is protected by half cover for 1 minute or until you're incapacitated.\nOnce you take this bonus action, you can't do so again until you finish a long rest, unless you expend a Psionic Energy die to take it again.")
                    if figlvl >= 18:     
                        player.classnotes.append("Telekinetic Master (see notes)")
                        player.notes.append("Telekinetic Master - Your ability to move creatures and objects with your mind is matched by few. You can cast the Telekinesis spell, requiring no components, and your spellcasting ability for the spell is Intelligence. On each of your turns while you concentrate on the spell, including the turn when you cast it, you can make one attack with a weapon as a bonus action.\nOnce you cast the spell with this feature, you can't do so again until you finish a long rest, unless you expend a Psionic Energy die to cast it again.")                                                            
                if player.subclass[i] == "Purple Dragon Knight Archetype Fighter":
                    player.classnotes.append("Rallying Cry (see notes)")
                    player.notes.append(f"Rallying Cry - When you choose this archetype at 3rd level, you learn how to inspire your allies to fight on past their injuries.\nWhen you use your Second Wind feature, you can choose up to three creatures within 60 feet of you that are allied with you. Each one regains hit points equal to your Fighter level, or {figlvl} hit points, provided that the creature can see or hear you.")
                    if figlvl >= 7:
                        if dnd_tools.skills["Persuasion"] not in player.skills:
                            player.skills.append(dnd_tools.skills["Persuasion"])
                        else:
                            SkillsList = [
                                dnd_tools.skills["AnimalHandling"], 
                                dnd_tools.skills["Insight"], 
                                dnd_tools.skills["Intimidation"], 
                                dnd_tools.skills["Performance"]
                                ]
                            player.skills = oneskillfromlist(param, player.skills, SkillsList)
                        player.classnotes.append("Royal Envoy (see notes)")
                        player.notes.append("Royal Envoy - Knights of high standing are expected to conduct themselves with grace;\nYour Proficiency Bonus is doubled for any ability check you make that uses Persuasion. You receive this benefit regardless of the skill proficiency you gain from this feature.")     
                    if figlvl >= 10:
                        player.classnotes.append("Inspiring Surge(1) - When you use your Action Surge feature, you can choose one creature within 60 feet of you that is allied with you. That creature can make one melee or ranged weapon attack with its reaction, provided that it can see or hear you.")
                    if figlvl >= 15:
                        player.classnotes.append("Bulwark (see notes)")
                        player.notes.append("Bulwark - You can extend the benefit of your Indomitable feature to an ally. When you decide to use Indomitable to reroll an Intelligence, a Wisdom, or a Charisma saving throw and you aren't incapacitated, you can choose one ally within 60 feet of you that also failed its saving throw against the same effect. If that creature can see or hear you, it can reroll its saving throw and must use the new roll.")                            
                    if figlvl >= 18:
                        player.classnotes.append("Inspiring Surge(2) - You can choose two allies within 60 feet of you, rather than one.")                                               
                if player.subclass[i] == "Rune Knight Archetype Fighter":
                    if dnd_tools.artisan_tools["SmthTools"] not in player.proficiencies:
                        player.proficiencies.append(dnd_tools.artisan_tools["SmthTools"])
                    if dnd_tools.languages["Gian"] not in player.languages:
                        player.languages.append(dnd_tools.languages["Gian"])
                    RuneAmount = 2
                    if ((figlvl >= 7) and (figlvl < 10)):
                        RuneAmount = 3
                    if ((figlvl >= 10) and (figlvl < 15)):
                        RuneAmount = 4
                    if figlvl >= 15:
                        RuneAmount = 5
                    player.classnotes.append(f"Rune Carver - You can use magic runes to enhance your gear. You know {RuneAmount} runes of your choice, from among the runes described below, and each time you gain a level in this class, you can replace one rune you know with a different one from this feature.\nWhenever you finish a long rest, you can touch a number of objects equal to the number of runes you know, and you inscribe a different rune onto each of the objects. To be eligible, an object must be a weapon, a suit of armor, a shield, a piece of jewelry, or something else you can wear or hold in a hand. Your rune remains on an object until you finish a long rest, and an object can bear only one of your runes at a time.\nThe Rune Knight Rune Table shows which runes are available to you when you learn a rune. If a rune has a level requirement, you must be at least that level in this class to learn the rune. If a rune requires a saving throw, your Rune Magic save DC equals 8 + your Proficienct Bonues + your Constitution modifier, or DC {8 + player.profbonus + player.ConMod}.")
                    player.classnotes.append("Giant's Might (see notes)")
                    player.notes.append(f"Giant's Might - You have learned how to imbue yourself with the might of giants. As a bonus action, you magically gain the following benefits, which last for 1 minute:\n- If you are smaller than Large, you become Large, along with anything you are wearing. If you lack the room to become Large, your size doesn't change.\n- You have advantage on Strength checks and Strength saving throws.\n- Once on each of your turns, one of your attacks with a weapon or an unarmed strike can deal an extra 1d6 damage to a target on a hit.\nYou can use this feature a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses of it when you finish a long rest.")
                    if figlvl >= 7:
                        player.classnotes.append("Runic Shield (see notes)")
                        player.notes.append(f"Runic Shield - You learn to invoke your rune magic to protect your allies. When another creature you can see within 60 feet of you is hit by an attack roll, you can use your reaction to force the attacker to reroll the d20 and use the new roll.\nYou can use this feature a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
                    if figlvl >= 10:
                        player.classnotes.append("Great Stature - The magic of your runes permanently alters you. When you gain this feature, roll 3d4. You grow a number of inches in height equal to the roll.\nMoreover, the extra damage you deal with your Giant's Might feature increases to 1d8.")
                    if figlvl >= 15:
                        player.classnotes.append("Master of Rune - You can invoke each rune you know from your Rune Carver feature twice, rather than once, and you regain all expended uses when you finish a short or long rest.")
                    if figlvl >= 18:
                        player.classnotes.append("Runic Juggernaut - You learn how to amplify your rune-powered transformation. As a result, the extra damage you deal with the Giant's Might feature increases to 1d10. Moreover, when you use that feature, your size can increase to Huge, and while you are that size, your reach increases by 5 feet.")
                if player.subclass[i] == "Samurai Archetype Fighter":
                    CavFig = ["Skills", "Language"]
                    if param == "Y":                        
                        print("0 - Random")
                        print("1 - Skill Proficiecy in Animal Handling, History, Insight, Performance, Persuasion")
                        print("2 - One Language of your choice")
                        cavfiginput = int(input("Choose what you would like your bonus, due to this class, to be. "))
                        if cavfiginput == 0:
                            CavFigChoice = random.choice(CavFig)
                        elif 1 <= cavfiginput <= len(CavFig):
                            CavFigChoice = CavFig[cavfiginput-1]
                        if CavFigChoice == "Skills":
                            SkillsList = [
                                dnd_tools.skills["History"], 
                                dnd_tools.skills["Insight"], 
                                dnd_tools.skills["Performance"], 
                                dnd_tools.skills["Persuasion"]
                                ]
                            player.skills = oneskillfromlist(param, player.skills, SkillsList)
                        if CavFigChoice == "Language":
                            player.languages, player.slang = languagegen(param, player.languages, player.slang)
                    if param == "N":
                        CavFigChoice = random.choice(CavFig)
                        if CavFigChoice == "Skills":
                            SkillsList = [
                                dnd_tools.skills["History"], 
                                dnd_tools.skills["Insight"], 
                                dnd_tools.skills["Performance"], 
                                dnd_tools.skills["Persuasion"]
                                ]
                            player.skills = oneskillfromlist(param, player.skills, SkillsList)
                        if CavFigChoice == "Language":
                            player.languages, player.slang = languagegen(param, player.languages, player.slang)                                            
                    FigSpiritTempHP = 5
                    if figlvl >= 7:
                        player.classnotes.append("Elegant Courtier (see notes)")
                        player.notes.append(f"Elegant Courtier - Your discipline and attention to detail allow you to excel in social situations. Whenever you make a Charisma (Persuasion) check, you gain a bonus to the check equal to your Wisdom modifier, or a bonus of {player.WisMod}.\nYour self-control also causes you to gain proficiency in Wisdom saving throws. If you already have this proficiency, you instead gain proficiency in Intelligence or Charisma saving throws (your choice).")
                    if figlvl >= 10:
                        FigSpiritTempHP = 10
                        player.classnotes.append("Tireless Spirit - When you roll initiative and have no uses of Fighting Spirit remaining, you regain one use.")
                    if figlvl >= 15:
                        FigSpiritTempHP = 15
                        player.classnotes.append("Rapid Strike (see notes)")
                        player.notes.append("Rapid Strike - You learn to trade accuracy for swift strikes. If you take the Attack action on your turn and have advantage on an attack roll against against one of the targets, you can forgo the advantage for that roll to make an additional weapon attack against that target, as part of the same action. You can do so no more than once per turn.")
                    if figlvl >= 18:
                        player.classnotes.append("Strength Before Death (see notes)")
                        player.notes.append("Strength Before Death - Your fighting spirit can delay the grasp of death. If you take damage that reduces you to 0 hit points, you can use your reaction to delay falling unconscious, and you can immediately take an extra turn. While you have 0 hit points during that extra turn, taking damage causes death saving throw failures as normal, and three death saving throw failures can still kill you. When the extra turn ends, you fall unconscious if you still have 0 hit points.\nOnce you use this feature, you can’t use it again until you finish a long rest.") 
                    player.classnotes.append("Fighting Spirit (see notes)")
                    player.notes.append(f"Fighting Spirit - Your intensity in battle can shield you and help you strike true. As a bonus action on your turn, you can give yourself advantage on all weapon attack rolls until the end of the current turn. When you do so, you also gain {FigSpiritTempHP} temporary hit points.\nYou can use this feature three times. You regain all expended uses of it when you finish a long rest.")                          
                if player.subclass[i] == "Scofflaw Archetype Fighter":        
                    CavFig = ["Skills", "Language"]
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Skill Proficiecy in Animal Handling, History, Insight, Performance, Persuasion")
                        print("2 - One Language of your choice")
                        cavfiginput = int(input("Choose what you would like your bonus, due to this class, to be. "))
                        if cavfiginput == 0:
                            CavFigChoice = random.choice(CavFig)
                        elif 1 <= cavfiginput <= len(CavFig):
                            CavFigChoice = CavFig[cavfiginput-1]
                        if CavFigChoice == "Skills":
                            SkillsList = [
                                dnd_tools.skills["Deception"], 
                                dnd_tools.skills["Insight"], 
                                dnd_tools.skills["Intimidation"], 
                                dnd_tools.skills["SleightofHand"], 
                                dnd_tools.skills["Stealth"]
                                ]
                            player.skills = oneskillfromlist(param, player.skills, SkillsList)
                        if CavFigChoice == "Language":
                            if dnd_tools.TCant not in player.languages:
                                player.languages.append(dnd_tools.TCant)
                    if param == "N":
                        CavFigChoice = random.choice(CavFig)
                        if CavFigChoice == "Skills":
                            SkillsList = [
                                dnd_tools.skills["Deception"], 
                                dnd_tools.skills["Insight"], 
                                dnd_tools.skills["Intimidation"],
                                dnd_tools.skills["SleightofHand"], 
                                dnd_tools.skills["Stealth"]
                                ]
                            player.skills = oneskillfromlist(param, player.skills, SkillsList)
                        if CavFigChoice == "Language":
                            if dnd_tools.TCant not in player.languages:
                                player.languages.append(dnd_tools.TCant)
                    player.classnotes.append("Intimidating Banter - You are adept at integrating insults and barbs into your fighting style. So long as you are in combat, you may choose to use Strength or Dexterity to make Charisma ability checks.")
                    player.classnotes.append("Brutal Brawler(1) (see notes)")
                    player.proficiencies.append("Improvised Weapons")
                    player.notes.append("Brutal Brawler(1) - Your tavernside scuffles have honed your ability to deal damage with just about anything that’s handy. You treat any improvised weapon you handle as if it has the finesse quality.\nAdditionally, whenever you hit with an improvised weapon, you may spend a bonus action to break it over your opponent. Doing this destroys the weapon, but deals the maximum number each of the weapon’s damage dice could deal to the target. Any additional dice added to the attack’s damage roll are not affected by this ability.")
                    if figlvl >= 7:
                        player.classnotes.append("Misdirection (see notes)")
                        player.notes.append(f"Misdirection - You are adept at using words and gestures to taunt or fakeout your opponent, turning their lack of composure against them. This allows you to goad your foe into swinging in ways that can cause them to strike their allies, or which leave them open to a counterattack. As a bonus action you can misdirect an opponent within 5 feet of you. The target must succeed on an Intelligence saving throw against a DC equal to 8 + your Proficiency Bonus, or {8 + player.profbonus}, + your Strength or Dexterity modifier (your choice). On a failure, they must spend their reaction to attack a creature of your choice within 5 feet of them. If no other creatures are present within 5 feet of them, they waste their reaction attacking the air where you once were.\nIn order for you to misdirect a creature in this way they must be able to see, hear, or otherwise be able to understand you.")
                    if figlvl >= 10:
                        player.classnotes.append("Brutal Brawler(2) (see notes)")
                        player.notes.append("Brutal Brawler(2) - The improvised weapons you wield become even more lethal in your hands. When you spend your bonus action to break an improvised weapon over your opponent, add an additional 2d6 to the weapon’s base damage dice.")
                        BlindsideDmg = "5d6"
                        if figlvl >= 15:
                            BlindsideDmg = "7d6"
                        if figlvl >= 18:
                            BlindsideDmg = "9d6"
                        if figlvl >= 18:
                            player.classnotes.append("Blindside (see notes)")
                            player.notes.append(f"Blindside - You are truly skilled at exploiting the openings you create in combat, hitting off-guard opponents with precise blows that are swift and deadly. You may use this technique against any creature that hasn’t yet taken a turn in combat, or who you have successfully misdirected this turn. You may also apply this technique to any attack roll you make with advantage. On a hit, you exploit an opening in the target's defenses, dealing an extra {BlindsideDmg} points of damage, and if you have no uses of this ability at the beginning of combat on your turn, you regain one use of it. Once you use this ability, you can’t use it again until you have taken a short or long rest.")
                        else:   
                            player.classnotes.append("Blindside (see notes)")
                            player.notes.append(f"Blindside - You are truly skilled at exploiting the openings you create in combat, hitting off-guard opponents with precise blows that are swift and deadly. You may use this technique against any creature that hasn’t yet taken a turn in combat, or who you have successfully misdirected this turn. You may also apply this technique to any attack roll you make with advantage. On a hit, you exploit an opening in the target's defenses, dealing an extra {BlindsideDmg} points of damage. Once you use this ability, you can’t use it again until you have taken a short or long rest.") 
                    if figlvl >= 15:
                        player.classnotes.append("Infamy (see notes)")
                        player.notes.append(f"Infamy - Your reputation precedes you, making it easy for you to strike fear into the hearts of anyone foolish enough to oppose you. As part of your attack action, you can utter deadly threats to a single target within 30 feet of you, causing them to become frightened of you for 1 minute on a failed Wisdom saving throw. An affected target may repeat this saving throw at the end of each of their turns, ending the effect on a success. The DC for this saving throw is 8 + your Proficiency Bonus, or {8 + player.profbonus}, + your Strength or Dexterity modifier (your choice). A creature who has witnessed or heard tales of your ruthlessness makes this saving throw with disadvantage.\nIn order for you to use this feature, a creature must be able to see, hear, or otherwise be able to understand you.")
                    if figlvl >= 18:
                        player.classnotes.append("Brutal Brawler(3) (see notes)")
                        player.notes.append("Brutal Brawler(3) - You have advantage on attacks you make with improvised weapons.")                       
                        player.classnotes.append("Two For Flinching (see notes)")
                        player.notes.append("Two For Flinching - You have perfected the art of exploiting your opponent’s weakness. Whenever you take the attack action against an opponent you have successfully misdirected this turn, or an opponent that is afflicted by a condition, you may make one additional attack against that opponent. You may only use this feature once per round.")                                          
            if figlvl >= 4:
                player.classnotes.append("Martial Versatility (see notes)")
                player.notes.append("Martial Versatility - Whenever you reach a level in this class that grants the Ability Score Improvement feature, you can do one of the following, as you shift the focus of your martial practice:\n- Replace a fighting style you know with another fighting style available to fighters.\n- If you know any maneuvers from the Battle Master archetype, you can replace one maneuver you know with a different maneuver.")
            if figlvl >= 5:
                FighterExtraAttack = 2
                if ((figlvl >= 11) and (figlvl < 20)):
                    FighterExtraAttack = 3
                if figlvl == 20:
                    FighterExtraAttack = 4
                player.classnotes.append(f"Extra Attack - You can attack {FighterExtraAttack} times, instead of once, whenever you take the Attack action on your turn.")
            if figlvl >= 9:
                FighterIndomitable = "one time"
                if ((figlvl >= 13) and (figlvl < 17)):
                    FighterIndomitable = "two times"
                if figlvl >= 17:
                    FighterIndomitable = "three times"
                player.classnotes.append(f"Indomitable - You can reroll a saving throw that you fail. If you do so, you must use the new roll, and you can’t use this feature again until you finish a long rest.\nYou can use this feature {FighterIndomitable} between long rests.")                   
        if player.Class[i] == "Monk":
            if ((param == "N") or (player.singlemulticlass == "N")):
                monklvl = player.level
                player.classlvl.append(monklvl) 
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    monklvl = int(input(f"Given your pool of levels of {poollevel}, what is your Monk level? "))    
                    if monklvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                
                poollevel = poollevel - monklvl
                player.classlvl.append(monklvl)
            if monklvl >= 1:
                player.hitdice.append(f"{monklvl}d8 for {player.Class[i]}")
                if monklvl == 1:
                    player.hitpoints += (8 + player.ConMod)
                else:
                    player.hitpoints += (8 + player.ConMod + hpcalc(monklvl, dice, 8)) 
                if i == 0:
                    profs = ["Simple Weapons", dnd_tools.martial_weapons["Shortsword"]["Name"]]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)       
                    player.proficiencies = artisantoolsmusicalinstr(param, player.proficiencies)
                    player.skills.append(dnd_tools.saving_throws["StrST"])
                    player.skills.append(dnd_tools.saving_throws["DexST"])
                    SkillsList = [
                        dnd_tools.skills["Acrobatics"], 
                        dnd_tools.skills["Athletics"], 
                        dnd_tools.skills["History"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Religion"], 
                        dnd_tools.skills["Stealth"]
                        ]    
                    player.skills = twoskillsfromlist(param, player.skills, SkillsList)  
                    StartEquip1 = ["Shortsword", "Any Simple Weapon"]
                    StartEquip2 = ["Dungeoneer's Pack", "Explorer's Pack"]
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Shortsword")
                        print("2 - Any Simple Weapon")
                        se1 = int(input("What would you like your first choice for starting equipment to be? "))
                        if se1 == 0:
                            SE1rand = random.choice(StartEquip1)
                            if SE1rand == "Shortsword":
                                 player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                            if SE1rand == "Any Simple Weapon":
                                SimpRandKey = random.choice(SimpleWeapons)
                                player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                        if se1 == 1:
                             player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                        if se1 == 2:
                            print("0 - Random")
                            for j, sw in enumerate(SimpleWeaponsNames, 1):
                                print(f"{j} - {sw}")
                            se1 = int(input("Which simple weapon would you like to add to your inventory? "))
                            if se1 == 0:
                                SimpRandKey = random.choice(SimpleWeapons)
                                player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                            elif 1 <= se1 <= len(SimpleWeapons):
                                SimpKey = SimpleWeapons[se1-1]
                                player.equipment.append(dnd_tools.simple_weapons[SimpKey].copy())
                        print("0 - Random")
                        print("1 - Dungeoneer's Pack")
                        print("2 - Explorer's Pack")
                        se2 = int(input("What would you like your second choice for starting equipment to be? "))
                        if se2 == 0:
                            SE2rand = random.choice(StartEquip2)
                            if SE2rand == "Dungeoneer's Pack":
                                player.equipment.extend(dnd_tools.packs["DungeoneersPack"]["contents"])
                            if SE2rand == "Explorer's Pack":
                                player.equipment.append(dnd_tools.packs["ExplorersPack"]["contents"])
                        if se2 == 1:
                            player.equipment.extend(dnd_tools.packs["DungeoneersPack"]["contents"])
                        if se2 == 2:
                            player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])
                        player.equipment.append("10 Darts")
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "Shortsword":
                             player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                        if SE1rand == "Any Simple Weapon":
                            SimpRandKey = random.choice(SimpleWeapons)
                            player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "Dungeoneer's Pack":
                            player.equipment.extend(dnd_tools.packs["DungeoneersPack"]["contents"])
                        if SE2rand == "Explorer's Pack":
                            player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])
                        player.equipment.append("10 Darts")       
                else:  
                    profs = ["Simple Weapons", "Shortsword"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
            player.classnotes.append(f"Unarmored Defense - While you are wearing no armor and not wielding a shield, your AC equals 10 + your Dexterity modifier + your Wisdom modifier, or AC {10 + player.DexMod + player.WisMod}.")
            MartialArts = "1d4"
            if monklvl >= 2:   
                KiPoints = 2
                player.spellsavedc.append(8+player.profbonus+player.WisMod)
                UnarmoredMovement = "+10 ft"    
                player.classnotes.append("Dedicated Weapon (see notes)")
                player.notes.append("Dedicated Weapon - You train yourself to use a variety of weapons as monk weapons, not just simple melee weapons and shortswords. Whenever you finish a short or long rest, you can touch one weapon, focus your ki on it, and then count that weapon as a monk weapon until you use this feature again.\nThe chosen weapon must meet these criteria:\n- The weapon must be a simple or martial weapon.\n- You must be proficient with it.\n- It must lack the heavy and special properties.")                                                                                      
            if monklvl >= 3:
                Mon = ["Way of the Ascendant Dragon Monk", "Way of the Astral Self Monk", "Way of the Cobalt Soul Monk", "Way of the Drunken Master Monk", "Way of the Four Elements Monk", "Way of the Kensei Monk", "Way of the Long Death Monk", "Way of Mercy Monk", "Way of the Open Hand Monk", "Way of the Shadow Monk", "Way of the Sun Soul Monk"]
                
                print(f"Subclasses are: {player.subclass}")
                if player.subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        for idx, subcl in enumerate(Mon, 1):
                            print(f"{idx} - {subcl}")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 0:
                            player.subclass[i] = random.choice(Mon)
                        elif 1 <= subc <= len(Mon):
                            player.subclass[i] = Mon[subc - 1]
                    if param == "N":
                        player.subclass[i] = random.choice(Mon)                               
                if player.subclass[i] == "Way of the Ascendant Dragon Monk":
                    ADO1 = "You honed your abilities by aligning your spirit with a dragon's world-altering power."
                    ADO2 = "A dragon personally took an active role in shaping your inner energy."
                    ADO3 = "You studied at a monastery that traces its teachings back centuries or more to a single dragon's instruction, or one that is devoted to a dragon god."
                    ADO4 = "You spent long stretches meditating in the region around an ancient dragon's lair, absorbing that lair's ambient magic."
                    ADO5 = "You found a scroll written in Draconic that contained inspiring new techniques."
                    ADO6 = "After a dream featuring a five-handed dragonborn, you awoke with the mystical breath of dragons."
                    ADO = [ADO1, ADO2, ADO3, ADO4, ADO5, ADO6]
                    AscenDragOrigin = random.choice(ADO)
                    player.classnotes.append(f"As a Way of the Ascendant Dragon Monk, your Ascendant Origin: {AscenDragOrigin}")              
                    if dnd_tools.languages["Drac"] not in player.languages:
                        player.languages.append(dnd_tools.languages["Drac"])
                    else:
                        player.languages, player.slang = languagegen(param, player.languages, player.slang)
                    player.classnotes.append("Draconic Disciple (see notes)")
                    player.notes.append("Draconic Disciple - You can channel draconic power to magnify your presence and imbue your unarmed strikes with the essence of a dragon's breath. You gain the following benefits:\nDraconic Presence. If you fail a Charisma (Intimidation) or Charisma (Persuasion) check, you can use your reaction to reroll the check, as you tap into the mighty presence of dragons. Once this feature turns a failure into a success, you can't use it again until you finish a long rest.\nDraconic Strike - When you damage a target with an unarmed strike, you can change the damage type to acid, cold, fire, lightning, or poison.\nTongue of Dragons. You learn to speak, read, and write Draconic or one other language of your choice (already done).") 
                    player.classnotes.append("Breath of the Dragon (see notes)")
                    player.notes.append(f"Breath of the Dragon - You can channel destructive waves of energy, like those created by the dragons you emulate. When you take the Attack action on your turn, you can replace one of the attacks with an exhalation of draconic energy in either a 20-foot cone or a 30-foot line that is 5 feet wide (your choice). Choose a damage type: acid, cold, fire, lightning, or poison. Each creature in that area must make a Dexterity saving throw against your ki save DC, or against {player.spellsavedc[i]}, taking damage of the chosen type equal to two rolls of your Martial Arts die on a failed save, or half as much damage on a successful one.")
                    if monklvl >= 6:
                        player.classnotes.append("Wings Unfurled (see notes)")
                        player.notes.append(f"Wings Unfurled - When you use your Step of the Wind, you can unfurl spectral draconic wings from your back that vanish at the end of your turn. While the wings exist, you have a flying speed equal to your walking speed.\nYou can use this feature a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.")                     
                    if monklvl >= 11:
                        player.classnotes.append("Breath of the Dragon(2) (see notes)")
                        player.notes.append(f"Breath of the Dragon(2) - The damage of this feature increases to three rolls of your Martial Arts die.You can use this feature a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest. While you have no uses available, you can spend 2 ki points to use this feature again.")                     
                        player.classnotes.append("Aspect of the Wyrm (see notes)")
                        player.notes.append(f"Aspect of the Wyrm - The power of your draconic spirit now radiates from you, warding your allies or inspiring fear in your enemies. As a bonus action, you can create an aura of draconic power that radiates 10 feet from you for 1 minute. For the duration, you gain one of the following effects of your choice:\nFrightful Presence - When you create this aura, and as a bonus action on subsequent turns, you can choose a creature within the aura. The target must succeed on a Wisdom saving throw against your ki save DC, or against {player.spellsavedc[i]}, or become frightened of you for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a successful save.\nResistance - Choose a damage type when you activate this aura: acid, cold, fire, lightning, or poison. You and your allies within the aura have resistance to that damage.\nOnce you create this aura, you can't create it again until you finish a long rest, unless you expend 3 ki points to create it again.")                     
                    if monklvl >= 17:
                        player.classnotes.append("Ascendant Aspect (see notes)")
                        player.notes.append("Ascendant Aspect - Your draconic spirit reaches its peak. You gain the following benefits:\nAugment Breath - When you use your Breath of the Dragon, you can spend 1 ki point to augment its shape and power. The exhalation of draconic energy becomes either a 60-foot cone or a 90-foot line that is 5 feet wide (your choice), and each creature in that area takes damage equal to four rolls of your Martial Arts die on a failed save, or half as much damage on a successful one.\nBlindsight - You gain blindsight out to 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you.\nExplosive Fury - When you activate your Aspect of the Wyrm, draconic fury explodes from you. Choose any number of creatures you can see in your aura. Each of those creatures must succeed on a Dexterity saving throw against your ki save DC or take 3d10 acid, cold, fire, lightning, or poison damage (your choice).") 
                if player.subclass[i] == "Way of the Astral Self Monk":
                    player.classnotes.append("Forms of Your Astral Self (see notes)")
                    player.notes.append("Forms of Your Astral Self - The astral self is a translucent embodiment of the monk's soul. As a result, an astral self can reflect aspects of a monk's background, ideals, flaws, and bonds, and an astral self doesn't necessarily look anything like the monk. for example, the astral self of a lanky human might be reminiscent of a minotaur—the strength of which the monk feels within. Similarly, an orc monk might manifest gossamer arms and a delicate visage, representing the gentle beauty of the orc's soul. Each astral self is unique, and some of the monks of this monastic tradition are known more for the appearance of their astral self than for their physical appearance.\nWhen choosing this path, consider the quirks that define your monk. Are you obsessed with something? Are you driven by justice or a selfish desire? Any of these motivations could manifest in the form of your astral self.")
                    player.classnotes.append("Arms of the Astral Self (see notes)")
                    player.notes.append(f"Arms of the Astral Self - Your mastery of your ki allows you to summon a portion of your astral self. As a bonus action, you can spend 1 ki point to summon the arms of your astral self. When you do so, each creature of your choice that you can see within 10 feet of you must succeed on a Dexterity saving throw or take force damage equal to two rolls of your Martial Arts die.\nFor 10 minutes, these spectral arms hover near your shoulders or surround your arms (your choice). You determine the arms' appearance, and they vanish early if you are incapacitated or die.\nWhile the spectral arms are present, you gain the following benefits:\n- You can use your Wisdom modifier in place of your Strength modifier when making Strength checks and Strength saving throws.\n- You can use the spectral arms to make unarmed strikes.\n- When you make an unarmed strike with the arms on your turn, your reach for it is 5 feet greater than normal.\n- The unarmed strikes you make with the arms can use your Wisdom modifier, or {player.WisMod}, in place of your Strength or Dexterity modifier for the attack and damage rolls, and their damage type is force.")                     
                    if monklvl >= 6:
                        player.classnotes.append("Visage of the Astral Self (see notes)")
                        player.notes.append("Visage of the Astral Self - You can summon the visage of your astral self. As a bonus action, or as part of the bonus action you take to activate Arms of the Astral Self, you can spend 1 ki point to summon this visage for 10 minutes. It vanishes early if you are incapacitated or die.\nThe spectral visage covers your face like a helmet or mask. You determine its appearance.\nWhile the spectral visage is present, you gain the following benefits.\nAstral Sight. You can see normally in darkness, both magical and nonmagical, to a distance of 120 feet.\nWisdom of the Spirit. You have advantage on Wisdom (Insight) and Charisma (Intimidation) checks.\nWord of the Spirit. When you speak, you can direct your words to a creature of your choice that you can see within 60 feet of you, making it so only that creature can hear you. Alternatively, you can amplify your voice so that all creatures within 600 feet can hear you.")                     
                    if monklvl >= 11:
                        player.classnotes.append("Awakening of the Astral Self (see notes)")
                        player.notes.append(f"Awakening of the Astral Self - When you have both your astral arms and visage summoned, you can cause the body of your astral self to appear (no action required). This spectral body covers your physical form like a suit of armor, connecting with the arms and visage. You determine its appearance.\nWhile the spectral body is present, you gain the following benefits.\nDeflect Energy - When you take acid, cold, fire, force, lightning, or thunder damage, you can use your reaction to deflect it. When you do so, the damage you take is reduced by 1d10 + your Wisdom modifier, or reduced by 1d10 + {player.WisMod}, minimum reduction of 1.\nEmpowered Arms - Once on each of your turns when you hit a target with the Arms of the Astral Self, you can deal extra damage to the target equal to your Martial Arts die.")                     
                    if monklvl >= 17:
                        player.classnotes.append("Complete Astral Self (see notes)")
                        player.notes.append("Complete Astral Self - Your connection to your astral self is complete, allowing you to unleash its full potential. As a bonus action, you can spend 5 ki points to summon the arms, visage, and body of your astral self and awaken it for 10 minutes. This awakening ends early if you are incapacitated or die.\nWhile your astral self is awakened, you gain the following benefits.\nArmor of the Spirit. You gain a +2 bonus to Armor Class.\nAstral Barrage. Whenever you use the Extra Attack feature to attack twice, you can instead attack three times if all the attacks are made with your astral arms.") 
                if player.subclass[i] == "Way of the Cobalt Soul Monk":
                    WCSMSkillsList = [
                        dnd_tools.skills["Arcana"], 
                        dnd_tools.skills["History"], 
                        dnd_tools.skills["Investigation"], 
                        dnd_tools.skills["Nature"], 
                        dnd_tools.skills["Religion"]
                        ]
                    player.classnotes.append("Extract Aspects (see notes)")
                    player.notes.append("Extract Aspects - You can strike pressure points to intuit crucial information about a foe. When you hit a creature with one of the attacks granted by your Flurry of Blows, you can analyze it. Whenever an analyzed creature misses you with an attack, you can immediately use your reaction to make an unarmed strike against that creature if it's within your reach. This benefit lasts until you finish a short or long rest.\nAdditionally, when you analyze a creature, you learn all of its damage vulnerabilities, damage resistances, damage immunities, and condition immunities.") 
                    if monklvl >= 6:
                        player.classnotes.append("Extort Truth (see notes)")
                        player.notes.append("Extort Truth - You can precisely strike a hidden cluster of nerves on a creature, temporarily preventing it from masking its true thoughts and intent. When you hit a creature with an unarmed strike, you can spend 1 ki point to force it to make a Charisma saving throw. On a failed save, the creature is unable to speak a deliberate lie, and all Charisma checks directed at the creature are made with advantage for up to 10 minutes. You know if it succeeded or failed on its saving throw.\nAn affected creature is aware of the effect and can thus avoid answering questions to which it would normally respond with a lie. Such a creature can be evasive in its answers as long as the effect lasts.\nIf you wish to impose this effect on a creature without injuring it, you can attack the creature to simply touch it, dealing no damage on a hit.") 
                        player.languages, player.slang = languagegen(param, player.languages, player.slang)
                        player.skills = oneskillfromlist(param, player.skills, WCSMSkillsList)
                        player.classnotes.append("Mystical Erudition(1) (see notes)")
                        player.notes.append("Mystical Erudition(1) - You have extensively studied the history and lore within the archives of the Cobalt Soul. You learn one language of your choice, and you gain proficiency with one of the following skills of your choice: Arcana, History, Investigation, Nature, or Religion. If you already have proficiency in one of the listed skills, you can instead choose to double your Proficiency Bonus for any ability check you make that uses the chosen proficiency (both have been addressed and added to your sheet already).\nMore languages and proficiencies are available at higher levels.") 
                    if monklvl >= 11:
                        player.languages, player.slang = languagegen(param, player.languages, player.slang)
                        player.skills = oneskillfromlist(param, player.skills, WCSMSkillsList)
                        player.notes.append("Mystical Erudition(2) - A new language and proficiency (or expertise) has been added.")
                        player.classnotes.append("Mind of Mercury - You've honed your awareness and reflexes through mental aptitude and pattern recognition. Once per turn, if you've already taken your reaction, you may spend 1 ki point to take an additional reaction. You can use only one reaction per triggering effect.")
                    if monklvl >= 17:
                        player.languages, player.slang = languagegen(param, player.languages, player.slang)
                        player.skills = oneskillfromlist(param, player.skills, WCSMSkillsList)     
                        player.notes.append("Mystical Erudition(3) - A new language and proficiency (or expertise) has been added.")                    
                        player.classnotes.append("Debilitating Barrage (see notes)")
                        player.notes.append("Debilitating Barrage - ou've gained the knowledge to manipulate a creature's ki to undermine their fortitude. When you hit a creature with an unarmed strike, you can spend 3 ki points to cause the creature to gain vulnerability to one damage type of your choice for 1 minute, or until the end of a turn in which it has taken damage of that type.\nIf a creature has resistance to the damage type you choose, this resistance is suppressed for 1 minute, rather than gaining vulnerability. A creature that is immune to the damage type you choose is unaffected. A creature who is affected by this feature cannot be affected by it again for 24 hours.") 
                if player.subclass[i] == "Way of the Drunken Master Monk":
                    if dnd_tools.skills["Performance"] not in player.skills:
                        player.skills.append(dnd_tools.skills["Performance"])
                    if dnd_tools.artisan_tools["BrewSupp"]["Name"] not in player.proficiencies:
                        player.proficiencies.append(dnd_tools.artisan_tools["BrewSupp"]["Name"])
                    player.classnotes.append("Drunken Technique - You learn how to twist and turn quickly as part of your Flurry of Blows. Whenever you use Flurry of Blows, you gain the benefit of the Disengage action, and your walking speed increases by 10 feet until the end of the current turn.")
                    if monklvl >= 6:
                        player.classnotes.append("Tipsy Sway (see notes)")
                        player.notes.append("Tipsy Sway - You can move in sudden, swaying ways. You gain the following benefits.\nLeap to Your Feet - When you're prone, you can stand up by spending 5 feet of movement, rather than half your speed.\nRedirect Attack - When a creature misses you with a melee attack roll, you can spend 1 ki point as a reaction to cause that attack to hit one creature of your choice, other than the attacker, that you can see within 5 feet of you.")
                    if monklvl >= 11:
                        player.classnotes.append("Drunkard's Luck - You always seem to get a lucky bounce at the right moment. When you make an ability check, an attack roll, or a saving throw and have disadvantage, you can spend 2 ki points to cancel the disadvantage for that roll.")
                    if monklvl >= 17:
                        player.classnotes.append("Intoxicated Frenzy (see notes)")
                        player.notes.append("Intoxicated Frenzy - You gain the ability to make an overwhelming number of attacks against a group of enemies. When you use your Flurry of Blows, you can make up to three additional attacks with it (up to a total of five Flurry of Blows attacks), provided that each Flurry of Blows attack targets a different creature this turn.")
                if player.subclass[i] == "Way of the Four Elements Monk":
                    ElementalDiscipline = 1
                    if monklvl >= 6:
                        ElementalDiscipline = 2
                    if monklvl >= 11:
                        ElementalDiscipline = 3
                    if monklvl >= 17:
                        ElementalDiscipline = 4
                    player.classnotes.append("Disciple of the Elements(1) (see notes)")
                    player.notes.append(f"Disciple of the Elements(1) - You learn magical disciplines that harness the power of the four elements. A discipline requires you to spend ki points each time you use it.\nYou know the Elemental Attunement discipline and {ElementalDiscipline} other elemental discipline(s) of your choice, from the Elemental Disciple table.\nWhenever you learn a new elemental discipline, you can also replace one elemental discipline that you already know with a different discipline.\nCasting Elemental Spells - Some elemental disciplines allow you to cast spells. To cast one of these spells, you use its casting time and other rules, but you don't need to provide material components for it.")
                    if monklvl >= 5:
                        player.classnotes.append("Disciple of the Elements(2) (see notes)")
                        player.notes.append("Disciple of the Elements(2) - You can spend additional ki points to increase the level of an elemental discipline spell that you cast, provided that the spell has an enhanced effect at a higher level, as Burning Hands does. The spell's level increases by 1 for each additional ki point you spend. For example, if you are a 5th-level monk and use Sweeping Cinder Strike to cast Burning Hands, you can spend 3 ki points to cast it as a 2nd-level spell (the discipline's base cost of 2 ki points plus 1).\nThe maximum number of ki points you can spend to cast a spell in this way (including its base ki point cost and any additional ki points you spend to increase its level) is determined by your Monk level, as mentioned in the following note.")
                        if ((monklvl >= 5) and (monklvl <= 8)):
                            SpellKi = 3
                        if ((monklvl >= 9) and (monklvl <= 12)):
                            SpellKi = 4
                        if ((monklvl >= 13) and (monklvl <= 16)):
                            SpellKi = 5
                        if ((monklvl >= 17) and (monklvl <= 20)):
                            SpellKi = 6
                        player.notes.append(f"Disciple of the Elements(3) - The amount of Ki that can be spent in this way is {SpellKi}.")
                if player.subclass[i] == "Way of the Kensei Monk":
                    toollist = [dnd_tools.artisan_tools["CallSupp"]["Name"], dnd_tools.artisan_tools["PaintSupp"]["Name"]]
                    player.proficiencies = toolprof(param, player.proficiencies, toollist)
                    player.classnotes.append("Path of the Kensei(1) (see notes)")
                    player.notes.append("Path of the Kensei(1) - Your special martial arts training leads you to master the use of certain weapons. This path also includes instruction in the deft strokes of calligraphy or painting. You gain the following benefits:\n- Kensei Weapons. Choose two types of weapons to be your kensei weapons: one melee weapon and one ranged weapon. Each of these weapons can be any simple or martial weapon that lacks the heavy and special properties. The longbow is also a valid choice. You gain proficiency with these weapons if you don't already have it. Weapons of the chosen types are monk weapons for you. Many of this tradition's features work only with your kensei weapons. More kensei weapons are available at higher levels.\n- Agile Parry. If you make an unarmed strike as part of the Attack action on your turn and are holding a kensei weapon, you can use it to defend yourself if it is a melee weapon. You gain a +2 bonus to AC until the start of your next turn, while the weapon is in your hand and you aren’t incapacitated.\n- Kensei's Shot. You can use a bonus action on your turn to make your ranged attacks with a kensei weapon more deadly. When you do so, any target you hit with a ranged attack using a kensei weapon takes an extra 1d4 damage of the weapon’s type. You retain this benefit until the end of the current turn.\n- Way of the Brush (addressed and added to proficiencies). You gain proficiency with your choice of calligrapher's supplies or painter's supplies.") 
                    if monklvl >= 6:
                        player.classnotes.append("Path of the Kensei(2) (see notes)")
                        player.notes.append("Path of the Kensei(2) - You have access to another kensei weapon, melee or ranged.")
                        player.classnotes.append("One with the Blade (see notes)")
                        player.notes.append("One with the Blade - You extend your ki into your kensei weapons, granting you the following benefits.\nMagic Kensei Weapons - Your attacks with your kensei weapons count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage.\nDeft Strike - When you hit a target with a kensei weapon, you can spend 1 ki point to cause the weapon to deal extra damage to the target equal to your Martial Arts die. You can use this feature only once on each of your turns.") 
                    if monklvl >= 11:
                        player.classnotes.append("Path of the Kensei(3) (see notes)")
                        player.notes.append("Path of the Kensei(3) - You have access to another kensei weapon, melee or ranged.")                        
                        player.classnotes.append("Sharpen the Blade (see notes)")
                        player.notes.append("Sharpen the Blade - You gain the ability to augment your weapons further with your ki. As a bonus action, you can expend up to 3 ki points to grant one kensei weapon you touch a bonus to attack and damage rolls when you attack with it. The bonus equals the number of ki points you spent. This bonus lasts for 1 minute or until you use this feature again. This feature has no effect on a magic weapon that already has a bonus to attack and damage rolls.") 
                    if monklvl >= 17:
                        player.classnotes.append("Path of the Kensei(4) (see notes)")
                        player.notes.append("Path of the Kensei(4) - You have access to another kensei weapon, melee or ranged.")                        
                        player.classnotes.append("Unerring Accuracy - Your mastery of weapons grants you extraordinary accuracy. If you miss with an attack roll using a monk weapon on your turn, you can reroll it. You can use this feature only once on each of your turns.")
                if player.subclass[i] == "Way of the Long Death Monk":
                    player.classnotes.append("Touch of Death (see notes)")
                    player.notes.append(f"Touch of Death - Your study of death allows you to extract vitality from another creature as it nears its demise. When you reduce a creature within 5 feet of you to 0 hit points, you gain temporary hit points equal to your Wisdom modifier + your Monk level, or {player.WisMod + monklvl} temporary hitpoints, minimum of 1 temporary hit point.")
                    if monklvl >= 6:
                        player.classnotes.append("Hour of Reaping (see notes)")
                        player.notes.append("Hour of Reaping - You gain the ability to unsettle or terrify those around you as an action, for your soul has been touched by the shadow of death. When you take this action, each creature within 30 feet of you that can see you must succeed on a Wisdom saving throw or be frightened of you until the end of your next turn.")
                    if monklvl >= 11:
                        player.classnotes.append("Mastery of Death - You use your familiarity with death to escape its grasp. When you are reduced to 0 hit points, you can expend 1 ki point (no action required) to have 1 hit point instead.")
                    if monklvl >= 17:
                        player.classnotes.append("Touch of the Long Death (see notes)")
                        player.notes.append("Touch of the Long Death - Your touch can channel the energy of death into a creature. As an action, you touch one creature within 5 feet of you, and you expend 1 to 10 ki points. The target must make a Constitution saving throw, and it takes 2d10 necrotic damage per ki point spent on a failed save, or half as much damage on a successful one.")
                if player.subclass[i] == "Way of Mercy Monk":
                    player.skills.append(dnd_tools.skills["Insight"])
                    player.skills.append(dnd_tools.skills["Medicine"])
                    player.proficiencies.append(dnd_tools.kits["HerbKit"]["Name"])
                    Mask1 = "Raven"
                    Mask2 = "Blank and white"
                    Mask3 = "Crying visage"
                    Mask4 = "Laughing visage"
                    Mask5 = "Skull"
                    Mask6 = "Butterfly"
                    Mask = [Mask1, Mask2, Mask3, Mask4, Mask5, Mask6]
                    MercyMask = random.choice(Mask)
                    player.classnotes.append(f"Implements of Mercy - You also gain a special mask, which you often wear when using the features of this subclass. Its appearance is determined by you or is random, which is {MercyMask}.")
                    player.classnotes.append("Hand of Healing (see notes)")
                    player.notes.append(f"Hand of Healing - Your mystical touch can mend wounds. As an action, you can spend 1 ki point to touch a creature and restore a number of hit points equal to a roll of your Martial Arts die + your Wisdom modifer, or a roll of your Martial Arts Die + {player.WisMod} hit points.\nWhen you use your Flurry of Blows, you can replace one of the unarmed strikes with a use of this feature without spending a ki point for the healing.")
                    player.classnotes.append(f"Hand of Harm - You use your ki to inflict wounds. When you hit a creature with an unarmed strike, you can spend 1 ki point to deal extra necrotic damage equal to one roll of your Martial Arts die + your Wisdom modifer, or a roll of your Martial Arts Die + {player.WisMod}. You can use this feature only once per turn.")
                    if monklvl >= 6:
                        player.classnotes.append("Physician's Touch (see notes)")
                        player.notes.append("Physician's Touch - You can administer even greater cures with a touch, and if you feel it's necessary, you can use your knowledge to cause harm.\nWhen you use Hand of Healing on a creature, you can also end one disease or one of the following conditions affecting the creature: blinded, deafened, paralyzed, poisoned, or stunned.\nWhen you use Hand of Harm on a creature, you can subject that creature to the poisoned condition until the end of your next turn.")
                    if monklvl >= 11:
                        player.classnotes.append("Flurry of Healing and Harm (see notes)")
                        player.notes.append("Flurry of Healing and Harm - You can now mete out a flurry of comfort and hurt. When you use Flurry of Blows, you can now replace each of the unarmed strikes with a use of your Hand of Healing, without spending ki points for the healing.\nIn addition, when you make an unarmed strike with Flurry of Blows, you can use Hand of Harm with that strike without spending the ki point for Hand of Harm. You can still use Hand of Harm only once per turn.")
                    if monklvl >= 17:
                        player.classnotes.append("Hand of Mercy (see notes)")
                        player.notes.append(f"Hand of Mercy - Your mastery of life energy opens the door to the ultimate mercy. As an action, you can touch the corpse of a creature that died within the past 24 hours and expend 5 ki points. The creature then returns to life, regaining a number of hit points equal to 4d10 + your Wisdom modifier, or 4d10 + {player.WisMod} hit points. If the creature died while subject to any of the following conditions, it revives with them removed: blinded, deafened, paralyzed, poisoned, and stunned.\nOnce you use this feature, you can't use it again until you finish a long rest.")
                if player.subclass[i] == "Way of the Open Hand Monk":
                    player.classnotes.append("Open Hand Technique (see notes)")
                    player.notes.append("Open Hand Technique - You can manipulate your enemy's ki when you harness your own. Whenever you hit a creature with one of the attacks granted by your Flurry of Blows, you can impose one of the following effects on that target:\n- It must succeed on a Dexterity saving throw or be knocked prone.\n- It must make a Strength saving throw. If it fails, you can push it up to 15 feet away from you.\n- It can't take reactions until the end of your next turn.")
                    if monklvl >= 6:
                        player.classnotes.append(f"Wholeness of Body - You gain the ability to heal yourself. As an action, you can regain hit points equal to three times your Monk level, or {3 * monklvl} hit points. You must finish a long rest before you can use this feature again.")
                    if monklvl >= 11:
                        player.classnotes.append("Tranquility (see notes)")
                        player.notes.append(f"Tranquility - You can enter a special meditation that surrounds you with an aura of peace. At the end of a long rest, you gain the effect of a Sanctuary spell that lasts until the start of your next long rest (the spell can end early as normal). The saving throw DC for the spell equals 8 + your Wisdom modifier + your Proficiency Bonus, or DC of {8 + player.WisMod + player.profbonus}.")
                    if monklvl >= 17:
                        player.classnotes.append("Quivering Palm (see notes)")
                        player.notes.append(f"Quivering Palm - You gain the ability to set up lethal vibrations in someone's body. When you hit a creature with an unarmed strike, you can spend 3 ki points to start these imperceptible vibrations, which last for a number of days equal to your Monk level, or {monklvl} days. The vibrations are harmless unless you use your action to end them. To do so, you and the target must be on the same plane of existence. When you use this action, the creature must make a Constitution saving throw. If it fails, it is reduced to 0 hit points. If it succeeds, it takes 10d10 necrotic damage.\nYou can have only one creature under the effect of this feature at a time. You can choose to end the vibrations harmlessly without using an action")
                if player.subclass[i] == "Way of the Shadow Monk":
                    player.classnotes.append("Shadow Arts (see notes)")
                    player.notes.append("Shadow Arts - You can use your ki to duplicate the effects of certain spells. As an action, you can spend 2 ki points to cast Darkness, Darkvision, Pass without Trace, or Silence, without providing material components. Additionally, you gain the Minor Illusion cantrip if you don't already know it.")
                    if monklvl >= 6:
                        player.classnotes.append("Shadow Step (see notes)")
                        player.notes.append("Shadow Step - You gain the ability to step from one shadow into another. When you are in dim light or darkness, as a bonus action you can teleport up to 60 feet to an unoccupied space you can see that is also in dim light or darkness. You then have advantage on the first melee attack you make before the end of the turn.")
                    if monklvl >= 11:
                        player.classnotes.append("Cloak of Shadows - You have learned to become one with the shadows. When you are in an area of dim light or darkness, you can use your action to become invisible. You remain invisible until you make an attack, cast a spell, or are in an area of bright light.")
                    if monklvl >= 17:
                        player.classnotes.append("Opportunist - You can exploit a creature's momentary distraction when it is hit by an attack. Whenever a creature within 5 feet of you is hit by an attack made by a creature other than you, you can use your reaction to make a melee attack against that creature.")
                if player.subclass[i] == "Way of the Sun Soul Monk":        
                    player.classnotes.append("Radiant Sun Bolt (see notes)")
                    player.notes.append(f"Radiant Sun Bolt - You can hurl searing bolts of magical radiance.\nYou gain a new attack option that you can use with the Attack action. This special attack is a ranged spell attack with a range of 30 feet. You are proficient with it, and you add your Dexterity modifier, or {player.DexMod}, to its attack and damage rolls. Its damage is radiant, and its damage die is a d4. This die changes as you gain Monk levels.\nWhen you take the Attack action on your turn and use this special attack as part of it, you can spend 1 ki point to make the special attack twice as a bonus action.\nWhen you gain the Extra Attack feature, this special attack can be used for any of the attacks you make as part of the Attack action.")
                    if monklvl >= 6:
                        player.classnotes.append("Searing Arc Strike (see notes)")
                        player.notes.append(f"Searing Arc Strike - You gain the ability to channel your ki into searing waves of energy. Immediately after you take the Attack action on your turn, you can spend 2 ki points to cast the Burning Hands spell as a bonus action.\nYou can spend additional ki points to cast Burning Hands as a higher level spell. Each additional ki point you spend increases the spell's level by 1. The maximum number of ki points (2 plus any additional points) that you can spend on the spell equals half your Monk level, rounded down, or {math.floor(monklvl/2)} Ki Points.")                        
                    if monklvl >= 11:
                        player.classnotes.append("Searing Sunburst (see notes)")
                        player.notes.append("Searing Sunburst - You gain the ability to create an orb of light that erupts into a devastating explosion. As an action, you magically create an orb and hurl it at a point you choose within 150 feet, where it erupts into a sphere of radiant light for a brief but deadly instant.\nEach creature in that 20-foot-radius sphere must succeed on a Constitution saving throw or take 2d6 radiant damage. A creature doesn't need to make the save if the creature is behind total cover that is opaque.\nYou can increase the sphere's damage by spending ki points. Each point you spend, up to a maximum of 3, increases the damage by 2d6.") 
                    if monklvl >= 17:
                        player.classnotes.append("Sun Shield (see notes)")
                        player.notes.append(f"Sun Shield - You become wreathed in a luminous, magical aura. You shed bright light in a 30-foot radius and dim light for an additional 30 feet. You can extinguish or restore the light as a bonus action.\nIf a creature hits you with a melee attack while this light shines, you can use your reaction to deal radiant damage to the creature. The radiant damage equals 5 + your Wisdom modifer, or {5 + player.WisMod} radiant damage.") 
            KiPoints = 3
            player.classnotes.append("Deflect Missiles (see notes)")
            player.notes.append(f"Deflect Missiles - You can use your reaction to deflect or catch the missile when you are hit by a ranged weapon attack. When you do so, the damage you take from the attack is reduced by 1d10 + your Dexterity modifier + your Monk level, or reduction of 1d10 + {player.DexMod + monklvl}.\nIf you reduce the damage to 0, you can catch the missile if it is small enough for you to hold in one hand and you have at least one hand free. If you catch a missile in this way, you can spend 1 ki point to make a ranged attack with the weapon or piece of ammunition you just caught, as part of the same reaction. You make this attack with proficiency, regardless of your weapon proficiencies, and the missile counts as a monk weapon for the attack, which has a normal range of 20 feet and a long range of 60 feet.")
            player.classnotes.append("Ki-fueled Attack - If you spend 1 ki point or more as part of your action on your turn, you can make one attack with an unarmed strike or a monk weapon as a bonus action before the end of the turn.")
            if monklvl >= 4:
                KiPoints = 4
                player.classnotes.append(f"Slow Fall - You can use your reaction when you fall to reduce any falling damage you take by an amount equal to five times your Monk level, or {5 * monklvl}.")
                player.classnotes.append(f"Quickened Healing - As an action, you can spend 2 ki points and roll a Martial Arts die. You regain a number of hit points equal to the number rolled plus your Proficiency Bonus, or plus {player.profbonus} Hit Points.")
            if monklvl >= 5:
                KiPoints = 5
                MartialArts = "1d6"
                player.classnotes.append("Extra Attack - You can attack twice, instead of once, whenever you take the Attack action on your turn.")
                player.classnotes.append("Stunning Strike (see notes)")
                player.notes.append("Stunning Strike - You can interfere with the flow of ki in an opponent’s body. When you hit another creature with a melee weapon attack, you can spend 1 ki point to attempt a stunning strike. The target must succeed on a Constitution saving throw or be stunned until the end of your next turn.")
                player.classnotes.append("Focused Aim - When you miss with an attack roll, you can spend 1 to 3 ki points to increase your attack roll by 2 for each of these ki points you spend, potentially turning the miss into a hit.")
            if monklvl >= 6:
                KiPoints = 6
                UnarmoredMovement = "15"
                player.classnotes.append("Ki-Empowered Strikes - Your unarmed strikes count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage.")
            if monklvl >= 7:
                KiPoints = 7
                player.classnotes.append("Evasion (see notes)")
                player.notes.append("Evasion - Your instinctive agility lets you dodge out of the way of certain area effects, such as a blue dragon’s lightning breath or a fireball spell. When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw, and only half damage if you fail.")
                player.classnotes.append("Stillness of Mind - You can use your action to end one effect on yourself that is causing you to be charmed or frightened.")
            if monklvl >= 8:
                KiPoints = 8
            if monklvl >= 9:
                KiPoints = 9
            if monklvl >= 10:
                KiPoints = 10
                UnarmoredMovement = "20"
                player.classnotes.append("Purity of Body - Your mastery of the ki flowing through you makes you immune to disease and poison.")
            if monklvl >= 11:
                KiPoints = 11
                MartialArts = "1d8"
            if monklvl >= 12:
                KiPoints = 12
            if monklvl >= 13:
                KiPoints = 13
                player.classnotes.append("Tongue of the Sun and Moon - You learn to touch the ki of other minds so that you understand all spoken languages. Moreover, any creature that can understand a language can understand what you say.")
            if monklvl >= 14:
                KiPoints = 14
                UnarmoredMovement = "25"
                player.classnotes.append("Diamond Soul - Your mastery of ki grants you proficiency in all saving throws.\nAdditionally, whenever you make a saving throw and fail, you can spend 1 ki point to reroll it and take the second result.")
            if monklvl >= 15:
                KiPoints = 15
                player.classnotes.append("Timeless Body - Your ki sustains you so that you suffer none of the frailty of old age, and you can’t be aged magically. You can still die of old age, however. In addition, you no longer need food or water.")
            if monklvl >= 16:
                KiPoints = 16
            if monklvl >= 17:
                KiPoints = 17
                MartialArts = "1d10"
            if monklvl >= 18:
                KiPoints = 18
                UnarmoredMovement = "30"
                player.classnotes.append("Empty Body (see notes)")
                player.notes.append("Empty Body - You can use your action to spend 4 ki points to become invisible for 1 minute. During that time, you also have resistance to all damage but force damage.\nAdditionally, you can spend 8 ki points to cast the Astral Projection spell, without needing material components. When you do so, you can’t take any other creatures with you.")
            if monklvl >= 19:
                KiPoints = 19
            if monklvl == 20:
                KiPoints = 20   
                player.classnotes.append("Perfect Self - When you roll for initiative and have no ki points remaining, you regain 4 ki points.")   
            player.classnotes.append("Martial Arts (see notes)")
            player.notes.append(f"Martial Arts - Your practice of martial arts gives you mastery of combat styles that use unarmed strikes and monk weapons, which are shortswords and any simple melee weapons that don’t have the two-handed or heavy property.\nYou gain the following benefits while you are unarmed or wielding only monk weapons and you aren’t wearing armor or wielding a shield:\n- You can use Dexterity instead of Strength for the attack and damage rolls of your unarmed strikes and monk weapons.\n- You can roll a {MartialArts} in place of the normal damage of your unarmed strike or monk weapon.\n- When you use the Attack action with an unarmed strike or a monk weapon on your turn, you can make one unarmed strike as a bonus action. For example, if you take the Attack action and attack with a quarterstaff, you can also make an unarmed strike as a bonus action, assuming you haven’t already taken a bonus action this turn.\nCertain monasteries use specialized forms of the monk weapons. For example, you might use a club that is two lengths of wood connected by a short chain (called a nunchaku) or a sickle with a shorter, straighter blade (called a kama). Whatever name you use for a monk weapon, you can use the game statistics provided for the weapon in the Weapons section.")
            if monklvl >= 2:
                player.classnotes.append("Ki (see notes)")
                player.notes.append(f"Ki - Your training allows you to harness the mystic energy of ki. Your access to this energy is represented by a number of ki points, {KiPoints}.\nYou can spend these points to fuel various ki features. You start knowing three such features: Flurry of Blows, Patient Defense, and Step of the Wind. You learn more ki features as you gain levels in this class.\nWhen you spend a ki point, it is unavailable until you finish a short or long rest, at the end of which you draw all of your expended ki back into yourself. You must spend at least 30 minutes of the rest meditating to regain your ki points.\nSome of your ki features require your target to make a saving throw to resist the feature’s effects. The saving throw DC is calculated as follows:\nKi save DC = 8 + your Proficiency Bonus + your Wisdom modifier, or DC {8 + player.profbonus + player.WisMod}.")
                player.classnotes.append("Unarmored Movement (see notes)")
                player.classnotes.append(f"Unarmored Movement(1) - Your speed increases by {UnarmoredMovement} feet while you are not wearing armor or wielding a shield.")
            if monklvl >= 9:
                player.notes.append("Unarmored Movement(2) - You gain the ability to move along vertical surfaces and across liquids on your turn without falling during the move.")  
        if player.Class[i] == "Paladin":
            if ((param == "N") or (player.singlemulticlass == "N")):
                pallvl = player.level
                player.classlvl.append(pallvl) 
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    pallvl = int(input(f"Given your pool of levels of {poollevel}, what is your Paladin level? "))      
                    if pallvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                
                poollevel = poollevel - pallvl
                player.classlvl.append(pallvl)
            if pallvl >= 1:
                player.hitdice.append(f"{pallvl}d10 for {player.Class[i]}")
                if pallvl == 1:
                    player.hitpoints += (10 + player.ConMod)
                else:
                    player.hitpoints += (10 + player.ConMod + hpcalc(pallvl, dice, 10))      
                if i == 0:
                    profs = ["Light Armor", "Medium Armor", "Heavy Armor", "Shield", "Simple Weapons", "Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)                            
                    player.skills.append(dnd_tools.saving_throws["WisST"])
                    player.skills.append(dnd_tools.saving_throws["ChaST"])
                    SkillsList = [
                        dnd_tools.skills["Athletics"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Intimidation"], 
                        dnd_tools.skills["Medicine"], 
                        dnd_tools.skills["Persuasion"], 
                        dnd_tools.skills["Religion"]
                        ]
                    player.skills = twoskillsfromlist(param, player.skills, SkillsList)      
                    StartEquip1 = ["A Martial Weapon and a Shield", "Two Martial Weapons"]
                    StartEquip2 = ["Five Javelins", "Any Simple Melee Weapon"]
                    StartEquip3 = ["Priest’s Pack", "Explorer’s Pack"]
                    if param == "Y":
                        print("0 - Random")
                        print("1 - A Martial Weapon and a Shield")
                        print("2 - Two Martial Weapons")
                        se1 = int(input("What would you like your first choice for starting equipment to be? "))
                        if se1 == 0:
                            SE1rand = random.choice(StartEquip1)
                            if SE1rand == "Martial Weapon and Shield":
                                player.equipment.append(random.choice(MartialWeapons))
                                player.equipment.append(dnd_tools.shields["Shield"].copy())
                            if SE1rand == "Two Martial Weapons":
                                MartWepRandKey1 = random.choice(MartialWeapons)
                                player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey1].copy())
                                MartWepRandKey2 = random.choice(MartialWeapons)
                                player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey2].copy())
                        if se2 == 1:
                            print("0 - Random")
                            for j, mw in enumerate(MartialWeaponsNames, 1):
                                print(f"{j} - {mw}")
                            se2mw = int(input("Which martial weapon would you like to add to your inventory? "))
                            if se2mw == 0:
                                MartWepRandKey = random.choice(MartialWeapons)
                                player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey].copy())
                            elif 1 <= se2mw <= len(MartialWeapons):
                                MartWepKey = MartialMeleeWeapons[se2mw-1]
                                player.equipment.append(dnd_tools.martial_weapons[MartWepKey].copy())
                            player.equipment.append(dnd_tools.shields["Shield"].copy())
                        if se2 == 2:
                            print("0 - Random")
                            for j, mw1 in enumerate(MartialWeaponsNames, 1):
                                print(f"{j} - {mw1}")
                            se2mw1 = int(input("Choose your first martial weapon to add to your inventory? "))
                            if se2mw1 == 0:
                                MartWepRandKey1 = random.choice(MartialWeapons)
                                player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey1].copy())
                            elif 1 <= se2mw1 <= len(MartialWeapons):
                                MartWepKey1 = MartialMeleeWeapons[se2mw1-1]
                                player.equipment.append(dnd_tools.martial_weapons[MartWepKey1].copy())                              
                            print("0 - Random")
                            for j, mw in enumerate(MartialWeaponsNames, 1):
                                print(f"{j} - {mw}")
                            se2mw2 = int(input("Choose your second martial weapon to add to your inventory? "))
                            if se2mw2 == 0:
                                MartWepRandKey2 = random.choice(MartialWeapons)
                                player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey2].copy())
                            elif 1 <= se2mw2 <= len(MartialWeapons):
                                MartWepKey2 = MartialMeleeWeapons[se2mw2-1]
                                player.equipment.append(dnd_tools.martial_weapons[MartWepKey2].copy())                                 
                        print("0 - Random")
                        print("1 - Five Javelins")
                        print("2 - Any Simple Melee Weapon")
                        se2 = int(input("What would you like your second choice for starting equipment to be? "))
                        if se2 == 0:
                            SE2rand = random.choice(StartEquip2)
                            if SE2rand == "Five Javelins":
                                for idx in range(1,5):
                                    player.equipment.append(dnd_tools.simple_weapons["Javelin"].copy())
                            if SE2rand == "Any Simple Melee Weapon":
                                SimpRandMKey = random.choice(SimpleMeleeWeapons)
                                player.equipment.append(dnd_tools.simple_weapons[SimpRandMKey].copy())
                        if se2 == 1:
                            player.equipment.append(dnd_tools.simple_weapons["Javelin"].copy())
                        if se2 == 2:
                            print("0 - Random")
                            for j, smw in enumerate(SimpleMeleeWeaponsNames, 1):
                                print(f"{j} - {smw}")
                            se2smw = int(input("Which simple melee weapon would you like to add to your inventory? "))
                            if se2smw == 0:
                                SimpRandMKey = random.choice(SimpleMeleeWeapons)
                                player.equipment.append(dnd_tools.simple_weapons[SimpRandMKey].copy())
                            elif 1 <= se2smw <= len(SimpleMeleeWeaponsNames):
                                SimpMKey = SimpleMeleeWeapons[se2smw-1]
                                player.equipment.append(dnd_tools.simple_weapons[SimpMKey].copy())  
                        print("0 - Random")
                        print("1 - A Priest's Pack")
                        print("2 - An Explorer's Pack")
                        se3 = int(input("What would you like your third choice for starting equipment to be? "))
                        if se3 == 0:
                            SE3rand = random.choice(StartEquip3)
                            if SE3rand == "Priest’s Pack":
                                player.equipment.extend(dnd_tools.packs["PriestsPack"]["contents"])
                            if SE3rand == "Explorer’s Pack":
                                player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])
                        if se3 == 1:
                            player.equipment.extend(dnd_tools.packs["PriestsPack"]["contents"])
                        if se3 == 2:
                            player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])
                        player.equipment.append(dnd_tools.heavy_armor["ChainMail"].copy())
                        player.equipment.append("A Holy Symbol")
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "Martial Weapon and Shield":
                            MartWepRandKey = random.choice(MartialWeapons)
                            player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey].copy())
                            player.equipment.append(dnd_tools.shields["Shield"].copy())
                        if SE1rand == "Two Martial Weapons":
                            MartWepRandKey1 = random.choice(MartialWeapons)
                            player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey1].copy())
                            MartWepRandKey2 = random.choice(MartialWeapons)
                            player.equipment.append(dnd_tools.martial_weapons[MartWepRandKey2].copy())
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "Five Javelins":
                            for idx in range(1,5):
                                player.equipment.append(dnd_tools.simple_weapons["Javelin"].copy())
                        if SE2rand == "Any Simple Melee Weapon":
                            SimpRandMKey = random.choice(SimpleMeleeWeapons)
                            player.equipment.append(dnd_tools.simple_weapons[SimpRandMKey].copy())
                        SE3rand = random.choice(StartEquip3)
                        if SE3rand == "Priest’s Pack":
                            player.equipment.extend(dnd_tools.packs["PriestsPack"]["contents"])
                        if SE3rand == "Explorer’s Pack":
                            player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])                            
                        player.equipment.append(dnd_tools.heavy_armor["ChainMail"].copy())
                        player.equipment.append("A Holy Symbol")    
                else:
                    profs = ["Light Armor", "Medium Armor", "Shield", "Simple Weapons", "Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)  
            player.classnotes.append("Divine Sense (see notes)")
            player.notes.append(f"Divine Sense - The presence of strong evil registers on your senses like a noxious odor, and powerful good rings like heavenly music in your ears. As an action, you can open your awareness to detect such forces. Until the end of your next turn, you know the location of any celestial, fiend, or undead within 60 feet of you that is not behind total cover. You know the type (celestial, fiend, or undead) of any being whose presence you sense, but not its identity (the vampire Count Strahd von Zarovich, for instance). Within the same radius, you also detect the presence of any place or object that has been consecrated or desecrated, as with the hallow spell.\nYou can use this feature a number of times equal to 1 + your Charisma modifier, or {1 + player.ChaMod} times. When you finish a long rest, you regain all expended uses.")
            player.classnotes.append("Lay on Hands (see notes)")
            player.notes.append(f"Lay on Hands - Your blessed touch can heal wounds. You have a pool of healing power that replenishes when you take a long rest. With that pool, you can restore a total number of hit points equal to {pallvl * 5}.\nAs an action, you can touch a creature and draw power from the pool to restore a number of hit points to that creature, up to the maximum amount remaining in your pool.\nAlternatively, you can expend 5 hit points from your pool of healing to cure the target of one disease or neutralize one poison affecting it. You can cure multiple diseases and neutralize multiple poisons with a single use of Lay on Hands, expending hit points separately for each one.\nThis feature has no effect on undead and constructs.")
            if pallvl >= 2:    
                player.spellcastingclass.append("Paladin")
                player.spellcastingability.append("Cha")
                player.spellsavedc.append(8 + player.profbonus + player.ChaMod)
                player.spellattackmod.append(player.profbonus + player.ChaMod)
                PaladinSpellSlot1 = 2
                PaladinSpellSlot2 = 0
                PaladinSpellSlot3 = 0
                PaladinSpellSlot4 = 0
                PaladinSpellSlot5 = 0 
                player.classnotes.append("Fighting Style (see notes)")
                player.notes.append(f"Fighting Style - You adopt a particular style of fighting as your specialty. Choose one of the following options. You can’t take a Fighting Style option more than once, even if you later get to choose again.\n- Blessed Warrior - You learn two cantrips of your choice from the cleric spell list. They count as paladin spells for you, and Charisma is your spellcasting ability for them. Whenever you gain a level in this class, you can replace one of these cantrips with another cantrip from the cleric spell list.\n- Blind Fighting - You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you.\n- Defense - While you are wearing armor, you gain a +1 bonus to AC.\n- Dueling - When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.\n- Great Weapon Fighting - When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit.\n- Interception - When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by 1d10 + your Proficiency Bonus, or reduction by 1d10 + {player.profbonus}, to a minimum of 0 damage. You must be wielding a shield or a simple or martial weapon to use this reaction.\n- Protection - When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.")
                player.classnotes.append("Divine Smite (see notes)")
                player.notes.append("Divine Smite - When you hit a creature with a melee weapon attack, you can expend one spell slot to deal radiant damage to the target, in addition to the weapon’s damage. The extra damage is 2d8 for a 1st-level spell slot, plus 1d8 for each spell level higher than 1st, to a maximum of 5d8. The damage increases by 1d8 if the target is an undead or a fiend, to a maximum of 6d8.")
            if pallvl >= 3:
                Pal= ["Oath of the Ancients Paladin", "Oath of Conquest Paladin", "Oath of the Crown Paladin", "Oath of Devotion Paladin", "Oath of Glory Paladin", "Oath of the Open Sea Paladin", "Oath of Redemption Paladin", "Oath of the Watchers Paladin", "Oath of Vengeance Paladin", "Oathbreaker Paladin"]
                

                if player.subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        for idx, subcl in enumerate(Pal, 1):
                            print(f"{idx} - {subcl}")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 0:
                            player.subclass[i] = random.choice(Pal)
                        elif 1 <= subc <= len(Pal):
                            player.subclass[i] = Pal[subc - 1]
                    if param == "N":
                        player.subclass[i] = random.choice(Pal)    
                PaladinOathSpells = []                 
                if player.subclass[i] == "Oath of the Ancients Paladin":
                    if pallvl >= 3:
                        PaladinOathSpells.append("Ensnaring Strike")
                        PaladinOathSpells.append("Speak with Animals")
                    if pallvl >= 5:
                        PaladinOathSpells.append("Moonbeam")
                        PaladinOathSpells.append("Misty Step")
                    if pallvl >= 9:
                        PaladinOathSpells.append("Plant Growth")
                        PaladinOathSpells.append("Protection from Energy")
                    if pallvl >= 13:
                        PaladinOathSpells.append("Ice Storm")
                        PaladinOathSpells.append("Stoneskin")
                    if pallvl >= 17:
                        PaladinOathSpells.append("Commune with Nature")
                        PaladinOathSpells.append("Tree Stride")
                    player.classnotes.append("Tenets of the Ancients (see notes)")
                    player.notes.append("Tenets of the Ancients - The tenets of the Oath of the Ancients have been preserved for uncounted centuries. This oath emphasizes the principles of good above any concerns of law or chaos. Its four central principles are simple.\nKindle the Light - Through your acts of mercy, kindness, and forgiveness, kindle the light of hope in the world, beating back despair.\nShelter the Light - Where there is good, beauty, love, and laughter in the world, stand against the wickedness that would swallow it. Where life flourishes, stand against the forces that would render it barren.\nPreserve Your Own Light - Delight in song and laughter, in beauty and art. If you allow the light to die in your own heart, you can't preserve it in the world.\nBe the Light - Be a glorious beacon for all who live in despair. Let the light of your joy and courage shine forth in all your deeds.")
                    player.classnotes.append("Channel Divinity (see notes)")
                    player.notes.append("Channel Divinity - You gain the following two Channel Divinity options.\nNature's Wrath - You can use your Channel Divinity to invoke primeval forces to ensnare a foe. As an action, you can cause spectral vines to spring up and reach for a creature within 10 feet of you that you can see. The creature must succeed on a Strength or Dexterity saving throw (its choice) or be restrained. While restrained by the vines, the creature repeats the saving throw at the end of each of its turns. On a success, it frees itself and the vines vanish.\nTurn the Faithless - You can use your Channel Divinity to utter ancient words that are painful for fey and fiends to hear. As an action, you present your holy symbol, and each fey or fiend within 30 feet of you that can hear you must make a Wisdom saving throw. On a failed save, the creature is turned for 1 minute or until it takes damage.\nA turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action.\nIf the creature's true form is concealed by an illusion, shapeshifting, or other effect, that form is revealed while it is turned.")
                    if pallvl >= 7:
                        player.classnotes.append("Aura of Warding(1) - Ancient magic lies so heavily upon you that it forms an eldritch ward. You and friendly creatures within 10 feet of you have resistance to damage from spells.")                       
                    if pallvl >= 15:
                        player.classnotes.append("Undying Sentinel (see notes)")
                        player.notes.append("Undying Sentinel - When you are reduced to 0 hit points and are not killed outright, you can choose to drop to 1 hit point instead. Once you use this ability, you can't use it again until you finish a long rest.\nAdditionally, you suffer none of the drawbacks of old age, and you can't be aged magically.")    
                    if pallvl >= 18:
                        player.classnotes.append("Aura of Warding(2) - The range of this aura increases to 30 feet.")                                                     
                    if pallvl >= 20:           
                        player.classnotes.append("Elder Champion (see notes)")
                        player.notes.append("Elder Champion - You can assume the form of an ancient force of nature, taking on an appearance you choose. For example, your skin might turn green or take on a bark-like texture, your hair might become leafy or moss-like, or you might sprout antlers or a lion-like mane.\nUsing your action, you undergo a transformation. For 1 minute, you gain the following benefits:\n- At the start of each of your turns, you regain 10 hit points.\n- Whenever you cast a paladin spell that has a casting time of 1 action, you can cast it using a bonus action instead.\n- Enemy creatures within 10 feet of you have disadvantage on saving throws against your paladin spells and Channel Divinity options.\nOnce you use this feature, you can't use it again until you finish a long rest.")                                                   
                if player.subclass[i] == "Oath of Conquest Paladin":
                    if pallvl >= 3:
                        PaladinOathSpells.append("Armor of Agathys")
                        PaladinOathSpells.append("Command")
                    if pallvl >= 5:
                        PaladinOathSpells.append("Hold Person")
                        PaladinOathSpells.append("Spiritual Weapon")
                    if pallvl >= 9:
                        PaladinOathSpells.append("Bestow Curse")
                        PaladinOathSpells.append("Fear")
                    if pallvl >= 13:
                        PaladinOathSpells.append("Dominate Beast")
                        PaladinOathSpells.append("Stoneskin")
                    if pallvl >= 17:
                        PaladinOathSpells.append("Cloudkill")
                        PaladinOathSpells.append("Dominate Person")   
                    player.classnotes.append("Tenets of Conquest (see notes)")
                    player.notes.append("Tenets of Conquest - A paladin who takes this oath has the tenets of conquest seared on the upper arm.\nDouse the Flame of Hope - It is not enough to merely defeat an enemy in battle. Your victory must be so overwhelming that your enemies’ will to fight is shattered forever. A blade can end a life. Fear can end an empire.\nRule with an Iron Fist - Once you have conquered, tolerate no dissent. Your word is law. Those who obey it shall be favored. Those who defy it shall be punished as an example to all who might follow.\nStrength Above All - You shall rule until a stronger one arises. Then you must grow mightier and meet the challenge, or fall to your own ruin.")
                    player.classnotes.append("Channel Divinity (see notes)")
                    player.notes.append("Channel Divinity - You gain the following two Channel Divinity options.\nConquering Presence - You can use your Channel Divinity to exude a terrifying presence. As an action, you force each creature of your choice that you can see within 30 feet of you to make a Wisdom saving throw. On a failed save, a creature becomes frightened of you for 1 minute. The frightened creature can repeat this saving throw at the end of each of its turns, ending the effect on itself on a success.\nGuided Strike - You can use your Channel Divinity to strike with supernatural accuracy. When you make an attack roll, you can use your Channel Divinity to gain a +10 bonus to the roll. You make this choice after you see the roll, but before the DM says whether the attack hits or misses.")
                    if pallvl >= 7:
                        player.classnotes.append("Aura of Conquest(1) (see notes)")
                        player.notes.append(f"Aura of Conquest(1) - You constantly emanate a menacing aura while you’re not incapacitated. The aura extends 10 feet from you in every direction, but not through total cover.\nIf a creature is frightened of you, its speed is reduced to 0 while in the aura, and that creature takes psychic damage equal to half your Paladin Proficiency Bonus, rounded down, or {math.floor(pallvl/2)} psychic damage, if it starts its turn there.")                        
                    if pallvl >= 15:
                        player.classnotes.append(f"Scornful Rebuke - Those who dare to strike you are psychically punished for their audacity. Whenever a creature hits you with an attack, that creature takes psychic damage equal to your Charisma modifier, or {player.ChaMod} psychic damage, minimum of 1, if you’re not incapacitated.")  
                    if pallvl >= 18:
                        player.classnotes.append("Aura of Conquest(2) (see notes)")
                        player.notes.append("Aura of Conquest(2) - The range of this aura increases to 30 feet.")                                                       
                    if pallvl >= 20:           
                        player.classnotes.append("Invincible Conqueror (see notes)")
                        player.notes.append("Invincible Conqueror - You gain the ability to harness extraordinary martial prowess. As an action, you can magically become an avatar of conquest, gaining the following benefits for 1 minute:\n- You have resistance to all damage.\n- When you take the Attack action on your turn, you can make one additional attack as part of that action.\n- Your melee weapon attacks score a critical hit on a roll of 19 or 20 on the d20.\nOnce you use this feature, you can’t use it again until you finish a long rest.")                                         
                if player.subclass[i] == "Oath of the Crown Paladin":
                    if pallvl >= 3:
                        PaladinOathSpells.append("Command")
                        PaladinOathSpells.append("Compelled Duel")
                    if pallvl >= 5:
                        PaladinOathSpells.append("Warding Bond")
                        PaladinOathSpells.append("Zone of Truth")
                    if pallvl >= 9:
                        PaladinOathSpells.append("Aura of Vitality")
                        PaladinOathSpells.append("Spirit Guardians")
                    if pallvl >= 13:
                        PaladinOathSpells.append("Banishment")
                        PaladinOathSpells.append("Guardian of Faith")
                    if pallvl >= 17:
                        PaladinOathSpells.append("Circle of Power")
                        PaladinOathSpells.append("Geas")            
                    player.classnotes.append("Tenets of the Crown (see notes)")
                    player.notes.append("Tenets of the Crown - The tenets of the Oath of the Crown are often set by the sovereign to which their oath is sworn, but generally emphasize the following tenets.\nLaw - The law is paramount. It is the mortar that holds the stones of civilization together, and it must be respected.\nLoyalty - Your word is your bond. Without loyalty, oaths and laws are meaningless.\nCourage - You must be willing to do what needs to be done for the sake of order, even in the face of overwhelming odds. If you don't act, then who will?\nResponsibility - You must deal with the consequences of your actions, and you are responsible for fulfilling your duties and obligations.")
                    player.classnotes.append("Channel Divinity (see notes)")
                    player.notes.append(f"Channel Divinity - You gain the following two Channel Divinity options.\nChampion Challenge - As a bonus action, you issue a challenge that compels other creatures to do battle with you. Each creature of your choice that you can see within 30 feet of you must make a Wisdom saving throw. On a failed save, a creature can't willingly move more than 30 feet away from you. This effect ends on the creature if you are incapacitated or die or if the creature is more than 30 feet away from you.\nTurn the Tide - As a bonus action, you can bolster injured creatures with your Channel Divinity. Each creature of your choice that can hear you within 30 feet of you regains hit points equal to 1d6 + your Charisma modifier, or 1d6 + {player.ChaMod} hit points, minimum of 1, if it has no more than half of its hit points.")
                    if pallvl >= 7:
                        player.classnotes.append("Divine Allegiance (see notes)")
                        player.notes.append("Divine Allegiance - When a creature within 5 feet of you takes damage, you can use your reaction to magically substitute your own health for that of the target creature, causing that creature not to take the damage. Instead, you take the damage. This damage to you can't be reduced or prevented in any way.")                        
                    if pallvl >= 15:
                        player.classnotes.append("Unyielding Saint - You have advantage on saving throws to avoid becoming paralyzed or stunned.")                              
                    if pallvl >= 20:           
                        player.classnotes.append("Exalted Champion (see notes)")
                        player.notes.append("Exalted Champion - Your presence on the field of battle is an inspiration to those dedicated to your cause. You can use your action to gain the following benefits for 1 hour:\n- You have resistance to bludgeoning, piercing, and slashing damage from nonmagical weapons.\n- Your allies have advantage on death saving throws while within 30 feet of you.\n- You have advantage on Wisdom saving throws, as do your allies within 30 feet of you.\nThis effect ends early if you are incapacitated or die. Once you use this feature, you can't use it again until you finish a long rest.")                                    
                if player.subclass[i] == "Oath of Devotion Paladin":
                    if pallvl >= 3:
                        PaladinOathSpells.append("Protection from Evil and Good")
                        PaladinOathSpells.append("Sanctuary")
                    if pallvl >= 5:
                        PaladinOathSpells.append("Lesser Restoration")
                        PaladinOathSpells.append("Zone of Truth")
                    if pallvl >= 9:
                        PaladinOathSpells.append("Beacon of Hope")
                        PaladinOathSpells.append("Dispel Magic")
                    if pallvl >= 13:
                        PaladinOathSpells.append("Freedom of Movement")
                        PaladinOathSpells.append("Guardian of Faith")
                    if pallvl >= 17:
                        PaladinOathSpells.append("Commune")
                        PaladinOathSpells.append("Flame Strike")   
                    player.classnotes.append("Tenets of Devotion (see notes)")
                    player.notes.append("Tenets of Devotion - Though the exact words and strictures of the Oath of Devotion vary, paladins of this oath share these tenets.\nHonesty - Don't lie or cheat. Let your word be your promise.\nCourage - Never fear to act, though caution is wise.\nCompassion - Aid others, protect the weak, and punish those who threaten them. Show mercy to your foes, but temper it with wisdom.\nHonor - Treat others with fairness, and let your honorable deeds be an example to them. Do as much good as possible while causing the least amount of harm.\nDuty - Be responsible for your actions and their consequences, protect those entrusted to your care, and obey those who have just authority over you.")
                    player.classnotes.append("Channel Divinity (see notes)")
                    player.notes.append(f"Channel Divinity - You gain the following two Channel Divinity options.\nSacred Weapon - As an action, you can imbue one weapon that you are holding with positive energy, using your Channel Divinity. For 1 minute, you add your Charisma modifier, or {player.ChaMod}, to attack rolls made with that weapon, with a minimum bonus of +1. The weapon also emits bright light in a 20-foot radius and dim light 20 feet beyond that. If the weapon is not already magical, it becomes magical for the duration.\nYou can end this effect on your turn as part of any other action. If you are no longer holding or carrying this weapon, or if you fall unconscious, this effect ends.\nTurn the Unholy - As an action, you present your holy symbol and speak a prayer censuring fiends and undead, using your Channel Divinity. Each fiend or undead that can see or hear you within 30 feet of you must make a Wisdom saving throw. If the creature fails its saving throw, it is turned for 1 minute or until it takes damage.\nA turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action.")
                    if pallvl >= 7:
                        player.classnotes.append("Aura of Devotion(1) - You and friendly creatures within 10 feet of you can't be charmed while you are conscious.")                      
                    if pallvl >= 15:
                        player.classnotes.append("Purity of Spirit - You are always under the effects of a Protection from Evil and Good spell.")
                    if pallvl >= 18:
                        player.classnotes.append("Aura of Devotion(2) - The range of this aura increases to 30 feet.")                                                        
                    if pallvl >= 20:           
                        player.classnotes.append("Holy Nimbus (see notes)")
                        player.notes.append("Holy Nimbus - You can emanate an aura of sunlight. For 1 minute, bright light shines from you in a 30-foot radius, and dim light shines 30 feet beyond that.\nWhenever an enemy creature starts its turn in the bright light, the creature takes 10 radiant damage.\nIn addition, for the duration, you have advantage on saving throws against spells cast by fiends or undead.\nOnce you use this feature, you can't use it again until you finish a long rest.")                                        
                if player.subclass[i] == "Oath of Glory Paladin":
                    if pallvl >= 3:
                        PaladinOathSpells.append("Guiding Bolt")
                        PaladinOathSpells.append("Heroism")
                    if pallvl >= 5:
                        PaladinOathSpells.append("Enhance Ability")
                        PaladinOathSpells.append("Magic Weapon")
                    if pallvl >= 9:
                        PaladinOathSpells.append("Haste")
                        PaladinOathSpells.append("Protection From Energy")
                    if pallvl >= 13:
                        PaladinOathSpells.append("Compulsion")
                        PaladinOathSpells.append("Freedom of Movement")
                    if pallvl >= 17:
                        PaladinOathSpells.append("Commune")
                        PaladinOathSpells.append("Flame Strike")
                    player.classnotes.append("Tenets of Glory (see notes)")
                    player.notes.append("Tenets of Glory - The tenets of the Oath of Glory drive a paladin to attempt heroics that might one day shine in legend.\nActions over Words - Strive to be known by glorious deeds, not words.\nChallenges Are but Tests - Face hardships with courage, and encourage your allies to face them with you.\nHone the Body - Like raw stone, your body must be worked so its potential can be realized.\nDiscipline the Soul - You must marshal the discipline to overcome failings within yourself that threaten to dim the glory of you and your friends.")
                    player.classnotes.append("Channel Divinity (see notes)")
                    player.notes.append(f"Channel Divinity - You gain the following two Channel Divinity options.\nPeerless Athlete - As a bonus action, you can use your Channel Divinity to augment your athleticism. For the next 10 minutes, you have advantage on Strength (Athletics) and Dexterity (Acrobatics) checks; you can carry, push, drag, and lift twice as much weight as normal; and the distance of your long and high jumps increases by 10 feet (this extra distance costs movement as normal).\nInspiring Smite - Immediately after you deal damage to a creature with your Divine Smite feature, you can use your Channel Divinity as a bonus action and distribute temporary hit points to creatures of your choice within 30 feet of you, which can include you. The total number of temporary hit points equals 2d8 + your Paladin level, or 2d8 + {pallvl} temporary hit points, divided among the chosen creatures however you like.")
                    if pallvl >= 7:
                        player.classnotes.append("Aura of Alacrity(1) (see notes)")
                        player.notes.append("Aura of Alacrity(1) - You emanate an aura that fills you and your companions with supernatural speed, allowing you to race across a battlefield in formation. Your walking speed increases by 10 feet. In addition, if you aren't incapacitated, the walking speed of any ally who starts their turn within 5 feet of you increases by 10 feet until the end of that turn.")                        
                    if pallvl >= 15:
                        player.classnotes.append("Glorious Defense (see notes)")
                        player.notes.append(f"Glorious Defense - You can turn defense into a sudden strike. When you or another creature you can see within 10 feet of you is hit by an attack roll, you can use your reaction to grant a bonus to the target's AC against that attack, potentially causing it to miss. The bonus equals your Charisma modifier, or {player.ChaMod}, minimum of + 1. If the attack misses, you can make one weapon attack against the attacker as part of this reaction, provided the attacker is within your weapon's range.\nYou can use this feature a number of times equal to your Charisma modifier, or {player.ChaMod} times, minimum of once, and you regain all expended uses when you finish a long rest.")     
                    if pallvl >= 18:
                        player.classnotes.append("Aura of Alacrity(2) (see notes)")
                        player.notes.append("Aura of Alacrity(2) - The range of the aura increases to 10 feet.")                                                    
                    if pallvl >= 20:           
                        player.classnotes.append("Living Legend (see notes)")
                        player.notes.append("Living Legend - You can empower yourself with the legends-whether true or exaggerated-of your great deeds. As a bonus action, you gain the following benefits for 1 minute:\n- You are blessed with an otherworldly presence, gaining advantage on all Charisma checks.\n- Once on each of your turns when you make a weapon attack and miss, you can cause that attack to hit instead.\n- If you fail a saving throw, you can use your reaction to reroll it. You must use this new roll.\nOnce you use this feature, you can't use it again until you finish a long rest, unless you expend a 5th-level spell slot to use it again.")                     
                if player.subclass[i] == "Oath of the Open Sea Paladin":
                    if pallvl >= 3:
                        PaladinOathSpells.append("Create or Destroy Water")
                        PaladinOathSpells.append("Expeditious Retreat")
                    if pallvl >= 5:
                        PaladinOathSpells.append("Augury")
                        PaladinOathSpells.append("Misty Step")
                    if pallvl >= 9:
                        PaladinOathSpells.append("Call Lightning")
                        PaladinOathSpells.append("Freedom of the Waves")
                    if pallvl >= 13:
                        PaladinOathSpells.append("Control Water")
                        PaladinOathSpells.append("Freedom of Movement")
                    if pallvl >= 17:
                        PaladinOathSpells.append("Commune with Nature")
                        PaladinOathSpells.append("Freedom of the Winds")
                    player.classnotes.append("Tenets of the Open Sea (see notes)")
                    player.notes.append("Tenets of the Open Sea - Freedom can be a selfless virtue or a selfish want. For paladins who swear the Oath of the Open Sea, freedom is the highest calling, and a gift to be granted to all.\nNo Greater Life than a Life Lived Free - One should be free to chart their own path without oppression. Those who would exert their power to dominate others shall be smote.\nTrust the Skies - The guidance of a strong breeze. The rumbling warnings of a coming storm. Nature is a source of portent and council that should be heeded.\nAdapt Like the Water - The waters of the ocean can shift around any obstacle—or become the most impassable obstacle of all. They carve away the land to reveal the secrets of the past, or swallow the truth and hide it forever. To embrace this fluidity is to be ready for any challenge.\nExplore the Uncharted - The world is filled with mystery. Through the pursuit of enigmatic ends, one can uncover those who hide their foul deeds, and find the path to becoming something great.")
                    player.classnotes.append("Channel Divinity (see notes)")
                    player.notes.append(f"Channel Divinity - You gain the following two Channel Divinity options.\nMarine Layer - As an action, you channel the sea to create a thick cloud of fog that surrounds you for 20 feet in all directions. The fog moves with you, remaining centered on you and making its area heavily obscured. You and each creature within 5 feet of you instead treat the area as lightly obscured. This fog lasts for 10 minutes, spreads around corners, and cannot be dispersed unless you choose to end this effect (no action required).\nFury of the Tides - As a bonus action, you channel the powerful might of the waves to bolster your attacks for 1 minute. Once per turn for the duration, when you hit a creature with a weapon attack, you can choose to push the target 10 feet away from you. If pushed into an obstacle or another creature, the target takes bludgeoning damage equal to your Charisma modifier, or {player.ChaMod} bludgeoning damage.")
                    player.notes.append("Rules Tip: Visibility - Fog and other effects can obscure vision for you, your enemies, and your allies. When you heavily obscure an area using your Marine Layer Channel Divinity option, all creatures within the area have their vision completely blocked, and creatures outside the area can't see in. Creatures that can't see automatically fail ability checks that require sight. Also, attack rolls against creatures that can't see have advantage, and their own attack rolls have disadvantage.\nCreatures in a lightly obscured area have disadvantage only on Wisdom (Perception) checks that rely on sight. The rules for when your vision is obscured are described completely in the fifth edition core rules.")
                    if pallvl >= 7:
                        player.classnotes.append("Aura of Liberation(1) (see notes)")
                        player.notes.append("Aura of Liberation(1) - You fill nearby creatures with the energy of movement. While you're not incapacitated, you and creatures of your choice within 10 feet of you cannot be grappled or restrained, and ignore penalties on movement and attacks while underwater. Creatures that are already grappled or restrained when they enter the aura can spend 5 feet of movement to automatically escape unless they are bound by magic restraints.")                        
                    if pallvl >= 15:
                        player.classnotes.append("Stormy Waters (see notes)")
                        player.notes.append(f"Stormy Waters - You can call on the force of crashing waters as a reaction whenever a creature moves into or out of your reach. The creature takes 1d12 bludgeoning damage and must succeed on a Strength saving throw against your spell save DC, or against {player.spellsavedc[i]}, or be knocked prone.")    
                    if pallvl >= 18:
                        player.classnotes.append("Aura of Liberation(2) (see notes)")
                        player.notes.append("Aura of Liberation(2) - The aura affects creatures within 30 feet of you.")                                                     
                    if pallvl >= 20:           
                        player.classnotes.append("Mythic Swashbuckler (see notes)")
                        player.notes.append("Mythic Swashbuckler - You learn to channel the spirits of historic sea captains to briefly become a paragon of heroic adventure. As an action, you embrace these spirits of the sea to gain the following benefits for 1 minute:\n- You have advantage on Strength (Athletics) checks and you gain a climbing speed equal to your walking speed. If you already have a climbing speed, it is doubled.\n- If you are within 5 feet of a creature and no other creatures are within 5 feet of you, you have advantage on attack rolls against that creature.\n- You can take the Dash or Disengage action as a bonus action.\n- You have advantage on Dexterity checks and Dexterity saving throws against effects you can see.\nOnce you use this feature, you can't use it again until you finish a long rest.")                                   
                if player.subclass[i] == "Oath of Redemption Paladin":
                    if pallvl >= 3:
                        PaladinOathSpells.append("Sanctuary")
                        PaladinOathSpells.append("Sleep")
                    if pallvl >= 5:
                        PaladinOathSpells.append("Calm Emotions")
                        PaladinOathSpells.append("Hold Person")
                    if pallvl >= 9:
                        PaladinOathSpells.append("Counterspell")
                        PaladinOathSpells.append("Hypnotic Pattern")
                    if pallvl >= 13:
                        PaladinOathSpells.append("Otiluke's Resilient Sphere")
                        PaladinOathSpells.append("Stoneskin")
                    if pallvl >= 17:
                        PaladinOathSpells.append("Hold Monster")
                        PaladinOathSpells.append("Wall of Force")  
                    player.classnotes.append("Tenets of Redemption (see notes)")
                    player.notes.append("Tenets of Redemption - The tenets of the Oath of Redemption hold a paladin to a high standard of peace and justice.\nPeace - Violence is a weapon of last resort. Diplomacy and understanding are the paths to long-lasting peace.\nInnocence - All people begin life in an innocent state, and it is their environment or the influence of dark forces that drives them to evil. By setting the proper example, and working to heal the wounds of a deeply flawed world, you can set anyone on a righteous path.\nPatience - Change takes time. Those who have walked the path of the wicked must be given reminders to keep them honest and true. Once you have planted the seed of righteousness in a creature, you must work day after day to allow it to survive and then flourish.\nWisdom - Your heart and mind must stay clear, for eventually you will be forced to admit defeat. While every creature can be redeemed, some are so far along the path of evil that you have no choice but to end their lives for the greater good. Any such action must be carefully weighed and the consequences fully understood, but once you have made the decision, follow through with it knowing your path is just.")
                    player.classnotes.append("Channel Divinity (see notes)")
                    player.notes.append("Channel Divinity - You gain the following two Channel Divinity options.\nEmissary of Peace - You can use your Channel Divinity to augment your presence with divine power. As a bonus action, you grant yourself a +5 bonus to Charisma (Persuasion) checks for the next 10 minutes.\nRebuke the Violent - You can use your Channel Divinity to rebuke those who use violence. Immediately after an attacker within 30 feet of you deals damage with an attack against a creature other than you, you can use your reaction to force the attacker to make a Wisdom saving throw. On a failed save, the attacker takes radiant damage equal to the damage it just dealt. On a successful save, it takes half as much damage.")
                    if pallvl >= 7:
                        player.classnotes.append("Aura of the Guardian(1) (see notes)")
                        player.notes.append("Aura of the Guardian(1) - You can shield your allies from harm at the cost of your own health. When a creature within 10 feet of you takes damage, you can use your reaction to magically take that damage, instead of that creature taking it. This feature doesn't transfer any other effects that might accompany the damage, and this damage can't be reduced in any way.")                        
                    if pallvl >= 15:
                        player.classnotes.append("Protective Spirit (see notes)")
                        player.notes.append(f"Protective Spirit - A holy presence mends your wounds in combat. You regain hit points equal to 1d6 + half your Paladin level, or 1d6 + {math.ceil(pallvl/2)} hit points, if you end your turn in combat with fewer than half of your hit points remaining and you aren’t incapacitated.")   
                    if pallvl >= 18:
                        player.classnotes.append("Aura of the Guardian(2) (see notes)")
                        player.notes.append("Aura of the Guardian(2) - The range of this aura increases to 30 feet.")                                                      
                    if pallvl >= 20:           
                        player.classnotes.append("Emissary of Redemption (see notes)")
                        player.notes.append("Emissary of Redemption - You become an avatar of peace, which gives you the following benefits.\n- You have resistance to all damage dealt by other creatures (their attacks, spells, and other effects).\n- Whenever a creature damages you, it takes radiant damage equal to half the amount it dealt to you.\nIf you attack a creature, cast a spell on it, or deal damage to it by any means but this feature, neither benefit works against that creature until you finish a long rest.")                                   
                if player.subclass[i] == "Oath of the Watchers Paladin":
                    if pallvl >= 3:
                        PaladinOathSpells.append("Alarm")
                        PaladinOathSpells.append("Detect Magic")
                    if pallvl >= 5:
                        PaladinOathSpells.append("Moonbeam")
                        PaladinOathSpells.append("See Invisibility")
                    if pallvl >= 9:
                        PaladinOathSpells.append("Counterspell")
                        PaladinOathSpells.append("Nondetection")
                    if pallvl >= 13:
                        PaladinOathSpells.append("Aura of Purity")
                        PaladinOathSpells.append("Banishment")
                    if pallvl >= 17:
                        PaladinOathSpells.append("Hold Monster")
                        PaladinOathSpells.append("Scrying")    
                    player.classnotes.append("Tenets of the Watchers (see notes)")
                    player.notes.append("Tenets of the Watchers - A paladin who assumes the Oath of the Watchers swears to safeguard mortal realms from otherworldly threats.\nVigilance - The threats you face are cunning, powerful, and subversive. Be ever alert for their corruption.\nLoyalty - Never accept gifts or favors from fiends or those who truck with them. Stay true to your order, your comrades, and your duty.\nDiscipline - You are the shield against the endless terrors that lie beyond the stars. Your blade must be forever sharp and your mind keen to survive what lies beyond.")
                    player.classnotes.append("Channel Divinity (see notes)")
                    player.notes.append(f"Channel Divinity - You gain the following Channel Divinity options.\nWatcher's Will - You can use your Channel Divinity to invest your presence with the warding power of your faith. As an action, you can choose a number of creatures you can see within 30 feet of you, up to a number equal to your Charisma modifier, or {player.ChaMod} creatures, minimum of one creature. For 1 minute, you and the chosen creatures have advantage on Intelligence, Wisdom, and Charisma saving throws.\nAbjure the Extraplanar - You can use your Channel Divinity to castigate unworldly beings. As anaction, you present your holy symbol and each aberration, celestial, elemental, fey, or fiend within 30 feet of you that can hear you must make a Wisdom saving throw. On a failed save, the creature is turned for 1 minute or until it takes damage.\nA turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly end its move in a space within 30 feet of you. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can take the Dodge action.")
                    if pallvl >= 7:
                        player.classnotes.append(f"Aura of the Sentinel(1) - You emit an aura of alertness while you aren't incapacitated. When you and any creatures of your choice within 10 feet of you roll initiative, you all gain a bonus to initiative equal to your Proficiency Bonus, or a bonus of {player.profbonus}.")
                    if pallvl >= 15:
                        player.classnotes.append("Vigilant Rebuke (see notes)")
                        player.notes.append(f"Vigilant Rebuke - You've learned how to chastise anyone who dares wield beguilements against you and your wards. Whenever you or a creature you can see within 30 feet of you succeeds on an Intelligence, a Wisdom, or a Charisma saving throw, you can use your reaction to deal 2d8 + your Charisma modifier, or 2d8 + {player.ChaMod} force damage, to the creature that forced the saving throw.")  
                    if pallvl >= 18:
                        player.classnotes.append("Aura of the Sentinel(2) - The range of this aura increases to 30 feet.")                                                       
                    if pallvl >= 20:           
                        player.classnotes.append("Mortal Bulwark (see notes)")
                        player.notes.append(f"Mortal Bulwark - You manifest a spark of divine power in defense of the mortal realms. As a bonus action, you gain the following benefits for 1 minute:\n- You gain truesight with a range of 120 feet.\n- You have advantage on attack rolls against aberrations, celestials, elementals, fey, and fiends.\nWhen you hit a creature with an attack roll and deal damage to it, you can also force it to make a Charisma saving throw against your spell save DC, or against {player.spellsavedc[i]}. On a failed save, the creature is magically banished to its native plane of existence if it's currently not there. On a successful save, the creature can't be banished by this feature for 24 hours. Once you use this bonus action, you can't use it again until you finish a long rest, unless you expend a 5th-level spell slot to use it again.")             
                if player.subclass[i] == "Oath of Vengeance Paladin":
                    if pallvl >= 3:
                        PaladinOathSpells.append("Bane")
                        PaladinOathSpells.append("Hunter’s Mark")
                    if pallvl >= 5:
                        PaladinOathSpells.append("Hold Person")
                        PaladinOathSpells.append("Misty Step")                    
                    if pallvl >= 9:
                        PaladinOathSpells.append("Haste")
                        PaladinOathSpells.append("Protection from Energy")
                    if pallvl >= 13:
                        PaladinOathSpells.append("Banishment")
                        PaladinOathSpells.append("Dimension Door")
                    if pallvl >= 17:
                        PaladinOathSpells.append("Hold Monster")
                        PaladinOathSpells.append("Scrying")  
                    player.classnotes.append("Tenets of Vengeance (see notes)")
                    player.notes.append("Tenets of Vengeance - The tenets of the Oath of Vengeance vary by paladin, but all the tenets revolve around punishing wrongdoers by any means necessary. Paladins who uphold these tenets are willing to sacrifice even their own righteousness to mete out justice upon those who do evil, so the paladins are often neutral or lawful neutral in alignment. The core principles of the tenets are brutally simple.\nFight the Greater Evil - Faced with a choice of fighting my sworn foes or combating a lesser evil, I choose the greater evil.\nNo Mercy for the Wicked - Ordinary foes might win my mercy, but my sworn enemies do not.\nBy Any Means Necessary - My qualms can't get in the way of exterminating my foes.\nRestitution - If my foes wreak ruin on the world, it is because I failed to stop them. I must help those harmed by their misdeeds.")          
                    player.classnotes.append("Channel Divinity (see notes)")
                    player.notes.append("Channel Divinity - You gain the following two Channel Divinity options.\nAbjure Enemy - As an action, you present your holy symbol and speak a prayer of denunciation, using your Channel Divinity. Choose one creature within 60 feet of you that you can see. That creature must make a Wisdom saving throw, unless it is immune to being frightened. Fiends and undead have disadvantage on this saving throw.\nOn a failed save, the creature is frightened for 1 minute or until it takes any damage. While frightened, the creature's speed is 0, and it can't benefit from any bonus to its speed.\nOn a successful save, the creature's speed is halved for 1 minute or until the creature takes any damage.\nVow of Enmity - As a bonus action, you can utter a vow of enmity against a creature you can see within 10 feet of you, using your Channel Divinity. You gain advantage on attack rolls against the creature for 1 minute or until it drops to 0 hit points or falls unconscious.")
                    if pallvl >= 7:
                        player.classnotes.append("Relentless Avenger (see notes)")
                        player.notes.append("Relentless Avenger - Your supernatural focus helps you close off a foe's retreat. When you hit a creature with an opportunity attack, you can move up to half your speed immediately after the attack and as part of the same reaction. This movement doesn't provoke opportunity attacks.")                        
                    if pallvl >= 15:
                        player.classnotes.append("Soul of Vengeance (see notes)")
                        player.notes.append("Soul of Vengeance - The authority with which you speak your Vow of Enmity gives you greater power over your foe. When a creature under the effect of your Vow of Enmity makes an attack, you can use your reaction to make a melee weapon attack against that creature if it is within range.")                               
                    if pallvl >= 20:           
                        player.classnotes.append("Avenging Angel (see notes)")
                        player.notes.append("Avenging Angel - You can assume the form of an angelic avenger. Using your action, you undergo a transformation. For 1 hour, you gain the following benefits:\n- Wings sprout from your back and grant you a flying speed of 60 feet.\n- You emanate an aura of menace in a 30-foot radius. The first time any enemy creature enters the aura or starts its turn there during a battle, the creature must succeed on a Wisdom saving throw or become frightened of you for 1 minute or until it takes any damage. Attack rolls against the frightened creature have advantage.\nOnce you use this feature, you can't use it again until you finish a long rest.")
                if player.subclass[i] == "Oathbreaker Paladin":        
                    if pallvl >= 3:
                        PaladinOathSpells.append("Hellish Rebuke")
                        PaladinOathSpells.append("Inflict Wounds")
                    if pallvl >= 5:
                        PaladinOathSpells.append("Crown of Madness")
                        PaladinOathSpells.append("Darkness")
                    if pallvl >= 9:
                        PaladinOathSpells.append("Animate Dead")
                        PaladinOathSpells.append("Bestow Curse")
                    if pallvl >= 13:
                        PaladinOathSpells.append("Blight")
                        PaladinOathSpells.append("Confusion")
                    if pallvl >= 17:
                        PaladinOathSpells.append("Contagion")
                        PaladinOathSpells.append("Dominate Person")
                    player.classnotes.append("Channel Divinity (see notes)")
                    player.notes.append(f"Channel Divinity - You gain the following two Channel Divinity options.\nControl Undead - As an action, you target one undead creature you can see within 30 feet of you. The target must make a Wisdom saving throw. On a failed save, the target must obey your commands for the next 24 hours, or until you use this Channel Divinity option again. An undead whose challenge rating is equal to or greater than your paladin level, or no greater than {pallvl}, is immune to this effect.\nDreadful Aspect - As an action, you channel the darkest emotions and focus them into a burst of magical menace. Each creature of your choice within 30 feet of you must make a Wisdom saving throw if it can see you. On a failed save, the target is frightened of you for 1 minute. If a creature frightened by this effect ends its turn more than 30 feet away from you, it can attempt another Wisdom saving throw to end the effect on it.")
                    if pallvl >= 7:
                        player.classnotes.append(f"Aura of Hate(1) - You, as well any fiends and undead within 10 feet of you, gain a bonus to melee weapon damage rolls equal to your Charisma modifier, or a bonus of {player.ChaMod}, minimum of +1. A creature can benefit from this feature from only one paladin at a time.")
                    if pallvl >= 15:
                        player.classnotes.append("Supernatural Resistance (see notes)")
                        player.notes.append("Supernatural Resistance - You gain resistance to bludgeoning, piercing, and slashing damage from nonmagical weapons.")  
                    if pallvl >= 18:
                        player.classnotes.append("Aura of Hate(2) - The range of this aura increases to 30 feet.")                             
                    if pallvl >= 20:           
                        player.classnotes.append("Dread Lord (see notes)")
                        player.notes.append(f"Dread Lord - You can, as an action, surround yourself with an aura of gloom that lasts for 1 minute. The aura reduces any bright light in a 30-foot radius around you to dim light. Whenever an enemy that is frightened by you starts its turn in the aura, it takes 4d10 psychic damage. Additionally, you and any creatures of your choosing in the aura are draped in deeper shadow. Creatures that rely on sight have disadvantage on attack rolls against creatures draped in this shadow.\nWhile the aura lasts, you can use a bonus action on your turn to cause the shadows in the aura to attack one creature. Make a melee spell attack against the target. If the attack hits, the target takes necrotic damage equal to 3d10 + your Charisma modifier, or 3d10 + {player.ChaMod} necrotic damage.\nAfter activating the aura, you can't do so again until you finish a long rest.")
            player.classnotes.append(f"Paladin Oath Spells - You gain oath spells at certain Paladin levels, currently your Oath Spells: {PaladinOathSpells}")
            PaladinSpellSlot1 = 3
            player.classnotes.append("Divine Health - The divine magic flowing through you makes you immune to disease.")
            HarnessDivinePower = 1
            if ((pallvl >= 7) and (pallvl < 15)):
                HarnessDivinePower = 2
            if pallvl >= 15:
                HarnessDivinePower = 3   
            player.classnotes.append("Harness Divine Power (see notes)")
            player.notes.append(f"Harness Divine Power - You can expend a use of your Channel Divinity to fuel your spells. As a bonus action, you touch your holy symbol, utter a prayer, and regain one expended spell slot, the level of which is half your Paladin Proficiency Bonus, or level being {math.ceil(pallvl/2)}. The number of times you can use this feature is based on your Paladin level, or {HarnessDivinePower} times.\nYou regain all expended uses when you finish a long rest.")
            if pallvl >= 4:
                player.classnotes.append("Martial Versatility (see notes)")
                player.notes.append("Martial Versatility - Whenever you reach a level in this class that grants the Ability Score Improvement feature, you can replace a fighting style you know with another fighting style available to paladins. This replacement represents a shift of focus in your martial practice.")
            if pallvl >= 5:
                PaladinSpellSlot1 = 4
                PaladinSpellSlot2 = 2
                player.classnotes.append("Extra Attack - You can attack twice, instead of once, whenever you take the Attack action on your turn.")
            if pallvl >= 6:
                player.classnotes.append(f"Aura of Protection(1) - Whenever you or a friendly creature within 10 feet of you must make a saving throw, the creature gains a bonus to the saving throw equal to your Charisma modifier, or a bonus of {player.ChaMod}, with a minimum bonus of +1. You must be conscious to grant this bonus.")
            if pallvl >= 7:
                PaladinSpellSlot2 = 3
            if pallvl >= 9:
                PaladinSpellSlot3 = 2
            if pallvl >= 10:
                player.classnotes.append("Aura of Courage - You and friendly creatures within 10 feet of you can’t be frightened while you are conscious.")
            if pallvl >= 11:
                PaladinSpellSlot3 = 3
                player.classnotes.append("Improved Divine Smite - You are so suffused with righteous might that all your melee weapon strikes carry divine power with them. Whenever you hit a creature with a melee weapon, the creature takes an extra 1d8 radiant damage.")
            if pallvl >= 13:
                PaladinSpellSlot4 = 1
            if pallvl >= 14:
                player.classnotes.append("Cleansing Touch (see notes)")
                player.notes.append(f"Cleansing Touch - You can use your action to end one spell on yourself or on one willing creature that you touch.\nYou can use this feature a number of times equal to your Charisma modifier, or {player.ChaMod} times, a minimum of once. You regain expended uses when you finish a long rest.")
            if pallvl >= 15:
                PaladinSpellSlot4 = 2
            if pallvl >= 17:
                PaladinSpellSlot4 = 3
                PaladinSpellSlot5 = 1
            if pallvl >= 18:
                player.classnotes.append("Aura of Protection(2) - The range of this aura increases to 30 feet.")
                player.classnotes.append("Aura of Courage(2) - The range of this aura increases to 30 feet.")
            if pallvl >= 19:
                PaladinSpellSlot5 = 2
            if PaladinSpellSlot1 != 0:
                player.notes.append(f"The number of first level spell slots you have as a Paladin is: {PaladinSpellSlot1}.")
            if PaladinSpellSlot2 != 0:
                player.notes.append(f"The number of second level spell slots you have as a Paladin is: {PaladinSpellSlot2}.")
            if PaladinSpellSlot3 != 0:                
                player.notes.append(f"The number of third level spell slots you have as a Paladin is: {PaladinSpellSlot3}.")
            if PaladinSpellSlot4 != 0:
                player.notes.append(f"The number of fourth level spell slots you have as a Paladin is: {PaladinSpellSlot4}.")
            if PaladinSpellSlot5 != 0:
                player.notes.append(f"The number of fifth level spell slots you have as a Paladin is: {PaladinSpellSlot5}.")                   
        #Now here for refactoring everything
        if player.Class[i] == "Ranger":
            if ((param == "N") or (player.singlemulticlass == "N")):
                ranlvl = player.level
                player.classlvl.append(ranlvl)
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    ranlvl = int(input(f"Given your pool of levels of {poollevel}, what is your Ranger level? "))  
                    if ranlvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                
                poollevel = poollevel - ranlvl
                player.classlvl.append(ranlvl)
            if ranlvl >= 1:
                player.hitdice.append(f"{ranlvl}d10 for {player.Class[i]}")
                if ranlvl == 1:
                    player.hitpoints += (10 + player.ConMod)
                else:
                    player.hitpoints += (10 + player.ConMod + hpcalc(ranlvl, dice, 10))   
                if i == 0:                               
                    profs = ["Light Armor", "Medium Armor", "Shield", "Simple Weapons", "Martial Weapons"]
                    for prof in profs:      
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)                             
                    player.skills.append(dnd_tools.saving_throws["StrST"])
                    player.skills.append(dnd_tools.saving_throws["DexST"])
                    SkillsList = [
                        dnd_tools.skills["AnimalHandling"], 
                        dnd_tools.skills["Athletics"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Investigation"], 
                        dnd_tools.skills["Nature"], 
                        dnd_tools.skills["Perception"], 
                        dnd_tools.skills["Stealth"], 
                        dnd_tools.skills["Survival"]
                        ]
                    player.skills = threeskillsfromlist(param, player.skills, SkillsList)         
                    StartEquip1 = ["Scale Mail", "Leather Armor"]
                    StartEquip2 = ["Two Shortswords", "Two Simple Melee Weapons"]
                    StartEquip3 = ["Dungeoneer's Pack", "Explorer's Pack"]
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Scale Mail")
                        print("2 - Leather Armor")
                        se1 = int(input("What would you like your first choice for starting equipment to be? "))
                        if se1 == 0:
                            SE1rand = random.choice(StartEquip1)
                            if SE1rand == "Scale Mail":
                                player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                            if SE1rand == "Leather Armor":
                                player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        if se1 == 1:
                            player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                        if se1 == 2:
                            player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        print("0 - Random")
                        print("1 - Two Shortswords")
                        print("2 - Two Simple Melee Weapons")
                        se2 = int(input("What would you like your second choice for starting equipment to be? "))
                        if se2 == 0:
                            SE2rand = random.choice(StartEquip2)
                            if SE2rand == "Two Shortswords":
                                 player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                                 player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                            if SE2rand == "Two Simple Melee Weapons":
                                SimpMRandKey1 = random.choice(SimpleMeleeWeapons)
                                player.equipment.append(dnd_tools.simple_weapons[SimpMRandKey1].copy())
                                SimpMRandKey2 = random.choice(SimpleMeleeWeapons)
                                player.equipment.append(dnd_tools.simple_weapons[SimpMRandKey2].copy())
                        if se2 == 1:
                             player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                             player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                        if se2 == 2:
                            print("0 - Random")
                            for j, smw in enumerate(SimpleMeleeWeaponsNames, 1):
                                print(f"{j} - {smw}")
                            se2smw1 = int(input("Which simple melee weapon would you like to add to your inventory first? "))
                            if se2smw1 == 0:
                                SimpMRandKey1 = random.choice(SimpleMeleeWeapons)
                                player.equipment.append(dnd_tools.simple_weapons[SimpMRandKey1].copy())
                            elif 1 <= se2smw1 <= len(SimpleMeleeWeaponsNames):
                                SimpMKey = SimpleMeleeWeapons[se2smw1-1]
                                player.equipment.append(dnd_tools.simple_weapons[SimpMKey].copy())
                            print("0 - Random")
                            for j, smw in enumerate(SimpleMeleeWeaponsNames, 1):
                                print(f"{j} - {smw}")
                            se2smw2 = int(input("Which simple melee weapon would you like to add to your inventory second? "))
                            if se2smw2 == 0:
                                SimpMRandKey2 = random.choice(SimpleMeleeWeapons)
                                player.equipment.append(dnd_tools.simple_weapons[SimpMRandKey2].copy())
                            elif 1 <= se2smw2 <= len(SimpleMeleeWeaponsNames):
                                SimpMKey = SimpleMeleeWeapons[se2smw2-1]
                                player.equipment.append(dnd_tools.simple_weapons[SimpMKey].copy())                              
                        print("0 - Random")
                        print("1 - Dungeoneer's Pack")
                        print("2 - Explorer's Pack")
                        se3 = int(input("What would you like your third choice for starting equipment to be? "))
                        if se3 == 0:
                            SE3rand = random.choice(StartEquip3)
                            if SE3rand == "Dungeoneer's Pack":
                                player.equipment.extend(dnd_tools.packs["DungeoneersPack"]["contents"])                       
                            if SE3rand == "Explorer's Pack":
                                player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])
                        if se3 == 1:
                            player.equipment.extend(dnd_tools.packs["DungeoneersPack"]["contents"])
                        if se3 == 2:
                            player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])
                        player.equipment.append(dnd_tools.martial_weapons["Longbow"].copy())
                        player.equipment.append("A Quiver of 20 Arrows")
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "Scale Mail":
                            player.equipment.append(dnd_tools.medium_armor["ScaleMail"].copy())
                        if SE1rand == "Leather Armor":
                            player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "Two Shortswords":
                             player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                             player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                        if SE2rand == "Two Simple Melee Weapons":
                            SimpMRandKey1 = random.choice(SimpleMeleeWeapons)
                            player.equipment.append(dnd_tools.simple_weapons[SimpMRandKey1].copy())
                            SimpMRandKey2 = random.choice(SimpleMeleeWeapons)
                            player.equipment.append(dnd_tools.simple_weapons[SimpMRandKey2].copy())
                        SE3rand = random.choice(StartEquip3)
                        if SE3rand == "Dungeoneer's Pack":
                            player.equipment.extend(dnd_tools.packs["DungeoneersPack"]["contents"])                       
                        if SE3rand == "Explorer's Pack":
                            player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])                        
                        player.equipment.append(dnd_tools.martial_weapons["Longbow"].copy())
                        player.equipment.append("A Quiver of 20 Arrows")   
                else:
                    profs = ["Light Armor", "Medium Armor", "Shield", "Simple Weapons", "Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)      
                    SkillsList = [
                        dnd_tools.skills["AnimalHandling"], 
                        dnd_tools.skills["Athletics"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Investigation"], 
                        dnd_tools.skills["Nature"], 
                        dnd_tools.skills["Perception"], 
                        dnd_tools.skills["Stealth"], 
                        dnd_tools.skills["Survival"]
                        ]
                    player.skills = oneskillfromlist(param, player.skills, SkillsList)       
            player.classnotes.append("Favored Enemy(1) (see notes)")
            player.notes.append("Favored Enemy(1) - You have significant experience studying, tracking, hunting, and even talking to a certain type of enemy.\nChoose a type of favored enemy: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies.\nYou have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.\nWhen you gain this feature, you also learn one language of your choice that is spoken by your favored enemies, if they speak one at all (not adapted into your languages).\nMore options are available at higher levels. As you gain levels, your choices should reflect the types of monsters you have encountered on your adventures.")
            player.classnotes.append("Natural Explorer (see notes)")
            player.notes.append("Natural Explorer - You are particularly familiar with one type of natural environment and are adept at traveling and surviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, grassland, mountain, swamp, or the Underdark. When you make an Intelligence or Wisdom check related to your favored terrain, your Proficiency Bonus is doubled if you are using a skill that you’re proficient in.\nWhile traveling for an hour or more in your favored terrain, you gain the following benefits:\n- Difficult terrain doesn’t slow your group’s travel.\n- Your group can’t become lost except by magical means.\n- Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.\n- If you are traveling alone, you can move stealthily at a normal pace.\n- When you forage, you find twice as much food as you normally would.\n- While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.\nYou choose additional favored terrain types at 6th and 10th level.")
            if ranlvl >= 2:
                player.spellcastingclass.append("Ranger")
                player.spellcastingability.append("Wis")
                player.spellsavedc.append(8 + player.profbonus + player.WisMod)
                player.spellattackmod.append(player.profbonus + player.WisMod)
                RangerSpellsKnown = 2
                RangerSpellSlot1 = 2
                RangerSpellSlot2 = 0
                RangerSpellSlot3 = 0
                RangerSpellSlot4 = 0
                RangerSpellSlot5 = 0  
                player.classnotes.append("Spellcasting Focus - You can use a druidic focus as a spellcasting focus for your ranger spells. A druidic focus might be a sprig of mistletoe or holly, a wand or rod made of yew or another special wood, a staff drawn whole from a living tree, or an object incorporating feathers, fur, bones, and teeth from sacred animals.")     
                player.notes.append("Fighting Style - You adopt a particular style of fighting as your specialty. Choose one of the following options. You can’t take a Fighting Style option more than once, even if you later get to choose again.\n- Archery - You gain a +2 bonus to attack rolls you make with ranged weapons.\n- Blind Fighting - You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you.\n- Defense - While you are wearing armor, you gain a +1 bonus to AC.\n- Dueling - When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.\n- Thrown Weapon Fighting - You can draw a weapon that has the thrown property as part of the attack you make with the weapon. In addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll.\n- Two-Weapon Fighting - When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.")
            if ranlvl >= 3:
                Ran = ["Beast Master Archetype Ranger", "Drakewarden Ranger", "Fey Wanderer Archetype Ranger", "Gloom Stalker Archetype Ranger", "Horizon Walker Archetype Ranger", "Hunter Archetype Ranger", "Monster Slayer Archetype Ranger", "Swarmkeeper Archetype Ranger"]
                

                if player.subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        for idx, subcl in enumerate(Ran, 1):
                            print(f"{idx} - {subcl}")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 0:
                            player.subclass[i] = random.choice(Ran)
                        elif 1 <= subc <= len(Ran):
                            player.subclass[i] = Ran[subc - 1]
                    if param == "N":
                        player.subclass[i] = random.choice(Ran)                            
                if player.subclass[i] == "Beast Master Archetype Ranger":
                    player.classnotes.append("Ranger's Companion (see notes)")
                    player.notes.append(f"Ranger's Companion - You gain a beast companion that accompanies you on your adventures and is trained to fight alongside you. Choose a beast that is no larger than Medium and that has a challenge rating of 1/4 or lower (appendix D of the Player's Handbook presents statistics for the Hawk, Mastiff, and Panther as examples). Add your Proficiency Bonus, or {player.profbonus}, to the beast's AC, attack rolls, and damage rolls, as well as to any saving throws and skills it is proficient in. Its hit point maximum equals the hit point number in its stat block or four times your Ranger level, or hit point maximum of {4*ranlvl}, whichever is higher. Like any creature, it can spend Hit Dice during a short rest to regain hit points.\nThe beast obeys your commands as best as it can. It takes its turn on your initiative. On your turn, you can verbally command the beast where to move (no action required by you). You can use your action to verbally command it to take the Attack, Dash, Disengage, or Help action. Once you have the Extra Attack feature, you can make one weapon attack yourself when you command the beast to take the Attack action. If you don't issue a command, the beast takes the Dodge action.\nIf you are incapacitated or absent, the beast acts on its own, focusing on protecting you and itself. The beast never requires your command to use its reaction, such as when making an opportunity attack.\nWhile traveling through your favored terrain with only the beast, you can move stealthily at a normal pace.\nIf the beast dies, you can obtain a new companion by spending 8 hours magically bonding with a beast that isn't hostile to you and that meets the requirements.")
                    player.classnotes.append("Primal Companion (see notes)")
                    player.notes.append("Primal Companion - Instead of Ranger's Companion, if you choose, you magically summon a primal beast, which draws strength from your bond with nature. The beast is friendly to you and your companions and obeys your commands. Choose its stat block-Beast of the Land, Beast of the Sea, or Beast of the Sky-which uses your Proficiency Bonus (PB) in several places. You also determine the kind of animal the beast is, choosing a kind appropriate for the stat block. Whatever kind you choose, the beast bears primal markings, indicating its mystical origin.\nIn combat, the beast acts during your turn. It can move and use its reaction on its own, but the only action it takes is the Dodge action, unless you take a bonus action on your turn to command it to take another action. That action can be one in its stat block or some other action. You can also sacrifice one of your attacks when you take the Attack action to command the beast to take the Attack action. If you are incapacitated, the beast can take any action of its choice, not just Dodge.\nIf the beast has died within the last hour, you can use your action to touch it and expend a spell slot of 1st level or higher. The beast returns to life after 1 minute with all its hit points restored.\nWhen you finish a long rest, you can summon a different primal beast. The new beast appears in an unoccupied space within 5 feet of you, and you choose its stat block and appearance. If you already have a beast from this feature, it vanishes when the new beast appears. The beast also vanishes if you die.")
                    if ranlvl >= 7:
                        player.classnotes.append("Exceptional Training (see notes)")
                        player.notes.append("Exceptional Training - On any of your turns when your beast companion doesn't attack, you can use a bonus action to command the beast to take the Dash, Disengage, Dodge, or Help action on its turn.\nIn addition, the beast's attacks now count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage.")                             
                    if ranlvl >= 11:
                        player.classnotes.append("Bestial Fury - When you command your beast companion to take the Attack action, the beast can make two attacks, or it can take the Multiattack action if it has that action.")                             
                    if ranlvl >= 15:
                        player.classnotes.append("Share Spells - When you cast a spell targeting yourself, you can also affect your beast companion with the spell if the beast is within 30 feet of you.") 
                if player.subclass[i] == "Drakewarden Ranger":
                    DWO1 = "You studied a dragon's scale or claw, or a trinket from a dragon's hoard, creating your bond through that token's lingering draconic magic."
                    DWO2 = "A secret order of rangers who collect and guard draconic lore taught you their ways."
                    DWO3 = "A dragon gave you a geode or gemstone to care for. To your surprise, the drake hatched from that stone."
                    DWO4 = "You ingested a few drops of dragon blood, forever infusing your nature magic with draconic power."
                    DWO5 = "An ancient Draconic inscription on a standing stone empowered you when you read it aloud."
                    DWO6 = "You had a vivid dream of a mysterious figure accompanied by seven yellow canaries, who warned you of impending doom. When you awoke, your drake was there, watching you."
                    DWO = [DWO1, DWO2, DWO3, DWO4, DWO5, DWO6]
                    DrakewardenOrigin = random.choice(DWO)
                    player.classnotes.append(f"As a Drakewarden Ranger, your Drakewarden Origin: {DrakewardenOrigin}")       
                    if dnd_tools.languages["Drac"] not in player.languages:
                        player.languages.append(dnd_tools.languages["Drac"])
                    else:
                        player.languages, player.slang = languagegen(param, player.languages, player.slang)
                    player.classnotes.append("Draconic Gift (see notes)")
                    player.notes.append("Draconic Gift - The bond you share with your drake creates a connection to dragonkind, granting you understanding and empowering your presence. You gain the following benefits:\nThaumaturgy - You learn the Thaumaturgy cantrip, which is a ranger spell for you.\nTongue of Dragons - You learn to speak, read, and write Draconic or one other language of your choice (this last one has been addressed).")
                    player.classnotes.append("Drake Companion (see notes)")
                    player.notes.append("Drake Companion - As an action, you can magically summon the drake that is bound to you. It appears in an unoccupied space of your choice within 30 feet of you.\nThe drake is friendly to you and your companions, and it obeys your commands. See its game statistics in the Drake Companion stat block in 'Fizban's Treasury of Dragons', which uses your Proficiency Bonus (PB) in several places. Whenever you summon the drake, choose a damage type listed in its Draconic Essence trait. You can determine the cosmetic characteristics of the drake, such as its color, its scale texture, or any visible effect of its Draconic Essence; your choice has no effect on its game statistics.\nIn combat, the drake shares your initiative count, but it takes its turn immediately after yours. It can move and use its reaction on its own, but the only action it takes on its turn is the Dodge action, unless you take a bonus action on your turn to command it to take another action. That action can be one in its stat block or some other action. If you are incapacitated, the drake can take any action of its choice, not just Dodge.\nThe drake remains until it is reduced to 0 hit points, until you use this feature to summon the drake again, or until you die. Anything the drake was wearing or carrying is left behind when the drake vanishes.\nOnce you summon the drake, you can't do so again until you finish a long rest, unless you expend a spell slot of 1st level or higher to summon it.")
                    if ranlvl >= 7:
                        player.classnotes.append("Bond of Fang and Scale (see notes)")
                        player.notes.append("Bond of Fang and Scale - The bond you share with your drake intensifies, protecting you and stoking the drake's fury. When you summon your drake, it grows wings on its back and gains a flying speed equal to its walking speed.\nIn addition, while your drake is summoned, you and the drake gain the following benefits:\nDrake Mount - The drake grows to Medium size. Reflecting your special bond, you can use the drake as a mount if your size is Medium or smaller. While you are riding your drake, it can't use the flying speed of this feature.\nMagic Fang - The drake's Bite attack deals an extra 1d6 damage of the type chosen for the drake's Draconic Essence.\nResistance - You gain resistance to the damage type chosen for the drake's Draconic Essence.")                             
                    if ranlvl >= 11:
                        DrakesBreathDmg = "8d6"
                        if ranlvl >= 15:
                            DrakesBreathDmg = "10d6"
                        player.classnotes.append("Drake's Breath (see notes)")
                        player.notes.append(f"Drake's Breath - As an action, you can exhale a 30-foot cone of damaging breath or cause your drake to exhale it. Choose acid, cold, fire, lightning, or poison damage (your choice doesn't have to match your drake's Draconic Essence). Each creature in the cone must make a Dexterity saving throw against your spell save DC, or against {player.spellsavedc[i]}, taking {DrakesBreathDmg} damage on a failed save, or half as much damage on a successful one.\nOnce you use this feature, you can't do so again until you finish a long rest, unless you expend a spell slot of 3rd level or higher to use it again.")                             
                    if ranlvl >= 15:
                        player.classnotes.append("Perfected Bond (see notes)")
                        player.notes.append(f"Perfected Bond - Your bond to your drake reaches the pinnacle of its power. While your drake is summoned, you and the drake gain the following benefits:\nEmpowered Bite - The drake's Bite attack deals an extra 1d6 damage of the type chosen for its Draconic Essence (for a total of 2d6 extra damage).\nLarge Drake - The drake grows to Large size. When you ride your drake, it is no longer prohibited from using the flying speed of Bond of Fang and Scale.\nReflexive Resistance - When either you or the drake takes damage while you're within 30 feet of each other, you can use your reaction to give yourself or the drake resistance to that instance of damage. You can use this reaction a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.") 
                if player.subclass[i] == "Fey Wanderer Archetype Ranger":
                    RangerFeyWandererSpells = []
                    if ranlvl >= 3:
                        RangerFeyWandererSpells.append("Charm Person")
                    if ranlvl >= 5:
                        RangerFeyWandererSpells.append("Misty Step")
                    if ranlvl >= 9:
                        RangerFeyWandererSpells.append("Dispel Magic")
                    if ranlvl >= 13:
                        RangerFeyWandererSpells.append("Dimension Door")
                    if ranlvl >= 17:
                        RangerFeyWandererSpells.append("Mislead")
                    DreadfulStrikeDmg = "1d4"
                    if ranlvl >= 11:
                        DreadfulStrikeDmg = "1d6"
                    player.classnotes.append("Dreadful Strikes (see notes)")
                    player.notes.append(f"Dreadful Strikes - You can augment your weapon strikes with mind-scarring magic, drawn from the gloomy hollows of the Feywild. When you hit a creature with a weapon, you can deal an extra {DreadfulStrikeDmg} psychic damage to the target, which can take this extra damage only once per turn.")
                    FWG1 = "Illusory butterflies flutter around you while you take a short or long rest."
                    FWG2 = "Fresh, seasonal flowers sprout from your hair each dawn."
                    FWG3 = "You faintly smell of cinnamon, lavender, nutmeg, or another comforting herb or spice."
                    FWG4 = "Your shadow dances while no one is looking directly at it."
                    FWG5 = "Horns or antlers sprout from your head."
                    FWG6 = "Your skin and hair change color to match the season at each dawn."
                    FWG = [FWG1, FWG2, FWG3, FWG4, FWG5, FWG6]
                    if param == "Y":
                        print("0 - Random")
                        for r, fwg in enumerate(FWG, 1):
                            print(f"{r} - {fwg}")
                        fwginput = int(input("Choose the blessing you receieve from a fey ally or place of fey power. "))
                        if fwginput == 0:
                            FWGChoice = random.choice(FWG)
                        elif 1 <= fwginput <= len(FWG):
                            FWGChoice = FWG[fwginput - 1]
                    if param == "N":
                        FWGChoice = random.choice(FWG)
                    player.classnotes.append("Fey Wanderer Magic (see notes)")
                    player.notes.append(f"Fey Wanderer Magic - You learn an additional spell when you reach certain levels in this class. Each spell counts as a ranger spell for you, but it doesn't count against the number of ranger spells you know. Currently, as a Fey Wanderer Ranger, you know: {RangerFeyWandererSpells}; You also possess a preternatural blessing from a fey ally or a place of fey power. Your blessing is {FWGChoice}")
                    player.classnotes.append("Otherworldly Glamour (see notes)")
                    player.notes.append(f"Otherworldly Glamour - Your fey qualities give you a supernatural charm. As a result, whenever you make a Charisma check, you gain a bonus to the check equal to your Wisdom modifier, or a bonus of {player.WisMod}, minimum of +1.")
                    SkillsList = [
                        dnd_tools.skills["Deception"], 
                        dnd_tools.skills["Performance"], 
                        dnd_tools.skills["Persuasion"]
                        ]
                    player.skills = oneskillfromlist(param, player.skills, SkillsList)
                    if ranlvl >= 7:
                        player.classnotes.append("Beguiling Twist (see notes)")
                        player.notes.append(f"Beguiling Twist - The magic of the Feywild guards your mind. You have advantage on saving throws against being charmed or frightened.\nIn addition, whenever you or a creature you can see within 120 feet of you succeeds on a saving throw against being charmed or frightened, you can use your reaction to force a different creature you can see within 120 feet of you to make a Wisdom saving throw against your spell save DC, or against {player.spellsavedc[i]}. If the save fails, the target is charmed or frightened by you (your choice) for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a successful save.")                             
                    if ranlvl >= 11:
                        player.classnotes.append("Fey Reinforcements (see notes)")
                        player.notes.append("Fey Reinforcements - The royal courts of the Feywild have blessed you with the assistance of fey beings: you know summon fey (a spell in chapter 3 of Tasha's Cauldron). It doesn't count against the number of ranger spells you know, and you can cast it without a material component. You can also cast it once without a spell slot, and you regain the ability to do so when you finish a long rest.\nWhenever you start casting the spell, you can modify it so that it doesn't require concentration. If you do so, the spell's duration becomes 1 minute for that casting.")                             
                    if ranlvl >= 15:
                        player.classnotes.append(f"Misty Wanderer - You can slip in and out of the Feywild to move in a blink of an eye: you can cast misty step without expending a spell slot. You can do so a number of times equal to your Wisdom modifier, or {player.WisMod} times, minimum of once, and you regain all expended uses when you finish a long rest.\nIn addition, whenever you cast misty step, you can bring along one willing creature you can see within 5 feet of you. That creature teleports to an unoccupied space of your choice within 5 feet of your destination space.")                        
                if player.subclass[i] == "Gloom Stalker Archetype Ranger":
                    RangerGloomStalkerSpells = []
                    if ranlvl >= 3:
                        RangerGloomStalkerSpells.append("Disguise Self")
                    if ranlvl >= 5:
                        RangerGloomStalkerSpells.append("Rope Trick")
                    if ranlvl >= 9:
                        RangerGloomStalkerSpells.append("Fear")
                    if ranlvl >= 13:
                        RangerGloomStalkerSpells.append("Greater Invisibility")
                    if ranlvl >= 17:
                        RangerGloomStalkerSpells.append("Seeming")
                    player.classnotes.append("Gloom Stalker Magic (see notes)")
                    player.notes.append(f"Gloom Stalker Magic - You learn an additional spell when you reach certain levels in this class. The spell counts as a ranger spell for you, but it doesn't count against the number of ranger spells you know. Currently, as a Gloom Stalker Ranger, you know: {RangerGloomStalkerSpells}")
                    player.classnotes.append("Dread Ambusher (see notes)")
                    player.notes.append(f"Dread Ambusher - You master the art of the ambush. You can give yourself a bonus to your initiative rolls equal to your Wisdom modifier, or a bonus of {player.WisMod}.\nAt the start of your first turn of each combat, your walking speed increases by 10 feet, which lasts until the end of that turn. If you take the Attack action on that turn, you can make one additional weapon attack as part of that action. If that attack hits, the target takes an extra 1d8 damage of the weapon's damage type.")
                    player.classnotes.append("Umbral Sight (see notes)")
                    player.notes.append("Umbral Sight - You gain darkvision out to a range of 60 feet. If you already have darkvision from your race, its range increases by 30 feet.\nYou are also adept at evading creatures that rely on darkvision. While in darkness, you are invisible to any creature that relies on darkvision to see you in that darkness.")
                    if ranlvl >= 7:
                        if dnd_tools.saving_throws["WisST"] not in player.proficiencies:
                            player.skills.append(dnd_tools.saving_throws["WisST"])
                        else:
                            SavingThrowList = [dnd_tools.saving_throws["IntST"], dnd_tools.saving_throws["ChaST"]]
                            player.skills = oneskillfromlist(param, player.skills, SavingThrowList)
                        player.classnotes.append("Iron Mind - You have honed your ability to resist the mind-altering powers of your prey. You gain proficiency in Wisdom saving throws. If you already have this proficiency, you instead gain proficiency in Intelligence or Charisma saving throws (your choice), these all have been addressed.")                          
                    if ranlvl >= 11:
                        player.classnotes.append("Stalker's Flurry - You learn to attack with such unexpected speed that you can turn a miss into another strike. Once on each of your turns when you miss with a weapon attack, you can make another weapon attack as part of the same action.")                            
                    if ranlvl >= 15:
                        player.classnotes.append("Shadowy Dodge - You can dodge in unforeseen ways, with wisps of supernatural shadow around you. Whenever a creature makes an attack roll against you and doesn't have advantage on the roll, you can use your reaction to impose disadvantage on it. You must use this feature before you know the outcome of the attack roll.")                    
                if player.subclass[i] == "Horizon Walker Archetype Ranger":
                    RangerHorizonWalkerSpells = []
                    if ranlvl >= 3:
                        RangerHorizonWalkerSpells.append("Protection from Evil and Good")
                    if ranlvl >= 5:
                        RangerHorizonWalkerSpells.append("Misty Step")
                    if ranlvl >= 9:
                        RangerHorizonWalkerSpells.append("Haste")
                    if ranlvl >= 13:
                        RangerHorizonWalkerSpells.append("Banishment")
                    if ranlvl >= 17:
                        RangerHorizonWalkerSpells.append("Teleportation Circle")                    
                    player.classnotes.append("Horizon Walker Magic (see notes)")
                    player.notes.append(f"Horizon Walker Magic - You learn an additional spell when you reach certain levels in this class. The spell counts as a ranger spell for you, but it doesn’t count against the number of ranger spells you know. Currently, as a Horizon Walker Ranger, you know: {RangerHorizonWalkerSpells}")
                    player.classnotes.append("Detect Portal (see notes)")
                    player.notes.append("Detect Portal - You gain the ability to magically sense the presence of a planar portal. As an action, you detect the distance and direction to the closest planar portal within 1 mile of you.\nOnce you use this feature, you can't use it again until you finish a short or long rest.\nSee the 'Planar Travel' section in chapter 2 of the Dungeon Master's Guide for examples of planar portals.")
                    PlanarWarriorDmg = "1d8"
                    if ranlvl >= 11:
                        PlanarWarriorDmg = "2d8"
                    player.classnotes.append("Planar Warrior (see notes)")
                    player.notes.append(f"Planar Warrior - You learn to draw on the energy of the multiverse to augment your attacks.\nAs a bonus action, choose one creature you can see within 30 feet of you. The next time you hit that creature on this turn with a weapon attack, all damage dealt by the attack becomes force damage, and the creature takes an extra {PlanarWarriorDmg} force damage from the attack.")
                    if ranlvl >= 7:
                        player.classnotes.append("Ethereal Step (see notes)")
                        player.notes.append("Ethereal Step - You learn to step through the Ethereal Plane. As a bonus action on your turn, you can cast the Etherealness spell with this feature, without expending a spell slot, but the spell ends at the end of the current turn.\nOnce you use this feature, you can’t use it again until you finish a short or long rest.")                             
                    if ranlvl >= 11:
                        player.classnotes.append("Distant Strike (see notes)")
                        player.notes.append("Distant Strike - You gain the ability to pass between the planes in a blink of an eye. When you use the Attack action, you can teleport up to 10 feet before each attack to an unoccupied space you can see.\nIf you attack at least two different creatures with the action, you can make one additional attack with it against a third creature.")                             
                    if ranlvl >= 15:
                        player.classnotes.append("Spectral Defense - Your ability to move between planes enables you to slip through the planar boundaries to lessen the harm done to you during battle. When you take damage from an attack, you can use your reaction to give yourself resistance to all of that attack's damage on this turn.")
                if player.subclass[i] == "Hunter Archetype Ranger":
                    player.classnotes.append("Hunter's Prey (see notes)")
                    player.notes.append("Hunter's Prey - You gain one of the following features of your choice.\nColossus Slayer - Your tenacity can wear down the most potent foes. When you hit a creature with a weapon attack, the creature takes an extra 1d8 damage if it’s below its hit point maximum. You can deal this extra damage only once per turn.\nGiant Killer - When a Large or larger creature within 5 feet of you hits or misses you with an attack, you can use your reaction to attack that creature immediately after its attack, provided that you can see the creature.\nHorde Breaker - Once on each of your turns when you make a weapon attack, you can make another attack with the same weapon against a different creature that is within 5 feet of the original target and within range of your weapon.")
                    if ranlvl >= 7:
                        player.classnotes.append("Defensive Tactics (see notes)")
                        player.notes.append("Defensive Tactics - You gain one of the following features of your choice.\nEscape the Horde - Opportunity attacks against you are made with disadvantage.\nMultiattack Defense - When a creature hits you with an attack, you gain a +4 bonus to AC against all subsequent attacks made by that creature for the rest of the turn.\nSteel Will - You have advantage on saving throws against being frightened.")                             
                    if ranlvl >= 11:
                        player.classnotes.append("Multiattack (see notes)")
                        player.notes.append("Multiattack - You gain one of the following features of your choice.\nVolley - You can use your action to make a ranged attack against any number of creatures within 10 feet of a point you can see within your weapon’s range. You must have ammunition for each target, as normal, and you make a separate attack roll for each target\nWhirlwind Attack - You can use your action to make melee attacks against any number of creatures within 5 feet of you, with a separate attack roll for each target.")                             
                    if ranlvl >= 15:
                        player.classnotes.append("Superior Hunter's Defense (see notes)")
                        player.notes.append("Superior Hunter's Defense - You gain one of the following features of your choice.\nEvasion - When you are subjected to an effect, such as a red dragon’s fiery breath or a lightning bolt spell, that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on a saving throw, and only half damage if you fail\nStand Against the Tide - When a hostile creature misses you with a melee attack, you can use your reaction to force that creature to repeat the same attack against another creature (other than itself) of your choice.\nUncanny Dodge - When an attacker that you can see hits you with an attack, you can use your reaction to halve the attack’s damage against you.")
                if player.subclass[i] == "Monster Slayer Archetype Ranger":
                    RangerMonsterSlayerSpells = []
                    if ranlvl >= 3:
                        RangerMonsterSlayerSpells.append("Protection from Evil and Good")
                    if ranlvl >= 5:
                        RangerMonsterSlayerSpells.append("Zone of Truth")
                    if ranlvl >= 9:
                        RangerMonsterSlayerSpells.append("Magic Circle")
                    if ranlvl >= 13:
                        RangerMonsterSlayerSpells.append("Banishment")
                    if ranlvl >= 17:
                        RangerMonsterSlayerSpells.append("Hold Monster")
                    player.classnotes.append("Monster Slayer Magic (see notes)")
                    player.notes.append(f"Monster Slayer Magic - You learn an additional spell when you reach certain levels in this class. The spell counts as a ranger spell for you, but it doesn't count against the number of ranger spells you know. Currently, your Monster Slayer spells are: {RangerMonsterSlayerSpells}.")                    
                    player.classnotes.append("Hunter's Sense (see notes)")
                    player.notes.append(f"Hunter's Sense - You gain the ability to peer at a creature and magically discern how best to hurt it. As an action, choose one creature you can see within 60 feet of you. You immediately learn whether the creature has any damage immunities, resistances, or vulnerabilities and what they are. If the creature is hidden from divination magic, you sense that it has no damage immunities, resistances, or vulnerabilities.\nYou can use this feature a number of times equal to your Wisdom modifier, or {player.WisMod} times, minimum of once. You regain all expended uses of it when you finish a long rest.")
                    player.classnotes.append("Slayer's Prey (see notes)")
                    player.notes.append("Slayer's Prey - You can focus your ire on one foe, increasing the harm you inflict on it. As a bonus action, you designate one creature you can see within 60 feet of you as the target of this feature. The first time each turn that you hit that target with a weapon attack, it takes an extra 1d6 damage from the weapon.\nThis benefit lasts until you finish a short or long rest. It ends early if you designate a different creature.")
                    if ranlvl >= 7:
                        player.classnotes.append("Supernatural Defense - You gain extra resilience against your prey’s assaults on your mind and body. Whenever the target of your Slayer’s Prey forces you to make a saving throw and whenever you make an ability check to escape that target's grapple, add 1d6 to your roll.")
                    if ranlvl >= 11:
                        player.classnotes.append("Magic-User's Nemesis (see notes)")
                        player.notes.append(f"Magic-User's Nemesis - You gain the ability to thwart someone else's magic. When you see a creature casting a spell or teleporting within 60 feet of you, you can use your reaction to try to magically foil it. The creature must succeed on a Wisdom saving throw against your spell save DC, or against {player.spellsavedc[i]}, or its spell or teleport fails and is wasted.\nOnce you use this feature, you can't use it again until you finish a short or long rest.")
                    if ranlvl >= 15:
                        player.classnotes.append("Slayer's Counter (see notes)")
                        player.notes.append("Slayer's Counter - You gain the ability to counterattack when your prey tries to sabotage you. If the target of your Slayer’s Prey forces you to make a saving throw, you can use your reaction to make one weapon attack against the quarry. You make this attack immediately before making the saving throw. If the attack hits, your save automatically succeeds, in addition to the attack’s normal effects.")
                if player.subclass[i] == "Swarmkeeper Archetype Ranger": 
                    Swarm1 = "Swarming insects"
                    Swarm2 = "Miniature twig blights"
                    Swarm3 = "Fluttering birds"
                    Swarm4 = "Playful pixies"    
                    Swarm = [Swarm1, Swarm2, Swarm3, Swarm4]
                    if param == "Y":
                        print("0 - Random")
                        for r, swm in enumerate(Swarm, 1):
                            print(f"{r} - {swm}")                 
                        swarmkeeper = int(input("Choose the appearance of your Swarm. "))
                        if swarmkeeper == 0:
                            swarmchoice = random.choice(Swarm)
                        elif 1 <= swarmkeeper <= len(Swarm):
                            swarmchoice = Swarm[swarmkeeper - 1]
                    if param == "N":
                        swarmchoice = random.choice(Swarm)
                    RangerSwarmkeeperSpells = []
                    if ranlvl >= 3:
                        RangerSwarmkeeperSpells.append("Faerie Fire")
                        RangerSwarmkeeperSpells.append("Mage Hand")
                    if ranlvl >= 5:
                        RangerSwarmkeeperSpells.append("Web")
                    if ranlvl >= 9:
                        RangerSwarmkeeperSpells.append("Gaseous Form")
                    if ranlvl >= 13:
                        RangerSwarmkeeperSpells.append("Arcane Eye")
                    if ranlvl >= 17:
                        RangerSwarmkeeperSpells.append("Insect Plague")                        
                    player.classnotes.append("Gathered Swarm (see notes)")
                    player.notes.append(f"Gathered Swarm - A swarm of intangible nature spirits has bonded itself to you and can assist you in battle. Until you die, the swarm remains in your space, crawling on you or flying and skittering around you within your space. You can determine its appearance, which is: {swarmchoice}.\nOnce on each of your turns, you can cause the swarm to assist you in one of the following ways, immediately after you hit a creature with an attack:\n- The attack's target takes 1d6 piercing damage from the swarm.\n- The attack's target must succeed on a Strength saving throw against your spell save DC, or against {player.spellsavedc[i]}, or be moved by the swarm up to 15 feet horizontally in a direction of your choice.\n- You are moved by the swarm 5 feet horizontally in a direction of your choice.")
                    player.classnotes.append("Swarmkeeper Magic (see notes)")
                    player.notes.append(f"Swarmkeeper Magic - You learn the Mage Hand cantrip if you don't already know it. When you cast it, the hand takes the form of your swarming nature spirits.\nYou also learn an additional spell of 1st level or higher when you reach certain levels in this class. Each spell counts as a ranger spell for you, but it doesn't count against the number of ranger spells you know. Currently, your Swarmkeeper Spells are {RangerSwarmkeeperSpells}")
                    player.notes.append("It's Your Swarm - A Swarmkeeper's swarm and spells are reflections of the character's bond with nature spirits. Take the opportunity to describe the swarm and the ranger's magic in play. For example, when your ranger casts gaseous form, they might appear to melt into the swarm, instead of a cloud of mist, or the arcane eye spell could create an extension of your swarm that spies for you. Such descriptions don't change the effects of spells, but they are an exciting opportunity to explore your character's narrative through their class abilities. For more guidance on customizing spells, see the 'Personalizing Spells' section in chapter 3 of the Player's Handbook.\nAlso, remember that the swarm's appearance is yours to customize, and don't feel confined to a single appearance. Perhaps the spirits' look changes with the ranger's mood or with the seasons. You decide!")
                    if ranlvl >= 7:
                        player.classnotes.append("Writhing Tide (see notes)")
                        player.notes.append(f"Writhing Tide - You can condense part of your swarm into a focused mass that lifts you up. As a bonus action, you gain a flying speed of 10 feet and can hover. This effect lasts for 1 minute or until you are incapacitated.\nYou can use this feature a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.")                             
                    if ranlvl >= 11:
                        player.classnotes.append("Mighty Swarm (see notes)")
                        player.notes.append("Mighty Swarm - Your Gathered Swarm grows mightier in the following ways:\n- The damage of Gathered Swarm increases to 1d8.\n- If a creature fails its saving throw against being moved by Gathered Swarm, you can also cause the swarm to knock the creature prone.\n- When you are moved by Gathered Swarm, it gives you half cover until the start of your next turn.")                             
                    if ranlvl >= 15:
                        player.classnotes.append("Swarming Dispersal (see notes)")
                        player.notes.append(f"Swarming Dispersal - You can discorporate into your swarm, avoiding danger. When you take damage, you can use your reaction to give yourself resistance to that damage. You vanish into your swarm and then teleport to an unoccupied space that you can see within 30 feet of you, where you reappear with the swarm.\nYou can use this feature a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.")                                            
            player.classnotes.append("Primeval Awareness (see notes)")
            player.notes.append("Primeval Awareness - You can use your action and expend one ranger spell slot to focus your awareness on the region around you. For 1 minute per level of the spell slot you expend, you can sense whether the following types of creatures are present within 1 mile of you (or within up to 6 miles if you are in your favored terrain): aberrations, celestials, dragons, elementals, fey, fiends, and undead. This feature doesn’t reveal the creatures’ location or number.")                    
            PrimalAwareSpells = []
            PrimalAwareSpells.append("Speak With Animals")
            if ranlvl >= 5:
                PrimalAwareSpells.append("Beast Sense")
            if ranlvl >= 9:
                PrimalAwareSpells.append("Speak With Plants")
            if ranlvl >= 13:
                PrimalAwareSpells.append("Locate Creature")
            if ranlvl >= 17:
                PrimalAwareSpells.append("Commune With Nature")
                PrimalAwareSpells_str = ", ".join(f"{spell}" for spell in PrimalAwareSpells)
                player.classnotes.append("Primal Awareness (see notes)")
                player.notes.append(f"Primal Awareness - [Instead of Primeval Awareness] You can focus your awareness through the interconnections of nature: you learn additional spells when you reach certain levels in this class if you don't already know them. These spells don't count against the number of ranger spells you know.\nThe spells known are: {PrimalAwareSpells_str}.\nYou can cast each of these spells once without expending a spell slot. Once you cast a spell in this way, you can't do so again until you finish a long rest.")
            RangerSpellsKnown = 3
            RangerSpellSlot1 = 3        
            if ranlvl >= 4:
                player.classnotes.append("Martial Versatility - Whenever you reach a level in this class that grants the Ability Score Improvement feature, you can replace a fighting style you know with another fighting style available to rangers. This replacement represents a shift of focus in your martial practice.")
            if ranlvl >= 5:
                RangerSpellSlot1 = 4
                RangerSpellSlot2 = 2
                player.classnotes.append("Extra Attack - You can attack twice, instead of once, whenever you take the Attack action on your turn.")
            if ranlvl >= 6:
                player.classnotes.append("Favored Enemy(2) (see notes)")
                player.notes.append("Favored Enemy(2) - You have significant experience studying, tracking, hunting, and even talking to a certain type of enemy.\nChoose an additional type of favored enemy: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies.\nYou have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.\nWhen you gain this feature, you also learn one language of your choice that is spoken by your favored enemies, if they speak one at all.\nMore options are available at higher levels. As you gain levels, your choices should reflect the types of monsters you have encountered on your adventures.")
            if ranlvl >= 7:
                RangerSpellsKnown = 5
                RangerSpellSlot2 = 3
            if ranlvl >= 8:
                player.classnotes.append("Land’s Stride (see notes)")
                player.notes.append("Land’s Stride - Moving through nonmagical difficult terrain costs you no extra movement. You can also pass through nonmagical plants without being slowed by them and without taking damage from them if they have thorns, spines, or a similar hazard.\nIn addition, you have advantage on saving throws against plants that are magically created or manipulated to impede movement, such those created by the Entangle spell.")
            if ranlvl >= 9:
                RangerSpellsKnown = 6
                RangerSpellSlot3 = 2
            if ranlvl >= 10:
                player.classnotes.append("Hide in Plain Sight (see notes)")
                player.notes.append("Hide in Plain Sight - You can spend 1 minute creating camouflage for yourself. You must have access to fresh mud, dirt, plants, soot, and other naturally occurring materials with which to create your camouflage.\nOnce you are camouflaged in this way, you can try to hide by pressing yourself up against a solid surface, such as a tree or wall, that is at least as tall and wide as you are. You gain a +10 bonus to Dexterity (Stealth) checks as long as you remain there without moving or taking actions. Once you move or take an action or a reaction, you must camouflage yourself again to gain this benefit.")
                player.classnotes.append("Nature's Veil (see notes)")
                player.notes.append(f"Nature's Veil - You draw on the powers of nature to hide yourself from view briefly. As a bonus action, you can magically become invisible, along with any equipment you are wearing or carrying, until the start of your next turn.\nYou can use this feature a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
            if ranlvl >= 11:
                RangerSpellsKnown = 7
                RangerSpellSlot3 = 3
            if ranlvl >= 13:
                RangerSpellsKnown = 8
                RangerSpellSlot4 = 1
            if ranlvl >= 14:
                player.classnotes.append("Vanish - You can use the Hide action as a bonus action on your turn. Also, you can’t be tracked by nonmagical means, unless you choose to leave a trail.")
                player.classnotes.append("Favored Enemy(3) (see notes)")
                player.notes.append("Favored Enemy(3) - You have significant experience studying, tracking, hunting, and even talking to a certain type of enemy.\nChoose an additional type of favored enemy: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies.\nYou have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.\nWhen you gain this feature, you also learn one language of your choice that is spoken by your favored enemies, if they speak one at all.")
            if ranlvl >= 15:
                RangerSpellsKnown = 9
                RangerSpellSlot4 = 2
            if ranlvl >= 17:
                RangerSpellsKnown = 10
                RangerSpellSlot4 = 3
                RangerSpellSlot5 = 1
            if ranlvl >= 18:
                player.classnotes.append("Feral Senses (see notes)")
                player.notes.append("Feral Senses - You gain preternatural senses that help you fight creatures you can’t see. When you attack a creature you can’t see, your inability to see it doesn’t impose disadvantage on your attack rolls against it.\nYou are also aware of the location of any invisible creature within 30 feet of you, provided that the creature isn’t hidden from you and you aren’t blinded or deafened.")                
            if ranlvl >= 19:
                RangerSpellsKnown = 11
                RangerSpellSlot5 = 2
            if ranlvl == 20: 
                player.classnotes.append("Foe Slayer (see notes)")
                player.notes.append(f"Foe Slayer - You become an unparalleled hunter of your enemies. Once on each of your turns, you can add your Wisdom modifier, or {player.WisMod}, to the attack roll or the damage roll of an attack you make against one of your favored enemies. You can choose to use this feature before or after the roll, but before any effects of the roll are applied.")
            if ranlvl >= 2:
                player.notes.append(f"You know {RangerSpellsKnown} spells.")
                player.notes.append(f"The number of first level spell slots you have as a Ranger is: {RangerSpellSlot1}.")
            if RangerSpellSlot2 != 0:
                player.notes.append(f"The number of second level spell slots you have as a Ranger is: {RangerSpellSlot2}.")
            if RangerSpellSlot3 != 0:                
                player.notes.append(f"The number of third level spell slots you have as a Ranger is: {RangerSpellSlot3}.")
            if RangerSpellSlot4 != 0:
                player.notes.append(f"The number of fourth level spell slots you have as a Ranger is: {RangerSpellSlot4}.")
            if RangerSpellSlot5 != 0:
                player.notes.append(f"The number of fifth level spell slots you have as a Ranger is: {RangerSpellSlot5}.")             
        if player.Class[i] == "Rogue":
            if ((param == "N") or (player.singlemulticlass == "N")):
                roglvl = player.level
                player.classlvl.append(roglvl)
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    roglvl = int(input(f"Given your pool of levels of {poollevel}, what is your Rogue level? "))   
                    if roglvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                
                poollevel = poollevel - roglvl
                player.classlvl.append(roglvl)
            if roglvl >= 1:
                player.hitdice.append(f"{roglvl}d8 for {player.Class[i]}")
                if roglvl == 1:
                    player.hitpoints += (8 + player.ConMod)
                else:
                    player.hitpoints += (8 + player.ConMod + hpcalc(roglvl, dice, 8))     
                if i == 0:       
                    profs = ["Light Armor", "Simple Weapons",
                            dnd_tools.martial_weapons["HandCrossbow"]["Name"],
                            dnd_tools.martial_weapons["Longsword"]["Name"],
                            dnd_tools.martial_weapons["Rapier"]["Name"],
                            dnd_tools.martial_weapons["Shortsword"]["Name"]
                            ]     
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    player.proficiencies.append(dnd_tools.kits["ThievKit"]["Name"]) 
                    player.skills.append(dnd_tools.saving_throws["IntST"])
                    player.skills.append(dnd_tools.saving_throws["DexST"])
                    SkillsList = [
                        dnd_tools.skills["Acrobatics"], 
                        dnd_tools.skills["Athletics"], 
                        dnd_tools.skills["Deception"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Intimidation"], 
                        dnd_tools.skills["Investigation"], 
                        dnd_tools.skills["Perception"], 
                        dnd_tools.skills["Performance"], 
                        dnd_tools.skills["Persuasion"], 
                        dnd_tools.skills["SleightofHand"], 
                        dnd_tools.skills["Stealth"]
                        ]
                    player.skills = fourskillsfromlist(param, player.skills, SkillsList)   
                    StartEquip1 = ["Rapier", "Shortsword"]
                    StartEquip2 = ["Shortbow and Quiver of 20 Arrows", "Shortsword"]
                    StartEquip3 = ["Burglar's Pack", "Dungeoneer's Pack", "Explorer's Pack"]
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Rapier")
                        print("2 - Shortsword")
                        se1 = int(input("What would you like your first choice for starting equipment to be? "))
                        if se1 == 0:
                            SE1rand = random.choice(StartEquip1)
                            if SE1rand == "Rapier":
                                player.equipment.append(dnd_tools.martial_weapons["Rapier"].copy())
                            if SE1rand == "Shortsword":
                                 player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                        if se1 == 1:
                            player.equipment.append(dnd_tools.martial_weapons["Rapier"].copy())
                        if se1 == 2:
                             player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                        print("0 - Random")
                        print("1 - Shortbow and Quiver of 20 Arrows")
                        print("2 - Shortsword")
                        se2 = int(input("What would you like your second choice for starting equipment to be? "))
                        if se2 == 0:
                            SE2rand = random.choice(StartEquip2)
                            if SE2rand == "Shortbow and Quiver of 20 Arrows":
                                player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                                player.equipment.append("Quiver of 20 Arrows")
                            if SE2rand == "Shortsword":
                                 player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                        if se2 == 1:
                            player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                            player.equipment.append("Quiver of 20 Arrows")
                        if se2 == 2:
                             player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                        print("0 - Random")
                        print("1 - Burglar's Pack")
                        print("2 - Dungeoneer's Pack")
                        print("3 - Explorer's Pack")
                        se3 = int(input("What would you like your third choice for starting equipment to be? "))     
                        if se3 == 0:
                            SE3rand = random.choice(StartEquip3)
                            if SE3rand == "Burglar's Pack":
                                player.equipment.extend(dnd_tools.packs["BurglarsPack"]["contents"])
                            if SE3rand == "Dungeoneer's Pack":
                                player.equipment.extend(dnd_tools.packs["DungeoneersPack"]["contents"])
                            if SE3rand == "Explorer's Pack":
                                player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])
                        if se3 == 1:
                            player.equipment.extend(dnd_tools.packs["BurglarsPack"]["contents"])
                        if se3 == 2:
                            player.equipment.extend(dnd_tools.packs["DungeoneersPack"]["contents"])
                        if se3 == 3:
                            player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])
                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                        player.equipment.append(dnd_tools.kits["ThievKit"].copy())
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "Rapier":
                            player.equipment.append(dnd_tools.martial_weapons["Rapier"].copy())
                        if SE1rand == "Shortsword":
                            player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "Shortbow and Quiver of 20 Arrows":
                            player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                            player.equipment.append("Quiver of 20 Arrows")
                        if SE2rand == "Shortsword":
                             player.equipment.append(dnd_tools.martial_weapons["Shortsword"].copy())
                        SE3rand = random.choice(StartEquip3)
                        if SE3rand == "Burglar's Pack":
                            player.equipment.extend(dnd_tools.packs["BurglarsPack"]["contents"])
                        if SE3rand == "Dungeoneer's Pack":
                            player.equipment.extend(dnd_tools.packs["DungeoneersPack"]["contents"])
                        if SE3rand == "Explorer's Pack":
                            player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])                            
                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                        player.equipment.append(dnd_tools.kits["ThievKit"].copy())                                                   
                else:
                    profs = ["Light Armor"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    SkillsList = [
                        dnd_tools.skills["Acrobatics"], 
                        dnd_tools.skills["Athletics"], 
                        dnd_tools.skills["Deception"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Intimidation"], 
                        dnd_tools.skills["Investigation"], 
                        dnd_tools.skills["Perception"], 
                        dnd_tools.skills["Performance"], 
                        dnd_tools.skills["Persuasion"], 
                        dnd_tools.skills["SleightofHand"], 
                        dnd_tools.skills["Stealth"]
                        ]                            
                    player.skills = oneskillfromlist(param, player.skills, SkillsList)
                    player.proficiencies.append(dnd_tools.kits["ThievKit"]["Name"]) 
            SneakAttack = "1d6"
            player.classnotes.append("Thieves’ Cant (see notes)")
            player.notes.append("Thieves’ Cant - During your rogue training you learned thieves’ cant, a secret mix of dialect, jargon, and code that allows you to hide messages in seemingly normal conversation. Only another creature that knows thieves’ cant understands such messages. It takes four times longer to convey such a message than it does to speak the same idea plainly.\nIn addition, you understand a set of secret signs and symbols used to convey short, simple messages, such as whether an area is dangerous or the territory of a thieves’ guild, whether loot is nearby, or whether the people in an area are easy marks or will provide a safe house for thieves on the run.")
            if roglvl >= 2:
                player.classnotes.append("Cunning Action - Your quick thinking and agility allow you to move and act quickly. You can take a bonus action on each of your turns in combat. This action can be used only to take the Dash, Disengage, or Hide action.")                                      
            if roglvl >= 3:
                Rog = ["Arcane Trickster Archetype Rogue", "Assassin Archetype Rogue", "Inquisitive Archetype Rogue", "Mastermind Archetype Rogue", "Phantom Archetype Rogue", "Scout Archetype Rogue", "Soulknife Archetype Rogue", "Swashbuckler Archetype Rogue", "Thief Archetype Rogue"]
                

                if player.subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        for idx, subcl in enumerate(Rog, 1):
                            print(f"{idx} - {subcl}")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 0:
                            player.subclass[i] = random.choice(Rog)
                        elif 1 <= subc <= len(Rog):
                            player.subclass[i] = Rog[subc - 1]
                    if param == "N":
                        player.subclass[i] = random.choice(Rog)                               
                if player.subclass[i] == "Arcane Trickster Archetype Rogue":
                    player.spellcastingclass.append("Arcane Trickster Rogue")
                    player.spellcastingability.append("Int")
                    player.spellsavedc.append(8 + player.profbonus + player.IntMod)
                    player.spellattackmod.append(player.profbonus + player.IntMod)                    
                    ATRogueCantrips = 2
                    ATRogueSpellsKnown = 3
                    ATRogueSpellSlot1 = 2
                    ATRogueSpellSlot2 = 0
                    ATRogueSpellSlot3 = 0
                    ATRogueSpellSlot4 = 0
                    if roglvl >= 4:
                        ATRogueSpellsKnown = 4
                        ATRogueSpellSlot1 = 3
                    if roglvl >= 7:
                        ATRogueSpellsKnown = 5
                        ATRogueSpellSlot1 = 4
                        ATRogueSpellSlot2 = 2
                    if roglvl >= 8:
                        ATRogueSpellsKnown = 6
                    if roglvl >= 10:
                        ATRogueCantrips = 3
                        ATRogueSpellsKnown = 7
                        ATRogueSpellSlot2 = 3
                    if roglvl >= 11:
                        ATRogueSpellsKnown = 8
                    if roglvl >= 13:
                        ATRogueSpellsKnown = 9
                        ATRogueSpellSlot3 = 2 
                    if roglvl >= 14:
                        ATRogueSpellsKnown = 10                                               
                    if roglvl >= 16:
                        ATRogueSpellsKnown = 11
                        ATRogueSpellSlot3 = 3
                    if roglvl >= 19:
                        ATRogueSpellsKnown = 12
                        ATRogueSpellSlot4 = 1
                    if roglvl == 20:
                        ATRogueSpellsKnown = 13
                    player.notes.append(f"You know the Mage Hand Cantrip and {ATRogueCantrips} cantrips.")
                    player.notes.append(f"You know {ATRogueSpellsKnown} spells.")
                    player.notes.append(f"The number of first level spell slots you have as a Arcane Trickster Rogue is: {ATRogueSpellSlot1}.")
                    if ATRogueSpellSlot2 != 0:
                        player.notes.append(f"The number of second level spell slots you have as a Arcane Trickster Rogue is: {ATRogueSpellSlot2}.")
                    if ATRogueSpellSlot3 != 0:                
                        player.notes.append(f"The number of third level spell slots you have as a Arcane Trickster Rogue is: {ATRogueSpellSlot3}.")
                    if ATRogueSpellSlot4 != 0:
                        player.notes.append(f"The number of fourth level spell slots you have as a Arcane Trickster Rogue is: {ATRogueSpellSlot4}.")                    
                    player.classnotes.append("Mage Hand Legerdemain (see notes)")
                    player.notes.append("Mage Hand Legerdemain - When you cast Mage Hand, you can make the spectral hand invisible, and you can perform the following additional tasks with it:\n-You can stow one object the hand is holding in a container worn or carried by another creature.\n- You can retrieve an object in a container worn or carried by another creature.\n- You can use thieves' tools to pick locks and disarm traps at range.\nYou can perform one of these tasks without being noticed by a creature if you succeed on a Dexterity (Sleight of Hand) check contested by the creature's Wisdom (Perception) check.\nIn addition, you can use the bonus action granted by your Cunning Action to control the hand.")
                    if roglvl >= 9:
                        player.classnotes.append("Magical Ambush - If you are hidden from a creature when you cast a spell on it, the creature has disadvantage on any saving throw it makes against the spell this turn.")
                    if roglvl >= 13:
                        player.classnotes.append("Versatile Trickster - You gain the ability to distract targets with your Mage Hand. As a bonus action on your turn, you can designate a creature within 5 feet of the spectral hand created by the spell. Doing so gives you advantage on attack rolls against that creature until the end of the turn.")
                    if roglvl >= 17:
                        player.classnotes.append(f"Spell Thief - You gain the ability to magically steal the knowledge of how to cast a spell from another spellcaster.\nImmediately after a creature casts a spell that targets you or includes you in its area of effect, you can use your reaction to force the creature to make a saving throw with its spellcasting ability modifier. The DC equals your spell save DC, or {player.spellsavedc[i]}. On a failed save, you negate the spell's effect against you, and you steal the knowledge of the spell if it is at least 1st level and of a level you can cast (it doesn't need to be a wizard spell). For the next 8 hours, you know the spell and can cast it using your spell slots. The creature can't cast that spell until the 8 hours have passed.\nOnce you use this feature, you can't use it again until you finish a long rest.")
                if player.subclass[i] == "Assassin Archetype Rogue":
                    player.proficiencies.append(dnd_tools.kits["DisgKit"]["Name"])
                    player.proficiencies.append(dnd_tools.kits["PoisKit"]["Name"])
                    player.classnotes.append("Assassinate - You are at your deadliest when you get the drop on your enemies. You have advantage on attack rolls against any creature that hasn't taken a turn in the combat yet. In addition, any hit you score against a creature that is surprised is a critical hit.")
                    if roglvl >= 9:
                        player.classnotes.append("Infiltration Expertise (see notes)")
                        player.notes.append("Infiltration Expertise - You can unfailingly create false identities for yourself. You must spend seven days and 25 gp to establish the history, profession, and affiliations for an identity. You can't establish an identity that belongs to someone else. For example, you might acquire appropriate clothing, letters of introduction, and official- looking certification to establish yourself as a member of a trading house from a remote city so you can insinuate yourself into the company of other wealthy merchants.\nThereafter, if you adopt the new identity as a disguise, other creatures believe you to be that person until given an obvious reason not to.")
                    if roglvl >= 13:
                        player.classnotes.append("Impostor (see notes)")
                        player.notes.append("Impostor - You gain the ability to unerringly mimic another person's speech, writing, and behavior. You must spend at least three hours studying these three components of the person's behavior, listening to speech, examining handwriting, and observing mannerisms.\nYour ruse is indiscernible to the casual observer. If a wary creature suspects something is amiss, you have advantage on any Charisma (Deception) check you make to avoid detection.")
                    if roglvl >= 17:
                        player.classnotes.append("Death Strike (see notes)")
                        player.notes.append(f"Death Strike - You become a master of instant death. When you attack and hit a creature that is surprised, it must make a Constitution saving throw, DC 8 + your Dexterity modifier + your Proficiency Bonus, or DC {8 + player.DexMod + player.profbonus}. On a failed save, double the damage of your attack against the creature.")
                if player.subclass[i] == "Inquisitive Archetype Rogue":
                    player.classnotes.append("Ear for Deceit - You develop a keen ear for picking out lies. Whenever you make a Wisdom (Insight) check to determine whether a creature is lying, treat a roll of 7 or lower on the d20 as an 8.")
                    player.classnotes.append("Eye for Detail - You can use a bonus action to make a Wisdom (Perception) check to spot a hidden creature or object or to make an Intelligence (Investigation) check to uncover or decipher clues.")
                    player.classnotes.append("Insightful Fighting (see notes)")
                    player.notes.append("Insightful Fighting - You gain the ability to decipher an opponent’s tactics and develop a counter to them. As a bonus action, you make a Wisdom (Insight) check against a creature you can see that isn’t incapacitated, contested by the target’s Charisma (Deception) check. If you succeed, you can use your Sneak Attack against that target even if you don't have advantage on the attack roll, but not if you have disadvantage on it.\nThis benefit lasts for 1 minute or until you successfully use this feature against a different target.")
                    if roglvl >= 9:
                        player.classnotes.append("Steady Eye - You gain advantage on any Wisdom (Perception) or Intelligence (Investigation) check if you move no more than half your speed on the same turn.")
                    if roglvl >= 13:
                        player.classnotes.append("Unerring Eye (see notes)")
                        player.notes.append(f"Unerring Eye - Your senses are almost impossible to foil. As an action, you sense the presence of illusions, shapechangers not in their original form, and other magic designed to deceive the senses within 30 feet of you, provided you aren't blinded or deafened. You sense that an effect is attempting to trick you, but you gain no insight into what is hidden or into its true nature.\nYou can use this feature a number of times equal to your Wisdom modifier, or {player.WisMod} times, a minimum of once, and you regain all expended uses of it when you finish a long rest.")
                    if roglvl >= 17:
                        player.classnotes.append("Eye for Weakness - You learn to exploit a creature’s weaknesses by carefully studying its tactics and movement. While your Insightful Fighting feature applies to a creature, your Sneak Attack damage against that creature increases by 3d6.")                   
                if player.subclass[i] == "Mastermind Archetype Rogue":
                    player.proficiencies.append(dnd_tools.kits["DisgKit"]["Name"])
                    player.proficiencies.append(dnd_tools.kits["ForgKit"]["Name"]) 
                    player.proficiencies = gamingsets(param, player.proficiencies)  
                    player.languages, player.slang = languagegen(param, player.languages, player.slang)
                    player.languages, player.slang = languagegen(param, player.languages, player.slang)                 
                    player.classnotes.append("Master of Intrigue - You can unerringly mimic the speech patterns and accent of a creature that you hear speak for at least 1 minute, enabling you to pass yourself off as a native speaker of a particular land, provided that you know the language.")
                    player.classnotes.append("Master of Tactics - You can use the Help action as a bonus action. Additionally, when you use the Help action to aid an ally in attacking a creature, the target of that attack can be within 30 feet of you, rather than 5 feet of you, if the target can see or hear you.")
                    if roglvl >= 9:
                        player.classnotes.append("Insightful Manipulator (see notes)")
                        player.notes.append("Insightful Manipulator - If you spend at least 1 minute observing or interacting with another creature outside combat, you can learn certain information about its capabilities compared to your own. The DM tells you if the creature is your equal, superior, or inferior in regard to two of the following characteristics of your choice:\n- Intelligence score\n- Wisdom score\n- Charisma score\n- Class levels (if any)\nAt the DM's option, you might also realize you know a piece of the creature's history or one of its personality traits, if it has any.")
                    if roglvl >= 13:
                        player.classnotes.append("Misdirection - You can sometimes cause another creature to suffer an attack meant for you. When you are targeted by an attack while a creature within 5 feet of you is granting you cover against that attack, you can use your reaction to have the attack target that creature instead of you.")
                    if roglvl >= 17:
                        player.classnotes.append("Soul of Deceit (see notes)")
                        player.notes.append("Soul of Deceit - Your thoughts can't be read by telepathy or other means, unless you allow it. You can present false thoughts by making a Charisma (Deception) check contested by the mind reader's Wisdom (Insight) check.\nAdditionally, no matter what you say, magic that would determine if you are telling the truth indicates you are being truthful if you so choose, and you can't be compelled to tell the truth by magic.")
                if player.subclass[i] == "Phantom Archetype Rogue":
                    player.classnotes.append("Whispers of the Dead - Echoes of those who have died cling to you. Whenever you finish a short or long rest, you can choose one skill or tool proficiency that you lack and gain it, as a ghostly presence shares its knowledge with you. You lose this proficiency when you use this feature to choose a different proficiency that you lack.")
                    player.classnotes.append("Wails from the Grave (see notes)")
                    player.notes.append(f"Wails from the Grave - As you nudge someone closer to the grave, you can channel the power of death to harm someone else as well. Immediately after you deal your Sneak Attack damage to a creature on your turn, you can target a second creature that you can see within 30 feet of the first creature. Roll half the number of Sneak Attack dice for your level (round up), and the second creature takes necrotic damage equal to the roll's total, as wails of the dead sound around them for a moment.\nYou can use this feature a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
                    if roglvl >= 9:
                        player.classnotes.append("Tokens of the Departed (see notes)")
                        player.notes.append(f"Tokens of the Departed - When a life ends in your presence, you're able to snatch a token from the departing soul, a sliver of its life essence that takes physical form: as a reaction when a creature you can see dies within 30 feet of you, you can open your free hand and cause a Tiny trinket to appear there, a soul trinket. The DM determines the trinket's form or has you roll on the Trinkets table in the Player's Handbook to generate it.\nYou can have a maximum number of soul trinkets equal to a number of trinkets equal to your Proficiency Bonus, or {player.profbonus} trinkets, and you can't create one while at your maximum.\nYou can use soul trinkets in the following ways:\n- While a soul trinket is on your person, you have advantage on death saving throws and Constitution saving throws, for your vitality is enhanced by the life essence within the object.\n- When you deal Sneak Attack damage on your turn, you can destroy one of your soul trinkets that's on your person and then immediately use Wails from the Grave, without expending a use of that feature.\n- As an action, you can destroy one of your soul trinkets, no matter where it's located. When you do so, you can ask the spirit associated with the trinket one question. The spirit appears to you and answers in a language it knew in life. It's under no obligation to be truthful, and it answers as concisely as possible, eager to be free. The spirit knows only what it knew in life, as determined by the DM.")
                    if roglvl >= 13:
                        player.classnotes.append("Ghost Walk (see notes)")
                        player.notes.append("Ghost Walk - You can phase partially into the realm of the dead, becoming like a ghost. As a bonus action, you assume a spectral form. While in this form, you have a flying speed of 10 feet, you can hover, and attack rolls have disadvantage against you. You can also move through creatures and objects as if they were difficult terrain, but you take 1d10 force damage if you end your turn inside a creature or an object.\nYou stay in this form for 10 minutes or until you end it as a bonus action. To use this feature again, you must finish a long rest or destroy one of your soul trinkets as part of the bonus action you use to activate Ghost Walk.")
                    if roglvl >= 17:
                        player.classnotes.append("Death Knell (see notes)")
                        player.notes.append("Death Knell - Your association with death has become so close that you gain the following benefits:\n- When you use your Wails from the Grave, you can deal the necrotic damage to both the first and the second creature.\n- At the end of a long rest, a soul trinket appears in your hand if you don't have any soul trinkets, as the spirits of the dead are drawn to you.")
                if player.subclass[i] == "Scout Archetype Rogue":
                    player.classnotes.append("Skirmisher - You are difficult to pin down during a fight. You can move up to half your speed as a reaction when an enemy ends its turn within 5 feet of you. This movement doesn’t provoke opportunity attacks.")
                    sklprof = [dnd_tools.skills["Nature"], dnd_tools.skills["Survival"]]
                    for prof in sklprof:
                        if prof not in player.skills:
                            player.skills.append(prof)                   
                    player.classnotes.append("Survivalist - You gain proficiency in the Nature and Survival skills if you don't already have it (addressed). Your Proficiency Bonus is doubled for any ability check you make that uses either of those proficients.")
                    if roglvl >= 9:
                        player.classnotes.append("Superior Mobility - Your walking speed increases by 10 feet. If you have a climbing or swimming speed, this increase applies to that speed as well.")
                    if roglvl >= 13:
                        player.classnotes.append("Ambush Master (see notes)")
                        player.notes.append("Ambush Master - You excel at leading ambushes and acting first in a fight.\nYou have advantage on initiative rolls. In addition, the first creature you hit during the first round of a combat becomes easier for you and others to strike; attack rolls against that target have advantage until the start of your next turn.")
                    if roglvl >= 17:
                        player.classnotes.append("Sudden Strike (see notes)")
                        player.notes.append("Sudden Strike - You can strike with deadly speed. If you take the Attack action on your turn, you can make one additional attack as a bonus action. This attack can benefit from your Sneak Attack even if you have already used it this turn, but you can't use your Sneak Attack against the same target more than once in a turn.")
                if player.subclass[i] == "Soulknife Archetype Rogue":
                    SkPsionicEnergyDice = "d6"
                    if roglvl >= 5:
                        SkPsionicEnergyDice = "d8"
                    if roglvl >= 11:
                        SkPsionicEnergyDice = "d10"
                    if roglvl >= 17:
                        SkPsionicEnergyDice = "d12"
                    player.classnotes.append("Psionic Power (see notes)")
                    player.notes.append(f"Psionic Power - You harbor a wellspring of psionic energy within yourself. This energy is represented by your Psionic Energy dice, which are each a {SkPsionicEnergyDice}. You have a number of these dice equal to twice your Proficiency Bonus, or {2*player.profbonus} dice, and they fuel various psionic powers you have, which are detailed below.\nSome of your powers expend the Psionic Energy die they use, as specified in a power's description, and you can't use a power if it requires you to use a die when your dice are all expended. You regain all your expended Psionic Energy dice when you finish a long rest. In addition, as a bonus action, you can regain one expended Psionic Energy die, but you can't do so again until you finish a short or long rest.\nWhen you reach certain levels in this class, the size of your Psionic Energy dice increases (reflected in your damage dice).\nThe powers below use your Psionic Energy dice.\nPsi-Bolstered Knack - When your nonpsionic training fails you, your psionic power can help: if you fail an ability check using a skill or tool with which you have proficiency, you can roll one Psionic Energy die and add the number rolled to the check, potentially turning failure into success. You expend the die only if the roll succeeds.\nPsychic Whispers - You can establish telepathic communication between yourself and others-perfect for quiet infiltration. As an action, choose one or more creatures you can see, up to a number of creatures equal to your Proficiency Bonus, or {player.profbonus} creatures, and then roll one Psionic Energy die. For a number of hours equal to the number rolled, the chosen creatures can speak telepathically with you, and you can speak telepathically with them. To send or receive a message (no action required), you and the other creature must be within 1 mile of each other. A creature can't use this telepathy if it can't speak any languages, and a creature can end the telepathic connection at any time (no action required). You and the creature don't need to speak a common language to understand each other.\nThe first time you use this power after each long rest, you don't expend the Psionic Energy die. All other times you use the power, you expend the die.")
                    player.classnotes.append("Psychic Blades (see notes)")
                    player.notes.append("Psychic Blades - You can manifest your psionic power as shimmering blades of psychic energy. Whenever you take the Attack action, you can manifest a psychic blade from your free hand and make the attack with that blade. This magic blade is a simple melee weapon with the finesse and thrown properties. It has a normal range of 60 feet and no long range, and on a hit, it deals psychic damage equal to ld6 plus the ability modifier you used for the attack roll. The blade vanishes immediately after it hits or misses its target, and it leaves no mark on its target if it deals damage.\nAfter you attack with the blade, you can make a melee or ranged weapon attack with a second psychic blade as a bonus action on the same turn, provided your other hand is free to create it. The damage die of this bonus attack is 1d4, instead of 1d6.")
                    if roglvl >= 9:
                        player.classnotes.append("Soul Blades (see notes)")
                        player.notes.append("Soul Blades - Your Psychic Blades are now an expression of your psi-suffused soul, giving you these powers that use your Psionic Energy dice:\nHoming Strikes - If you make an attack roll with your Psychic Blades and miss the target, you can roll one Psionic Energy die and add the number rolled to the attack roll. If this causes the attack to hit, you expend the Psionic Energy die.\nPsychic Teleportation - As a bonus action, you manifest one of your Psychic Blades, expend one Psionic Energy die and roll it, and throw the blade at an unoccupied space you can see, up to a number of feet away equal to 10 times the number rolled. You then teleport to that space, and the blade vanishes.")
                    if roglvl >= 13:
                        player.classnotes.append("Psychic Veil (see notes)")
                        player.notes.append("Psychic Veil - You can weave a veil of psychic static to mask yourself. As an action, you can magically become invisible, along with anything you are wearing or carrying, for 1 hour or until you dismiss this effect (no action required). This invisibility ends early immediately after you deal damage to a creature or you force a creature to make a saving throw.\nOnce you use this feature, you can't do so again until you finish a long rest, unless you expend a Psionic Energy die to use this feature again.")
                    if roglvl >= 17:
                        player.classnotes.append("Rend Mind (see notes)")
                        player.notes.append(f"Rend Mind - You can sweep your Psychic Blades directly through a creature's mind. When you use your Psychic Blades to deal Sneak Attack damage to a creature, you can force that target to make a Wisdom saving throw (DC equal to 8 + your Proficiency Bonus + your Dexterity modifier, or DC {8 + player.profbonus + player.DexMod}). If the save fails, the target is stunned for 1 minute. The stunned target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.\nOnce you use this feature, you can't do so again until you finish a long rest, unless you expend three Psionic Energy dice to use it again.")
                if player.subclass[i] == "Swashbuckler Archetype Rogue":
                    player.classnotes.append("Fancy Footwork - You learn how to land a strike and then slip away without reprisal. During your turn, if you make a melee attack against a creature, that creature can't make opportunity attacks against you for the rest of your turn.")
                    player.classnotes.append("Rakish Audacity (see notes)")
                    player.notes.append(f"Rakish Audacity - Your confidence propels you into battle. You can give yourself a bonus to your initiative rolls equal to your Charisma modifier, or a bonus of {player.ChaMod}.\nYou also gain an additional way to use your Sneak Attack; you don't need advantage on the attack roll to use your Sneak Attack against a creature if you are within 5 feet of it, no other creatures are within 5 feet of you, and you don't have disadvantage on the attack roll. All the other rules for Sneak Attack still apply to you.")
                    if roglvl >= 9:
                        player.classnotes.append("Panache (see notes)")
                        player.notes.append("Panache - Your charm becomes extraordinarily beguiling. As an action, you can make a Charisma (Persuasion) check contested by a creature's Wisdom (Insight) check. The creature must be able to hear you, and the two of you must share a language.\nIf you succeed on the check and the creature is hostile to you, it has disadvantage on attack rolls against targets other than you and can't make opportunity attacks against targets other than you. This effect lasts for 1 minute, until one of your companions attacks the target or affects it with a spell, or until you and the target are more than 60 feet apart.\nIf you succeed on the check and the creature isn't hostile to you, it is charmed by you for 1 minute. While charmed, it regards you as a friendly acquaintance. This effect ends immediately if you or your companions do anything harmful to it.")
                    if roglvl >= 13:
                        player.classnotes.append("Elegant Maneuver - You can use a bonus action on your turn to gain advantage on the next Dexterity (Acrobatics) or Strength (Athletics) check you make during the same turn.")
                    if roglvl >= 17:
                        player.classnotes.append("Master Duelist - Your mastery of the blade lets you turn failure into success in combat. If you miss with an attack roll, you can roll it again with advantage. Once you do so, you can't use this feature again until you finish a short or long rest.")
                if player.subclass[i] == "Thief Archetype Rogue":        
                    player.classnotes.append("Fast Hands - You can use the bonus action granted by your Cunning Action to make a Dexterity (Sleight of Hand) check, use your thieves' tools to disarm a trap or open a lock, or take the Use an Object action.")
                    player.classnotes.append(f"Second-Story Work - You gain the ability to climb faster than normal; climbing no longer costs you extra movement.\nIn addition, when you make a running jump, the distance you cover increases by a number of feet equal to your Dexterity modifier, or {player.DexMod} feet.")
                    if roglvl >= 9:
                        player.classnotes.append("Supreme Sneak - You have advantage on a Dexterity (Stealth) check if you move no more than half your speed on the same turn.")
                    if roglvl >= 13:
                        player.classnotes.append("Use Magic Device - You have learned enough about the workings of magic that you can improvise the use of items even when they are not intended for you. You ignore all class, race, and level requirements on the use of magic items.")
                    if roglvl >= 17:
                        player.classnotes.append("Thief's Reflexes - You have become adept at laying ambushes and quickly escaping danger. You can take two turns during the first round of any combat. You take your first turn at your normal initiative and your second turn at your initiative minus 10. You can't use this feature when you are surprised.")
            SneakAttack = "2d6"
            player.classnotes.append("Steady Aim - As a bonus action, you give yourself advantage on your next attack roll on the current turn. You can use this bonus action only if you haven't moved during this turn, and after you use the bonus action, your speed is 0 until the end of the current turn.")
            if roglvl >= 4:
                player.classnotes.append("Uncanny Dodge - When an attacker that you can see hits you with an attack, you can use your reaction to halve the attack’s damage against you.")
            if roglvl >= 5:
                SneakAttack = "3d6"
            if roglvl >= 6:
                player.classnotes.append("Expertise - Choose two more of your skill proficiencies, or one more of your skill proficiencies and your proficiency with thieves’ tools. Your Proficiency Bonus is doubled for any ability check you make that uses either of the chosen proficiencies.")
            if roglvl >= 7:
                SneakAttack = "4d6"
                player.classnotes.append("Evasion (see notes)")
                player.notes.append("Evasion - You can nimbly dodge out of the way of certain area effects, such as an Ancient Red Dragon’s fiery breath or an Ice Storm spell. When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw, and only half damage if you fail.")
            if roglvl >= 9:
                SneakAttack = "5d6"
            if roglvl >= 11:
                SneakAttack = "6d6"
                player.classnotes.append("Reliable Talent - You have refined your chosen skills until they approach perfection. Whenever you make an ability check that lets you add your Proficiency Bonus, you can treat a d20 roll of 9 or lower as a 10.")
            if roglvl >= 13:
                SneakAttack = "7d6"
            if roglvl >= 14:
                player.classnotes.append("Blindsense - If you are able to hear, you are aware of the location of any hidden or invisible creature within 10 feet of you.")
            if roglvl >= 15:
                SneakAttack = "8d6"
                player.skills.append(dnd_tools.saving_throws["WisST"])
            if roglvl >= 17:
                SneakAttack = "9d6"
            if roglvl >= 18:
                player.classnotes.append("Elusive - You are so evasive that attackers rarely gain the upper hand against you. No attack roll has advantage against you while you aren’t incapacitated.")
            if roglvl >= 19:
                SneakAttack = "10d6"
            if roglvl == 20:   
                player.classnotes.append("Stroke of Luck - You have an uncanny knack for succeeding when you need to. If your attack misses a target within range, you can turn the miss into a hit. Alternatively, if you fail an ability check, you can treat the d20 roll as a 20.\nOnce you use this feature, you can’t use it again until you finish a short or long rest.")
            player.classnotes.append("Sneak Attack (see notes)")
            player.notes.append(f"Sneak Attack - You know how to strike subtly and exploit a foe’s distraction. Once per turn, you can deal an extra {SneakAttack} damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon.\nYou don’t need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn’t incapacitated, and you don’t have disadvantage on the attack roll.\nThe amount of the extra damage increases as you gain levels in this class.")     
        if player.Class[i] == "Sorcerer":
            if ((param == "N") or (player.singlemulticlass == "N")):
                sorclvl = player.level
                player.classlvl.append(sorclvl)              
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    sorclvl = int(input(f"Given your pool of levels of {poollevel}, what is your Sorcerer level? "))  
                    if sorclvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                
                poollevel = poollevel - sorclvl
                player.classlvl.append(sorclvl)
            if sorclvl >= 1:
                player.hitdice.append(f"{sorclvl}d6 for {player.Class[i]}")
                if sorclvl == 1:
                    player.hitpoints += (6 + player.ConMod)
                else:
                    player.hitpoints += (6 + player.ConMod + hpcalc(sorclvl, dice, 6))         
                if i == 0: 
                    profs = [
                        dnd_tools.simple_weapons["Dagger"]["Name"],
                        dnd_tools.simple_weapons["Dart"]["Name"],
                        dnd_tools.simple_weapons["Sling"]["Name"],
                        dnd_tools.simple_weapons["Quarterstaff"]["Name"],
                        dnd_tools.simple_weapons["LightCrossbow"]["Name"]
                        ]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)       
                    player.skills.append(dnd_tools.saving_throws["ConST"])
                    player.skills.append(dnd_tools.saving_throws["ChaST"])
                    SkillsList = [
                        dnd_tools.skills["Arcana"], 
                        dnd_tools.skills["Deception"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Intimidation"], 
                        dnd_tools.skills["Persuasion"], 
                        dnd_tools.skills["Religion"]
                        ]
                    player.skills = twoskillsfromlist(param, player.skills, SkillsList)  
                    StartEquip1 = ["A Light Crossbow and 20 Bolts", "Any Simple Weapon"]
                    StartEquip2 = ["A Component Pouch", "An Arcane Focus"]
                    StartEquip3 = ["Dungeoneer's Pack", "Explorer's Pack"]
                    if param == "Y":
                        print("0 - Random")
                        print("1 - A Light Crossbow and 20 Bolts")
                        print("2 - Any Simple Weapon")
                        se1 = int(input("What would you like your first choice for starting equipment to be? "))
                        if se1 == 0:
                            SE1rand = random.choice(StartEquip1)
                            if SE1rand == "A Light Crossbow and 20 Bolts":
                                player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                                player.equipment.append("20 Bolts")
                            if SE1rand == "Any Simple Weapon":
                                SimpRandKey = random.choice(SimpleWeapons)
                                player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                        if se1 == 1:
                            player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                            player.equipment.append("20 Bolts")
                        if se1 == 2:
                            print("0 - Random")
                            for j, sw in enumerate(SimpleWeaponsNames, 1):
                                print(f"{j} - {sw}")
                            se1 = int(input("Which simple weapon would you like to add to your inventory? "))
                            if se1 == 0:
                                SimpRandKey = random.choice(SimpleWeapons)
                                player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                            elif 1 <= se1 <= len(SimpleWeapons):
                                SimpKey = SimpleWeapons[se1-1]
                                player.equipment.append(dnd_tools.simple_weapons[SimpKey].copy())
                        print("0 - Random")
                        print("1 - A Component Pouch")
                        print("2 - An Arcane Focus")
                        se2 = int(input("What would you like your second choice for starting equipment to be? "))
                        if se2 == 0:
                            SE2rand = random.choice(StartEquip2)
                            if SE2rand == "A Component Pouch":
                                player.equipment.append("Component Pouch")
                            if SE2rand == "An Arcane Focus":
                                player.equipment.append("Arcane Focus")
                        if se2 == 1:
                            player.equipment.append("Component Pouch")
                        if se2 == 2:
                            player.equipment.append("Arcane Focus")
                        print("0 - Random")
                        print("1 - Dungeoneer's Pack")
                        print("2 - Explorer's Pack")
                        se3 = int(input("What would you like your third choice for starting equipment to be? "))  
                        if se3 == 0:
                            SE3rand = random.choice(StartEquip3)
                            if SE3rand == "Dungeoneer's Pack":
                                player.equipment.extend(dnd_tools.packs["DungeoneersPack"]["contents"])
                            if SE3rand == "Explorer's Pack":
                                player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])
                        if se3 == 1:
                            player.equipment.extend(dnd_tools.packs["DungeoneersPack"]["contents"])
                        if se3 == 2:    
                            player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])                  
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "A Light Crossbow and 20 Bolts":
                            player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                            player.equipment.append("20 Bolts")
                        if SE1rand == "Any Simple Weapon":
                            SimpRandKey = random.choice(SimpleWeapons)
                            player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "A Component Pouch":
                            player.equipment.append("Component Pouch")
                        if SE2rand == "An Arcane Focus":
                            player.equipment.append("Arcane Focus")
                        SE3rand = random.choice(StartEquip3)
                        if SE3rand == "Dungeoneer's Pack":
                            player.equipment.extend(dnd_tools.packs["DungeoneersPack"]["contents"])
                        if SE3rand == "Explorer's Pack":
                            player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])                            
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())  
                player.spellcastingclass.append("Sorcerer")
                player.spellcastingability.append("Cha")
                player.spellsavedc.append(8 + player.profbonus + player.ChaMod)
                player.spellattackmod.append(player.profbonus + player.ChaMod)
                SorcCantripsKnown = 4
                SorcSpellsKnown = 2
                SorcSpellSlot1 = 2
                SorcSpellSlot2 = 0
                SorcSpellSlot3 = 0
                SorcSpellSlot4 = 0
                SorcSpellSlot5 = 0
                SorcSpellSlot6 = 0
                SorcSpellSlot7 = 0
                SorcSpellSlot8 = 0
                SorcSpellSlot9 = 0                                                        
                Sor = ["Aberrant Mind Origin Sorcerer", "Clockwork Soul Origin Sorcerer", "Divine Soul Origin Sorcerer", "Draconic Bloodline Origin Sorcerer", "Lunar Magic Origin Sorcerer", "Runechild Origin Sorcerer", "Shadow Origin Sorcerer", "Storm Origin Sorcerer", "Wild Magic Origin Sorcerer"]
                
                print(f"Subclasses are: {player.subclass}")
                if player.subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        for idx, subcl in enumerate(Sor, 1):
                            print(f"{idx} - {subcl}")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 0:
                            player.subclass[i] = random.choice(Sor)
                        elif 1 <= subc <= len(Sor):
                            player.subclass[i] = Sor[subc - 1]
                    if param == "N":
                        player.subclass[i] = random.choice(Sor)                                  
                if player.subclass[i] == "Aberrant Mind Origin Sorcerer":
                    AbSO1 = "You were exposed to the Far Realm's warping influence. You are confinced that a tentacle is now growing on you, but no one else can see it."
                    AbSO2 = "A psychic wind from the Astral Plane carried psionic energy to you. When you use your powers, faint motes of light sparkle around you."
                    AbSO3 = "You once suffered the dominating powers of an aboleth, leaving a psychic splinter in your mind."
                    AbSO4 = "You were implanted with a mind flayer tadpole, but the ceremorphosis never completed. And now its psionic power is yours. When you use it, your flesh shines with a strange mucus."
                    AbSO5 = "As a child, you had an imaginary friend that looked like a flumph or a strange platypus-like creature. One day, it gifted you with psionic powers, which have ended up being not so imaginary."
                    AbSO6 = "Your nightmares whisper the truth to you: your psionic powers are not your own. You draw them from your parasitic twin."
                    AbSO = [AbSO1, AbSO2, AbSO3, AbSO4, AbSO5, AbSO6]
                    AberrantOrigin = random.choice(AbSO)
                    player.classnotes.append(f"As an Aberrant Mind Origin Sorcerer, the Aberrant Origin is {AberrantOrigin}")     
                    SorcAberrantMindSpells = []
                    if sorclvl >= 1:
                        SorcAberrantMindSpells.append("Arms of Hadar")
                        SorcAberrantMindSpells.append("Dissonant Whispers")
                        SorcAberrantMindSpells.append("Mind Sliver")
                    if sorclvl >= 3:
                        SorcAberrantMindSpells.append("Calm Emotions")
                        SorcAberrantMindSpells.append("Detect Thoughts")
                    if sorclvl >= 5:
                        SorcAberrantMindSpells.append("Hunger of Hadar")
                        SorcAberrantMindSpells.append("Sending")
                    if sorclvl >= 7:
                        SorcAberrantMindSpells.append("Evard's Black Tentacles")
                        SorcAberrantMindSpells.append("Summon Aberration")
                    if sorclvl >= 9:
                        SorcAberrantMindSpells.append("Rary's Telepathic Bond")
                        SorcAberrantMindSpells.append("Telekinesis")
                    player.classnotes.append("Psionic Spells (see notes)")
                    player.notes.append(f"Psionic Spells - You learn additional spells when you reach certain levels in this class. Each of these spells counts as a sorcerer spell for you, but it doesn't count against the number of sorcerer spells you know, currently you know: {SorcAberrantMindSpells}\nWhenever you gain a Sorcerer level, you can replace one spell you gained from this feature with another spell of the same level. The new spell must be a divination or an enchantment spell from the sorcerer, warlock, or wizard spell list.")
                    player.classnotes.append("Telepathic Speech (see notes)")
                    player.notes.append(f"Telepathic Speech - You can form a telepathic connection between your mind and the mind of another. As a bonus action, choose one creature you can see within 30 feet of you. You and the chosen creature can speak telepathically with each other while the two of you are within a number of miles of each other equal to your Charisma modifier, or {player.ChaMod} miles, minimum of 1 mile. To understand each other, you each must speak mentally in a language the other knows.\nThe telepathic connection lasts for an amount of minutes equal to your Sorcerer level, or {sorclvl} minutes. It ends early if you are incapacitated or die or if you use this ability to form a connection with a different creature.")
                    if sorclvl >= 6:
                        player.classnotes.append("Psionic Sorcery (see notes)")
                        player.notes.append("Psionic Sorcery - When you cast any spell of 1st level or higher from your Psionic Spells feature, you can cast it by expending a spell slot as normal or by spending a number of sorcery points equal to the spell's level. If you cast the spell using sorcery points, it requires no verbal or somatic components, and it requires no material components, unless they are consumed by the spell.")
                        player.classnotes.append("Psychic Defenses - You gain resistance to psychic damage, and you have advantage on saving throws against being charmed or frightened.")
                    if sorclvl >= 14:
                        player.classnotes.append("Revelation in Flesh (see notes)")
                        player.notes.append("Revelation in Flesh - You can unleash the aberrant truth hidden within yourself. As a bonus action, you can spend 1 or more sorcery points to magically transform your body for 10 minutes. For each sorcery point you spend, you can gain one of the following benefits of your choice, the effects of which last until the transformation ends:\n- You can see any invisible creature within 60 feet of you, provided it isn't behind total cover. Your eyes also turn black or become writhing sensory tendrils.\n- You gain a flying speed equal to your walking speed, and you can hover. As you fly, your skin glistens with mucus or shines with an otherworldly light.\n- You gain a swimming speed equal to twice your walking speed, and you can breathe underwater. Moreover, gills grow from your neck or fan out from behind your ears, your fingers become webbed, or you grow writhing cilia that extend through your clothing.\n- Your body, along with any equipment you are wearing or carrying, becomes slimy and pliable. You can move through any space as narrow as 1 inch without squeezing, and you can spend 5 feet of movement to escape from nonmagical restraints or being grappled.")
                    if sorclvl >= 18:
                        player.classnotes.append("Warping Implosion (see notes)")
                        player.notes.append("Warping Implosion - You can unleash your aberrant power as a space-warping anomaly. As an action, you can teleport to an unoccupied space you can see within 120 feet of you. Immediately after you disappear, each creature within 30 feet of the space you left must make a Strength saving throw. On a failed save, a creature takes 3d10 force damage and is pulled straight toward the space you left, ending in an unoccupied space as close to your former space as possible. On a successful save, the creature takes half as much damage and isn't pulled.\nOnce you use this feature, you can't do so again until you finish a long rest, unless you spend 5 sorcery points to use it again.")                       
                if player.subclass[i] == "Clockwork Soul Origin Sorcerer":
                    SorcClockworkSoulSpells = []
                    if sorclvl >= 1:
                        SorcClockworkSoulSpells.append("Alarm")
                        SorcClockworkSoulSpells.append("Protection From Evil and Good")
                    if sorclvl >= 3:
                        SorcClockworkSoulSpells.append("Aid")
                        SorcClockworkSoulSpells.append("Lesser Restoration")
                    if sorclvl >= 5:
                        SorcClockworkSoulSpells.append("Dispel Magic")
                        SorcClockworkSoulSpells.append("Protection From Energy")
                    if sorclvl >= 7:
                        SorcClockworkSoulSpells.append("Freedom of Movement")
                        SorcClockworkSoulSpells.append("Summon Construct")
                    if sorclvl >= 9:
                        SorcClockworkSoulSpells.append("Greater Restoration")
                        SorcClockworkSoulSpells.append("Wall of Force")
                    player.classnotes.append("Clockwork Magic (see notes)")
                    player.notes.append(f"Clockwork Magic - You learn additional spells when you reach certain levels in this class. Each of these spells counts as a sorcerer spell for you, but it doesn't count against the number of sorcerer spells you know, currently you know: {SorcClockworkSoulSpells}\nWhenever you gain a Sorcerer level, you can replace one spell you gained from this feature with another spell of the same level. The new spell must be an abjuration or a transmutation spell from the sorcerer, warlock, or wizard spell list.")
                    ManOrd1 = "Spectral cogwheels hover behind you."
                    ManOrd2 = "The hands of a clock spin in your eyes."
                    ManOrd3 = "Your skin glows with a brassy sheen."
                    ManOrd4 = "Floating equations and geometric objects overlay your body."
                    ManOrd5 = "Your spellcasting focus temporarily takes the form of a Tiny clockwork mechanism."
                    ManOrd6 = "The ticking of gears or ringing of a clock can be heard by you and those affected by your magic."
                    ManOrd = [ManOrd1, ManOrd2, ManOrd3, ManOrd4, ManOrd5, ManOrd6]
                    if param == "Y":
                        print("0 - Random")
                        for s, manorder in enumerate(ManOrd, 1):
                            print(f"{s} - {manorder}")
                        manordinput = int(input("Choose which Manifestation of Order you wish to go with your Clockwork Soul Origin. "))
                        if manordinput == 0:
                            ManOrdChoice = random.choice(ManOrd)
                        elif 1 <= manordinput <= len(ManOrd):
                            ManOrdChoice = ManOrd[manordinput-1] 
                    if param == "N":
                         ManOrdChoice = random.choice(ManOrd)
                    player.classnotes.append("Clockwork Magic(2) (see notes)")
                    player.notes.append(f"Clockwork Magic(2) - In addition, you chose which Manifestation of Order to go with your Clockwork Soul Origin, determining a way your connection to order manifests while you are casting any of your sorcerer spells, which is: {ManOrdChoice}")
                    player.classnotes.append("Restore Balance (see notes)")
                    player.notes.append(f"Restore Balance - Your connection to the plane of absolute order allows you to equalize chaotic moments. When a creature you can see within 60 feet of you is about to roll a d20 with advantage or disadvantage, you can use your reaction to prevent the roll from being affected by advantage and disadvantage.\nYou can use this feature a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
                    if sorclvl >= 6:
                        player.classnotes.append("Bastion of Law (see notes)")
                        player.notes.append("Bastion of Law - You can tap into the grand equation of existence to imbue a creature with a shimmering shield of order. As an action, you can expend 1 to 5 sorcery points to create a magical ward around yourself or another creature you can see within 30 feet of you. The ward lasts until you finish a long rest or until you use this feature again.\nThe ward is represented by a number of d8s equal to the number of sorcery points spent to create it. When the warded creature takes damage, it can expend a number of those dice, roll them, and reduce the damage taken by the total rolled on those dice.")
                    if sorclvl >= 14:
                        player.classnotes.append("Trance of Order (see notes)")
                        player.notes.append("Trance of Order - You gain the ability to align your consciousness to the endless calculations of Mechanus. As a bonus action, you can enter this state for 1 minute. For the duration, attack rolls against you can't benefit from advantage, and whenever you make an attack roll, an ability check, or a saving throw, you can treat a roll of 9 or lower on the d20 as a 10.\nOnce you use this bonus action, you can't use it again until you finish a long rest, unless you spend 5 sorcery points to use it again.")
                    if sorclvl >= 18:
                        player.classnotes.append("Clockwork Cavalcade (see notes)")
                        player.notes.append("Clockwork Cavalcade - You summon spirits of order to expunge disorder around you. As an action, you summon the spirits in a 30-foot cube originating from you. The spirits look like modrons or other constructs of your choice. The spirits are intangible and invulnerable, and they create the following effects within the cube before vanishing:\n- The spirits restore up to 100 hit points, divided as you choose among any number of creatures of your choice in the cube.\n- Any damaged objects entirely in the cube are repaired instantly.\n- Every spell of 6th level or lower ends on creatures and objects of your choice in the cube.\nOnce you use this action, you can't use it again until you finish a long rest, unless you spend 7 sorcery points to use it again.")                       
                if player.subclass[i] == "Divine Soul Origin Sorcerer":
                    SorcDivineSoulSpells = []
                    if sorclvl >= 1:
                        SorcDivineSoulSpells.append("Alarm")
                        SorcDivineSoulSpells.append("Protection From Evil and Good")
                    if sorclvl >= 3:
                        SorcDivineSoulSpells.append("Aid")
                        SorcDivineSoulSpells.append("Lesser Restoration")
                    if sorclvl >= 5:
                        SorcDivineSoulSpells.append("Dispel Magic")
                        SorcDivineSoulSpells.append("Protection From Energy")
                    if sorclvl >= 7:
                        SorcDivineSoulSpells.append("Freedom of Movement")
                        SorcDivineSoulSpells.append("Summon Construct")
                    if sorclvl >= 9:
                        SorcDivineSoulSpells.append("Greater Restoration")
                        SorcDivineSoulSpells.append("Wall of Force")
                    affinity_spells = {
                        "Good": "Cure Wounds",
                        "Evil": "Inflict Wounds",
                        "Law": "Bless",
                        "Chaos": "Bane",
                        "Neutrality": "Protection from Evil and Good"
                    }
                    if param == "Y":
                        print("0 - Random")
                        for idx, affinity in enumerate(affinity_spells.keys(), 1):
                            print(f"{idx} - {affinity}")
                        choice = int(input("Choose an affinity for the source of your divine power. "))
                        if choice == 0:
                            selected_affinity = random.choice(list(affinity_spells.keys()))
                        elif 1 <= choice <= len(affinity_spells):
                            selected_affinity = list(affinity_spells.keys())[choice - 1]
                    if param == "N":
                        selected_affinity = random.choice(list(affinity_spells.keys()))
                    selected_spell = affinity_spells[selected_affinity]
                    player.classnotes.append("Divine Magic (see notes)")
                    player.notes.append(f"Divine Magic - Your link to the divine allows you to learn spells normally associated with the cleric class. When your Spellcasting feature lets you learn a sorcerer cantrip or a sorcerer spell of 1st level or higher, you can choose the new spell from the cleric spell list or the sorcerer spell list. You must otherwise obey all the restrictions for selecting the spell, and it becomes a sorcerer spell for you.\nIn addition, you chose an affinity for the source of your divine power, which is {selected_affinity}, and you lean an additional spell based on that affinity, which is {selected_spell}. It is a sorcerer spell for you, but it doesn't count against your number of sorcerer spells known. If you later replace this spell, you must replace it with a spell from the cleric spell list.")
                    player.classnotes.append("Favored by the Gods - Divine power guards your destiny. If you fail a saving throw or miss with an attack roll, you can roll 2d4 and add it to the total, possibly changing the outcome.\nOnce you use this feature, you can’t use it again until you finish a short or long rest.")
                    if sorclvl >= 6:
                        player.classnotes.append("Empowered Healing (see notes)")
                        player.notes.append("Empowered Healing - The divine energy coursing through you can empower healing spells. Whenever you or an ally within 5 feet of you rolls dice to determine the number of hit points a spell restores, you can spend 1 sorcery point to reroll any number of those dice once, provided you aren't incapacitated. You can use this feature only once per turn.")
                    if sorclvl >= 14:
                        player.classnotes.append("Angelic Form (see notes)")
                        player.notes.append("Angelic Form - You can use a bonus action to manifest a pair of spectral wings from your back. While the wings are present, you have a flying speed of 30 feet. The wings last until you're incapacitated, you die, or you dismiss them as a bonus action.\nThe affinity you chose for your Divine Magic feature determines the appearance of the spectral wings: eagle wings for good or law, bat wings for evil or chaos, and dragonfly wings for neutrality.")
                    if sorclvl >= 18:
                        player.classnotes.append(f"Unearthly Recovery - You gain the ability to overcome grievous injuries. As a bonus action when you have fewer than half of your hit points remaining, you can regain a number of hit points equal half your hitpoints, or {math.ceil(hitpoints/2)} hit points.\nOnce you use this feature, you can’t use it again until you finish a long rest.")
                if player.subclass[i] == "Draconic Bloodline Origin Sorcerer":
                    dragon_damage = {
                        "Black": "Acid",
                        "Blue": "Lightning",
                        "Brass": "Fire",
                        "Bronze": "Lightning",
                        "Copper": "Acid",
                        "Gold": "Fire",
                        "Green": "Poison",
                        "Red": "Fire",
                        "Silver": "Cold",
                        "White": "Cold"
                    }
                    if param == "Y":
                        print("0 - Random")
                        for idx, color in enumerate(dragon_damage.keys(), 1):
                            print(f"{idx} - {color}")
                        choice = int(input("Choose a dragon color, and thus damage type. "))
                        if choice == 0:
                            selected_color = random.choice(list(dragon_damage.keys()))
                        elif 1 <= choice <= len(dragon_damage):
                            selected_color = list(dragon_damage.keys())[choice - 1]
                    if param == "N":
                        selected_color = random.choice(list(dragon_damage.keys()))                    
                    selected_damage = dragon_damage[selected_color]
                    if dnd_tools.languages["Drac"] not in player.languages:
                        player.languages.append(dnd_tools.languages["Drac"])
                    player.classnotes.append("Dragon Ancestor (see notes)")
                    player.notes.append(f"Dragon Ancestor - You choose one type of dragon as your ancestor. The damage type associated with each dragon is used by features you gain later. Your color is {selected_color}, and the damage is {selected_damage}.\nYou can speak, read, and write Draconic(addressed). Additionally, whenever you make a Charisma check when interacting with dragons, your Proficiency Bonus is doubled if it applies to the check.")
                    player.classnotes.append("Draconic Resilience (see notes)")
                    player.notes.append(f"Draconic Resilience - As magic flows through your body, it causes physical traits of your dragon ancestors to emerge. Your hit point maximum increases by 1 for every level in this class, meaning your Hit Points are now: {player.hitpoints + sorclvl}.\nAdditionally, parts of your skin are covered by a thin sheen of dragon-like scales. When you aren't wearing armor, your AC equals 13 + your Dexterity modifier, or AC {13 + player.DexMod}.")
                    if sorclvl >= 6:
                        player.classnotes.append(f"Elemental Affinity - When you cast a spell that deals damage of the type associated with your draconic ancestry, add your Charisma modifier, or {player.ChaMod}, to that damage. At the same time, you can spend 1 sorcery point to gain resistance to that damage type for 1 hour.")
                    if sorclvl >= 14:
                        player.classnotes.append("Dragon Wings (see notes)")
                        player.notes.append("Dragon Wings - You gain the ability to sprout a pair of dragon wings from your back, gaining a flying speed equal to your current speed. You can create these wings as a bonus action on your turn. They last until you dismiss them as a bonus action on your turn.\nYou can't manifest your wings while wearing armor unless the armor is made to accommodate them, and clothing not made to accommodate your wings might be destroyed when you manifest them.")
                    if sorclvl >= 18:
                        player.classnotes.append("Draconic Presence (see notes)")
                        player.notes.append("Draconic Presence - You can channel the dread presence of your dragon ancestor, causing those around you to become awestruck or frightened. As an action, you can spend 5 sorcery points to draw on this power and exude an aura of awe or fear (your choice) to a distance of 60 feet. For 1 minute or until you lose your concentration (as if you were casting a concentration spell), each hostile creature that starts its turn in this aura must succeed on a Wisdom saving throw or be charmed (if you chose awe) or frightened (if you chose fear) until the aura ends. A creature that succeeds on this saving throw is immune to your aura for 24 hours.")                       
                if player.subclass[i] == "Lunar Magic Origin Sorcerer":
                    MoonPhases = ["Full Moon", "New Moon", "Crescent Moon"]
                    if param == "Y":
                        print("0 - Random")
                        for idx, phase in enumerate(MoonPhases, 1):
                            print(f"{idx} - {phase}")
                        choice = int(input("Choose which lunar phase manifests its power through your magic. "))
                        if choice == 0:
                            selected_phase = random.choice(MoonPhases)
                        elif 1 <= choice <= len(MoonPhases):
                            selected_phase = MoonPhases[choice - 1]
                    if param == "N":
                        selected_phase = random.choice(MoonPhases)
                    SorcLunarMagicSpells = []
                    if selected_phase == "Full Moon":
                        if sorclvl >= 1:
                            SorcLunarMagicSpells.append("Shield")
                        if sorclvl >= 3:
                            SorcLunarMagicSpells.append("Lesser Restoration")
                        if sorclvl >= 5:
                            SorcLunarMagicSpells.append("Dispel Magic")
                        if sorclvl >= 7:
                            SorcLunarMagicSpells.append("Death Ward")
                        if sorclvl >= 9:
                            SorcLunarMagicSpells.append("Rary's Telepathic Bond")
                    elif selected_phase == "New Moon":
                        if sorclvl >= 1:
                            SorcLunarMagicSpells.append("Ray of Sickness")
                        if sorclvl >= 3:
                            SorcLunarMagicSpells.append("Blindness/Deafness")
                        if sorclvl >= 5:
                            SorcLunarMagicSpells.append("Vampiric Touch")
                        if sorclvl >= 7:
                            SorcLunarMagicSpells.append("Confusion")
                        if sorclvl >= 9:
                            SorcLunarMagicSpells.append("Hold Monster")
                    elif selected_phase == "Crescent Moon":
                        if sorclvl >= 1:
                            SorcLunarMagicSpells.append("Color Spray")
                        if sorclvl >= 3:
                            SorcLunarMagicSpells.append("Alter Self")
                        if sorclvl >= 5:
                            SorcLunarMagicSpells.append("Phantom Steed")
                        if sorclvl >= 7:
                            SorcLunarMagicSpells.append("Hallucinatory Terrain")
                        if sorclvl >= 9:
                            SorcLunarMagicSpells.append("Mislead") 
                    player.classnotes.append("Lunar Embodiment (see notes)")
                    player.notes.append(f"Lunar Embodiment - You learn additional spells when you reach certain levels in this class. Each of these spells counts as a sorcerer spell for you, but it doesn't count against the number of sorcerer spells you know.\nWhenever you finish a long rest, you can choose what lunar phase manifests its power through your magic. While in the chosen phase, you can cast the associated spell once without expending a spell slot. Once you cast the associated spell(s) in this way, you can't do so again until you finish a long rest. The spell(s) given in this way currently are: {SorcLunarMagicSpells}")                   
                    player.classnotes.append("Moon Fire (see notes)")
                    player.notes.append("Moon Fire - You can call down the radiant light of the moon on command. You learn the Sacred Flame spell, which doesn't count against the number of sorcerer cantrips you know. When you cast the spell, you can target one creature as normal or target two creatures within range that are within 5 feet of each other.")
                    if sorclvl >= 6:
                        player.classnotes.append("Lunar Boons (see notes)")
                        player.notes.append(f"Lunar Boons - The current phase of your Lunar Embodiment can affect your Metamagic feature. Each Lunar Embodiment phase is associated with certain schools of magic, as shown here:\nFull Moon - Abjuration and divination spells\nNew Moon - Enchantment and necromancy spells\nCrescent Moon - Illusion and transmutation spells\nWhenever you use Metamagic on a spell of a school of magic associated with your current Lunar Embodiment phase, you can reduce the sorcery points spent by 1 (minimum 0). You can reduce the sorcery points spent for your Metamagic a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
                        player.classnotes.append("Waxing and Waning (see notes)")
                        player.notes.append("Waxing and Waning - You gain greater control over the phases of your lunar magic. As a bonus action, you can spend 1 sorcery point to change your current Lunar Embodiment phase to a different one.\nYou can now cast one 1st-level spell from each lunar phase of the Lunar Spells table once without expending a spell slot, provided your current phase is the same as the lunar phase spell. Once you cast a lunar phase spell in this way, you can't do so again until you finish a long rest.")
                    if sorclvl >= 14:
                        player.classnotes.append("Lunar Empowerment (see notes)")
                        player.notes.append("Lunar Empowerment - The power of a lunar phase saturates your being. While you are in a Lunar Embodiment phase, you also gain the following benefit associated with that phase:\nFull Moon - You can use a bonus action to shed bright light in a 10-foot radius and dim light for an additional 10 feet or to douse the light. In addition, you and creatures of your choice have advantage on Intelligence (Investigation) and Wisdom (Perception) checks while within the bright light you shed.\nNew Moon - You have advantage on Dexterity (Stealth) checks. In addition, while you are entirely in darkness, attack rolls have disadvantage against you.\nCrescent Moon - You have resistance to necrotic and radiant damage.")
                    if sorclvl >= 18:
                        player.classnotes.append("Lunar Phenomenon (see notes)")
                        player.notes.append(f"Lunar Phenomenon - As a bonus action, you can tap into a special power of your current Lunar Embodiment phase. Alternatively, as part of the bonus action you take to change your lunar phase using the Waxing and Waning feature, you can immediately use the power of the lunar phase you are entering:\nFull Moon - You radiate moonlight for a moment. Each creature of your choice within 30 feet of you must succeed on a Constitution saving throw against your spell save DC or be blinded until the end of its next turn. In addition, one creature of your choice in that area regains 3d8 hit points.\nNew Moon - You momentarily emanate gloom. Each creature of your choice within 30 feet of you must succeed on a Dexterity saving throw against your spell save DC, or against {player.spellsavedc[i]}, or take 3d10 necrotic damage and have its speed reduced to 0 until the end of its next turn. In addition, you become invisible until the end of your next turn, or until immediately after you make an attack roll or cast a spell.\nCrescent Moon - You can magically teleport to an unoccupied space you can see within 60 feet of yourself. You can bring along one willing creature you can see within 5 feet of yourself. That creature teleports to an unoccupied space of your choice that you can see within 5 feet of your destination space. In addition, you and that creature gain resistance to all damage until the start of your next turn.\nOnce you use one of these bonus action benefits, you can't use that benefit again until you finish a long rest, unless you spend 5 sorcery points to use it again.")                       
                if player.subclass[i] == "Runechild Origin Sorcerer":
                    SorcRunechildSpells = []
                    if sorclvl >= 1:
                        SorcRunechildSpells.append("Longstrider")
                        SorcRunechildSpells.append("Protection from Evil and Good")
                    if sorclvl >= 3:
                        SorcRunechildSpells.append("Lesser Restoration")
                        SorcRunechildSpells.append("Protection from Poison")
                    if sorclvl >= 5:
                        SorcRunechildSpells.append("Glyph of Warding")
                        SorcRunechildSpells.append("Magic Circle")
                    if sorclvl >= 7:
                        SorcRunechildSpells.append("Death Ward")
                        SorcRunechildSpells.append("Freedom of Movement")
                    if sorclvl >= 9:
                        SorcRunechildSpells.append("Greater Restoration")
                        SorcRunechildSpells.append("Telekinesis")
                    player.classnotes.append("Runic Magic (see notes)")
                    player.notes.append(f"Runic Magic - You learn additional spells when you reach certain levels in this class. Each of these spells counts as a sorcerer spell for you, but it doesn't count against the number of sorcerer spells you know. You currently know: {SorcRunechildSpells}\nWhen you gain a level in this class, you can replace one spell you gained from this feature with another spell of the same level. The new spell must be an abjuration or transmutation spell from the sorcerer, warlock, or wizard spell list.")
                    GlyphAegisDie = "d6"
                    if sorclvl >= 14:
                        GlyphAegisDie = "d8"
                    player.classnotes.append("Glyph of Aegis(1) (see notes)")
                    player.notes.append(f"Glyph of Aegis(1) - You can release the stored arcane power within your runes to absorb or deflect threatening attacks. Whenever you take damage, you can expend any number of charged runes as a reaction. Roll a number of {GlyphAegisDie}s equal to the number of runes you expended, and reduce the damage by the total.")
                    if sorclvl >= 6:
                        player.classnotes.append("Glyph of Aegis(2) (see notes)")
                        player.notes.append(f"Glyph of Aegis(2) - You can touch a creature as an action and expend up to 3 charged runes to transfer your protective power to it for up to 1 hour. The next time that creature takes damage within the next hour, it rolls 1{GlyphAegisDie} per charged rune spent and reduces the damage by the total. You can't transfer this power to a creature already under the effect of Glyph of Aegis.")
                        player.classnotes.append("Sigilic Augmentation (see notes)")
                        player.notes.append("Sigilic Augmentation - You can channel your runes to temporarily bolster your physical capabilities. When you make a Strength, Dexterity, or Constitution ability check, you can expend a charged rune as a reaction to gain advantage on the roll.\nIn addition, when you are forced to make a Strength, Dexterity, or Constitution saving throw, you can use your reaction and expend a charged rune to gain advantage on the saving throw. Once you use this feature in this way, you can't use it in this way again until you complete a long rest.")
                        player.classnotes.append("Manifest Inscriptions (see notes)")
                        player.notes.append("Manifest Inscriptions - You can reveal hidden glyphs and enchantments that surround you. As an action, you expend one charged rune to reveal hidden or invisible arcane traps, marks, runes, wards, sensors, or glyphs within 60 feet of you. They glow with dim light in a 5-foot radius for 1 minute.\nYou have advantage on Intelligence (Arcana) checks to discern the nature of any magic revealed in this way for the duration. If the glyphs you reveal mean something in a language you can't read, you can understand them while they are glowing as if you knew that language.")                        
                    if sorclvl >= 14:
                        player.classnotes.append("Runic Torrent (see notes)")
                        player.notes.append(f"Runic Torrent - You can channel runic energy to overpower even the staunchest defenses. When you cast a spell, you can expend 2 charged runes to cause the spell to deal force damage instead of its usual damage types. Additionally, all creatures targeted by the spell or within the spell's area must succeed on a Strength saving throw against your spell save DC, or against {player.spellsavedc[i]}, or be knocked prone or pushed up to 15 feet away from the spell's point of origin (your choice).\nOnce you use this feature, you can't do so again until you complete a short or long rest.")
                    if sorclvl >= 18:
                        player.classnotes.append("Arcane Exemplar (see notes)")
                        player.notes.append("Arcane Exemplar - You can use a bonus action and expend a charged rune to become a being of pure magical energy. While in your exemplar form, you gain the following benefits:\n- You have a flying speed of 60 feet.\n- Creatures have disadvantage on saving throws against your sorcerer spells.\n- You have resistance to damage dealt by spells.\n- Whenever you cast a spell of 1st level or higher, you regain hit points equal to the spell's level.\nYour exemplar form lasts until the end of your turn. However, you can expend a charged rune at the end of your turn (no action required) to extend the duration until the end of your next turn. When your exemplar form ends, you are stunned until the end of your next turn.\nOnce you use this feature, you can't use it again until you complete a long rest.")                    
                if player.subclass[i] == "Shadow Origin Sorcerer":
                    ShSorc1 = "You are always icy cold to the touch."
                    ShSorc2 = "When you are asleep, you don't appear to breathe (though you must still breathe to survive)."
                    ShSorc3 = "You barely bleed, even when badly injured."
                    ShSorc4 = "Your heart beats once per minute. This event sometimes surprises you."
                    ShSorc5 = "You have trouble remembering that living creatures and corpses should be treated differently."
                    ShSorc6 = "You blinked. Once. Last week."
                    ShSorc = [ShSorc1, ShSorc2, ShSorc3, ShSorc4, ShSorc5, ShSorc6]
                    if param == "Y":
                        print("0 - Random")
                        for so, shsorcq in enumerate(ShSorc, 1):
                            print(f"{so} - {shsorcq}")
                        ssqinput = int(input("Choose which Quirk your Shadow Sorcerer has. "))
                        if ssqinput == 0:
                            ShSorc_Choice = random.choice(ShSorc)
                        elif 1 <= ssqinput <= len(ShSorc):
                            ShSorc_Choice = ShSorc[ssqinput-1]
                    if param == "N":
                        ShSorc_Choice = random.choice(ShSorc)
                    player.classnotes.append(f"Shadow Sorcerer Quirks - Your Quirk as a Shadow Sorcerer: {ShSorc_Choice}")                        
                    player.classnotes.append("Eyes of the Dark(1) (see notes)")
                    player.notes.append("Eyes of the Dark(1) - You have darkvision with a range of 120 feet.")                     
                    player.classnotes.append("Strength of the Grave (see notes)")
                    player.notes.append("Strength of the Grave - Your existence in a twilight state between life and death makes you difficult to defeat. When damage reduces you to 0 hit points, you can make a Charisma saving throw (DC 5 + the damage taken). On a success, you instead drop to 1 hit point. You can't use this feature if you are reduced to 0 hit points by radiant damage or by a critical hit.\nAfter the saving throw succeeds, you can't use this feature again until you finish a long rest.")
                    if sorclvl >= 3:
                        player.classnotes.append("Eyes of the Dark(2) (see notes)")
                        player.notes.append("Eyes of the Dark(2) - You learn the Darkness spell, which doesn't count against your number of sorcerer spells known. In addition, you can cast it by spending 2 sorcery points or by expending a spell slot. If you cast it with sorcery points, you can see through the darkness created by the spell.")   
                    if sorclvl >= 6:
                        player.classnotes.append("Hound of Ill Omen (see notes)")
                        player.notes.append(f"Hound of Ill Omen - You gain the ability to call forth a howling creature of darkness to harass your foes. As a bonus action, you can spend 3 sorcery points to summon a hound of ill omen to target one creature you can see within 120 feet of you. The hound uses the dire wolf’s statistics, with the following changes:\n- The hound is size Medium, not Large, and it counts as a monstrosity, not a beast.\n- It appears with a number of temporary hit points equal to half your Sorcerer level, or {math.floor(sorclvl/2)} temporary hitpoints.\n- It can move through other creatures and objects as if they were difficult terrain. The hound takes 5 force damage if it ends its turn inside an object.\n- At the start of its turn, the hound automatically knows its target’s location. If the target was hidden, it is no longer hidden from the hound.\nThe hound appears in an unoccupied space of your choice within 30 feet of the target. Roll initiative for the hound. On its turn, it can move only toward its target by the most direct route, and it can use its action only to attack its target. The hound can make opportunity attacks, but only against its target. Additionally, while the hound is within 5 feet of the target, the target has disadvantage on saving throws against any spell you cast. The hound disappears if it is reduced to 0 hit points, if its target is reduced to 0 hit points, or after 5 minutes.")   
                    if sorclvl >= 14:
                        player.classnotes.append("Shadow Walk - You gain the ability to step from one shadow into another. When you are in dim light or darkness, as a bonus action, you can teleport up to 120 feet to an unoccupied space you can see that is also in dim light or darkness.")
                    if sorclvl >= 18:
                        player.classnotes.append("Umbral Form (see notes)")
                        player.notes.append("Umbral Form - You can spend 6 sorcery points as a bonus action to transform yourself into a shadowy form. In this form, you have resistance to all damage except force and radiant damage, and you can move through other creatures and objects as if they were difficult terrain. You take 5 force damage if you end your turn inside an object.\nYou remain in this form for 1 minute. It ends early if you are incapacitated, if you die, or if you dismiss it as a bonus action.")                                                                                  
                if player.subclass[i] == "Storm Origin Sorcerer":  
                    if dnd_tools.languages["Prim"] not in player.languages:
                        player.languages.append(dnd_tools.languages["Prim"])
                    player.classnotes.append("Wind Speaker - The arcane magic you command is infused with elemental air. You can speak, read, and write Primordial (addressed). Knowing this language allows you to understand and be understood by those who speak its dialects: Aquan, Auran, Ignan, and Terran.")
                    player.classnotes.append("Tempestuous Magic - You can use a bonus action on your turn to cause whirling gusts of elemental air to briefly surround you, immediately before or after you cast a spell of 1st level or higher. Doing so allows you to fly up to 10 feet without provoking opportunity attacks.")
                    if sorclvl >= 6:
                        player.classnotes.append("Heart of the Storm (see notes)")
                        player.notes.append(f"Heart of the Storm - You gain resistance to lightning and thunder damage. In addition, whenever you start casting a spell of 1st level or higher that deals lightning or thunder damage, stormy magic erupts from you. This eruption causes creatures of your choice that you can see within 10 feet of you to take lightning or thunder damage (choose each time this ability activates) equal to half your Sorcery level, or {math.floor(sorclvl/2)}.")
                        player.classnotes.append("Storm Guide (see notes)")
                        player.notes.append("Storm Guide - You gain the ability to subtly control the weather around you.\nIf it is raining, you can use an action to cause the rain to stop falling in a 20-foot-radius sphere centered on you. You can end this effect as a bonus action.\nIf it is windy, you can use a bonus action each round to choose the direction that the wind blows in a 100-foot-radius sphere centered on you. The wind blows in that direction until the end of your next turn. This feature doesn't alter the speed of the wind.")
                    if sorclvl >= 14:
                        player.classnotes.append("Storm's Fury (see notes)")
                        player.notes.append(f"Storm's Fury - When you are hit by a melee attack, you can use your reaction to deal lightning damage to the attacker. The damage equals your Sorcerer level, or {sorclvl}. The attacker must also make a Strength saving throw against your sorcerer spell save DC, or against {player.spellsavedc[i]}. On a failed save, the attacker is pushed in a straight line up to 20 feet away from you.")
                    if sorclvl >= 18:
                        player.classnotes.append("Wind Soul (see notes)")
                        player.notes.append(f"Wind Soul - You gain immunity to lightning and thunder damage.\nYou also gain a magical flying speed of 60 feet. As an action, you can reduce your flying speed to 30 feet for 1 hour and choose a number of creatures within 30 feet of you equal to 3 + your Charisma Modifier, or {3 + player.ChaMod} creatures. The chosen creatures gain a magical flying speed of 30 feet for 1 hour. Once you reduce your flying speed in this way, you can't do so again until you finish a short or long rest.")                                                                        
                if player.subclass[i] == "Wild Magic Origin Sorcerer":                  
                    player.classnotes.append("Wild Magic Surge - Your spellcasting can unleash surges of untamed magic. Immediately after you cast a sorcerer spell of 1st level or higher, the DM can have you roll a d20. If you roll a 1, roll on the Wild Magic Surge table to create a random magical effect.")
                    player.classnotes.append("Tides of Chaos (see notes)")
                    player.notes.append("Tides of Chaos - You can manipulate the forces of chance and chaos to gain advantage on one attack roll, ability check, or saving throw. Once you do so, you must finish a long rest before you can use this feature again.\nAny time before you regain the use of this feature, the DM can have you roll on the Wild Magic Surge table immediately after you cast a sorcerer spell of 1st level or higher. You then regain the use of this feature.")
                    if sorclvl >= 6:
                        player.classnotes.append("Bend Luck (see notes)")
                        player.notes.append("Bend Luck - You have the ability to twist fate using your wild magic. When another creature you can see makes an attack roll, an ability check, or a saving throw, you can use your reaction and spend 2 sorcery points to roll 1d4 and apply the number rolled as a bonus or penalty (your choice) to the creature's roll. You can do so after the creature rolls but before any effects of the roll occur.")
                    if sorclvl >= 14:
                        player.classnotes.append("Controlled Chaos - You gain a modicum of control over the surges of your wild magic. Whenever you roll on the Wild Magic Surge table, you can roll twice and use either number.")
                    if sorclvl >= 18:
                        player.classnotes.append("Spell Bombardment - The harmful energy of your spells intensifies. When you roll damage for a spell and roll the highest number possible on any of the dice, choose one of those dice, roll it again and add that roll to the damage. You can use the feature only once per turn.")
            if sorclvl >= 2:
                SorcSpellsKnown = 3
                SorcSpellSlot1 = 3
            if sorclvl >= 3:                    
                SorcSpellsKnown = 4
                SorcSpellSlot1 = 4
                SorcSpellSlot2 = 2
                MetamagicAbilities = 2
                if ((sorclvl >= 10) and (sorclvl < 17)):
                    MetamagicAbilities = "three"
                if sorclvl > 17:
                    MetamagicAbilities = "four"
                player.classnotes.append("Metamagic (see notes)")
                player.notes.append(f"Metamagic - You gain the ability to twist your spells to suit your needs. You gain {MetamagicAbilities} of the following Metamagic options of your choice. You gain another one at 10th and 17th level.\nYou can use only one Metamagic option on a spell when you cast it, unless otherwise noted.\nCareful Spell - When you cast a spell that forces other creatures to make a saving throw, you can protect some of those creatures from the spell’s full force. To do so, you spend 1 sorcery point and choose a number of those creatures up to your Charisma modifier, or {player.ChaMod} creatures, minimum of one creature. A chosen creature automatically succeeds on its saving throw against the spell.\nDistant Spell - When you cast a spell that has a range of 5 feet or greater, you can spend 1 sorcery point to double the range of the spell.\nWhen you cast a spell that has a range of touch, you can spend 1 sorcery point to make the range of the spell 30 feet.\nEmpowered Spell - When you roll damage for a spell, you can spend 1 sorcery point to reroll a number of the damage dice up to your Charisma modifier, or {player.ChaMod} dice, minimum of one. You must use the new rolls.\nYou can use Empowered Spell even if you have already used a different Metamagic option during the casting of the spell.\nExtended Spell - When you cast a spell that has a duration of 1 minute or longer, you can spend 1 sorcery point to double its duration, to a maximum duration of 24 hours.\nHeightened Spell - When you cast a spell that forces a creature to make a saving throw to resist its effects, you can spend 3 sorcery points to give one target of the spell disadvantage on its first saving throw made against the spell.\nQuickened Spell - When you cast a spell that has a casting time of 1 action, you can spend 2 sorcery points to change the casting time to 1 bonus action for this casting.\nSeeking Spell - If you make an attack roll for a spell and miss, you can spend 2 sorcery points to reroll the d20, and you must use the new roll.\nYou can use Seeking Spell even if you have already used a different Metamagic option during the casting of the spell.\nSubtle Spell - When you cast a spell, you can spend 1 sorcery point to cast it without any somatic or verbal components.\nTransmuted Spell - When you cast a spell that deals a type of damage from the following list, you can spend 1 sorcery point to change that damage type to one of the other listed types: acid, cold, fire, lightning, poison, thunder.\nTwinned Spell - When you cast a spell that targets only one creature and doesn’t have a range of self, you can spend a number of sorcery points equal to the spell’s level to target a second creature in range with the same spell (1 sorcery point if the spell is a cantrip).\nTo be eligible, a spell must be incapable of targeting more than one creature at the spell’s current level. For example, Magic Missile and Scorching Ray aren’t eligible, but Ray of Frost and Chromatic Orb are.")                
            if sorclvl >= 4:
                SorcSpellsKnown = 5
                SorcSpellSlot2 = 3
                player.classnotes.append("Sorcerous Versatility (see notes)")
                player.notes.append("Sorcerous Versatility - Whenever you reach a level in this class that grants the Ability Score Improvement feature, you can do one of the following, representing the magic within you flowing in new ways:\n- Replace one of the options you chose for the Metamagic feature with a different Metamagic option available to you.\n- Replace one cantrip you learned from this class's Spellcasting feature with another cantrip from the sorcerer spell list.")
            if sorclvl >= 5:
                SorcSpellsKnown = 6
                SorcSpellSlot3 = 2
                player.classnotes.append("Magical Guidance - You can tap into your inner wellspring of magic to try to conjure success from failure. When you make an ability check that fails, you can spend 1 sorcery point to reroll the d20, and you must use the new roll, potentially turning the failure into a success.")
            if sorclvl >= 6:
                SorcSpellsKnown = 7
                SorcSpellSlot2 = 3
            if sorclvl >= 7:
                SorcSpellsKnown = 8
                SorcSpellSlot4 = 1
            if sorclvl >= 8:
                SorcSpellsKnown = 9
                SorcSpellSlot4 = 2
            if sorclvl >= 9:
                SorcSpellsKnown = 10
                SorcSpellSlot4 = 3
                SorcSpellSlot5 = 1
            if sorclvl >= 10:
                SorcSpellsKnown = 11
                SorcSpellSlot5 = 2
            if sorclvl >= 11:
                SorcSpellsKnown = 12
                SorcSpellSlot6 = 1
            if sorclvl >= 13:
                SorcSpellsKnown = 13
                SorcSpellSlot7 = 1
            if sorclvl >= 15:
                SorcSpellsKnown = 14
                SorcSpellSlot8 = 1
            if sorclvl >= 17:
                SorcSpellsKnown = 15
                SorcSpellSlot9 = 1
            if sorclvl >= 18:
                SorcSpellSlot5 = 3
            if sorclvl >= 19:
                SorcSpellSlot6 = 2
            if sorclvl == 20:  
                SorcSpellSlot7 = 2
                player.classnotes.append("Sorcerous Restoration - You regain 4 expended sorcery points whenever you finish a short rest.")                
            if sorclvl > 1:
                SorceryPoints = sorclvl  
                player.classnotes.append("Sorcery Points (see notes)")
                player.notes.append("Sorcery Points - You have a number of sorcery points, determined by your level. You can never have more sorcery points than your level. You regain all spent sorcery points when you finish a long rest.\nFlexible Casting - You can use your sorcery points to gain additional spell slots, or sacrifice spell slots to gain additional sorcery points. You learn other ways to use your sorcery points as you reach higher levels.\nCreating Spell Slots - You can transform unexpended sorcery points into one spell slot as a bonus action on your turn. The Creating Spell Slots table shows the cost of creating a spell slot of a given level. You can create spell slots no higher in level than 5th. Any spell slot you create with this feature vanishes when you finish a long rest.\n1st Spell Slot costs 2 Sorcery Points\n2nd Spell Slot costs 3 Sorcery Points\n3rd Spell Slot costs 5 Sorcery Points\n4th Spell Slot costs 6 Sorcery Points\n5th Spell Slot costs 7 Sorcery Points\nConverting a Spell Slot to Sorcery Points. As a bonus action on your turn, you can expend one spell slot and gain a number of sorcery points equal to the slot’s level.")
            player.notes.append(f"You have {SorcCantripsKnown} cantrips available to you.")
            player.notes.append(f"You know {SorcSpellsKnown} spells.")
            player.notes.append(f"The number of first level spell slots you have as a Sorcerer is: {SorcSpellSlot1}.")
            if SorcSpellSlot2 != 0:
                player.notes.append(f"The number of second level spell slots you have as a Sorcerer is: {SorcSpellSlot2}.")
            if SorcSpellSlot3 != 0:                
                player.notes.append(f"The number of third level spell slots you have as a Sorcerer is: {SorcSpellSlot3}.")
            if SorcSpellSlot4 != 0:
                player.notes.append(f"The number of fourth level spell slots you have as a Sorcerer is: {SorcSpellSlot4}.")
            if SorcSpellSlot5 != 0:
                player.notes.append(f"The number of fifth level spell slots you have as a Sorcerer is: {SorcSpellSlot5}.")
            if SorcSpellSlot6 != 0:
                player.notes.append(f"The number of sixth level spell slots you have as a Sorcerer is: {SorcSpellSlot6}.")
            if SorcSpellSlot7 != 0:
                player.notes.append(f"The number of seventh level spell slots you have as a Sorcerer is: {SorcSpellSlot7}.")
            if SorcSpellSlot8 != 0:
                player.notes.append(f"The number of eighth level spell slots you have as a Sorcerer is: {SorcSpellSlot8}.")
            if SorcSpellSlot9 != 0:
                player.notes.append(f"The number of ninth level spell slots you have as a Sorcerer is: {SorcSpellSlot9}.")                                
        if player.Class[i] == "Warlock":   
            if ((param == "N") or (player.singlemulticlass == "N")):
                warlvl = player.level
                player.classlvl.append(warlvl) 
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    warlvl = int(input(f"Given your pool of levels of {poollevel}, what is your Warlock level? "))    
                    if warlvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                
                poollevel = poollevel - warlvl
                player.classlvl.append(warlvl)
            if warlvl >= 1:
                player.hitdice.append(f"{warlvl}d8 for {player.Class[i]}")
                if warlvl == 1:
                    player.hitpoints += (8 + player.ConMod)
                else:
                    player.hitpoints += (8 + player.ConMod + hpcalc(warlvl, dice, 8))                    
                if i == 0: 
                    profs = ["Light Armor", "Simple Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)                                
                    player.skills.append(dnd_tools.saving_throws["ChaST"])
                    player.skills.append(dnd_tools.saving_throws["WisST"])
                    SkillsList = [
                        dnd_tools.skills["Arcana"], 
                        dnd_tools.skills["Deception"], 
                        dnd_tools.skills["History"], 
                        dnd_tools.skills["Intimidation"], 
                        dnd_tools.skills["Investigation"], 
                        dnd_tools.skills["Nature"], 
                        dnd_tools.skills["Religion"]
                        ]
                    player.skills = twoskillsfromlist(param, player.skills, SkillsList)  
                    StartEquip1 = ["A Light Crossbow and 20 Bolts", "Any Simple Weapon"]
                    StartEquip2 = ["A Component Pouch", "An Arcane Focus"]
                    StartEquip3 = ["Scholar's Pack", "Dungeoneer's Pack"]
                    if param == "Y":
                        print("0 - Random")
                        print("1 - A Light Crossbow and 20 Bolts")
                        print("2 - Any Simple Weapon")
                        se1 = int(input("What would you like your first choice for starting equipment to be? "))
                        if se1 == 0:
                            SE1rand = random.choice(StartEquip1)
                            if SE1rand == "A Light Crossbow and 20 Bolts":
                                player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                                player.equipment.append("20 Bolts")
                            if SE1rand == "Any Simple Weapon":
                                SimpRandKey = random.choice(SimpleWeapons)
                                player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                        if se1 == 1:
                            player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                            player.equipment.append("20 Bolts")
                        if se1 == 2:
                            print("0 - Random")
                            for j, sw in enumerate(SimpleWeaponsNames, 1):
                                print(f"{j} - {sw}")
                            se1sw = int(input("Which simple weapon would you like to add to your inventory? "))
                            if se1sw == 0:
                                SimpRandKey = random.choice(SimpleWeapons)
                                player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                            elif 1 <= se1sw <= len(SimpleWeapons):
                                SimpKey = SimpleWeapons[se1sw - 1]
                                player.equipment.append(dnd_tools.simple_weapons[SimpKey].copy())
                        print("0 - Random")
                        print("1 - A Component Pouch")
                        print("2 - An Arcane Focus")
                        se2 = int(input("What would you like your second choice for starting equipment to be? "))
                        if se2 == 0:
                            SE2rand = random.choice(StartEquip2)
                            if SE2rand == "A Component Pouch":
                                player.equipment.append("Component Pouch")
                            if SE2rand == "An Arcane Focus":
                                player.equipment.append("Arcane Focus")
                        if se2 == 1:
                            player.equipment.append("Component Pouch")
                        if se2 == 2:
                            player.equipment.append("Arcane Focus")
                        print("0 - Random")
                        print("1 - A Scholar's Pack")
                        print("2 - A Dungeoneer's Pack")
                        se3 = int(input("What would you like your third choice for starting equipment to be? "))    
                        if se3 == 0:
                            SE3rand = random.choice(StartEquip3)
                            if SE3rand == "Scholar's Pack":
                                player.equipment.extend(dnd_tools.packs["ScholarsPack"]["contents"])
                            if SE3rand == "Dungeoneer's Pack":
                                player.equipment.extend(dnd_tools.packs["DungeoneersPack"]["contents"])
                        if se3 == 1:
                            player.equipment.extend(dnd_tools.packs["ScholarsPack"]["contents"])
                        if se3 == 2:
                            player.equipment.extend(dnd_tools.packs["DungeoneersPack"]["contents"])                                       
                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        print("0 - Random")
                        for j, sw in enumerate(SimpleWeaponsNames, 1):
                            print(f"{j} - {sw}")
                        sesw = int(input("Which simple weapon would you like to add to your inventory? "))
                        if sesw == 0:
                            SimpRandKey = random.choice(SimpleWeapons)
                            player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                        elif 1 <= sesw <= len(SimpleWeapons):
                            SimpKey = SimpleWeapons[sesw - 1]
                            player.equipment.append(dnd_tools.simple_weapons[SimpKey].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "A Light Crossbow and 20 Bolts":
                            player.equipment.append(dnd_tools.simple_weapons["LightCrossbow"].copy())
                            player.equipment.append("20 Bolts")
                        if SE1rand == "Any Simple Weapon":
                            SimpRandKey = random.choice(SimpleWeapons)
                            player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "A Component Pouch":
                            player.equipment.append("Component Pouch")
                        if SE2rand == "An Arcane Focus":
                            player.equipment.append("Arcane Focus")
                        SE3rand = random.choice(StartEquip3)
                        if SE3rand == "Scholar's Pack":
                            player.equipment.extend(dnd_tools.packs["ScholarsPack"]["contents"])
                        if SE3rand == "Dungeoneer's Pack":
                            player.equipment.extend(dnd_tools.packs["DungeoneersPack"]["contents"])                            
                        player.equipment.append(dnd_tools.light_armor["Leather"].copy())
                        SimpRandKey = random.choice(SimpleWeapons)
                        player.equipment.append(dnd_tools.simple_weapons[SimpRandKey].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                        player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())  
                else:
                    profs = ["Light Armor", "Simple Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)                                                                         
                player.spellcastingclass.append("Warlock")
                player.spellcastingability.append("Cha")
                player.spellsavedc.append(8 + player.profbonus + player.ChaMod)
                player.spellattackmod.append(player.profbonus + player.ChaMod)
                WarlockCantripsKnown = 2
                WarlockSpellsKnown = 2
                WarlockSpellSlots = 1
                WarlockSlotLevel = "1st"        
                War = ["Archfey Patron Warlock", "Beachball Patron Warlock", "Celestial Patron Warlock", "The Fathomless Patron Warlock", "Fiend Patron Warlock", "The Genie Patron Warlock", "Great Old One Patron Warlock", "Hexblade Patron Warlock", "Undead Patron Warlock", "Undying Patron Warlock"]    
                
                print(f"Subclasses are: {player.subclass}")
                if player.subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        for idx, subcl in enumerate(War, 1):
                            print(f"{idx} - {subcl}")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 0:
                            WarRand = random.choice(War)
                            if WarRand == "Beachball Patron Warlock":
                                War.remove("Beachball Patron Warlock")
                                WarRand = random.choice(War)
                                player.subclass[i] = WarRand
                                BeachballFlag = True
                            else:
                                player.subclass[i] = random.choice(War)
                        elif 1 <= subc <= len(War):
                            if subc == 2:
                                War.remove("Beachball Patron Warlock")
                                player.subclass[i] = random.choice(War)
                                BeachballFlag = True                                    
                            else:
                                player.subclass[i] = War[subc - 1]
                    if param == "N":
                        WarRand = random.choice(War)
                        if WarRand == "Beachball Patron Warlock":
                            War.remove("Beachball Patron Warlock")
                            WarRand = random.choice(War)
                            player.subclass[i] = WarRand
                            BeachballFlag = True
                        else:
                            player.subclass[i] = random.choice(War)                         
                if player.subclass[i] == "Archfey Patron Warlock":
                    Patron = "Archfey"
                    if player.beachballflag == True:
                        Patron = "Beachball"
                        player.subclass[i] == "Beachball(Archfey) Patron Warlock"
                    WarArchfeySpells = {
                        1: ["Faerie Fire", "Sleep"],
                        2: ["Calm Emotions", "Phantasmal Force"],
                        3: ["Blink", "Plant Growth"],
                        4: ["Dominate Beast", "Greater Invisibility"],
                        5: ["Dominate Person", "Seeming"]
                    }
                    spell_list = []
                    for level, spells in WarArchfeySpells.items():
                        if level == 1:
                            spell_list.append(f"for {level}st level you get {', '.join(spells)}")
                        if level == 2:
                            spell_list.append(f"for {level}nd level you get {', '.join(spells)}")
                        if level == 3:
                            spell_list.append(f"for {level}rd level you get {', '.join(spells)}")                            
                        if level == 4:
                            spell_list.append(f"for {level}th level you get {', '.join(spells)}")
                        if level == 5:
                            spell_list.append(f"for {level}th level you get {', '.join(spells)}")                                                    
                    player.classnotes.append("Expanded Spell List (see notes)")
                    player.notes.append(f"Expanded Spell List - {Patron} lets you choose from an expanded list of spells when you learn a warlock spell. The following spells are added to the warlock spell list for you: {', '.join(spell_list)}.")
                    player.classnotes.append("Fey Presence (see notes)")
                    player.notes.append(f"Fey Presence - Your patron bestows upon you the ability to project the beguiling and fearsome presence of the fey. As an action, you can cause each creature in a 10-foot cube originating from you to make a Wisdom saving throw against your warlock spell save DC, or against {player.spellsavedc[i]}. The creatures that fail their saving throws are all charmed or frightened by you (your choice) until the end of your next turn.\nOnce you use this feature, you can't use it again until you finish a short or long rest.")
                    if warlvl >= 6:
                        player.classnotes.append("Misty Escape (see notes)")
                        player.notes.append("Misty Escape - You can vanish in a puff of mist in response to harm. When you take damage, you can use your reaction to turn invisible and teleport up to 60 feet to an unoccupied space you can see. You remain invisible until the start of your next turn or until you attack or cast a spell.\nOnce you use this feature, you can't use it again until you finish a short or long rest.")
                    if warlvl >= 10:
                        player.classnotes.append("Beguiling Defenses (see notes)")
                        player.notes.append(f"Beguiling Defenses - Your patron teaches you how to turn the mind-affecting magic of your enemies against them. You are immune to being charmed, and when another creature attempts to charm you, you can use your reaction to attempt to turn the charm back on that creature. The creature must succeed on a Wisdom saving throw against your warlock spell save DC, or against {player.spellsavedc[i]}, or be charmed by you for 1 minute or until the creature takes any damage.")
                    if warlvl >= 14:
                        player.classnotes.append("Dark Delirium (see notes)")
                        player.notes.append("Dark Delirium - You can plunge a creature into an illusory realm. As an action, choose a creature that you can see within 60 feet of you. It must make a Wisdom saving throw against your warlock spell save DC. On a failed save, it is charmed or frightened by you (your choice) for 1 minute or until your concentration is broken (as if you are concentrating on a spell). This effect ends early if the creature takes any damage.\nUntil this illusion ends, the creature thinks it is lost in a misty realm, the appearance of which you choose. The creature can see and hear only itself, you, and the illusion.\nYou must finish a short or long rest before you can use this feature again.")                 
                if player.subclass[i] == "Celestial Patron Warlock":
                    Patron = "Celestial"
                    if player.beachballflag == True:
                        Patron = "Beachball"
                        player.subclass[i] == "Beachball(Celestial) Patron Warlock"
                    WarCelestialSpells = {
                        1: ["Cure Wounds", "Guiding Bolt"],
                        2: ["Flaming Sphere", "Lesser Restoration"],
                        3: ["Daylight", "Revivify"],
                        4: ["Guardian of Faith", "Wall of Fire"],
                        5: ["Flame Strike", "Greater Restoration"]
                    }
                    spell_list = []
                    for level, spells in WarCelestialSpells.items():
                        if level == 1:
                            spell_list.append(f"for {level}st level you get {', '.join(spells)}")
                        if level == 2:
                            spell_list.append(f"for {level}nd level you get {', '.join(spells)}")
                        if level == 3:
                            spell_list.append(f"for {level}rd level you get {', '.join(spells)}")                            
                        if level == 4:
                            spell_list.append(f"for {level}th level you get {', '.join(spells)}")
                        if level == 5:
                            spell_list.append(f"for {level}th level you get {', '.join(spells)}")                                                    
                    player.classnotes.append("Expanded Spell List (see notes)")
                    player.notes.append(f"Expanded Spell List - {Patron} lets you choose from an expanded list of spells when you learn a warlock spell. The following spells are added to the warlock spell list for you: {', '.join(spell_list)}.")                        
                    player.classnotes.append("Bonus Cantrips - You learn the Light and Sacred Flame cantrips. They count as warlock cantrips for you, but they don’t count against your number of cantrips known.")
                    player.classnotes.append("Healing Light (see notes)")
                    player.notes.append(f"Healing Light - You gain the ability to channel celestial energy to heal wounds. You have a pool of d6s that you spend to fuel this healing. The number of dice in the pool equals 1 + your Warlock level, or {1 + warlvl} dice.\nAs a bonus action, you can heal one creature you can see within 60 feet of you, spending dice from the pool. The maximum number of dice you can spend at once equals your Charisma modifier, or {player.ChaMod} dice, minimum of one die. Roll the dice you spend, add them together, and restore a number of hit points equal to the total.\nYour pool regains all expended dice when you finish a long rest.")
                    if warlvl >= 6:
                        player.classnotes.append(f"Radiant Soul - Your link to the Celestial allows you to serve as a conduit for radiant energy. You have resistance to radiant damage, and when you cast a spell that deals radiant or fire damage, you add your Charisma modifier, or {player.ChaMod}, to one radiant or fire damage roll of that spell against one of its targets.")
                    if warlvl >= 10:
                        player.classnotes.append("Celestial Resistance (see notes)")
                        player.notes.append(f"Celestial Resistance - You gain temporary hit points whenever you finish a short or long rest. These temporary hit points equal your Warlock level + your Charisma modifier, or {warlvl + player.ChaMod} temporary hit points. Additionally, choose up to five creatures you can see at the end of the rest. Those creatures each gain temporary hit points equal to your Warlock level + your Charisma modifier, divided in half, or {math.floor((warlvl+player.ChaMod)/2)} temporary hit points.")
                    if warlvl >= 14:
                        player.classnotes.append("Searing Vengeance (see notes)")
                        player.notes.append(f"Searing Vengeance - The radiant energy you channel allows you to resist death. When you have to make a death saving throw at the start of your turn, you can instead spring back to your feet with a burst of radiant energy. You regain hit points equal to half of your hitpoints, or {math.ceil(hitpoints/2)} hitpoints, and then you stand up if you so choose. Each creature of your choice that is within 30 feet of you takes radiant damage equal to 2d8 + your Charisma modifier, or 2d8 + {player.ChaMod} radiant damage, and is blinded until the end of the current turn.\nOnce you use this feature, you can’t use it again until you finish a long rest.")                
                if player.subclass[i] == "The Fathomless Patron Warlock":
                    Patron = "The Fathomless"
                    if player.beachballflag == True:
                        Patron = "Beachball"
                        player.subclass[i] == "Beachball(The Fathomless) Patron Warlock"
                    WarFathomlessSpells = {
                        1: ["Create or Destroy Water", "Thunderwave"],
                        2: ["Gust of Wind", "Silence"],
                        3: ["Lightning Bolt", "Sleet Storm"],
                        4: ["Control Water", "Summon Elemental (water only)"],
                        5: ["Bigby's Hand (appears as a tentacle)", "Cone of Cold"]
                    }
                    spell_list = []
                    for level, spells in WarFathomlessSpells.items():
                        if level == 1:
                            spell_list.append(f"for {level}st level you get {', '.join(spells)}")
                        if level == 2:
                            spell_list.append(f"for {level}nd level you get {', '.join(spells)}")
                        if level == 3:
                            spell_list.append(f"for {level}rd level you get {', '.join(spells)}")                            
                        if level == 4:
                            spell_list.append(f"for {level}th level you get {', '.join(spells)}")
                        if level == 5:
                            spell_list.append(f"for {level}th level you get {', '.join(spells)}")                                                    
                    player.classnotes.append("Expanded Spell List (see notes)")
                    player.notes.append(f"Expanded Spell List - {Patron} lets you choose from an expanded list of spells when you learn a warlock spell. The following spells are added to the warlock spell list for you: {', '.join(spell_list)}.")                        
                    TentacleDeepsDmg = "1d8"
                    if warlvl >= 10:
                        TentacleDeepsDmg = "2d8"
                    player.classnotes.append("Tentacle of the Deeps (see notes)")
                    player.notes.append(f"Tentacle of the Deeps - You can magically summon a spectral tentacle that strikes at your foes. As a bonus action, you create a 10-foot-long tentacle at a point you can see within 60 feet of you. The tentacle lasts for 1 minute or until you use this feature to create another tentacle.\nWhen you create the tentacle, you can make a melee spell attack against one creature within 10 feet of it. On a hit, the target takes {TentacleDeepsDmg} cold damage, and its speed is reduced by 10 feet until the start of your next turn.\nAs a bonus action on your turn, you can move the tentacle up to 30 feet and repeat the attack.\nYou can summon the tentacle a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
                    player.classnotes.append("Gift of the Sea - You gain a swimming speed of 40 feet, and you can breathe underwater.")
                    if warlvl >= 6:
                        player.classnotes.append("Oceanic Soul - You are now even more at home in the depths. You gain resistance to cold damage. In addition, when you are fully submerged, any creature that is also fully submerged can understand your speech, and you can understand theirs.")
                        GuardianCoilDmg = "1d8"
                        if warlvl >= 10:
                            GuardianCoilDmg = "2d8"
                        player.classnotes.append("Guardian Coil (see notes)")
                        player.notes.append(f"Guardian Coil - Your Tentacle of the Deeps can defend you and others, interposing itself between them and harm.\nWhen you or a creature you can see takes damage while within 10 feet of the tentacle, you can use your reaction to choose one of those creatures and reduce the damage to that creature by {GuardianCoilDmg}.")
                    if warlvl >= 10:
                        player.classnotes.append("Grasping Tentacles (see notes)")
                        player.notes.append(f"Grasping Tentacles - You learn the spell Evard's Black Tentacles. It counts as a warlock spell for you, but it doesn't count against the number of spells you know. You can also cast it once without a spell slot, and you regain the ability to do so when you finish a long rest.\nWhenever you cast this spell, your patron's magic bolsters you, granting you a number of temporary hit points equal to your Warlock level, or {warlvl} temporary hit points. Moreover, damage can't break your concentration on this spell.")
                    if warlvl >= 14:
                        player.classnotes.append("Fathomless Plunge (see notes)")
                        player.notes.append("Fathomless Plunge - You can magically open temporary conduits to watery destinations. As an action, you can teleport yourself and up to five other willing creatures that you can see within 30 feet of you. Amid a whirl of tentacles, you all vanish and then reappear up to 1 mile away in a body of water you've seen (pond size or larger) or within 30 feet of it, each of you appearing in an unoccupied space within 30 feet of the others.\nOnce you use this feature, you can't use it again until you finish a short or long rest.")                 
                if player.subclass[i] == "Fiend Patron Warlock":
                    Patron = "Fiend"
                    if player.beachballflag == True:
                        Patron = "Beachball"
                        player.subclass[i] == "Beachball(Fiend) Patron Warlock"
                    WarFiendSpells = {
                        1: ["Burning Hands", "Command"],
                        2: ["Blindness/Deafness", "Scorching Ray"],
                        3: ["Fireball", "Stinking Cloud"],
                        4: ["Fire Shield", "Wall of Fire"],
                        5: ["Flame Strike", "Hallow"]
                    }
                    spell_list = []
                    for level, spells in WarFiendSpells.items():
                        if level == 1:
                            spell_list.append(f"for {level}st level you get {', '.join(spells)}")
                        if level == 2:
                            spell_list.append(f"for {level}nd level you get {', '.join(spells)}")
                        if level == 3:
                            spell_list.append(f"for {level}rd level you get {', '.join(spells)}")                            
                        if level == 4:
                            spell_list.append(f"for {level}th level you get {', '.join(spells)}")
                        if level == 5:
                            spell_list.append(f"for {level}th level you get {', '.join(spells)}")                                                    
                    player.classnotes.append("Expanded Spell List (see notes)")
                    player.notes.append(f"Expanded Spell List - {Patron} lets you choose from an expanded list of spells when you learn a warlock spell. The following spells are added to the warlock spell list for you: {', '.join(spell_list)}.")                        
                    player.classnotes.append(f"Dark One's Blessing - When you reduce a hostile creature to 0 hit points, you gain temporary hit points equal to your Charisma modifier + your warlock level, or {player.ChaMod + warlvl} temporary hitpoints.")
                    if warlvl >= 6:
                        player.classnotes.append("Dark One's Own Luck (see notes)")
                        player.notes.append("Dark One's Own Luck - You can call on your patron to alter fate in your favor. When you make an ability check or a saving throw, you can use this feature to add a d10 to your roll. You can do so after seeing the initial roll but before any of the roll's effects occur.\nOnce you use this feature, you can't use it again until you finish a short or long rest.")
                    if warlvl >= 10:
                        player.classnotes.append("Fiendish Resilience - You can choose one damage type when you finish a short or long rest. You gain resistance to that damage type until you choose a different one with this feature. Damage from magical weapons or silver weapons ignores this resistance.")
                    if warlvl >= 14:
                        player.classnotes.append("Hurl Through Hell (see notes)")
                        player.notes.append("Hurl Through Hell - When you hit a creature with an attack, you can use this feature to instantly transport the target through the lower planes. The creature disappears and hurtles through a nightmare landscape.\nAt the end of your next turn, the target returns to the space it previously occupied, or the nearest unoccupied space. If the target is not a fiend, it takes 10d10 psychic damage as it reels from its horrific experience.\nOnce you use this feature, you can't use it again until you finish a long rest")                 
                if player.subclass[i] == "The Genie Patron Warlock":
                    GenK1 = "Dao, or Earth Genie"
                    GenK2 = "Djinni, or Air Genie"
                    GenK3 = "Efreeti, or Fire Genie"
                    GenK4 = "Marid, or Water Genie"
                    GenK = [GenK1, GenK2, GenK3, GenK4]
                    if param == "Y":
                        print("0 - Random")
                        for w, genie in enumerate(GenK, 1):
                            print(f"{w} - {genie}")
                        genieinput = int(input("Choose the kind of Genie your patron will be. "))
                        if genieinput == 0:
                            GenieKind = random.choice(GenK)
                        elif 1 <= genieinput <= len(GenK):
                            GenieKind = GenK[genieinput - 1]
                    if param == "N":
                        GenieKind = random.choice(GenK)
                    Patron = "The Genie"
                    if player.beachballflag == True:
                        Patron = "Beachball"
                        player.subclass[i] == "Beachball(The Genie) Patron Warlock"
                        player.classnotes.append(f"As a Beachball-styled Genie Patron Warlock, your Beachball-Genie is a(n): {GenieKind}")
                    else:
                        player.classnotes.append(f"As a Genie Patron Warlock, your Genie is a(n): {GenieKind}")                  
                    if GenieKind == GenK1:  # Dao
                        WarGenieSpells = {
                            1: ["Detect Evil and Good", "Sanctuary"],
                            2: ["Phantasmal Force", "Spike Growth"],
                            3: ["Create Food and Water", "Meld Into Stone"],
                            4: ["Phantasmal Killer", "Stone Shape"],
                            5: ["Creation", "Wall of Stone"],
                            9: ["Wish"]
                        }

                    elif GenieKind == GenK2:  # Djinni
                        WarGenieSpells = {
                            1: ["Detect Evil and Good", "Thunderwave"],
                            2: ["Phantasmal Force", "Gust of Wind"],
                            3: ["Create Food and Water", "Wind Wall"],
                            4: ["Phantasmal Killer", "Greater Invisibility"],
                            5: ["Creation", "Seeming"],
                            9: ["Wish"]
                        }

                    elif GenieKind == GenK3:  # Efreeti
                        WarGenieSpells = {
                            1: ["Detect Evil and Good", "Burning Hands"],
                            2: ["Phantasmal Force", "Scorching Ray"],
                            3: ["Create Food and Water", "Fireball"],
                            4: ["Phantasmal Killer", "Fire Shield"],
                            5: ["Creation", "Flame Strike"],
                            9: ["Wish"]
                        }

                    elif GenieKind == GenK4:  # Marid
                        WarGenieSpells = {
                            1: ["Detect Evil and Good", "Fog Cloud"],
                            2: ["Phantasmal Force", "Blur"],
                            3: ["Create Food and Water", "Sleet Storm"],
                            4: ["Phantasmal Killer", "Control Water"],
                            5: ["Creation", "Cone of Cold"],
                            9: ["Wish"]
                        }
                    spell_list = []
                    for level, spells in WarGenieSpells.items():
                        if level == 1:
                            spell_list.append(f"for {level}st level you get {', '.join(spells)}")
                        if level == 2:
                            spell_list.append(f"for {level}nd level you get {', '.join(spells)}")
                        if level == 3:
                            spell_list.append(f"for {level}rd level you get {', '.join(spells)}")                            
                        if level == 4:
                            spell_list.append(f"for {level}th level you get {', '.join(spells)}")
                        if level == 5:
                            spell_list.append(f"for {level}th level you get {', '.join(spells)}")                                                    
                    player.classnotes.append("Expanded Spell List (see notes)")
                    player.notes.append(f"Expanded Spell List - {Patron} lets you choose from an expanded list of spells when you learn a warlock spell. The following spells are added to the warlock spell list for you, and you will also get spells associated with your patron's kind (dao, djinni, efreeti, or marid): {', '.join(spell_list)}.")                
                    Vessel1 = "Oil lamp"
                    Vessel2 = "Urn"
                    Vessel3 = "Ring with a compartment"
                    Vessel4 = "Stoppered bottle"
                    Vessel5 = "Hollow statuette"
                    Vessel6 = "Ornate lantern"
                    Vessel = [Vessel1, Vessel2, Vessel3, Vessel4, Vessel5, Vessel6]
                    if param == "Y":
                        print("0 - Random")
                        for w, gv in enumerate(Vessel, 1):
                            print(f"{w} - {gv}")
                        gvinput = int(input("Choose which Genie Vessel for your patron you would prefer. "))
                        if gvinput == 0:
                            GenieVessel = random.choice(Vessel)
                        elif 1 <= gvinput <= len(Vessel):
                            GenieVessel = Vessel[gvinput - 1]
                    if param == "N":
                        GenieVessel = random.choice(Vessel)
                    player.classnotes.append("Genie's Vessel (see notes)")
                    player.notes.append(f"Genie's Vessel - Your patron gifts you a magical vessel that grants you a measure of the genie's power. The vessel is a Tiny object, and you can use it as a spellcasting focus for your warlock spells. The Vessel was decided either randomly or via a questionnaire upon making the character. While you are touching the vessel, you can use it in the following ways:\nBottled Respite - As an action, you can magically vanish and enter your vessel, which remains in the space you left. The interior of the vessel is an extradimensional space in the shape of a 20-foot-radius cylinder, 20 feet high, and resembles your vessel. The interior is appointed with cushions and low tables and is a comfortable temperature. While inside, you can hear the area around your vessel as if you were in its space. You can remain inside the vessel up to a number of hours equal to twice your Proficiency Bonus, or {player.profbonus * 2} hours. You exit the vessel early if you use a bonus action to leave, if you die, or if the vessel is destroyed. When you exit the vessel, you appear in the unoccupied space closest to it. Any objects left in the vessel remain there until carried out, and if the vessel is destroyed, every object stored there harmlessly appears in the unoccupied spaces closest to the vessel's former space. Once you enter the vessel, you can't enter again until you finish a long rest.Genie's Wrath - Once during each of your turns when you hit with an attack roll, you can deal extra damage to the target equal to your Proficiency Bonus, or {player.profbonus}. The type of this damage is determined by your patron: bludgeoning (dao), thunder (djinni), fire (efreeti), or cold (marid).\nThe vessel's AC equals your spell save DC, or {player.spellsavedc[i]}. Its hit points equal your Warlock level + your Proficiency Bonus, or {warlvl + player.profbonus} hit points, and it is immune to poison and psychic damage.\nIf the vessel is destroyed or you lose it, you can perform a 1-hour ceremony to receive a replacement from your patron. This ceremony can be performed during a short or long rest, and the previous vessel is destroyed if it still exists. The vessel vanishes in a flare of elemental power when you die.")
                    if warlvl >= 6:
                        player.classnotes.append("Elemental Gift (see notes)")
                        player.notes.append(f"Elemental Gift - You begin to take on characteristics of your patron's kind. You now have resistance to a damage type determined by your patron's kind: bludgeoning (dao), thunder (djinni), fire (efreeti), or cold (marid).\nIn addition, as a bonus action, you can give yourself a flying speed of 30 feet that lasts for 10 minutes, during which you can hover. You can use this bonus action a number of times equal to your Proficieny Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.")
                    if warlvl >= 10:
                        player.classnotes.append("Sanctuary Vessel (see notes)")
                        player.notes.append(f"Sanctuary Vessel - When you enter your Genie's Vessel via the Bottled Respite feature, you can now choose up to five willing creatures that you can see within 30 feet of you, and the chosen creatures are drawn into the vessel with you.\nAs a bonus action, you can eject any number of creatures from the vessel, and everyone is ejected if you leave or die or if the vessel is destroyed.\nIn addition, anyone (including you) who remains within the vessel for at least 10 minutes gains the benefit of finishing a short rest, and anyone can add your Proficiency Bonus, or {player.profbonus}, to the number of hit points they regain if they spend any Hit Dice as part of a short rest there.")
                    if warlvl >= 14:
                        player.classnotes.append("Limited Wish (see notes)")
                        player.notes.append("Limited Wish - You entreat your patron to grant you a small wish. As an action, you can speak your desire to your Genie's Vessel, requesting the effect of one spell that is 6th level or lower and has a casting time of 1 action. The spell can be from any class's spell list, and you don't need to meet the requirements in that spell, including costly components: the spell simply takes effect as part of this action.\nOnce you use this feature, you can't use it again until you finish 1d4 long rests.")
                if player.subclass[i] == "Great Old One Patron Warlock":
                    Patron = "Great Old One"
                    if player.beachballflag == True:
                        Patron = "Beachball"
                        player.subclass[i] == "Beachball(Great Old One) Patron Warlock"
                    WarGreatOldOneSpells = {
                        1: ["Dissonant Whispers", "Tasha's Hideous Laughter"],
                        2: ["Detect Thoughts", "Phantasmal Force"],
                        3: ["Clairvoyance", "Sending"],
                        4: ["Dominate Beast", "Evard's Black Tentacles"],
                        5: ["Dominate Person", "Telekinesis"]
                    }
                    spell_list = []
                    for level, spells in WarGreatOldOneSpells.items():
                        if level == 1:
                            spell_list.append(f"for {level}st level you get {', '.join(spells)}")
                        if level == 2:
                            spell_list.append(f"for {level}nd level you get {', '.join(spells)}")
                        if level == 3:
                            spell_list.append(f"for {level}rd level you get {', '.join(spells)}")                            
                        if level == 4:
                            spell_list.append(f"for {level}th level you get {', '.join(spells)}")
                        if level == 5:
                            spell_list.append(f"for {level}th level you get {', '.join(spells)}")                                                    
                    player.classnotes.append("Expanded Spell List (see notes)")
                    player.notes.append(f"Expanded Spell List - {Patron} lets you choose from an expanded list of spells when you learn a warlock spell. The following spells are added to the warlock spell list for you: {', '.join(spell_list)}.")                        
                    player.classnotes.append("Awakened Mind (see notes)")
                    player.notes.append("Awakened Mind - Your alien knowledge gives you the ability to touch the minds of other creatures. You can communicate telepathically with any creature you can see within 30 feet of you. You don't need to share a language with the creature for it to understand your telepathic utterances, but the creature must be able to understand at least one language.")
                    if warlvl >= 6:
                        player.classnotes.append("Entropic Ward (see notes)")
                        player.notes.append("Entropic Ward - You learn to magically ward yourself against attack and to turn an enemy's failed strike into good luck for yourself. When a creature makes an attack roll against you, you can use your reaction to impose disadvantage on that roll. If the attack misses you, your next attack roll against the creature has advantage if you make it before the end of your next turn.\nOnce you use this feature, you can't use it again until you finish a short or long rest.")
                    if warlvl >= 10:
                        player.classnotes.append("Thought Shield - Your thoughts can't be read by telepathy or other means unless you allow it. You also have resistance to psychic damage, and whenever a creature deals psychic damage to you, that creature takes the same amount of damage that you do.")
                    if warlvl >= 14:
                        player.classnotes.append("Create Thrall (see notes)")
                        player.notes.append("Create Thrall - You gain the ability to infect a humanoid's mind with the alien magic of your patron. You can use your action to touch an incapacitated humanoid. That creature is then charmed by you until a Remove Curse spell is cast on it, the charmed condition is removed from it, or you use this feature again.\nYou can communicate telepathically with the charmed creature as long as the two of you are on the same plane of existence.")
                if player.subclass[i] == "Hexblade Patron Warlock":
                    Patron = "Hexblade"
                    if player.beachballflag == True:
                        Patron = "Beachball"
                        player.subclass[i] == "Beachball(Hexblade) Patron Warlock"
                    WarHexbladeSpells = {
                        1: ["Shield", "Wrathful Smite"],
                        2: ["Blur", "Branding Smite"],
                        3: ["Blink", "Elemental Weapon"],
                        4: ["Phantasmal Killer", "Staggering Smite"],
                        5: ["Banishing Smite", "Cone of Cold"]
                    }
                    spell_list = []
                    for level, spells in WarHexbladeSpells.items():
                        if level == 1:
                            spell_list.append(f"for {level}st level you get {', '.join(spells)}")
                        if level == 2:
                            spell_list.append(f"for {level}nd level you get {', '.join(spells)}")
                        if level == 3:
                            spell_list.append(f"for {level}rd level you get {', '.join(spells)}")                            
                        if level == 4:
                            spell_list.append(f"for {level}th level you get {', '.join(spells)}")
                        if level == 5:
                            spell_list.append(f"for {level}th level you get {', '.join(spells)}")                                                    
                    player.classnotes.append("Expanded Spell List (see notes)")
                    player.notes.append(f"Expanded Spell List - {Patron} lets you choose from an expanded list of spells when you learn a warlock spell. The following spells are added to the warlock spell list for you: {', '.join(spell_list)}.")                        
                    player.classnotes.append("Hexblade's Curse (see notes)")
                    player.notes.append(f"Hexblade's Curse - You gain the ability to place a baleful curse on someone. As a bonus action, choose one creature you can see within 30 feet of you. The target is cursed for 1 minute. The curse ends early if the target dies, you die, or you are incapacitated. Until the curse ends, you gain the following benefits:\n- You gain a bonus to damage rolls against the cursed target equal to your Proficiency Bonus, or a bonus of {player.profbonus}.\n- Any attack roll you make against the cursed target is a critical hit on a roll of 19 or 20 on the d20.\n- If the cursed target dies, you regain hit points equal to your Warlock level + your Charisma modifier, or {warlvl + player.ChaMod} hit points.\nYou can’t use this feature again until you finish a short or long rest.")
                    profs = ["Medium Armor", "Shield", "Martial Weapons"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)                  
                    player.classnotes.append("Hex Warrior (see notes)")
                    player.notes.append(f"Hex Warrior - The influence of your patron also allows you to mystically channel your will through a particular weapon. Whenever you finish a long rest, you can touch one weapon that you are proficient with and that lacks the two-handed property. When you attack with that weapon, you can use your Charisma modifier, or {player.ChaMod}, instead of Strength or Dexterity, for the attack and damage rolls. This benefit lasts until you finish a long rest. If you later gain the Pact of the Blade feature, this benefit extends to every pact weapon you conjure with that feature, no matter the weapon's type.")
                    if warlvl >= 6:
                        player.classnotes.append("Accursed Specter (see notes)")
                        player.notes.append(f"Accursed Specter - You can curse the soul of a person you slay, temporarily binding it in your service. When you slay a humanoid, you can cause its spirit to rise from its corpse as a Specter. When the specter appears, it gains temporary hit points equal to half your Warlock level, or {math.ceil(warlvl/2)} temporary hit points. Roll initiative for the specter, which has its own turns. It obeys your verbal commands, and it gains a special bonus to its attack rolls equal to your Charisma modifier, or a bonus of {player.ChaMod}.\nThe specter remains in your service until the end of your next long rest, at which point it vanishes to the afterlife.\nOnce you bind a specter with this feature, you can't use the feature again until you finish a long rest.")
                    if warlvl >= 10:
                        player.classnotes.append("Armor of Hexes - Your hex grows more powerful. If the target cursed by your Hexblade’s Curse hits you with an attack roll, roll a d6. On a 4 or higher, the attack instead misses you, regardless of its roll.")
                    if warlvl >= 14:
                        player.classnotes.append("Master of Hexes (see notes)")
                        player.notes.append("Master of Hexes - You can spread your Hexblade's Curse from a slain creature to another creature. When the creature cursed by your Hexblade's Curse dies, you can apply the curse to a different creature you can see within 30 feet of you, provided you aren't incapacitated. When you apply the curse in this way, you don't regain hit points from the death of the previously cursed creature.")                
                if player.subclass[i] == "Undead Patron Warlock":
                    Patron = "Undead"
                    if player.beachballflag == True:
                        Patron = "Beachball"
                        player.subclass[i] == "Beachball(Undead) Patron Warlock"
                    WarUndeadSpells = {
                        1: ["Bane", "False Life"],
                        2: ["Blindness/Deafness", "Phantasmal Force"],
                        3: ["Phantom Steed", "Speak With Dead"],
                        4: ["Death Ward", "Greater Invisibility"],
                        5: ["Antilife Shell", "Cloudkill"]
                    }
                    spell_list = []
                    for level, spells in WarUndeadSpells.items():
                        if level == 1:
                            spell_list.append(f"for {level}st level you get {', '.join(spells)}")
                        if level == 2:
                            spell_list.append(f"for {level}nd level you get {', '.join(spells)}")
                        if level == 3:
                            spell_list.append(f"for {level}rd level you get {', '.join(spells)}")                            
                        if level == 4:
                            spell_list.append(f"for {level}th level you get {', '.join(spells)}")
                        if level == 5:
                            spell_list.append(f"for {level}th level you get {', '.join(spells)}")                                                    
                    player.classnotes.append("Expanded Spell List (see notes)")
                    player.notes.append(f"Expanded Spell List - {Patron} lets you choose from an expanded list of spells when you learn a warlock spell. The following spells are added to the warlock spell list for you: {', '.join(spell_list)}.")                        
                    player.classnotes.append("Form of Dread (see notes)")
                    player.notes.append(f"Form of Dread - You manifest an aspect of your patron’s dreadful power. As a bonus action, you transform for 1 minute. You gain the following benets while transformed:\n- You gain temporary hit points equal to 1d10 + your Warlock level, or 1d10 + {warlvl} temporary hitpoints.\n- Once during each of your turns, when you hit a creature with an attack roll, you can force it to make a Wisdom saving throw, and if the saving throw fails, the target is frightened of you until the end of your next turn.\n- You are immune to the frightened condition.\nYou can transform a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses when you finish a long rest.\nThe appearance of your Form of Dread reflects some aspect of your patron. For example, your form could be a shroud of shadows forming the crown and robes of your lich patron, or your body might glow with glyphs from ancient funerary rites and be surrounded by desert winds, suggesting your mummy patron.")
                    if warlvl >= 6:
                        player.classnotes.append("Grave Touched (see notes)")
                        player.notes.append("Grave Touched - Your patron’s powers have a profound effect on your body and magic. You don’t need to eat, drink, or breathe.\nIn addition, once during each of your turns, when you hit a creature with an attack roll and roll damage against the creature, you can replace the damage type with necrotic damage. While you are using your Form of Dread, you can roll one additional damage die when determining the necrotic damage the target takes.")
                    if warlvl >= 10:
                        player.classnotes.append("Necrotic Husk (see notes)")
                        player.notes.append(f"Necrotic Husk - Your connection to undeath and necrotic energy now saturates your body. You have resistance to necrotic damage. If you are transformed using your Form of Dread, you instead become immune to necrotic damage.\nIn addition, when you would be reduced to 0 hit points, you can use your reaction to drop to 1 hit point instead and cause your body to erupt with deathly energy. Each creature of your choice that is within 30 feet of you takes necrotic damage equal to 2d10 + your Warlock level, or 2d10 + {warlvl} necrotic damage. You then gain 1 level of exhaustion. Once you use this reaction, you can’t do so again until you finish 1d4 long rests.")
                    if warlvl >= 14:
                        player.classnotes.append("Spirit Projection (see notes)")
                        player.notes.append("Spirit Projection - Your spirit can become untethered from your physical form. As an action, you can project your spirit from your body. The body you leave behind is unconscious and in a state of suspended animation.\nYour spirit resembles your mortal form in almost every way, replicating your game statistics but not your possessions. Any damage or other effects that apply to your spirit or physical body affects the other. Your spirit can remain outside your body for up to 1 hour or until your concentration is broken (as if concentrating on a spell). When your projection ends, your spirit returns to your body or your body magically teleports to your spirit’s space (your choice).\nWhile projecting your spirit, you gain the following benefits:\n- Your spirit and body gain resistance to bludgeoning, piercing, and slashing damage.\n- When you cast a spell of the conjuration or necromancy school, the spell doesn’t require verbal or somatic components or material components that lack a gold cost.\n- You have a flying speed equal to your walking speed and can hover. You can move through creatures and objects as if they were difficult terrain, but you take 1d10 force damage if you end your turn inside a creature or an object.\n- While you are using your Form of Dread, once during each of your turns when you deal necrotic damage to a creature, you regain hit points equal to half the amount of necrotic damage dealt.\nOnce you use this feature, you can’t do so again until you finish a long rest.")                
                if player.subclass[i] == "Undying Patron Warlock":                 
                    Patron = "Undying"
                    if player.beachballflag == True:
                        Patron = "Beachball"
                        player.subclass[i] == "Beachball(Undying) Patron Warlock"
                    WarUndyingSpells = {
                        1: ["False Life", "Ray of Sickness"],
                        2: ["Blindness/Deafness", "Silence"],
                        3: ["Feign Death", "Speak with Dead"],
                        4: ["Aura of Life", "Death Ward"],
                        5: ["Contagion", "Legend Lore"]
                    }
                    spell_list = []
                    for level, spells in WarUndyingSpells.items():
                        if level == 1:
                            spell_list.append(f"for {level}st level you get {', '.join(spells)}")
                        if level == 2:
                            spell_list.append(f"for {level}nd level you get {', '.join(spells)}")
                        if level == 3:
                            spell_list.append(f"for {level}rd level you get {', '.join(spells)}")                            
                        if level == 4:
                            spell_list.append(f"for {level}th level you get {', '.join(spells)}")
                        if level == 5:
                            spell_list.append(f"for {level}th level you get {', '.join(spells)}")                                                    
                    player.classnotes.append("Expanded Spell List (see notes)")
                    player.notes.append(f"Expanded Spell List - {Patron} lets you choose from an expanded list of spells when you learn a warlock spell. The following spells are added to the warlock spell list for you: {', '.join(spell_list)}.")                        
                    player.classnotes.append("Among the Dead (see notes)")
                    player.notes.append(f"Among the Dead - You learn the Spare the Dying cantrip, which counts as a warlock cantrip for you. You also have advantage on saving throws against any disease.\nAdditionally, undead have difficulty harming you. If an undead targets you directly with an attack or a harmful spell, that creature must make a Wisdom saving throw against your spell save DC, or against {player.spellsavedc[i]} (an undead needn't make the save when it includes you in an area effect, such as the explosion of Fireball). On a failed save, the creature must choose a new target or forfeit targeting someone instead of you, potentially wasting the attack or spell. On a successful save, the creature is immune to this effect for 24 hours. An undead is also immune to this effect for 24 hours if you target it with an attack or a harmful spell.")
                    if warlvl >= 6:
                        player.classnotes.append("Defy Death (see notes)")
                        player.notes.append(f"Defy Death - You can give yourself vitality when you cheat death or when you help someone else cheat it. You can regain hit points equal to 1d8 + your Constitution modifier, or 1d8 + {player.ChaMod} hitpoints, minimum of 1 hit point, when you succeed on a death saving throw or when you stabilize a creature with Spare the Dying.\nOnce you use this feature, you can't use it again until you finish a long rest.")
                    if warlvl >= 10:
                        player.classnotes.append("Undying Nature (see notes)")
                        player.notes.append("Undying Nature - You can hold your breath indefinitely, and you don't require food, water, or sleep, although you still require rest to reduce exhaustion and still benefit from finishing short and long rests.\nIn addition, you age at a slower rate. For every 10 years that pass, your body ages only 1 year, and you are immune to being magically aged.")
                    if warlvl >= 14:
                        player.classnotes.append("Indestructible Life (see notes)")
                        player.notes.append(f"Indestructible Life - You partake of some of the true secrets of the Undying. On your turn, you can use a bonus action to regain hit points equal to 1d8 + your Warlock level, or 1d8 + {warlvl} hit points. Additionally, if you put a severed body part of yours back in place when you use this feature, the part reattaches.\nOnce you use this feature, you can't use it again until you finish a short or long rest.")                    
            if warlvl >= 2:
                WarlockSpellsKnown = 3
                WarlockSpellSlots = 2
                WarlockEldritchInvocations = 2
            if warlvl >= 3:                    
                WarlockSpellsKnown = 4
                WarlockSlotLevel = "2nd"
                player.classnotes.append("Pact Boon (see notes)")
                player.notes.append(f"Pact Boon - Your otherworldly patron bestows a gift upon you for your loyal service. You gain one of the following features of your choice.\nPact of the Blade - You can use your action to create a pact weapon in your empty hand. You can choose the form that this melee weapon takes each time you create it (see the Weapons section for weapon options). You are proficient with it while you wield it. This weapon counts as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage.\nYour pact weapon disappears if it is more than 5 feet away from you for 1 minute or more. It also disappears if you use this feature again, if you dismiss the weapon (no action required), or if you die.\nYou can transform one magic weapon into your pact weapon by performing a special ritual while you hold the weapon. You perform the ritual over the course of 1 hour, which can be done during a short rest. You can then dismiss the weapon, shunting it into an extradimensional space, and it appears whenever you create your pact weapon thereafter. You can’t affect an artifact or a sentient weapon in this way. The weapon ceases being your pact weapon if you die, if you perform the 1-hour ritual on a different weapon, or if you use a 1-hour ritual to break your bond to it. The weapon appears at your feet if it is in the extradimensional space when the bond breaks.\nPact of the Chain - You learn the Find Familiar spell and can cast it as a ritual. The spell doesn’t count against your number of spells known.\nWhen you cast the spell, you can choose one of the normal forms for your familiar or one of the following special forms: Imp, Pseudodragon, Quasit, or Sprite.\nAdditionally, when you take the Attack action, you can forgo one of your own attacks to allow your familiar to make one attack with its reaction.\n- Pact of the Talisman - Your patron gives you an amulet, a talisman that can aid the wearer when the need is great. When the wearer fails an ability check, they can add a d4 to the roll, potentially turning the roll into a success. This benefit can be used a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and all expended uses are restored when you finish a long rest.\nIf you lose the talisman, you can perform a 1-hour ceremony to receive a replacement from your patron. This ceremony can be performed during a short or long rest, and it destroys the previous amulet. The talisman turns to ash when you die.\n- Pact of the Tome - Your patron gives you a grimoire called a Book of Shadows. When you gain this feature, choose three cantrips from any class’s spell list (the three needn’t be from the same list). While the book is on your person, you can cast those cantrips at will. They don’t count against your number of cantrips known. If they don’t appear on the warlock spell list, they are nonetheless warlock spells for you.\nIf you lose your Book of Shadows, you can perform a 1-hour ceremony to receive a replacement from your patron. This ceremony can be performed during a short or long rest, and it destroys the previous book. The book turns to ash when you die.")
            if warlvl >= 4:
                WarlockCantripsKnown = 3
                WarlockSpellsKnown = 5
                player.classnotes.append("Eldritch Versatility (see notes)")
                player.notes.append("Eldritch Versatility - Whenever you reach a level in this class that grants the Ability Score Improvement feature, you can do one of the following, representing a change of focus in your occult studies:\n- Replace one cantrip you learned from this class's Pact Magic feature with another cantrip from the warlock spell list.\n- Replace the option you chose for the Pact Boon feature with one of that feature's other options.\n= If you're 12th level or higher, replace one spell from your Mystic Arcanum feature with another warlock spell of the same level.\nIf this change makes you ineligible for any of your Eldritch Invocations, you must also replace them now, choosing invocations for which you qualify.")
            if warlvl >= 5:
                WarlockSpellsKnown = 6
                WarlockSlotLevel = "3rd"
                WarlockEldritchInvocations = 3
            if warlvl >= 6:
                WarlockSpellsKnown = 7
            if warlvl >= 7:
                WarlockSpellsKnown = 8
                WarlockSlotLevel = "4th"
                WarlockEldritchInvocations = 4
            if warlvl >= 8:
                WarlockSpellsKnown = 9
            if warlvl >= 9:
                WarlockSpellsKnown = 10
                WarlockSlotLevel = "5th"
                WarlockEldritchInvocations = 5
            if warlvl >= 10:
                WarlockCantripsKnown = 4
            if warlvl >= 11:
                WarlockSpellsKnown = 11
                WarlockSpellSlots = 3
                MysticArcanum = []
                MysticArcanum.append("6th level spell")
                if warlvl >= 13:
                    MysticArcanum.append("7th level spell")
                if warlvl >= 15:
                    MysticArcanum.append("8th level spell")
                if warlvl >= 17:
                    MysticArcanum.append("9th level spell")
                MysticArcanum_str = ", ".join(f" one {warspell}" for warspell in MysticArcanum)
                player.classnotes.append("Mystic Arcanum (see notes)")
                player.notes.append(f"Mystic Arcanum - Your patron bestows upon you a magical secret called an arcanum. The spells acquired by this are: {MysticArcanum_str}, from the warlock spell list as this arcanum.\nYou can cast your arcanum spell once without expending a spell slot. You must finish a long rest before you can do so again.\nMore spells are unlocked at higher levels. You regain all uses of your Mystic Arcanum when you finish a long rest.")
            if warlvl >= 12:
                WarlockEldritchInvocations = 6
            if warlvl >= 13:
                WarlockSpellsKnown = 12
            if warlvl >= 15:
                WarlockSpellsKnown = 13
                WarlockEldritchInvocations = 7
            if warlvl >= 17:
                WarlockSpellsKnown = 14
                WarlockSpellSlots = 4
            if warlvl >= 18:
                WarlockEldritchInvocations = 8
            if warlvl >= 19:
                WarlockSpellsKnown = 15
            if warlvl == 20:
                player.classnotes.append("Eldritch Master (see notes)")
                player.notes.append("Eldritch Master - You can draw on your inner reserve of mystical power while entreating your patron to regain expended spell slots. You can spend 1 minute entreating your patron for aid to regain all your expended spell slots from your Pact Magic feature. Once you regain spell slots with this feature, you must finish a long rest before you can do so again.")
            player.notes.append(f"You have {WarlockCantripsKnown} cantrips available to you.")
            player.notes.append(f"You know {WarlockSpellsKnown} spells.")
            player.notes.append(f"You have {WarlockSpellSlots} spell slots available.")
            player.notes.append(f"Your spell slots are {WarlockSlotLevel} level.")
            if warlvl >= 2:
                player.classnotes.append("Eldritch Invocations (see notes)")
                player.notes.append(f"Eldritch Invocations - In your study of occult lore, you have unearthed eldritch invocations, fragments of forbidden knowledge that imbue you with an abiding magical ability. A level prerequisite refers to your level in this class.\nYou have {WarlockEldritchInvocations} available to you, of your choice.\nAdditionally, when you gain a level in this class, you can choose one of the invocations you know and replace it with another invocation that you could learn at that level.\nIf an eldritch invocation has prerequisites, you must meet them to learn it. You can learn the invocation at the same time that you meet its prerequisites. A level prerequisite refers to your level in this class.")
        if player.Class[i] == "Wizard":
            if ((param == "N") or (player.singlemulticlass == "N")):
                wizlvl = player.level
                player.classlvl.append(wizlvl)  
            if param == "Y":
                charlvlwhile = False
                while not charlvlwhile:                
                    wizlvl = int(input(f"Given your pool of levels of {poollevel}, what is your Wizard level? "))  
                    if wizlvl <= poollevel:
                        charlvlwhile = True
                    else:
                        print("You are only able to invest within your pool.")                
                poollevel = poollevel - wizlvl
                player.classlvl.append(wizlvl)     
            if wizlvl >= 1:
                player.hitdice.append(f"{wizlvl}d6 for {player.Class[i]}")
                if wizlvl == 1:
                    player.hitpoints += (6 + player.ConMod)
                else:
                    player.hitpoints += (6 + player.ConMod + hpcalc(wizlvl, dice, 6))    
                if i == 0:
                    profs = [
                        dnd_tools.simple_weapons["Dagger"]["Name"],
                        dnd_tools.simple_weapons["Dart"]["Name"],
                        dnd_tools.simple_weapons["Sling"]["Name"],
                        dnd_tools.simple_weapons["Quarterstaff"]["Name"],
                        dnd_tools.simple_weapons["LightCrossbow"]["Name"]
                        ]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)   
                    player.skills.append(dnd_tools.saving_throws["IntST"])
                    player.skills.append(dnd_tools.saving_throws["WisST"])
                    SkillsList = [
                        dnd_tools.skills["Arcana"], 
                        dnd_tools.skills["History"], 
                        dnd_tools.skills["Insight"], 
                        dnd_tools.skills["Investigation"], 
                        dnd_tools.skills["Medicine"], 
                        dnd_tools.skills["Religion"]
                        ]
                    player.skills = twoskillsfromlist(param, player.skills, SkillsList) 
                    StartEquip1 = ["Quarterstaff", "Dagger"]
                    StartEquip2 = ["A Component Pouch", "An Arcane Focus"]
                    StartEquip3 = ["Scholar's Pack", "Explorer's Pack"]
                    if param == "Y":
                        print("0 - Random")
                        print("1 - Quarterstaff")
                        print("2 - Dagger")
                        se1 = int(input("What would you like your first choice for starting equipment to be? "))
                        if se1 == 0:
                            SE1rand = random.choice(StartEquip1)
                            if SE1rand == "Quarterstaff":
                                player.equipment.append(dnd_tools.simple_weapons["Quarterstaff"].copy())
                            if SE1rand == "Dagger":
                                player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                        if se1 == 1:
                            player.equipment.append(dnd_tools.simple_weapons["Quarterstaff"].copy())
                        if se1 == 2:
                            player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                        print("0 - Random")
                        print("1 - A Component Pouch")
                        print("2 - An Arcane Focus")
                        se2 = int(input("What would you like your second choice for starting equipment to be? "))
                        if se2 == 0:
                            SE2rand = random.choice(StartEquip2)
                            if SE2rand == "A Component Pouch":
                                player.equipment.append("Component Pouch")
                            if SE2rand == "An Arcane Focus":
                                player.equipment.append("Arcane Focus")
                        if se2 == 1:
                            player.equipment.append("Component Pouch")
                        if se2 == 2:
                            player.equipment.append("Arcane Focus")
                        print("0 - Random")
                        print("1 - A Scholar's Pack")
                        print("2 - An Explorer's Pack")
                        se3 = int(input("What would you like your third choice for starting equipment to be? "))
                        if se3 == 0:
                            SE3rand = random.choice(StartEquip3)
                            if SE3rand == "Scholar's Pack":
                                player.equipment.extend(dnd_tools.packs["ScholarsPack"]["contents"])
                            if SE3rand == "Explorer's Pack":
                                player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])
                        if se3 == 1:
                            player.equipment.extend(dnd_tools.packs["ScholarsPack"]["contents"])   
                        if se3 == 2:
                            player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])
                        player.equipment.append("Spellbook")
                    if param == "N":
                        SE1rand = random.choice(StartEquip1)
                        if SE1rand == "Quarterstaff":
                            player.equipment.append(dnd_tools.simple_weapons["Quarterstaff"].copy())
                        if SE1rand == "Dagger":
                            player.equipment.append(dnd_tools.simple_weapons["Dagger"].copy())
                        SE2rand = random.choice(StartEquip2)
                        if SE2rand == "A Component Pouch":
                            player.equipment.append("Component Pouch")
                        if SE2rand == "An Arcane Focus":
                            player.equipment.append("Arcane Focus")
                        SE3rand = random.choice(StartEquip3)
                        if SE3rand == "Scholar's Pack":
                            player.equipment.extend(dnd_tools.packs["ScholarsPack"]["contents"])
                        if SE3rand == "Explorer's Pack":
                            player.equipment.extend(dnd_tools.packs["ExplorersPack"]["contents"])                            
                        player.equipment.append("Spellbook")       
                player.spellcastingclass.append("Wizard")
                player.spellcastingability.append("Int")
                player.spellsavedc.append(8 + player.profbonus + player.ChaMod)
                player.spellattackmod.append(player.profbonus + player.ChaMod)
                WizardCantripsKnown = 3
                WizardSpellSlot1 = 2
                WizardSpellSlot2 = 0
                WizardSpellSlot3 = 0
                WizardSpellSlot4 = 0
                WizardSpellSlot5 = 0
                WizardSpellSlot6 = 0
                WizardSpellSlot7 = 0
                WizardSpellSlot8 = 0
                WizardSpellSlot9 = 0  
                player.classnotes.append("Learning Spells of 1st Level and Higher (see notes)")
                player.notes.append("Learning Spells of 1st Level and Higher - Each time you gain a Wizard level, you can add two wizard spells of your choice to your spellbook for free. Each of these spells must be of a level for which you have spell slots, as shown on the Wizard table. On your adventures, you might find other spells that you can add to your spellbook (see the “Your Spellbook” sidebar).")                                                                                   
                player.classnotes.append("Your Spellbook (see notes)")
                player.notes.append("Your Spellbook - The spells that you add to your spellbook as you gain levels reflect the arcane research you conduct on your own, as well as intellectual breakthroughs you have had about the nature of the multiverse. You might find other spells during your adventures. You could discover a spell recorded on a scroll in an evil wizard’s chest, for example, or in a dusty tome in an ancient library.\nCopying a Spell into the Book. When you find a wizard spell of 1st level or higher, you can add it to your spellbook if it is of a spell level you can prepare and if you can spare the time to decipher and copy it.\nCopying that spell into your spellbook involves reproducing the basic form of the spell, then deciphering the unique system of notation used by the wizard who wrote it. You must practice the spell until you understand the sounds or gestures required, then transcribe it into your spellbook using your own notation.\nFor each level of the spell, the process takes 2 hours and costs 50 gp. The cost represents material components you expend as you experiment with the spell to master it, as well as the fine inks you need to record it. Once you have spent this time and money, you can prepare the spell just like your other spells.\nReplacing the Book. You can copy a spell from your own spellbook into another book—for example, if you want to make a backup copy of your spellbook. This is just like copying a new spell into your spellbook, but faster and easier, since you understand your own notation and already know how to cast the spell. You need spend only 1 hour and 10 gp for each level of the copied spell.\nIf you lose your spellbook, you can use the same procedure to transcribe the spells that you have prepared into a new spellbook. Filling out the remainder of your spellbook requires you to find new spells to do so, as normal. For this reason, many wizards keep backup spellbooks in a safe place.\nThe Book’s Appearance. Your spellbook is a unique compilation of spells, with its own decorative flourishes and margin player.notes. It might be a plain, functional leather volume that you received as a gift from your master, a finely bound gilt-edged tome you found in an ancient library, or even a loose collection of notes scrounged together after you lost your previous spellbook in a mishap.")
                player.classnotes.append("Arcane Recovery (see notes)")
                player.notes.append(f"Arcane Recovery - You have learned to regain some of your magical energy by studying your spellbook. Once per day when you finish a short rest, you can choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your Wizard level (rounded up), or {math.ceil(wizlvl/2)}, and none of the slots can be 6th level or higher.")
            if wizlvl >= 2:
                Wiz = ["Abjuration Arcane Tradition Wizard", "Bladesinging Arcane Tradition Wizard", "Blood Magic Arcane Tradition Wizard", "Chronurgy Magic Wizard", "Conjuration Arcane Tradition Wizard", "Divination Arcane Tradition Wizard", "Enchantment Arcane Tradition Wizard", "Evocation Arcane Tradition Wizard", "Graviturgy Magic Wizard", "Illusion Arcane Tradition Wizard", "Necromancy Arcane Tradition Wizard", "Order of Scribes Arcane Tradition Wizard", "Transmutation Arcane Tradition Wizard", "War Magic Arcane Tradition Wizard"]
                
                print(f"Subclasses are: {player.subclass}")
                if player.subclass[i] == "":
                    if param == "Y":
                        print("0 - Random")
                        for idx, subcl in enumerate(Wiz, 1):
                            print(f"{idx} - {subcl}")
                        subc = int(input("Which subclass would you like? ")) 
                        if subc == 0:
                            player.subclass[i] = random.choice(Wiz)
                        elif 1 <= subc <= len(Wiz):
                            player.subclass[i] = Wiz[subc - 1]
                    if param == "N":
                        player.subclass[i] = random.choice(Wiz)                               
                if player.subclass[i] == "Abjuration Arcane Tradition Wizard":
                    player.classnotes.append("Abjuration Savant - The gold and time you must spend to copy a abjuration spell into your spellbook is halved.")
                    player.classnotes.append("Arcane Ward (see notes)")
                    player.notes.append(f"Arcane Ward - You can weave magic around yourself for protection. When you cast an abjuration spell of 1st level or higher, you can simultaneously use a strand of the spell's magic to create a magical ward on yourself that lasts until you finish a long rest. The ward has hit points equal to twice your Wizard level + your Intelligence modifier, or {(2*wizlvl) + player.IntMod} hit points. Whenever you take damage, the ward takes the damage instead. If this damage reduces the ward to 0 hit points, you take any remaining damage.\nWhile the ward has 0 hit points, it can't absorb damage, but its magic remains. Whenever you cast an abjuration spell of 1st level or higher, the ward regains a number of hit points equal to twice the level of the spell.\nOnce you create the ward, you can't create it again until you finish a long rest.")
                    if wizlvl >= 6:
                        player.classnotes.append("Projected Ward - When a creature that you can see within 30 feet of you takes damage, you can use your reaction to cause your Arcane Ward to absorb that damage. If this damage reduces the ward to 0 hit points, the warded creature takes any remaining damage.")
                    if wizlvl >= 10:
                        player.classnotes.append(f"Improved Abjuration - When you cast an abjuration spell that requires you to make an ability check as a part of casting that spell (as in Counterspell and Dispel Magic), you add your Proficiency Bonus, or {player.profbonus}, to that ability check.")
                    if wizlvl >= 14:
                        player.classnotes.append("Spell Resistance - You have advantage on saving throws against spells.\nFurthermore, you have resistance against the damage of spells.")
                if player.subclass[i] == "Bladesinging Arcane Tradition Wizard":
                    profs = ["Light Armor"]
                    for prof in profs:
                        if prof not in player.proficiencies:
                            player.proficiencies.append(prof)
                    if dnd_tools.skills["Performance"] not in player.skills:
                        player.skills.append(dnd_tools.skills["Performance"])
                    if param == "Y":
                        print("0 - Random")
                        for wiz, ohw in enumerate(OneHandedWeaponsNames, 1):
                            print(f"{wiz} - {ohw}")
                        ohwinput = int(input("Choose a one-handed melee weapon to be gain proficiency in. "))
                        if ohwinput == 0:
                            Ohw_choice_rand = random.choice(OneHandedWeaponsNames)
                            player.proficiencies.append(Ohw_choice_rand)
                        elif 1 <= ohwinput <= len(OneHandedWeaponsNames):
                            player.proficiencies.append(OneHandedWeaponsNames[ohwinput-1])
                    if param == "N":
                        Ohw_choice_rand = random.choice(OneHandedWeaponsNames)
                        player.proficiencies.append(Ohw_choice_rand)
                    player.classnotes.append("Bladesong (see notes)")
                    player.notes.append(f"Bladesong - You can invoke an elven magic called the Bladesong, provided that you aren't wearing medium or heavy armor or using a shield. It graces you with supernatural speed, agility, and focus.\nYou can use a bonus action to start the Bladesong, which lasts for 1 minute. It ends early if you are incapacitated, if you don medium or heavy armor or a shield, or if you use two hands to make an attack with a weapon. You can also dismiss the Bladesong at any time (no action required).\nWhile your Bladesong is active, you gain the following benefits:\n- You gain a bonus to your AC equal to your Intelligence modifier, or bonus of {player.IntMod}, minimum of +1.\n- Your walking speed increases by 10 feet.\n- You have advantage on Dexterity (Acrobatics) checks.\n- You gain a bonus to any Constitution saving throw you make to maintain your concentration on a spell. The bonus equals your Intelligence modifier, or bonus of {player.IntMod}, minimum of +1.\nYou can use this feature a number of times equal to your Proficiency Bonus, or {player.profbonus} times, and you regain all expended uses of it when you finish a long rest.")
                    if wizlvl >= 6:
                        player.classnotes.append("Extra Attack - You can attack twice, instead of once, whenever you take the Attack action on your turn. Moreover, you can cast one of your can trips in place of one of those attacks.")
                    if wizlvl >= 10:
                        player.classnotes.append("Song of Defense - You can direct your magic to absorb damage while your Bladesong is active. When you take damage, you can use your reaction to expend one spell slot and reduce that damage to you by an amount equal to five times the spell slot's level.")
                    if wizlvl >= 14:
                        player.classnotes.append(f"Song of Victory - You can add your Intelligence modifier, or {player.IntMod}, minimum of +1, to the damage of your melee weapon attacks while your Bladesong is active.")
                if player.subclass[i] == "Blood Magic Arcane Tradition Wizard":
                    player.classnotes.append("Blood Channeling (see notes)")
                    player.notes.append("Blood Channeling - You are able to use your own depleted life essence to channel your magical abilities. Whenever your current hit points are below your hit point maximum, you can use your own body as an arcane focus.\nIn addition, when casting a wizard spell that requires a costly material component, you can forego the component by taking 1d10 necrotic damage per 50 gp of the cost of the component (minimum 1d10). This damage can't be reduced in any way. If this damage reduces you to 0 hit points, the spell fails but the spell slot is not expended.")
                    player.classnotes.append("Sanguine Burst (see notes)")
                    player.notes.append(f"Sanguine Burst - You learn how to weave your life force into a spell you cast, boosting its intensity at the cost of your vitality. Whenever you roll damage for a spell you've cast of 1st level or higher, you can choose to take necrotic damage equal to the spell's level to reroll a number of the damage dice up to your Intelligence modifier, or {player.IntMod} dice, minimum one. This damage can't be reduced in any way, and you must use the new rolls.")
                    if wizlvl >= 6:
                        BondMutualSuffering = "once"
                        if wizlvl >= 14:
                            BondMutualSuffering = "twice"
                        player.classnotes.append("Bond of Mutual Suffering (see notes)")
                        player.notes.append(f"Bond of Mutual Suffering - When a creature you can see hits you with an attack, you can use your reaction to bind your vitality to the attacker and force them to share your pain. The attacker takes damage equal to the damage you took.\nThis feature cannot be used against constructs or undead. You can use this feature {BondMutualSuffering}. You must finish a short or long rest before you can use it again.")
                    if wizlvl >= 10:
                        player.classnotes.append("Glyph of Hemorrhaging (see notes)")
                        player.notes.append(f"Glyph of Hemorrhaging - When you damage a creature with a spell, you can choose to curse that creature for 1 minute. While cursed in this way, whenever the creature is hit by an attack, it takes an extra 1d6 necrotic damage. At the end of each of the creature's turns, it can make a Constitution saving throw against your spell save DC, or against {player.spellsavedc[i]}, ending the curse on a success.\nThis feature cannot be used against creatures that are undead or constructs. Once you use this feature, you can't use it again until you finish a short or long rest.")
                    if wizlvl >= 14:
                        player.classnotes.append("Thicker than Water (see notes)")
                        player.notes.append(f"Thicker than Water - The blood that flows through your veins is empowered with arcane vigor that mends wounds and helps preserve your life. Whenever a spell or magical effect causes you to regain hit points, you regain an additional number of hit points equal to your Proficiency Bonus, or {player.profbonus} hit points.\nIn addition, while you are concentrating on a spell, you have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks.")  
                if player.subclass[i] == "Chronurgy Magic Wizard":
                    ChronurgySpells = {
                        "Cantrip": "Sapping Sting",
                        "1st Level Spell": "Gift of Alacrity",
                        "2nd Level Spell": ["Fortune's Favor", "Wristpocket"],
                        "3rd Level Spell": "Pulse Wave",
                        "5th Level Spell": "Temporal Shunt",
                        "7th Level Spell": "Tether Essence",
                        "8th Level Spell": "Reality Break",
                        "9th Level Spell": "Time Ravage",
                    }
                    long_string = ", ".join(
                        f"{level} : {spells}"
                        if isinstance(spells, str)
                        else f"{level} : {', '.join(spells)}"
                        for level, spells in ChronurgySpells.items()
                        )
                    player.classnotes.append("Expanded Spell List (see notes)")
                    player.notes.append(f"Expanded Spell List - The School of Chronurgy Magic lets you choose from an expanded list of spells developed through the manipulation of dunamis. The following Dunamancy Spells are added to the wizard spell list for you: {long_string}")
                    player.classnotes.append("Chronal Shift (see notes)")
                    player.notes.append("Chronal Shift - You can magically exert limited control over the flow of time around a creature. As a reaction, after you or a creature you can see within 30 feet of you makes an attack roll, an ability check, or a saving throw, you can force the creature to reroll. You make this decision after you see whether the roll succeeds or fails. The target must use the result of the second roll.\nYou can use this ability twice, and you regain any expended uses when you finish a long rest.")
                    player.classnotes.append(f"Temporal Awareness - You can add your Intelligence modifier, or {player.IntMod}, to your initiative rolls.")
                    if wizlvl >= 6:
                        player.classnotes.append("Momentary Stasis (see notes)")
                        player.notes.append(f"Momentary Stasis - As an action, you can magically force a Large or smaller creature you can see within 60 feet of you to make a Constitution saving throw against your spell save DC, or against {player.spellsavedc[i]}. Unless the saving throw is a success, the creature is encased in a field of magical energy until the end of your next turn or until the creature takes any damage. While encased in this way, the creature is incapacitated and has a speed of 0.\nYou can use this feature a number of times equal to your Intelligence modifier, or {player.IntMod} times, a minimum of once. You regain all expended uses when you finish a long rest.")
                    if wizlvl >= 10:
                        player.classnotes.append("Arcane Abeyance (see notes)")
                        player.notes.append(f"Arcane Abeyance - When you cast a spell using a spell slot of 4th level or lower, you can condense the spell's magic into a mote. The spell is frozen in time at the moment of casting and held within a gray bead for 1 hour. This bead is a Tiny object with AC 15 and 1 hit point, and it is immune to poison and psychic damage. When the duration ends, or if the bead is destroyed, it vanishes in a flash of light, and the spell is lost.\nA creature holding the bead can use its action to release the spell within, whereupon the bead disappears. The spell uses your spell attack bonus and save DC, or {player.spellattackmod[i]} and {player.spellsavedc[i]}, respectively, and the spell treats the creature who released it as the caster for all other purposes.\nOnce you create a bead with this feature, you can't do so again until you finish a short or long rest.")
                    if wizlvl >= 14:
                        player.classnotes.append("Convergent Future (see notes)")
                        player.notes.append("Convergent Future - You can peer through possible futures and magically pull one of them into events around you, ensuring a particular outcome. When you or a creature you can see within 60 feet of you makes an attack roll, an ability check, or a saving throw, you can use your reaction to ignore the die roll and decide whether the number rolled is the minimum needed to succeed or one less than that number (your choice).\nWhen you use this feature, you gain one level of exhaustion. Only by finishing a long rest can you remove a level of exhaustion gained in this way")  
                if player.subclass[i] == "Conjuration Arcane Tradition Wizard":
                    player.classnotes.append("Conjuration Savant - Beginning when you select this school at 2nd level, the gold and time you must spend to copy a Conjuration spell into your spellbook is halved.")
                    player.classnotes.append("Minor Conjuration (see notes)")
                    player.notes.append("Minor Conjuration - You can use your action to conjure up an inanimate object in your hand or on the ground in an unoccupied space that you can see within 10 feet of you. This object can be no larger than 3 feet on a side and weigh no more than 10 pounds, and its form must be that of a nonmagical object that you have seen. The object is visibly magical, radiating dim light out to 5 feet.\nThe object disappears after 1 hour, when you use this feature again, or if it takes any damage.")
                    if wizlvl >= 6:
                        player.classnotes.append("Benign Transportation (see notes)")
                        player.notes.append("Benign Transportation - You can use your action to teleport up to 30 feet to an unoccupied space that you can see. Alternatively, you can choose a space within range that is occupied by a Small or Medium creature. If that creature is willing, you both teleport, swapping places.\nOnce you use this feature, you can't use it again until you finish a long rest or you cast a conjuration spell of 1st level or higher.")
                    if wizlvl >= 10:
                        player.classnotes.append("Focused Conjuration - While you are concentrating on a conjuration spell, your concentration can't be broken as a result of taking damage.")
                    if wizlvl >= 14:
                        player.classnotes.append("Durable Summons - Any creature that you summon or create with a conjuration spell has 30 temporary hit points.")
                if player.subclass[i] == "Divination Arcane Tradition Wizard":
                    player.classnotes.append("Divination Savant - The gold and time you must spend to copy a Divination spell into your spellbook is halved.")
                    player.classnotes.append("Portent (see notes)")
                    player.notes.append("Portent - Glimpses of the future begin to press in on your awareness. When you finish a long rest, roll two d20s and record the numbers rolled. You can replace any attack roll, saving throw, or ability check made by you or a creature that you can see with one of these foretelling rolls. You must choose to do so before the roll, and you can replace a roll in this way only once per turn.\nEach foretelling roll can be used only once. When you finish a long rest, you lose any unused foretelling rolls.")
                    if wizlvl >= 6:
                        player.classnotes.append("Expert Divination (see notes)")
                        player.notes.append("Expert Divination - Casting divination spells comes so easily to you that it expends only a fraction of your spellcasting efforts. When you cast a divination spell of 2nd level or higher using a spell slot, you regain one expended spell slot. The slot you regain must be of a level lower than the spell you cast and can't be higher than 5th level.")
                    if wizlvl >= 10:
                        player.classnotes.append("The Third Eye (see notes)")
                        player.notes.append("The Third Eye - You can use your action to increase your powers of perception. When you do so, choose one of the following benefits, which lasts until you are incapacitated or you take a short or long rest. You can't use the feature again until you finish a short or long rest.\nDarkvision - You gain darkvision out to a range of 60 feet.\nEthereal Sight - You can see into the Ethereal Plane within 60 feet of you.\nGreater Comprehension - You can read any language.\nSee Invisibility - You can see invisible creatures and objects within 10 feet of you that are within line of sight.")
                    if wizlvl >= 14:
                        player.classnotes.append("Greater Portent - The visions in your dreams intensify and paint a more accurate picture in your mind of what is to come. You roll three d20s for your Portent feature, rather than two.")
                if player.subclass[i] == "Enchantment Arcane Tradition Wizard":
                    player.classnotes.append("Enchantment Savant - The gold and time you must spend to copy a Enchantment spell into your spellbook is halved.")
                    player.classnotes.append("Hypnotic Gaze (see notes)")
                    player.notes.append(f"Hypnotic Gaze - Your soft words and enchanting gaze can magically enthrall another creature. As an action, choose one creature that you can see within 5 feet of you. If the target can see or hear you, it must succeed on a Wisdom saving throw against your wizard spell save DC, or against {player.spellsavedc[i]}, or be charmed by you until the end of your next turn. The charmed creature's speed drops to 0, and the creature is incapacitated and visibly dazed.\nOn subsequent turns, you can use your action to maintain this effect, extending its duration until the end of your next turn. However, the effect ends if you move more than 5 feet away from the creature, if the creature can neither see nor hear you, or if the creature takes damage.\nOnce the effect ends, or if the creature succeeds on its initial saving throw against this effect, you can't use this feature on that creature again until you finish a long rest.")
                    if wizlvl >= 6:
                        player.classnotes.append("Instinctive Charm (see notes)")
                        player.notes.append(f"Instinctive Charm - When a creature you can see within 30 feet of you makes an attack roll against you, you can use your reaction to divert the attack, provided that another creature is within the attack's range. The attacker must make a Wisdom saving throw against your wizard spell save DC, or against {player.spellsavedc[i]}. On a failed save, the attacker must target the creature that is closest to it, not including you or itself. If multiple creatures are closest, the attacker chooses which one to target.On a successful save, you can't use this feature on the attacker again until you finish a long rest.\nYou must choose to use this feature before knowing whether the attack hits or misses. Creatures that can't be charmed are immune to this effect.")
                    if wizlvl >= 10:
                        player.classnotes.append("Split Enchantment - When you cast an enchantment spell of 1st level or higher that targets only one creature, you can have it target a second creature.")
                    if wizlvl >= 14:
                        player.classnotes.append("Alter Memories (see notes)")
                        player.notes.append(f"Alter Memories - You gain the ability to make a creature unaware of your magical influence on it. When you cast an enchantment spell to charm one or more creatures, you can alter one creature's understanding so that it remains unaware of being charmed.\nAdditionally, once before the spell expires, you can use your action to try to make the chosen creature forget some of the time it spent charmed. The creature must succeed on an Intelligence saving throw against your wizard spell save DC, or against {player.spellsavedc[i]}, or lose a number of hours of its memories equal to {1+player.ChaMod} hours, minimum 1. You can make the creature forget less time, and the amount of time can't exceed the duration of your enchantment spell.")  
                if player.subclass[i] == "Evocation Arcane Tradition Wizard":
                    player.classnotes.append("Evocation Savant - The gold and time you must spend to copy a Evocation spell into your spellbook is halved.")
                    player.classnotes.append("Sculpt Spells (see notes)")
                    player.notes.append("Sculpt Spells - You can create pockets of relative safety within the effects of your evocation spells. When you cast an evocation spell that affects other creatures that you can see, you can choose a number of them equal to 1 + the spell's level. The chosen creatures automatically succeed on their saving throws against the spell, and they take no damage if they would normally take half damage on a successful save.")
                    if wizlvl >= 6:
                        player.classnotes.append("Potent Cantrip - Your damaging cantrips affect even creatures that avoid the brunt of the effect. When a creature succeeds on a saving throw against your cantrip, the creature takes half the cantrip's damage (if any) but suffers no additional effect from the cantrip.")
                    if wizlvl >= 10:
                        player.classnotes.append(f"Empowered Evocation - You can add your Intelligence modifier, or {player.IntMod}, minimum of +1, to the damage roll of any wizard evocation spell that you cast. The damage bonus applies to one damage roll of a spell, not multiple rolls.")
                    if wizlvl >= 14:
                        player.classnotes.append("Overchannel (see notes)")
                        player.notes.append("Overchannel - You can increase the power of your simpler spells. When you cast a wizard spell of 5th level or lower that deals damage and isn't a cantrip, you can deal maximum damage with that spell.\nThe first time you do so, you suffer no adverse effect. If you use this feature again before you finish a long rest, you take 2d12 necrotic damage for each level of the spell, immediately after you cast it. Each time you use this feature again before finishing a long rest, the necrotic damage per spell level increases by 1d12. This damage ignores resistance and immunity.")  
                if player.subclass[i] == "Graviturgy Magic Wizard":
                    GraviturgySpells = {
                        "Cantrip": "Sapping Sting",
                        "1st Level Spell": "Magnify Gravity",
                        "2nd Level Spell": ["Fortune's Favor", "Immovable Object", "Wristpocket"],
                        "3rd Level Spell": "Pulse Wave",
                        "4th Level Spell": "Gravity Sinkhole",
                        "6th Level Spell": "Gravity Fissure",
                        "7th Level Spell": "Tether Essence",
                        "8th Level Spell": "Dark Star",
                        "9th Level Spell": "Ravenous Void"
                    }
                    long_string = ", ".join(
                        f"{level} : {spells}"
                        if isinstance(spells, str)
                        else f"{level} : {', '.join(spells)}"
                        for level, spells in GraviturgySpells.items()
                    )                    
                    player.classnotes.append("Expanded Spell List (see notes)")
                    player.notes.append(f"Expanded Spell List - The School of Graviturgy Magic lets you choose from an expanded list of spells developed through the manipulation of dunamis. The following Dunamancy Spells are added to the wizard spell list for you: {long_string}")
                    AdjustDensity = "Large or Smaller"
                    if wizlvl >= 10:
                        AdjustDensity = "Huge of smaller"
                    player.classnotes.append("Adjust Density (see notes)")
                    player.notes.append(f"Adjust Density - As an action, you can magically alter the weight of one object or creature you can see within 30 feet of you. The object or creature must be {AdjustDensity}. The target's weight is halved or doubled for up to 1 minute or until your concentration ends (as if you were concentrating on a spell).\nWhile the weight of a creature is halved by this effect, the creature's speed increases by 10 feet, it can jump twice as far as normal, and it has disadvantage on Strength checks and Strength saving throws. While the weight of a creature is doubled by this effect, the creature's speed is reduced by 10 feet, and it has advantage on Strength checks and Strength saving throws.")
                    if wizlvl >= 6:
                        player.classnotes.append("Gravity Well - You've learned how to manipulate gravity around a living being: whenever you cast a spell on a creature, you can move the target 5 feet to an unoccupied space of your choice if the target is willing to move, the spell hits it with an attack, or it fails a saving throw against the spell.")
                    if wizlvl >= 10:
                        player.classnotes.append("Violent Attraction (see notes)")
                        player.notes.append(f"Violent Attraction - When another creature that you can see within 60 feet of you hits with a weapon attack, you can use your reaction to increase the attack's velocity, causing the attack's target to take an extra 1d10 damage of the weapon's type.\nAlternatively, if a creature within 60 feet of you takes damage from a fall, you can use your reaction to increase the fall's damage by 2d10.\nYou can use this feature a number of times equal to your Intelligence modifier, or {player.IntMod} times, a minimum of once. You regain all expended uses when you finish a long rest.")
                    if wizlvl >= 14:
                        player.classnotes.append("Event Horizon (see notes)")
                        player.notes.append(f"Event Horizon - As an action, you can magically emit a powerful field of gravitational energy that tugs at other creatures for up to 1 minute or until your concentration ends (as if you were concentrating on a spell). For the duration, whenever a creature hostile to you starts its turn within 30 feet of you, it must make a Strength saving throw against your spell save DC, or against {player.spellsavedc[i]}. On a failed save, it takes 2d10 force damage, and its speed is reduced to 0 until the start of its next turn. On a successful save, it takes half as much damage, and every foot it moves this turn costs 2 extra feet of movement.\nOnce you use this feature, you can't do so again until you finish a long rest or until you expend a spell slot of 3rd level or higher on it.")  
                if player.subclass[i] == "Illusion Arcane Tradition Wizard":
                    player.classnotes.append("Illusion Savant - The gold and time you must spend to copy a Illusion spell into your spellbook is halved.")
                    player.classnotes.append("Improved Minor Illusion (see notes)")
                    player.notes.append("Improved Minor Illusion - You learn the Minor Illusion cantrip. If you already know this cantrip, you learn a different wizard cantrip of your choice. The cantrip doesn't count against your number of cantrips known.\nWhen you cast Minor Illusion, you can create both a sound and an image with a single casting of the spell.")
                    if wizlvl >= 6:
                        player.classnotes.append("Malleable Illusions - When you cast an illusion spell that has a duration of 1 minute or longer, you can use your action to change the nature of that illusion (using the spell's normal parameters for the illusion), provided that you can see the illusion.")
                    if wizlvl >= 10:
                        player.classnotes.append("Illusory Self (see notes)")
                        player.notes.append("Illusory Self - You can create an illusory duplicate of yourself as an instant, almost instinctual reaction to danger. When a creature makes an attack roll against you, you can use your reaction to interpose the illusory duplicate between the attacker and yourself. The attack automatically misses you, then the illusion dissipates.\nOnce you use this feature, you can't use it again until you finish a short or long rest.")
                    if wizlvl >= 14:
                        player.classnotes.append("Illusory Reality (see notes)")
                        player.notes.append("Illusory Reality - You have learned the secret of weaving shadow magic into your illusions to give them a semi-reality. When you cast an illusion spell of 1st level or higher, you can choose one inanimate, nonmagical object that is part of the illusion and make that object real. You can do this on your turn as a bonus action while the spell is ongoing. The object remains real for 1 minute. For example, you can create an illusion of a bridge over a chasm and then make it real long enough for your allies to cross.\nThe object can't deal damage or otherwise directly harm anyone.")  
                if player.subclass[i] == "Necromancy Arcane Tradition Wizard":
                    player.classnotes.append("Necromancy Savant - The gold and time you must spend to copy a Necromancy spell into your spellbook is halved.")
                    player.classnotes.append("Grim Harvest (see notes)")
                    player.notes.append("Grim Harvest - You gain the ability to reap life energy from creatures you kill with your spells. Once per turn when you kill one or more creatures with a spell of 1st level or higher, you regain hit points equal to twice the spell's level, or three times its level if the spell belongs to the School of Necromancy. You don't gain this benefit for killing constructs or undead.")
                    if wizlvl >= 6:
                        player.classnotes.append("Undead Thralls (see notes)")
                        player.notes.append(f"Undead Thralls - You add the Animate Dead spell to your spellbook if it is not there already. When you cast Animate Dead, you can target one additional corpse or pile of bones, creating another zombie or skeleton, as appropriate.\nWhenever you create an undead using a necromancy spell, it has additional benefits:\n- The creature's hit point maximum is increased by an amount equal to your Wizard level, or hitpoint maximum of {wizlvl}.\n- The creature adds your Proficiency Bonus, or {player.profbonus}, to its weapon damage rolls.")
                    if wizlvl >= 10:
                        player.classnotes.append("Inured to Undeath - You have resistance to necrotic damage, and your hit point maximum can't be reduced. You have spent so much time dealing with undead and the forces that animate them that you have become inured to some of their worst effects.")
                    if wizlvl >= 14:
                        player.classnotes.append("Command Undead (see notes)")
                        player.notes.append(f"Command Undead - You can use magic to bring undead under your control, even those created by other wizards. As an action, you can choose one undead that you can see within 60 feet of you. That creature must make a Charisma saving throw against your wizard spell save DC, or against {player.spellsavedc[i]}. If it succeeds, you can't use this feature on it again. If it fails, it becomes friendly to you and obeys your commands until you use this feature again.\nIntelligent undead are harder to control in this way. If the target has an Intelligence of 8 or higher, it has advantage on the saving throw. If it fails the saving throw and has an Intelligence of 12 or higher, it can repeat the saving throw at the end of every hour until it succeeds and breaks free.")  
                if player.subclass[i] == "Order of Scribes Arcane Tradition Wizard":
                    player.classnotes.append("Wizardly Quill (see notes)")
                    player.notes.append("Wizardly Quill - As a bonus action, you can magically create a Tiny quill in your free hand. The magic quill has the following properties:\n- The quill doesn't require ink. When you write with it, it produces ink in a color of your choice on the writing surface.\n- The time you must spend to copy a spell into your spell book equals 2 minutes per spell level if you use the quill for the transcription.\n- You can erase anything you write with the quill if you wave the feather over the text as a bonus action, provided the text is within 5 feet of you.\nThis quill disappears if you create another one or if you die.")
                    player.classnotes.append("Awakened Spellbook (see notes)")
                    player.notes.append("Awakened Spellbook - Using specially prepared inks and ancient incantations passed down by your wizardly order, you have awakened an arcane sentience within your spellbook.\nWhile you are holding the book, it grants you the following benefits:\n- You can use the book as a spellcasting focus for your wizard spells.\n- When you cast a wizard spell with a spell slot, you can temporarily replace its damage type with a type that appears in another spell in your spellbook, which magically alters the spell's formula for this casting only. The latter spell must be of the same level as the spell slot you expend.\n- When you cast a wizard spell as a ritual, you can use the spell's normal casting time, rather than adding 10 minutes to it. Once you use this benefit, you can't do so again until you finish a long rest.\nIf necessary, you can replace the book over the course of a short rest by using your Wizardly Quill to write arcane sigils in a blank book or a magic spellbook to which you're attuned. At the end of the rest, your spellbook's consciousness is summoned into the new book, which the consciousness transforms into your spellbook, along with all its spells. If the previous book still existed somewhere, all the spells vanish from its pages.")
                    if wizlvl >= 6:
                        player.classnotes.append("Manifest Mind (see notes)")
                        player.notes.append(f"Manifest Mind - You can conjure forth the mind of your Awakened Spellbook. As a bonus action while the book is on your person, you can cause the mind to manifest as a Tiny spectral object, hovering in an unoccupied space of your choice within 60 feet of you. The spectral mind is intangible and doesn't occupy its space, and it sheds dim light in a 10-foot radius. It looks like a ghostly tome, a cascade of text, or a scholar from the past (your choice).\nWhile manifested, the spectral mind can hear and see, and it has darkvision with a range of 60 feet. The mind can telepathically share with you what it sees and hears (no action required).\nWhenever you cast a wizard spell on your turn, you can cast it as if you were in the spectral mind's space, instead of your own, using its senses. You can do so a number of times equal to your Proficiency Bonus per day, or {player.profbonus} times per day, and you regain all expended uses when you finish a long rest.\nAs a bonus action, you can cause the spectral mind to hover up to 30 feet to an unoccupied space that you or it can see. It can pass through creatures but not objects.\nThe spectral mind stops manifesting if it is ever more than 300 feet away from you, if someone casts Dispel Magic on it, if the Awakened Spellbook is destroyed, if you die, or if you dismiss the spectral mind as a bonus action.\nOnce you conjure the mind, you can't do so again until you finish a long rest, unless you expend a spell slot of any level to conjure it again.")
                    if wizlvl >= 10:
                        player.classnotes.append("Master Scrivener (see notes)")
                        player.notes.append("Master Scrivener - Whenever you finish a long rest, you can create one magic scroll by touching your Wizardly Quill to a blank piece of paper or parchment and causing one spell from your Awakened Spellbook to be copied onto the scroll. The spellbook must be within 5 feet of you when you make the scroll.\nThe chosen spell must be of 1st or 2nd level and must have a casting time of 1 action. Once in the scroll, the spell's power is enhanced, counting as one level higher than normal. You can cast the spell from the scroll by reading it as an action. The scroll is unintelligible to anyone else, and the spell vanishes from the scroll when you cast it or when you finish your next long rest.\nYou are also adept at crafting spell scrolls, which are described in the treasure chapter of the Dungeon Master's Guide. The gold and time you must spend to make such a scroll are halved if you use your Wizardly Quill.")
                    if wizlvl >= 14:
                        player.classnotes.append("One with the Word (see notes)")
                        player.notes.append("One with the Word - Your connection to your Awakened Spellbook has become so profound that your soul has become entwined with it. While the book is on your person, you have advantage on all Intelligence (Arcana) checks, as the spellbook helps you remember magical lore.\nMoreover, if you take damage while your spellbook's mind is manifested, you can prevent all of that damage to you by using your reaction to dismiss the spectral mind, using its magic to save yourself. Then roll 3d6. The spellbook temporarily loses spells of your choice that have a combined spell level equal to that roll or higher. For example, if the roll's total is 9, spells vanish from the book that have a combined level of at least 9, which could mean one 9th-level spell, three 3rd-level spells, or some other combination. If there aren't enough spells in the book to cover this cost, you drop to 0 hit points.\nUntil you finish 1d6 long rests, you are incapable of casting the lost spells, even if you find them on a scroll or in another spellbook. After you finish the required number of rests, the spells reappear in the spell book.\nOnce you use this reaction, you can't do so again until you finish a long rest.")
                if player.subclass[i] == "Transmutation Arcane Tradition Wizard":
                    player.classnotes.append("Transmutation Savant - The gold and time you must spend to copy a Transmutation spell into your spellbook is halved.")
                    player.classnotes.append("Minor Alchemy (see notes)")
                    player.notes.append("Minor Alchemy - You can temporarily alter the physical properties of one nonmagical object, changing it from one substance into another. You perform a special alchemical procedure on one object composed entirely of wood, stone (but not a gemstone), iron, copper, or silver, transforming it into a different one of those materials. For each 10 minutes you spend performing the procedure, you can transform up to 1 cubic foot of material. After 1 hour, or until you lose your concentration (as if you were concentrating on a spell), the material reverts to its original substance.")
                    if wizlvl >= 6:
                        player.classnotes.append("Transmuter's Stone (see notes)")
                        player.notes.append("Transmuter's Stone - You can spend 8 hours creating a transmuter's stone that stores transmutation magic. You can benefit from the stone yourself or give it to another creature. A creature gains a benefit of your choice as long as the stone is in the creature's possession. When you create the stone, choose the benefit from the following options:\n- Darkvision out to a range of 60 feet\n- An increase to speed of 10 feet while the creature is unencumbered\n- Proficiency in Constitution saving throws\n- Resistance to acid, cold, fire, lightning, or thunder damage (your choice whenever you choose this benefit)\nEach time you cast a transmutation spell of 1st level or higher, you can change the effect of your stone if the stone is on your person.\nIf you create a new transmuter's stone, the previous one ceases to function.")
                    if wizlvl >= 10:
                        player.classnotes.append("Shapechanger (see notes)")
                        player.notes.append("Shapechanger - You add the Polymorph spell to your spellbook, if it is not there already. You can cast Polymorph without expending a spell slot. When you do so, you can target only yourself and transform into a beast whose challenge rating is 1 or lower.\nOnce you cast Polymorph in this way, you can't do so again until you finish a short or long rest, though you can still cast it normally using an available spell slot.")
                    if wizlvl >= 14:
                        player.classnotes.append("Master Transmuter (see notes)")
                        player.notes.append("Master Transmuter - You can use your action to consume the reserve of transmutation magic stored within your transmuter's stone in a single burst. When you do so, choose one of the following effects. Your transmuter's stone is destroyed and can't be remade until you finish a long rest.\nMajor Transformation - You can transmute one nonmagical object – no larger than a 5-foot cube – into another nonmagical object of similar size and mass and of equal or lesser value. You must spend 10 minutes handling the object to transform it.\nPanacea - You remove all curses, diseases, and poisons affecting a creature that you touch with the transmuter's stone. The creature also regains all its hit points.\nRestore Life - You cast the Raise Dead spell on a creature you touch with the transmuter's stone, without expending a spell slot or needing to have the spell in your spellbook.\nRestore Youth - You touch the transmuter's stone to a willing creature, and that creature's apparent age is reduced by 3d10 years, to a minimum of 13 years. This effect doesn't extend the creature's lifespan.")                    
                if player.subclass[i] == "War Magic Arcane Tradition Wizard":
                    player.classnotes.append("Arcane Deflection (see notes)")
                    player.notes.append("Arcane Deflection - You have learned to weave your magic to fortify yourself against harm. When you are hit by an attack or you fail a saving throw, you can use your reaction to gain a +2 bonus to your AC against that attack or a +4 bonus to that saving throw.\nWhen you use this feature, you can’t cast spells other than cantrips until the end of your next turn.")
                    player.classnotes.append(f"Tactical Wit - Your keen ability to assess tactical situations allows you to act quickly in battle. You can give yourself a bonus to your initiative rolls equal to your Intelligence modifier, or bonus of {player.IntMod}.")
                    if wizlvl >= 6:
                        player.classnotes.append("Power Surge (see notes)")
                        player.notes.append(f"Power Surge - You can store magical energy within yourself to later empower your damaging spells.\nYou can store a maximum number of power surges equal to your Intelligence modifier, or {player.IntMod} power surges, minimum of one. Whenever you finish a long rest, your number of power surges resets to one. Whenever you successfully end a spell with Dispel Magic or Counterspell, you gain one power surge, as you steal magic from the spell you foiled. If you end a short rest with no power surges, you gain one power surge.\nOnce per turn when you deal damage to a creature or object with a wizard spell, you can spend one power surge to deal extra force damage to that target. The extra damage equals half your Wizard level, or {math.floor(wizlvl/2)} extra damage.")
                    if wizlvl >= 10:
                        player.classnotes.append("Durable Magic - The magic you channel helps ward off harm. While you maintain concentration on a spell, you have a +2 bonus to AC and all saving throws.")
                    if wizlvl >= 14:
                        player.classnotes.append(f"Deflecting Shroud - Your Arcane Deflection becomes infused with deadly magic. When you use your Arcane Deflection feature, you can cause magical energy to arc from you. Up to three creatures of your choice within 60 feet of you each take force damage equal to half your Wizard level, or {math.floor(wizlvl/2)} force damage.")
                WizardSpellSlot1 = 3
            if wizlvl >= 3:                    
                WizardSpellSlot1 = 4
                WizardSpellSlot2 = 2
                player.classnotes.append("Cantrip Formulas (see notes)")
                player.notes.append("Cantrip Formulas - You have scribed a set of arcane formulas in your spellbook that you can use to formulate a cantrip in your mind. Whenever you finish a long rest and consult those formulas in your spellbook, you can replace one wizard cantrip you know with another cantrip from the wizard spell list.")
            if wizlvl >= 4:
                WizardCantripsKnown = 4
                WizardSpellSlot2 = 3
            if wizlvl >= 5:
                WizardSpellSlot3 = 2
            if wizlvl >= 6:
                WizardSpellSlot3 = 3
            if wizlvl >= 7:
                WizardSpellSlot4 = 1
            if wizlvl >= 8:
                WizardSpellSlot4 = 2
            if wizlvl >= 9:
                WizardSpellSlot4 = 3
                WizardSpellSlot5 = 1
            if wizlvl >= 10:
                WizardCantripsKnown = 5
                WizardSpellSlot5 = 2
            if wizlvl >= 11:
                WizardSpellSlot6 = 1
            if wizlvl >= 13:
                WizardSpellSlot7 = 1
            if wizlvl >= 15:
                WizardSpellSlot8 = 1
            if wizlvl >= 17:
                WizardSpellSlot9 = 1
            if wizlvl >= 18:
                WizardSpellSlot5 = 3
                player.classnotes.append("Spell Mastery (see notes)")
                player.notes.append("Spell Mastery - You have achieved such mastery over certain spells that you can cast them at will. Choose a 1st-level wizard spell and a 2nd-level wizard spell that are in your spellbook. You can cast those spells at their lowest level without expending a spell slot when you have them prepared. If you want to cast either spell at a higher level, you must expend a spell slot as normal.\nBy spending 8 hours in study, you can exchange one or both of the spells you chose for different spells of the same levels.")
            if wizlvl >= 19:
                WizardSpellSlot6 = 2
            if wizlvl == 20:                    
                WizardSpellSlot7 = 2
                player.classnotes.append("Signature Spells (see notes)")
                player.notes.append("Signature Spells - You gain mastery over two powerful spells and can cast them with little effort. Choose two 3rd-level wizard spells in your spellbook as your signature spells. You always have these spells prepared, they don’t count against the number of spells you have prepared, and you can cast each of them once at 3rd level without expending a spell slot. When you do so, you can’t do so again until you finish a short or long rest.\nIf you want to cast either spell at a higher level, you must expend a spell slot as normal.")
            player.notes.append(f"You have {WizardCantripsKnown} cantrips available to you.")
            player.notes.append(f"The number of first level spell slots you have as a Wizard is: {WizardSpellSlot1}.")
            if WizardSpellSlot2 != 0:
                player.notes.append(f"The number of second level spell slots you have as a Wizard is: {WizardSpellSlot2}.")
            if WizardSpellSlot3 != 0:                
                player.notes.append(f"The number of third level spell slots you have as a Wizard is: {WizardSpellSlot3}.")
            if WizardSpellSlot4 != 0:
                player.notes.append(f"The number of fourth level spell slots you have as a Wizard is: {WizardSpellSlot4}.")
            if WizardSpellSlot5 != 0:
                player.notes.append(f"The number of fifth level spell slots you have as a Wizard is: {WizardSpellSlot5}.")
            if WizardSpellSlot6 != 0:
                player.notes.append(f"The number of sixth level spell slots you have as a Wizard is: {WizardSpellSlot6}.")
            if WizardSpellSlot7 != 0:
                player.notes.append(f"The number of seventh level spell slots you have as a Wizard is: {WizardSpellSlot7}.")
            if WizardSpellSlot8 != 0:
                player.notes.append(f"The number of eighth level spell slots you have as a Wizard is: {WizardSpellSlot8}.")
            if WizardSpellSlot9 != 0:
                player.notes.append(f"The number of ninth level spell slots you have as a Wizard is: {WizardSpellSlot9}.")

    ##after coding the feats list, do the skill/feat decision on the ability score increases, and one on.... at least variant human has it.
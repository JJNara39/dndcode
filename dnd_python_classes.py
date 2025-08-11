import random
import math
import dnd_bkg_gen
import dnd_bkg_race_sum
import dnd_class_expl
import dnd_class_gen
import dnd_race_gen
import dnd_tools
import dnd_spells
import dnd_update
from PyPDF2 import PdfReader, PdfWriter


def dice(dicenum):
    # Rolls a dice with dicenum sides
    result = random.randint(1, dicenum)
    return result

class Player:
    def __init__(self, name, plName, PlayerLevel): #The player would start out "blank"; this is your init class, what you start as
        self.name = name
        self.playername = plName
        self.level = PlayerLevel  
        self.multi = False
        self.nat1choice = False
        self.classlvl = []
        self.feattrait = {}     
        self.race = None
        self.size = None
        self.sharkinviciousbitedmg = None
        self.subrace = None
        self.color = None
        self.gem = None
        self.metal = None
        self.season = None
        self.lineage = None
        self.height = 0
        self.weight = 0
        self.type = None
        self.hollowone = False
        self.languages = []
        self.slang = list(dnd_tools.languages.keys())
        self.speed = {}
        self.resistances = []
        self.immunities = []
        self.conditions = []
        self.vulnerabilities = []
        self.condition_immunities = []
        self.notes = {}
        self.proficiencies = []
        self.skills = []
        self.ability_scores = {
            "STR": 0,
            "DEX": 0,
            "CON": 0,
            "INT": 0,
            "WIS": 0,
            "CHA": 0
        }    
        self.profbonus = math.ceil(self.level/4)+1
        self.armor_class = 10        
        self.player_class = None
        self.Class = []
        self.subclass = []
        self.singlemulticlass = "N"
        self.classnum = 1
        self.beachballflag = False
        self.curlup = False
        self.shiftershift = False
        self.armordon = False
        self.shield_equipped = False
        self.conscious = True
        self.background = None
        self.skills_dict = {
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
        self.Trait = None
        self.Ideal = None
        self.Bond = None
        self.Flaw = None
        self.platinum = 0
        self.gold = 0
        self.silver = 0
        self.electrum = 0
        self.copper = 0
        self.equipment = []        
        self.hitpoints = 0 
        self.firsthp = False
        self.hitpointsset = False
        self.adtlinfonotes = {}
        self.attacksspellcasting = {} 
        self.alliesorg = []
        self.hitdice = {}
        self.spelllist = {}
        self.spellcastingclass = []
        self.spellcastingability = []
        self.spellsavedc = {}
        self.spellattackmod = {}
        self.spellcastingfocus = None
        self.artlvl = 0
        self.artinfknown = 0
        self.artinfitems = 0
        self.artelixirs = 0
        self.artalcprof = False
        self.artarmprof = False
        self.artartprof = False
        self.artbattlesmithprof = False
        self.barblvl = 0
        self.barbrages = 0
        self.barbragedmg = 0
        self.barbbrutwep = 0
        self.barbpathbeastorigin = None
        self.barbssred = None
        self.barbwildmagic = None
        self.barbextraskill1 = False
        self.barbextraskill2 = False
        self.bardlvl = 0
        self.bardicinspiration = None
        self.bardsongrest = None
        self.bardperfcreation = None
        self.bardcgtemp = 0
        self.bardpsychicbladedmg = None
        self.clerlvl = 0
        self.clericarcanadomainspells = {}
        self.clericarcanebanishment = None
        self.clericblooddomainspells = {}
        self.clericdivinestrike = None
        self.clericcommunitydomainspells = {}
        self.clericdeathdomainspells = {}
        self.clericforgedomainspells = {}
        self.clericgravedomainspells = {}
        self.clericknowledgedomainspells = {}
        self.clericknowledgelanguages = False
        self.clericlifedomainspells = {}
        self.clericlightdomainspells = {}
        self.clericmoondomainspells = {}
        self.clericnaturedomainspells = {}
        self.clericnatureskl = False
        self.clericnightdomainspells = {}
        self.clericorderdomainspells = {}
        self.clericorderskl = False
        self.clericpeacedomainspells = {}
        self.clericpeaceskl = False
        self.clerictempestdomainspells = {}
        self.clerictrickerydomainspells = {}
        self.clerictwilightdomainspells = {}
        self.clericwardomainspells = {}
        self.clericchanneldivinity = 0
        self.clericdestroyundeadcr = None
        self.druidlvl = 0
        self.druidwildshapecr = None
        self.druidwildshapelimit = None
        self.druiddefilegrounddmg = None
        self.druidlandchoice = None
        self.druidcirclelandspells = {}
        self.druidcirclesporespells = {}
        self.druidhalosporesdmg = None
        self.druidstarmap = None
        self.druidcirclewildfirespells = {}
        self.figlvl = 0
        self.figactionsurge = None
        self.figextraatk = 0
        self.figindomitable = None
        self.figsuperioritydie = None
        self.figbattlemasterprof = False
        self.figsuperioritydievalue = None
        self.figcavskllang = False
        self.figpsionicenergydice = None
        self.figpurpdragkngtskl = False
        self.figruneamount = 0 
        self.figsamskllang = False
        self.figspirittemphp = 0
        self.figscoffskllang = False
        self.figblindsidedmg = None
        self.monklvl = 0
        self.monkmartialarts = None
        self.monkkipoints = 0
        self.monkunmov = 0
        self.monkascdragonorigin = None
        self.monkcobaltmonkskllang1 = False
        self.monkcobaltmonkskllang2 = False
        self.monkcobaltmonkskllang3 = False
        self.monkelementaldiscipline = 0
        self.monkspellki = 0
        self.monkkenseitl = False
        self.monkmercymask = None
        self.pallvl = 0
        self.palharnessdivinepower = 0
        self.paloathancspells = {}
        self.paloathconqspells = {}
        self.paloathcrownspells = {}
        self.paloathdevspells = {}
        self.paloathgloryspells = {}
        self.paloathseaspells = {}
        self.paloathredspells = {}
        self.paloathwatchspells = {}
        self.paloathvengspells = {}
        self.paloathoathbreakspells = {}
        self.ranlvl = 0
        self.randrakewardenorigin = None
        self.randrakewardenbreathdmg = None
        self.randwdreadfulstrikedmg = None
        self.ranfeywandererspells = {}
        self.ranfeywanderergift = None
        self.ranfeywandererskl = False
        self.rangloomstalkerspells = {}
        self.rangloomstalkerskl = False
        self.ranhorizonwalkerspells = {}
        self.ranplanarwarrdmg = None
        self.ranmonsterslayerspells = {}
        self.ranswarmchoice = None
        self.ranswarmkeeperspells = {}
        self.ranprimalawarepells = {}
        self.roglvl = 0
        self.rogassassinskl = False
        self.rogmastermindskl = False
        self.rogskpsionicdmg = None
        self.rogsnkatk = None
        self.sorclvl = 0
        self.sorcmetamagicabilities = 0
        self.sorcsorcerypoints = 0
        self.sorcabermindorigin = None
        self.sorcaberrantmindspells = {}
        self.sorcclockworksoulspells = {}
        self.sorcrunechildspells = {}
        self.sorclunarmagicspells = {}
        self.sorccwmanord = None
        self.sorcdivsoulaffinity = None
        self.sorcdracbloodcolor = None
        self.sorclunarmagicphase = None
        self.sorcglyphaegisdice = None
        self.sorcshadowchoice = None
        self.warlvl = 0
        self.warpatron = None
        self.wararchfeyspells = {}
        self.warcelestialspells = {}
        self.warfathomlessspells = {}
        self.wartentacledeepsdmg = None
        self.warguardiancoildmg = None
        self.warfiendspells = {}
        self.wargeniekind = None
        self.wargeniespells = {}
        self.wargenievessel = None
        self.wargreatoldonespells = {}
        self.warhexbladespells = {}
        self.warundeadspells = {}
        self.warundyingspells = {}
        self.wareldinv = 0
        self.warmysticarcanum = None
        self.wizlvl = 0
        self.wizbladesingwep = False
        self.wizbloodmagicbondms = None
        self.wizadjustdensity = None
        self.leveldiff = 0
        self.position = (0,0)
        self.actions = {}
        self.advantage = False
        self.disadvantage = False  
        self.grappling = []      
        self.has_swallowed = False
        self.swallowed_by = None    
        self.advantage_against = {}
        self.disadvantage_against = {}    
        self.reach = 5
        self.traits = {}
        self.team = None
        self.opportunity_attack_immune = False
        self.no_healing = False
        self.mainhand = None
        self.offhand = None
        self.disarmed_item = None
        self.disarmed = False
        self.dragonbornbreathdamagetype = None
        self.dragonbornbwdmg = None
        self.deathsave_success = 0
        self.deathsave_fail = 0
        self.dead = False
        


    def choose_race(self, param):
        dnd_race_gen.dndCharGenRace(param, self)
        print(f"Your race is {self.race}")

    def choose_class(self, param):
        dnd_class_gen.dndchargen_class(param, self)
        for cl in self.Class:
            print(f"Your class is: {cl}")

    def choose_bkg(self, param):
        dnd_bkg_gen.dndCharGenBkg(param, self)
        print(f"Your bkg is {self.background}")
    
    def class_explained(self, param):
        dnd_class_expl.dndchargen_characterbuilder(param, self)

    def update(self, param):
        self.ChaMod = math.floor((self.ability_scores["CHA"]-10)/2)
        self.ConMod = math.floor((self.ability_scores["CON"]-10)/2)
        self.DexMod = math.floor((self.ability_scores["DEX"]-10)/2)
        self.IntMod = math.floor((self.ability_scores["INT"]-10)/2)
        self.StrMod = math.floor((self.ability_scores["STR"]-10)/2)
        self.WisMod = math.floor((self.ability_scores["WIS"]-10)/2)        
        self.attacksspellcasting["Unarmed Strike Damage: Fist"] = { #There needs to be US: Damage, US: Grapple and US: Shove; in update! delete US: Damage and write a new one? Or can I replace the entire US: Damage, make sure to change the "Source" tag
            'Name' : "Unarmed Strike Damage: Fist",
            'Modifier': "STR",
            'Attack Type': 'Melee Weapon',
            'Damage Bonus' : self.StrMod,
            'Proficient': True,                
            'Damage' : "1",
            'Damage Type' : "Bludgeoning",                
        }        
        self.actions["Unarmed Strike Damage: Fist"] = self.attacksspellcasting["Unarmed Strike Damage: Fist"]        
        dnd_update.dnd_update(param, self)
        spellslots = {}
        for cl in self.Class:
            if cl == "Warlock":
                for note_key in self.notes:
                    if note_key.startswith(f"{cl} ") and "Spell Slots" in note_key:
                            spellslots[note_key] = self.notes[note_key]                
            else:
                for note_key in self.notes:
                    if note_key.startswith(f"{cl} ") and "Spell Slots Known" in note_key:
                            spellslots[note_key] = self.notes[note_key]
            #I may be able to recombine this if-else if classes like sorc, bard, etc have "Spell Slots Known" and no other note that says "Spell Slots" because I can do that Warlock-search for all classes
        #Save that full dictionary but also copy it
        self.spellslots_list = spellslots
        self.spellslots_list_editable = self.spellslots_list.copy()

        #Now the total and copy
        self.spellslots = sum(self.spellslots_list.values())
        self.spellslots_editable = self.spellslots

        self.currenthitpoints = self.hitpoints #This updates in combat function
        self.hitpointstemp = self.hitpoints
        self.initiative = self.DexMod #this will need some updating when Fears/Spells add to initiative
        for note_title, note in sorted(self.notes.items()):
            self.feattrait[note_title] = f"{note_title} - {note}"
        feattrait = []
        for note_title, note in sorted(self.feattrait.items()):
            if len(note) >= 100:
                feattrait.append(f"{note_title} (see notes)")
            else:
                feattrait.append(f"{note}")
        feat_trait_str = "\n".join(f'- {item}' for item in feattrait)
        allies_str = '\n'.join(f'- {item}' for item in self.alliesorg)
        classlevel_str = "/".join(f"{item}" for item in self.Class)
        EQP_string = "\n".join(
            f" - {item['Name']}" + 
            ("\n" + "\n".join(f" -- {content}" for content in item['Contents']) 
            if 'Contents' in item and isinstance(item['Contents'], list) else "")
            if isinstance(item, dict) and 'Name' in item 
            else f" - {item}"
            for item in self.equipment
        )
        ProfLang = self.proficiencies + self.languages
        prof_lang_str = '\n'.join(f'- {item}' for item in ProfLang) 
        SpellcastingClass_str = '/'.join(f"{item}" for item in self.spellcastingclass) #Commenting the 4 spell lines for now, they will go in a different function that gets constantly updated
        SpellcastingAbility_str = '/'.join(f"{item}" for item in self.spellcastingability)
        SpellsaveDC_str = '/'.join(f"{item}" for item in self.spellsavedc)
        SpellAttackMod_str = '/'.join(f"{item}" for item in self.spellattackmod)
        subclass_str = "\n".join(f"- {item}" for item in self.subclass)
        feat_trait_str = 'Subclass:' + '\n' + f'{subclass_str}' + '\n' + feat_trait_str    
        hitdie = list(self.hitdice.values())
        Hitdice_Str = ', '.join(f"{item}" for item in hitdie)
        Currenthitdice_str = ', '.join(f"{item}" for item in hitdie) #This is update in the combat function     
        self.data = {
            'ClassLevel':classlevel_str + ' ' + str(self.level),
            'Background':self.background,
            'PlayerName':self.playername,
            'CharacterName':self.name,
            'CharacterName 2':self.name,
            'Race ':(self.subrace if self.subrace is not None else self.race),
            'STR':str(self.ability_scores["STR"]),
            'ProfBonus':str(self.profbonus),
            'AC':self.armor_class,
            'Initiative': str(self.DexMod),
            'Speed': str(self.speed) + "ft",
            'PersonalityTraits ':self.Trait,
            'STRmod':str(self.StrMod),
            'DEX':str(self.ability_scores["DEX"]),
            'Ideals':self.Ideal,
            'DEXmod ':str(self.DexMod),
            'Bonds':self.Bond,
            'CON':str(self.ability_scores["CON"]),
            'CONmod':str(self.ConMod),
            'Flaws':self.Flaw,
            'INT':str(self.ability_scores["INT"]),
            'INTmod':str(self.IntMod),        
            'WIS':str(self.ability_scores["WIS"]),        
            'WISmod':str(self.WisMod),
            'CHA':str(self.ability_scores["CHA"]),        
            'CHamod':str(self.ChaMod),
            'GP':str(self.gold),
            'Height':str(self.height) + ' inches',
            'Weight':str(self.weight) + ' pounds',
            'Allies':allies_str,
            'HPMax' : str(self.hitpoints),
            'HPCurrent' : str(self.currenthitpoints), #This is updated in the combat function
            'Equipment' : EQP_string,
            'ProficienciesLang' : prof_lang_str,
            'Features and Traits' : feat_trait_str,
            'Spellcasting Class 2' : SpellcastingClass_str,
            'SpellcastingAbility 2' : SpellcastingAbility_str,
            'SpellSaveDC  2' : SpellsaveDC_str,
            'SpellAtkBonus 2' : SpellAttackMod_str, #These 4 are saved for a future function
            'Check Box 11' : '/Yes' if dnd_tools.saving_throws["StrST"] in self.skills else '/No',
            'Check Box 18' : '/Yes' if dnd_tools.saving_throws["DexST"] in self.skills else '/No',
            'Check Box 19' : '/Yes' if dnd_tools.saving_throws["ConST"] in self.skills else '/No',
            'Check Box 20' : '/Yes' if dnd_tools.saving_throws["IntST"] in self.skills else '/No',
            'Check Box 21' : '/Yes' if dnd_tools.saving_throws["WisST"] in self.skills else '/No',
            'Check Box 22' : '/Yes' if dnd_tools.saving_throws["ChaST"] in self.skills else '/No',
            'ST Charisma' : str(self.ChaMod + (self.profbonus if dnd_tools.saving_throws["ChaST"] in self.skills else 0)),
            'ST Constitution' : str(self.ConMod + (self.profbonus if dnd_tools.saving_throws["ConST"] in self.skills else 0)),
            'ST Dexterity' : str(self.DexMod + (self.profbonus if dnd_tools.saving_throws["DexST"] in self.skills else 0)),
            'ST Intelligence' : str(self.IntMod + (self.profbonus if dnd_tools.saving_throws["IntST"] in self.skills else 0)),
            'ST Strength' : str(self.StrMod + (self.profbonus if dnd_tools.saving_throws["StrST"] in self.skills else 0)),
            'ST Wisdom' : str(self.WisMod + (self.profbonus if dnd_tools.saving_throws["WisST"] in self.skills else 0)),
            'HDTotal' : Hitdice_Str,
            'HD' : Currenthitdice_str,
            'Nature' : str(self.skills_dict["NatuNum"] + self.IntMod + (self.profbonus if 'Nature' in self.skills else 0)),
            'Performance' : str(self.skills_dict["PerfNum"] + self.ChaMod + (self.profbonus if 'Performance' in self.skills else 0)),
            'Medicine' : str(self.skills_dict["MediNum"] + self.WisMod + (self.profbonus if 'Medicine' in self.skills else 0)),
            'Religion' : str(self.skills_dict["ReliNum"] + self.IntMod + (self.profbonus if 'Religion' in self.skills else 0)),
            'Stealth ' : str(self.skills_dict["SteaNum"] + self.DexMod + (self.profbonus if 'Stealth' in self.skills else 0)),
            'Check Box 23' : '/Yes' if 'Acrobatics' in self.skills else '/No',
            'Check Box 24' : '/Yes' if 'Animal Handling' in self.skills else '/No',
            'Check Box 25' : '/Yes' if 'Arcana' in self.skills else '/No',
            'Check Box 26' : '/Yes' if 'Athletics' in self.skills else '/No',
            'Check Box 27' : '/Yes' if 'Deception' in self.skills else '/No',
            'Check Box 28' : '/Yes' if 'History' in self.skills else '/No',
            'Check Box 29' : '/Yes' if 'Insight' in self.skills else '/No',
            'Check Box 30' : '/Yes' if 'Intimidation' in self.skills else '/No',
            'Check Box 31' : '/Yes' if 'Investigation' in self.skills else '/No',
            'Check Box 32' : '/Yes' if 'Medicine' in self.skills else '/No',
            'Check Box 33' : '/Yes' if 'Nature' in self.skills else '/No',
            'Check Box 34' : '/Yes' if 'Perception' in self.skills else '/No',
            'Check Box 35' : '/Yes' if 'Performance' in self.skills else '/No',
            'Check Box 36' : '/Yes' if 'Persuasion' in self.skills else '/No',
            'Check Box 37' : '/Yes' if 'Religion' in self.skills else '/No',
            'Check Box 38' : '/Yes' if 'Sleight of Hand' in self.skills else '/No',
            'Check Box 39' : '/Yes' if 'Stealth' in self.skills else '/No',
            'Check Box 40' : '/Yes' if 'Survival' in self.skills else '/No',
            'Acrobatics' : str(self.skills_dict["AcroNum"] + self.DexMod + (self.profbonus if 'Acrobatics' in self.skills else 0)),
            'Animal' : str(self.skills_dict["AnHaNum"] + self.WisMod + (self.profbonus if 'Animal Handling' in self.skills else 0)),
            'Athletics' : str(self.skills_dict["AthlNum"] + self.StrMod + (self.profbonus if 'Athletics' in self.skills else 0)),
            'Deception ' : str(self.skills_dict["DeceNum"] + self.ChaMod + (self.profbonus if 'Deception' in self.skills else 0)),
            'History ' : str(self.skills_dict["HistNum"] + self.IntMod + (self.profbonus if 'History' in self.skills else 0)),
            'Insight' : str(self.skills_dict["InsiNum"] + self.WisMod + (self.profbonus if 'Insight' in self.skills else 0)),
            'Intimidation' : str(self.skills_dict["IntiNum"] + self.ChaMod + (self.profbonus if 'Intimidation' in self.skills else 0)),
            'Investigation ' : str(self.skills_dict["InveNum"] + self.IntMod + (self.profbonus if 'Investigation' in self.skills else 0)),
            'Arcana' : str(self.skills_dict["ArcaNum"] + self.IntMod + (self.profbonus if 'Arcana' in self.skills else 0)),
            'Perception ' : str(self.skills_dict["PercNum"] + self.WisMod + (self.profbonus if 'Perception' in self.skills else 0)),
            'Persuasion' : str(self.skills_dict["PersNum"] + self.ChaMod + (self.profbonus if 'Persuasion' in self.skills else 0)),
            'SleightofHand' : str(self.skills_dict["SloHNum"] + self.DexMod + (self.profbonus if 'Sleight of Hand' in self.skills else 0)),
            'Survival' : str(self.skills_dict["SurvNum"] + self.WisMod + (self.profbonus if 'Survival' in self.skills else 0)),
            'Passive' : str(10 + self.skills_dict["PercNum"] + self.WisMod + (self.profbonus if 'Perception' in self.skills else 0)),
            }  
        
    def post_spell_update(self):
        for item in self.equipment:
            if isinstance(item, dict) and "Damage" in item:
                copy_item = item.copy()
                modifier = copy_item.get("Modifier", "") #need to get the Modifier, so .get('Modifier')
                if modifier == "Finesse":
                    stat_mod = max(self.StrMod, self.DexMod)
                else:
                    stat_mod = math.floor((self.ability_scores[modifier]-10)/2)
                copy_item["Damage Bonus"] = stat_mod

                # Proficiency check: does Weapon Type match a listed proficiency?
                weapon_type = copy_item.get("Weapon Type", "")
                is_proficient = weapon_type in self.proficiencies
                prof_bonus = self.profbonus if is_proficient else 0
                copy_item["Proficient"] = is_proficient

                # Store into attack/spell list
                self.attacksspellcasting[copy_item["Name"]] = copy_item
               
        atksclist = sorted(self.attacksspellcasting.keys(), key = lambda k: self.attacksspellcasting[k].get('Damage Bonus', 0), reverse = True) #Sorts descending by modifier     
        #print(f"Right now, atkssclist looks like: {atksclist}") #debug
        atkscdict = {}
        for i, cl in enumerate(self.Class, 1):
            for atk in atksclist:  # Enumerate from 1   
                key = f"{atk} ({cl})"
                attack_data = self.attacksspellcasting[atk]  # Get attack details, atk is the key for attacksspellcasting
                #print(f"Attack Bonus for {key} before: {attack_data.get('Attack Bonus', None)}") #debug
                dmg_bonus = attack_data.get("Damage Bonus", 0) #get the damage bonus, store it in a variable, this is how we will use the :+ later
                attack_data["Attack Bonus"] = attack_data.get("Damage Bonus", 0) + (self.profbonus if attack_data.get("Proficient") == True else 0)
                #print(f"Attack Bonus for {key} after: {attack_data.get('Attack Bonus', None)}") #debug
                if attack_data.get("Original Name") in dnd_spells.spells:
                    spell_data = dnd_spells.spells[attack_data.get("Original Name")]
                    effect = spell_data.get("Effect", {})
                    scaling = effect.get("Scaling", {})
                    int_level_scaling = {int(k): v for k, v in scaling.items()}
                    max_level = max([k for k in int_level_scaling if k <= self.level], default=None)
                    #print(f"Spell Data is {spell_data}") #debug
                    if "Spell List" in spell_data and cl in spell_data["Spell List"]:
                        # Only assign this class if the spell belongs to it
                        #print(f"Spell Data is {spell_data}") #debug
                        if "Eldritch Blast" in spell_data['Name']:
                            damage = spell_data["Effect"]["Damage"]
                        else:
                            damage = spell_data["Effect"]["Scaling"].get(str(self.classlvl[i-1]), spell_data["Effect"]["Scaling"][1])
                        attack_data["Using Class"] = cl
                        damage_type_str = spell_data.get("Effect", {}).get("Damage Type", '')
                        damage_str = f"{damage} + {dmg_bonus:+} {damage_type_str}"
                elif atk == "Breath Weapon":
                    damage_str = f"{scaling[str(max_level)]} + {spell_data['Effect']['Damage Type']}"
                else:
                    #print(f"Attack Data is {attack_data}")
                    damage_str = f"{attack_data.get('Damage', 0)} + {dmg_bonus:+} {attack_data.get('Damage Type', '')}" #This is what Wpn{i} equates to
                if "Weapon Type" in attack_data.keys():
                    sb = attack_data.get("Spell Mod", 0)
                    print(f"Current class is {cl}")
                    if cl == "Sorcerer": #Supposed to be Druid, currently Sorcerer for testing                        
                        #print(f"Classes: {self.Class}") #debug
                        #print(f"Spell attack mods: {self.spellattackmod}") #debug
                        attack_data["Spell Mod"] = self.spellattackmod[f"{cl} Spell Attack Mod"]
                        #print(f"Spell Mod on the weapon is: {attack_data['Spell Mod']}") #debug


            #The wpn atkbonus is self.spellattackmodifier, not just the ability but also proficiency bonus, check the PHB
            #The wpn damage for spells should be... attack_data['Effect']['Scaling'][self.classlvl], and damage type should be attack_data['Effect']['Damage Type]

            for i, atk in enumerate(atksclist, 1):
                if i <= 3:
                    if i == 1:
                        self.data['Wpn Name'] = atk   
                        self.data[f'Wpn{i} AtkBonus'] = f"{dmg_bonus:+}"
                        self.data[f'Wpn{i} Damage'] = damage_str
                    elif i == 2:
                        self.data['Wpn Name 2'] = atk   
                        self.data[f'Wpn{i} AtkBonus '] = f"{dmg_bonus:+}"
                        self.data[f'Wpn{i} Damage '] = damage_str
                    elif i == 3:
                        self.data['Wpn Name 3'] = atk   
                        self.data[f'Wpn{i} AtkBonus  '] = f"{dmg_bonus:+}"
                        self.data[f'Wpn{i} Damage '] = damage_str                    
                else:
                    atkscdict[atk] = f"{atk} - {attack_data['Modifier']} - {damage_str}"
        # Convert remaining attacks into a string for the Attacks & Spellcasting section
        attacksspellcasting_str = "\n".join(atkscdict.values())
        self.data['AttacksSpellcasting'] = attacksspellcasting_str
        self.actions = self.attacksspellcasting

    def summation(self, param):
        ability_score_names = list(self.ability_scores.keys())
        n=0
        Sums = []
        run = True
        while run:
            Value1 = dice(6)
            Value2 = dice(6)
            Value3 = dice(6)
            Value4 = dice(6)
            value = (Value1, Value2, Value3, Value4)
            for v in value:
                if v == 1:
                    v = dice(6)
            Value = sorted(value)
            del Value[0]
            sum = 0
            for k in range(len(Value)):
                sum += Value[k]
            Sums.append(sum)
            n += 1
            if n >= 6:
                run = False    
        if param == "Y":
            for i, sum in enumerate(Sums, 1):
                print(f"Score {i} to apply: {sum}")  
            for _ in range(len(Sums)):
                if len(Sums) == 1:
                    last_score = Sums[0]
                    last_ability_score = ability_score_names[0]
                    self.ability_scores[last_ability_score] = last_score
                    break #This way it leaves the for loop and does not run the rest
                while True:
                    try:
                        print("0 - Random")
                        for jdx, asname in enumerate(ability_score_names, 1):
                            print(f"{jdx} - {asname}")
                        abil_score_choice = int(input(f"Which score would you like to apply {Sums[0]} to? "))
                        if abil_score_choice == 0:
                            rand_ab_sc = random.choice(ability_score_names)
                            sum_applied = Sums[0]
                            self.ability_scores[rand_ab_sc] = sum_applied
                            ability_score_names.remove(rand_ab_sc)
                            Sums.remove(sum_applied)
                            break
                        elif 1 <= abil_score_choice <= len(Sums):
                            picked_score = ability_score_names[abil_score_choice - 1]
                            number = Sums[0]
                            self.ability_scores[picked_score] = number
                            ability_score_names.remove(picked_score)
                            Sums.remove(number)
                            break
                        else:
                            print("Invalid choice, please choose a valid option.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
        if param == "N":
            for _ in range(len(Sums)):
                rand_ab_sc = random.choice(ability_score_names)
                sum_applied = random.choice(Sums)
                self.ability_scores[rand_ab_sc] = sum_applied
                ability_score_names.remove(rand_ab_sc)
                Sums.remove(sum_applied)
        self.ChaMod = math.floor((self.ability_scores["CHA"]-10)/2)
        self.ConMod = math.floor((self.ability_scores["CON"]-10)/2)
        self.DexMod = math.floor((self.ability_scores["DEX"]-10)/2)
        self.IntMod = math.floor((self.ability_scores["INT"]-10)/2)
        self.StrMod = math.floor((self.ability_scores["STR"]-10)/2)
        self.WisMod = math.floor((self.ability_scores["WIS"]-10)/2)  
        dnd_bkg_race_sum.summation(param, self)

    def create_sheet(self):
        input_pdf_path = 'DnD_5E_CharacterSheet_FormFillable.pdf'
        output_pdf_path = f'{self.name}_{self.playername}_level{self.level}_charsheet.pdf'        
        # Read input file
        with open(input_pdf_path, 'rb') as pdf_file:
            reader = PdfReader(pdf_file)
            writer = PdfWriter()

            # Loop through all the pages
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                writer.add_page(page)

                #Get form fields from that page
                fields = reader.get_fields()

                # If there are fields, fill them with field name
                if fields:
                    for key, value in self.data.items():
                        #Fill each field with name
                        writer.update_page_form_field_values(
                            writer.pages[page_num], {key: value}
                        )
            # Write the output pdf
            with open(output_pdf_path, 'wb') as output_pdf:
                writer.write(output_pdf)

    def write_notes(self):
        filename = f"{self.name}_{self.playername}_level{self.level}_notes.txt"
        with open(filename, "w") as file:
            file.write(f"{self.name}'s Notes\n")
            file.write("=" * (len(self.name)+8) + "\n\n") #Decorative Header
            for note_title, note in self.notes.items():
                file.write("-"+note_title + ": " + str(note)+"\n\n")                                  

    def take_damage(self, dmg, damage_type, announcer):
        if damage_type in self.resistances:
            dmg = dmg // 2
        elif damage_type in self.vulnerabilities:
            dmg *= 2
        elif damage_type in self.immunities:
            dmg = 0

        self.currenthitpoints -= dmg
        if self.currenthitpoints <= self.hitpoints // 2:
            if not any(cond.get("Name") == "Bloodied" for cond in self.conditions):
                condition_to_apply = {
                    "Name": "Bloodied",  
                }
                self.conditions.append(condition_to_apply)     
                print(f"{self.name} is bloodied!")         
        if self.currenthitpoints <= 0:
            self.conscious = False
            if not any(c.get("Name") == "Unconscious" for c in self.conditions):
                announcer.announce("knockout", name=self.name)
                condition_to_apply = {
                    "Name": "Unconscious",
                    "Target": self
                }
                self.conditions.append(condition_to_apply)  
            #why did I if-check unconscious? Because things can still hit you when you are down                   
    
''' Eventually this will be the class for when I want to create a list of monsters
class Monster:
    def __init__(self, data):
        self.name = data['Name']
        self.hp = data['HP']
        self.ac = data['AC']
        # and so on...

wolf = Monster(monsters['Wolf'])'''


'''
#Several Characters
players = {}
for i in range(1,101):
    character_name = f"Marik{i}"
    player_name = f"Nara{i}"
    players[character_name] = Player(name = character_name, plName= player_name)
    players[character_name].choose_race(param="N")
    players[character_name].choose_class(param="N")
    players[character_name].choose_bkg(param="N")
    players[character_name].choose_skills(param="N")
    players[character_name].summation(param="N")
    players[character_name].update()
    for attribute, value in players[character_name].data.items():
        if value not in [None, []]:  # Exclude None and empty lists
            print(f"{attribute}: {value}")
'''

class Monster:
    def __init__(self, monster_dict):
        self.name = monster_dict.get('Name', 'Unknown')
        self.size = monster_dict.get('Size', 'Medium')
        self.type = monster_dict.get('Type', 'Unknown')
        self.alignment = monster_dict.get('Alignment', 'Unaligned')
        self.armor_class = monster_dict.get('AC', 10)
        self.initiative = monster_dict.get("Initiative", 0) #This is meant to be a modifier
        self.hitpoints = monster_dict.get('HP', 1)
        self.hit_dice = monster_dict.get('Hit Dice', '1d4')
        self.speed = monster_dict.get('Speed', {})
        self.traits = monster_dict.get('Traits', {})
        self.position = (0,0)
        self.grappling = []
        self.has_swallowed = False
        self.swallowed_by = None
        self.reach = 5
        self.opportunity_attack_immune = False
        self.regainhp = True
        self.no_healing = False
        self.equipped_weapon = None
        self.disarmed_weapon = None
        self.disarmed = False        
        

        self.ability_scores = monster_dict.get("Ability Scores", {})
        
        self.StrMod = (self.ability_scores["STR"] - 10) // 2
        self.DexMod = (self.ability_scores["DEX"] - 10) // 2
        self.ConMod = (self.ability_scores["CON"] - 10) // 2
        self.IntMod = (self.ability_scores["INT"] - 10) // 2
        self.WisMod = (self.ability_scores["WIS"] - 10) // 2
        self.ChaMod = (self.ability_scores["CHA"] - 10) // 2
        self.saving_throws = {
            "STR ST": monster_dict.get('STR Save', 0),
            "DEX ST": monster_dict.get('DEX Save', 0),
            "CON ST": monster_dict.get('CON Save', 0),
            "INT ST": monster_dict.get('INT Save', 0),
            "WIS ST": monster_dict.get('WIS Save', 0),
            "CHA ST": monster_dict.get('CHA Save', 0)
        }
        self.skills = monster_dict.get("Skills", {})
        self.senses = monster_dict.get("Senses", {})
        self.languages = monster_dict.get("Languages", [])
        self.challenge = monster_dict.get('Challenge', 0)
        self.immunities = monster_dict.get('DamageImmunities', [])
        self.resistances = monster_dict.get('DamageResistances', [])
        self.vulnerabilities = monster_dict.get('DamageVulnerabilities', [])
        self.condition_immunities = monster_dict.get('ConditionImmunities', [])
        
        self.XP = monster_dict.get('XP', 0)
        self.actions = monster_dict.get('Actions', {})
        self.advantage = False
        self.disadvantage = False
        
        self.conditions = []
        self.currenthitpoints = self.hitpoints
        self.hitpointstemp = self.hitpoints

        self.advantage_against = {}
        self.disadvantage_against = {}      
        self.team = None 
        self.disarmed = False    


    def take_damage(self, dmg, damage_type, announcer):
        if damage_type in self.resistances:
            dmg = dmg // 2
        elif damage_type in self.vulnerabilities:
            dmg *= 2
        elif damage_type in self.immunities:
            dmg = 0

        self.currenthitpoints -= dmg
        if self.currenthitpoints <= self.hitpoints // 2:
            if not any(cond.get("Name") == "Bloodied" for cond in self.conditions):
                condition_to_apply = {
                    "Name": "Bloodied",  
                }
                self.conditions.append(condition_to_apply)     
                print(f"{self.name} is bloodied!")               
        if self.currenthitpoints <= 0:
            announcer.announce("death", name = self.name)  

class Team:
    def __init__(self, controller, members):
        self.controller = controller
        self.members = members
        self.name = f"{controller}'s Team"

class Announcer:
    def __init__(self):
        self.quotes = {
            "start_round": [
                "Round {round_num} begins!",
                "Time to see who takes the lead in Round {round_num}!",
            ],
            "critical_hit": [
                "A CRITICAL HIT! Absolute devastation!",
                "That one’s going in the highlight reel!",
            ],
            "critical_fail": [
                "OH NO! A NAT 1! A catastrophic failure!",
                "That attack flopped harder than a fish out of water!",
            ],
            "death_save_crit_fail": [
                "OH NO! A NAT 1 — that’s two death save fails for {name}!",
                "Disaster! {name} rolls a NAT 1 and is inches from death!",
                "The crowd gasps — {name} just suffered a critical failure!",
            ],
            "death_save_crit_success": [
                "WHAT?! {name} rolls a NAT 20 and springs back into action!",
                "From the brink! {name} is on their feet again!",
                "A miracle! {name} cheats death and jumps back in the fight!",
            ],            
            "death_save_fail": [
                "{name} fails another death save! The end may be near!",
                "Tick tock—{name} is clinging to life!",
            ],
            "death_save_success": [
                "{name} hangs on! The fight’s not over yet!",
                "A successful save! {name} refuses to go down!",
                "{name} clings to life with sheer willpower!",
                "The crowd roars — {name} is still in it!",
                "{name} cheats death for another round!",
            ],            
            "knockout": [
                "{name} goes down! The battlefield shrinks!",
                "And {name} is OUTTA HERE!",
            ],
            "victory": [
                "What an end! The battle is won!",
                "Triumph at last! What a wild ride!",
            ],
            "death": [
                "And that’s the end of the line for {name}… rest in pieces.",
                "{name} has fallen for good — no saving throws left to roll!",
                "The crowd falls silent… {name} is no more.",
                "That’s it! {name} has exited the realm of the living!",
                "{name} has been erased from the initiative order permanently!",
            ],   
            "stable": [
                "{name} is stable! No more death saves needed… for now.",
                "The bleeding stops — {name} clings to life!",
                "{name} is no longer at death’s door!",
                "Steady breathing… {name} will live to fight another day!",
                "The crisis passes — {name} is safe, but still down.",
            ],              
        }

    def announce(self, event_type, **kwargs):
        import random
        if event_type in self.quotes:
            line = random.choice(self.quotes[event_type])
            print(line.format(**kwargs))
        
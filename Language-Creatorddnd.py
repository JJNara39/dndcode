## Language-Creator ##

Aara = "Aarakocra"
Abys = "Abyssal"
Aqua = "Aquan"
Aura = "Auran"
Bird = "Birdfolk"
Cele = "Celestial"
Cerva = "Cervan"
Comm = "Common"
DpSp = "Deep Speech"
Drac = "Draconic"
Dwarvi = "Dwarvish"
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
SLANG = [Aara, Abys, Aqua, Aura, Bird, Cele, Cerva, Comm, DpSp, Drac, Dwarvi, Elvi, Gian, GithL, Gnom, Gobl, Grun, Hafl, Hedg, Infe, Jerb, Krau, Leon, Loxo, Mapa, Mino, Orc, Quo, Prim, Sylv, Unde, Veda, Vulp]

SLANGstr = [
    "Aara", "Abys", "Aqua", "Aura", "Bird", "Cele", "Cerva", "Comm", "DpSp", "Drac", "Dwarvi", "Elvi", "Gian", "GithL", "Gnom", "Gobl", "Grun", "Hafl", "Hedg", "Infe", "Jerb", "Leon", "Loxo", 
    "Mapa", "Mino", "Orc", "Quo", "Prim", "Sylv", "Unde", "Veda", "Vulp"
]
'''
print('pllang = None')
print('while not pllang:')
print('    pllang = int(input(Please pick a language from the above list: ))')
for i, lang in enumerate(languages, 1):
    for j, slang in enumerate(SLANG, 1):
        if i == j:
            print(f'    if pllang == {i}:')
            print(f'        if {slang} in PlLang:')
            print('            print("You know this language, please select a different one")')
            print('            pllang = None')
            print('        else:')
            print(f'            PlLang = PlLang + {slang}')
            print(f'            SLANG.remove({slang})')

#For 2 languages

print('pllang = None')
print('pllang2 = None')
print('while not pllang and not pllang2:')
print("    if pllang == None:")
print('        pllang = int(input("Please pick a language from the above list: "))')
print("    if pllang2 == None:")
print('        pllang2 = int(input("Please pick a second language from the above list: "))')
for i, lang in enumerate(languages, 1):
    for j, slang in enumerate(SLANG, 1):
        if i == j:
            print(f'    if pllang == {i}:')
            print(f'        if {slang} in PlLang:')
            print('            print("You know this language, please select a different one")')
            print('            pllang = None')
            print(f'    if pllang2 == {i}:')
            print(f'        if {slang} in PlLang:')
            print('            print("You know this language, please select a different one")')
            print('            pllang2 = None')            
            print('        else:')
            print(f'            PlLang = PlLang + {slang}')
'''
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
NavTools = "Navigator's Tools"
ThievKit = "Thieves' Tools" 
MusicalInstruments = [Bagpipes, Birdpipes, Drum, Dulcimer, Flute, Glaur, HndDrum, Horn, Longhorn, Lute, Lyre, PFlute, Shawm, Songhorn, Tantan, Thelarr, Viol, Wargong, Yarting, Zulkoon]
MusicalInstrumentsStr = ["Bagpipes", "Birdpipes", "Drum", "Dulcimer", "Flute", "Glaur", "HndDrum", "Horn", "Longhorn", "Lute", "Lyre",
                          "PFlute", "Shawm", "Songhorn", "Tantan", "Thelarr", "Viol", "Wargong", "Yarting", "Zulkoon"
                        ]

#for i, musin in enumerate(MusicalInstruments, 1):
#    print(f'print("{i} - {musin}")')
#print('urbmi1 = int(input("Choose a musical instrument you wish to be proficient in. "))')
#for i, musinstr in enumerate(MusicalInstrumentsStr, 1):
#    print(f'    if urbmi1 == {i}:')
#    print(f'        UrbBHProf1 = {musinstr}')
'''
DiceSet = "Dice Set"
DrgnChSet = "Dragonchess Set"
PlyCrdSet = "Playing Card Set"
ThrDgnASet = "Three-Dragon Ante Set"

GSMIstr = ["DiceSet", "DrgnChSet", "PlyCrdSet", "ThrDgnASet", "Bagpipes", "Birdpipes", "Drum", "Dulcimer", "Flute", "Glaur", "HndDrum", "Horn", "Longhorn", "Lute", "Lyre", "PFlute", "Shawm", "Songhorn", "Tantan", "Thelarr", "Viol", "Wargong", "Yarting", "Zulkoon"]
GSMI = [DiceSet, DrgnChSet, PlyCrdSet, ThrDgnASet, Bagpipes, Birdpipes, Drum, Dulcimer, Flute, Glaur, HndDrum, Horn, Longhorn, Lute, Lyre, PFlute, Shawm, Songhorn, Tantan, Thelarr, Viol, Wargong, Yarting, Zulkoon]

for i, gsmi in enumerate(GSMI, 1):
    for j, gsmistr in enumerate(GSMIstr, 1):
        if i == j:
            print(f'print("{i} - {gsmi}")')
            print(f'if {gsmistr} in PlProf:')
            print(f'    print("You are already proficient in: " + {gsmistr} + ", therefore this option is unavailable")')
print('gsmi = int(input("Choose a gaming set or musical instrument to be proficient in. "))')
print('while not gsmi:')
for i, gsmi in enumerate(GSMI, 1):
    for j, gsmistr in enumerate(GSMIstr, 1):
        if i == j:
            print(f'    if gsmi == {i}:')
            print(f'        if {gsmistr} in PlProf:')
            print(f'            print("You are proficient in: " + {gsmistr} + ", please select a different one.")')
            print('            badeprof = None')
            print("        else:")
            print(f'            PlProf = PlProf + " and " + {gsmistr}')
'''            
'''
for i, musi in enumerate(MusicalInstruments, 1):
    for j, musistr in enumerate(MusicalInstrumentsStr, 1):
        if i == j:
            print(f'print("{i} - {musi}")')
            print(f'if {musistr} in PlProf:')
            print(f'    print("You are already proficient in: " + {musistr} ", therefore this option is unavailable.")')
print('musi = int(input("Choose a musical instrument to be proficient in. "))')            
print('while not musi:')
for i, musi in enumerate(MusicalInstruments, 1):
    for j, musistr in enumerate(MusicalInstrumentsStr, 1):
        if i == j:
            print(f'    if musi == {i}:')
            print(f'        if {musistr} in PlProf:')
            print(f'            print("You are proficient in: " + {musistr} + ", please select a different one.")')
            print('            musi = None')
            print('        else:')
            print(f'            PlProf = PlProf + {musistr}')
'''
'''
MusicalInstrumentsThiev = [Bagpipes, Birdpipes, Drum, Dulcimer, Flute, Glaur, HndDrum, Horn, Longhorn, Lute, Lyre, PFlute,
                            Shawm, Songhorn, Tantan, Thelarr, Viol, Wargong, Yarting, Zulkoon, ThievKit
                        ]
MusicalInstrumentsThievStr = ["Bagpipes", "Birdpipes", "Drum", "Dulcimer", "Flute", "Glaur", "HndDrum", "Horn", "Longhorn", "Lute", "Lyre",
                          "PFlute", "Shawm", "Songhorn", "Tantan", "Thelarr", "Viol", "Wargong", "Yarting", "Zulkoon", "Thievkit"
                        ]

for i, musit in enumerate(MusicalInstrumentsThiev, 1):
    for j, musitstr in enumerate(MusicalInstrumentsThievStr, 1):
        if i == j:
            print(f'print("{i} - {musit}")')
            print(f'if {musitstr} in PlProf:')
            print(f'    print("You are already proficient in: " + {musitstr} ", therefore this option is unavailable.")')
print('musit = int(input("Choose a musical instrument to be proficient in. "))')            
print('while not musit:')
for i, musit in enumerate(MusicalInstrumentsThiev, 1):
    for j, musitstr in enumerate(MusicalInstrumentsThievStr, 1):
        if i == j:
            print(f'    if musit == {i}:')
            print(f'        if {musitstr} in PlProf:')
            print(f'            print("You are proficient in: " + {musitstr} + ", please select a different one.")')
            print('            musi = None')
            print('        else:')
            print(f'            PlProf = PlProf + {musitstr}')
'''
'''
#4-lang
lang1 = "lang1"
lang2 = "lang2"
lang3 = "lang3"
lang4 = "lang4"
fourlang = [lang1, lang2, lang3, lang4]
for i, lang in enumerate(fourlang, 1):
    print(f'print("{i} - {lang}")')
    print(f'if {lang} in PlLang:')
    print(f'    print("You already know: " + {lang} + ", therefore this option is unavailable.")')
print('flang = int(input("Please pick a language from the above list. "))')
print('while not lang4:')
for i, lang in enumerate(fourlang, 1):
    print(f'    if flang == {i}:')
    print(f'        if {lang} in PlLang:')
    print(f'            print("You know: " + {lang} + ", please select a different option.")')
    print('        else:')
    print(f'            PlLang = PlLang + {lang}')
    '''

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
ArtisanTools = [AlchSupp, BrewSupp, CallSupp, CarpTools, CartTools, CobbTools, CooksUten, GlasTools, JeweTools, LthrwrkTools, MasnTools, PaintSupp, PottTools, SmthTools, TinkTools, WeavTools, WdcrvTools]
ArtisanToolsStr = ["AlchSupp", "BrewSupp", "CallSupp", "CarpTools", "CartTools", "CobbTools", "CooksUten", "GlasTools", "JeweTools", "LthrwrkTools", "MasnTools", "PaintSupp", "PottTools", "SmthTools", "TinkTools", "WeavTools", "WdcrvTools"]
'''
for i, arttool in enumerate(ArtisanTools, 1):
    for j, arttoolstr in enumerate(ArtisanToolsStr, 1):
        if i == j:
            print(f'print("{i} - {arttool}")')
            print(f'if {arttoolstr} in PlProf:')
            print(f'    print("You are already proficient in: " + {arttoolstr} ", therefore this option is unavailable.")')
print('arttool = int(input("Choose a musical instrument to be proficient in. "))')            
print('while not arttool:')
for i, arttool in enumerate(ArtisanTools, 1):
    for j, arttoolstr in enumerate(ArtisanToolsStr, 1):
        if i == j:
            print(f'    if arttool == {i}:')
            print(f'        if {arttoolstr} in PlProf:')
            print(f'            print("You are proficient in: " + {arttoolstr} + ", please select a different one.")')
            print('            arttool = None')
            print('        else:')
            print(f'            PlProf = PlProf + {arttoolstr}')
            print(f'            ArtisanTools.remove({arttoolstr})')
'''
'''
DiceSet = "Dice Set"
DrgnChSet = "Dragonchess Set"
PlyCrdSet = "Playing Card Set"
ThrDgnASet = "Three-Dragon Ante Set"            
GamingSets = [DiceSet, DrgnChSet, PlyCrdSet, ThrDgnASet]
GamingSetsStr = ["DiceSet", "DrgnChSet", "PlyCrdSet", "ThrDgnASet"]
print('print("0 - Random")')
for i, gamset in enumerate(GamingSets, 1):
    for j, gamsetstr in enumerate(GamingSetsStr, 1):
        if i == j:
            print(f'print("{i} - {gamset}")')
            print(f'if {gamsetstr} in PlProf:')
            print(f'    print("You are already proficient in: " + {gamsetstr} ", therefore this option is unavailable.")')
print('gamset = int(input("Choose a musical instrument to be proficient in. "))')            
print('while not arttool:')
for i, gamset in enumerate(GamingSets, 1):
    for j, gamsetstr in enumerate(GamingSetsStr, 1):
        if i == j:
            print(f'    if gamset == {i}:')
            print(f'        if {gamsetstr} in PlProf:')
            print(f'            print("You are proficient in: " + {gamsetstr} + ", please select a different one.")')
            print('            gamset = None')
            print('        else:')
            print(f'            PlProf = PlProf + {gamsetstr}')
            print(f'            GamingSets.remove({gamsetstr})')
'''

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
ArtisanTools = [AlchSupp, BrewSupp, CallSupp, CarpTools, CartTools, CobbTools, CooksUten, GlasTools, JeweTools, LthrwrkTools, MasnTools, PaintSupp, PottTools, SmthTools, TinkTools, WeavTools, WdcrvTools]
ArtisanToolsStr = ["AlchSupp", "BrewSupp", "CallSupp", "CarpTools", "CartTools", "CobbTools", "CooksUten", "GlasTools", "JeweTools", "LthrwrkTools", "MasnTools", "PaintSupp", "PottTools", "SmthTools", "TinkTools", "WeavTools", "WdcrvTools"]
ArtTlNavTlSLANG = [AlchSupp, BrewSupp, CallSupp, CarpTools, CartTools, CobbTools, CooksUten, GlasTools, JeweTools, LthrwrkTools, MasnTools, PaintSupp, PottTools, SmthTools, TinkTools, WeavTools, WdcrvTools, NavTools, Aara, Abys, Aqua, Aura, Bird, Cele, Cerva, Comm, DpSp, Drac, Dwarvi, Elvi, Gian, GithL, Gnom, Gobl, Grun, Hafl, Hedg, Infe, Jerb, Krau, Leon, Loxo, Mapa, Mino, Orc, Quo, Prim, Sylv, Unde, Veda, Vulp]

ArtTlNavTlSLANGstr = [
    "AlchSupp", "BrewSupp", "CallSupp", "CarpTools", "CartTools", "CobbTools", "CooksUten", "GlasTools", "JeweTools", "LthrwrkTools",
    "MasnTools", "PaintSupp", "PottTools", "SmthTools", "TinkTools", "WeavTools", "WdcrvTools", "NavTools", "Aara", "Abys", "Aqua", "Aura",
    "Bird", "Cele", "Cerva", "Comm", "DpSp", "Drac", "Dwarvi", "Elvi", "Gian", "GithL", "Gnom", "Gobl", "Grun", "Hafl", "Hedg", "Infe", "Jerb",
    "Krau", "Leon", "Loxo", "Mapa", "Mino", "Orc", "Quo", "Prim", "Sylv", "Unde", "Veda", "Vulp"
]
'''
print('print("0 - Random")')
for i, arttlnavtlslang in enumerate(ArtTlNavTlSLANG, 1):
    for j, arttlnavtlslangstr in enumerate(ArtTlNavTlSLANGstr, 1):
        if i == j:
            print(f'print("{i} - {arttlnavtlslang}")')
            print(f'if {arttlnavtlslangstr} in PlProf:')
            print(f'    print("You are already proficient in: " + {arttlnavtlslangstr} ", therefore this option is unavailable.")')
print('arttlnavtlslang = int(input("Choose an instrument, navigation tools, or language to be proficient in. "))')            
print('while not arttlnavtlslang:')
for i, arttlnavtlslang in enumerate(ArtTlNavTlSLANG, 1):
    for j, arttlnavtlslangstr in enumerate(ArtTlNavTlSLANGstr, 1):
        if i == j:
            print(f'    if arttlnavtlslang == {i}:')
            print(f'        if {arttlnavtlslangstr} in PlProf:')
            print(f'            print("You are proficient in: " + {arttlnavtlslangstr} + ", please select a different one.")')
            print('            arttlnavtlslang = None')
            print('        else:')
            print(f'            PlProf = PlProf + {arttlnavtlslangstr}')

'''

'''
ExoticLang = [Abys, Cele, DpSp, Drac, Infe, Prim, Sylv, Unde]
ExoticLangstr = ["Abys", "Cele", "DpSp", "Drac", "Infe", "Prim", "Sylv", "Unde"]
print('print("0 - Random")')
for i, exoticlang in enumerate(ExoticLang, 1):
    for j, exoticlangstr in enumerate(ExoticLangstr, 1):
        if i == j:
            print(f'print("{i} - {exoticlang}")')
            print(f'if {exoticlangstr} in PlProf:')
            print(f'    print("You already know: " + {exoticlangstr} ", therefore this option is unavailable.")')
print('exoticlang = int(input("Choose an instrument, navigation tools, or language to be proficient in. "))')            
print('while not exoticlang:')
for i, exoticlang in enumerate(ExoticLang, 1):
    for j, exoticlangstr in enumerate(ExoticLangstr, 1):
        if i == j:
            print(f'    if exoticlang == {i}:')
            print(f'        if {exoticlangstr} in PlProf:')
            print(f'            print("You already know: " + {exoticlangstr} + ", please select a different one.")')
            print('            exoticlang = None')
            print('        else:')
            print(f'            PlProf = PlProf + {exoticlangstr}')
            print(f'            SLANG.remove({exoticlangstr})')
            
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
MIART = [Bagpipes, Birdpipes, Drum, Dulcimer, Flute, Glaur, HndDrum, Horn, Longhorn, Lute, Lyre, PFlute, Shawm, Songhorn, Tantan, Thelarr, Viol, Wargong, Yarting, Zulkoon, AlchSupp, BrewSupp, CallSupp, CarpTools, CartTools, CobbTools, CooksUten, GlasTools, JeweTools, LthrwrkTools, MasnTools, PaintSupp, PottTools, SmthTools, TinkTools, WeavTools, WdcrvTools]
MIARTstr = ["Bagpipes", "Birdpipes", "Drum", "Dulcimer", "Flute", "Glaur", "HndDrum", "Horn", "Longhorn", "Lute", "Lyre", "PFlute", "Shawm", "Songhorn", "Tantan", "Thelarr", "Viol", "Wargong", "Yarting", "Zulkoon", "AlchSupp", "BrewSupp", "CallSupp", "CarpTools", "CartTools", "CobbTools", "CooksUten", "GlasTools", "JeweTools", "LthrwrkTools", "MasnTools", "PaintSupp", "PottTools", "SmthTools", "TinkTools", "WeavTools", "WdcrvTools"]
for i, prof in enumerate(MIART, 1):
    print(f'print("{i} - {prof}")')
print('prof = int(input("Pick an artisan tool or musical instrument to be proficient in. "))')
for i, prof in enumerate(MIART, 1):
    for j, profstr in enumerate(MIARTstr, 1):
        if i == j:
            print(f'if prof == {i}:')
            print(f'    PlProf = PlPof + {profstr}')

Shark = ["Blue Sharkin", "Basking Sharkin", "Bull Sharkin", "Cookie Cutter Sharkin", "Goblin Sharkin", "Hammerhead Sharkin", "Leopard Sharkin", "Mako Sharkin", "Nurse Sharkin", "Thresher Sharkin", "Tiger Sharkin", "Whale Sharkin", "Great White Sharkin", "Cladoselache", "Cretoxyrhina", "Edestus", "Helicoprion", "Hybodus", "Megalodon", "Ptychodus", "Scapanorhynchus", "Stethacanthus", "Xenacanthus"]
for i, shark in enumerate(Shark, 1):
    print(f'if subrace == "{shark}":')
'''
Charisma = 0
Constitution = 0
Dexterity = 0
Intelligence = 0
Strength = 0
Wisdom = 0
MainSkills = [
    Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom
]
MainSkillsStr = [
    "Charisma", "Constitution", "Dexterity", "Intelligence", "Strength", "Wisdom"
]
MainSkillsF3Str = [
    "Charisma", "Constitution", "Dexterity"
]
'''
for i, mskillstr in enumerate(MainSkillsStr, 1):
    print(f'print({i} - {mskillstr})')
print('mskill = int(input("Choose a skill to increase by 2. "))')
print('mskill2 = int(input("Choose an additional skill (could be the same skill) to increase by 1. "))')
for i, mskillstr in enumerate(MainSkillsStr, 1):
    for j, mskillstr2 in enumerate(MainSkillsStr, 1):
        print(f'if mskill == {i}:')
        print(f'    {mskillstr} += 2')
        print(f'    if mskill2 == {j}:')
        print(f'        {mskillstr2} += 1')


for i, mskillstr1 in enumerate(MainSkillsF3Str, 1):
    for j, mskillstr2 in enumerate(MainSkillsStr, 1):
        for k, mskillstr3 in enumerate(MainSkillsStr, 1):
            print(f'if mskill3one1 == {i}:')
            print(f'    {mskillstr1} += 1')
            print(f'    if mskill3one2 == {j}:')
            print(f'        {mskillstr2} += 1')
            print(f'        if mskill3one3 == {k}:')
            print(f'            {mskillstr3} += 1')
                  
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
ArtisanTools = [AlchSupp, BrewSupp, CallSupp, CarpTools, CartTools, CobbTools, CooksUten, GlasTools, JeweTools, LthrwrkTools, MasnTools, PaintSupp, PottTools, SmthTools, TinkTools, WeavTools, WdcrvTools]
ArtisanToolsStr = ["AlchSupp", "BrewSupp", "CallSupp", "CarpTools", "CartTools", "CobbTools", "CooksUten", "GlasTools", "JeweTools", "LthrwrkTools", "MasnTools", "PaintSupp", "PottTools", "SmthTools", "TinkTools", "WeavTools", "WdcrvTools"]
ArtisanTools2Str = ["AlchSupp", "BrewSupp"]
for i, arttools in enumerate(ArtisanToolsStr, 1):
    print(f'print("{i} - {arttools})')
print('arttools1 = int(input("Choose a tool to be proficient in. "))')
print('arttools2 = int(input("Choose a second tool to be proficient in. "))')
for i, arttools in enumerate(ArtisanTools2Str, 1):
    for j, arttools2 in enumerate(ArtisanToolsStr, 1):
        print(f'if arttools == {i}:')
        print(f'    PlProf = PlProf + ", " + {arttools}')
        print(f'    if arttools2 == {j}:')
        print(f'        PlProf = PlProf + ", " + {arttools2}')


Skill = [
    "Acrobatics", "AnimalHandling", "Arcana", "Athletics", "Deception", "History", "Insight",
    "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance",
    "Persuasion", "Religion", "SleightofHand", "Stealth", "Survival"    
]

for i, skl in enumerate(Skill, 1):
    print(f'print("{i} - {skl}")')
print('sklprof1 = int(input("Choose a skill to be proficient in. "))')
print('sklprof2 = int(input("Choose a second skill to be proficient in. "))')
for i, skl in enumerate(Skill, 1):
    print(f'if sklprof1 == {i}:')
    print(f'    PlProf = PlProf + ", " + {skl}')
for i, skl in enumerate(Skill, 1):
    print(f'if sklprof2 == {i}:')
    print(f'    PlProf = PlProf + ", " + {skl}')

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
HeavyLongbow = "Heavy Longbow"
Net = "Net"
MartialWeapons = [
        Battleaxe, DoubleBladedScimitar, Flail, Glaive, Greataxe, Greatsword, Halberd, Lance, Longsword, Maul, Morningstar, Pike, Rapier, Scimitar,
        Shortsword, Trident, WarPick, Warhammer, Whip, Blowgun, Crossbow, HandCrossbow, HeavyLongbow, Net
    ]
MartialWeaponsStr = [
        "Battleaxe", "DoubleBladedScimitar", "Flail", "Glaive", "Greataxe", "Greatsword", "Halberd", "Lance", "Longsword", "Maul", "Morningstar", "Pike", "Rapier", "Scimitar",
        "Shortsword", "Trident", "WarPick", "Warhammer", "Whip", "Blowgun", "Crossbow", "HandCrossbow", "HeavyLongbow", "Net"
    ]
print('print("0 - Random")')
for i, MW in enumerate(MartialWeapons, 1):
    print(f'print("{i} - {MW}")')
print('martwep1 = int(input("Choose a Martial Weapon to be proficient with. "))')
print('martwep2 = int(input("Choose a second Martial Weapon to be proficient with. ))')
for i, MWStr in enumerate(MartialWeaponsStr, 1):
    print(f'if martwep1 == {i}:')
    print(f'    PlProf = PlProf + ", " + {MWStr}')
print("if martwep1 == 0:")
print('    PlProf = PlProf + ", " + MartWepRand1')
for i, MWStr in enumerate(MartialWeaponsStr, 1):
    print(f'if martwep2 == {i}:')
    print(f'    PlProf = PlProf + ", " + {MWStr}')
print("if martwep2 == 0:")
print('    PlProf = PlProf + ", " + MartWepRand2')
'''
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
ArtisanTools = ["AlchSupp", "BrewSupp", "CallSupp", "CarpTools", "CartTools", "CobbTools", "CooksUten", "GlasTools", "JeweTools", "LthrwrkTools", "MasnTools", "PaintSupp", "PottTools", "SmthTools", "TinkTools", "WeavTools", "WdcrvTools"]
for i, arttl in enumerate(ArtisanTools, 1):
    print(f'if arttools1 == {i}:')
    print(f'    PlProf.append({arttl})')
for i, arttl in enumerate(ArtisanTools, 1):
    print(f'if arttools2 == {i}:')
    print(f'    PlProf.append({arttl})')


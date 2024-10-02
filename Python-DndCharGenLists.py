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
DiceSet = "Dice Set"
DrgnChSet = "Dragonchess Set"
PlyCrdSet = "Playing Card Set"
ThrDgnASet = "Three-Dragon Ante Set"
GamingSets = [DiceSet, DrgnChSet, PlyCrdSet, ThrDgnASet]
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

Aara = " Aarakocra,"
Abys = " Abyssal,"
Aqua = " Aquan,"
Aura = " Auran,"
Bird = " Birdfolk,"
Cele = " Celestial,"
Cerva = " Cervan,"
Comm = " Common,"
Drac = " Draconic,"
Dwarvi = " Dwarvish,"
Elvi = " Elvish,"
Gian = " Giant,"
GithL = " Gith,"
Gnom = " Gnomish,"
Gobl = " Goblin,"
Grun = " Grung,"
Hafl = " Hafling,"
Hedg = " Hedge,"
Infe = " Infernal,"
Jerb = " Jerbeen,"
Leon = " Leonin,"
Loxo = " Loxodon,"
Mapa = " Mapach,"
Mino = " Minotaur,"
Orc = " Orc,"
Quo = " Quori,"
Prim = " Primordial,"
Sylv = " Sylvan,"
Unde = " Undercommon,"
Veda = " Vedalken,"
Vulp = " Vulpin,"

PlLang = []

        

        ## 2 languages
pllang = None
pllang2 = None
while not pllang and not pllang2:
    if pllang == None:
        pllang = int(input("Please pick a language from the above list: "))
    if pllang2 == None:
        pllang2 = int(input("Please pick a second language from the above list: "))
    if pllang == 1:
        if Aara in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 1:
        if Aara in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Aara
    if pllang == 2:
        if Abys in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 2:
        if Abys in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Abys
    if pllang == 3:
        if Aqua in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 3:
        if Aqua in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Aqua
    if pllang == 4:
        if Aura in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 4:
        if Aura in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Aura
    if pllang == 5:
        if Bird in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 5:
        if Bird in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Bird
    if pllang == 6:
        if Cele in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 6:
        if Cele in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Cele
    if pllang == 7:
        if Cerva in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 7:
        if Cerva in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Cerva
    if pllang == 8:
        if Comm in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 8:
        if Comm in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Comm
    if pllang == 9:
        if Drac in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 9:
        if Drac in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Drac
    if pllang == 10:
        if Dwarvi in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 10:
        if Dwarvi in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Dwarvi
    if pllang == 11:
        if Elvi in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 11:
        if Elvi in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Elvi
    if pllang == 12:
        if Gian in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 12:
        if Gian in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Gian
    if pllang == 13:
        if GithL in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 13:
        if GithL in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + GithL
    if pllang == 14:
        if Gnom in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 14:
        if Gnom in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Gnom
    if pllang == 15:
        if Gobl in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 15:
        if Gobl in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Gobl
    if pllang == 16:
        if Grun in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 16:
        if Grun in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Grun
    if pllang == 17:
        if Hafl in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 17:
        if Hafl in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Hafl
    if pllang == 18:
        if Hedg in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 18:
        if Hedg in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Hedg
    if pllang == 19:
        if Infe in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 19:
        if Infe in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Infe
    if pllang == 20:
        if Jerb in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 20:
        if Jerb in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Jerb
    if pllang == 21:
        if Leon in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 21:
        if Leon in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Leon
    if pllang == 22:
        if Loxo in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 22:
        if Loxo in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Loxo
    if pllang == 23:
        if Mapa in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 23:
        if Mapa in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Mapa
    if pllang == 24:
        if Mino in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 24:
        if Mino in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Mino
    if pllang == 25:
        if Orc in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 25:
        if Orc in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Orc
    if pllang == 26:
        if Quo in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 26:
        if Quo in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Quo
    if pllang == 27:
        if Prim in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 27:
        if Prim in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Prim
    if pllang == 28:
        if Sylv in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 28:
        if Sylv in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Sylv
    if pllang == 29:
        if Unde in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 29:
        if Unde in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Unde
    if pllang == 30:
        if Veda in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 30:
        if Veda in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Veda
    if pllang == 31:
        if Vulp in PlLang:
            print("You know this language, please select a different one")
            pllang = None
    if pllang2 == 31:
        if Vulp in PlLang:
            print("You know this language, please select a different one")
            pllang2 = None
        else:
            PlLang = PlLang + Vulp    
    if pllang == 0:
        PlRandLang = random.choice(SLANG)
        PlLang = PlLang + PlRandLang
        SLANG.remove(PlRandLang)
    if pllang2 == 0:
        PlRandLang2 = random.choice(SLANG)
        PlLang = PlLang + PlRandLang2
        SLANG.remove(PlRandLang2)
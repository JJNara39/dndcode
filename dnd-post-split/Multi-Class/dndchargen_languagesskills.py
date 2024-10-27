import random

def languagegen(param, PlLang, SLANG):
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
    Languages = [Aara, Abys, Aqua, Aura, Bird, Cele, Cerva, Comm, DpSp, Drac, Dwarvi, Elvi, Gian, GithL, Gnom, Gobl, Grun, Hafl, Hedg, Infe, Jerb, Krau, Leon, Loxo, Mapa, Mino, Orc, Quo, Prim, Sylv, Unde, Veda, Vulp]
    if param == "Y": 
        print("0 - Random")      
        print("1 - Aarakocra")
        if Aara in PlLang:
            print("You already know Aarakocra, therefore this option is unavailable")
        print("2 - Abyssal")
        if Abys in PlLang:
            print("You already know Abyssal, therefore this option is unavailable")
        print("3 - Aquan")
        if Aqua in PlLang:
            print("You already know Aquan, therefore this option is unavailable")
        print("4 - Auran")
        if Aura in PlLang:
            print("You already know Auran, therefore this option is unavailable")
        print("5 - Birdfolk")
        if Bird in PlLang:
            print("You already know Birdfolk, therefore this option is unavailable")
        print("6 - Celestial")
        if Cele in PlLang:
            print("You already know Celestial, therefore this option is unavailable")
        print("7 - Cervan")
        if Cerva in PlLang:
            print("You already know Cervan, therefore this option is unavailable")
        print("8 - Common")
        if Comm in PlLang:
            print("You already know Common, therefore this option is unavailable")
        print("9 - Deep Speech")
        if DpSp in PlLang:
            print("You already know Deep Speech, therefore this option is unavailable")            
        print("10 - Draconic")
        if Drac in PlLang:
            print("You already know Draconic, therefore this option is unavailable")
        print("11 - Dwarvish")
        if Dwarvi in PlLang:
            print("You already know Dwarvish, therefore this option is unavailable")
        print("12 - Elvish")
        if Elvi in PlLang:
            print("You already know Elvish, therefore this option is unavailable")
        print("13 - Giant")
        if Gian in PlLang:
            print("You already know Giant, therefore this option is unavailable")
        print("14 - Gith")
        if GithL in PlLang:
            print("You already know Gith, therefore this option is unavailable")
        print("15 - Gnomish")
        if Gnom in PlLang:
            print("You already know Gnomish, therefore this option is unavailable")
        print("16 - Goblin")
        if Gobl in PlLang:
            print("You already know Goblin, therefore this option is unavailable")
        print("17 - Grung")
        if Grun in PlLang:
            print("You already know Grung, therefore this option is unavailable")
        print("18 - Halfling")
        if Hafl in PlLang:
            print("You already know Halfling, therefore this option is unavailable")
        print("19 - Hedge")
        if Hedg in PlLang:
            print("You already know Hedge, therefore this option is unavailable")
        print("20 - Infernal")
        if Infe in PlLang:
            print("You already know Infernal, therefore this option is unavailable")
        print("21 - Jerbeen")
        if Jerb in PlLang:
            print("You already know Jerbeen, therefore this option is unavailable")
        print("22 - Kraul")
        if Krau in PlLang:
            print("You already know Kraul, therefore this option is unavailable")            
        print("23 - Leonin")
        if Leon in PlLang:
            print("You already know Leonin, therefore this option is unavailable")
        print("24 - Loxodon")
        if Loxo in PlLang:
            print("You already know Loxodon, therefore this option is unavailable")
        print("25 - Mapach")
        if Mapa in PlLang:
            print("You already know Mapach, therefore this option is unavailable")
        print("26 - Minotaur")
        if Mino in PlLang:
            print("You already know Minotaur, therefore this option is unavailable")
        print("27 - Orc")
        if Orc in PlLang:
            print("You already know Orc, therefore this option is unavailable")
        print("28 - Quori")
        if Quo in PlLang:
            print("You already know Quori, therefore this option is unavailable")
        print("29 - Primordial")
        if Prim in PlLang:
            print("You already know Primordial, therefore this option is unavailable")
        print("30 - Sylvan")
        if Sylv in PlLang:
            print("You already know Sylvan, therefore this option is unavailable")
        print("31 - Undercommon")
        if Unde in PlLang:
            print("You already know Undercommon, therefore this option is unavailable")
        print("32 - Vedalken")
        if Veda in PlLang:
            print("You already know Vedalken, therefore this option is unavailable")
        print("33 - Vulpin")
        if Vulp in PlLang:
            print("You already know Vulpin, therefore this option is unavailable")
        pllang = False
        pllang_input = int(input("Please pick a language from the above list: "))
        while not pllang:
            if pllang_input == 0:
                randLang = False
                while not randLang:
                    try:     
                        PlRandLang = random.choice(SLANG)
                        SLANG.remove(PlRandLang)           
                        PlLang.append(PlRandLang)
                        randLang = True
                    except ValueError:
                        pass
                    except IndexError:
                        break   
                pllang = True                 
            else:
                if Languages[pllang_input - 1] in PlLang:
                    print("You know: " + Languages[pllang_input - 1] + ", please select a different option.")
                else:
                    PlLang.append(Languages[pllang_input - 1])
                    SLANG.remove(Languages[pllang_input - 1])
                    pllang = True
    if param == "N":
        randLang = False
        while not randLang:
            try:     
                PlRandLang = random.choice(SLANG)
                SLANG.remove(PlRandLang)           
                PlLang.append(PlRandLang)
                randLang = True
            except ValueError:
                pass
            except IndexError:
                break      
    return PlLang, SLANG
def gamingsetsmusicalinstr(param, PlProf):
    DiceSet = "Dice Set"
    DrgnChSet = "Dragonchess Set"
    PlyCrdSet = "Playing Card Set"
    ThrDgnASet = "Three-Dragon Ante Set"
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
    GSMI = [DiceSet, DrgnChSet, PlyCrdSet, ThrDgnASet, Bagpipes, Birdpipes, Drum, Dulcimer, Flute, Glaur, HndDrum, Horn, Longhorn, Lute, Lyre, PFlute, Shawm, Songhorn, Tantan, Thelarr, Viol, Wargong, Yarting, Zulkoon]
    GSMIrand = random.choice(GSMI)
    if param == "Y":
        print("0 - Random")
        print("1 - Dice Set")
        print("2 - Dragonchess Set")
        print("3 - Playing Card Set")
        print("4 - Three-Dragon Ante Set")
        print("5 - Bagpipes")
        print("6 - Birdpipes")
        print("7 - Drum")
        print("8 - Dulcimer")
        print("9 - Flute")
        print("10 - Glaur")
        print("11 - Hand Drum")
        print("12 - Horn")
        print("13 - Longhorn")
        print("14 - Lute")
        print("15 - Lyre")
        print("16 - Pan Flute")
        print("17 - Shawm")
        print("18 - Songhorn")
        print("19 - Tantan")
        print("20 - Thelarr")
        print("21 - Viol")
        print("22 - Wargong")
        print("23 - Yarting")
        print("24 - Zulkoon")
        gsmi = int(input("Choose a gaming set or musical instrument to be proficient in. "))
        if gsmi == 1:
            PlProf.append(DiceSet)
        if gsmi == 2:
            PlProf.append(DrgnChSet)
        if gsmi == 3:
            PlProf.append(PlyCrdSet)
        if gsmi == 4:
            PlProf.append(ThrDgnASet)
        if gsmi == 5:
            PlProf.append(Bagpipes)
        if gsmi == 6:
            PlProf.append(Birdpipes)
        if gsmi == 7:
            PlProf.append(Drum)
        if gsmi == 8:
            PlProf.append(Dulcimer)
        if gsmi == 9:
            PlProf.append(Flute)
        if gsmi == 10:
            PlProf.append(Glaur)
        if gsmi == 11:
            PlProf.append(HndDrum)
        if gsmi == 12:
            PlProf.append(Horn)
        if gsmi == 13:
            PlProf.append(Longhorn)
        if gsmi == 14:
            PlProf.append(Lute)
        if gsmi == 15:
            PlProf.append(Lyre)
        if gsmi == 16:
            PlProf.append(PFlute)
        if gsmi == 17:
            PlProf.append(Shawm)
        if gsmi == 18:
            PlProf.append(Songhorn)
        if gsmi == 19:
            PlProf.append(Tantan)
        if gsmi == 20:
            PlProf.append(Thelarr)
        if gsmi == 21:
            PlProf.append(Viol)
        if gsmi == 22:
            PlProf.append(Wargong)
        if gsmi == 23:
            PlProf.append(Yarting)
        if gsmi == 24:
            PlProf.append(Zulkoon)
        if gsmi == 0:
            PlProf.append(GSMIrand)
    if param == "N":
        PlProf.append(GSMIrand)
    return PlProf
def gamingsetmusicalinstrthieves(param, PlProf):
    DiceSet = "Dice Set"
    DrgnChSet = "Dragonchess Set"
    PlyCrdSet = "Playing Card Set"
    ThrDgnASet = "Three-Dragon Ante Set"
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
    ThievKit = "Thieves' Tools"    
    GSMIT = [DiceSet, DrgnChSet, PlyCrdSet, ThrDgnASet, Bagpipes, Birdpipes, Drum, Dulcimer, Flute, Glaur, HndDrum, Horn, Longhorn, Lute, Lyre, PFlute, Shawm, Songhorn, Tantan, Thelarr, Viol, Wargong, Yarting, Zulkoon, ThievKit]
    GSMIT1rand = random.choice(GSMIT)
    if param == "Y":
        print("0 - Random")
        print("1 - Dice Set")
        print("2 - Dragonchess Set")
        print("3 - Playing Card Set")
        print("4 - Three-Dragon Ante Set")
        print("5 - Bagpipes")
        print("6 - Birdpipes")
        print("7 - Drum")
        print("8 - Dulcimer")
        print("9 - Flute")
        print("10 - Glaur")
        print("11 - Hand Drum")
        print("12 - Horn")
        print("13 - Longhorn")
        print("14 - Lute")
        print("15 - Lyre")
        print("16 - Pan Flute")
        print("17 - Shawm")
        print("18 - Songhorn")
        print("19 - Tantan")
        print("20 - Thelarr")
        print("21 - Viol")
        print("22 - Wargong")
        print("23 - Yarting")
        print("24 - Zulkoon")
        print("25 - Thieves' Tools")
        gsmit1 = int(input("Choose a tool to be proficient in. "))
        gsmit2 = int(input("Choose a second tool to be proficient in. "))
        if gsmit1 == 1:
            PlProf.append(DiceSet)
        if gsmit1 == 2:
            PlProf.append(DrgnChSet)
        if gsmit1 == 3:
            PlProf.append(PlyCrdSet)
        if gsmit1 == 4:
            PlProf.append(ThrDgnASet)
        if gsmit1 == 5:
            PlProf.append(Bagpipes)
        if gsmit1 == 6:
            PlProf.append(Birdpipes)
        if gsmit1 == 7:
            PlProf.append(Drum)
        if gsmit1 == 8:
            PlProf.append(Dulcimer)
        if gsmit1 == 9:
            PlProf.append(Flute)
        if gsmit1 == 10:
            PlProf.append(Glaur)
        if gsmit1 == 11:
            PlProf.append(HndDrum)
        if gsmit1 == 12:
            PlProf.append(Horn)
        if gsmit1 == 13:
            PlProf.append(Longhorn)
        if gsmit1 == 14:
            PlProf.append(Lute)
        if gsmit1 == 15:
            PlProf.append(Lyre)
        if gsmit1 == 16:
            PlProf.append(PFlute)
        if gsmit1 == 17:
            PlProf.append(Shawm)
        if gsmit1 == 18:
            PlProf.append(Songhorn)
        if gsmit1 == 19:
            PlProf.append(Tantan)
        if gsmit1 == 20:
            PlProf.append(Thelarr)
        if gsmit1 == 21:
            PlProf.append(Viol)
        if gsmit1 == 22:
            PlProf.append(Wargong)
        if gsmit1 == 23:
            PlProf.append(Yarting)
        if gsmit1 == 24:
            PlProf.append(Zulkoon)
        if gsmit1 == 25:
            PlProf.append(ThievKit)
        if gsmit1 == 0:
            PlProf.append(GSMIT1rand)
        if gsmit2 == 1:
            PlProf.append(DiceSet)
        if gsmit2 == 2:
            PlProf.append(DrgnChSet)
        if gsmit2 == 3:
            PlProf.append(PlyCrdSet)
        if gsmit2 == 4:
            PlProf.append(ThrDgnASet)
        if gsmit2 == 5:
            PlProf.append(Bagpipes)
        if gsmit2 == 6:
            PlProf.append(Birdpipes)
        if gsmit2 == 7:
            PlProf.append(Drum)
        if gsmit2 == 8:
            PlProf.append(Dulcimer)
        if gsmit2 == 9:
            PlProf.append(Flute)
        if gsmit2 == 10:
            PlProf.append(Glaur)
        if gsmit2 == 11:
            PlProf.append(HndDrum)
        if gsmit2 == 12:
            PlProf.append(Horn)
        if gsmit2 == 13:
            PlProf.append(Longhorn)
        if gsmit2 == 14:
            PlProf.append(Lute)
        if gsmit2 == 15:
            PlProf.append(Lyre)
        if gsmit2 == 16:
            PlProf.append(PFlute)
        if gsmit2 == 17:
            PlProf.append(Shawm)
        if gsmit2 == 18:
            PlProf.append(Songhorn)
        if gsmit2 == 19:
            PlProf.append(Tantan)
        if gsmit2 == 20:
            PlProf.append(Thelarr)
        if gsmit2 == 21:
            PlProf.append(Viol)
        if gsmit2 == 22:
            PlProf.append(Wargong)
        if gsmit2 == 23:
            PlProf.append(Yarting)
        if gsmit2 == 24:
            PlProf.append(Zulkoon)
        if gsmit2 == 25:
            PlProf.append(ThievKit)
        if gsmit2 == 0:
            GSMIT2rand = random.choice(GSMIT)
            PlProf.append(GSMIT2rand)
    if param == "N":
        PlProf.append(GSMIT1rand)  
        GSMIT2rand = random.choice(GSMIT)
        PlProf.append(GSMIT2rand)
    return PlProf
def musicalinstr(param, PlProf):
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
    MusicalInstrumentRand = random.choice(MusicalInstruments)     
    if param == "Y":
        print("0 - Random")
        print("1 - Bagpipes")
        print("2 - Birdpipes")
        print("3 - Drum")
        print("4 - Dulcimer")
        print("5 - Flute")
        print("6 - Glaur")
        print("7 - Hand Drum")
        print("8 - Horn")
        print("9 - Longhorn")
        print("10 - Lute")
        print("11 - Lyre")
        print("12 - Pan Flute")
        print("13 - Shawm")
        print("14 - Songhorn")
        print("15 - Tantan")
        print("16 - Thelarr")
        print("17 - Viol")
        print("18 - Wargong")
        print("19 - Yarting")
        print("20 - Zulkoon")
        musi = int(input("Choose a musical instrument to be proficient in. "))
        if musi == 1:
            PlProf.append(Bagpipes)
        if musi == 2:
            PlProf.append(Birdpipes)
        if musi == 3:
            PlProf.append(Drum)
        if musi == 4:
            PlProf.append(Dulcimer)
        if musi == 5:
            PlProf.append(Flute)
        if musi == 6:
            PlProf.append(Glaur)
        if musi == 7:
            PlProf.append(HndDrum)
        if musi == 8:
            PlProf.append(Horn)
        if musi == 9:
            PlProf.append(Longhorn)
        if musi == 10:
            PlProf.append(Lute)
        if musi == 11:
            PlProf.append(Lyre)
        if musi == 12:
            PlProf.append(PFlute)
        if musi == 13:
            PlProf.append(Shawm)
        if musi == 14:
            PlProf.append(Songhorn)
        if musi == 15:
            PlProf.append(Tantan)
        if musi == 16:
            PlProf.append(Thelarr)
        if musi == 17:
            PlProf.append(Viol)
        if musi == 18:
            PlProf.append(Wargong)
        if musi == 19:
            PlProf.append(Yarting)
        if musi == 20:
            PlProf.append(Zulkoon)
        if musi == 0:
            PlProf.append(MusicalInstrumentRand)
    if param == "N":    
        PlProf.append(MusicalInstrumentRand)
    return PlProf
def choicefourlang(param, PlLang, SLANG, lang1, lang2, lang3, lang4):
    FourLang = [lang1, lang2, lang3, lang4]
    if param == "Y":
        print("0 - Random")
        print(f"1 - {lang1}")
        if lang1 in PlLang:
            print("You already know: " + lang1 + ", therefore this option is unavailable.")
        print(f"2 - {lang2}")
        if lang2 in PlLang:
            print("You already know: " + lang2 + ", therefore this option is unavailable.")
        print(f"3 - {lang3}")
        if lang3 in PlLang:
            print("You already know: " + lang3 + ", therefore this option is unavailable.")
        print(f"4 - {lang4}")
        if lang4 in PlLang:
            print("You already know: " + lang4 + ", therefore this option is unavailable.")
        flang_input = int(input("Please pick a language from the above list. "))
        flang = False
        while not flang:
            if flang_input == 0:
                randflang = False
                while not randflang:
                    try:
                        fourlangrand = random.choice(FourLang)
                        SLANG.remove(fourlangrand)
                        PlLang.append(fourlangrand)
                        randflang = True
                    except ValueError:
                        pass
                    except IndexError:
                        break  
                flang = True
            else:
                if FourLang[flang_input - 1] in PlLang:
                    print("You know: " + FourLang[flang_input - 1] + ", please select a different option.")
                else:
                    PlLang.append(FourLang[flang_input - 1])
                    SLANG.remove(FourLang[flang_input - 1])
                    flang = True
    if param == "N":
        randflang = False
        while not randflang:
            try:
                fourlangrand = random.choice(SLANG)
                SLANG.remove(fourlangrand)
                PlLang.append(fourlangrand)
                randflang = True
            except ValueError:
                pass 
            except IndexError:
                break         
    return PlLang, SLANG   
def artisantools(param, PlProf):
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
    ArtisanToolsRand = random.choice(ArtisanTools)
    if param == "Y":
        print("0 - Random")
        print("1 - Alchemist's Supplies")
        print("2 - Brewer's Supplies")
        print("3 - Calligrapher's Supplies")
        print("4 - Carpenter's Tools")
        print("5 - Cartographer's Tools")
        print("6 - Cobbler's Tools")
        print("7 - Cook's Utensils")
        print("8 - Glassblower's Tools")
        print("9 - Jeweler's Tools")
        print("10 - Leatherworker's Tools")
        print("11 - Mason's Tools")
        print("12 - Painter's Supplies")
        print("13 - Potter's Tools")
        print("14 - Smith's Tools")
        print("15 - Tinker's Tools")
        print("16 - Weaver's Tools")
        print("17 - Woodcarver's Tools")
        arttool = int(input("Choose an artisan tool to be proficient in. "))
        if arttool == 1:
            PlProf.append(AlchSupp)
        if arttool == 2:
            PlProf.append(BrewSupp)
        if arttool == 3:
            PlProf.append(CallSupp)
        if arttool == 4:
            PlProf.append(CarpTools)
        if arttool == 5:
            PlProf.append(CartTools)
        if arttool == 6:
            PlProf.append(CobbTools)
        if arttool == 7:
            PlProf.append(CooksUten)
        if arttool == 8:
            PlProf.append(GlasTools)
        if arttool == 9:
            PlProf.append(JeweTools)
        if arttool == 10:
            PlProf.append(LthrwrkTools)
        if arttool == 11:
            PlProf.append(MasnTools)
        if arttool == 12:
            PlProf.append(PaintSupp)
        if arttool == 13:
            PlProf.append(PottTools)
        if arttool == 14:
            PlProf.append(SmthTools)
        if arttool == 15:
            PlProf.append(TinkTools)
        if arttool == 16:
            PlProf.append(WeavTools)
        if arttool == 17:
            PlProf.append(WdcrvTools)
        if arttool == 0:
            PlProf.append(ArtisanToolsRand)
    if param == "N":           
        PlProf.append(ArtisanToolsRand)
    return PlProf
def gamingsets(param, PlProf):
    DiceSet = "Dice Set"
    DrgnChSet = "Dragonchess Set"
    PlyCrdSet = "Playing Card Set"
    ThrDgnASet = "Three-Dragon Ante Set"            
    GamingSets = [DiceSet, DrgnChSet, PlyCrdSet, ThrDgnASet]
    GSrand = random.choice(GamingSets)
    if param == "Y":
        print("0 - Random")
        print("1 - Dice Set")
        print("2 - Dragonchess Set")
        print("3 - Playing Card Set")
        print("4 - Three-Dragon Ante Set")
        gamset = int(input("Choose a gaming set to be proficient in. "))
        if gamset == 1:
            PlProf.append(DiceSet)
        if gamset == 2:
            PlProf.append(DrgnChSet)
        if gamset == 3:
            PlProf.append(PlyCrdSet)
        if gamset == 4:
            PlProf.append(ThrDgnASet)
        if gamset == 0:
            PlProf.append(GSrand)
    if param == "N":
        PlProf.append(GSrand)
    return PlProf
def choicethreelang(param, PlLang, SLANG, lang1, lang2, lang3):
    ThreeLang = [lang1, lang2, lang3]
    if param == "Y":
        print("0 - Random")
        print(f"1 - {lang1}")
        if lang1 in PlLang:
            print("You already know: " + lang1 + ", therefore this option is unavailable.")
        print(f"2 - {lang2}")
        if lang2 in PlLang:
            print("You already know: " + lang2 + ", therefore this option is unavailable.")
        print(f"3 - {lang3}")
        if lang3 in PlLang:
            print("You already know: " + lang3 + ", therefore this option is unavailable.")
        tlang_input = int(input("Please pick a language from the above list. "))
        tlang = False
        while not tlang:
            if tlang_input == 0:
                randtlang = False
                while not randtlang:
                    try:
                        threelangrand = random.choice(ThreeLang)
                        SLANG.remove(threelangrand)
                        PlLang.append(threelangrand)
                        randtlang = True
                    except ValueError:
                        pass
                    except IndexError:
                        break
                tlang = True
            else: 
                if ThreeLang[tlang_input - 1] in PlLang:
                    print("You know: " + ThreeLang[tlang_input - 1] + ", please select a different option.")  
                else:
                    PlLang.append(ThreeLang[tlang_input - 1])
                    SLANG.remove(ThreeLang[tlang_input - 1])
                    tlang = True        
    if param == "N":
        randtlang = False
        while not randtlang:
            try:
                threelangrand = random.choice(ThreeLang)
                SLANG.remove(threelangrand)
                PlLang.append(threelangrand)
                randtlang = True
            except ValueError:
                pass
            except IndexError:
                break
    return PlLang, SLANG
def choicefourskill(param, skills_dict, skill1, skill2, skill3, skill4, skillname1, skillname2, skillname3, skillname4):
    FourSkill = [skill1, skill2, skill3, skill4]
    fourskillrand = random.randint(0, len(FourSkill) - 1)
    if param == "Y":
        print("0 - Random")
        print(f"1 - {skillname1}")
        print(f"2 - {skillname2}")
        print(f"3 - {skillname3}")
        print(f"4 - {skillname4}")
        fskl = int(input("Please pick a skill from the above list. "))
        if fskl == 0:
            skills_dict[FourSkill[fourskillrand]] += 1
        else:
            skills_dict[FourSkill[fskl - 1]] += 1
    if param == "N":
        skills_dict[FourSkill[fourskillrand]] += 1
    return [skills_dict[skill] for skill in FourSkill]
def choicethreeskill(param, skills_dict, skill1, skill2, skill3, skillname1, skillname2, skillname3):
    ThreeSkill = [skill1, skill2, skill3]
    threeskillrand = random.randint(0, len(ThreeSkill) - 1)
    if param == "Y":
        print("0 - Random")
        print(f"1 - {skillname1}")
        print(f"2 - {skillname2}")
        print(f"3 - {skillname3}")
        thrskl = int(input("Please pick a skill from the above list. "))
        if thrskl == 0:
            skills_dict[ThreeSkill[threeskillrand]] += 1
        else:
            skills_dict[ThreeSkill[thrskl - 1]] += 1
    if param == "N":
        skills_dict[ThreeSkill[threeskillrand]] += 1
    return [skills_dict[skill] for skill in ThreeSkill]
def choicethreeskill2(param, skills_dict, skill1, skill2, skill3, skillname1, skillname2, skillname3):
    ThreeSkill = [skill1, skill2, skill3]
    threeskillrand = random.randint(0, len(ThreeSkill) - 1)
    threeskillrand2 = random.randint(0, len(ThreeSkill) - 1)
    if param == "Y":
        print("0 - Random")
        print(f"1 - {skillname1}")
        print(f"2 - {skillname2}")
        print(f"3 - {skillname3}")
        thrskl = int(input("Please pick a skill from the above list. "))
        thrskl2 = int(input("Please pick a second skill from the above list. "))
        if thrskl == 0:
            skills_dict[ThreeSkill[threeskillrand]] += 1
        else:
            skills_dict[ThreeSkill[thrskl - 1]] += 1   

        if thrskl2 == 0:
            skills_dict[ThreeSkill[threeskillrand2]] += 1
        else:
            skills_dict[ThreeSkill[thrskl2 - 1]] += 1
    if param == "N":
        skills_dict[ThreeSkill[threeskillrand]] += 1    
        skills_dict[ThreeSkill[threeskillrand2]] += 1    
    return [skills_dict[skill] for skill in ThreeSkill]
def choicefourskill2(param, skills_dict, skill1, skill2, skill3, skill4, skillname1, skillname2, skillname3, skillname4):
    FourSkill = [skill1, skill2, skill3, skill4]
    fourskillrand = random.randint(0, len(FourSkill) - 1)
    fourskillrand2 = random.randint(0, len(FourSkill) - 1)
    if param == "Y":
        print("0 - Random")
        print(f"1 - {skillname1}")
        print(f"2 - {skillname2}")
        print(f"3 - {skillname3}")
        print(f"4 - {skillname4}")
        fskl = int(input("Please pick a skill from the above list. "))
        fskl2 = int(input("Please pick a second skill from the above list. "))
        if fskl == 0:
            skills_dict[FourSkill[fourskillrand]] += 1
        else:
            skills_dict[FourSkill[fskl - 1]] += 1    

        if fskl2 == 0:
            skills_dict[FourSkill[fourskillrand2]] += 1   
        else:
            skills_dict[FourSkill[fskl2 - 1]] += 1             
    if param == "N":
        skills_dict[FourSkill[fourskillrand]] += 1
        skills_dict[FourSkill[fourskillrand2]] += 1
    return [skills_dict[skill] for skill in FourSkill]
def musicalinstrthiev(param, PlProf):
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
    ThievKit = "Thieves' Tools"
    MusInstrThiev = [Bagpipes, Birdpipes, Drum, Dulcimer, Flute, Glaur, HndDrum, Horn, Longhorn, Lute, Lyre, PFlute, Shawm, Songhorn, Tantan, Thelarr, Viol, Wargong, Yarting, Zulkoon, ThievKit]
    MusInstrThievRand = random.choice(MusInstrThiev)
    if param == "Y":
        print("0 - Random")
        print("1 - Bagpipes")
        print("2 - Birdpipes")
        print("3 - Drum")
        print("4 - Dulcimer")
        print("5 - Flute")
        print("6 - Glaur")
        print("7 - Hand Drum")
        print("8 - Horn")
        print("9 - Longhorn")
        print("10 - Lute")
        print("11 - Lyre")
        print("12 - Pan Flute")
        print("13 - Shawm")
        print("14 - Songhorn")
        print("15 - Tantan")
        print("16 - Thelarr")
        print("17 - Viol")
        print("18 - Wargong")
        print("19 - Yarting")
        print("20 - Zulkoon")
        print("21 - Thieves' Tools")
        musit = int(input("Choose a musical instrument to be proficient in. "))
        if musit == 1:
            PlProf.append(Bagpipes)
        if musit == 2:
            PlProf.append(Birdpipes)
        if musit == 3:
            PlProf.append(Drum)
        if musit == 4:
            PlProf.append(Dulcimer)
        if musit == 5:
            PlProf.append(Flute)
        if musit == 6:
            PlProf.append(Glaur)
        if musit == 7:
            PlProf.append(HndDrum)
        if musit == 8:
            PlProf.append(Horn)
        if musit == 9:
            PlProf.append(Longhorn)
        if musit == 10:
            PlProf.append(Lute)
        if musit == 11:
            PlProf.append(Lyre)
        if musit == 12:
            PlProf.append(PFlute)
        if musit == 13:
            PlProf.append(Shawm)
        if musit == 14:
            PlProf.append(Songhorn)
        if musit == 15:
            PlProf.append(Tantan)
        if musit == 16:
            PlProf.append(Thelarr)
        if musit == 17:
            PlProf.append(Viol)
        if musit == 18:
            PlProf.append(Wargong)
        if musit == 19:
            PlProf.append(Yarting)
        if musit == 20:
            PlProf.append(Zulkoon)
        if musit == 21:
            PlProf.append(ThievKit)    
        if musit == 0:
            PlProf.append(MusInstrThievRand)
    if param == "N":
        PlProf.append(MusInstrThievRand)
    return PlProf
def ArtTlNavTlLang(param, PlProf, PlLang, SLANG):
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
    NavTools = "Navigator's Tools"
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
    ArtTlNavTlSLANG = [AlchSupp, BrewSupp, CallSupp, CarpTools, CartTools, CobbTools, CooksUten, GlasTools, JeweTools, LthrwrkTools, MasnTools, PaintSupp, PottTools, SmthTools, TinkTools, WeavTools, WdcrvTools, NavTools, Aara, Abys, Aqua, Aura, Bird, Cele, Cerva, Comm, DpSp, Drac, Dwarvi, Elvi, Gian, GithL, Gnom, Gobl, Grun, Hafl, Hedg, Infe, Jerb, Krau, Leon, Loxo, Mapa, Mino, Orc, Quo, Prim, Sylv, Unde, Veda, Vulp]
    ArtTlNavTlSLANGrand = random.choice(ArtTlNavTlSLANG)
    ArtTlNavTlSLANGlang = [Aara, Abys, Aqua, Aura, Bird, Cele, Cerva, Comm, DpSp, Drac, Dwarvi, Elvi, Gian, GithL, Gnom, Gobl, Grun, Hafl, Hedg, Infe, Jerb, Krau, Leon, Loxo, Mapa, Mino, Orc, Quo, Prim, Sylv, Unde, Veda, Vulp]
    if param == "Y":
        print("0 - Random")
        print("1 - Alchemist's Supplies")
        print("2 - Brewer's Supplies")
        print("3 - Calligrapher's Supplies")
        print("4 - Carpenter's Tools")
        print("5 - Cartographer's Tools")
        print("6 - Cobbler's Tools")
        print("7 - Cook's Utensils")
        print("8 - Glassblower's Tools")
        print("9 - Jeweler's Tools")
        print("10 - Leatherworker's Tools")
        print("11 - Mason's Tools")
        print("12 - Painter's Supplies")
        print("13 - Potter's Tools")
        print("14 - Smith's Tools")
        print("15 - Tinker's Tools")
        print("16 - Weaver's Tools")
        print("17 - Woodcarver's Tools")
        print("18 - Navigator's Tools")
        print("19 - Aarakocra")
        if Aara in PlLang:
            print("You already know: " + Aara + ", therefore this option is unavailable.")
        print("20 - Abyssal")
        if Abys in PlLang:
            print("You already know: " + Abys + ", therefore this option is unavailable.")
        print("21 - Aquan")
        if Aqua in PlLang:
            print("You already know: " + Aqua + ", therefore this option is unavailable.")
        print("22 - Auran")
        if Aura in PlLang:
            print("You already know: " + Aura + ", therefore this option is unavailable.")
        print("23 - Birdfolk")
        if Bird in PlLang:
            print("You already know: " + Bird + ", therefore this option is unavailable.")
        print("24 - Celestial")
        if Cele in PlLang:
            print("You already know: " + Cele + ", therefore this option is unavailable.")
        print("25 - Cervan")
        if Cerva in PlLang:
            print("You already know: " + Cerva + ", therefore this option is unavailable.")
        print("26 - Common")
        if Comm in PlLang:
            print("You already know: " + Comm + ", therefore this option is unavailable.")
        print("27 - Deep Speech")
        if DpSp in PlLang:
            print("You already know: " + DpSp + ", therefore this option is unavailable.")
        print("28 - Draconic")
        if Drac in PlLang:
            print("You already know: " + Drac + ", therefore this option is unavailable.")
        print("29 - Dwarvish")
        if Dwarvi in PlLang:
            print("You already know: " + Dwarvi + ", therefore this option is unavailable.")
        print("30 - Elvish")
        if Elvi in PlLang:
            print("You already know: " + Elvi + ", therefore this option is unavailable.")
        print("31 - Giant")
        if Gian in PlLang:
            print("You already know: " + Gian + ", therefore this option is unavailable.")
        print("32 - Gith")
        if GithL in PlLang:
            print("You already know: " + GithL + ", therefore this option is unavailable.")
        print("33 - Gnomish")
        if Gnom in PlLang:
            print("You already know: " + Gnom + ", therefore this option is unavailable.")
        print("34 - Goblin")
        if Gobl in PlLang:
            print("You already know: " + Gobl + ", therefore this option is unavailable.")
        print("35 - Grung")
        if Grun in PlLang:
            print("You already know: " + Grun + ", therefore this option is unavailable.")
        print("36 - Hafling")
        if Hafl in PlLang:
            print("You already know: " + Hafl + ", therefore this option is unavailable.")
        print("37 - Hedge")
        if Hedg in PlLang:
            print("You already know: " + Hedg + ", therefore this option is unavailable.")
        print("38 - Infernal")
        if Infe in PlLang:
            print("You already know: " + Infe + ", therefore this option is unavailable.")
        print("39 - Jerbeen")
        if Jerb in PlLang:
            print("You already know: " + Jerb + ", therefore this option is unavailable.")
        print("40 - Kraul")
        if Krau in PlLang:
            print("You already know: " + Krau + ", therefore this option is unavailable.")
        print("41 - Leonin")
        if Leon in PlLang:
            print("You already know: " + Leon + ", therefore this option is unavailable.")
        print("42 - Loxodon")
        if Loxo in PlLang:
            print("You already know: " + Loxo + ", therefore this option is unavailable.")
        print("43 - Mapach")
        if Mapa in PlLang:
            print("You already know: " + Mapa + ", therefore this option is unavailable.")
        print("44 - Minotaur")
        if Mino in PlLang:
            print("You already know: " + Mino + ", therefore this option is unavailable.")
        print("45 - Orc")
        if Orc in PlLang:
            print("You already know: " + Orc + ", therefore this option is unavailable.")
        print("46 - Quori")
        if Quo in PlLang:
            print("You already know: " + Quo + ", therefore this option is unavailable.")
        print("47 - Primordial")
        if Prim in PlLang:
            print("You already know: " + Prim + ", therefore this option is unavailable.")
        print("48 - Sylvan")
        if Sylv in PlLang:
            print("You already know: " + Sylv + ", therefore this option is unavailable.")
        print("49 - Undercommon")
        if Unde in PlLang:
            print("You already know: " + Unde + ", therefore this option is unavailable.")
        print("50 - Vedalken")
        if Veda in PlLang:
            print("You already know: " + Veda + ", therefore this option is unavailable.")
        print("51 - Vulpin")
        if Vulp in PlLang:
            print("You already know: " + Vulp + ", therefore this option is unavailable.")
        arttlnavtlslang = int(input("Choose an instrument, navigation tools, or language to be proficient in. "))
        while not arttlnavtlslang:
            if arttlnavtlslang == 1:
                PlProf.append(AlchSupp)
            if arttlnavtlslang == 2:
                PlProf.append(BrewSupp)
            if arttlnavtlslang == 3:
                PlProf.append(CallSupp)
            if arttlnavtlslang == 4:
                PlProf.append(CarpTools)
            if arttlnavtlslang == 5:
                PlProf.append(CartTools)
            if arttlnavtlslang == 6:
                PlProf.append(CobbTools)
            if arttlnavtlslang == 7:
                PlProf.append(CooksUten)
            if arttlnavtlslang == 8:
                PlProf.append(GlasTools)
            if arttlnavtlslang == 9:
                PlProf.append(JeweTools)
            if arttlnavtlslang == 10:
                PlProf.append(LthrwrkTools)
            if arttlnavtlslang == 11:
                PlProf.append(MasnTools)
            if arttlnavtlslang == 12:
                PlProf.append(PaintSupp)
            if arttlnavtlslang == 13:
                PlProf.append(PottTools)
            if arttlnavtlslang == 14:
                PlProf.append(SmthTools)
            if arttlnavtlslang == 15:
                PlProf.append(TinkTools)
            if arttlnavtlslang == 16:
                PlProf.append(WeavTools)
            if arttlnavtlslang == 17:
                PlProf.append(WdcrvTools)
            if arttlnavtlslang == 18:
                PlProf.append(NavTools)
            if arttlnavtlslang == 19:
                if Aara in PlLang:
                    print("You already know: " + Aara + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Aara)
                    SLANG.remove(Aara)
            if arttlnavtlslang == 20:
                if Abys in PlLang:
                    print("You already know: " + Abys + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Abys)
                    SLANG.remove(Abys)
            if arttlnavtlslang == 21:
                if Aqua in PlLang:
                    print("You already know: " + Aqua + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Aqua)
                    SLANG.remove(Aqua)
            if arttlnavtlslang == 22:
                if Aura in PlLang:
                    print("You already know: " + Aura + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Aura)
                    SLANG.remove(Aura)
            if arttlnavtlslang == 23:
                if Bird in PlLang:
                    print("You already know: " + Bird + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Bird)
                    SLANG.remove(Bird)
            if arttlnavtlslang == 24:
                if Cele in PlLang:
                    print("You already know: " + Cele + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Cele)
                    SLANG.remove(Cele)
            if arttlnavtlslang == 25:
                if Cerva in PlLang:
                    print("You already know: " + Cerva + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Cerva)
                    SLANG.remove(Cerva)
            if arttlnavtlslang == 26:
                if Comm in PlLang:
                    print("You already know: " + Comm + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Comm)
                    SLANG.remove(Comm)
            if arttlnavtlslang == 27:
                if DpSp in PlLang:
                    print("You already know: " + DpSp + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(DpSp)
                    SLANG.remove(DpSp)
            if arttlnavtlslang == 28:
                if Drac in PlLang:
                    print("You already know: " + Drac + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Drac)
                    SLANG.remove(Drac)
            if arttlnavtlslang == 29:
                if Dwarvi in PlLang:
                    print("You already know: " + Dwarvi + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Dwarvi)
                    SLANG.remove(Dwarvi)
            if arttlnavtlslang == 30:
                if Elvi in PlLang:
                    print("You already know: " + Elvi + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Elvi)
                    SLANG.remove(Elvi)
            if arttlnavtlslang == 31:
                if Gian in PlLang:
                    print("You already know: " + Gian + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Gian)
                    SLANG.remove(Gian)
            if arttlnavtlslang == 32:
                if GithL in PlLang:
                    print("You already know: " + GithL + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(GithL)
                    SLANG.remove(GithL)
            if arttlnavtlslang == 33:
                if Gnom in PlLang:
                    print("You already know: " + Gnom + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Gnom)
                    SLANG.remove(Gnom)
            if arttlnavtlslang == 34:
                if Gobl in PlLang:
                    print("You already know: " + Gobl + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Gobl)
                    SLANG.remove(Gobl)
            if arttlnavtlslang == 35:
                if Grun in PlLang:
                    print("You already know: " + Grun + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Grun)
                    SLANG.remove(Grun)
            if arttlnavtlslang == 36:
                if Hafl in PlLang:
                    print("You already know: " + Hafl + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Hafl)
                    SLANG.remove(Hafl)
            if arttlnavtlslang == 37:
                if Hedg in PlLang:
                    print("You already know: " + Hedg + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Hedg)
                    SLANG.remove(Hedg)
            if arttlnavtlslang == 38:
                if Infe in PlLang:
                    print("You already know: " + Infe + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Infe)
                    SLANG.remove(Infe)
            if arttlnavtlslang == 39:
                if Jerb in PlLang:
                    print("You already know: " + Jerb + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Jerb)
                    SLANG.remove(Jerb)
            if arttlnavtlslang == 40:
                if Krau in PlLang:
                    print("You already know: " + Krau + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Krau)
                    SLANG.remove(Krau)
            if arttlnavtlslang == 41:
                if Leon in PlLang:
                    print("You already know: " + Leon + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Leon)
                    SLANG.remove(Leon)
            if arttlnavtlslang == 42:
                if Loxo in PlLang:
                    print("You already know: " + Loxo + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Loxo)
                    SLANG.remove(Loxo)
            if arttlnavtlslang == 43:
                if Mapa in PlLang:
                    print("You already know: " + Mapa + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Mapa)
                    SLANG.remove(Mapa)
            if arttlnavtlslang == 44:
                if Mino in PlLang:
                    print("You already know: " + Mino + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Mino)
                    SLANG.remove(Mino)
            if arttlnavtlslang == 45:
                if Orc in PlLang:
                    print("You already know: " + Orc + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Orc)
                    SLANG.remove(Orc)
            if arttlnavtlslang == 46:
                if Quo in PlLang:
                    print("You already know: " + Quo + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Quo)
                    SLANG.remove(Quo)
            if arttlnavtlslang == 47:
                if Prim in PlLang:
                    print("You already know: " + Prim + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Prim)
                    SLANG.remove(Prim)
            if arttlnavtlslang == 48:
                if Sylv in PlLang:
                    print("You already know: " + Sylv + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Sylv)
                    SLANG.remove(Sylv)
            if arttlnavtlslang == 49:
                if Unde in PlLang:
                    print("You already know: " + Unde + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Unde)
                    SLANG.remove(Unde)
            if arttlnavtlslang == 50:
                if Veda in PlLang:
                    print("You already know: " + Veda + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Veda)
                    SLANG.remove(Veda)
            if arttlnavtlslang == 51:
                if Vulp in PlLang:
                    print("You already know: " + Vulp + ", please select a different option.")
                    arttlnavtlslang = None
                else:
                    PlLang.append(Vulp)
                    SLANG.remove(Vulp)
            if arttlnavtlslang == 0:
                if (ArtTlNavTlSLANGrand == AlchSupp) or (ArtTlNavTlSLANGrand == BrewSupp) or (ArtTlNavTlSLANGrand == CallSupp) or (ArtTlNavTlSLANGrand == CarpTools) or (ArtTlNavTlSLANGrand == CartTools) or (ArtTlNavTlSLANGrand == CobbTools) or (ArtTlNavTlSLANGrand == CooksUten) or (ArtTlNavTlSLANGrand == GlasTools) or (ArtTlNavTlSLANGrand == JeweTools) or (ArtTlNavTlSLANGrand == LthrwrkTools) or (ArtTlNavTlSLANGrand == MasnTools) or (ArtTlNavTlSLANGrand == PaintSupp) or (ArtTlNavTlSLANGrand == PottTools) or (ArtTlNavTlSLANGrand == SmthTools) or (ArtTlNavTlSLANGrand == TinkTools) or (ArtTlNavTlSLANGrand == WeavTools) or (ArtTlNavTlSLANGrand == WdcrvTools) or (ArtTlNavTlSLANGrand == NavTools):
                    PlProf.append(ArtTlNavTlSLANGrand)
                else:
                    arttlnavtlslangwhile = False
                    while not arttlnavtlslangwhile:
                        try:
                            ArtTlNavTlSLANGrand = random.choice(ArtTlNavTlSLANGlang)
                            PlLang.append(ArtTlNavTlSLANGrand)
                            SLANG.remove(ArtTlNavTlSLANGrand)
                            arttlnavtlslangwhile = True
                        except ValueError:
                            pass
                        except IndexError:
                            break                                 
    if param == "N":
        if (ArtTlNavTlSLANGrand == AlchSupp) or (ArtTlNavTlSLANGrand == BrewSupp) or (ArtTlNavTlSLANGrand == CallSupp) or (ArtTlNavTlSLANGrand == CarpTools) or (ArtTlNavTlSLANGrand == CartTools) or (ArtTlNavTlSLANGrand == CobbTools) or (ArtTlNavTlSLANGrand == CooksUten) or (ArtTlNavTlSLANGrand == GlasTools) or (ArtTlNavTlSLANGrand == JeweTools) or (ArtTlNavTlSLANGrand == LthrwrkTools) or (ArtTlNavTlSLANGrand == MasnTools) or (ArtTlNavTlSLANGrand == PaintSupp) or (ArtTlNavTlSLANGrand == PottTools) or (ArtTlNavTlSLANGrand == SmthTools) or (ArtTlNavTlSLANGrand == TinkTools) or (ArtTlNavTlSLANGrand == WeavTools) or (ArtTlNavTlSLANGrand == WdcrvTools) or (ArtTlNavTlSLANGrand == NavTools):
            PlProf.append(ArtTlNavTlSLANGrand)
        else:
            arttlnavtlslangwhile = False
            while not arttlnavtlslangwhile:
                try:
                    ArtTlNavTlSLANGrand = random.choice(ArtTlNavTlSLANGlang)
                    PlLang.append(ArtTlNavTlSLANGrand)
                    SLANG.remove(ArtTlNavTlSLANGrand)
                    arttlnavtlslangwhile = True  
                except ValueError:
                    pass
                except IndexError:
                    break         
    return PlProf, PlLang, SLANG      
def ExoticLang(param, PlLang, SLANG):
    Abys = "Abyssal"
    Cele = "Celestial"
    DpSp = "Deep Speech"
    Drac = "Draconic"
    Infe = "Infernal"
    Prim = "Primordial"
    Sylv = "Sylvan"
    Unde = "Undercommon"
    ExoticLang = [Abys, Cele, DpSp, Drac, Infe, Prim, Sylv, Unde]
    if param == "Y":
        print("0 - Random")
        print("1 - Abyssal")
        if Abys in PlLang:
            print("You already know: " + Abys + ", therefore this option is unavailable.")
        print("2 - Celestial")
        if Cele in PlLang:
            print("You already know: " + Cele + ", therefore this option is unavailable.")
        print("3 - Deep Speech")
        if DpSp in PlLang:
            print("You already know: " + DpSp + ", therefore this option is unavailable.")
        print("4 - Draconic")
        if Drac in PlLang:
            print("You already know: " + Drac + ", therefore this option is unavailable.")
        print("5 - Infernal")
        if Infe in PlLang:
            print("You already know: " + Infe + ", therefore this option is unavailable.")
        print("6 - Primordial")
        if Prim in PlLang:
            print("You already know: " + Prim + ", therefore this option is unavailable.")
        print("7 - Sylvan")
        if Sylv in PlLang:
            print("You already know: " + Sylv + ", therefore this option is unavailable.")
        print("8 - Undercommon")
        if Unde in PlLang:
            print("You already know: " + Unde + ", therefore this option is unavailable.")
        exoticlang_input = int(input("Please pick a language from the above list: "))
        exoticlang = False
        while not exoticlang:
            if exoticlang_input == 0:
                exoticlang_while = False
                while not exoticlang_while:
                    try:
                        ExoticLangRand = random.choice(ExoticLang)
                        PlLang.append(ExoticLangRand)
                        SLANG.remove(ExoticLangRand)
                        exoticlang_while = True
                    except ValueError:
                        pass
                    except IndexError:
                        break   
                exoticlang = True
            else:
                if ExoticLang[exoticlang_input - 1] in PlLang:
                     print("You already know: " + ExoticLang[exoticlang_input - 1] + ", please select a different one.")               
                else:
                    PlLang.append(ExoticLang[exoticlang_input - 1])
                    SLANG.remove(ExoticLang[exoticlang_input - 1])
                    exoticlang = True       
    if param == "N":
        exoticlang_while = False
        while not exoticlang_while:
            try:
                ExoticLangRand = random.choice(ExoticLang)
                PlLang.append(ExoticLangRand)
                SLANG.remove(ExoticLangRand)
                exoticlang_while = True
            except ValueError:
                pass
            except IndexError:
                break       
    return PlLang, SLANG
def musicalinstrdisg(param, PlProf):
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
    DisgKit = "Disguise Kit"
    MusInstrDisg = [Bagpipes, Birdpipes, Drum, Dulcimer, Flute, Glaur, HndDrum, Horn, Longhorn, Lute, Lyre, PFlute, Shawm, Songhorn, Tantan, Thelarr, Viol, Wargong, Yarting, Zulkoon, DisgKit]
    MusInstrDisgRand = random.choice(MusInstrDisg)
    if param == "Y":
        print("0 - Random")
        print("1 - Bagpipes")
        print("2 - Birdpipes")
        print("3 - Drum")
        print("4 - Dulcimer")
        print("5 - Flute")
        print("6 - Glaur")
        print("7 - Hand Drum")
        print("8 - Horn")
        print("9 - Longhorn")
        print("10 - Lute")
        print("11 - Lyre")
        print("12 - Pan Flute")
        print("13 - Shawm")
        print("14 - Songhorn")
        print("15 - Tantan")
        print("16 - Thelarr")
        print("17 - Viol")
        print("18 - Wargong")
        print("19 - Yarting")
        print("20 - Zulkoon")
        print("21 - Disguise Kit")
        musid = int(input("Choose a musical instrument to be proficient in. "))
        if musid == 1:
            PlProf.append(Bagpipes)
        if musid == 2:
            PlProf.append(Birdpipes)
        if musid == 3:
            PlProf.append(Drum)
        if musid == 4:
            PlProf.append(Dulcimer)
        if musid == 5:
            PlProf.append(Flute)
        if musid == 6:
            PlProf.append(Glaur)
        if musid == 7:
            PlProf.append(HndDrum)
        if musid == 8:
            PlProf.append(Horn)
        if musid == 9:
            PlProf.append(Longhorn)
        if musid == 10:
            PlProf.append(Lute)
        if musid == 11:
            PlProf.append(Lyre)
        if musid == 12:
            PlProf.append(PFlute)
        if musid == 13:
            PlProf.append(Shawm)
        if musid == 14:
            PlProf.append(Songhorn)
        if musid == 15:
            PlProf.append(Tantan)
        if musid == 16:
            PlProf.append(Thelarr)
        if musid == 17:
            PlProf.append(Viol)
        if musid == 18:
            PlProf.append(Wargong)
        if musid == 19:
            PlProf.append(Yarting)
        if musid == 20:
            PlProf.append(Zulkoon)
        if musid == 21:
            PlProf.append(DisgKit)
        if musid == 0:
            PlProf.append(MusInstrDisgRand)
    if param == "N":
        PlProf.append(MusInstrDisgRand)
    return PlProf
def artisantoolsmusicalinstr(param, PlProf):
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
    MIART = [Bagpipes, Birdpipes, Drum, Dulcimer, Flute, Glaur, HndDrum, Horn, Longhorn, Lute, Lyre, PFlute, Shawm, Songhorn, Tantan, Thelarr, Viol, Wargong, Yarting, Zulkoon, AlchSupp, BrewSupp, CallSupp, CarpTools, CartTools, CobbTools, CooksUten, GlasTools, JeweTools, LthrwrkTools, MasnTools, PaintSupp, PottTools, SmthTools, TinkTools, WeavTools, WdcrvTools]
    MIARTrand = random.choice(MIART)
    if param == "Y":
        print("1 - Bagpipes")
        print("2 - Birdpipes")
        print("3 - Drum")
        print("4 - Dulcimer")
        print("5 - Flute")
        print("6 - Glaur")
        print("7 - Hand Drum")
        print("8 - Horn")
        print("9 - Longhorn")
        print("10 - Lute")
        print("11 - Lyre")
        print("12 - Pan Flute")
        print("13 - Shawm")
        print("14 - Songhorn")
        print("15 - Tantan")
        print("16 - Thelarr")
        print("17 - Viol")
        print("18 - Wargong")
        print("19 - Yarting")
        print("20 - Zulkoon")
        print("21 - Alchemist's Supplies")
        print("22 - Brewer's Supplies")
        print("23 - Calligrapher's Supplies")
        print("24 - Carpenter's Tools")
        print("25 - Cartographer's Tools")
        print("26 - Cobbler's Tools")
        print("27 - Cook's Utensils")
        print("28 - Glassblower's Tools")
        print("29 - Jeweler's Tools")
        print("30 - Leatherworker's Tools")
        print("31 - Mason's Tools")
        print("32 - Painter's Supplies")
        print("33 - Potter's Tools")
        print("34 - Smith's Tools")
        print("35 - Tinker's Tools")
        print("36 - Weaver's Tools")
        print("37 - Woodcarver's Tools")
        prof = int(input("Pick an artisan tool or musical instrument to be proficient in. "))
        if prof == 1:
            PlProf.append(Bagpipes)
        if prof == 2:
            PlProf.append(Birdpipes)
        if prof == 3:
            PlProf.append(Drum)
        if prof == 4:
            PlProf.append(Dulcimer)
        if prof == 5:
            PlProf.append(Flute)
        if prof == 6:
            PlProf.append(Glaur)
        if prof == 7:
            PlProf.append(HndDrum)
        if prof == 8:
            PlProf.append(Horn)
        if prof == 9:
            PlProf.append(Longhorn)
        if prof == 10:
            PlProf.append(Lute)
        if prof == 11:
            PlProf.append(Lyre)
        if prof == 12:
            PlProf.append(PFlute)
        if prof == 13:
            PlProf.append(Shawm)
        if prof == 14:
            PlProf.append(Songhorn)
        if prof == 15:
            PlProf.append(Tantan)
        if prof == 16:
            PlProf.append(Thelarr)
        if prof == 17:
            PlProf.append(Viol)
        if prof == 18:
            PlProf.append(Wargong)
        if prof == 19:
            PlProf.append(Yarting)
        if prof == 20:
            PlProf.append(Zulkoon)
        if prof == 21:
            PlProf.append(AlchSupp)
        if prof == 22:
            PlProf.append(BrewSupp)
        if prof == 23:
            PlProf.append(CallSupp)
        if prof == 24:
            PlProf.append(CarpTools)
        if prof == 25:
            PlProf.append(CartTools)
        if prof == 26:
            PlProf.append(CobbTools)
        if prof == 27:
            PlProf.append(CooksUten)
        if prof == 28:
            PlProf.append(GlasTools)
        if prof == 29:
            PlProf.append(JeweTools)
        if prof == 30:
            PlProf.append(LthrwrkTools)
        if prof == 31:
            PlProf.append(MasnTools)
        if prof == 32:
            PlProf.append(PaintSupp)
        if prof == 33:
            PlProf.append(PottTools)
        if prof == 34:
            PlProf.append(SmthTools)
        if prof == 35:
            PlProf.append(TinkTools)
        if prof == 36:
            PlProf.append(WeavTools)
        if prof == 37:
            PlProf.append(WdcrvTools)
        if prof == 0:
            PlProf.append(MIARTrand)
    if param == "N":
        PlProf.append(MIARTrand)
    return PlProf
def abilityscores(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom):
    AbilityScores = [Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom]
    if param == "Y":
        print("0 - Random")
        print("1 - Increase One Skill by 2 and One Skill by 1")
        print("2 - Increase Three Skills by 1")
        abinc = int(input("Choose how to increase ability scores. "))
        if abinc == 1:
            print("0 - Random")
            print("1 - Charisma")
            print("2 - Constitution")
            print("3 - Dexterity")
            print("4 - Intelligence")
            print("5 - Strength")
            print("6 - Wisdom")
            mskill1 = int(input("Choose a skill to increase by 2. "))
            mskill2 = int(input("Choose an additional skill (could be the same skill) to increase by 1. "))
            if mskill1 == 0:
                skill2inc = random.randint(0, len(AbilityScores) - 1)
                AbilityScores[skill2inc] += 2
            else:
                AbilityScores[mskill1 - 1] += 2

            if mskill2 == 0:
                skill1inc = random.randint(0, len(AbilityScores) - 1)
                AbilityScores[skill1inc] += 1
            else:
                AbilityScores[mskill2 - 1] += 1
        if abinc == 2:
            print("0 - Random")
            print("1 - Charisma")
            print("2 - Constitution")
            print("3 - Dexterity")
            print("4 - Intelligence")
            print("5 - Strength")
            print("6 - Wisdom")
            mskill3one1 = int(input("Choose the first skill to increase by 1. "))
            mskill3one2 = int(input("Choose the second skill to increase by 1. "))
            mskill3one3 = int(input("Choose the third skill to increase by 1. "))
            if mskill3one1 == 0:
                randabsc1 = random.randint(0, len(AbilityScores) - 1)
                AbilityScores[randabsc1] += 1
            else:
                AbilityScores[mskill3one1 - 1] += 1

            if mskill3one2 == 0:
                randabsc2 = random.randint(0, len(AbilityScores) - 1)
                AbilityScores[randabsc2] += 1
            else:
                AbilityScores[mskill3one2 - 1] += 1

            if mskill3one3 == 0:                
                randabsc3 = random.randint(0, len(AbilityScores) - 1)
                AbilityScores[randabsc3] += 1
            else:
                AbilityScores[mskill3one3 - 1] += 1
        if abinc == 0:
            abilityscoreincreases = ["One by 2, One by 1", "Three by 1"]
            abilityscoreincreasesrand = random.choice(abilityscoreincreases)
            if abilityscoreincreasesrand == "One by 2, One by 1":
                randAbScore = random.randint(0, len(AbilityScores) - 1)
                randAbScore2 = random.randint(0, len(AbilityScores) - 1)
                AbilityScores[randAbScore] += 2
                AbilityScores[randAbScore2] += 1
            if abilityscoreincreasesrand == "Three by 1":
                randAbScore1 = random.randint(0, len(AbilityScores) - 1)
                randAbScore2 = random.randint(0, len(AbilityScores) - 1)
                randAbScore3 = random.randint(0, len(AbilityScores) - 1)
                AbilityScores[randAbScore1] += 1
                AbilityScores[randAbScore2] += 1
                AbilityScores[randAbScore3] += 1
    if param == "N":
        abilityscoreincreases = ["One by 2, One by 1", "Three by 1"]
        abilityscoreincreasesrand = random.choice(abilityscoreincreases)
        if abilityscoreincreasesrand == "One by 2, One by 1":
            randAbScore = random.randint(0, len(AbilityScores) - 1)
            randAbScore2 = random.randint(0, len(AbilityScores) - 1)
            AbilityScores[randAbScore] += 2
            AbilityScores[randAbScore2] += 1           
        if abilityscoreincreasesrand == "Three by 1":
            randAbScore1 = random.randint(0, len(AbilityScores) - 1)
            randAbScore2 = random.randint(0, len(AbilityScores) - 1)
            randAbScore3 = random.randint(0, len(AbilityScores) - 1)
            AbilityScores[randAbScore1] += 1
            AbilityScores[randAbScore2] += 1
            AbilityScores[randAbScore3] += 1
    return AbilityScores
def arttool2(param, PlProf):
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
    randArtTool1 = random.choice(ArtisanTools)
    randArtTool2 = random.choice(ArtisanTools)
    if param == "Y":
        print("1 - Alchemist's Supplies")
        print("2 - Brewer's Supplies")
        print("3 - Calligrapher's Supplies")
        print("4 - Carpenter's Tools")
        print("5 - Cartographer's Tools")
        print("6 - Cobbler's Tools")
        print("7 - Cook's Utensils")
        print("8 - Glassblower's Tools")
        print("9 - Jeweler's Tools")
        print("10 - Leatherworker's Tools")
        print("11 - Mason's Tools")
        print("12 - Painter's Supplies")
        print("13 - Potter's Tools")
        print("14 - Smith's Tools")
        print("15 - Tinker's Tools")
        print("16 - Weaver's Tools")
        print("17 - Woodcarver's Tools")
        arttools1 = int(input("Choose a tool to be proficient in. "))
        arttools2 = int(input("Choose a second tool to be proficient in. "))
        if arttools1 == 1:
            PlProf.append(AlchSupp)
        if arttools1 == 2:
            PlProf.append(BrewSupp)
        if arttools1 == 3:
            PlProf.append(CallSupp)
        if arttools1 == 4:
            PlProf.append(CarpTools)
        if arttools1 == 5:
            PlProf.append(CartTools)
        if arttools1 == 6:
            PlProf.append(CobbTools)
        if arttools1 == 7:
            PlProf.append(CooksUten)
        if arttools1 == 8:
            PlProf.append(GlasTools)
        if arttools1 == 9:
            PlProf.append(JeweTools)
        if arttools1 == 10:
            PlProf.append(LthrwrkTools)
        if arttools1 == 11:
            PlProf.append(MasnTools)
        if arttools1 == 12:
            PlProf.append(PaintSupp)
        if arttools1 == 13:
            PlProf.append(PottTools)
        if arttools1 == 14:
            PlProf.append(SmthTools)
        if arttools1 == 15:
            PlProf.append(TinkTools)
        if arttools1 == 16:
            PlProf.append(WeavTools)
        if arttools1 == 17:
            PlProf.append(WdcrvTools)
        if arttools1 == 0:
            PlProf.append(randArtTool1)            
        if arttools2 == 1:
            PlProf.append(AlchSupp)
        if arttools2 == 2:
            PlProf.append(BrewSupp)
        if arttools2 == 3:
            PlProf.append(CallSupp)
        if arttools2 == 4:
            PlProf.append(CarpTools)
        if arttools2 == 5:
            PlProf.append(CartTools)
        if arttools2 == 6:
            PlProf.append(CobbTools)
        if arttools2 == 7:
            PlProf.append(CooksUten)
        if arttools2 == 8:
            PlProf.append(GlasTools)
        if arttools2 == 9:
            PlProf.append(JeweTools)
        if arttools2 == 10:
            PlProf.append(LthrwrkTools)
        if arttools2 == 11:
            PlProf.append(MasnTools)
        if arttools2 == 12:
            PlProf.append(PaintSupp)
        if arttools2 == 13:
            PlProf.append(PottTools)
        if arttools2 == 14:
            PlProf.append(SmthTools)
        if arttools2 == 15:
            PlProf.append(TinkTools)
        if arttools2 == 16:
            PlProf.append(WeavTools)
        if arttools2 == 17:
            PlProf.append(WdcrvTools)        
        if arttools2 == 0:
            PlProf.append(randArtTool2)
    if param == "N":           
        PlProf.append(randArtTool1)
        PlProf.append(randArtTool2)  
    return PlProf     
def singleabilityscore(param, Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom):
    MainSkills = [
        Charisma, Constitution, Dexterity, Intelligence, Strength, Wisdom
    ]
    mainSkillRand = random.randint(0, len(MainSkills) - 1)    
    if param == "Y":
        print("0 - Random")
        print("1 - Charisma")
        print("2 - Constitution")
        print("3 - Dexterity")
        print("4 - Intelligence")
        print("5 - Strength")
        print("6 - Wisdom")
        abinc = int(input("Choose a score to increase by 1. "))
        if abinc == 0:    
            MainSkills[mainSkillRand] += 1 
        else:
            MainSkills[abinc-1] += 1
    if param == "N":       
        MainSkills[mainSkillRand] += 1    
    return MainSkills
def fourskillprof(param, PlProf, skillname1, skillname2, skillname3, skillname4):
    ProfFourSkill = [skillname1, skillname2, skillname3, skillname4]
    randprofskill = random.choice(ProfFourSkill)
    if param == "Y":
        print("0 - Random")
        print(f"1 - {skillname1}")
        print(f"2 - {skillname2}")
        print(f"3 - {skillname3}")
        print(f"4 - {skillname4}")
        profsklfour = int(input("Choose a skill to be proficient in. "))
        if profsklfour == 1:
            PlProf.append(skillname1)
        if profsklfour == 2:
            PlProf.append(skillname2)
        if profsklfour == 3:
            PlProf.append(skillname3)
        if profsklfour == 4:
            PlProf.append(skillname4)
        if profsklfour == 0:
            PlProf.append(randprofskill)
    if param == "N":
        PlProf.append(randprofskill) 
    return PlProf        
def skillprof2(param, PlProf):
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
    SklProf = [
        Acrobatics, AnimalHandling, Arcana, Athletics, Deception, History, Insight,
        Intimidation, Investigation, Medicine, Nature, Perception, Performance,
        Persuasion, Religion, SleightofHand, Stealth, Survival    
    ]
    RandSklProf1 = random.choice(SklProf)
    RandSklProf2 = random.choice(SklProf)
    if param == "Y":
        print("0 - Random")
        print("1 - Acrobatics")
        print("2 - Animal Handling")
        print("3 - Arcana")
        print("4 - Athletics")
        print("5 - Deception")
        print("6 - History")
        print("7 - Insight")
        print("8 - Intimidation")
        print("9 - Investigation")
        print("10 - Medicine")
        print("11 - Nature")
        print("12 - Perception")
        print("13 - Performance")
        print("14 - Persuasion")
        print("15 - Religion")
        print("16 - Sleight of Hand")
        print("17 - Stealth")
        print("18 - Survival")
        sklprof1 = int(input("Choose a skill to be proficient in. "))
        sklprof2 = int(input("Choose a second skill to be proficient in. "))
        if sklprof1 == 1:
            PlProf.append(Acrobatics)
        if sklprof1 == 2:
            PlProf.append(AnimalHandling)
        if sklprof1 == 3:
            PlProf.append(Arcana)
        if sklprof1 == 4:
            PlProf.append(Athletics)
        if sklprof1 == 5:
            PlProf.append(Deception)
        if sklprof1 == 6:
            PlProf.append(History)
        if sklprof1 == 7:
            PlProf.append(Insight)
        if sklprof1 == 8:
            PlProf.append(Intimidation)
        if sklprof1 == 9:
            PlProf.append(Investigation)
        if sklprof1 == 10:
            PlProf.append(Medicine)
        if sklprof1 == 11:
            PlProf.append(Nature)
        if sklprof1 == 12:
            PlProf.append(Perception)
        if sklprof1 == 13:
            PlProf.append(Performance)
        if sklprof1 == 14:
            PlProf.append(Persuasion)
        if sklprof1 == 15:
            PlProf.append(Religion)
        if sklprof1 == 16:
            PlProf.append(SleightofHand)
        if sklprof1 == 17:
            PlProf.append(Stealth)
        if sklprof1 == 18:
            PlProf.append(Survival)
        if sklprof1 == 0:
            PlProf.append(RandSklProf1)
        if sklprof2 == 1:
            PlProf.append(Acrobatics)
        if sklprof2 == 2:
            PlProf.append(AnimalHandling)
        if sklprof2 == 3:
            PlProf.append(Arcana)
        if sklprof2 == 4:
            PlProf.append(Athletics)
        if sklprof2 == 5:
            PlProf.append(Deception)
        if sklprof2 == 6:
            PlProf.append(History)
        if sklprof2 == 7:
            PlProf.append(Insight)
        if sklprof2 == 8:
            PlProf.append(Intimidation)
        if sklprof2 == 9:
            PlProf.append(Investigation)
        if sklprof2 == 10:
            PlProf.append(Medicine)
        if sklprof2 == 11:
            PlProf.append(Nature)
        if sklprof2 == 12:
            PlProf.append(Perception)
        if sklprof2 == 13:
            PlProf.append(Performance)
        if sklprof2 == 14:
            PlProf.append(Persuasion)
        if sklprof2 == 15:
            PlProf.append(Religion)
        if sklprof2 == 16:
            PlProf.append(SleightofHand)
        if sklprof2 == 17:
            PlProf.append(Stealth)
        if sklprof2 == 18:
            PlProf.append(Survival)        
        if sklprof2 == 0:
            PlProf.append(RandSklProf2)
    if param == "N":
        PlProf.append(RandSklProf1)
        PlProf.append(RandSklProf2)
    return PlProf
def threetoolprof(param, PlProf, tool1, tool2, tool3):
    ThreeTools = [tool1, tool2, tool3]
    threetoolrand = random.choice(ThreeTools)
    if param == "Y":
        print("0 - Random")
        print(f"1 - {tool1}")
        print(f"2 - {tool2}")
        print(f"3 - {tool3}")
        thrtl = int(input("Please pick a skill from the above list. "))
        if thrtl == 1:
            PlProf.append(tool1)
        if thrtl == 2:
            PlProf.append(tool2)
        if thrtl == 3:
            PlProf.append(tool3)
        if thrtl == 0:
            PlProf.append(threetoolrand)
    if param == "N":
        PlProf.append(threetoolrand)  
    return PlProf    
def toolskillprof(param, PlProf):
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
    SklTlProf = [
        Acrobatics, AnimalHandling, Arcana, Athletics, Deception, History, Insight,
        Intimidation, Investigation, Medicine, Nature, Perception, Performance,
        Persuasion, Religion, SleightofHand, Stealth, Survival, AlchSupp, BrewSupp,
        CallSupp, CarpTools, CartTools, CobbTools, CooksUten, GlasTools, JeweTools,
        LthrwrkTools, MasnTools, PaintSupp, PottTools, SmthTools, TinkTools, WeavTools, WdcrvTools
    ]
    SklTlProfRand = random.choice(SklTlProf)
    if param == "Y":
        print("0 - Random")
        print("1 - Acrobatics")
        print("2 - Animal Handling")
        print("3 - Arcana")
        print("4 - Athletics")
        print("5 - Deception")
        print("6 - History")
        print("7 - Insight")
        print("8 - Intimidation")
        print("9 - Investigation")
        print("10 - Medicine")
        print("11 - Nature")
        print("12 - Perception")
        print("13 - Performance")
        print("14 - Persuasion")
        print("15 - Religion")
        print("16 - Sleight of Hand")
        print("17 - Stealth")
        print("18 - Survival")        
        print("19 - Alchemist's Supplies")
        print("20 - Brewer's Supplies")
        print("21 - Calligrapher's Supplies")
        print("22 - Carpenter's Tools")
        print("23 - Cartographer's Tools")
        print("24 - Cobbler's Tools")
        print("25 - Cook's Utensils")
        print("26 - Glassblower's Tools")
        print("27 - Jeweler's Tools")
        print("28 - Leatherworker's Tools")
        print("29 - Mason's Tools")
        print("30 - Painter's Supplies")
        print("31 - Potter's Tools")
        print("32 - Smith's Tools")
        print("33 - Tinker's Tools")
        print("34 - Weaver's Tools")
        print("35 - Woodcarver's Tools")
        arttoolskl = int(input("Choose a skill or an artisan tool to be proficient in. "))
        if arttoolskl == 1:
            PlProf.append(Acrobatics)
        if arttoolskl == 2:
            PlProf.append(AnimalHandling)
        if arttoolskl == 3:
            PlProf.append(Arcana)
        if arttoolskl == 4:
            PlProf.append(Athletics)
        if arttoolskl == 5:
            PlProf.append(Deception)
        if arttoolskl == 6:
            PlProf.append(History)
        if arttoolskl == 7:
            PlProf.append(Insight)
        if arttoolskl == 8:
            PlProf.append(Intimidation)
        if arttoolskl == 9:
            PlProf.append(Investigation)
        if arttoolskl == 10:
            PlProf.append(Medicine)
        if arttoolskl == 11:
            PlProf.append(Nature)
        if arttoolskl == 12:
            PlProf.append(Perception)
        if arttoolskl == 13:
            PlProf.append(Performance)
        if arttoolskl == 14:
            PlProf.append(Persuasion)
        if arttoolskl == 15:
            PlProf.append(Religion)
        if arttoolskl == 16:
            PlProf.append(SleightofHand)
        if arttoolskl == 17:
            PlProf.append(Stealth)
        if arttoolskl == 18:
            PlProf.append(Survival)     
        if arttoolskl == 19:
            PlProf.append(AlchSupp)
        if arttoolskl == 20:
            PlProf.append(BrewSupp)
        if arttoolskl == 21:
            PlProf.append(CallSupp)
        if arttoolskl == 22:
            PlProf.append(CarpTools)
        if arttoolskl == 23:
            PlProf.append(CartTools)
        if arttoolskl == 24:
            PlProf.append(CobbTools)
        if arttoolskl == 25:
            PlProf.append(CooksUten)
        if arttoolskl == 26:
            PlProf.append(GlasTools)
        if arttoolskl == 27:
            PlProf.append(JeweTools)
        if arttoolskl == 28:
            PlProf.append(LthrwrkTools)
        if arttoolskl == 29:
            PlProf.append(MasnTools)
        if arttoolskl == 30:
            PlProf.append(PaintSupp)
        if arttoolskl == 31:
            PlProf.append(PottTools)
        if arttoolskl == 32:
            PlProf.append(SmthTools)
        if arttoolskl == 33:
            PlProf.append(TinkTools)
        if arttoolskl == 34:
            PlProf.append(WeavTools)
        if arttoolskl == 35:
            PlProf.append(WdcrvTools)
        if arttoolskl == 0:
            PlProf.append(SklTlProfRand)
    if param == "N":
        PlProf.append(SklTlProfRand)
    return PlProf
def martwepprof2(param, PlProf):
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
    MartWepRand1 = random.choice(MartialWeapons)
    MartWepRand2 = random.choice(MartialWeapons)
    if param == "Y":
        print("0 - Random")
        print("1 - Battleaxe")
        print("2 - Double-Bladed Scimitar")
        print("3 - Flail")
        print("4 - Glaive")
        print("5 - Greataxe")
        print("6 - Greatsword")
        print("7 - Halberd")
        print("8 - Lance")
        print("9 - Longsword")
        print("10 - Maul")
        print("11 - Morningstar")
        print("12 - Pike")
        print("13 - Rapier")
        print("14 - Scimitar")
        print("15 - Shortsword")
        print("16 - Trident")
        print("17 - War Pick")
        print("18 - Warhammer")
        print("19 - Whip")
        print("20 - Blowgun")
        print("21 - Crossbow")
        print("22 - Hand Crossbow")
        print("23 - Longbow")
        print("24 - Net")
        martwep1 = int(input("Choose a Martial Weapon to be proficient with. "))
        martwep2 = int(input("Choose a second Martial Weapon to be proficient with. "))
        if martwep1 == 1:
            PlProf.append(Battleaxe)
        if martwep1 == 2:
            PlProf.append(DoubleBladedScimitar)
        if martwep1 == 3:
            PlProf.append(Flail)
        if martwep1 == 4:
            PlProf.append(Glaive)
        if martwep1 == 5:
            PlProf.append(Greataxe)
        if martwep1 == 6:
            PlProf.append(Greatsword)
        if martwep1 == 7:
            PlProf.append(Halberd)
        if martwep1 == 8:
            PlProf.append(Lance)
        if martwep1 == 9:
            PlProf.append(Longsword)
        if martwep1 == 10:
            PlProf.append(Maul)
        if martwep1 == 11:
            PlProf.append(Morningstar)
        if martwep1 == 12:
            PlProf.append(Pike)
        if martwep1 == 13:
            PlProf.append(Rapier)
        if martwep1 == 14:
            PlProf.append(Scimitar)
        if martwep1 == 15:
            PlProf.append(Shortsword)
        if martwep1 == 16:
            PlProf.append(Trident)
        if martwep1 == 17:
            PlProf.append(WarPick)
        if martwep1 == 18:
            PlProf.append(Warhammer)
        if martwep1 == 19:
            PlProf.append(Whip)
        if martwep1 == 20:
            PlProf.append(Blowgun)
        if martwep1 == 21:
            PlProf.append(Crossbow)
        if martwep1 == 22:
            PlProf.append(HandCrossbow)
        if martwep1 == 23:
            PlProf.append(Longbow)
        if martwep1 == 24:
            PlProf.append(Net)
        if martwep1 == 0:
            PlProf.append(MartWepRand1)
        if martwep2 == 1:
            PlProf.append(Battleaxe)
        if martwep2 == 2:
            PlProf.append(DoubleBladedScimitar)
        if martwep2 == 3:
            PlProf.append(Flail)
        if martwep2 == 4:
            PlProf.append(Glaive)
        if martwep2 == 5:
            PlProf.append(Greataxe)
        if martwep2 == 6:
            PlProf.append(Greatsword)
        if martwep2 == 7:
            PlProf.append(Halberd)
        if martwep2 == 8:
            PlProf.append(Lance)
        if martwep2 == 9:
            PlProf.append(Longsword)
        if martwep2 == 10:
            PlProf.append(Maul)
        if martwep2 == 11:
            PlProf.append(Morningstar)
        if martwep2 == 12:
            PlProf.append(Pike)
        if martwep2 == 13:
            PlProf.append(Rapier)
        if martwep2 == 14:
            PlProf.append(Scimitar)
        if martwep2 == 15:
            PlProf.append(Shortsword)
        if martwep2 == 16:
            PlProf.append(Trident)
        if martwep2 == 17:
            PlProf.append(WarPick)
        if martwep2 == 18:
            PlProf.append(Warhammer)
        if martwep2 == 19:
            PlProf.append(Whip)
        if martwep2 == 20:
            PlProf.append(Blowgun)
        if martwep2 == 21:
            PlProf.append(Crossbow)
        if martwep2 == 22:
            PlProf.append(HandCrossbow)
        if martwep2 == 23:
            PlProf.append(Longbow)
        if martwep2 == 24:
            PlProf.append(Net)
        if martwep2 == 0:
            PlProf.append(MartWepRand2)
    if param == "N":
        PlProf.append(MartWepRand1)
        PlProf.append(MartWepRand2)
    return PlProf
def fiveskillprof(param, PlProf, skillname1, skillname2, skillname3, skillname4, skillname5):
    ProfFiveSkill = [skillname1, skillname2, skillname3, skillname4, skillname5]
    randprofskill = random.choice(ProfFiveSkill)
    if param == "Y":
        print("0 - Random")
        print(f"1 - {skillname1}")
        print(f"2 - {skillname2}")
        print(f"3 - {skillname3}")
        print(f"4 - {skillname4}")
        print(f"5 - {skillname5}")
        profsklfive = int(input("Choose a skill to be proficient in. "))
        if profsklfive == 1:
            PlProf.append(skillname1)
        if profsklfive == 2:
            PlProf.append(skillname2)
        if profsklfive == 3:
            PlProf.append(skillname3)
        if profsklfive == 4:
            PlProf.append(skillname4)
        if profsklfive == 5:
            PlProf.append(skillname5)           
        if profsklfive == 0:
            PlProf.append(randprofskill)
    if param == "N":
        PlProf.append(randprofskill)   
    return PlProf  
def twoskillprof(param, PlProf, skillname1, skillname2):
    ProfTwoSkill = [skillname1, skillname2]
    randprofskill = random.choice(ProfTwoSkill)
    if param == "Y":
        print("0 - Random")
        print(f"1 - {skillname1}")
        print(f"2 - {skillname2}")
        profskltwo = int(input("Choose a skill to be proficient in. "))
        if profskltwo == 1:
            PlProf.append(skillname1)
        if profskltwo == 2:
            PlProf.append(skillname2)
        if profskltwo == 0:
            PlProf.append(randprofskill)
    if param == "N":
        PlProf.append(randprofskill)    
    return PlProf
def vedsixskillprof(param, PlProf, skillname1, skillname2, skillname3, skillname4, skillname5, skillname6):
    ProfSixSkill = [skillname1, skillname2, skillname3, skillname4, skillname5, skillname6]
    randprofskill = random.choice(ProfSixSkill)
    if param == "Y":
        print("0 - Random")
        print(f"1 - {skillname1}")
        print(f"2 - {skillname2}")
        print(f"3 - {skillname3}")
        print(f"4 - {skillname4}")
        print(f"5 - {skillname5}")
        print(f"6 - {skillname6}")
        profsklsix = int(input("Choose a skill to be proficient in. "))
        if profsklsix == 1:
            PlProf.append(skillname1)
            PlProf.append("Whenever you make an ability check with the chosen skill, roll a d4 and add the number rolled to the check's total.")
        if profsklsix == 2:
            PlProf.append(skillname2)
            PlProf.append("Whenever you make an ability check with the chosen skill, roll a d4 and add the number rolled to the check's total.")
        if profsklsix == 3:
            PlProf.append(skillname3)
            PlProf.append("Whenever you make an ability check with the chosen skill, roll a d4 and add the number rolled to the check's total.")
        if profsklsix == 4:
            PlProf.append(skillname4)
            PlProf.append("Whenever you make an ability check with the chosen skill, roll a d4 and add the number rolled to the check's total.")
        if profsklsix == 5:
            PlProf.append(skillname5)
            PlProf.append("Whenever you make an ability check with the chosen skill, roll a d4 and add the number rolled to the check's total.")  
        if profsklsix == 6:
            PlProf.append(skillname6)
            PlProf.append("Whenever you make an ability check with the chosen skill, roll a d4 and add the number rolled to the check's total.")                       
        if profsklsix == 0:
            PlProf.append(randprofskill)
            PlProf.append("Whenever you make an ability check with the chosen skill, roll a d4 and add the number rolled to the check's total.")
    if param == "N": 
        PlProf.append(randprofskill)
        PlProf.append("Whenever you make an ability check with the chosen skill, roll a d4 and add the number rolled to the check's total.")    
    return PlProf
def vedartisantools(param, PlProf):
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
    ArtisanToolsRand = random.choice(ArtisanTools)
    if param == "Y":
        print("0 - Random")
        print("1 - Alchemist's Supplies")
        print("2 - Brewer's Supplies")
        print("3 - Calligrapher's Supplies")
        print("4 - Carpenter's Tools")
        print("5 - Cartographer's Tools")
        print("6 - Cobbler's Tools")
        print("7 - Cook's Utensils")
        print("8 - Glassblower's Tools")
        print("9 - Jeweler's Tools")
        print("10 - Leatherworker's Tools")
        print("11 - Mason's Tools")
        print("12 - Painter's Supplies")
        print("13 - Potter's Tools")
        print("14 - Smith's Tools")
        print("15 - Tinker's Tools")
        print("16 - Weaver's Tools")
        print("17 - Woodcarver's Tools")
        arttool = int(input("Choose an artisan tool to be proficient in. "))
        if arttool == 1:
            PlProf.append(AlchSupp)
            PlProf.append("Whenever you make an ability check with the chosen tool, roll a d4 and add the number rolled to the check's total.")
        if arttool == 2:
            PlProf.append(BrewSupp)
            PlProf.append("Whenever you make an ability check with the chosen tool, roll a d4 and add the number rolled to the check's total.")
        if arttool == 3:
            PlProf.append(CallSupp)
            PlProf.append("Whenever you make an ability check with the chosen tool, roll a d4 and add the number rolled to the check's total.")
        if arttool == 4:
            PlProf.append(CarpTools)
            PlProf.append("Whenever you make an ability check with the chosen tool, roll a d4 and add the number rolled to the check's total.")
        if arttool == 5:
            PlProf.append(CartTools)
            PlProf.append("Whenever you make an ability check with the chosen tool, roll a d4 and add the number rolled to the check's total.")
        if arttool == 6:
            PlProf.append(CobbTools)
            PlProf.append("Whenever you make an ability check with the chosen tool, roll a d4 and add the number rolled to the check's total.")
        if arttool == 7:
            PlProf.append(CooksUten)
            PlProf.append("Whenever you make an ability check with the chosen tool, roll a d4 and add the number rolled to the check's total.")
        if arttool == 8:
            PlProf.append(GlasTools)
            PlProf.append("Whenever you make an ability check with the chosen tool, roll a d4 and add the number rolled to the check's total.")
        if arttool == 9:
            PlProf.append(JeweTools)
            PlProf.append("Whenever you make an ability check with the chosen tool, roll a d4 and add the number rolled to the check's total.")
        if arttool == 10:
            PlProf.append(LthrwrkTools)
            PlProf.append("Whenever you make an ability check with the chosen tool, roll a d4 and add the number rolled to the check's total.")
        if arttool == 11:
            PlProf.append(MasnTools)
            PlProf.append("Whenever you make an ability check with the chosen tool, roll a d4 and add the number rolled to the check's total.")
        if arttool == 12:
            PlProf.append(PaintSupp)
            PlProf.append("Whenever you make an ability check with the chosen tool, roll a d4 and add the number rolled to the check's total.")
        if arttool == 13:
            PlProf.append(PottTools)
            PlProf.append("Whenever you make an ability check with the chosen tool, roll a d4 and add the number rolled to the check's total.")
        if arttool == 14:
            PlProf.append(SmthTools)
            PlProf.append("Whenever you make an ability check with the chosen tool, roll a d4 and add the number rolled to the check's total.")
        if arttool == 15:
            PlProf.append(TinkTools)
            PlProf.append("Whenever you make an ability check with the chosen tool, roll a d4 and add the number rolled to the check's total.")
        if arttool == 16:
            PlProf.append(WeavTools)
            PlProf.append("Whenever you make an ability check with the chosen tool, roll a d4 and add the number rolled to the check's total.")
        if arttool == 17:
            PlProf.append(WdcrvTools)
            PlProf.append("Whenever you make an ability check with the chosen tool, roll a d4 and add the number rolled to the check's total.")
        if arttool == 0:
            PlProf.append(ArtisanToolsRand)
            PlProf.append("Whenever you make an ability check with the chosen tool, roll a d4 and add the number rolled to the check's total.")
    if param == "N":           
        PlProf.append(ArtisanToolsRand)
        PlProf.append("Whenever you make an ability check with the chosen tool, roll a d4 and add the number rolled to the check's total.")
    return PlProf
def skillprof(param, PlProf):
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
    SklProf = [
        Acrobatics, AnimalHandling, Arcana, Athletics, Deception, History, Insight,
        Intimidation, Investigation, Medicine, Nature, Perception, Performance,
        Persuasion, Religion, SleightofHand, Stealth, Survival    
    ]
    RandSklProf1 = random.choice(SklProf)
    if param == "Y":
        print("0 - Random")
        print("1 - Acrobatics")
        print("2 - Animal Handling")
        print("3 - Arcana")
        print("4 - Athletics")
        print("5 - Deception")
        print("6 - History")
        print("7 - Insight")
        print("8 - Intimidation")
        print("9 - Investigation")
        print("10 - Medicine")
        print("11 - Nature")
        print("12 - Perception")
        print("13 - Performance")
        print("14 - Persuasion")
        print("15 - Religion")
        print("16 - Sleight of Hand")
        print("17 - Stealth")
        print("18 - Survival")
        sklprof1 = int(input("Choose a skill to be proficient in. "))
        if sklprof1 == 1:
            PlProf.append(Acrobatics)
        if sklprof1 == 2:
            PlProf.append(AnimalHandling)
        if sklprof1 == 3:
            PlProf.append(Arcana)
        if sklprof1 == 4:
            PlProf.append(Athletics)
        if sklprof1 == 5:
            PlProf.append(Deception)
        if sklprof1 == 6:
            PlProf.append(History)
        if sklprof1 == 7:
            PlProf.append(Insight)
        if sklprof1 == 8:
            PlProf.append(Intimidation)
        if sklprof1 == 9:
            PlProf.append(Investigation)
        if sklprof1 == 10:
            PlProf.append(Medicine)
        if sklprof1 == 11:
            PlProf.append(Nature)
        if sklprof1 == 12:
            PlProf.append(Perception)
        if sklprof1 == 13:
            PlProf.append(Performance)
        if sklprof1 == 14:
            PlProf.append(Persuasion)
        if sklprof1 == 15:
            PlProf.append(Religion)
        if sklprof1 == 16:
            PlProf.append(SleightofHand)
        if sklprof1 == 17:
            PlProf.append(Stealth)
        if sklprof1 == 18:
            PlProf.append(Survival)
        if sklprof1 == 0:
            PlProf.append(RandSklProf1)
    if param == "N":
        PlProf.append(RandSklProf1)
    return PlProf

def twoskillsfromlist(param, SkillsProf, skill1, skill2, skill3, skill4, skill5, skill6, skill7):
    SleightofHand = "Sleight of Hand"
    SkillsList = [skill1, skill2, skill3, skill4, skill5, skill6, skill7]
    if param == "Y":
        print("0 - Random")
        for i, skill in enumerate(SkillsList, 1):
            print(f"{i} - {skill}")
        skillone = int(input("Which is the first skill to be proficient in? "))
        skilltwo = int(input("Which is the second skill to be proficient in? "))
        if skillone == 1:
            SkillsProf.append(skill1)
        if skillone == 2:
            SkillsProf.append(skill2)
        if skillone == 3:
            SkillsProf.append(skill3)
        if skillone == 4:
            SkillsProf.append(skill4)
        if skillone == 5:
            SkillsProf.append(skill5)
        if skillone == 6:
            SkillsProf.append(skill6)
        if skillone == 7:
            SkillsProf.append(skill7)
        if skillone == 0:
            SkillsListRand1 = random.choice(SkillsList)
            SkillsProf.append(SkillsListRand1)
        if skilltwo == 1:
            SkillsProf.append(skill1)
        if skilltwo == 2:
            SkillsProf.append(skill2)
        if skilltwo == 3:
            SkillsProf.append(skill3)
        if skilltwo == 4:
            SkillsProf.append(skill4)
        if skilltwo == 5:
            SkillsProf.append(skill5)
        if skilltwo == 6:
            SkillsProf.append(skill6)
        if skilltwo == 7:
            SkillsProf.append(skill7)
        if skilltwo == 0:
            SkillsListRand2 = random.choice(SkillsList)
            SkillsProf.append(SkillsListRand2)
    if param == "N":
        SkillsListRand1 = random.choice(SkillsList)
        SkillsProf.append(SkillsListRand1)
        SkillsListRand2 = random.choice(SkillsList)
        SkillsProf.append(SkillsListRand2)
    return SkillsProf

def twosimpleweapons(param, EQP):
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
    SimpleWeapons = ["Club", "Dagger", "Dart", "Greatclub", "Handaxe", "Javelin", "LightCrossbow", "LightHammer", "Mace", "Quarterstaff", "Shortbow", "Sickle", "Sling", "Spear", "Yklwa"]
    if param == "Y":
        print("0 - Random")
        for i, sw in enumerate(SimpleWeapons,1):
            print(f"{i} - {sw}")
        simpleweapon1 = int(input("Which simple weapon do you want to be proficient in first? "))
        simpleweapon2 = int(input("Which simple weapon do you want to be proficient in second? "))
        if ((simpleweapon1 == 1) or (simpleweapon2 == 1)):
            EQP.append(Club)
        if ((simpleweapon1 == 2) or (simpleweapon2 == 2)):
            EQP.append(Dagger)
        if ((simpleweapon1 == 3) or (simpleweapon2 == 3)):
            EQP.append(Dart)
        if ((simpleweapon1 == 4) or (simpleweapon2 == 4)):
            EQP.append(Greatclub)
        if ((simpleweapon1 == 5) or (simpleweapon2 == 5)):
            EQP.append(Handaxe)
        if ((simpleweapon1 == 6) or (simpleweapon2 == 6)):
            EQP.append(Javelin)
        if ((simpleweapon1 == 7) or (simpleweapon2 == 7)):
            EQP.append(LightCrossbow)
        if ((simpleweapon1 == 8) or (simpleweapon2 == 8)):
            EQP.append(LightHammer)
        if ((simpleweapon1 == 9) or (simpleweapon2 == 9)):
            EQP.append(Mace)
        if ((simpleweapon1 == 10) or (simpleweapon2 == 10)):
            EQP.append(Quarterstaff)
        if ((simpleweapon1 == 11) or (simpleweapon2 == 11)):
            EQP.append(Shortbow)
        if ((simpleweapon1 == 12) or (simpleweapon2 == 12)):
            EQP.append(Sickle)
        if ((simpleweapon1 == 13) or (simpleweapon2 == 13)):
            EQP.append(Sling)
        if ((simpleweapon1 == 14) or (simpleweapon2 == 14)):
            EQP.append(Spear)
        if ((simpleweapon1 == 15) or (simpleweapon2 == 15)):
            EQP.append(Yklwa)
        if ((simpleweapon1 == 0) or (simpleweapon2 == 0)):
            RandomSW = random.choice(SimpleWeapons)
            EQP.append(RandomSW)
    if param == "N":
        RandomSW1 = random.choice(SimpleWeapons)
        EQP.append(RandomSW1)
        SimpleWeapons.remove(RandomSW1)
        RandomSW2 = random.choice(SimpleWeapons)
        EQP.append(RandomSW2)
    return EQP
import random
from dndchargenv3 import *
from fractions import Fraction

#Dice are in dndchargen

'''
DMorPlay = int(input("Are you a 1 - DM or 2 - Player? "))
if DMorPlay == 1:
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
            chLvl = int(input("What level is character {}? ".format(p+1)))
            chLvlList.append(chLvl)
            para = input("Set parameters on character {}? Y/N ".format(p+1))
            dndCharGen(para)
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
            para = input("Set parameters on character {}? Y/N ".format(p+1))
            dndCharGen(para)
else:
    #Add in a level check for classes, if the level is 3+, the subclass is available.
    para = input("Set parameters on character? Y/N ")
    dndCharGen(para)    

'''
#This block of code is to make sure dndCharGen works
#for i in range(500):
para = "N"
dndCharGen(para)

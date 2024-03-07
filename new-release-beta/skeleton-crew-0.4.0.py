#starting boat score average of 1200 with neutral fatigue mod
from colorama import init, Fore, Back, Style

init(convert=True)
import random
global opheliaEvent
opheliaEvent=0
global compStarter
compStarter = 2500
global compIncrement
compIncrement = 600
global winCounter
winCounter=0
global robinQuestComplete
robinQuestComplete=0
global robinQuestEnable
robinQuestEnable=0
global robinQuestStage
robinQuestStage=0
global featherArtifact
featherArtifact=0
global foundFeather
foundFeather=0
global boatDamage
boatDamage=0
global practiceTimeModifier
practiceTimeModifier=0
global arrowheadsInPossession
arrowheadsInPossession = 0
global coinArtifact
coinArtifact=0
global foundCoin
foundCoin=0
global foundHarpoon 
foundHarpoon = 0
global harpoonArtifact
harpoonArtifact = 0
global fishermenRep
fishermenRep=0
global beingEncountered
beingEncountered = 0
global meteorLanded
meteorLanded = 0
global compCounter
compCounter = 1
global fishInPossession
fishInPossession = 0
global artifactInPossession
artifactInPossession = 0
global opheliaLove
opheliaLove=0
global opheliaAuthority
opheliaAuthority = 0
global boatAddRhythm
global boatAddPower
global boatAddTechnique
global samDeny
global ollieDeny
global noelDeny
global robinDeny
global krisDeny
global milanDeny
global angelDeny
global santanaDeny
santanaDeny = 0
global progressMod
progressMod = 0.5
global day
day = 0
global week
week = 0
global nightTerror
nightTerror = 0
# Sam variable block
global samEndurance 
samEndurance=100
global samPower
samPower=90
global samFatigue
samFatigue= 0
global samMorale
samMorale=500
global samRhythm
samRhythm= 50
global samTechnique
samTechnique= 50
global samTerror
samTerror= 0

# Ollie variable block
global ollieEndurance 
ollieEndurance=90
global olliePower
olliePower=80
global ollieFatigue
ollieFatigue= 0
global ollieMorale
ollieMorale=500
global ollieRhythm
ollieRhythm= 70
global ollieTechnique
ollieTechnique= 70
global ollieTerror
ollieTerror= 0

# Noel variable block
global noelEndurance 
noelEndurance=90
global noelPower
noelPower=90
global noelFatigue
noelFatigue= 0
global noelMorale
noelMorale=500
global noelRhythm
noelRhythm= 90
global noelTechnique
noelTechnique= 110
global noelTerror
noelTerror= 0

# Robin variable block
global robinEndurance 
robinEndurance=100
global robinPower
robinPower=90
global robinFatigue
robinFatigue= 0
global robinMorale
robinMorale=500
global robinRhythm
robinRhythm= 110
global robinTechnique
robinTechnique= 90
global robinTerror
robinTerror= 0

# Kris variable block
global krisEndurance 
krisEndurance=90
global krisPower
krisPower=120
global krisFatigue
krisFatigue= 0
global krisMorale
krisMorale=500
global krisRhythm
krisRhythm= 80
global krisTechnique
krisTechnique= 90
global krisTerror
krisTerror= 0

# Milan variable block
global milanEndurance 
milanEndurance=100
global milanPower
milanPower=90
global milanFatigue
milanFatigue= 0
global milanMorale
milanMorale=500
global milanRhythm
milanRhythm= 70
global milanTechnique
milanTechnique= 90
global milanTerror
milanTerror= 15

# Angel variable block
global angelEndurance 
angelEndurance=90
global angelPower
angelPower=90
global angelFatigue
angelFatigue= 0
global angelMorale
angelMorale=500
global angelRhythm
angelRhythm= 90
global angelTechnique
angelTechnique= 90
global angelTerror
angelTerror= 15

# Santana variable block
global santanaEndurance 
santanaEndurance=90
global santanaPower
santanaPower=90
global santanaFatigue
santanaFatigue= 0
global santanaMorale
santanaMorale=500
global santanaRhythm
santanaRhythm= 90
global santanaTechnique
santanaTechnique= 90
global santanaTerror
santanaTerror= 15

def teamAverageTerror():
 global samTerror
 global ollieTerror
 global noelTerror
 global robinTerror
 global krisTerror
 global milanTerror
 global angelTerror
 global santanaTerror

 aveTerror = (samTerror+ollieTerror+noelTerror+robinTerror+krisTerror+milanTerror+angelTerror+santanaTerror)/8\
 
 return aveTerror

#put before each day, to return teamAdd variables to 0
def teamAddBlock():
 global teamAddEndurance
 teamAddEndurance = 0
 global teamAddPower
 teamAddPower = 0
 global teamAddMorale
 teamAddMorale = 0
 global teamAddRhythm
 teamAddRhythm = 0
 global teamAddFatigue
 teamAddFatigue = 0
 global teamAddTechnique
 teamAddTechnique = 0
 global teamAddTerror
 teamAddTerror = 0

def updateSam():
 # Sam's focus is on endurance and power.  Low technique and rhythm modifiers.  Is not tired or frightened easily.  Dejected easily.
 global samPower
 global samEndurance
 global samFatigue
 global samMorale
 global samRhythm
 global samTechnique
 global samTerror
 samEnduranceMod=1.1
 samPowerMod=1
 samFatigueMod=0.8
 samMoraleMod=1.15
 samRhythmMod=0.85
 samTechniqueMod=0.85
 samTerrorMod=0.9
 samEndurance=samEndurance+teamAddEndurance*samEnduranceMod*progressMod
 samPower=samPower+teamAddPower*samPowerMod*progressMod
 samFatigue=samFatigue+teamAddFatigue*samFatigueMod
 samMorale=samMorale+teamAddMorale*samMoraleMod
 samRhythm=samRhythm+teamAddRhythm*samRhythmMod*progressMod
 samTechnique=samTechnique+teamAddTechnique*samTechniqueMod*progressMod
 samTerror=samTerror+teamAddTerror*samTerrorMod

def updateOllie():
 # Ollie's focus is on technique and rhythm.  Low power and morale modifiers.  Not frightened easily.
 global olliePower
 global ollieEndurance
 global ollieFatigue
 global ollieMorale
 global ollieRhythm
 global ollieTechnique
 global ollieTerror
 ollieEnduranceMod=1
 olliePowerMod=0.9
 ollieFatigueMod=0.9
 ollieMoraleMod=0.85
 ollieRhythmMod=1.2
 ollieTechniqueMod=1.2
 ollieTerrorMod=0.9
 ollieEndurance=ollieEndurance+teamAddEndurance*ollieEnduranceMod*progressMod
 olliePower=olliePower+teamAddPower*olliePowerMod*progressMod*progressMod
 ollieFatigue=ollieFatigue+teamAddFatigue*ollieFatigueMod
 ollieMorale=ollieMorale+teamAddMorale*ollieMoraleMod
 ollieRhythm=ollieRhythm+teamAddRhythm*ollieRhythmMod*progressMod
 ollieTechnique=ollieTechnique+teamAddTechnique*ollieTechniqueMod*progressMod
 ollieTerror=ollieTerror+teamAddTerror*ollieTerrorMod

def updateNoel():
 # Noel balances most aspects.  Easy to tire but resilient against mental harm.  Keeps a cool head.
 global noelPower
 global noelEndurance
 global noelFatigue
 global noelMorale
 global noelRhythm
 global noelTechnique
 global noelTerror
 noelEnduranceMod=1
 noelPowerMod=1
 noelFatigueMod=1.15
 noelMoraleMod=1
 noelRhythmMod=1.0
 noelTechniqueMod=1.2
 noelTerrorMod=0.75
 noelEndurance=noelEndurance+teamAddEndurance*noelEnduranceMod*progressMod
 noelPower=noelPower+teamAddPower*noelPowerMod*progressMod
 noelFatigue=noelFatigue+teamAddFatigue*noelFatigueMod
 noelMorale=noelMorale+teamAddMorale*noelMoraleMod
 noelRhythm=noelRhythm+teamAddRhythm*noelRhythmMod*progressMod
 noelTechnique=noelTechnique+teamAddTechnique*noelTechniqueMod*progressMod
 noelTerror=noelTerror+teamAddTerror*noelTerrorMod

def updateRobin():
 # Robin has high spirits and is well in tune with the mood of the team.  Notable in morale, less good with power.
 global robinPower
 global robinEndurance
 global robinFatigue
 global robinMorale
 global robinRhythm
 global robinTechnique
 global robinTerror
 robinEnduranceMod=1
 robinPowerMod=0.8
 robinFatigueMod=0.9
 robinMoraleMod=1.3
 robinRhythmMod=1.1
 robinTechniqueMod=1
 robinTerrorMod=1.3
 robinEndurance=robinEndurance+teamAddEndurance*robinEnduranceMod*progressMod
 robinPower=robinPower+teamAddPower*robinPowerMod*progressMod
 robinFatigue=robinFatigue+teamAddFatigue*robinFatigueMod
 robinMorale=robinMorale+teamAddMorale*robinMoraleMod
 robinRhythm=robinRhythm+teamAddRhythm*robinRhythmMod*progressMod
 robinTechnique=robinTechnique+teamAddTechnique*robinTechniqueMod*progressMod
 robinTerror=robinTerror+teamAddTerror*robinTerrorMod

def updateKris():
 # Kris is quite strong.  Their strength means they are unable to be in time as well.  Mentally resilient, but less so physically.
 global krisPower
 global krisEndurance
 global krisFatigue
 global krisMorale
 global krisRhythm
 global krisTechnique
 global krisTerror
 krisEnduranceMod=0.9
 krisPowerMod=1.2
 krisFatigueMod=1.1
 krisMoraleMod=0.85
 krisRhythmMod=0.75
 krisTechniqueMod=0.85
 krisTerrorMod=0.85
 krisEndurance=krisEndurance+teamAddEndurance*krisEnduranceMod*progressMod
 krisPower=krisPower+teamAddPower*krisPowerMod*progressMod
 krisFatigue=krisFatigue+teamAddFatigue*krisFatigueMod
 krisMorale=krisMorale+teamAddMorale*krisMoraleMod
 krisRhythm=krisRhythm+teamAddRhythm*krisRhythmMod*progressMod
 krisTechnique=krisTechnique+teamAddTechnique*krisTechniqueMod*progressMod
 krisTerror=krisTerror+teamAddTerror*krisTerrorMod

def updateMilan():
 # Milan is quite average, but tires very slowly.  Unstable in every sense.
 global milanPower
 global milanEndurance
 global milanFatigue
 global milanMorale
 global milanRhythm
 global milanTechnique
 global milanTerror
 milanEnduranceMod=1.2
 milanPowerMod=1
 milanFatigueMod=0.75
 milanMoraleMod=1
 milanRhythmMod=1
 milanTechniqueMod=0.75
 milanTerrorMod=1.4
 milanEndurance=milanEndurance+teamAddEndurance*milanEnduranceMod*progressMod
 milanPower=milanPower+teamAddPower*milanPowerMod*progressMod
 milanFatigue=milanFatigue+teamAddFatigue*milanFatigueMod
 milanMorale=milanMorale+teamAddMorale*milanMoraleMod
 milanRhythm=milanRhythm+teamAddRhythm*milanRhythmMod*progressMod
 milanTechnique=milanTechnique+teamAddTechnique*milanTechniqueMod*progressMod
 milanTerror=milanTerror+teamAddTerror*milanTerrorMod

def updateAngel():
 # Angel is exceptionally mentally resilient.  Otherwise unremarkable.
 global angelPower
 global angelEndurance
 global angelFatigue
 global angelMorale
 global angelRhythm
 global angelTechnique
 global angelTerror
 angelEnduranceMod=1
 angelPowerMod=1
 angelFatigueMod=1
 angelMoraleMod=0.75
 angelRhythmMod=1
 angelTechniqueMod=1
 angelTerrorMod=0.6
 angelEndurance=angelEndurance+teamAddEndurance*angelEnduranceMod*progressMod
 angelPower=angelPower+teamAddPower*angelPowerMod*progressMod
 angelFatigue=angelFatigue+teamAddFatigue*angelFatigueMod
 angelMorale=angelMorale+teamAddMorale*angelMoraleMod
 angelRhythm=angelRhythm+teamAddRhythm*angelRhythmMod*progressMod
 angelTechnique=angelTechnique+teamAddTechnique*angelTechniqueMod*progressMod
 angelTerror=angelTerror+teamAddTerror*angelTerrorMod

def updateSantana():
 # Santana is gifted with exceptional power and technique.  Their sustain, however, is lacking.
 global santanaPower
 global santanaEndurance
 global santanaFatigue
 global santanaMorale
 global santanaRhythm
 global santanaTechnique
 global santanaTerror
 santanaEnduranceMod=0.75
 santanaPowerMod=1.3
 santanaFatigueMod=1.3
 santanaMoraleMod=1
 santanaRhythmMod=1.2
 santanaTechniqueMod=1.3
 santanaTerrorMod=1.15
 santanaEndurance=santanaEndurance+teamAddEndurance*santanaEnduranceMod*progressMod
 santanaPower=santanaPower+teamAddPower*santanaPowerMod*progressMod
 santanaFatigue=santanaFatigue+teamAddFatigue*santanaFatigueMod
 santanaMorale=santanaMorale+teamAddMorale*santanaMoraleMod
 santanaRhythm=santanaRhythm+teamAddRhythm*santanaRhythmMod*progressMod
 santanaTechnique=santanaTechnique+teamAddTechnique*santanaTechniqueMod*progressMod
 santanaTerror=santanaTerror+teamAddTerror*santanaTerrorMod

def actionOne():
  print("The team practices steady state rowing on the ergs.  A good time to put on a podcast.")
  global teamAddEndurance
  global teamAddPower
  global teamAddFatigue
  global teamAddMorale
  global teamAddRhythm
  global teamAddTechnique
  global teamAddTerror
  global practiceTime
  teamAddEndurance = 10
  teamAddPower = 4
  teamAddMorale = -5
  teamAddFatigue = 16
  updateSam()
  updateOllie()
  updateNoel()
  updateRobin()
  updateKris()
  updateMilan()
  updateAngel()
  updateSantana()
  practiceTime=practiceTime-30
  print("")

def actionTwo():
  print("The team practices anaerobic rowing on the ergs.  It hurts like hell, but you know it's helping.")
  global teamAddEndurance
  global teamAddPower
  global teamAddFatigue
  global teamAddMorale
  global teamAddRhythm
  global teamAddTechnique
  global teamAddTerror
  global practiceTime
  teamAddEndurance = 4
  teamAddPower = 10
  teamAddMorale = -5
  teamAddFatigue = 26
  updateSam()
  updateOllie()
  updateNoel()
  updateRobin()
  updateKris()
  updateMilan()
  updateAngel()
  updateSantana()
  practiceTime=practiceTime-30
  print("")

def actionThree():
  print("The team practices steady state rowing on the water.  It's calm out here.")
  global teamAddEndurance
  global teamAddPower
  global teamAddFatigue
  global teamAddMorale
  global teamAddRhythm
  global teamAddTechnique
  global teamAddTerror
  global practiceTime
  global tempMentalModifier
  global tempExerciseModifier
  global nightTerror
  tempExerciseModifier=1
  tempMentalModifier=1
  teamAddEndurance = 7*tempExerciseModifier
  teamAddPower = 3*tempExerciseModifier
  teamAddTechnique = 9
  teamAddRhythm = 6
  teamAddMorale = 2*tempMentalModifier
  teamAddFatigue = 14
  teamAddTerror=0+nightTerror
  updateSam()
  updateOllie()
  updateNoel()
  updateRobin()
  updateKris()
  updateMilan()
  updateAngel()
  updateSantana()
  practiceTime=practiceTime-30
  print("")

def actionFour():
  print("The team practices anaerobic rowing on the water.  Eventually, your teammates are just trying to outdo each other.")
  global teamAddEndurance
  global teamAddPower
  global teamAddFatigue
  global teamAddMorale
  global teamAddRhythm
  global teamAddTechnique
  global teamAddTerror
  global practiceTime
  global tempMentalModifier
  global tempExerciseModifier
  global nightTerror
  tempExerciseModifier=1
  tempMentalModifier=1
  teamAddEndurance = 3*tempExerciseModifier
  teamAddPower = 7*tempExerciseModifier
  teamAddTechnique = 6
  teamAddRhythm = 9
  teamAddMorale = 2*tempMentalModifier
  teamAddFatigue = 20
  teamAddTerror=0+nightTerror

  updateSam()
  updateOllie()
  updateNoel()
  updateRobin()
  updateKris()
  updateMilan()
  updateAngel()
  updateSantana()
  practiceTime=practiceTime-30
  print("")

def actionFive():
  print("The team practices lifting weights.  Blasting music and heavy weights is a good way to spend time.")
  global teamAddEndurance
  global teamAddPower
  global teamAddFatigue
  global teamAddMorale
  global teamAddRhythm
  global teamAddTechnique
  global teamAddTerror
  global practiceTime
  teamAddEndurance = 0
  teamAddPower = 12
  teamAddMorale = 4
  teamAddFatigue = 30

  updateSam()
  updateOllie()
  updateNoel()
  updateRobin()
  updateKris()
  updateMilan()
  updateAngel()
  updateSantana()
  practiceTime=practiceTime-30
  print("")

def actionSix():
  print("The team practices running.  Unfamiliar landscapes pass by as the team runs down the channel.")
  global teamAddEndurance
  global teamAddPower
  global teamAddFatigue
  global teamAddMorale
  global teamAddRhythm
  global teamAddTechnique
  global teamAddTerror
  global practiceTime
  global nightTerror
  teamAddEndurance = 15
  teamAddPower = 0
  teamAddTechnique = 0
  teamAddRhythm = -2
  teamAddMorale = 0
  teamAddFatigue = 14
  teamAddTerror = 3*(nightTerror*2)

  updateSam()
  updateOllie()
  updateNoel()
  updateRobin()
  updateKris()
  updateMilan()
  updateAngel()
  updateSantana()
  practiceTime=practiceTime-30
  print("")

def actionSeven():
  print("The team practices core.  It burns in a good way.")
  global teamAddEndurance
  global teamAddPower
  global teamAddFatigue
  global teamAddMorale
  global teamAddRhythm
  global teamAddTechnique
  global teamAddTerror
  global practiceTime
  teamAddEndurance = 15
  teamAddPower = 0
  teamAddTechnique = 16
  teamAddRhythm = 0
  teamAddMorale = 4
  teamAddFatigue = -8
  teamAddTerror = 0

  updateSam()
  updateOllie()
  updateNoel()
  updateRobin()
  updateKris()
  updateMilan()
  updateAngel()
  updateSantana()
  practiceTime=practiceTime-30
  print("")

def actionEight():
  print("You give a rousing speech about your expectations for the time.  After finishing, you cede the floor for questions.")
  global teamAddEndurance
  global teamAddPower
  global teamAddFatigue
  global teamAddMorale
  global teamAddRhythm
  global teamAddTechnique
  global teamAddTerror
  global practiceTime
  teamAddEndurance = 0
  teamAddPower = 0
  teamAddTechnique = 0
  teamAddRhythm = 0
  teamAddMorale = 25
  teamAddFatigue = -16
  teamAddTerror = -5

  updateSam()
  updateOllie()
  updateNoel()
  updateRobin()
  updateKris()
  updateMilan()
  updateAngel()
  updateSantana()
  practiceTime=practiceTime-30
  print("")

def actionNine():
  print("You give the team a break.  It is much appreciated.")
  global teamAddEndurance
  global teamAddPower
  global teamAddFatigue
  global teamAddMorale
  global teamAddRhythm
  global teamAddTechnique
  global teamAddTerror
  global practiceTime
  teamAddEndurance = 0
  teamAddPower = 0
  teamAddTechnique = 0
  teamAddRhythm = 0
  teamAddMorale = 7
  teamAddFatigue = -36
  teamAddTerror = 2

  updateSam()
  updateOllie()
  updateNoel()
  updateRobin()
  updateKris()
  updateMilan()
  updateAngel()
  updateSantana()
  practiceTime=practiceTime-30
  print("")

def actionInspect():
  print("You watch your teammates.  Which would you like to watch?")
  print("1. Sam")
  print("2. Ollie")
  print("3. Noel")
  print("4. Robin")
  print("5. Kris")
  print("6. Milan")
  print("7. Angel")
  print("8. Santana")
  inspectTarget=input()
  inspectCharacter(inspectTarget)
  input()
  print("")

def inspectCharacter(inspectTarget):
 if inspectTarget == "1":
  inspectSam()
 if inspectTarget == "2":
  inspectOllie()
 if inspectTarget == "3":
  inspectNoel()
 if inspectTarget == "4":
  inspectRobin()
 if inspectTarget == "5":
  inspectKris()
 if inspectTarget == "6":
  inspectMilan()
 if inspectTarget == "7":
  inspectAngel()
 if inspectTarget == "8":
  inspectSantana()


def inspectSam():
 print("You take a look at Sam.")
 print("")
 print("Sam appears to be directing his teammates.")
 print("Tall, strong, and ruddy, they are definitely noticeable even from a distance.")
 print("They always seem to need to be talking about something or other.")
 print("")
 print("They appear ",terrorRating(samTerror))
 print("-----")
 print("Their Power ", (physicalRating(samPower)))
 print("Their Endurance ", (physicalRating(samEndurance)))
 print("Their Technique ", (physicalRating(samTechnique)))
 print("Their Rhythm ", (physicalRating(samRhythm)))
 print("-----")
 print("Sam ", (moraleRating(samMorale)))
 print("Sam ", (fatigueRating(samFatigue)))

def inspectOllie():
 print("You take a look at Ollie.")
 print("")
 print("Ollie is tall, long, and lean.")
 print("They keep their eyes cast down for the most part,")
 print("but whenever they look up you can see a fire of intensity.")
 print("")
 print("They appear ",terrorRating(ollieTerror))
 print("-----")
 print("Their Power ", (physicalRating(olliePower)))
 print("Their Endurance ", (physicalRating(ollieEndurance)))
 print("Their Technique ", (physicalRating(ollieTechnique)))
 print("Their Rhythm ", (physicalRating(ollieRhythm)))
 print("-----")
 print("Ollie ", (moraleRating(ollieMorale)))
 print("Ollie ", (fatigueRating(ollieFatigue)))

def inspectNoel():
 print("You take a look at Noel.")
 print("")
 print("Noel relaxes amongst their teammates.")
 print("They use their jet-black hair to shield their eyes from the sun as they lean back.")
 print("Somehow, they're always whistling a tune.")
 print("")
 print("They appear ",terrorRating(noelTerror))
 print("-----")
 print("Their Power ", (physicalRating(noelPower)))
 print("Their Endurance ", (physicalRating(noelEndurance)))
 print("Their Technique ", (physicalRating(noelTechnique)))
 print("Their Rhythm ", (physicalRating(noelRhythm)))
 print("-----")
 print("Noel ", (moraleRating(noelMorale)))
 print("Noel ", (fatigueRating(noelFatigue)))

def inspectRobin():
 print("You take a look at Robin.")
 print("")
 print("Short and nimble, Robin weaves in amongst the team.")
 print("They're always wearing a new fancy outfit, each more colorful than the last.")
 print("They are always attempting to start a conversation, to mixed success.")
 print("")
 print("They appear ",terrorRating(robinTerror))
 print("-----")
 print("Their Power ", (physicalRating(robinPower)))
 print("Their Endurance ", (physicalRating(robinEndurance)))
 print("Their Technique ", (physicalRating(robinTechnique)))
 print("Their Rhythm ", (physicalRating(robinRhythm)))
 print("-----")
 print("Robin ", (moraleRating(robinMorale)))
 print("Robin ", (fatigueRating(robinFatigue)))

def inspectKris():
 print("You take a look at Kris.")
 print("")
 print("Kris stands away from the team.  Tall and strong, they stand out.")
 print("Dark eyes and close-cropped hair make for an intimidating figure.")
 print("They're still sporting their trademark scowl.")
 print("")
 print("They appear ",terrorRating(krisTerror))
 print("-----")
 print("Their Power ", (physicalRating(krisPower)))
 print("Their Endurance ", (physicalRating(krisEndurance)))
 print("Their Technique ", (physicalRating(krisTechnique)))
 print("Their Rhythm ", (physicalRating(krisRhythm)))
 print("-----")
 print("Kris ", (moraleRating(krisMorale)))
 print("Kris ", (fatigueRating(krisFatigue)))

def inspectMilan():
 print("You take a look at Milan.")
 print("")
 print("Milan is of average build, and is quite wiry.")
 print("Their deep brown hair seems to get in their way.")
 print("You see an unnatural glint in their eyes.")
 print("")
 print("They appear ",terrorRating(milanTerror))
 print("-----")
 print("Their Power ", (physicalRating(milanPower)))
 print("Their Endurance ", (physicalRating(milanEndurance)))
 print("Their Technique ", (physicalRating(milanTechnique)))
 print("Their Rhythm ", (physicalRating(milanRhythm)))
 print("-----")
 print("Milan ", (moraleRating(milanMorale)))
 print("Milan ", (fatigueRating(milanFatigue)))

def inspectAngel():
 print("You take a look at Angel.")
 print("")
 print("Angel is strikingly blonde, of average height, and is relatively unimpressive physically.")
 print("They sport a weary smile, which never seems to leave their face.")
 print("")
 print("They appear ",terrorRating(angelTerror))
 print("-----")
 print("Their Power ", (physicalRating(angelPower)))
 print("Their Endurance ", (physicalRating(angelEndurance)))
 print("Their Technique ", (physicalRating(angelTechnique)))
 print("Their Rhythm ", (physicalRating(angelRhythm)))
 print("-----")
 print("Angel ", (moraleRating(angelMorale)))
 print("Angel ", (fatigueRating(angelFatigue)))

def inspectSantana():
 print("You take a look at Santana.")
 print("")
 print("Tall and muscular, Santana appears the figure of an ideal athlete.")
 print("Their tousled brown hair complements their white tank top nicely.")
 print("Whenever they think you're not looking, they're tossing something in their hand.")
 print("They appear ",terrorRating(santanaTerror))
 print("-----")
 print("Their Power ", (physicalRating(santanaPower)))
 print("Their Endurance ", (physicalRating(santanaEndurance)))
 print("Their Technique ", (physicalRating(santanaTechnique)))
 print("Their Rhythm ", (physicalRating(santanaRhythm)))
 print("-----")
 print("Santana ", (moraleRating(santanaMorale)))
 print("Santana ", (fatigueRating(santanaFatigue)))

def terrorRating(terror):
 if terror < 50:
  return ("excited.")
 if terror >= 50:
  if terror >= 150:
   if terror >= 300:
    if terror >= 500:
     if terror >= 700:
      if terror >= 800:
       if terror >= 900:
        return ("insane.")
       return ("horrified.")
      return("distraught.")
     return("unwell.")
    return("uncomfortable.")
   return ("uneasy.")
  return ("normal.")
  
def physicalRating(physical):
 if physical < 50:
  return ("is exceptionally weak.")
 if physical >= 50:
  if physical >= 150:
   if physical >= 300:
    if physical >= 500:
     if physical >= 700:
      if physical >= 800:
       if physical >= 900:
        return ("is peerless.")
       return ("is impressive.")
      return("is well-known.")
     return("is notable.")
    return("is quite good.")
   return ("is improving.")
  return ("needs work.") 
 
def moraleRating(mental):
 if mental < 50:
  return ("appears completely defeated.")
 if mental >= 50:
  if mental >= 150:
   if mental >= 300:
    if mental >= 500:
     if mental >= 700:
      if mental >= 800:
       if mental >= 900:
        return ("is beaming.")
       return ("wears a nice smile.")
      return("is quite happy.")
     return("appears normal.")
    return("appears somewhat dejected.")
   return ("is hardly focused.")
  return ("is dejected.")

def fatigueRating(tired):
 if tired < 50:
  return ("appears very energetic.")
 if tired >= 50:
  if tired >= 150:
   if tired >= 300:
    if tired >= 500:
     if tired >= 700:
      if tired >= 800:
       if tired >= 900:
        return ("could fall asleep at any moment.")
       return ("is exhausted.")
      return("is exceptionally tired.")
     return("is quite tired.")
    return("is slowing down.")
   return ("is starting to fatigue.")
  return ("is fresh.")

def actionSelect(action):
 if action == "1":
  actionOne()
 elif action == "2":
  actionTwo()
 elif action == "3":
  actionThree()
 elif action == "4":
  actionFour()
 elif action == "5":
  actionFive()
 elif action == "6":
  actionSix()
 elif action == "7":
  actionSeven()
 elif action == "8":
  actionEight()
 elif action == "9":
  actionNine()
 elif action == "0":
  actionInspect()
  
def actionMenu():
 global practiceTime
 print("")
 print("Workouts -----")
 print("1. Erg: Steady State - (" + Fore.GREEN + "++ Endurance + Power " + Fore.RED + "- Morale - Fatigue" + Style.RESET_ALL + ", 30min.)")
 print("2. Erg: Power - (" + Fore.GREEN + "+ Endurance ++ Power " + Fore.RED + "- Morale -- Fatigue" +Style.RESET_ALL+ ", 30min.)")
 print("3. Water: Steady State - (" + Fore.GREEN + "+ Endurance + Technique + Rhythm + Morale " + Fore.RED + "- Fatigue" +Style.RESET_ALL+", 30min)")
 print("4. Water: Power - ("+ Fore.GREEN + "+ Power + Technique + Rhythm + Morale " +Fore.RED+ "-- Fatigue" +Style.RESET_ALL+", 30min)")
 print("5. Weights - (" + Fore.GREEN +"++ Power + Morale "+Fore.RED+"- Rhythm -Fatigue"+Style.RESET_ALL+ ", 30min)")
 print("6. Running - (" + Fore.GREEN +"++ Endurance + Rhythm "+Fore.RED+"- Technique --Fatigue"+Style.RESET_ALL+", 30min)")
 print("7. Core - ("+ Fore.GREEN +"++ Technique + Fatigue + Morale"+Style.RESET_ALL+", 30min.)")
 print("Misc. -----")
 print("8. Speech - ("+ Fore.GREEN +"+++ Morale + Fatigue"+Style.RESET_ALL+", 30min)")
 print("9. Rest - ("+ Fore.GREEN +"++ Fatigue + Morale"+Style.RESET_ALL+", 30min.)")
 print("")
 print("0. Inspect Teammate")
 print("")
 print("What would you like to do?")

def insomniaCalc(terror):
 if terror < 50:
  return (1.5)
 if terror >= 50:
  if terror >= 150:
   if terror >= 300:
    if terror >= 500:
     if terror >= 700:
      if terror >= 800:
       if terror >= 900:
        return (0.3)
       return (0.5)
      return (0.6)
     return (0.8)
    return (1.0)
   return (1.2)
  return (1.4)
 
def teamSleep():
 print("You and your teammates head home to get some rest.")
 global samFatigue
 global ollieFatigue
 global noelFatigue
 global robinFatigue
 global krisFatigue
 global milanFatigue
 global angelFatigue
 global santanaFatigue

 samFatigue=samFatigue-(30*insomniaCalc(samTerror))
 if samFatigue < 0:
  samFatigue=0
 ollieFatigue=ollieFatigue-(30*insomniaCalc(ollieTerror))
 if ollieFatigue < 0:
  ollieFatigue=0
 noelFatigue=noelFatigue-(30*insomniaCalc(noelTerror))
 if noelFatigue < 0:
  noelFatigue=0
 robinFatigue=robinFatigue-(30*insomniaCalc(robinTerror))
 if robinFatigue < 0:
  robinFatigue=0
 krisFatigue=krisFatigue-(30*insomniaCalc(krisTerror))
 if krisFatigue < 0:
  krisFatigue=0
 milanFatigue = milanFatigue-(30*insomniaCalc(milanTerror))
 if milanFatigue < 0:
  milanFatigue=0
 angelFatigue=angelFatigue-(30*insomniaCalc(angelTerror))
 if angelFatigue < 0:
  angelFatigue=0
 santanaFatigue=santanaFatigue-(30*insomniaCalc(santanaTerror))
 if santanaFatigue < 0:
  santanaFatigue=0

def eventTrigger(eventNumber):
 global boatDamage
 global samFatigue
 global ollieFatigue
 global noelFatigue
 global robinFatigue
 global krisFatigue
 global milanFatigue
 global angelFatigue
 global santanaFatigue
 global samTechnique
 global ollieTechnique
 global noelTechnique
 global robinTechnique
 global krisTechnique
 global milanTechnique
 global angelTechnique
 global santanaTechnique
 global samPower
 global olliePower
 global noelPower
 global robinPower
 global krisPower
 global milanPower
 global angelPower
 global santanaPower
 global samEndurance
 global ollieEndurance
 global noelEndurance
 global robinEndurance
 global krisEndurance
 global milanEndurance
 global angelEndurance
 global santanaEndurance
 global samRhythm
 global ollieRhythm
 global noelRhythm
 global robinRhythm
 global krisRhythm
 global milanRhythm
 global angelRhythm
 global santanaRhythm
 global samMorale
 global ollieMorale
 global noelMorale
 global robinMorale
 global krisMorale
 global milanMorale
 global angelMorale
 global santanaMorale
 global samTerror
 global ollieTerror
 global noelTerror
 global robinTerror
 global krisTerror
 global milanTerror
 global angelTerror
 global santanaTerror
 global teamAddEndurance
 global teamAddPower
 global teamAddFatigue
 global teamAddMorale
 global teamAddRhythm
 global teamAddTechnique
 global teamAddTerror 
 global opheliaLove
 global fishInPossession
 global robinQuestEnable
 global robinTerror
 global robinQuestComplete
 if eventNumber==1:
  print("Sam catches a crab while bringing the boat in.")
  print("They swim to the surface, showing off their swimming skill.")
  print("The setting sun reflects well in their deep brown eyes.")
  print("The team has a good laugh at their expense.")
  samPower=samPower-3
  samTerror=samTerror+10
  teamAddMorale=teamAddMorale+10
 if eventNumber==2:
  print("Ollie catches a crab while bringing the boat in.")
  print("They quickly recover their position, climbing back into the boat.")
  print("They take a moment to move their long black hair from their eyes.")
  print("The team has a good laugh at their expense.")
  olliePower=olliePower+5
  ollieTerror=ollieTerror+10
  teamAddMorale=teamAddMorale+10
 if eventNumber==3:
  print("Noel catches a crab while bringing the boat in.")
  print("They laugh it off, and climb back into the boat.")
  print("They take a moment to catch their breath, then continue rowing.")
  print("The team has a good laugh at their expense.")
  noelPower=noelPower-3
  noelTerror=noelTerror+10
  teamAddMorale=teamAddMorale+10
 if eventNumber==4:
  print("Robin catches a crab while bringing the boat in.")
  print("They surface above the water, obviously upset at their nice outfit being soaked.")
  print("They laugh it off, though, and wave to their teammates.")
  print("The team has a good laugh at their expense.")
  robinPower=robinPower-3
  robinTerror=robinTerror+10
  teamAddMorale=teamAddMorale+10
 if eventNumber==5:
  print("Kris catches a crab while bringing the boat in.")
  print("They swiftly climb back into the boat.")
  print("The team has a good laugh at their expense.")
  print("Kris, meanwhile, is glowering.")
  krisPower=krisPower-3
  krisTerror=krisTerror+10
  teamAddMorale=teamAddMorale+10
 if eventNumber==6:
  print("Milan catches a crab while bringing the boat in.")
  print("They look like they're about to shout.")
  print("Even while soaked, their deep brown hair loses none of its luster.")
  print("The team has a good laugh at their expense.")
  milanPower=milanPower-3
  milanTerror=milanTerror+10
  teamAddMorale=teamAddMorale+10
 if eventNumber==7:
  print("Angel catches a crab while bringing the boat in.")
  print("As they surface, the fading sunlight glints off their blond hair.")
  print("They laugh off the sudden crab, smiling all the while.")
  print("The team has a good laugh at their expense.")
  angelPower=angelPower-3
  angelTerror=angelTerror+5
  teamAddMorale=teamAddMorale+10
 if eventNumber==8:
  print("Santana catches a crab while bringing the boat in.")
  print("Taking advantage of the sudden eyes on them, Santana surfaces in a dramatic manner.")
  print("As they emerge from the water, they slick their hair back and draw attention to their now transparent tank top.")
  print("The team has a good laugh at their expense.")
  santanaPower=santanaPower+3
  santanaTerror=santanaTerror+7
  teamAddMorale=teamAddMorale+20
 if eventNumber==9:
  print("Sam wins an impromptu team race.")
  print("They smile and wave to the rest of the team, courteous in victory.")
  print("The rest of the team celebrate Sam's victory.")
  samPower=samPower+12
  samEndurance=samEndurance+12
  samTechnique=samTechnique+12
  samRhythm=samRhythm+12
  samMorale=samMorale+20
 if eventNumber==10:
  print("Ollie wins an impromptu team race.")
  print("They sheepishly look towards the ground.")
  print("The rest of the team celebrate Ollie's victory.")
  olliePower=olliePower+12
  ollieEndurance=ollieEndurance+12
  ollieTechnique=ollieTechnique+12
  ollieRhythm=ollieRhythm+12
  ollieMorale=ollieMorale+20
 if eventNumber==11:
  print("Noel wins an impromptu team race.")
  print("Noel pants after the exertion, extending a hand to wave.")
  print("The rest of the team celebrate Noel's victory.")
  noelPower=noelPower+12
  noelEndurance=noelEndurance+12
  noelTechnique=noelTechnique+12
  noelRhythm=noelRhythm+12
  noelMorale=noelMorale+20
 if eventNumber==12:
  print("Robin wins an impromptu team race.")
  print("They bounce around, obviously incredibly excited.")
  print("The rest of the team celebrate Robin's victory.")
  robinPower=robinPower+12
  robinEndurance=robinEndurance+12
  robinTechnique=robinTechnique+12
  robinRhythm=robinRhythm+12
  robinMorale=robinMorale+20
 if eventNumber==13:
  print("Kris wins an impromptu team race.")
  print("They say nothing, instead surveying the rest of the team.")
  print("The rest of the team celebrate Kris's victory.")
  krisPower=krisPower+12
  krisEndurance=krisEndurance+12
  krisTechnique=krisTechnique+12
  krisRhythm=krisRhythm+12
  krisMorale=krisMorale+20
 if eventNumber==14:
  print("Milan wins an impromptu team race.")
  print("Their eyes light up, and they whisper something to themself.")
  print("The rest of the team celebrate Milan's victory.")
  milanPower=milanPower+12
  milanEndurance=milanEndurance+12
  milanTechnique=milanTechnique+12
  milanRhythm=milanRhythm+12
  milanMorale=milanMorale+20
 if eventNumber==15:
  print("Angel wins an impromptu team race.")
  print("They just continue to smile and wave.")
  print("The rest of the team celebrate Angel's victory.")
  angelPower=angelPower+12
  angelEndurance=angelEndurance+12
  angelTechnique=angelTechnique+12
  angelRhythm=angelRhythm+12
  angelMorale=angelMorale+20
 if eventNumber==16:
  print("Santana wins an impromptu team race.")
  print("They take the opportunity to pose and show off.")
  print("The rest of the team celebrate Santana's victory.")
  santanaPower=santanaPower+12
  santanaEndurance=santanaEndurance+12
  santanaTechnique=santanaTechnique+12
  santanaRhythm=santanaRhythm+12
  santanaMorale=santanaMorale+20
 if eventNumber==17:
  print("The wind picks up.  It'll be harder to work out.")
  teamAddPower=teamAddPower-5
  teamAddEndurance=teamAddEndurance-5
  teamAddRhythm=teamAddRhythm-10
  teamAddTechnique=teamAddTechnique+10
 if eventNumber==18:
  print("The wind picks up.  It'll be harder to work out.")
  teamAddPower=teamAddPower-5
  teamAddEndurance=teamAddEndurance-5
  teamAddRhythm=teamAddRhythm-10
  teamAddTechnique=teamAddTechnique+10
 if eventNumber==19:
  print("The wind picks up.  It'll be harder to work out.")
  teamAddPower=teamAddPower-5
  teamAddEndurance=teamAddEndurance-5
  teamAddRhythm=teamAddRhythm-10
  teamAddTechnique=teamAddTechnique+10
 if eventNumber==20:
  print("The wind picks up.  It'll be harder to work out.")
  teamAddPower=teamAddPower-5
  teamAddEndurance=teamAddEndurance-5
  teamAddRhythm=teamAddRhythm-10
  teamAddTechnique=teamAddTechnique+10
 if eventNumber==21:
  print("The wind picks up.  It'll be harder to work out.")
  teamAddPower=teamAddPower-5
  teamAddEndurance=teamAddEndurance-5
  teamAddRhythm=teamAddRhythm-10
  teamAddTechnique=teamAddTechnique+10
 if eventNumber==22:
  print("The wind picks up.")
  if week <=3:
   print("The sound of the wind in the coastal trees is comforting.")
   teamAddMorale=teamAddMorale+10
   teamAddTerror=teamAddTerror-10
  if week >3:
   print("You hear a voice singing, seemingly from the water.")
   print("It's a beautiful song, but haunting.")
   teamAddTerror=teamAddTerror+10
   if week >6:
    print("A siren calls to you from across the waves.")
    print("You can't see her, but you know she's there.")
    teamAddTerror=teamAddTerror+20
 if eventNumber==22:
  print("A fog descends on the boathouse.")
  teamAddTerror=teamAddTerror+10
  teamAddMorale=teamAddMorale-5
  teamAddEndurance=teamAddEndurance+5
 if eventNumber==23:
  print("A fog descends on the boathouse.")
  teamAddTerror=teamAddTerror+10
  teamAddMorale=teamAddMorale-5
  teamAddEndurance=teamAddEndurance+5
 if eventNumber==24:
  print("A fog descends on the boathouse.")
  teamAddTerror=teamAddTerror+10
  teamAddMorale=teamAddMorale-5
  teamAddEndurance=teamAddEndurance+5
 if eventNumber==25:
  print("A fog descends on the boathouse.")
  teamAddTerror=teamAddTerror+10
  teamAddMorale=teamAddMorale-5
  teamAddEndurance=teamAddEndurance+5
 if eventNumber==26:
  if teamAverageTerror > 400:
   teamAddTerror+=20
   teamAddMorale-=10
   print("Something is floating in the water.")
   print("As you get closer, you can see an eyeball, peeking above the waves.")
   print("It quickly dips back under.")
  if teamAverageTerror <= 400:
   print("Something is floating in the water.")
   print("As you get closer, you can see it's just an empty bottle.")
 if eventNumber==27: 
  print("The water pulls back into the sea.")
  print("It pulls back farther than you ever though possible, before the boat is marooned on a sandbar.")
  boatDamage+=1
  print("Eventually the water pulls in once more, freeing the boat, though damaging it in the process.")
 if eventNumber==28:
  print("A large spider emerges from under one of the riggers, spooking the Robin.")
  print("Santana laughs, and splashes water on it, causing it to fall into the water.")
  teamAddMorale+=5
  teamAddTerror+=5
 if eventNumber==29:
  print("Angel points out a large shadow following the boat during a break.")
  print("Soon enough, the whole team is trying to get a look.")
  print("It turns out to be a harbor seal.")
  teamAddMorale+=15
  teamAddTerror-=5
 if eventNumber==30:
  print("Noel points out a large shadow following the boat during a break.")
  print("Soon enough, the whole team is trying to get a look.")
  print("It disappears before the team can get a good eye on it.")
  teamAddMorale-=15
  teamAddTerror+=25
 if eventNumber==31:
  print("It smells like rotting fish.")
  teamAddEndurance-=5
 if eventNumber==32:
  print("A small sparrow falls out of the sky, into the boat.")
  print("It appears to have died on impact.")
  teamAddMorale-=5
 if eventNumber==33:
  print("A dove lands at the bow of your boat.")
  print("It looks at you with inquisitive, familiar eyes.")
  opheliaLove+=5
 if eventNumber==34:
  print("The waters look sickly today.")
  print("An algae bloom spreads beneath your oars.")
  teamAddFatigue+=10
 if eventNumber==35:
  print("The waters look sickly today.")
  print("Dead fish float to the surface.")
  teamAddFatigue+=30
  teamAddTerror+=15
 if eventNumber==36:
  print("You and your teammates hear the din of a foghorn in the distance.")
  print("Must be a shipping vessel.")
 if eventNumber==37:
  print("You and your teammates hear the din of a foghorn in the distance.")
  print("There are no ships out today.")
  teamAddTerror+=10
 if eventNumber==38:
  print("A log below the surface breaks across your stern.")
  print("Your boat doesn't sink, but comes out worse for wear.")
  boatDamage+=1
 if eventNumber==39:
  print("Weeds choke the skeg.")
  print("Steering is still functional, but you'll have to get that repaired.")
  boatDamage+=1
 if eventNumber==40:
  print("A sudden raincloud opens up above the boathouse.")
  teamAddFatigue+=15
 if eventNumber==41:
  print("A sudden raincloud opens up above the boathouse.")
  teamAddFatigue+=15
 if eventNumber==42:
  print("Nothing out of the ordinary happens.")
 if eventNumber==43:
  print("The sky is choked with clouds.")
  teamAddMorale-=5
  teamAddTechnique+=5
 if eventNumber==44:
  print("...")
  teamAddTerror+=30
 if eventNumber==45:
  print("You and your team are hit with an overwhelming wave of lethargy.")
  teamAddFatigue+=30
 if eventNumber==46:
  print("A misshapen fish flops into the boat.  When no one is looking, you grab it.")
  fishInPossession+=1
 if eventNumber==47:
  print("Two teammates break into an argument.")
  print("You calm them down quick enough, but the damage has been done.")
  teamAddMorale-=10
 if eventNumber==48:
  print("A raven flies overhead.")
 if eventNumber==49:
  print("You can't help but notice, it's a beautiful day.")
  teamAddMorale+=10
 if eventNumber==50:
  print("Someone is watching you from the shoreline.")
  teamAddTerror+=15
 if eventNumber==51:
  if (robinTerror > 300  ):
   if robinQuestComplete == 0:
    robinQuestEnable == 1
    print(Fore.RED)
    print("Robin doesn't look very good today.  You might want to check on them after practice.")
    print(Style.RESET_ALL)
   else:
    print("You watch Robin rowing, and feel proud of them.")
  else:
   print("You feel as if you're doing something right.")
 input()

 





def firstDay():
 teamAddBlock()
 global day
 day=day+1
 global week
 week=1
 if day>7:
  day=1
  week=week+1
 dayOneString = "It is Day {} of Week {}.  It is a nice summer day.".format(day, week)
 print(Fore.CYAN)
 print(dayOneString)
 print(Style.RESET_ALL)
 global practiceTime
 practiceTime = 120
 print("You show up at practice.  Your teammates are there waiting for you.")
 while practiceTime > 0:
  practiceTimeString = "You have {} minutes left of practice".format(practiceTime)
  print(practiceTimeString)
  actionMenu() 
  action=input()
  actionSelect(action)
 if practiceTime == 0:
  print("Everyone begins to pack their things and head home.")
  endEnable=1
 if endEnable==1:
  print(Fore.CYAN + "The sun sets.  It's a new day.")
  print(Style.RESET_ALL)
  print("")
  print("")
  print("")
  teamSleep()
  newDay()

def boatClear():
 global boatAddRhythm
 boatAddRhythm = 0
 global boatAddPower
 boatAddPower = 0
 global boatAddEndurance
 boatAddEndurance = 0
 global boatAddTechnique
 boatAddTechnique = 0
  
def strokeCall(athlete):
 if athlete == "1":
  print("You select Sam as Stroke seat.")
  global boatAddRhythm
  boatAddRhythm = samRhythm
  global samDeny
  samDeny = 1

 if athlete == "2":
  print("You select Ollie as Stroke seat.")
  boatAddRhythm = ollieRhythm
  global ollieDeny
  ollieDeny = 1

 if athlete == "3":
  print("You select Noel as Stroke seat.")
  boatAddRhythm = samRhythm
  global noelDeny
  noelDeny = 1

 if athlete == "4":
  print("You select Robin as Stroke seat.")
  
  boatAddRhythm = robinRhythm
  global robinDeny
  robinDeny = 1

 if athlete == "5":
  print("You select Kris as Stroke seat.")
  
  boatAddRhythm = krisRhythm
  global krisDeny
  krisDeny = 1

 if athlete == "6":
  print("You select Milan as Stroke seat.")
  
  boatAddRhythm = milanRhythm
  global milanDeny
  milanDeny=1

 if athlete == "7":
  print("You select Angel as Stroke seat.")
  
  boatAddRhythm = angelRhythm
  global angelDeny
  angelDeny = 1

 if athlete == "8":
  print("You select Santana as Stroke seat.")
  
  boatAddRhythm = santanaRhythm
  global santanaDeny
  santanaDeny = 1
 

def sevenCall(athlete):
 global samDeny
 global ollieDeny
 global noelDeny
 global robinDeny
 global krisDeny
 global milanDeny
 global angelDeny
 global santanaDeny
 if athlete == "1":
  if samDeny != 1:
   print("You select Sam as Seven seat.")
   global boatAddRhythm
   boatAddRhythm = boatAddRhythm+samRhythm
   samDeny = 1
  else:
   print("Sam is occupied already.  Pick another athlete.")
   athleteSeven=input()
   sevenCall(athleteSeven)

 if athlete == "2":
  if ollieDeny != 1:
   print("You select Ollie as Seven seat.")
   
   boatAddRhythm = boatAddRhythm+ollieRhythm
   ollieDeny = 1
  else:
   print("Ollie is occupied already.  Pick another athlete.")
   athleteSeven=input()
   sevenCall(athleteSeven)
 
 if athlete == "3":
  if noelDeny != 1:
   print("You select Noel as Seven seat.")
   
   boatAddRhythm = boatAddRhythm+noelRhythm
   noelDeny = 1
  else:
   print("Noel is occupied already.  Pick another athlete.")
   athleteSeven=input()
   sevenCall(athleteSeven)

 if athlete == "4":
  if robinDeny != 1:
   print("You select Robin as Seven seat.")
   
   boatAddRhythm = boatAddRhythm+robinRhythm
   robinDeny = 1
  else:
   print("Robin is occupied already.  Pick another athlete.")
   athleteSeven=input()
   sevenCall(athleteSeven)

 if athlete == "5":
  if krisDeny != 1:
   print("You select Kris as Seven seat.")
   
   boatAddRhythm = boatAddRhythm+krisRhythm
   krisDeny = 1
  else:
   print("Kris is occupied already.  Pick another athlete.")
   athleteSeven=input()
   sevenCall(athleteSeven)

 if athlete == "6":
  if milanDeny != 1:
   print("You select Milan as Seven seat.")
   
   boatAddRhythm = boatAddRhythm+milanRhythm
   milanDeny = 1
  else:
   print("Milan is occupied already.  Pick another athlete.")
   athleteSeven=input()
   sevenCall(athleteSeven)

 if athlete == "7":
  if angelDeny != 1:
   print("You select Angel as Seven seat.")
   
   boatAddRhythm = boatAddRhythm+angelRhythm
   angelDeny = 1
  else:
   print("Angel is occupied already.  Pick another athlete.")
   athleteSeven=input()
   sevenCall(athleteSeven)
   
 if athlete == "8":
  if santanaDeny != 1:
   print("You select Santana as Seven seat.")
   
   boatAddRhythm = boatAddRhythm+santanaRhythm
   santanaDeny = 1
  else:
   print("Santana is occupied already.  Pick another athlete.")
   athleteSeven=input()
   sevenCall(athleteSeven)

def sixCall(athlete):
 global samDeny
 global ollieDeny
 global noelDeny
 global robinDeny
 global krisDeny
 global milanDeny
 global angelDeny
 global santanaDeny
 global boatAddPower
 if athlete == "1":
  if samDeny != 1:
   print("You select Sam as Six seat.")
   
   boatAddPower = boatAddPower+samPower
   samDeny = 1
  else:
   print("Sam is occupied already.  Pick another athlete.")
   athleteSix=input()
   sixCall(athleteSix)

 if athlete == "2":
  if ollieDeny != 1:
   print("You select Ollie as Six seat.")
   
   boatAddPower = boatAddPower+olliePower
   ollieDeny = 1
  else:
   print("Ollie is occupied already.  Pick another athlete.")
   athleteSix=input()
   sixCall(athleteSix)
 
 if athlete == "3":
  if noelDeny != 1:
   print("You select Noel as Six seat.")
   
   boatAddPower = boatAddPower+noelPower
   noelDeny = 1
  else:
   print("Noel is occupied already.  Pick another athlete.")
   athleteSix=input()
   sixCall(athleteSix)

 if athlete == "4":
  if robinDeny != 1:
   print("You select Robin as Six seat.")
   
   boatAddPower = boatAddPower+robinPower
   robinDeny = 1
  else:
   print("Robin is occupied already.  Pick another athlete.")
   athleteSix=input()
   sixCall(athleteSix)

 if athlete == "5":
  if krisDeny != 1:
   print("You select Kris as Six seat.")
   
   boatAddPower = boatAddPower+krisPower
   krisDeny = 1
  else:
   print("Kris is occupied already.  Pick another athlete.")
   athleteSix=input()
   sixCall(athleteSix)

 if athlete == "6":
  if milanDeny != 1:
   print("You select Milan as Six seat.")
   
   boatAddPower = boatAddPower+milanPower
   milanDeny = 1
  else:
   print("Milan is occupied already.  Pick another athlete.")
   athleteSix=input()
   sixCall(athleteSix)

 if athlete == "7":
  if angelDeny != 1:
   print("You select Angel as Six seat.")
   
   boatAddPower = boatAddPower+angelPower
   angelDeny = 1
  else:
   print("Angel is occupied already.  Pick another athlete.")
   athleteSix=input()
   sixCall(athleteSix)
   
 if athlete == "8":
  if santanaDeny != 1:
   print("You select Santana as Six seat.")
   
   boatAddPower = boatAddPower+santanaPower
   santanaDeny = 1
  else:
   print("Santana is occupied already.  Pick another athlete.")
   athleteSix=input()
   sixCall(athleteSix)

def fiveCall(athlete):
 global samDeny
 global ollieDeny
 global noelDeny
 global robinDeny
 global krisDeny
 global milanDeny
 global angelDeny
 global santanaDeny
 if athlete == "1":
  if samDeny != 1:
   print("You select Sam as Five seat.")
   global boatAddPower
   boatAddPower = boatAddPower+samPower
   samDeny = 1
  else:
   print("Sam is occupied already.  Pick another athlete.")
   athleteFive=input()
   fiveCall(athleteFive)

 if athlete == "2":
  if ollieDeny != 1:
   print("You select Ollie as Five seat.")
   
   boatAddPower = boatAddPower+olliePower
   ollieDeny = 1
  else:
   print("Ollie is occupied already.  Pick another athlete.")
   athleteFive=input()
   fiveCall(athleteFive)
 
 if athlete == "3":
  if noelDeny != 1:
   print("You select Noel as Five seat.")
   
   boatAddPower = boatAddPower+noelPower
   noelDeny = 1
  else:
   print("Noel is occupied already.  Pick another athlete.")
   athleteFive=input()
   fiveCall(athleteFive)

 if athlete == "4":
  if robinDeny != 1:
   print("You select Robin as Five seat.")
   
   boatAddPower = boatAddPower+robinPower
   robinDeny = 1
  else:
   print("Robin is occupied already.  Pick another athlete.")
   athleteFive=input()
   fiveCall(athleteFive)

 if athlete == "5":
  if krisDeny != 1:
   print("You select Kris as Five seat.")
   
   boatAddPower = boatAddPower+krisPower
   krisDeny = 1
  else:
   print("Kris is occupied already.  Pick another athlete.")
   athleteFive=input()
   fiveCall(athleteFive)

 if athlete == "6":
  if milanDeny != 1:
   print("You select Milan as Five seat.")
   
   boatAddPower = boatAddPower+milanPower
   milanDeny = 1
  else:
   print("Milan is occupied already.  Pick another athlete.")
   athleteFive=input()
   fiveCall(athleteFive)

 if athlete == "7":
  if angelDeny != 1:
   print("You select Angel as Five seat.")
   
   boatAddPower = boatAddPower+angelPower
   angelDeny = 1
  else:
   print("Angel is occupied already.  Pick another athlete.")
   athleteFive=input()
   fiveCall(athleteFive)
   
 if athlete == "8":
  if santanaDeny != 1:
   print("You select Santana as Five seat.")
   
   boatAddPower = boatAddPower+santanaPower
   santanaDeny = 1
  else:
   print("Santana is occupied already.  Pick another athlete.")
   athleteFive=input()
   fiveCall(athleteFive)

def fourCall(athlete):
 global samDeny
 global ollieDeny
 global noelDeny
 global robinDeny
 global krisDeny
 global milanDeny
 global angelDeny
 global santanaDeny
 if athlete == "1":
  if samDeny != 1:
   print("You select Sam as Four seat.")
   global boatAddEndurance
   boatAddEndurance = boatAddEndurance+samEndurance
   samDeny = 1
  else:
   print("Sam is occupied already.  Pick another athlete.")
   athleteFour=input()
   fourCall(athleteFour)

 if athlete == "2":
  if ollieDeny != 1:
   print("You select Ollie as Four seat.")
   
   boatAddEndurance = boatAddEndurance+ollieEndurance
   ollieDeny = 1
  else:
   print("Ollie is occupied already.  Pick another athlete.")
   athleteFour=input()
   fourCall(athleteFour)
 
 if athlete == "3":
  if noelDeny != 1:
   print("You select Noel as Four seat.")
   
   boatAddEndurance = boatAddEndurance+noelEndurance
   noelDeny = 1
  else:
   print("Noel is occupied already.  Pick another athlete.")
   athleteFour=input()
   fourCall(athleteFour)

 if athlete == "4":
  if robinDeny != 1:
   print("You select Robin as Four seat.")
   
   boatAddEndurance = boatAddEndurance+robinEndurance
   robinDeny = 1
  else:
   print("Robin is occupied already.  Pick another athlete.")
   athleteFour=input()
   fourCall(athleteFour)

 if athlete == "5":
  if krisDeny != 1:
   print("You select Kris as Four seat.")
   
   boatAddEndurance = boatAddEndurance+krisEndurance
   krisDeny = 1
  else:
   print("Kris is occupied already.  Pick another athlete.")
   athleteFour=input()
   fourCall(athleteFour)

 if athlete == "6":
  if milanDeny != 1:
   print("You select Milan as Four seat.")
   
   boatAddEndurance = boatAddEndurance+milanEndurance
   milanDeny = 1
  else:
   print("Milan is occupied already.  Pick another athlete.")
   athleteFour=input()
   fourCall(athleteFour)

 if athlete == "7":
  if angelDeny != 1:
   print("You select Angel as Four seat.")
   
   boatAddEndurance = boatAddEndurance+angelEndurance
   angelDeny = 1
  else:
   print("Angel is occupied already.  Pick another athlete.")
   athleteFour=input()
   fourCall(athleteFour)
   
 if athlete == "8":
  if santanaDeny != 1:
   print("You select Santana as Four seat.")
   
   boatAddEndurance = boatAddEndurance+santanaEndurance
   santanaDeny = 1
  else:
   print("Santana is occupied already.  Pick another athlete.")
   athleteFour=input()
   fourCall(athleteFour)

def threeCall(athlete):
 global samDeny
 global ollieDeny
 global noelDeny
 global robinDeny
 global krisDeny
 global milanDeny
 global angelDeny
 global santanaDeny
 if athlete == "1":
  if samDeny != 1:
   print("You select Sam as Three seat.")
   global boatAddEndurance
   boatAddEndurance = boatAddEndurance+samEndurance
   samDeny = 1
  else:
   print("Sam is occupied already.  Pick another athlete.")
   athleteThree=input()
   threeCall(athleteThree)

 if athlete == "2":
  if ollieDeny != 1:
   print("You select Ollie as Three seat.")
   
   boatAddEndurance = boatAddEndurance+ollieEndurance
   ollieDeny = 1
  else:
   print("Ollie is occupied already.  Pick another athlete.")
   athleteThree=input()
   threeCall(athleteThree)
 
 if athlete == "3":
  if noelDeny != 1:
   print("You select Noel as Three seat.")
   
   boatAddEndurance = boatAddEndurance+noelEndurance
   noelDeny = 1
  else:
   print("Noel is occupied already.  Pick another athlete.")
   athleteThree=input()
   threeCall(athleteThree)

 if athlete == "4":
  if robinDeny != 1:
   print("You select Robin as Three seat.")
   
   boatAddEndurance = boatAddEndurance+robinEndurance
   robinDeny = 1
  else:
   print("Robin is occupied already.  Pick another athlete.")
   athleteThree=input()
   threeCall(athleteThree)

 if athlete == "5":
  if krisDeny != 1:
   print("You select Kris as Three seat.")
   
   boatAddEndurance = boatAddEndurance+krisEndurance
   krisDeny = 1
  else:
   print("Kris is occupied already.  Pick another athlete.")
   athleteThree=input()
   threeCall(athleteThree)

 if athlete == "6":
  if milanDeny != 1:
   print("You select Milan as Three seat.")
   
   boatAddEndurance = boatAddEndurance+milanEndurance
   milanDeny = 1
  else:
   print("Milan is occupied already.  Pick another athlete.")
   athleteThree=input()
   threeCall(athleteThree)

 if athlete == "7":
  if angelDeny != 1:
   print("You select Angel as Three seat.")
   
   boatAddEndurance = boatAddEndurance+angelEndurance
   angelDeny = 1
  else:
   print("Angel is occupied already.  Pick another athlete.")
   athleteThree=input()
   threeCall(athleteThree)
   
 if athlete == "8":
  if santanaDeny != 1:
   print("You select Santana as Three seat.")
   
   boatAddEndurance = boatAddEndurance+santanaEndurance
   santanaDeny = 1
  else:
   print("Santana is occupied already.  Pick another athlete.")
   athleteThree=input()
   threeCall(athleteThree)

def twoCall(athlete):
 global samDeny
 global ollieDeny
 global noelDeny
 global robinDeny
 global krisDeny
 global milanDeny
 global angelDeny
 global santanaDeny
 if athlete == "1":
  if samDeny != 1:
   print("You select Sam as Two seat.")
   global boatAddTechnique
   boatAddTechnique = boatAddTechnique+samTechnique
   samDeny = 1
  else:
   print("Sam is occupied already.  Pick another athlete.")
   athleteTwo=input()
   twoCall(athleteTwo)

 if athlete == "2":
  if ollieDeny != 1:
   print("You select Ollie as Two seat.")
   
   boatAddTechnique = boatAddTechnique+ollieTechnique
   ollieDeny = 1
  else:
   print("Ollie is occupied already.  Pick another athlete.")
   athleteTwo=input()
   twoCall(athleteTwo)
 
 if athlete == "3":
  if noelDeny != 1:
   print("You select Noel as Two seat.")
   
   boatAddTechnique = boatAddTechnique+noelTechnique
   noelDeny = 1
  else:
   print("Noel is occupied already.  Pick another athlete.")
   athleteTwo=input()
   twoCall(athleteTwo)

 if athlete == "4":
  if robinDeny != 1:
   print("You select Robin as Two seat.")
   
   boatAddTechnique = boatAddTechnique+robinTechnique
   robinDeny = 1
  else:
   print("Robin is occupied already.  Pick another athlete.")
   athleteTwo=input()
   twoCall(athleteTwo)

 if athlete == "5":
  if krisDeny != 1:
   print("You select Kris as Two seat.")

   boatAddTechnique = boatAddTechnique+krisTechnique
   krisDeny = 1
  else:
   print("Kris is occupied already.  Pick another athlete.")
   athleteTwo=input()
   twoCall(athleteTwo)

 if athlete == "6":
  if milanDeny != 1:
   print("You select Milan as Two seat.")
   
   boatAddTechnique = boatAddTechnique+milanTechnique
   milanDeny = 1
  else:
   print("Milan is occupied already.  Pick another athlete.")
   athleteTwo=input()
   twoCall(athleteTwo)

 if athlete == "7":
  if angelDeny != 1:
   print("You select Angel as Two seat.")
   
   boatAddTechnique = boatAddTechnique+angelTechnique
   angelDeny = 1
  else:
   print("Angel is occupied already.  Pick another athlete.")
   athleteTwo=input()
   twoCall(athleteTwo)
   
 if athlete == "8":
  if santanaDeny != 1:
   print("You select Santana as Two seat.")
   
   boatAddTechnique = boatAddTechnique+santanaTechnique
   santanaDeny = 1
  else:
   print("Santana is occupied already.  Pick another athlete.")
   athleteTwo=input()
   twoCall(athleteTwo)

def bowCall(athlete):
 global samDeny
 global ollieDeny
 global noelDeny
 global robinDeny
 global krisDeny
 global milanDeny
 global angelDeny
 global santanaDeny
 if athlete == "1":
  if samDeny != 1:
   print("You select Sam as Bow seat.")
   global boatAddTechnique
   boatAddTechnique = boatAddTechnique+samTechnique
   samDeny = 1
  else:
   print("Sam is occupied already.  Pick another athlete.")
   athleteBow=input()
   bowCall(athleteBow)

 if athlete == "2":
  if ollieDeny != 1:
   print("You select Ollie as Bow seat.")
   
   boatAddTechnique = boatAddTechnique+ollieTechnique
   ollieDeny = 1
  else:
   print("Ollie is occupied already.  Pick another athlete.")
   athleteBow=input()
   bowCall(athleteBow)
 
 if athlete == "3":
  if noelDeny != 1:
   print("You select Noel as Bow seat.")
   
   boatAddTechnique = boatAddTechnique+noelTechnique
   noelDeny = 1
  else:
   print("Noel is occupied already.  Pick another athlete.")
   athleteBow=input()
   bowCall(athleteBow)

 if athlete == "4":
  if robinDeny != 1:
   print("You select Robin as Bow seat.")
   
   boatAddTechnique = boatAddTechnique+robinTechnique
   robinDeny = 1
  else:
   print("Robin is occupied already.  Pick another athlete.")
   athleteBow=input()
   bowCall(athleteBow)

 if athlete == "5":
  if krisDeny != 1:
   print("You select Kris as Bow seat.")
   
   boatAddTechnique = boatAddTechnique+krisTechnique
   krisDeny = 1
  else:
   print("Kris is occupied already.  Pick another athlete.")
   athleteBow=input()
   bowCall(athleteBow)

 if athlete == "6":
  if milanDeny != 1:
   print("You select Milan as Two seat.")
   
   boatAddTechnique = boatAddTechnique+milanTechnique
   milanDeny = 1
  else:
   print("Milan is occupied already.  Pick another athlete.")
   athleteTwo=input()
   bowCall(athleteTwo)

 if athlete == "7":
  if angelDeny != 1:
   print("You select Angel as Two seat.")
   
   boatAddTechnique = boatAddTechnique+angelTechnique
   angelDeny = 1
  else:
   print("Angel is occupied already.  Pick another athlete.")
   athleteTwo=input()
   bowCall(athleteTwo)
   
 if athlete == "8":
  if santanaDeny != 1:
   print("You select Santana as Two seat.")
   
   boatAddTechnique = boatAddTechnique+santanaTechnique
   santanaDeny = 1
  else:
   print("Santana is occupied already.  Pick another athlete.")
   athleteTwo=input()
   bowCall(athleteTwo)

def clearDeny():
 global samDeny
 samDeny=0
 global ollieDeny
 ollieDeny = 0
 global noelDeny
 noelDeny = 0
 global robinDeny
 robinDeny = 0
 global krisDeny
 krisDeny = 0
 global milanDeny
 milanDeny = 0
 global angelDeny
 angelDeny = 0
 global santanaDeny
 santanaDeny = 0

def moraleModifier():
  global samMorale
  global ollieMorale
  global noelMorale
  global robinMorale
  global krisMorale
  global milanMorale
  global angelMorale
  global santanaMorale

 
 
  mental = (samMorale+ollieMorale+noelMorale+krisMorale+milanMorale+angelMorale+santanaMorale)/8

  if mental < 50:
   return (0.4)
  if mental >= 50:
   if mental >= 150:
    if mental >= 300:
     if mental >= 500:
      if mental >= 700:
       if mental >= 800:
        if mental >= 900:
         return (1.5)
        return (1.2)
       return(1.1)
      return(1.0)
     return(0.95)
    return (0.88)
   return (0.7)
  
def fatigueModifier():
  global samFatigue
  global ollieFatigue
  global noelFatigue
  global robinFatigue
  global krisFatigue
  global milanFatigue
  global angelFatigue
  global santanaFatigue

 
 
  fatigue = (samFatigue+ollieFatigue+noelFatigue+krisFatigue+milanFatigue+angelFatigue+santanaFatigue)/8

  if fatigue < 50:
   return (1.0)
  if fatigue >= 50:
   if fatigue >= 150:
    if fatigue >= 300:
     if fatigue >= 500:
      if fatigue >= 700:
       if fatigue >= 800:
        if fatigue >= 900:
         return (0.3)
        return (0.4)
       return(0.5)
      return(0.6)
     return(0.7)
    return (0.8)
   return (0.9)
 
def boatScore():
 global boatDamage
 global boatRating
 fatigueModOutput=fatigueModifier()
 moraleModOutput=moraleModifier()
 boatRating=(boatAddEndurance+boatAddPower+boatAddRhythm+boatAddTechnique) * moraleModOutput * fatigueModOutput * (1/(boatDamage+1))


def raceDay():
 print("It's Race Day.")
 print("")
 print("As captain, you need to assemble your boat lineup to maximize performance.")
 print("")
 print("Here is your athlete list:")
 print("1. Sam")
 print("2. Ollie")
 print("3. Noel")
 print("4. Robin")
 print("5. Kris")
 print("6. Milan")
 print("7. Angel")
 print("8. Santana")
 print("")

 global boatAddRhythm
 boatAddRhythm = 0
 global boatAddPower
 boatAddPower = 0
 global boatAddEndurance
 boatAddEndurance = 0
 global boatAddTechnique
 boatAddTechnique = 0

 global samDeny
 samDeny=0
 global ollieDeny
 ollieDeny = 0
 global noelDeny
 noelDeny = 0
 global robinDeny
 robinDeny = 0
 global krisDeny
 krisDeny = 0
 global milanDeny
 milanDeny = 0
 global angelDeny
 angelDeny = 0
 global santanaDeny
 santanaDeny = 0

 print("Who would you like to place in Stroke seat?")
 strokeInput=input()
 strokeCall(strokeInput)
 print("Who would you like to place in Seven seat?")
 sevenInput=input()
 sevenCall(sevenInput)
 print("Who would you like to place in Six seat?")
 sixInput=input()
 sixCall(sixInput)
 print("Who would you like to place in Five seat?")
 fiveInput=input()
 fiveCall(fiveInput)
 print("Who would you like to place in Four seat?")
 fourInput=input()
 fourCall(fourInput)
 print("Who would you like to place in Three seat?")
 threeInput=input()
 threeCall(threeInput)
 print("Who would you like to place in Two seat?")
 twoInput=input()
 twoCall(twoInput)
 print("Who would you like to place in Bow seat?")
 bowInput=input()
 bowCall(bowInput)
 boatScore()
 print(boatRating)
 global compCounter
 global compStarter
 global compIncrement
 CompetitorScore = compStarter + (compIncrement*compCounter)
 if boatRating > CompetitorScore:
  global winCounter
  winCounter=winCounter+1
  winString = "{} is able to secure a win against Newhaven Crew in the local scrimmage.".format(teamName)
  print(winString)
  compCounter=compCounter+1
 if boatRating < CompetitorScore:
  lossString = "Newhaven Crew is once again able to score a win against {} in the local scrimmage.".format(teamName)
  print(lossString)
 if boatRating == CompetitorScore:
  tieString = "It's unprecedented!  Newhaven Crew and {} tie, exactly!".format(teamName)
  global hasAchievementTie
  hasAchievementTie=1
  print(tieString)
 input()

 newDay()

def pillowTalkOphelia():
 randomPillowTalk=random.randint(1,6)

 if randomPillowTalk == 1:
  print("'I need to take you back to the sea, sometime.'")
  print("'I saw a massive whale, just on the horizon.'")
  print("'I think you'd like it.'")
  print("'I love you so much...'")
 if randomPillowTalk == 2:
  print("Ophelia appears to be talking to herself.")
  print("'Now where did I set that book?'")
  print("'I could have sworn I had it in my exhibit.'")
  print("'I should probably look by the docks - that's where it washed up.'")
 if randomPillowTalk == 3:
  print("'Stay away from the docks, my love.'")
  print("'I want us to be able to keep doing this.'")
 if randomPillowTalk == 4:
  print("'You should take me to your boathouse, sometime.'")
  print("'I've heard rumours aout that place...'")
  print("'I doubt any are true, though...'")
 if randomPillowTalk == 5:
  print("'I'm so sleepy...'")
  print("'Hold me closer, will you?'")
  print("'It must be the fog...'")
 if randomPillowTalk == 6:
  print("'I should probably get to sudying.'")
  print("'But I'd much rather stay here with you.'")
  print("'Hold me closer, will you?'")


 
 
def eventDayTwo():
 print("~~~~~~~~")
 print("")
 print("As you direct your team through their workout, you hear an unfamiliar female voice call out.")
 print("'Hey!  You there!  I've been looking for you!'")
 print("- - -")
 print("- What would you like to say? -")
 print("1. 'What do you want?  You're interrupting our practice.'")
 print("2. 'What's up?  What do you need?'")
 print("3. 'Huh?'")
 print("4. 'I'm busy, go away.'")
 global opheliaAuthority
 global opheliaLove
 dialog1=input()
 if dialog1 == "1":
  opheliaLove=opheliaLove+3
  opheliaAuthority=opheliaAuthority+40
  print("You turn and see a girl bounding up to the shore.  She wears modest clothing, a cross necklace, an oddly heavy coat, and wears her brown hair down in curls.")
  print("Her glasses flash in the sunlight, and she looks at you with admiration.")
  print("'I'm sorry, I didn't mean to interrupt.  I just wanted to introduce myself!'")
  print("'My name is Ophelia!  I've lived here my whole life, and take a keen interest in local history.'")
  print("'I'll keep it quick, but if you find anything... interesting... around here, just come see me, okay?'")
 elif dialog1 == "2":
  opheliaLove=opheliaLove+25
  opheliaAuthority=opheliaAuthority+10 
  print("You turn and see a girl bounding up to the shore.  She wears modest clothing, a cross necklace, an oddly heavy coat, and wears her brown hair down in curls.")
  print("Her glasses flash in the sunlight, and she looks at you with a beaming smile.") 
  print("'Hi!  I'm so glad I found you!  My name is Ophelia!'")
  print("'I've lived here my whole life and always had an interest in local history.'")
  print("'I live on the outskirts of town, down by the woods.  If you find anything... interesting... just come see me, okay?'")
 elif dialog1 == "3":
  opheliaLove=opheliaLove+40
  opheliaAuthority=opheliaAuthority+3
  print("You turn and see a girl bounding up to the shore.  She wears modest clothing, a cross necklace, an oddly heavy coat, and wears her brown hair down in curls.")
  print("Her glasses flash in the sunlight, and she looks at you with an understanding smile.")
  print("'Hey!  It's good to catch you.  I'm not being a bother, am I?  My name's Ophelia!'")
  print("'Oh geez, I'm so sorry for intruding!  Anyways, I'm really into local history, so if you find anything... interesting...'")
  print("'Just let me know, okay?")
 elif dialog1 == "4":
  print("You turn to the shore and see a girl, walking away dejected.  You don't get a good look at her.")
 input()

def nightActionMenu():
 print("~~~~~~~~")
 print("Travel -----")
 print("1. Local Museum - 60 min.")
 print("2. Fishing Pier - 60 min.")
 print("3. Park - 60 min.")
 print("4. Boathouse - 60 min. [Partially Implemented]")
 print("Actions -----")
 print("5. Night Walk - 60 min. [Not Implemented]")
 print("6. Study - 60 min. [Not Implemented]")
 print("~~~~~~~~")

def summerVisions():
 visionSelect = random.randint(1,10)
 if visionSelect == 1:
  print("The lights coalesce into a figure.")
  print("Cold and still, the figure rests atop a bed of kelp.")
  print("It rocks back and forth whith the waves, seeminly undisturbed.")
  print("The longer you watch, the more the figure dissolves into lines and shapes, until only the waves remain.")
  input()
 if visionSelect == 2:
  print("The lights coalesce into a swarm of glittering pinpricks of light.")
  print("The swarm glides over the waves, approaching the pier.")
  print("As the miniature stars reach the pier, they blink out of existence, leaving only the dark water.")
  print("Eventually, the moonlight returns to normal.")
  input()
 if visionSelect == 3:
  print("The lights coalesce into the figure of a woman, wrapped in tattered wings.")
  print("As her form moves closer to the dock, the darkness of the waters push in closer and closer.")
  print("Her wings are pressed tighter and tighter to her chest, until she reaches the dock and the lights dissipate.")
  print("You feel a sense of appreciation.")
  global opheliaLove 
  opheliaLove = opheliaLove +10
  input()
 if visionSelect == 4:
  print("The lights coalesce into a reflection of the night sky.")
  print("The stars twinkle and remain for a while before dispersing.")
  print("You feel better.")
  global teamAddTerror
  teamAddTerror=teamAddTerror-20
  input()
 if visionSelect == 5:
  print("The lights coalesce into the figure of what you presume to be a mermaid.")
  print("She beckons to you as she drifts towards the pier.")
  print("As she approaches you, her features stretch and distort, until she is unrecognizable.")
  print("As she disappears beneath the pier, you have the strangest urge to follow her.")
  teamAddTerror=teamAddTerror+20
  input()
 if visionSelect == 6:
  print("The lights try to coalesce into a variety of shapes and patterns.")
  print("None stick around for long.")
  print("You stare at the water for a while.")
  print("It's as hauntingly beautiful as ever.")
  input()
 if visionSelect == 7:
  print("The lights coalesce into what appears to be vaguely fish-like.")
  print("The 'fish' swims around on the surface of the water for a while.")
  print("As it draws closer, its body begins to stretch and deform, until eventually it dissolves into stars.")
  print("The sight disturbs you.")
  teamAddTerror=teamAddTerror+20
 if visionSelect == 8:
  print("The lights coalesce into the tail of a whale.")
  print("The whale swims languidly for a while, before it begins to dissolve into stars.")
  print("The stars spread out like an oil slick on the surface of the water.")
  print("You feel more in touch with the sea.")
 if visionSelect == 9:
  print("The lights coalesce into the figure of a large man.")
  print("He floats atop the waves, bobbing in the water.  He does not move. ")
  print("The bloated figure continues to float for a while, as you watch, transfixed.")
  print("The figure turns its face to look at you.")
  print("- - - - -")
  print("You do not remember what happened after that, but you taste blood in your mouth.")
  print("It's time to leave.")
  input()
  teamAddTerror=teamAddTerror+50
 if visionSelect == 10:
  print("The lights coalesce into a forest of tall coastal pines.")
  print("The pines stand sentinel as you watch.")
  print("A falling pinprick of light descends into the trees, and the trees begin to dissolve and distort.")
  print("The rays of moonlight collect themselves into a shape that vaguely looks like a pair of wings.")
  print("Eventually, the moonlight returns to normal.")
  input()

def fallVisions():
 visionSelect = random.randint(1,10)
 if visionSelect == 1:
  print("The wind coalesces into words in your ear.")
  print("You can hear a gravelly voice whisper in the wind.")
  print("+Ashes to ashes, dust to dust. Sea to sky, to rot and rust.+")
  print("The voice fades as quickly as it arrived, leaving you alone on the pier.")
  input()
 if visionSelect == 2:
  print("The wind coalesces into words in your ear.")
  print("You hear a musical voice on the waves.")
  print("It sings a beautiful tune, but you fail to make out the words.")
  print("Eventually, the tune is drowned out by the wind, leaving your heart oddly empty.")
  global teamAddFatigue
  teamAddFatigue=teamAddFatigue+15
  input()
 if visionSelect == 3:
  print("The wind coalesces into words in your ear.")
  print("A gentle, familiar voice can be heard over the waves.")
  print("'May God the Father who made us, bless us.'")
  print("'May God the Son send his healing among us.'")
  print("As quickly as she is heard, her voice is once again lost to the roaring wind.")
  print("You stand on the dock for a while, watching the lighthouse in the distance.")
  global teamAddTerror
  teamAddTerror=teamAddTerror-10
 if visionSelect == 4:
  print("The wind coalesces into words in your ear.")
  print("You hear eldritch voices and incantations echoing through the wind.")
  print("You can't understand what they're saying, but it unnerves you all the same.")
  teamAddTerror=teamAddTerror+40
 if visionSelect == 5:
  print("The wind coalesces into your ear.")
  print("All you can hear is heavy breathing.")
  print("It sounds far more ancient than anything you could imagine.")
  print("- - - - -")
  print("You don't know how long you've spent on the pier.")
  print("It's time to leave.")
  input()
 if visionSelect == 6:
  print("The wind coalesces into your ear.")
  print("Over the whipping wind, you can hear a sonorous whale call.")
  print("There are no whales left in this area... right?")
  print("You listen for a while longer but the noise does not reappear.")
  input()
 if visionSelect == 7:
  print("The wind coalesces into your ear.")
  print("You can hear the sound of a knife on a chopping block.")
  print("It carries with it the air of a cruel malice.")
  print("The sea begins to smell sickly to you.  It's time to go.")
  input()
 if visionSelect == 8:
  print("The wind blows, like it always has.")
  print("The longer you sit and listen, the less it sounds like the sea.")
  print("In fact, you would swear that it sounds like the wind through pines.")
  print("You have the feeling not all is as it seems.")
  input()
 if visionSelect == 9:
  print("The wind falls silent.")
  input()
  print("...")
  input()
  print("...")
  input()
  print("...")
  input()
  print("It's time to go home.")
  input()
 if visionSelect == 10:
  print("The wind coalesces into a voice in your ears.")
  print("It is your own voice, undeniably, and it whisperes to you.")
  print("You cannot make out what it says.")
  print("It's time to leave.")
  input()


def winterVisions():
 teamTerror=teamAverageTerror
 global fogStrength
 global teamAddPower
 visionSelect=random.randint(1,10)
 if visionSelect == 1:
  if teamTerror < 300:
   print("The fog pulls in close to your chest, cooling to a chill inside your lungs.")
   print("It's a uniquely odd feeling.")
   print("It feels almost as if it's taken something from you.")
   fogStrength=fogStrength+15
   teamAddPower=teamAddPower-7
   print("The fog seems to grow thicker around you.")
   input()
  if teamTerror >= 300:
   print("You can see figures in the fog.")
   print("They float as wraiths, spectres adrift in the gentle currents of the fog.")
   print("As you watch, they draw ever closer, revealing tendrils hidden within their figures.")
   print("Paralyzed, they descend upon you, and a chill reaches your bones.")
   input()
   fogStrength=fogStrength+30
   teamAddPower=teamAddPower-20
 if visionSelect == 2:
  if teamTerror < 200:
   print("The fog pulls in closer, enveloping you in a cool mist.")
   print("Through the fog, you can hear singing in an ethereal, unearthly language.")
   print("I's a beautiful song.  You feel refreshed, having heard it.")
   print("The fog lifts a little.")
   input()
   fogStrength=fogStrength-5
   teamAddEndurance=teamAddEndurance+5
  if teamTerror >= 200:
   print("The fog pulls in closer, enveloping you in a cool mist.")
   print("Through the fog, you hear unearthly singing.")
   print("Despite being in an unfamiliar language, the terror of the song seeps into you.")
   print("The fog grows thicker around you.")
   input()
   fogStrength=fogStrength+10
   teamAddTerror=teamAddTerror+10
 if visionSelect == 3:
  if teamTerror < 600:
   print("The glint of a shooting star shines through the fog.")
   print("It lights up the sky for but a moment, taking some of the fog with it.")
   print("You make a wish.")
   input()
  if teamTerror >= 600:
   print("The sky is illuminated in a sickly green glow, surrounding a streak of peridot light.")
   print("Voices surround you, whispering in unholy tongues as the meteor lights up the heavens.")
   print("Terror settles in your bones, and you cannot help but feel as if something was irreversably changed.")
   global meteorLanded
   meteorLanded = 1
   print("It's time to go home.")
   input()
 if visionSelect == 4:
  if teamTerror < 500:
   print("A metallic smell permeates the sea.")
   print("The water smells like old pennies.")
   print("You still can't see.")
   print("It's time to head home.")
   input()
  if teamTerror >= 500:
   print("The air is filled with the scent of old pennies.")
   print("As you look down, the water flows red with blood.")
   print("You can't tell where the blood is coming from.")
   print("The blood-fumes feel rejuvanating in your lungs.")
   teamAddTerror=teamAddTerror+30
   teamAddEndurance=teamAddEndurance+30
   input()
 if visionSelect == 5:
  if teamTerror < 300:
   print("A sonorous whale call echoes through the fog.")
   print("And yet?  There are no whales in Watson' Harbor.")
   print("And whale calls can't be heard above water.")
   print("You feel unnerved.")
   teamAddTerror=teamAddTerror+3
   input()
  if teamTerror >= 300:
   print("A haunting whale call echoes over the horizon.")
   print("A hulking shape can be seen through the fog, illuminated by the lighthouse.")
   print("The air feels thick, like water.")
   print("It fills your lungs, leaving you a coughing, sputtering mess on the wooden pier.")
   teamAddEndurance=teamAddEndurance-5
   print("It's time to go home.")
   input()
 if visionSelect == 6:
  if teamTerror < 100:
   print("The fog lifts around you.")
   print("The stars twinkle up above, in a comforting light.")
   print("Despite the cold, you sit for a while and enjoy the beauty of it.")
   teamAddMorale=teamAddMorale+20
   input()
  if teamTerror >= 100:
   print("The fog lifts for a moment.")
   print("You see the stars above you, but they flicker in new constellations unknown to you.")
   print("They arrange themselves in shifting patterns as you watch on.")
   print("The more you watch, the more the patterns connect in your mind.")
   teamAddTerror=teamAddTerror+20
   teamAddTechnique=teamAddTechnique+20
   input()
 if visionSelect == 7:
  if teamTerror < 700:
   print("You sit on the pier and let the fog surround you.")
   print("Beneath the waves, a group of luminescent deep-sea fish come up to the surface to feed.")
   print("They flit about, searching for morsels of food, free from their local predators.")
   print("Eventually, they sink back below the waves.")
   input()
  if teamTerror >= 700:
   print("As you stand on the edge of the pier, you feel your eyes pressing into your skull.")
   print("Beneath the wave, streaks of yellow light grow closer and closer to the surface.")
   print("As you watch on in horror, the lights rise above the surface of the water.")
   print("They coalesce into eyes; eyes of a great and ancient beast, something unknowable and forgotten.")
   print("The creature stares at you for what feels like hours, before slinking back below the waves.")
   teamAddTerror=teamAddTerror+50
   global beingEncountered
   beingEncountered=1
   input()
 if visionSelect == 8:
  if teamTerror < 300:
   print("A foghorn sounds in the distance.")
   print("No doubt a fishing vessel, out to late on dark seas.")
   print("You wonder what there is to catch at night.")
   input()
  if teamTerror >= 300:
   print("You hear the lonesome whine of a foghorn in the distance.")
   print("As the lights of the boat draw closer, you notice the light is somehow wrong.")
   print("The lighthouse beam passes over the vessel, revealing the silhouette of a massive fish.")
   print("The fish then dives below the surface.")
   input()
 if visionSelect == 9:
  if teamTerror < 500:
   print("The air is salty.")
   print("The salt coats your skin, your clothes, your tongue.")
   print("You feel it dry you out, like jerky in the sun.")
   print("You feel tougher, more durable, like sailors of old.")
   teamAddEndurance=teamAddEndurance+30
   input()
  if teamTerror >= 500:
   print("The air is salty.")
   print("The salt coats your skin, your clothes, your tongue.")
   print("You feel it dry you out, like jerky in the sun.")
   print("It sinks into your skin, ever dyer, ever dryer.")
   print("You have never been more parched in your life.")
   print("It burns, so wonderfully terribly.")
   print("Eventually, you come to.  You feel stronger.")
   teamAddEndurance=teamAddEndurance+60
   teamAddTerror=teamAddTerror+40
   input()
 if visionSelect == 10:
  if teamTerror < 400:
   print("Below you on the pier, you see a small octopus glide by.  It looks at you for a moment.")
   print("You can see the intelligence in its eyes.")
   print("Just as quickly, it disappears into the black.")
   print("You feel better.")
   teamAddTerror=teamAddTerror-10
   input()
  if teamTerror >= 400:
   print("The water below the pier roils, as if agitated by some great creature.")
   print("It calms down once more, and as you stare, a single tentacle peers out.")
   print("It pokes around inquisitively, as if looking around the area.")
   print("Eventually, it sinks below the waves, leaving only a dead malformed fish where it once way.")
   global fishInPossession
   fishInPossession=fishInPossession+1
   input()



def fishermenDialogue():
 global fishermenRep
 print("~~~~~~~~~")
 print("The fishermen are gathered in a large group.")
 print("Some smoke cigarettes as they wait around for the next boat to come in.")
 print("------")
 print("What would you like to say?")
 print("1. How's the harvest been?")
 print("2. How's the water?")
 print("3. Have you... y'know, seen anything out there?")
 print("4. What can I do with any fish I find?")
 fishermenResponse = input()
 if fishermenResponse == "1":
  fishermenRep=fishermenRep+15
  if week <= 3:
   print("'Weather's been good lately.  Been light out for longer, too.'")
   print("'We can still snag some yellowfin for a while, so we've mainly been looking for that.'")
   print("'Overall, a good season.'")
   input()
  if week > 3:
   print("'With the fog rolling in, it's getting harder.'")
   print("'Hard to stay out late, hard to deal with the cold...'")
   print("'Hard to deal with everything else.'")
   print("'It's a hard job, but someone has to do it.'")
   input()
 if fishermenResponse == "2":
  if week <=3:
   print("'Water's been calm, about as calm as it can be during the summer.'")
   print("'No complaints on our end, I guess.'")
   print("'It can be plenty nice out.'")
   fishermenRep=fishermenRep+20
   input()
  if week > 3:
   print("The fishermen look at you, and then at the ground.")
   print("It's silent for a while.")
   print("It's clear they don't want to talk about it.")
   input()
 if fishermenResponse == "3":
  print("'Yeah, you see things on the water.'")
  print("'You're never sure exactly what's real and what isn't.'")
  print("The fisherman looks at the ground for a while.")
  print("You can tell he doesn't want to talk about it.")
  input()
 if fishermenResponse == "4":
  print("'Take them to old Foster in his stall.'")
  print("'He doesn't offer much in the way of money, but his advice is always helpful.'")
  input()






def actionTwoN():
 global fishInPossession
 global nightTime
 global teamAddEndurance
 global teamAddPower
 global teamAddFatigue
 global teamAddMorale
 global teamAddRhythm
 global teamAddTechnique
 global teamAddTerror 
 nightTime=nightTime-60
 print("You make your way to the fishing pier.")
 print("Sailboat masts clink together gently, and you hear the lapping of the waves against the stones below.")
 if week > 0:
  if week > 3: 
   if week > 6:
    print("The sodium lamps cut through the fog.  The lighthouse sweeps through the sky.")
   print("The wind cuts through your clothing, leaving you shivering.")
  print("The moon reflects off the waves below.   It's quite beautiful.")
 print("Despite the late night, boats are still present on the dock, unloading their catch.")
 print("A few figures are present, milling about on the docks.  You recognize them, having seen their boats during practice.")
 print("~~~~~~~~")
 print("What would you like do to?")
 print("1. Walk out onto the pier.")
 print("2. Approach the fishermen.")
 print("3. Make your way below the pier.")
 print("4. Approach the Fishmonger's stall.")
 actionInput=input()
 if actionInput == "1":
  if week > 0:
   print("The lights are dimmer out here.")
   print("The moonlight is brighter, and the waves are higher.")
   print("You can almost make out patterns in scattered light on the waves.")
   input()
   summerVisions()
   if week > 3:
    print("It's dark out here.  The lights from the pier do their best to cut through the night, but not fully.")
    print("The wind cuts through your coat and howls in your ear.")
    print("You can almost make out words in the screaming wind.")
    fallVisions()
    if week > 6:
     print("The fog surrounds you.")
     print("Only the light from the lighthouse can be seen out here.")
     print("The tendrils of the fog surround you, creeping in closer.")
     winterVisions()
 if actionInput == "2":
  print("The fishermen scowl at you as you approach.")
  global fishermenRep
  if fishermenRep == 0:
   print("One of the fishermen call out to you as they notice your arrival.")
   print("'And who the fuck are you?'")
   print("'What are you doing here?'")
   print("How would you like to respond?")
   print("1. I'm "  +name+ ", I run the crew team around here.")
   print("2. None of your fucking business.")
   print("3. Just saying hi, is all.")
   print("4. Oh, I'm just going now, I'm sorry.")
   discInput = input()
   if discInput == "1":
    fishermenRep=fishermenRep+30
    print("'Oh, I've heard about you.  Apparently, we've been doing better with you in charge.'")
    print("'Well, it's good to finally meet you.  What do you need?'")
    input()
    fishermenDialogue()
   if discInput == "2":
    fishermenRep=fishermenRep+40
    print("The fishermen laugh uproariously.")
    print("'Shit!  You've got some balls walking in here and talking like that.'")
    print("'I like it!  What can we help you with?'")
    input()
    fishermenDialogue()
   if discInput == "3":
    fishermenRep=fishermenRep+10
    print("'Just saying hi?  You serious?'")
    print("The fisherman is incredulous when he sees you are serious.")
    print("His tone softens.")
    print("'Well, I guess you are polite.  What do you need?'")
    input()
    fishermenDialogue()
   if discInput == "4":
    fishermenRep=fishermenRep+1
    print("'Hmph.  Going so soon?'")
    print("'I though we were going to get acquinted first!'")
    print("You hear the fishermen guffaw behind you.")
    input()
  if fishermenRep > 0:
   print("'Hmph.  You again.'")
   print("The fishermen leer at you from their congregation.")
   print("'What do you want?'")
   print("")
   fishermenDialogue()
 if actionInput == "3":
  print("You find a rocky outcropping and descend beneath the pier.")
  print("The sand here is soft, and makes a nice place to relax.")
  print("Sea life gathers near the water's edge in tidepools.")
  print("- - - - -")
  print("What would you like to do?")
  print("1. Relax on the sand")
  print("2. Go tidepooling")
  beachInput=input()
  global artifactInPossession
  global fishInPossession
  if beachInput == "1":
   print("You relax under the pier.")
   print("The rhythmic sound of the waves helps you get some rest.")
   print("After an hour, it's time to leave.")
   teamAddFatigue=teamAddFatigue-20
   input()
  if beachInput == "2":
   print("You search the beaches for anything that may have washed up.")
   tidepoolItems=random.randint(1,10)
   if tidepoolItems == 1:
    if artifactInPossession == 0:
     if foundHarpoon == 0:
      artifactInPossession = 1
      print("You come across the sharpened barb of a whaling harpoon.")
      print("You gingerly place it in your pocket.  Ophelia will want to see this.")
      global harpoonArtifact
      harpoonArtifact=1
      input()
     if foundHarpoon == 1:
      print("You run across the place you found the harpoon fragment.")
      print("The indent in the sand is mysteriously still there.")
      input()
    if artifactInPossession == 1:
     print("You have a feeling that holding on to an artifact is bad luck.")
     print("You should take it to Ophelia.")
     input()
   if tidepoolItems == 2:
    print("While searching the tidepools, you see a fish flopping on the beach.")
    print("Upon closer inspection, you can see it's twisted and warped.")
    print("You may want to hold on to this one.  Someone might be interested.")
    fishInPossession=fishInPossession+1
    input()
   if tidepoolItems == 3:
    print("While searching the tidepools, you see a fish flopping on the beach.")
    print("Upon closer inspection, you can see it's twisted and warped.")
    print("You may want to hold on to this one.  Someone might be interested.")
    fishInPossession=fishInPossession+1
    input()
   if tidepoolItems > 3:
    print("You scan the tidepools, but find nothing out of the ordinary.")
    print("It's probably time to go.")
    input()
 if actionInput == "4":

  print("You make your way to the Fishmonger's Stall.")
  print("Fishmonger Foster cuts up a small tuna on a bloody table as you approach.")
  print("The thin and lanky figure leans over the counter, the light behind him shrouding his features.")
  print("<What are you here for?  Come to purchase, or deliver?>")
  print("- - - - -")
  print("What would you like to say?")
  print("1. What kind of fish do you buy here?")
  print("2. Who buys, mostly?")
  print("3. I'm here to drop off some fish.")
  fishmongerInput = input()
  if fishmongerInput == "1":
   print("<I have more than enough... mundane.. fish, if you will.>")
   print("<From you?  I'm only buying anything out of the ordinary.>")
   print("<You'll know them when you see them.>")
   input()
  if fishmongerInput == "2":
   print("Foster stares at you a moment.")
   print("<You know I can't tell you that.>")
   input()
  if fishmongerInput == "3":
   
   if fishInPossession == 0:
    
    print("<You don't have any fish.  I can't give you anything.>")
   if fishInPossession > 0:
    fishInPossession=fishInPossession-1
    print("<In exchange for that fish, how about I teach you some things?>")
    print("<Foster whispers a few incantations over the fish, as he extracts the heart from the body.>")
    teamAddTerror=teamAddTerror+30
    skillRoulette=random.randint(1,4)
    if skillRoulette == 1:
     teamAddPower=teamAddPower+30
     print("You feel more powerful.")
    if skillRoulette == 2:
     print("You feel tougher.")
     teamAddEndurance=teamAddEndurance+30
    if skillRoulette == 3:
     print("You feel more in sync.")
     teamAddRhythm=teamAddRhythm+30
    if skillRoulette == 4:
     print("You feel more dextrous.")
     teamAddTechnique=teamAddTechnique+30
    input()


     



def actionOneN():
 global opheliaLove
 global opheliaAuthority
 global nightTime
 global harpoonArtifact
 global artifactInPossession
 global foundCoin
 global coinArtifact
 global featherArtifact
 global foundFeather
 global arrowheadsInPossession
 nightTime=nightTime-60
 print("You make your way through the darkening town to a small, run-down house on the exterior of town.")
 print("The crows congregate around the roof of the house, fending off the encroaching seagulls.")
 print("An obviously home-made banner is draped haphazardly across the front porch:")
 print("'Local History Museum'")
 print("")
 print("Ophelia steps out into the porchlight, glasses glinting.")
 greetingEnable=1
 if opheliaLove == 0:
  print("She scowls.")
  print("'Hmph.  What do you want?'")
 if opheliaLove > 0:
  if opheliaLove > 50:
   if opheliaLove > 150:
    if opheliaLove > 250:
     if greetingEnable == 1:
      print("'"+name+"!  It's so good to see you...'")
      print("'It's so late!  Come in!")
      print("'Did you bring something for me...?'")
      greetingEnable = 0
    if greetingEnable == 1:
     print("'Oh!'  She averts her gaze to the ground.")
     print("It's, uhm, it's good to see you again?'")
     print("'What... what brings you by?  Did you need to see me?'")
     greetingEnable = 0
   if greetingEnable == 1:  
    print("She beckons for your attention.")
    print("'Hey, it's good to see you again!'")
    print("'Have you brought something for me?'")
    greetingEnable = 0
  if greetingEnable == 1:  
   print("She calls out to you.")
   print("'What brings you around here?'")
   print("'Do you have something for me?'")
   greetingEnable = 0
 print("~~~~~~~~")
 print("What would you like to say?")
 print("1. I just wanted to check in on you.  How are you doing?")
 print("2. Can you give me a tour of your exhibits?")
 print("3. Can you tell me anything about local history?")
 print("4. Tell me about yourself.")
 print("5. Let's just hang out a while.")
 print("6. Can you take a look at this artifact I found?")
 print("7. Can you tell me about those artifacts I brought you?")
 print("8. I brought you some arrowheads!")
 print("")
 print("9. Close")
 print("~~~~~~~~")
 actionInput=input()
 if actionInput=="1":
  opheliaLove=opheliaLove+15
  opheliaAuthority=opheliaAuthority+8
  print("Ophelia turns to you and her eyes light up.")
  if week > 0:
   if week > 3:
    if week > 9:
     print("'Winter is a hard time here in Watson's Harbor.  It's so dark out, lately.  Lonely, too.'")
     print("'Will you stay a bit longer with me?  I could really use that.'")
     print("'Winter is never a good time for me.'")

    print("'It's starting to get colder!  I love the chill in the air...'")
    print("'I think autumn is my favorite season to be honest, it's just so beautiful out.")
    print("'The seagulls are coming in from the sea, though.")
    print("I just enjoy my walks this season.")
    
   print("'The end of summer is always really nice for exploring and searching for different artifacts!'")
   print("'Most recently, I came across an interesting collection of arrowheads!'")
   print("'I really enjoy how light it is out lately - when it gets dark it's a lot less fun.'")
   print("'Overall, I've been having a great time lately!  Thank you for asking!'")
   input()
 if actionInput=="2":
  opheliaLove=opheliaLove+20
  print("'You'd really like to see the exhibits?'")
  print("Ophelia blushes at your suggestion.")
  print("'Follow me!'")
  print("Ophelia rushes off into the cluttered museum/house.")
  print("She gestures towards a glass case, containing a multitude of obsidian and granite arrowheads.")
  print("'These are my arrowheads!  I found every one of them searching in the woods.  If you find any more, give me a call!'")
  print("'Would you like to keep going?'")
  print("~~~~~~~~")
  print("1. Of course!")
  print("2. No, I'm sorry, it's getting late.")
  print("3. I'm sorry, this has been a terrible waste of my time.  Goodnight.")
  museumSelect = input()
  if museumSelect == "1":
   print("'Great!'")
   print("Ophelia grabs your hand and ushers you towards a rusty hunk of iron leaning against a wall.  It looks mean, and under the rust...")
   print("You could swear it was stained with blood.")
   print("'This here is an old harpoon, back from Watson's Harbor's whaling days!'")
   print("'Some say this harpoon was wielded by Ezekiel Watson himself to bring in a massive bowhead whale!'")
   print("Looking at the thing disturbs you.  You quickly move along.")
   print("Ophelia pulls you to the next exhibit, a massive fishing rod placed on a table.  Likely, it is over 12 feet long.")
   print("The rod itself is caked in sand and rust.")
   print("'I like this one a lot!  I found it on the beach after a storm - had a really hard time bringing it back home.'")
   print("'For the life of me, I can't figure out what it's for!'")
   print("'Let's keep moving!'")
   input()
   print("You approach a container of varied bits of sea glass.  Some pieces of fine pottery, softened by the sea, are present.")
   print("'Did you know all the glass on the beach all came from one shipwreck off the coast in 1845?'")
   print("'It was carrying a load of bottles and china, which shattered and now the shards gradually float to shore, softened by the sea!'")
   print("Ophelia leads you to a glass case mounted on the wall.")
   print("Inside the case lies the skeleton of a fish.")
   print("However, the fish appears malformed, with twisted bones and a singular eye socket.")
   print("Ophelia says nothing, simply staring at the case.")
   print("The two of you stare silently for a moment, before Ophelia shuffles you out of the room.")
   input()
  if museumSelect == "2":
   opheliaAuthority=opheliaAuthority+10
   opheliaLove=opheliaLove-5
   print("'Oh-'")
   print("'She looks crestfallen.'")
   print("'It is late, you should head home. I'm sorry.'")
  if museumSelect== "3":
   opheliaLove=opheliaLove-20
   opheliaAuthority=opheliaAuthority+20
   print("'Oh -'")
   print("She turns away from you, in an effort to hide her hurt.")
 if actionInput == "3":
  print("'You'd like to learn about local history?'")
  print("Ophelia is beaming.")
  opheliaLove=opheliaLove+30
  print("What would you like to say?")
  print("1. What can you tell me about how the town was founded?")
  print("2. Who was Watson, anyway?")
  print("3. Tell me about Newhaven.")
  print("4. What's the deal with the fishing docks?")
  print("5. What kind of artifacts can you find around here?")
  print("~~~~~~~~")
  historyInput=input()
  if historyInput == "1":
   print("'Oh, you want to know about the start of Watson's Harbor?'")
   print("'Well, it all started in 1846 - Ezekiel Watson and his whaling crew established a settlement here after a particularly good haul.'")
   print("'Industry came soon after, in order to profit off the catch.  Fishing vessels came, too, and eventually a government was formed.'")
   print("'Watson was acting mayor while the town was under construction, and for about 15 years afterwards.'")
   print("'He managed both the town and his whaling fleet until his mysterious death in 1870.'")
   print("'After that, government passed down through a couple other figureheads, until a city council was made, and things stabilized.'")
   print("'Was that all you wanted to know?'")
   input()
  if historyInput == "2":
   print("'You want to know about Ezekiel Watson?'")
   print("'What can I say...  Watson was an odd fellow.'")
   print("'Namesake of the town, obviously, and founded it with his whaling band in 1846.'")
   print("'He was an imposing figure to say the least - recorded as being over 6 foot 6 and about 300 pounds, he gathered attention anywhere he went.'")
   print("Ophelia withdraws a faded old photo.  It depicts a massive man in a greatcoat, doubtless posing for a photo.")
   print("He holds an equally massive harpoon, bloodied and stained, and wears a crazed look in his eyes.")
   input()
   print("'Even though he was a captain of great fame, Ezekiel Watson was also a shrewd politician.'")
   print("'He somehow managed to attract lots of industrial attention to Watson's Harbor through striking deals with company owners.'")
   print("'Believe it or not, Watson's Harbor was once a hub of industrial activity.'")
   print("'Given the state of things now, that's quite a surprise.'")
   input()
   print("'While Watson was mayor, the town prospered, and its residents enjoyed a nice and easy life.'")
   print("'It went on like that for 15 years, until mysterious events started occuring.'")
   print("'First, a choking fog began to roll into town during the fall and winter.  Even fishing boat lamps couldn't cut through it.'")
   print("'After that, fish started to wash up on the shore.  Twisted, malformed.  Couldn't be sold, and sure couldn't be eaten.'")
   input()
   print("'Later that year, Watson was found, drowned, in the harbor bearing his name.'")
   print("'The best the coroners could gather, he had been dead for several days by the time they found him.'")
   print("'No one really knows how he died, given he was a strong swimmer up until the time of his death.'")
   print("'Is that what you wanted to know?'")
  if historyInput == "3":
   print("'You're curious about Newhaven?  Or do you just want to learn more about your opposition?'")
   print("'Well, Newhaven was established around 1750, as a new colony outpost.  It's been on a relatively consistent uptick since then.'")
   print("'Newhaven always focused on shipping and manufacturing, and it's treated them well since the 1800s.'")
   print("'They did fall on hard times during the 1860s when industry moved out to Watson's Harbor, but they recovered.'")
   print("'We didn't.  Now it's just this.'")
   opheliaAuthority=opheliaAuthority+10
   print("Ophelia looks sour.")
  if historyInput == "4":
   print("Ophelia shudders at the mention of the place.")
   print("'Don't go there.  I like you too much for you to be hanging around with those people.'")
   print("'The fishing docks are where the fishermen like to hang out.  Rough crowd, to be sure.'")
   print("'Not much good fishing, but some of the fishmongers there might be able to reward you for what you find.'")
   input()
  if historyInput == "5":
   print("'You can find plenty of artifacts if you know where to look!'")
   print("'The easiest to find would be arrowheads and sea glass - both very common on the beaches and in the woods.'")
   print("'Other more valuable artifacts happen to wash up now and again - and still more are entirely unaccounted for.'")
   print("'If you find anything interesting, please bring it to me!")
  input() 
 if actionInput == "4":
  print("'You really want to learn more about me...?'")
  opheliaAuthority=opheliaAuthority+15
  opheliaLove=opheliaLove+35
  print("'What would you like to know...?'")
  print("~~~~~~~~")
  print("1. How did you end up in Watson's Harbor?")
  print("2. What got you so interested in local history?")
  print("3. What do you even do all day?")
  print("4. If you weren't here, what would you be doing?")
  print("5. Why did you set up the museum in your house?")
  print("6. Do you get many visitors here?")
  print("7. How'd such a pretty girl like you end up in a place like this?")
  opheliaInput=input()
  if opheliaInput == "1":
   print("'I was born here!  My parents grew up in this house, too!  They still pay for it, as well.'")
   print("'They're off pursuing some business opportunities overseas, and have been for over a year.'")
   print("'And so now I'm here!  Even though it gets really lonely sometimes, I like it.'")
   print("'I spend most of my time tidying the exhibits and doing research at the library.'")
   print("'I could move to Newhaven or elsewhere.  I could even sell the house if I wanted!'")
   print("'But I've built a nice thing here.  I think I'd like to stay.'")
   print("Ophelia trails off as she mumbles to herself.")
   print("You think you catch her saying something about being bound to stay.")
   input()
  if opheliaInput == "2":
   print("'History was always a passion of mine!'")
   print("'When I was growing up here, I'd always be playing down by the beach and find all sorts of little trinkets.'")
   print("'I thought nothing of it at first, but after a while I found more and more.'")
   print("'I began to find some very interesting things, like harpoons and such!'")
   print("'And then I started going to the library, and reading about the town.'")
   print("'I found out some very interesting things, and now we're here!'")
   print("Ophelia gives you a warm smile.")
   print("'Places like here always have more to them then you give them credit.'")
   print("'You're new here, but I hope you come to realize that in time.'")
   input()
  if opheliaInput == "3":
   print("'Oh, I try to keep myself busy!'")
   print("'Idle hands are the devil's playthings, after all!'")
   print("'Most of my day is spent at the local library!  It's really just me in there, mostly.'")
   print("'Their book selection leaves a lot to be desired, but the archives are pretty useful!'")
   print("'When I'm not in the library, I'm here tidying the exhibits.  The work never ends!'")
   print("'On the rare moment's I'm not busy, I'm usually out in the park!'")
   print("'I like watching the ravens!  They're so pretty...'")
   print("Ophelia is beaming.")
   input()
  if opheliaInput == "4":
   print("'If I weren't here in Watson's Harbor...?'")
   print("'Oh, that's a hard question...'")
   print("'Sometimes I find myself wanting to go into the city, maybe Newhaven.'")
   print("'Go to university, study history, settle down with someone...'")
   print("'Sometimes I wish I could do that.'")
   print("'But I'm really very happy here!'")
   input()
  if opheliaInput == "5":
   print("'Having the museum in my house makes things a lot easier for me.'")
   print("'The money is already covered, at minimum, and I don't have enough money to rent a new place.'")
   print("'As well, I can take better care of the exhibits, and make sure they always look their best!'")
   print("'I don't like letting the exhibits out of my sight.'")
   print("'Can never be *too* careful, after all!'")
   print("Ophelia smiles nervously.")
   input()
  if opheliaInput == "6":
   print("'Not many.  Just enough to cover upkeep fees for admission.'")
   print("'But I like you a lot, so you can get in free!'")
   print("'Hopefully you keep coming back, I could use the company...'")
   print("'It does get very lonely out here.")
   print("'As long as I get just enough visitors, it's okay.'")
   print("'More time for research, I say!'")
   input()
  if opheliaInput == "7":
   opheliaLove=opheliaLove+40
   print("Ophelia immediately flushes red.")
   print("'...'")
   print("'You... you really think I'm pretty...?'")
   if opheliaLove > 200:
    print("She runs up and embraces you, planting a kiss on your cheek.")
    print("You feel warm.")
    global teamAddMorale
    global teamAddTerror
    teamAddMorale=teamAddMorale+15
    teamAddTerror=teamAddTerror-15
    print("She eventually releases her grasp, and the two of you laugh together for a moment.")
   else:
    print("She blushes more, and turns away from you.")
    print("After a while of stammering excuses and denials, she reaches out a hand.")
    print("You take it.  You feel warmer.")
    teamAddMorale=teamAddMorale+10
    teamAddTerror=teamAddTerror-10
   input()
 global opheliaEvent
 if actionInput == "5":
  if opheliaLove == 0:
   print("'I really would rather not.'")
 
  if opheliaLove > 0:
   opheliaEvent = 1
   if opheliaLove > 100:
    opheliaEvent = 2
    if opheliaLove > 200:
     opheliaEvent = 3
     if opheliaLove >500:
      opheliaEvent = 4
      if opheliaLove > 650:
       opheliaEvent = 5


  if opheliaEvent == 1:
   opheliaLove=opheliaLove+40
   print("'Oh, sure!  Would you like to help me sort exhibits?'")
   input()
   print("You and Ophelia spend the next hour sorting and organizing exhibits.")
   print("You learn a few things to take back to your team.")
   input()
   global teamAddTechnique
   teamAddTechnique=teamAddTechnique+10

  if opheliaEvent == 2:
    opheliaLove=opheliaLove+50
    print("'I would love to!'")
    print("'Let's go to the park and watch the ravens!'")
    global teamAddPower
    teamAddPower=teamAddPower+10
    input()
    print("You and Ophelia watch the ravens in the park a while.")
    print("They're strikingly beautiful creatures.")
    print("You learn a few things to take back to your team.")
    input()

  if opheliaEvent == 3:
     opheliaLove=opheliaLove+60
     print("'I would love nothing more!'")
     print("'Let's go to the water and hang out, shall we?'")
     input()
     print("You and Ophelia find a rocky outcropping, overlooking the waves.")
     if week > 0:
      if week > 3:
        if week > 6:
         print("Ophelia pulls tight into your side, evidently savoring your warmth.")
         print("The wind howls above you two, and you watch a massive fogbank roll in from the sea.")
         print("'It's so cold out.'")
         print("'Hold me closer, will you?'")
         print("'It's going to be a long winter.")
         print("'You're new here, so I don't think you know what you're in for.'")
         print("'Things happen here, during the winter.'")
         print("'Weird things.  Things I don't have any explanation for.'")
         print("'We're going to be in danger.  I just need you to stay safe.'")
         print("'And do take care of your teammates.  They need you more than ever.'")
         input()

        print("'Ophelia scoots over to sit close to you.'")
        print("'Have you felt the chill in the air?  It's getting closer to winter.'")
        print("Ophelia is quiet for a while.")
        print("She turns to you - her eyes are glistening.")
        print("'Stay safe, okay?  I can't lose you.'")
        input()


     print("Ophelia turns to you.")
     print("'I know summer is ending, but I'm so happy I got to spend it with you.'")
     print("'Things are going to get harder, you know.  Will you stay with me during the winter?'")
     print("'Best not to worry about it now.  Let's stay and enjoy the waves.'")
     input()
  
  if opheliaEvent == 4:
      opheliaLove=opheliaLove+70
      print("'Yes!  Of course!  Do you like baking?  Let's bake an apple pie!'")
      input()
      print("You and Ophelia retreat into the kitchen.")
      print("After an hour of work, your pie is ready!")
      print("It looks delicious, though Ophelia has managed to cover herself in an infeasible amount of flour.")
      print("After taking the pie out of the oven, she pulls you in for a kiss, coating your face in flour too.")
      print("'Hey, you should take ths pie to your team!  I think they'd appreciate it!'")
      print("You learn a few things you can take back to your team.")
      global teamAddFatigue
      teamAddFatigue=teamAddFatigue-30
      teamAddMorale=teamAddMorale+40

  if opheliaEvent == 5:
       print("'I missed you so much!'")
       print("'It's so cold out, let's relax in my room...")
       print("You and Ophelia go into her room.")
       print("It's a small room, occupied mostly by a large, comfortable looking bed.")
       print("The rest is occupied by a massive desk, scattered with maps, books, and writings.")
       print("Her sweaters and other clothing is scattered haphazardly about the room, but she quickly cleans off her bed, and beckons for you to join her.")
       print("As you both lie down on the bed, you start to feel one of Ophelia's hands start to wander.")
       print("~~~~~~~~")
       print("What would you like to do?")
       print("1. Let her continue.")
       print("2. Gently move her hand away.")
       inputCheck=input()
       if inputCheck == "1":
        print("You let Ophelia continue, before turning to her and kissing her passionately.")
        print("Later, the two of you lie in bed next to each other.")
        print("Ophelia turns to you with rosy cheeks, a loving smile painted on her features.")
        print("You hear her mumble something about you being wonderful.")
        print("She continues to mumble to herself, and you swear you can pick out this:")
        print("'I'm so glad you came here.  I didn't think I would ever meet someone so perfect.")
        opheliaLove=opheliaLove+100
        pillowTalkOphelia()
       if inputCheck == "2":
        print("You and Ophelia pore over the scattered maps.")
        print("You tease each other as you review the historical documents, and manage to have plenty of fun.")
        print("You finish off the time by cuddling in bed to save warmth.")

 if actionInput == "6":
  if artifactInPossession == 0:
   print("'I'm sorry, it doesn't look like you have any artifacts for me.'")
  if artifactInPossession == 1:
   if harpoonArtifact == 1:
    harpoonArtifact = 0
    global foundHarpoon 
    foundHarpoon = 1
    artifactInPossession = 0
    print("'Thank you so much!  I'll get this set up in the exhibits immediately.'")
   if coinArtifact== 1:
    coinArtifact = 0
    global foundCoin
    foundCoin=1
    artifactInPossession = 0
    print("'Where did you find this?  I'll get it to the exhibits right away!'")
  if featherArtifact == 1:
   featherArtifact=0
   global foundFeather
   foundFeather=1
   artifactInPossession=0
   print("Ophelia's face falls.  She turns away from you quickly, putting the feather away.")

 if actionInput == "7":
  print("'Which artifact do you want to learn more about?'")
  if foundHarpoon == 1:
   print("1. I'd like to learn about the harpoon.")
  if foundCoin == 1:
   print("2. I'd like to learn about the coin.")
  if foundFeather == 1:
   print("3. I'd like to learn about the feather.")

  artifactInput = input()
  if artifactInput == "1":
   print("Ophelia nods, picking up the rusted hunk of metal.")
   print("'As I'm sure you know, this is a piece of an old whaling harpoon.'")
   print("'Hard to find, as I'm sure you know.'")
   print("'Chances are it broke off during the killing of a whale.'")
   print("'That's about it, I think.'")
   print("- - - - -")
   print("What would you like to say?")
   print("1. Thanks for the history lesson!")
   print("2. I'm sure you know more.  Won't you tell me?")
   print("3. I know that's not it.  Tell me more.")
   harpoonResponse = input()
   if harpoonResponse == "1":
    opheliaLove=opheliaLove+15
    print("'You're welcome, "+name+" !'")
    input()
   if harpoonResponse == "2" or harpoonResponse == "3":
    if opheliaLove>300 or opheliaAuthority>40:
     print("'Yeah.  You're right.  I guess I should tell you.'")
     print("'This shard is a part of Ezekiel Watson's personal harpoon.'")
     print("'How do I know?  Simple, really.'")
     print("Ophelia flashes you a smile.")
     print("'It told me!'")
     print("She holds out the shard, and as it gets closer to you, you hear a faint whispering inside your skull.")
     teamAddTerror=teamAddTerror+20
     print("She puts the shard away.")
     input()
    if opheliaLove<=400 or opheliaAuthority<=50:
     print("'I told you, it's nothing.'")
     print("'Let's just forget it.'")
     input()
  if artifactInput == "2":
    print("Ophelia nods, picking up the tarnished coin.")
    print("'This is a silver coin used during the initial founding of the town.'")
    print("'They used a different currency back then, due to being so isolated.'")
    print("'This was a whaler's one week pay.  Someone must have dropped it.'")
    print("'Nothing much more interesting about this.")
    print("- - - - -")
    print("What would you like to say?")
    print("1. Thanks for the insight!")
    print("2. That's not all, right?")
    print("3. You're hiding something.  Tell me.")
    coinResponse = input()
    if coinResponse == "1":
     opheliaLove=opheliaLove+15
     print("'You're welcome, "+name+" !'")
     input()
    if coinResponse == "2" or coinResponse == "3":
     if opheliaLove > 300 or opheliaAuthority > 40:
      print("'Yeah, you got me.'")
      print("'This coin is... remarkable.'")
      print("She holds up the coin closer to you.  You can see a black scar of corrosion in one of the cracks in the silver.")
      print("'This corrosion isn't chemically viable, or stable, or really anything that can be explained.'")
      print("'It's just... weird.  And I haven't been able to find examples of it anywhere except for certain areas around here.'")
      print("'Anywhere that's exposed to the fog for too long ends up like this.")
      input()
     if opheliaLove <= 250 or opheliaAuthority <= 50:
      print("Like I said, it's nothing.")
      print("Let's talk about something else.")
      input()
  if artifactInput=="3":
   print("Ophelia looks at you, eyes boring into your soul.")
   print("'That one's personal.'")
   input()

 if actionInput == "8":
  if arrowheadsInPossession == 0:
   print("'You must be mistaken!  You don't have any arrowheads on you right now.'")
  if arrowheadsInPossession > 0:
   teamAddMorale=teamAddMorale+(arrowheadsInPossession*20)
   teamAddFatigue=teamAddFatigue-(arrowheadsInPossession*15)
   arrowheadsInPossession=0
   print("'Thank you so much!  I baked some bread for you and your team in exchange!'")
   input()

   
def actionThreeN():
 global artifactInPossession
 global coinArtifact
 global foundCoin
 global arrowheadsInPossession
 global nightTime
 global teamAddEndurance
 global teamAddTerror
 global featherArtifact
 global foundFeather
 nightTime-=60
 print("The park is illuminated by orange lamps.")
 print("An open field with a playground section for the children lies ahead of you, off the main road.")
 print("Tall, old growth evergreen trees frame the park, looming ahead in the darkness.")
 print("No one is out at this time, and the fog is heavy in the park.")
 print("- - - - -")
 print("What would you like to do?")
 print("1. Search the park")
 print("2. Take a walk")
 print("3. Approach the playground")
 print("4. Enter the forest")
 print("5. Rest in the park")
 print("")
 actionInput=input()
 if actionInput=="1":
  print("You walk through the field and the forest edge, searcing for any lost objects.")
  parkItems=random.randint(1,10)
  print(parkItems)
  if parkItems==1:
   if artifactInPossession == 1:
    print("You have a feeling carrying an artifact is bad luck.")
    print("You should take it to Ophelia.")
   if artifactInPossession == 0:
    if foundCoin == 0:
     print("You find a tarnished silver coin.")
     print("It looks very, very old.")
     print("Perhaps Ophelia would want to take a look at it.")
     coinArtifact = 1
     artifactInPossession =1
    if foundCoin == 1:
     print("You find nothing of note.")
   input()
  if parkItems ==2 or parkItems ==3:
   print("You find a hewn obsidian arrowhead by the trail.")
   print("It looks important.")
   arrowheadsInPossession=arrowheadsInPossession+1
   input()
  if parkItems >3:
   print("You find nothing of note.")
 if actionInput =="2":
  global teamAddMorale
  print("You take a relaxed walk around the park.")
  print("It's misty out, but the lamps cut through it well enough.")
  print("You feel better.")
  teamAddMorale=teamAddMorale+20
 if actionInput == "3":
  print("You walk into the mist, heading in the direction of the playground.")
  print("The woodchips are damp, and the steel is rusty, but the playground evidently still gets used.")
  print("What would you like to do?")
  print("- - - - -")
  print("1. Relax in the park")
  print("2. Swing on the swingset")
  print("3. Smoke a cigarette")
  parkInput=input()
  if parkInput == "1":
   print("You take a seat on some of the steel playground equipment.")
   print("The mist hugs tighter to you as you relax.")
   print("At least the light works.")
   global teamAddFatigue
   teamAddFatigue=teamAddFatigue-5
   input()
  if parkInput == "2":
   print("Even though it's pitch-black out, you find a seat on the old, creaking swing.")
   print("You slowly start swinging, picking up in pace.")
   print("You find yourself having a good time.")
   teamAddMorale+=15
   teamAddEndurance+=5
   input()
  if parkInput== "3":
   print("You pull a cigarette from your pocket and light it.")
   print("You take a drag.  The pilot light shines through the dark.")
   teamAddTerror-=15
   input()
 if actionInput == "4":
  print("You walk towards the forest.")
  print("The looming trees grow closer and closer, until they obscure even the night sky.")
  print("The forest is hushed and quiet tonight, and the mist hangs low to the ground.")
  print("What would you like to do?")
  print("- - - - -")
  print("1. Search the clearing")
  print("2. Follow the light")
  forestInput=input()
  if forestInput == "1":
   searchResult=random.randint(1,10)
   if searchResult==1:
    if artifactInPossession == 1:
     print("You have a feeling carrying an artifact is bad luck.")
     print("You should take it to Ophelia.")
    if artifactInPossession == 0:
     if foundFeather == 1:
      print("You find nothing of note.")
     if foundFeather == 0:
      print("You find a pure white feather, far too large for any bird.")
      print("It looks almost ethereal.")
      print("Perhaps Ophelia would want to take a look at it.")
      featherArtifact = 1
      artifactInPossession =1
   if searchResult >1:
    print("You find nothing of note.  You feel like something is watching you.")  
   input()
  if forestInput=="2":
   print("You don't feel ready to follow the light.")
   print("[TO BE INTRODUCED]")
  input()
 if actionInput=="5":
  print("The mist hugs you closer as you sit down and rest.")
  teamAddEndurance+=10
  print("It's relaxing here.  It's a nice break.")
 

def actionFourN():
  global nightTime
  global boatDamage
  global teamAddTechnique
  global teamAddFatigue
  nightTime-=60
  print("The boathouse is quiet now, the team already having gone home.")
  print("The chain-link fence is rusted and cool to the touch.")
  print("The gentle clinking of sailboat masks can be heard.")
  print("Inside, the shells sit in dead silence.")
  if robinQuestEnable == 1:
   print("As you flick the lights on, you notice Robin in the corner.")
   print("They evidently want to talk to you.")
  print("What would you like to do?")
  print("- - - - -")
  print("1. Repair the shell")
  print("2. Rest")
  if robinQuestEnable == 1:
   print("7. Talk to Robin")
  boathouseInput=input()
  if boathouseInput == "1":
   boatDamage-=1
   if boatDamage < 0:
    print("There is no damage to repair.")
    boatDamage=0
   else:
    if boatDamage > 0:
      print("You repair some of the damage, but there is more to do.")
    else:
     print("You fully repair the boat.")
  if boathouseInput == "2":
   print("You feel more well rested.  It feels safe here.")
   teamAddFatigue-=10
   teamAddTechnique-=10
  

  if boathouseInput == "7":
   print("What would you like to say to Robin?")
   print("FEATURE NOT IMPLEMENTED")

   
   
   
   

def nightActionSelect(action):
 if action == "1":
  actionOneN()
 elif action == "2":
  actionTwoN()
 elif action == "3":
  actionThreeN()
 elif action == "4":
  actionFourN()
 elif action == "5":
  print("actionFiveN()")
 elif action == "6":
  print("actionSixN()")


def night():
 global nightTime
 nightTime=120
 print("~~~~~~~~")
 print("The sun has long since set, and you find yourself alone on the streets of Watson's Harbor.")
 while nightTime > 0:
  nightTimeString = "You have {} minutes left before you need to head home.".format(nightTime)
  print(nightTimeString)
  print("What would you like to do?")
  nightActionMenu()
  nightAction=input()
  nightActionSelect(nightAction)
  nightEndEnable=1
 if nightTime < 0:
  teamAddFatigue=teamAddFatigue+30
  print("")
  print("You stayed out too late.")
  print("You feel tired.")
  print("")
 if nightTime == 0:
  if nightEndEnable == 1:
   print("You head home and go to sleep for the night.")
   nightEndEnable=0
   newDay()


def newDay():

 eventDeny=0
 global eventPicker
 global practiceTimeModifier
 eventPicker=random.randint(1,51)
 global day
 global practiceTime
 global teamAddFatigue
 global boatDamage
 endEnable=0
 if day > 0:
  day=day+1
  global week
 if day == 7:
  raceDay()
 if day>7:
  day=1
  week=week+1
 dayNewString = "It is Day {} of Week {}.  It is a nice summer day.".format(day, week)
 if week > 3:
  dayNewString = "It is Day {} of Week {}.  It is a crisp fall.".format(day, week)
  if week > 6:
   dayNewString = "It is Day {} of Week {}.  It is a cold, foggy winter day.".format(day, week)
 print(Fore.CYAN)
 print(dayNewString)
 print(Style.RESET_ALL)
 print("")
 if day < 7:
  if boatDamage>1:
    print(Fore.RED)
    print("Your boat is damaged!")
    print(Style.RESET_ALL)
    print("")
    teamAddFatigue+=5*boatDamage
  practiceTime = 120 + practiceTimeModifier
  practiceTimeModifier = 0
  print("You show up at practice.  Your teammates are there waiting for you.")
  while practiceTime > 0:
   practiceTimeString = "You have {} minutes left of practice.".format(practiceTime)
   print(practiceTimeString)
   actionMenu() 
   action=input()
   actionSelect(action)
   endEnable=1
   if practiceTime == 30:
    if day == 2:
     if week == 1:
      eventDayTwo() 
     else:
      if eventDeny==0:
       eventTrigger(eventPicker)
       eventDeny=1
    else:
     if eventDeny ==0:
      eventTrigger(eventPicker)
      eventDeny=1

    
  if practiceTime == 0:
   if endEnable==1:
    print("Everyone begins to pack their things and head home.")
    endEnable=0
    teamSleep()
    teamAddBlock()
    night()
  



if day==0:
 while True:
  
  print(Fore.CYAN + "Welcome to Skeleton Crew!")
  print(Style.RESET_ALL)
  print("You are the captain of your local youth rowing club.")
  print("You're in charge of training your teammates and managing the team.")
  print("You're an experienced rower, and you feel confident in your abilities to lead the team.")
  print("~~~~~~~~~")
  print("You and your team live in the small coastal town of Watson's Harbor.  To the north lies the larger city of Newhaven.")
  print("Watson's Harbor is a fishing town, and as such you and your team occupy a small boathouse near the harbor proper.")
  print("Since it's a small town, the team only has 8 athletes.")
  print("You've moved to the town recently and have assumed position as the new captain due to your wealth of experience.")
  print("The town is charming, but the locals always seem to avoid going out at night.")
  print("Unfortunately, practice runs late.")
  print("~~~~~~~~~")
  print("You'll have practice every Monday - Saturday for two hours each day, not including prep and cleaning.")
  print("Race days are Sundays, where you scrimmage against Newhaven Crew, your rival team.")
  print("~~~~~~~~~")
  print("Let's start with your name: ")
  name = input()
  print("Good luck, " +name+ ".")
  print("Now how about your team's name?")
  teamName = input()
  print("~~~~~~~~")
  print("Here's what you'll need to know in order to play.")
  print("As you've already seen, the game works via text inputs.")
  print("You will select workouts, lineups, text options, and everything else by entering numbers into the given text input.")
  print("Only select numbers that are listed with a given acton, please.")
  print("Sometimes, during dialogue, the game will appear to pause, and give you an opportunity to enter text.")
  print("With input opportunities without listed actions, just hit enter in order to proceed.")
  print("~~~~~~~~")
  print("It's your first day.  Let's go to practice.")
  firstDay()
  day=1

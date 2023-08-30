#starting boat score average of 1200 with neutral fatigue mod

import random
global compCounter
compCounter = 1
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
  teamAddFatigue = 8
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
  teamAddFatigue = 13
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
  teamAddFatigue = 7
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
  teamAddFatigue = 10
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
  teamAddFatigue = 15

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
  teamAddFatigue = 7
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
  teamAddFatigue = -4
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
  teamAddFatigue = -8
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
  teamAddFatigue = -18
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
 print("Kris stands away from the team.  Tall and strong, they stands out.")
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
 print("Wheneve they think you're not looking, they're tossing something in their hand.")
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
 print("1. Erg: Steady State - (++ Endurance + Power - Morale - Fatigue, 30min.)")
 print("2. Erg: Power - (+ Endurance ++ Power - Morale -- Fatigue, 30min.)")
 print("3. Water: Steady State - (+ Endurance + Technique + Rhythm + Morale -Fatigue, 30min)")
 print("4. Water: Power - (+ Power + Technique + Rhythm + Morale -- Fatigue, 30min)")
 print("5. Weights - (++ Power + Morale - Rhythm -Fatigue, 30min)")
 print("6. Running - (++ Endurance + Rhythm - Technique --Fatigue, 30min)")
 print("7. Core - (++ Technique + Fatigue + Morale, 30min.)")
 print("Misc. -----")
 print("8. Speech - (+++ Morale + Fatigue, 30min)")
 print("9. Rest - (-- Fatigue + Morale, 30min.)")
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
 angelFatigue=angelFatigue-(30*insomniaCalc(angelTerror))
 if angelFatigue < 0:
  angelFatigue=0
 santanaFatigue=santanaFatigue-(30*insomniaCalc(santanaTerror))
 if santanaFatigue < 0:
  santanaFatigue=0

def eventTrigger(eventNumber):
 print("event happens here:",eventNumber)

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
 print(dayOneString)
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
  print("The sun sets.  It's a new day.")
  print("")
  print("")
  print("")
  teamSleep()
  print(samFatigue)
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
 global boatRating
 fatigueModOutput=fatigueModifier()
 moraleModOutput=moraleModifier()
 boatRating=(boatAddEndurance+boatAddPower+boatAddRhythm+boatAddTechnique) * moraleModOutput * fatigueModOutput


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
 CompetitorScore = 1200 * (600*compCounter)
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
  tieString = "It's unprecedented!  Newhave Crew and {} tie, exactly!".format(teamName)
  global hasAchievementTie
  hasAchievementTie=1
  print(tieString)

 newDay()
 

def newDay():
 global eventPicker
 eventPicker=random.randint(1,100)
 global day
 global practiceTime
 endEnable=0
 if day > 0:
  if practiceTime == 0:
   teamAddBlock()
  day=day+1
  global week
 if day == 7:
  raceDay()
 if day>7:
  day=1
  week=week+1
 dayNewString = "It is Day {} of Week {}.  It is a nice summer day.".format(day, week)
 print(dayNewString)
 print("")
 if day < 7:
  practiceTime = 120
  print("You show up at practice.  Your teammates are there waiting for you.")
  while practiceTime > 0:
   practiceTimeString = "You have {} minutes left of practice".format(practiceTime)
   print(practiceTimeString)
   actionMenu() 
   action=input()
   actionSelect(action)
   endEnable=1
   if practiceTime == 30:
    eventTrigger(eventPicker)
  if practiceTime == 0:
   if endEnable==1:
    print("Everyone begins to pack their things and head home.")
    endEnable=0
    teamSleep()
    newDay()
  



if day==0:
 while True:
  print("Welcome to Skeleton Crew!")
  print("You are the captain of your local youth rowing club.")
  print("You're in charge of training your teammates and managing the team")
  print("You're an experience rower, and you feel confident in your abilities to lead the team.")
  print("Let's start with your name: ")
  name = input()
  print("Good luck, " +name+ ".")
  print("Now how about your team's name?")
  teamName = input()
  print("It's your first day.  Let's go to practice.")
  firstDay()
  day=1

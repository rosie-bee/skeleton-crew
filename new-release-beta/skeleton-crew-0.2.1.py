#starting boat score average of 1200 with neutral fatigue mod

import random
global compCounter
compCounter = 1
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
  tieString = "It's unprecedented!  Newhaven Crew and {} tie, exactly!".format(teamName)
  global hasAchievementTie
  hasAchievementTie=1
  print(tieString)

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
 print("As you direct your team through their workout, you hear and unfamiliar female voice call out.")
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
  print("You turn and see a girl bounding up to the shore.  She wears modest clothing, an oddly heavy coat, and wears her brown hair down in curls.")
  print("Her glasses flash in the sunlight, and she looks at you with admiration.")
  print("'I'm sorry, I didn't mean to interrupt.  I just wanted to introduce myself!'")
  print("'My name is Ophelia!  I've lived here my whole life, and take a keen interest in local history.'")
  print("'I'll keep it quick, but if you find anything... interesting... around here, just come see me, okay?'")
 elif dialog1 == "2":
  opheliaLove=opheliaLove+25
  opheliaAuthority=opheliaAuthority+10
  print("You turn and see a girl bounding up to the shore.  She wears modest clothing, an oddly heavy coat, and wears her brown hair down in curls.")
  print("Her glasses flash in the sunlight, and she looks at you with a beaming smile.") 
  print("'Hi!  I'm so glad I found you!  My name is Ophelia!'")
  print("'I've lived here my whole life and always had an interest in local history.")
  print("I live on the outskirts of town, down by the woods.  If you find anything... interesting... just come see me, okay?")
 elif dialog1 == "3":
  opheliaLove=opheliaLove+40
  opheliaAuthority=opheliaAuthority+3
  print("You turn and see a girl bounding up to the shore.  She wears modest clothing, an oddly heavy coat, and wears her brown hair down in curls.")
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
 print("2. Fishing Pier - 60 min. [Not Implemented]")
 print("3. Park - 60 min. [Not Implemented]")
 print("4. Boathouse - 60 min. [Not Implemented]")
 print("Actions -----")
 print("5. Night Walk - 60 min. [Not Implemented]")
 print("6. Study - 60 min. [Not Implemented]")
 print("~~~~~~~~")

def actionOneN():
 global opheliaLove
 global opheliaAuthority
 global nightTime
 nightTime=nightTime-60
 print("You make your way through the darkening town to a small, run-down house on the exterior of town.")
 print("The crows congregate around the roof of the house, fending off the encroaching seagulls.")
 print("An obviously home-made banner is draped haphazardly across the front porch:")
 print("'Local History Museum'")
 print("")
 print("Ophelia steps out into the porchlight, glasses glinting.")
 if opheliaLove == 0:
  print("She scowls.")
  print("'Hmph.  What do you want?'")
 if opheliaLove > 0:
  if opheliaLove > 50:
   if opheliaLove > 150:
    if opheliaLove > 250:
     print("'"+name+"!  It's so good to see you...'")
     print("'It's so late!  Come in!")
     print("'Did you bring something for me...?'")
    print("'Oh!'  She averts her gaze to the ground.")
    print("It's, uhm, it's good to see you again?'")
    print("'What... what brings you by?  Did you need to see me?'")
   print("She beckons for your attention.")
   print("'Hey, it's good to see you again!'")
   print("'Have you brought something for me?'")
  print("She calls out to you.")
  print("'What brings you around here?'")
  print("'Do you have something for me?'")
 print("~~~~~~~~")
 print("What would you like to say?")
 print("1. I just wanted to check in on you.  How are you doing?")
 print("2. Can you give me a tour of your exhibits?")
 print("3. Can you tell me anything about local history?")
 print("4. Tell me about yourself.")
 print("5. Let's just hang out a while.")
 print("6. Can you take a look at this artifact I found?")
 print("")
 print("7. Close")
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
 if actionInput=="2":
  print("'You'd really like to see the exhibits?'")
  print("Ophelia blushes at your suggestion.")
  print("'Follow me!'")
  print("Ophelia rushes off into the cluttered museum/house.")
  print("She gestures towards a glass case, containing a multitude of obsidian and granite arrowheads.")
  print("'These are my arrowheads!  I found every one of them searching in the woods.  If you find any more, give me a call!'")
  print("'Would you like to keep going?'")
  input()
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
  print("'Let's keep moving!")
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
   print("'I found out some very interesting things, and now we're here!")
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
   print("'Ophelia is beaming.'")
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
    print("She eventually releases her grasp, and the two of you laught together for a moment.")
   else:
    print("She blushes more, and turns away from you.")
    print("After a while of stammering excuses and denials, she reaches out a hand.")
    print("You take it.  You feel warmer.")
    teamAddMorale=teamAddMorale+10
    teamAddTerror=teamAddTerror-10
   input()
 if actionInput == "5":
  if opheliaLove == 0:
   print("'I really would rather not.")

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
  print("'I'm sorry, it doesn't look like you have any artifacts on you!'")
  
   

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
  actionFiveN()
 elif action == "6":
  actionSixN()


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
 if nightTime == 0:
  if nightEndEnable == 1:
   print("You head home and go to sleep for the night.")
   nightEndEnable=0
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
      eventTrigger(eventPicker)
    else:
     eventTrigger(eventPicker)

    
  if practiceTime == 0:
   if endEnable==1:
    print("Everyone begins to pack their things and head home.")
    endEnable=0
    teamSleep()
    night()
  



if day==0:
 while True:
  
  print("Welcome to Skeleton Crew!")
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
  print("You'll have practice every Monday-Saturday for two hours each day, not including prep and cleaning.")
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
  print("With inpu opportunities with listed actions, just hit enter in order to proceed.")
  print("~~~~~~~~")
  print("It's your first day.  Let's go to practice.")
  firstDay()
  day=1

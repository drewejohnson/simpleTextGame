#-------------------
# Andrew Johnson
# 20 May, 2016
#
# A Simple Text-Based Game
#---------------------
"""
A simple text-based game where you explore a maze,
fight monsters, and obtain gear.
"""

#----------------------
#	Modules Import
#----------------------

import verbFuncMod as VFM
import classMod as CM
<<<<<<< HEAD
import itemMod as IM
=======
import launch
>>>>>>> refs/remotes/origin/master

#--------------
# Launch screen
#--------------
gameSpace = 40
launch.prettyIntro(gameSpace,__doc__)
#------------
# Creatures
#------------
gobbly = CM.Goblin("gobbly")
#------------
# Game
#------------
<<<<<<< HEAD
pName = input("What is your name, brave adventurer: \n")
player = CM.Player(pName.lower())
startSword = IM.Sword("trusty")
print(VFM.take(startSword.itemName))
print("And so, "+pName.capitalize()+" and their",\
	startSword.itemName,startSword.itemType,\
	"began their brave quest into the unknown!")
=======
pName = input("What is your name, brave adventurer?\n: ")
player = CM.Adventurer(pName)
print("And so, "+pName+' departed on their brave quest into the unknown!')
>>>>>>> refs/remotes/origin/master
while True:
	VFM.getInput()

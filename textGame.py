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
import itemMod as IM
import launch

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

pName = input("What is your name, brave adventurer: \n")
player = CM.Player(pName.lower())
startSword = IM.Sword("trusty")
print(VFM.take(startSword.itemName))
print("And so, "+pName.capitalize()+" and their",\
	startSword.itemName,startSword.itemType,\
	"began their brave quest into the unknown!")
while True:
	VFM.getInput()

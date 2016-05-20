#-------------------
# Andrew Johnson
# 19 May, 2016
#
# A Simple Text-Based Game
#---------------------
"""
A simple text-based game where you explore a maze, fight monsters, and obtain gear.
"""

#----------------------
#	Modules Import
#----------------------

import verbFuncMod as VFM
import classMod as CM

#------------
# Creatures
#------------
goblin = CM.Goblin("Gobbly")
#------------
# Game
#------------
pName = input("What is your name, brave adventurer: \n")
player = CM.Adventurer(pName)
print("And so, "+pName+' departed on their brave quest into the unknown!')
while True:
	VFM.getInput()
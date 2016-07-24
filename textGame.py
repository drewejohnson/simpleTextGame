#-------------------
# Andrew Johnson
#
# A Simple Text-Based Game
#---------------------
"""
A simple text-based game where you explore a maze,
fight monsters, and obtain gear.
"""

#----------------------
#	Modules Import/ Game Preparation
#----------------------

import launch
import roomMod as RM
import itemMod as IM
import verbFuncMod as VFM
import tutorial



launch.launchScreen()
print(VFM.help())
RM.buildGame()


# dummy = input("Press 'y' to begin a tutorial.\n  Or type SKIP to start the game")
dummy = 'y'
if dummy[0].lower() == 'y':
	tutorial.teachGame()

while True:
	VFM.getInput()

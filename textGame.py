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

launch.launchScreen()
print(VFM.help())
RM.buildGame()

while True:
	VFM.getInput()

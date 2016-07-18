#--------------------------------
# Andrew Johnson
#
# Simple Text Based Game
#
# Tutorial
#----------------------------
import classMod as CM
import itemMod as IM
import roomMod as RM
import verbFuncMod as VFM
from launch import gameSpace, prettyString,prettyPrint


#-------------
# Functions
#------------
def examineTutorial():
    print(VFM.examine(VFM.player.name))
    eStr = "The top line shows your health, attack strength, and defense. The next line shows your location in the dungeon."+\
        "The next few lines show what items you have equipped on your arms, legs, and head, plus any items stored in your pack."+\
        "Items you have equipped give you bonuses by increasing you health, attack strengh, or defense."+\
        "To see these benefits, type EXAMINE TRUSTY SWORD."
    prettyPrint(eStr)
    e = input(": ")





def teachGame():
    """Show a series of prompts teaching the player the basic moves of the game"""
    print("+"*gameSpace)
    print("{t:^{w}}".format(t="Tutorial",w=gameSpace))
    print("+"*gameSpace)
    prettyPrint("Commands in the tutorial will be shown in all caps. However, your inputs do not need to be upper or lower case.")
    prettyPrint("Let's learn about our brave adventurer, {0}. Type EXAMINE {1}".\
        format(VFM.player.name.capitalize(),VFM.player.name.upper()))
    while True:
        v = input(": ").split()
        if v[0].lower() == 'examine' and (v[1].lower() == 'self' or v[1].lower() == VFM.player.name.lower()):
            examineTutorial()
            break
        else:
            prettyPrint("Type EXAMINE {0}".format(VFM.player.name.upper()))

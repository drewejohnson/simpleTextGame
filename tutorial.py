#--------------------------------
# Andrew Johnson
#
# Simple Text Based Game
#
# Tutorial
#----------------------------
from time import sleep
import classMod as CM
import itemMod as IM
import roomMod as RM
import verbFuncMod as VFM
from launch import gameSpace, prettyString,prettyPrint


#-------------
# Functions
#------------
sTime = 0.5
def examineTutorial():
    print(VFM.examine(VFM.player.name)+"\n")
    sleep(sTime)
    eStr = "The top line shows your health, attack strength, and defense. The next line shows your location in the dungeon."+\
        " The next few lines show what items you have equipped on your arms, legs, and head, plus any items stored in your pack."
    prettyPrint(eStr)
    prettyPrint("Items you have equipped give you bonuses by increasing you health, attack strengh, or defense. To see these benefits, type EXAMINE TRUSTY SWORD.")
    while True:
        e = input(": ")
        if e.lower() == "examine trusty sword":
            print(VFM.examine("trusty","sword")+"\n")
            sleep(sTime)
            break
        else:
            print("type EXAMINE TRUSTY SWORD.")
    prettyPrint("Here, examine shows the specific bonus the trusty sword applies.")
    prettyPrint("The EXAMINE command is very powerful. It can show your personal traits, as well as the traits of enemies and items both in your pack and in your room.")
    prettyPrint("To see what interesting items and enemies are in your room, type EXAMINE ROOM")
    while True:
        e = input(": ")
        if e.lower() == 'examine room':
            print(VFM.examine("room")+"\n")
            sleep(sTime)
            break
        else:
            print("type EXAMINE ROOM")
    eStr = "Taking a look around, you can see your current location, and the enemies and items in your room."+\
        " Rooms may have enemies or items, or a combination of both. Some rooms will have nothing. That's the beauty of the game."+\
        " You can only take the loot from a room and move forward after you have defeated all the enemies in the room."
    prettyPrint(eStr)
    prettyPrint("Type EXAMINE GOBBLY to view the stats of your first enemy.")
    while True:
        e = input(": ")
        if e.lower() == 'examine gobbly':
            print(VFM.examine("gobbly")+"\n")
            sleep(sTime)
            break
        else:
            print("type EXAMINE GOBBLY")
    prettyPrint("These are the basics of the examine function. But looking at things isn't the point of the game. You're here to hit stuff. Let's talk about that next")






def teachGame():
    """Show a series of prompts teaching the player the basic moves of the game"""
    print("+"*gameSpace)
    print("{t:^{w}}".format(t="Tutorial",w=gameSpace))
    print("+"*gameSpace)
    prettyPrint("Commands in the tutorial will be shown in all caps. However, your inputs need not be upper nor lower case.")
    prettyPrint("Let's learn about our brave adventurer, {0}. Type EXAMINE {1}".\
        format(VFM.player.name.capitalize(),VFM.player.name.upper()))
    while True:
        v = input(": ").split()
        if v[0].lower() == 'examine' and (v[1].lower() == 'self' or v[1].lower() == VFM.player.name.lower()):
            examineTutorial()
            break
        else:
            prettyPrint("Type EXAMINE {0}".format(VFM.player.name.upper()))

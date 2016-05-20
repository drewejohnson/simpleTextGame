#-------------------
# Andrew Johnson
# 19 May, 2016
#
# A Simple Text-Based Game
#---------------------

# Create simple game to demonstrate the power of objects

#----------------------
# Creation of various game objects and creatures
#----------------------
class GameObject:
	className = ""
	desc = ""
	objects = {}
	
	def __init__(self,name):
		self.name = name
		GameObject.objects[self.className] = self
		
	def getDesc(self):
		return self.className+"\n"+self.desc
		
class Goblin(GameObject):
	def __init__(self,name):
		self.className = "goblin"
		self.health = 3
		super().__init__(name)
		self._desc = "A foul creature called "+self.name
		
	@property
	def desc(self):	# function for modifying the health line
		if self.health >= 3:
			return self._desc
		elif self.health == 2:
			healthLine = "It has a wound on its knee."
		elif self.health == 1:
			healthLine = "Its left arm has been cut off!"
		elif self.health <= 0:
			healthLine = "It is dead."
		return self._desc+"\n"+healthLine
	
	@desc.setter
	def desc(self,value):
		self._desc = value
#-----------
# Functions for interacting with the game
#-----------	
def getInput():
	command = input(": ").split()
	verbIn = command[0]
	if verbIn in verbDict:
		verb = verbDict[verbIn]
	else:
		print("Unknown verb {}".format(verbIn))
		return
	
	if len(command)> 1:
		nounIn = command[1]
		print(verb(nounIn))
	else:
		print(verb())
		
def say(noun):
	return 'You said "{}"'.format(noun)

def examine(noun):
	if noun in GameObject.objects:
		return GameObject.objects[noun].getDesc()
	else:
		return "There is no {} here".format(noun)
# looks for an object wth name noun in GameObjects object		
def hit(noun):
	if noun in GameObject.objects:
		thing = GameObject.objects[noun]
		thing.health = thing.health -1
		if thing.health <= 0:
			msg = "You killed the {}!".format(thing.className)
		else:
			msg = "You hit the {}".format(thing.className)
	else:
		msg = "There is no {} here.".format(noun)
	return msg
		
verbDict = {
	"say": say,
	"examine": examine,
	"hit": hit,
}

#------------
# Creatures
#------------
goblin = Goblin("Gobbly")
#------------
# Game
#------------
while True:
	getInput()
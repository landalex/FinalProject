# PYTHON LOL (Name a Work in Progess)
# Created by Evan Chisholm and Alex Land

import random
import turtle as t

# VARIABLES

godMode = ""
playerPos = -1
biomeData = []
biomeDiamonds = []
biomeSwords = []
biomeEnemies = []
localList = []
fillColor = "tan"
catastropheNumber = 0
pythonShine = ""
playerName = ""
startGame = ""
playerHealth = ""
catastrophe = ""
maximumTurns = ""
turnNumber = 0
playerSword = 0
playerDiamonds = 0
gameOn = False

# FUNCTIONS

def gameStart():
    global startGame
    startGame = ""
    while startGame != "y":
        startGame = raw_input("Would you like to play a game (y/n)? ")
        
    global godMode
    while godMode == "":
        godModeInput = raw_input("Would you like to manually choose biomes (y/n)? ")
        if godModeInput == "y":
            godMode = True
        elif godModeInput == "n":
            godMode = False
        else:
            print "Please enter y for yes or n for no."

def enterInfo():
    global playerHealth
    if godMode == True:
        playerHealth = input("What is your initial health? (Pick a number between 10 and 50) ")
    if godMode == False:
        playerHealth = 10* (random.randint(1,5))
        
    global playerName
    while playerName == "":
        playerName = raw_input("What is the name of your character? ")
        
    global maximumTurns
    maximumTurns = input("How many turns do you want to play (maximum)? ")

    global playerPos
    playerPos = 0

    global gameOn
    gameOn = True

    
    
def turnGenerator():
    global playerPos
    global turnNumber
    if turnNumber >= 0:
        if godMode == True:
            playerPos = input("Which biome would you like to go to (Pick a number between 1 and 7)? ")
        if godMode == False:
            playerPos = random.randint(1,7)
        
    turnNumber += 1
    print "Starting turn number", turnNumber
    print playerName, "has travelled to position", playerPos
    

def biomeDraw(fillColor):
        t.fillcolor(fillColor)
        t.begin_fill()
        t.forward(50)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.end_fill()
        t.forward(70)

def playerDraw():
    t.fillcolor("red")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
        
def drawBoard(catastropheNumber):
    biomeDraw() * (8 - catastropheNumber)

def drawPlayer(biomeNumber):
    t.penup()
    t.forward(25)
    t.forward((biomeNumber - 1) * 50)
    playerDraw()

def readFile(the_file):
    '''
    CODE PROVIDED TO INCORPORATE
    
    <file-name including extension .txt>(String) --> List of strings
    
    Assumptions:
    1) the_file is in the same directory as this program 
    2) the_file contains one biome data per line 
    3) after each biome in the file  there is a return (
       so that the next biome is in the next line), and also
      there is (one single) return after the last biome
      in the_file

    to call or invoke this function:
    listStrings = read_string_list_from_file(<file-name.txt in quotes>)
    '''
    
    fileRef = open(the_file,"r") # opening file to be read
    global localList
    localList=[]
    for line in fileRef:
        string = line[0:len(line)-1]  # eliminates trailing '\n'
                                      # of each line 
                                    
        localList.append(string)  # adds string to list
        
    fileRef.close()  
        
    #........
    #print "\n JUST TO TRACE, the local list of strings is:\n"
    #for element in localList:
    #    print element
    #print
    #........
        
    return localList

def biomeDataParser(localList):
    global biomeData
    global biomeDiamonds
    global biomeSwords
    global biomeEnemies
    for i in range(len(localList)):                 #wow, much comments
        biomeData.append(localList[i].split("-"))    # many biome lists, wow. 
    for j in range(len(biomeData)):
        for k in range(1):
            biomeDiamonds.append(int(biomeData[j][k]))
            biomeSwords.append(int(biomeData[j][k+1]))
            biomeEnemies.append(int(biomeData[j][k+2]))
    

def biomeTable():
    print "The current board state is as follows:"
    print "Biome Diamd Sword Enemy"
    for i in range(len(biomeData)):
        if pythonShine == i:
            print i , " " * (5-(len(str(i)))), biomeDiamonds[i], " " * (5-(len(str(biomeDiamonds[i])))), \
              biomeSwords[i], " " * (5-(len(str(biomeSwords[i])))), biomeEnemies[i], "  <=== PythonShine"
        elif playerPos == i and turnNumber >= 0:
            print i , " " * (5-(len(str(i)))), biomeDiamonds[i], " " * (5-(len(str(biomeDiamonds[i])))), \
                  biomeSwords[i], " " * (5-(len(str(biomeSwords[i])))), biomeEnemies[i], " <===", playerName
        elif playerPos == i and turnNumber < 0:
            print i , " " * (5-(len(str(i)))), biomeDiamonds[i], " " * (5-(len(str(biomeDiamonds[i])))), \
                  biomeSwords[i], " " * (5-(len(str(biomeSwords[i])))), biomeEnemies[i]
        elif pythonShine == i and playerName == i:
            print "You're in PythonShine!"
        else:
            print i , " " * (5-(len(str(i)))), biomeDiamonds[i], " " * (5-(len(str(biomeDiamonds[i])))), \
              biomeSwords[i], " " * (5-(len(str(biomeSwords[i])))), biomeEnemies[i]

def pythonShineGenerator():
    global pythonShine
    if godMode == True:
        pythonShine = input("Where do you want to place PythonShine? (Pick a number from 2 to 8) ")
        pythonShine += -1
    elif godMode == False:
        pythonShine = random.randint(1, 7)

def combatCalculator():
    global playerSword
    global playerHealth
    if biomeSwords[playerPos] > playerSword:
        playerSword = biomeSwords[playerPos]
        print playerName, "has picked up a level", playerSword, "sword!"
    if playerSword > biomeEnemies[playerPos]:
        healthGain = random.randint(1, playerHealth)
        playerHealth += healthGain
        print playerName, "won the fight and gained", healthGain, "health!"
    if biomeEnemies[playerPos] > playerSword:
        healthLost = random.randint(1, playerHealth)
        playerHealth -= healthLost
        print playerName, "lost the fight and lost", healthLost, "health."
    if playerSword == biomeEnemies[playerPos]:
        healthLost = random.randint(1, (playerHealth / 2))
        playerHealth -= healthLost
        print playerName, "tied the fight, but lost", healthLost, "health."
        

def diamondCalculator():
    global playerDiamonds
    if playerPos == pythonShine:
        playerDiamonds = 9999
    else:
        playerDiamonds += (biomeDiamonds[playerPos])/3
        print playerName, "has collected", (biomeDiamonds[playerPos]/3), "diamonds!"

def playerInfo():
    print playerName + " currently has:"
    print playerHealth, "health."
    print playerDiamonds, "diamonds."
    if playerSword == 0:
        print "No sword."
    else:
        "A level", playerSword, "sword."
    if playerPos == "":
        print "And is about to spawn."
    else:
        print "And is in position", playerPos
    
def gameCheck():
    global gameOn
    #if playerPos == pythonShine:
       # gameOn = False
    if playerHealth <= 0:
        gameOn = False
    if turnNumber == maximumTurns:
        gameOn = False
    

# EXECUTION TOP LEVEL

gameStart()
readFile("biomesData1.txt")
biomeDataParser(localList)
pythonShineGenerator()
biomeTable()
enterInfo()

# WHILE LOOP
while gameOn == True:
    biomeTable()
    playerInfo()
    turnGenerator()
    diamondCalculator()
    combatCalculator()
    gameCheck()

playerInfo()

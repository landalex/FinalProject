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
playerHealth = 0
catastrophe = ""
maximumTurns = 0
turnNumber = 0
playerSword = 0
playerDiamonds = 0
roundOn = False
playerPosInput = ""
gameOn = True
gameOnInput = ""
catastrophePos = ""
biomeList = []

# FUNCTIONS

def gameStart():
    global startGame
    counter = 0
    while startGame != "y":
        startGame = raw_input("Would you like to play a game (y/n)? ")
        if startGame != "y":
            print "Please enter y to play."
            counter += 1
        if counter >= 5:
            print "Think you're funny? You're not."
        
    global godMode
    while godMode == "":
        godModeInput = raw_input("Would you like to manually choose biomes (y/n)? ")
        if godModeInput == "y" or godModeInput == "yes":
            godMode = True
        elif godModeInput == "n" or godModeInput == "no":
            godMode = False
        else:
            print "Please enter y for yes or n for no."

def enterInfo():
    global playerHealth
    while playerHealth < 10 or playerHealth > 50:
        if godMode == True:
            playerHealth = input("What is your initial health? (Pick a number between 10 and 50) ")
            if playerHealth < 10 or playerHealth > 50:
                print "Please pick a value between 10 and 50."
        if godMode == False:
            playerHealth = 10* (random.randint(1,5))
        
    global playerName
    while playerName == "":
        playerName = raw_input("What is the name of your character? ")
        
    global maximumTurns
    while maximumTurns <= 0:
        maximumTurns = input("How many turns do you want to play (maximum)? ")
        if maximumTurns <= 0:
            print "Please input a value greater than 0."

    global playerPos
    playerPos = 0

    global roundOn
    roundOn = True

    
    
def turnGenerator():
    global playerPos
    global turnNumber
    global playerPosInput
    if turnNumber >= 0:
        if godMode == True:
            playerPos = input("Which biome would you like to go to (Pick a number between 1 and 7)? ")
            while playerPos <= 0 or playerPos > 7:
                print "Please input a value between 1 and 7."
                playerPos = input("Which biome would you like to go to (Pick a number between 1 and 7)? ")
        if godMode == False:
            playerPosInput = raw_input("Are you ready for the next turn? (y/n) ")
            if playerPosInput == "y":
                playerPos = ((playerPos + random.randint(1,6)) % 8)
            elif playerPosInput != "y":
                print "Tricked you, there was never a choice."
                playerPos = ((playerPos + random.randint(1,6)) % 8)
        
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
    global biomeList
    for i in range(len(localList)):                 #wow, much comments
        biomeData.append(localList[i].split("-"))    # many biome lists, wow. 
    for j in range(len(biomeData)):
        for k in range(1):
            biomeDiamonds.append(int(biomeData[j][k]))
            biomeSwords.append(int(biomeData[j][k+1]))
            biomeEnemies.append(int(biomeData[j][k+2]))
            biomeList.append(j)

def biomeTable():
    print "The current board state is as follows:"
    print "Biome Diamd Sword Enemy"
    for i in range(len(biomeList)):
        if godMode == True:
            if pythonShine == i:
                print biomeList[i] , " " * (5-(len(str(i)))), biomeDiamonds[i], " " * (5-(len(str(biomeDiamonds[i])))), \
                  biomeSwords[i], " " * (5-(len(str(biomeSwords[i])))), biomeEnemies[i], "  <=== PythonShine"
            elif playerPos == i and turnNumber >= 0:
                print biomeList[i] , " " * (5-(len(str(i)))), biomeDiamonds[i], " " * (5-(len(str(biomeDiamonds[i])))), \
                    biomeSwords[i], " " * (5-(len(str(biomeSwords[i])))), biomeEnemies[i], " <===", playerName
            elif playerPos == i and turnNumber < 0:
                print biomeList[i] , " " * (5-(len(str(i)))), biomeDiamonds[i], " " * (5-(len(str(biomeDiamonds[i])))), \
                      biomeSwords[i], " " * (5-(len(str(biomeSwords[i])))), biomeEnemies[i]
            elif pythonShine == playerPos:
                print biomeList[i] , " " * (5-(len(str(i)))), biomeDiamonds[i], " " * (5-(len(str(biomeDiamonds[i])))), \
                  biomeSwords[i], " " * (5-(len(str(biomeSwords[i])))), biomeEnemies[i], "  <=== PythonShine", " <===", playerName
            else:
                print biomeList[i] , " " * (5-(len(str(i)))), biomeDiamonds[i], " " * (5-(len(str(biomeDiamonds[i])))), \
                  biomeSwords[i], " " * (5-(len(str(biomeSwords[i])))), biomeEnemies[i]
        if godMode == False:
            if pythonShine == i:
                print biomeList[i] , " " * (5-(len(str(i)))), biomeDiamonds[i], " " * (5-(len(str(biomeDiamonds[i])))), \
                  biomeSwords[i], " " * (5-(len(str(biomeSwords[i])))), biomeEnemies[i]
            elif playerPos == i and turnNumber >= 0:
                print biomeList[i] , " " * (5-(len(str(i)))), biomeDiamonds[i], " " * (5-(len(str(biomeDiamonds[i])))), \
                      biomeSwords[i], " " * (5-(len(str(biomeSwords[i])))), biomeEnemies[i], " <===", playerName
            elif playerPos == i and turnNumber < 0:
                print biomeList[i] , " " * (5-(len(str(i)))), biomeDiamonds[i], " " * (5-(len(str(biomeDiamonds[i])))), \
                      biomeSwords[i], " " * (5-(len(str(biomeSwords[i])))), biomeEnemies[i]
            elif pythonShine == playerPos:
                print biomeList[i] , " " * (5-(len(str(i)))), biomeDiamonds[i], " " * (5-(len(str(biomeDiamonds[i])))), \
                  biomeSwords[i], " " * (5-(len(str(biomeSwords[i])))), biomeEnemies[i], "  <=== PythonShine", " <===", playerName
            else:
                print biomeList[i] , " " * (5-(len(str(i)))), biomeDiamonds[i], " " * (5-(len(str(biomeDiamonds[i])))), \
                  biomeSwords[i], " " * (5-(len(str(biomeSwords[i])))), biomeEnemies[i]

def pythonShineGenerator():
    global pythonShine
    if godMode == True:
        while pythonShine < 1 or pythonShine > 7:
            pythonShine = input("Where do you want to place PythonShine? (Pick a number from 1 to 7) ")
            if pythonShine < 1 or pythonShine > 7:
                print "Please input a value between 1 and 7."
            
    elif godMode == False:
        pythonShine = random.randint(1, 7)

def combatCalculator():
    global playerSword
    global playerHealth
    if biomeSwords[playerPos] > playerSword:
        tempSword = playerSword
        playerSword = biomeSwords[playerPos]
        biomeSwords[playerPos] = tempSword
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
    global playerSword
    global gameOn
    global gameOnInput
    if roundOn == True:
        print playerName + " currently has:"
        print playerHealth, "health."
        print playerDiamonds, "diamonds."
        if playerSword == 0:
            print "No sword."
        else:
            "A level", playerSword, "sword."
        if playerPos == -1:
            print "And is about to spawn."
        else:
            print "And is in position", playerPos
            
    elif roundOn == False:
        print "Game Over!"
        if playerHealth <= 0:
            print playerName + "has died."
        elif playerDiamonds == 9999:
            print playerName + "has won!"
        elif turnNumber == maximumTurns:
            print "The maximum number of turns has been reached."
        print playerName + " ended the game with:"
        print playerHealth, "health."
        print playerDiamonds, "diamonds."
        if playerSword == 0:
            print "No sword."
        else:
            "A level", playerSword, "sword."

    if gameOn == True:
        gameOnInput = raw_input("Would you like to play another game? (y/n) ")
        while gameOnInput != "y" or gameOnInput != "n":
            print "Please input y for yes or n for no."
        if gameOnInput == "y":
            gameOn = True
        if gameOnInput == "n":
            gameOn = False

            
def gameCheck():
    global roundOn
    if playerPos == pythonShine:
        roundOn = False
    if playerHealth <= 0:
        roundOn = False
    if turnNumber == maximumTurns:
        roundOn = False
    
def catastropheGenerator():
    global catastrophePos
    global catastropheNumber
    catastrophePos = (7 / 5) * (random.randint(1,7))
    for i in range(len(biomeList)):
        if catastrophePos == biomeList[i]:
            catastropheNumber += 1
            print "A catastrophe has occured in biome", catastrophePos
            print "Biome", catastrophePos, "has been destroyed!"
            biomelist.remove(catastrophePos)
            if playerPos == catastrophePos:
                playerHealth == 0
                print playerName, "has been caught in the catastrophe!"
                
# EXECUTION TOP LEVEL

gameStart()
readFile("biomesData1.txt")
biomeDataParser(localList)
pythonShineGenerator()
print 
biomeTable()
print 
enterInfo()


# WHILE LOOP
while gameOn == True:
    while roundOn == True:
        print 
        biomeTable()
        print 
        playerInfo()
        print 
        turnGenerator()
        diamondCalculator()
        combatCalculator()
        catastropheGenerator()
        gameCheck()

    print 
    playerInfo()

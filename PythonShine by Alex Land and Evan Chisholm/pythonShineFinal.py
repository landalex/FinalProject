# PythonShine
# Created by Evan Chisholm and Alex Land

import random
import turtle as t

# VARIABLES

startGame = ""              # Indicates if game should begin
godMode = ""               # Determines if player should choose their own position/health etc
fillColor = "tan"              # Default fill color of the biomes (For turtles)
playerPos = -1              # Indicates position of the player
playerName = ""            # Holds player name
playerHealth = ""            # Indicates current health of the player
playerSword = 0             # Indicates level of player's sword
playerDiamonds = 0         # Indicates number of player's diamonds
biomeData = []              # Holds information about all of the biomes (to be parsed)
biomeDiamonds = []         # Holds number of diamonds in each biome
biomeSwords = []            # Holds level of sword in each biome
biomeEnemies = []           # Holds level of enemy sword in each
biomeList = []               # Holds a list of all currently active biomes (minus catastrophe biomes)
localList = []                 # Contains all info from the text file
pythonShine = ""             # Indicates position of PythonShine
maximumTurns = ""          # Indicates maximum number of turns to play
turnNumber = 0             # Indicates current turn number
roundOn = False            # Indicates whether the game should loop for another turn, or restart
gameOn = True             # Indicates whether the game should end completely
catastrophe = ""            # Indicates whether the player wants catastrophes to occur or not
catastrophePos = ""         # Indicates the position of a catastrophe
catastropheNumber = 0     # Number of catastrophes occured (for positioning turtles)

# FUNCTIONS

def gameStart():            # This function initializes the game, and defines godMode (allows
    global startGame       # user to choose their own biomes etc)
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


def enterInfo():            # Gets player to enter information like health, name and max turns
    global playerHealth
    while playerHealth == "":
        if godMode == True:
            while playerHealth.isdigit() == False or int(playerHealth) < 10 or int(playerHealth) > 50:
                playerHealth = raw_input("What is your initial health? (Pick a number between 10 and 50) ")
            playerHealth = int(playerHealth)
        if godMode == False:
            playerHealth = 10* (random.randint(1,5))
        
    global playerName
    while playerName == "":
        playerName = raw_input("What is the name of your character? ")
        
    global maximumTurns
    while maximumTurns.isdigit() == False or int(maximumTurns) <= 0:
        maximumTurns = raw_input("How many turns do you want to play (maximum)? ")
    maximumTurns = int(maximumTurns)

    global catastrophe
    while catastrophe == "":
        catastropheInput = raw_input("Would you like to allow catastrophes (y/n)? ")
        if catastropheInput == "y":
            catastrophe = True
        elif catastropheInput == "n":
            catastrophe = False
        else:
            print "Please enter y for yes or n for no."

    global playerPos
    playerPos = 0

    global roundOn
    roundOn = True

    
    
def turnGenerator():        # Generates the "dice rolling" every turn, or allows player to choose
    global playerPos
    global turnNumber
    if turnNumber >= 0:
        if godMode == True:
            playerPos = raw_input("Which biome would you like to go to? ")
            while str(playerPos).isdigit() == False or (int(playerPos) <= 0 or int(playerPos) > (len(biomeList))):
                playerPos = raw_input("Which biome would you like to go to (Pick a number between 1 and 7)? ")
            playerPos = int(playerPos)
        if godMode == False:
            playerPosInput = raw_input("Are you ready for the next turn? (y/n) ")
            if playerPosInput == "y":
                playerPos = ((playerPos + random.randint(1,6)) % (len(biomeList)))
            elif playerPosInput != "y":
                print "Tricked you, there was never a choice."
                playerPos = ((playerPos + random.randint(1,6)) % (len(biomeList)))
        
    turnNumber += 1
    print "Starting turn number", turnNumber
    print playerName, "has travelled to position", playerPos
    

def biomeDraw(fillColor):       # Turtle function to draw an individual biome
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

def playerDraw():           # Turtle function to draw the player 
    t.fillcolor("red")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
        
def drawBoard():            # Turtle function to draw the entire board
    global catastropheNumber
    t.penup()
    t.forward(-300)
    t.pendown()
    for i in range(len(biomeList)):
        if i == pythonShine and godMode == True:
            biomeDraw("green")
        else:
            biomeDraw("tan")
    t.home()
    
def drawPlayer():       # Turtle function to position the turtle, so the player can be drawn correctly
    global playerPos
    t.penup()
    t.forward(-275)
    t.right(90)
    t.forward(50)
    t.left(90)
    if playerPos >= 0:
        t.forward((playerPos) * 70)
    playerDraw()

def readFile(the_file):     # Reads the text file in the same directory as this script
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

def biomeDataParser(localList):     # Parses text file, and seperates in to lists of each item
    global biomeData             # such as Diamonds, Swords and Enemies
    global biomeDiamonds
    global biomeSwords
    global biomeEnemies
    global biomeList
    for i in range(len(localList)):
        biomeData.append(localList[i].split("-")) 
    for j in range(len(biomeData)):
        for k in range(1):
            biomeDiamonds.append(int(biomeData[j][k]))
            biomeSwords.append(int(biomeData[j][k+1]))
            biomeEnemies.append(int(biomeData[j][k+2]))
            biomeList.append(j)


def biomeTable():           # Draws the table indicating information for each biome
    print "The current board state is as follows:"
    print "Biome Diamd Sword Enemy"
    for i in range(len(biomeList)):
        if godMode == True:
            if pythonShine == i:
                print biomeList[i] , " " * (5-(len(str(i)))), biomeDiamonds[i], " " * (5-(len(str(biomeDiamonds[i])))), \
                  biomeSwords[i], " " * (5-(len(str(biomeSwords[i])))), biomeEnemies[i], " <=== PythonShine"
            elif playerPos == i and turnNumber >= 0:
                print biomeList[i] , " " * (5-(len(str(i)))), biomeDiamonds[i], " " * (5-(len(str(biomeDiamonds[i])))), \
                    biomeSwords[i], " " * (5-(len(str(biomeSwords[i])))), biomeEnemies[i], " <===", playerName
            elif playerPos == i and turnNumber < 0:
                print biomeList[i] , " " * (5-(len(str(i)))), biomeDiamonds[i], " " * (5-(len(str(biomeDiamonds[i])))), \
                      biomeSwords[i], " " * (5-(len(str(biomeSwords[i])))), biomeEnemies[i]
            elif i == pythonShine and pythonShine == playerPos:
                print biomeList[i] , " " * (5-(len(str(i)))), biomeDiamonds[i], " " * (5-(len(str(biomeDiamonds[i])))), \
                  biomeSwords[i], " " * (5-(len(str(biomeSwords[i])))), biomeEnemies[i], " <=== PythonShine", " <===", playerName
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
            elif i == pythonShine and pythonShine == playerPos:
                print biomeList[i] , " " * (5-(len(str(i)))), biomeDiamonds[i], " " * (5-(len(str(biomeDiamonds[i])))), \
                  biomeSwords[i], " " * (5-(len(str(biomeSwords[i])))), biomeEnemies[i], " <=== PythonShine", " <===", playerName
            else:
                print biomeList[i] , " " * (5-(len(str(i)))), biomeDiamonds[i], " " * (5-(len(str(biomeDiamonds[i])))), \
                  biomeSwords[i], " " * (5-(len(str(biomeSwords[i])))), biomeEnemies[i]

def pythonShineGenerator():         # Generates the PythonShine position
    global pythonShine
    if godMode == True:
        while pythonShine.isdigit() == False or int(pythonShine) < 1 or int(pythonShine) > (len(biomeList)):
            pythonShine = raw_input("Where do you want to place PythonShine? ")
        pythonShine = int(pythonShine)
            
    elif godMode == False:
        pythonShine = random.randint(1, 7)

def combatCalculator():         # Calculates sword pickups, and combat scenarios
    global playerSword         # (adds or subtracts player health)
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
        if playerHealth > 1:
            healthLost = random.randint(1, playerHealth)
        if playerHealth == 1:
            healthLost = random.randint(0,1)
        playerHealth -= healthLost
        print playerName, "lost the fight and lost", healthLost, "health."
    if playerSword == biomeEnemies[playerPos]:
        healthLost = random.randint(1, (playerHealth / 2))
        playerHealth -= healthLost
        print playerName, "tied the fight, but lost", healthLost, "health."
        

def diamondCalculator():        # Calculates number of diamonds picked up in each biome
    global playerDiamonds
    if playerPos == pythonShine:
        playerDiamonds = 9999
    else:
        tempDiamonds = (biomeDiamonds[playerPos])/3
        playerDiamonds += tempDiamonds
        biomeDiamonds[playerPos] -= tempDiamonds
        print playerName, "has collected", tempDiamonds, "diamonds!"

def playerInfo():               # Displays information about the player's current stats, 
    global playerSword        # and prompts player to play again if dead
    global gameOn
    global roundOn
    gameOnInput = ""
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
        print "=========================================================="
            
    elif roundOn == False:
        print "Game Over!"
        if playerHealth <= 0:
            print playerName + " has died."
        elif playerPos == pythonShine:
            print playerName + " has won! " + playerName + " has found PythonShine!"
        elif turnNumber == maximumTurns:
            print "The maximum number of turns has been reached."
        print playerName + " ended the round with:"
        print playerHealth, "health."
        print playerDiamonds, "diamonds."
        if playerSword == 0:
            print "No sword."
        else:
            "A level", playerSword, "sword."
        print "=========================================================="

    if gameOn == True and roundOn == False:
        while gameOnInput == "" and gameOn == True:
            gameOnInput = raw_input("Would you like to play another game? (y/n) ")
            if gameOnInput == "y":
                gameOn = True
                roundOn = True
            elif gameOnInput == "n":
                gameOn = False
                endGameCalculations()
            else:
                print "Please input y for yes or n for no."
                gameOnInput = ""


            
def gameCheck():            # Checks if the game should continue, or end (if player is dead,
    global roundOn          # max turns reached, or player is in PythonShine)
    if playerPos == pythonShine:
        roundOn = False
    if playerHealth <= 0:
        roundOn = False
    if turnNumber == maximumTurns:
        roundOn = False
    
def roundReset():                       # Resets the variables to their default for each round
    global playerDiamonds
    global catastrophe
    global catastropheNumber
    global pythonShine
    global maximumTurns
    global playerHealth
    global turnNumber
    global biomeData
    global biomeDiamonds
    global biomeSwords
    global biomeEnemies
    global biomeList
    playerDiamonds = 0
    catastrophe = ""
    catastropheNumber = 0
    pythonShine = ""
    maximumTurns = ""
    playerHealth = ""
    turnNumber = 0
    biomeData = []
    biomeDiamonds = []
    biomeSwords = []
    biomeEnemies = []
    biomeList = []

def endGameCalculations():
    base2List = []
    base2Str = ""
    for i in range(len(biomeDiamonds)):
        if biomeDiamonds[i]%2 ==0:
            base2List.append(0)
        else:
            base2List.append(1)
    print "The base2 number created from the diamonds in the biomes is,", base2List
    base10Conversion = 0
    j = len(base2List)-1
    for i in range(len(base2List)):
        if base2List[i] == 0:
            base10Conversion += 0
        elif base2List[i] == 1:
            if i == len(base2List):
                base10Conversion += 1
            else:
                base10Conversion += 2**j
        j -= 1
    print "And so, lo and behold, your final score is....", base10Conversion

def catastropheGenerator(): # Generates position of catastrophes, and removes the biome
    global catastrophePos
    global catastropheNumber
    global pythonShine
    catastrophePos = random.randint(1,5*(len(biomeList)))
    if catastrophePos < len(biomeList):
        print "A catastrophe has occured in biome", catastrophePos
        print "Biome", catastrophePos, "has been destroyed!"
        biomeList.remove(catastrophePos)
        catastropheNumber += 1
        if playerPos == catastrophePos:
            playerHealth = 0
            print playerName, "has been caught in the catastrophe!"
        if pythonShine == catastrophePos:
            pythonShine = -1
        else:
            pythonShine -= 1
        for j in range(len(biomeList)):
            if j >= catastrophePos:
                biomeList[j] -= 1


# EXECUTION TOP LEVEL

# WHILE LOOP
while gameOn == True:
    gameStart()
    readFile("biomesData1.txt")
    biomeDataParser(localList)
    pythonShineGenerator()
    print
    biomeTable()
    print 
    enterInfo()
    while roundOn == True:
        t.speed(0)
        print 
        biomeTable()
        print 
        playerInfo()
        drawBoard()
        drawPlayer()
        print 
        turnGenerator()
        diamondCalculator()
        combatCalculator()
        print
        gameCheck()
        if catastrophe == True:
            catastropheGenerator()
        gameCheck()
        t.clearscreen()

    print 
    biomeTable()
    print 
    playerInfo()
    roundReset()

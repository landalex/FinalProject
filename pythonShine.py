# PYTHON LOL (Name a Work in Progess)
# Created by Evan Chisholm and Alex Land

import random
import turtle as t

# VARIABLES

godMode = ""
biomePosition = ""
fillColor = "tan"
catastropheNumber = 0

# FUNCTIONS

def gameStart():
    global godMode
    godMode = ""
    while godMode == "":
        godModeInput = raw_input("Would you like to manually choose biomes (y/n)? ")
        if godModeInput == "y":
            godMode = 1
        elif godModeInput == "n":
            godMode = 0
        else:
            print "Please enter y for yes or n for no."
    return godMode

def biomeGenerator(godMode):
    global biomePosition
    biomePosition = ""
    if godMode == 1:
        biomePosition = input("Which biome would you like to start at (Pick a number between 1 and 8)? ")
    if godMode == 0:
        biomePosition = random.randint(1,8)
    return biomePosition

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

def read_string_list_from_file(the_file):
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


def create_lists_board(listStrings):
    
    '''
    RECOMMENDED
    '''
    # your code...   
    
    return #.... as many lists as needed to represent the board
           # one for the diamonds values, etc.



def show_board(mssg):
    '''
    RECOMMENDED
    '''
    print "\nShowing board... " + mssg 
    print "\n The board at this point contains..."

    # your code... 


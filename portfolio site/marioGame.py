# MyMarioGame_A5.py
# 
# Description: Mario game has depicted in the sample runs 1, 2 and 3.
#               I pasted my assignmnet 4 below. Now I will work on the
#               game engine of the samples
#
# Author: AL + Mike Lazarevic
# Date: Nov. 2023


#-------- Assignment 4 section --------


def createMaze(aMaze, aWidth, aHeight, aCell):
    ''' Create and return "aMaze" of "aWidth" by "aHeight".
        Each cell of the maze is a string set to "aCell".      
    '''
    aMaze = [ [ (aCell) for i in range(aWidth) ] for j in range(aHeight) ]
    
    return aMaze

# -------------------------------------------------------------------

# Print Maze - This function is to used for testing and debugging purposes only!
def printMaze(aMaze, aHeight):
    ''' Print "aMaze" of "aHeight" - for testing and debugging purposes.
    ''' 
    for row in range(aHeight):
        print(aMaze[row])  
    return
		
# -------------------------------------------------------------------

def createBoundaryList(aWidth, bH = "---"):
    ''' Create and return a list that contains 2 lists: the first list
        is the top boundary of the maze and contains a string set to "bH".
        The second list is the bottom boundary of the maze and it also
        contains a string set to "bH".

        Other parameter:
         "aWidth" is the width of the maze.
    '''
    return list([[(bH) for number in range(aWidth)],
                 [(bH) for number in range(aWidth)]])                

# -------------------------------------------------------------------

def displayMaze(aMaze, aWidth, aHeight, hBoundary, bS = "|" ):
    ''' Display "aMaze" with column numbers at the top and row numbers
        to the left of each row along with the top and the bottom boundaries
        "hBoundary" that surround the maze.

        Other parameters:
         "aWidth" is the width of the maze.
         "aHeight" is the height of the maze.
         "bS" is the symbol used for the vertical border.
    '''
    
    offset = 3
    aString = (offset+1) * " "

    print()  
    # Display a row of numbers from 1 to aWidth
    for column in range(aWidth):
        aString = aString + str(column+1) + " "
        if len(str(column+1)) == 1 :
            aString += " "           
    print(aString)

    # Display the top boundary of maze
    print(offset * " " + "".join(hBoundary[0])) 
    
    # Display a column of numbers from 1 to aHeight
    # + left and right boundaries of the maze
    for row in range(aHeight):
        pre = str(row+1) + " " + bS

        # If the displayed row number is >= 10 - adjusting for extra digit
        if row >= 9: # Here 9 since we start at 0
           pre = str(row+1) + bS

        post = bS
        aRow = pre + ''.join(aMaze[row]) + post
        print(aRow)

    # Display the bottom boundary of maze
    print(offset * " " + "".join(hBoundary[1]))
    
    return

# -------------------------------------------------------------------

def placeExitGate(aWidth, aHeight, rowMario, columnMario, hBoundary,
                  exitGate = " = "):
    ''' Place the "exitGate" at the opposite corner of Mario's location.
	In other words, place the "exitGate" either in the top boundary or 
	in the bottom boundary whichever is at the opposite corner of
	Mario's location at coordinates ("columnMario","rowMario").

        Other parameters:
         "aWidth" is the width of the maze.
         "aHeight" is the height of the maze.
         "hBoundary" is a list of 2 lists: the first list is the top boundary
                                   and the second list is the bottom boundary.

        Returned value:
         "hBoundary" updated.
         "exitGateLocationList" contains coordinates x and y of the "exitgate".
    '''
    
    exitGateRight = False
    exitGateBottom = False

    # Create "exitGateLocationList" with initial location of "exitGate"
    # at the top left of maze
    exitGateLocationList.insert(0, 0)   
    exitGateLocationList.insert(1, 0)
    
    # Where is Mario?
    # If Mario is top left then exit gate is bottom right
    if columnMario <= ((aWidth) // 2) : # Mario on the left?
        exitGateLocationList[1] = aWidth - 1  # Yes, then "exitGate" on right
        exitGateRight = True
    # No, then assuption holds -> exit gate on the left
    if rowMario <= ((aHeight) // 2) :   # Mario at the top?
        exitGateLocationList[0] = aHeight - 1  # Yes, then "exitGate" at bottom
        exitGateBottom = True
        # No, then initial position of "exitGate" holds at the top left of maze

    # Place "exitGate" in appropriate top/bottom boundary
    if exitGateBottom :
        del hBoundary[1][exitGateLocationList[1]]
        hBoundary[1].insert(exitGateLocationList[1], exitGate)
    else:
        del hBoundary[0][exitGateLocationList[1]]
        hBoundary[0].insert(exitGateLocationList[1], exitGate)       

    # Can return a tuple -> elements sepatared by a coma
    return hBoundary, exitGateLocationList  

# -------------------------------------------------------------------


# ***Main part of the program

# Welcome the user and identify the game
print("""Welcome to my Mario game.\n""")

# Ask user for filename
#######filename = input("Please, enter a filename: ")

# Open file for reading
filename_open = open("InputData.txt", 'r')
lines = filename_open.readlines()

# Read the content of the file, one line at a time, and initialize 
# the following variables in the order these variables are listed
# mazeWidth, mazeHeight, aNumOfTreasures, aNumOfBombs must be assigned
# an integer value

mazeWidth = int(lines[0])
mazeHeight = int(lines[1])
aNumOfTreasures = int(lines[2])
aNumOfBombs = int(lines[3])

# emptyCell, obstacle, mario must be assigned a string
emptyCell = lines[4][0:3] #The second index gets the whitespaces needed
obstacle = lines[5][0:3]
mario = lines[6][0:3]

# marioLocationList must contain a list with two elements
# (of type "str") representing the coordinates x and y of Mario's
# location in the maze. For example: ['0', '0']
marioLocationList = (lines[7]).split() # get result list of ['9', '8']
# Turn to integers in order to + 1 the location
x = int(marioLocationList[1]) + 1
# Also I am setting x to take index 1, which is '8' and y '9'
y = int(marioLocationList[0]) + 1 
marioLocationList = [str(x),str(y)] # Now Mario's coord's-> x=9 and y=10 as int

# obstacleLocationDict must be a dictionary with items formatted as
# follows: {(x,y): -1} if there is a bomb in the cell at location x,y 
# in the maze and {(x,y): 1} if there is a treasure at the location x,y
# in the maze. If the cell is empty at the location x,y in the maze,
# this location is not stored in the dictionary obstacleLocationDict
obstacleLocationDict = {}

for line in lines[8:23]: # extracts each line from txt file (treasure ones)
    num_treasure = line.strip().split() # removes whitespaces AND places
                                        # each number to a list (split apart)

    # If the line includes 2 numbers (what I did to it above)
    # Then the expression is true and will:
    if num_treasure:        
        x = int(num_treasure[1]) + 1 #switch the index locations to x and y
        y = int(num_treasure[0]) + 1 # Also convert numbers to integers to + 1
                                    # +1 allows it to fit properly in grid
        obstacleLocationDict[(x,y)] = 1
        #Now each line's key is set to a value of 1 since it's a treasure

# Now doe the BOMBS###
for line in lines[23:53]: # Same as previous but from lines 23 to 53 
    num_bomb = line.strip().split()
    if num_bomb:
        x = int(num_bomb[1]) + 1
        y = int(num_bomb[0]) + 1
        obstacleLocationDict[(x,y)] = -1 # make sure the bomb keys are set to -1


# bombScoreRatio must be assigned an integer value
bombScoreRatio = int(lines[53]) # takes line 53 = '3' and turns to integer


# For testing and debugging purposes
#print(f"mazeWidth = {mazeWidth}")
#print(f"mazeHeight = {mazeHeight}")
#print(f"aNumOftreasures = {aNumOfTreasures}")
#print(f"aNumOfBombs = {aNumOfBombs}")
#print(f"emptyCell = '{emptyCell}'")
#print(f"obstacle = '{obstacle}'")
#print(f"mario = '{mario}'")     
#print(f"marioLocationList = {marioLocationList}")
#print(f"obstacleLocationDict = {obstacleLocationDict}")
#print(f"bombScoreRatio = {bombScoreRatio}")

# Close the file
filename_open.close()

# Create a maze
theMaze = list()
theMaze = createMaze(theMaze, mazeWidth,  mazeHeight, emptyCell)

# Create the top and bottom boundaries of the maze
# These boundaries are not part of the maze
hBoundary = list()
hBoundary = createBoundaryList(mazeWidth, bH= '---')

# Place the character (string) "obstacle" in the maze
# This is how we hide the treasures and bombs from the player

# Iterates through each index (Row) of the length in theMaze
for locationX in range(len(theMaze)): 
    # then by iterating again, it goes through each element
    # of the current row, therefore, goes through y at x 
    for locationY in range(len(theMaze[locationX])):

# When it goes though everything. We need to make sure that the coordiantes (x,y)
# are proper. By making it match theMaze, since the numbers around it make it +1
# for x and y. AND we must reverse x and y.
#Now IF this new coordinate(+1) is in the dictionary:
        if (locationY +1, locationX+1) in obstacleLocationDict:
#Then that location in theMaze equals obstacle
            theMaze[locationX][locationY] = obstacle

# Place Mario in the maze
# Put your code here!
MarioX = int(marioLocationList[0]) #Converted to int and isolated list to X
MarioY = int(marioLocationList[1]) # isolated Y as an integer
#BECAUSE theMaze indexes are integers so that's how it can == with locX & locY
#Go through all of the colums (locX) of the grid (theMaze)
for locX in range(len(theMaze)):
    #Now, Go through the rows (locY) location of y from theMaze at locX
    for locY in range(len(theMaze[locX])):

        #If locX and locY (+1 each) matches the location
        # of marioocationList (x,y). Then replace that
        # location in theMaze with mario (' M ')
        if locX+1== MarioX and locY+1 == MarioY:
            theMaze[locY][locX] = mario


         
# Call the appropriate function which computes the location of the
# exit gate and places it in either the top or the bottom boundary
exitGateLocationList = list()
# (x,y) from marioLocationList seperated to integers by rows and column
rowMario = int(marioLocationList[0])
columnMario = int(marioLocationList[1])

# Now, I am able to plug marioLocationList into placeExitGate properly
# Into the correct parameter
placeExitGate(mazeWidth, mazeHeight, rowMario, columnMario,
              hBoundary, exitGate = " = ")

# Call the appropriate function to display the maze 
#displayMaze(theMaze, mazeWidth, mazeHeight, hBoundary, bS = "|" )

#print("\n-------")


#------ Assignment 5 starts here ------
      
# Set Mario's score - Done!
# Setting Marios's score has already been done for you
# so you do not have to add any code to the following line:
marioScore = aNumOfBombs // bombScoreRatio

#--- The Algorithm for Assignment 5 starts here ---
# This is the algorithm of the game engine, expressed as comments.
# Your task is to convert these comments into corresponding Python code.

# Set the condition variables for your loop
playing = True
x,y = 0,0 # initialize variable that affects marios location at each input
marioLocationList = [rowMario, columnMario]
win = False
# As long as the player is playing AND marioScore > 0 AND
# Mario has not reached the exit gate, loop i.e., play:


#Moves the mario and ends the game is needed with playing and win
def marioMoves(x,y, marioLocationList,marioScore, win, playing):

        #All the work is here since the new location is affected by
        # the inputs of x and y changing it's location appropriately
        marioNewLocationList = (marioLocationList[0]+x,marioLocationList[1]+y)
        #print(marioNewLocationList)
        #print(exitGateLocationList)   #for help#
           
             # If Mario new location is still within the maze, i.e.,
        if 1 <= marioNewLocationList[1] <= mazeWidth and 1 <= marioNewLocationList[0] <= mazeHeight:
        # Erase Mario from his current location in the maze
            theMaze[marioLocationList[1] - 1][marioLocationList[0] - 1] = emptyCell
            # -1 to meet maze coord's!!!
        # Move Mario to his new location in the maze
            theMaze[marioNewLocationList[1] - 1][marioNewLocationList[0] - 1] = mario

            
        # Check whether Mario has stepped onto an obstacle and update Mario's score
            if marioNewLocationList in obstacleLocationDict:
                #Store the value of the key of the dictionary mario's location matches
                ValueOfObstacle = obstacleLocationDict.get(marioNewLocationList,0)
                # Change mario's score accordingly to the Value of the key
                marioScore += ValueOfObstacle

            marioLocationList = marioNewLocationList

        if marioScore == 0:
            print("\nMario's score is now down to 0! Sorry! You have lost!")
            #I don't need to add Playing = False or soemthing since the while loop will stop

            
        if exitGateLocationList[0]<mazeWidth/2: #Means that exit gate is on top left of grid

            #I added one to gate index 1 since the gate is "outside the grid" since
            # It is on the boundry and mario can not reach it. I modified the location of it
            # when it is at the top right to be "inside the grid for x but outside with Y

            #Therefore when mario inputs 'u' as it's tight below it, they will match locations
            # therefore, winning the game.

            #If this is confusing uncomment the print statements at the start of the function
            #To understadn each updated location of mario and the constant gate
            if marioNewLocationList == (exitGateLocationList[1]+1,exitGateLocationList[0]):
                win = True
                print(f'\nMario has reached the exit gate with a score of {marioScore}! Yay! You win!')
        if exitGateLocationList[0]>mazeWidth/2: #Means that exit gate is on bottom right of grid
            if marioNewLocationList == (exitGateLocationList[1],exitGateLocationList[0])+1:
                win = True
                print(f'\nMario has reached the exit gate with a score of {marioScore}! Yay! You win!')


        return x, y, marioLocationList, marioScore, win, playing



#Repeat loop as long as user is playing, has a score above 0 and did not win(yet)
    
while playing and marioScore > 0 and not win:

  # Display Mario's Sample Runs layout with the following code
    displayMaze(theMaze, mazeWidth, mazeHeight, hBoundary, bS = "|" )
    
    print(f"\nMario's score -> {marioScore}.")
  
  
    move = input("\nMove Mario by entering the letter 'r' for right, 'l' for left,"
          "'u' for up and 'd' for down, 'x' to exit the game: ")
  
     
    if move.lower() == 'r':
        x,y = 1,0

    elif move.lower() == 'l':
        x,y = -1,0      

    elif move.lower() == 'u':
        x,y = 0,-1      

    elif move.lower() == 'd':
        x,y = 0,1     

    elif move.lower() == 'x':
        playing = False

    else:
        print('\n\nsorry invalid input')
        x,y = 0,0 # make sure mario does NOT move it's previous direction
                  # that was inputed for move if an invalid 



    #Call function with the NEW variable changes from inputs and make sure that it will run if
    # user is playing, not win, and above 0 score
    x,y, marioLocationList, marioScore, win, playing = marioMoves(x, y, marioLocationList, marioScore, win, playing)



#When while loop is done: then end the program
print("\nBye!")
print("\n-------")

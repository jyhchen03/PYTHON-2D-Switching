from easygui import *
#createGrid: takes a specified length and width and creates a grid
#arguments: length, int as length of the grid; width, int as width of the grid
#returns: glist, list containing each list
def createGrid(length, width):
    glist = []
    for i in range(width):
        glist.append([]) #lists inside lists that act as different rows
        for j in range(length):
            glist[i].append(1)
    return glist

#changeGrid: takes grid printed out as a list and changes into grid with strings instead (much neater)
#arguments: grid, grid being changed into neater version
#returns: string, str with grid after being changed into neater version
def changeGrid(grid):
    string = ""
    for i in range(len(grid)):
        for j in grid[i]:
            string += str(j)
            string += " "
        string += "\n"
    return string

#switchNum: switches numbers from 1 to 0 or 0 to 1
#arguments: num, the int being switched
#returns: either 1 or 0
def switchNum(num):
    if num == 1:
        return 0
    if num == 0:
        return 1
    
#coordIndex: algorithm for taking specified coordinate and all coordinates around it into a list to modify later
#arguments: grid, list of lists with 1s and 0s; xco, x coordinate; yco, y coordinate
#returns: list of lists with specified coordinates
def coordIndex(grid, xco, yco):
    indlist = []
    for i in range(yco-1, yco+2):
        for j in range(xco-1, xco+2):
            if ((i-1)<len(grid) and i>0) and ((j-1)<len(grid) and j>0):
                indlist.append([i-1, j-1])
    return indlist

#changeNum: goes through grid and takes specified coordinate and surrounding coordinates and switches them
#arguments: grid, list of lists with 1s and 0s; xco x coordinate, yco, y coordinate
#returns: new grid with changed values
def changeNum(grid, xco, yco):
    index = coordIndex(grid, xco, yco)
    for i in index:
        grid[i[0]][i[1]] = switchNum(grid[i[0]][i[1]])
    return grid


#program body
userinp = raw_input("Please input grid size: ")
base = int(userinp)
grid = createGrid(base, base)
while userinp != 'n':
    userinp = raw_input("Please input x-coordinate: ")
    xcoordinate = int(userinp)
    userinp = raw_input("Please input y-coordinate: ")
    ycoordinate = int(userinp)
    grid = changeNum(grid, xcoordinate, ycoordinate)
    print changeGrid(grid)
    userinp = raw_input("Would you like to reset grid? <y/n> ")
    if userinp == 'y':
        userinp = raw_input("Would you like to change grid size? <y/n> ")
        if userinp == 'y':
            userinp = raw_input("Please input grid size: ")
            base = int(userinp)
        grid = createGrid(base, base)
    userinp = raw_input("Would you like to continue? <y/n> ")
    if userinp == 'n':
        print "The user has exited the program. Goodbye!"


import turtle
import pens
import bfsSearch
import dfsSearch
import uniformCostSearch
import values
#wn.setup(700,700)

def setupMaze():
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("A Maze Game")
    wn.setup(values.screenWidth, values.screenHeight)

    level_1 = []
    pos = 0
    for y in range(0,values.mazeWidth):
        insertLevel = ""
        for x in range(0,values.mazeHeight + 1):
            if values.insertLevelStr[pos] != "\n":
                insertLevel += values.insertLevelStr[pos]
            pos += 1
        level_1.append(insertLevel)



    levels = [""]


    levels.append(level_1)



    def setup_maze(level):
        pen = pens.Pen()
        MainCharacter = pens.MainCharacter()
        treasure = pens.Treasure()
        characterposition = (0,0)
        treasureposition = (0,0)
        for y in range(len(level)):
            for x in range(len(level[y])):
                character = level[y][x]
                screen_x = (values.screenWidth/2) + ((-1*values.screenWidth - (24 * values.mazeWidth))/2) + (x * 24)
                screen_y = (-1*values.screenHeight/2) + ((values.screenHeight + (24 * values.mazeHeight))/2) - (y * 24)
                if character == "X":
                    pen.goto(screen_x, screen_y)
                    pen.stamp()
                if character == "T":
                    treasureposition = (screen_x, screen_y)
                    treasure.goto(screen_x, screen_y)
                    treasure.stamp()
                if character == "C":
                    characterposition = x, y
                    MainCharacter.goto(screen_x, screen_y)
                    MainCharacter.stamp()
        #call for the path finder
        if values.algorithmType == 1:
            bfsSearch.bfs(characterposition, treasureposition)
        if values.algorithmType == 2:
            dfsSearch.dfs(characterposition, treasureposition)
        if values.algorithmType == 3:
            uniformCostSearch.ucs(characterposition, treasureposition)




    setup_maze(levels[1])

    wn.mainloop()
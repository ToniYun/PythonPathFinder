import turtle
import pens

#wn.setup(700,700)

def setupMaze(screenWidth,screenHeight,mazeWidth,mazeHeight, insertLevelStr):
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("A Maze Game")
    wn.setup(int(screenWidth), int(screenHeight))

    level_1 = []
    pos = 0
    for y in range(0,int(mazeWidth)):
        insertLevel = ""
        for x in range(0,int(mazeHeight) + 1):
            if insertLevelStr[pos] != "\n":
                print(pos, end=" ")
                insertLevel += insertLevelStr[pos]
            pos += 1
        print('\n')
        level_1.append(insertLevel)



    levels = [""]


    levels.append(level_1)



    def setup_maze(level):
        for y in range(len(level)):
            for x in range(len(level[y])):
                character = level[y][x]
                screen_x = (int(screenWidth)/2) + ((-1*int(screenWidth) - (24 * int(mazeWidth)))/2) + (x * 24)
                screen_y = (-1*int(screenHeight)/2) + ((int(screenHeight) + (24 * int(mazeHeight)))/2) - (y * 24)#288 - (y * 24)
                if character == "X":
                    pen.goto(screen_x, screen_y)
                    pen.stamp()
                if character == "T":
                    treasure.goto(screen_x, screen_y)
                    treasure.stamp()
                if character == "C":
                    MainCharacter.goto(screen_x, screen_y)
                    MainCharacter.stamp()
        #call for the path finder

    pen = pens.Pen()
    movement = pens.Movement()
    MainCharacter = pens.MainCharacter()
    treasure = pens.Treasure()

    setup_maze(levels[1])

    wn.mainloop()
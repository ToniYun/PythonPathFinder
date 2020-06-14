import turtle


#wn.setup(700,700)

def setupMaze(screenWidth,screenHeight,mazeWidth,mazeHeight):
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("A Maze Game")
    wn.setup(int(screenWidth), int(screenHeight))

    level_1 = []
    for x in range(0,int(mazeWidth)):
        insertLevel = ""
        for y in range(0,int(mazeHeight)):
             insertLevel += "X"
        level_1.append(insertLevel)


    class Pen(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("white")
            self.penup()
            # self.pensize(25)
            self.speed(0)

    levels = [""]


    levels.append(level_1)



    def setup_maze(level):
        for y in range(len(level)):
            for x in range(len(level[y])):
                character = level[y][x]
                screen_x = (int(screenWidth)/2) + ((-1*int(screenWidth) - (24 * int(mazeWidth)))/2) + (x * 24)
                screen_y = (-1*int(screenHeight)/2) + ((int(screenHeight) - (24 * int(mazeHeight)))/2) + (y * 24)#288 - (y * 24)
                if character == "X":
                    pen.goto(screen_x, screen_y)
                    pen.stamp()

    pen = Pen()

    setup_maze(levels[1])

    while True:
        pass
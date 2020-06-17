import tkinter
import values

def mazeDraw():
    def bfs():
        values.algorithmType = 1
        sendToMaze()
    def dfs():
        values.algorithmType = 2
        sendToMaze()
    def ucs():
        values.algorithmType = 3
        sendToMaze()
    def sendToMaze():
        values.insertLevelStr = list(TextIn.get("1.0",'end-1c'))
        newWindow.destroy()
        import maze
        maze.setupMaze()

    newWindow = tkinter.Tk()
    newWindow.title("GUI")
    height = values.mazeHeight * 24
    width = values.mazeWidth * 24
    newWindow.geometry(str(height) + "x" + str(width))
    insertLevel = ""
    for x in range(0, values.mazeWidth):
        for y in range(0, values.mazeWidth):
            insertLevel += "X"
        insertLevel += "\n"
    TextIn = tkinter.Text(newWindow)
    BFS = tkinter.Button(
        text="BFS",
        width = 25,
        height = 3,
        command = bfs
    )
    DFS = tkinter.Button(
        text="DFS",
        width = 25,
        height = 3,
        command = dfs
    )
    button = tkinter.Button(
        text="UCS",
        width = 25,
        height = 3,
        command = ucs
    )
    TextIn.pack()
    TextIn.insert(tkinter.END,insertLevel)
    BFS.pack()
    DFS.pack()
    button.pack()
    newWindow.mainloop()
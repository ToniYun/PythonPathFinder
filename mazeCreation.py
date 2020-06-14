import tkinter

window = tkinter.Tk()
window.title("GUI")
height = 25 * 24 # mazeheight * 24
width = 25 * 24 # mazewidth * 24
window.geometry(str(height) + "x" + str(width))
insertLevel = ""
for x in range(0, int(25)):#mazeWidth)):
    for y in range(0, int(25)):#mazeHeight)):
        insertLevel += "X"
    insertLevel += "\n"
TextIn = tkinter.Text(window)
button = tkinter.Button(
    text="Set Maze",
    width = 25,
    height = 3,
)
TextIn.pack()
TextIn.insert(tkinter.END,insertLevel)
button.pack()
window.mainloop()
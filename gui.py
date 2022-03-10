from tkinter import *
from PIL import ImageTk, Image

root = Tk()

canv = Canvas(root, width=1080, height=1920, bg='white')
canv.grid(row=2, column=3)

img = ImageTk.PhotoImage(Image.open("src/photo.jpg"))

def game1():
    import Snake
button1 = Button(root, text="SNAKE",command=game1)

def game2():
    import Pong
button2 = Button(root, text="PONG",command=game2)

def game3():
    import Tetris
button3 = Button(root, text="TETRIS",command=game3)

def game4():
    import
button4 = Button(root, text="STACK",command=game4)

canv.create_image(20, 20, anchor=NW, image=img)
button1_canvas = canv.create_window(500, 200,
                                       anchor="nw",
                                       window=button1)

button2_canvas = canv.create_window(500, 300,
                                       anchor="nw",
                                       window=button2)

button3_canvas = canv.create_window(500, 400, anchor="nw",
                                       window=button3)

button4_canvas = canv.create_window(500, 500, anchor="nw",
                                       window=button4)

mainloop()

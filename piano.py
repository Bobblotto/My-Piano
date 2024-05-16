import pygame
from tkinter import *

pygame.init()

window = Tk()
window.title = "My Piano"

window.minsize(315, 150)

c = "PIANO/assets/c4.mp3"
d = "PIANO/assets/d4.mp3"
e = "PIANO/assets/e4.mp3"
f = "PIANO/assets/f4.mp3"
g = "PIANO/assets/g4.mp3"
a = "PIANO/assets/a5.mp3"
b = "PIANO/assets/b5.mp3"

cs = "PIANO/assets/c-4.mp3"
ds = "PIANO/assets/d-4.mp3"
fs = "PIANO/assets/f-4.mp3"
gs = "PIANO/assets/g-4.mp3"
_as = "PIANO/assets/a-5.mp3"

offset = 0
ypos = 0

def keypress(key, index):
    print(key, str(index))
    
    sound = pygame.mixer.Sound(key)
    sound.play()


C1 = Button(bg="white", text="C1", command=lambda:keypress(c, 1), width=5, height=10)
C1.place(x=offset, y=ypos)
offset += 45

D1 = Button(bg="white", command=lambda:keypress(d, 1), width=5, height=10)
D1.place(x=offset, y=ypos)
offset += 45

E1 = Button(bg="white", command=lambda:keypress(e, 1), width=5, height=10)
E1.place(x=offset, y=ypos)
offset += 45

F1 = Button(bg="white", command=lambda:keypress(f, 1), width=5, height=10)
F1.place(x=offset, y=ypos)
offset += 45

G1 = Button(bg="white", command=lambda:keypress(g, 1), width=5, height=10)
G1.place(x=offset, y=ypos)
offset += 45

A1 = Button(bg="white", command=lambda:keypress(a, 1), width=5, height=10)
A1.place(x=offset, y=ypos)
offset += 45

B1 = Button(bg="white", command=lambda:keypress(b, 1), width=5, height=10)
B1.place(x=offset, y=ypos)

offset = 32.5

Db1 = Button(bg="black", command=lambda:keypress(cs, 1), width=2, height=5)
Db1.place(x=offset, y=ypos)
offset += 45

Db1 = Button(bg="black", command=lambda:keypress(ds, 1), width=2, height=5)
Db1.place(x=offset, y=ypos)
offset += 90

Db1 = Button(bg="black", command=lambda:keypress(fs, 1), width=2, height=5)
Db1.place(x=offset, y=ypos)
offset += 45

Db1 = Button(bg="black", command=lambda:keypress(gs, 1), width=2, height=5)
Db1.place(x=offset, y=ypos)
offset += 45

Db1 = Button(bg="black", command=lambda:keypress(_as, 1), width=2, height=5)
Db1.place(x=offset, y=ypos)
offset += 45


window.mainloop()
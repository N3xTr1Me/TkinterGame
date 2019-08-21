import tkinter as tk
import random as rn

def k_prsd(event):
    if event.keysym == 'Up':
        canvas.move(pl, 0, -(step))
    if event.keysym == 'Down':
        canvas.move(pl, 0, step)
    if event.keysym == 'Left':
        canvas.move(pl, -(step), 0)
    if event.keysym == 'Right':
        canvas.move(pl, step, 0)

class Player():

    def __init__(this, clr):
        this.x = this.randomPoz(N_X)
        this.y = this.randomPoz(N_Y)
        this.color = clr

    def draw(this):
        a = canvas.create_oval((this.x, this.y),
                           (this.x+step, this.y+step),
                            fill = this.color)
        return a
        
    def randomPoz(this, top):
        return rn.randint(1, top - 1)*step

master = tk.Tk()
step = 60
N_X = 10
N_Y = 10
canvas = tk.Canvas(master, bg = '#00FFFF', height = step*N_X, width = step*N_Y)

player = Player('#32CD32')
pl = (player.draw())
exit_g = Player('#FFD700')
exit_g.draw()

canvas.pack()
master.bind('<KeyPress>', k_prsd)
master.mainloop()









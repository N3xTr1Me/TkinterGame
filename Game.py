import tkinter as tk
import random as rn

class Player():

    def __init__(this, clr):
        this.x = this.randomPoz(N_X)
        this.y = this.randomPoz(N_Y)
        this.color = clr

    def draw(this):
        canvas.create_oval((this.x, this.y),
                           (this.x+step, this.y+step),
                            fill = this.color)
        
    def randomPoz(this, top):
        return rn.randint(1, top - 1)*step

master = tk.Tk()
step = 60
N_X = 10
N_Y = 10
canvas = tk.Canvas(master, bg = '#04F8D3', height = step*N_X, width = step*N_Y)

player = Player('#04EFF6')
player.draw()
exit_g = Player('#F6DA08')
exit_g.draw()



canvas.pack()
master.mainloop()












import tkinter as tk
import random as rn

def k_prsd(event):
    if event.keysym == 'Up' or event.keysym == 'w':
        player.y -= step
        reDraw(pl, 0, -(step))
    if event.keysym == 'Down' or event.keysym == 's':
        player.y += step
        reDraw(pl, 0, step)
    if event.keysym == 'Left' or event.keysym == 'a':
        player.x -= step
        reDraw(pl, -(step), 0)
    if event.keysym == 'Right' or event.keysym == 'd':
        player.x += step
        reDraw(pl, step, 0)
    endGame()

def add_enemies():
    for i in range(6):
        enemy = Enemy()
        enemy.draw()
        enemies_s.append(enemy)

def reDraw(obj, x, y):
    canvas.move(obj, x, y)

def endGame():
    if player.comparePoz(exit_g):
        print('GG')
        print('U won!!!')

class Player:

    def __init__(this, clr):
        this.x = this.randomPoz(N_X)
        this.y = this.randomPoz(N_Y)
        this.color = clr
        this.draw()

    def draw(this):
        body = canvas.create_oval((this.x, this.y),
                                  (this.x+step, this.y+step),
                                   fill = this.color)
        return body
        
    def randomPoz(this, top):
        return rn.randint(1, top - 1)*step

class Exit(Player):
    def __init__(this):
        super().__init__('#FFD700')

class Enemy(Player):
    def __init__(this):
        super().__init__('#32CD32')

class Hero(Player):
    def __init__(this):
        super().__init__('red')
        
    def comparePoz(this, other):
        return this.x == other.x and this.y == other.y

master = tk.Tk()
step = 60
N_X = 10
N_Y = 10
enemies_s = []
canvas = tk.Canvas(master, bg = '#00FFFF', height = step*N_X, width = step*N_Y)

exit_g = Exit()
add_enemies()
player = Hero()

canvas.pack()
master.bind('<KeyPress>', k_prsd)
master.mainloop()









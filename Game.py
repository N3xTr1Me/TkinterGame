import tkinter as tk
import random as rn

def k_prsd(event):
    keys = {'Up', 'w', 'Down', 's', 'Left', 'a', 'Right', 'd'}
    if event.keysym in keys:
        keyListener(event.keysym)
        enemiesTurn()
        endGame()

def keyListener(key):
    if key == 'Up' or key == 'w':
        player.reDraw(0, -(step))
    elif key == 'Down' or key == 's':
        player.reDraw(0, step)
    elif key == 'Left' or key == 'a':
        player.reDraw(-(step), 0)
    elif key == 'Right' or key == 'd':
        player.reDraw(step, 0)

def enemiesTurn():
    for enemy in enemies_d:
        enemy.randMove()

def add_enemies():
    for i in range(6):
        enemy = Enemy()
        enemies_s.append(enemy)
    for i in range(3):
        enemy = EnemyD()
        enemies_d.append(enemy)
        
def endGame():
    if player.comparePoz(exit_g):
        print('GG')
        print('U won!!!')
    enemies = enemies_d + enemies_s
    for enemy in enemies:
        if player.comparePoz(enemy):
            print('Game Over')
            print('U suck!!!')
            break

class Player:

    objects = set = {(-1,-1)}

    def __init__(this, clr):
        this.x, this.y = -1, -1
        while (this.x, this.y) in Player.objects:
            this.x = this.randomPoz(N_X)
            this.y = this.randomPoz(N_Y)
        Player.objects.add((this.x, this.y))
        this.color = clr
        this.draw()

    def draw(this):
        this.body = canvas.create_oval((this.x, this.y),
                                       (this.x+step, this.y+step),
                                        fill = this.color)
        
    def randomPoz(this, top):
        return rn.randint(1, top - 1)*step

    def reDraw(this, x, y):
        ol_x, ol_y = this.x, this.y
        this.x = (this.x + x) % (step*N_X)
        this.y = (this.y + y) % (step*N_Y)
        canvas.move(this.body, (this.x - ol_x), (this.y - ol_y))

class Exit(Player):
    def __init__(this):
        super().__init__('#FFD700')

class Enemy(Player):
    def __init__(this, color = '#C71585'):
        super().__init__(color)

class EnemyD(Enemy):
    def __init__(this):
        super().__init__('#FF4500')

    def randMove(this):
        r = rn.randint(1,4)
        if   r == 1:
            super().reDraw(step, 0)
        elif r == 2:
            super().reDraw(-step, 0)
        elif r == 3:
            super().reDraw(0, step)
        else:
            super().reDraw(0, -step)
            

class Hero(Player):
    def __init__(this):
        super().__init__('#32CD32')
        
    def comparePoz(this, other):
        return this.x == other.x and this.y == other.y

master = tk.Tk()
step = 60
N_X = 10
N_Y = 10
enemies_s = []
enemies_d = []
canvas = tk.Canvas(master, bg = '#00FFFF', height = step*N_X, width = step*N_Y)

exit_g = Exit()
add_enemies()
player = Hero()

canvas.pack()
master.bind('<KeyPress>', k_prsd)
master.mainloop()









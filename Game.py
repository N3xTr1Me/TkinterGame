import tkinter as tk
import random as rn

def randomPoz(top):
    return rn.randint(1, top - 1)*step

master = tk.Tk()
step = 60
N_X = 10
N_Y = 10
canvas = tk.Canvas(master, bg = 'blue', height = step*N_X, width = step*N_Y)

player_pos = (randomPoz(N_X), randomPoz(N_Y))
exit_pos   = (randomPoz(N_X), randomPoz(N_Y))


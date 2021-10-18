from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']

class Sharik:
	def __init__(self,x,y,Vx,Vy,Ax,Ay,r):
		self.x = x
		self.y = y
		self.Vx = Vx
		self.Vy = Vy
		self.Ax = Ax
		self.Ay = Ay
		self.r = r
		self.ball = canv.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=choice(colors), width=0)
	def update(self):
		self.x += self.Vx
		self.y += self.Vy
		if self.x <= self.r:
			self.Vx = rnd(1,10)
			self.Vy = rnd(-10,10)
		if self.x >= 800-self.r:
			self.Vx = -rnd(1,10)
			self.Vy = rnd(-10,10)
		if self.y >= 600-self.r:
			self.Vy = -rnd(1,10)
			self.Vx = rnd(-10,10)
		if self.y <= self.r:
			self.Vy = rnd(1,10)
			self.Vx = rnd(-10,10)
		canv.move(self.ball,self.Vx,self.Vy)
		root.after(50, self.update)

def fullgame():
	ball1 = Sharik(rnd(50, 750), rnd(50, 550), rnd(-5, 5), rnd(-5, 5), 0, 0, rnd(20, 40))
	ball2 = Sharik(rnd(50, 750), rnd(50, 550), rnd(-5, 5), rnd(-5, 5), 0, 0, rnd(20, 40))
	ball3 = Sharik(rnd(50, 750), rnd(50, 550), rnd(-5, 5), rnd(-5, 5), 0, 0, rnd(20, 40))
	ball1.update()
	ball2.update()
	ball3.update()
	root.after(3000,fullgame)

fullgame()
mainloop()



	

import sys
# import tkinter as tk
import copy
from time import sleep
import tkinter as tk

# for search tiles around (0, 0)
trans = [[-1,-1], [ 0,-1], [ 1,-1],
		 [-1, 0],          [ 1, 0],
		 [-1, 1], [ 0, 1], [ 1, 1]]

#def printmap(gmap):
#	for row in gmap:
#		for c in row:
#			if(c == '#'):
#				print("■",end='')
#			else:
#				print("□",end='')
#			# print(c,end="")
#		print()

def countlives(gmap, j, i):
	xmax = len(gmap[0])
	ymax = len(gmap)
	cnt = 0
	for cup in trans:
		pos = []
		pos.append(i - cup[0])
		pos.append(j - cup[1])
		x = pos[0]
		y = pos[1]
		if(x >= 0 and x < xmax):
			if(y >= 0 and y < ymax):
				if(gmap[y][x] == '#'):
					cnt += 1
	return cnt

# return next generation
def nextmap(gmap):
	nmap = [[0 for i in range(len(gmap[0]))] for j in range(len(gmap))]
	for j in range(len(gmap)):
		for i in range(len(gmap[j])):
			lives = countlives(gmap, j, i)
			if(gmap[j][i] == '#'):
				if(lives == 2 or lives == 3):
					nmap[j][i] = '#'
				else:
					nmap[j][i] = '.'
			else:
				if(lives == 3):
					nmap[j][i] = '#'
				else:
					nmap[j][i] = '.'
	return nmap
# print(sys.argv[1])
f = open(sys.argv[1], 'r')

gmap = []
tkmap = []
i = 0
for row in f:
	tkmap.append([])
	gmap.append([])
	for j in range(len(row)):
		c = row[j]
		if(c != '\n'):
			gmap[i].append(c)
	i += 1
f.close()

boxscale = 15
root = tk.Tk()
canvas = tk.Canvas(root, width=50+boxscale*len(gmap[0]), height=50+boxscale*len(gmap))
canvas.pack()

for i in range(len(gmap)):
	tkmap.append([])
	for j in range(len(gmap[0])):
		tkmap[i].append(canvas.create_rectangle(10+boxscale*(j+1), 10+boxscale*(i+1), 20+boxscale*(j+1), 20+boxscale*(i+1), fill="#000"))

#while(true):
#	gmap = nextmap(gmap)
#	printmap(gmap)
#	sleep(0.1)

# a = canvas.create_rectangle(100, 200, 200, 300, fill="#000")
# b = canvas.create_rectangle(300, 200, 400, 300, fill="#000")

L = ["#000", "#fff"]

# def next():
# 	canvas.itemconfig(a, fill=L[0])
# 	canvas.itemconfig(b, fill=L[1])
# 	(L[0], L[1]) = (L[1], L[0])
# 	root.after(500, next)

def next():
	global gmap
	gmap = nextmap(gmap)
	for i in range(len(gmap)):
		for j in range(len(gmap[0])):
			if(gmap[i][j] == "#"):
				canvas.itemconfig(tkmap[i][j], fill=L[1])
				# tkmap[i][j] = L[1]
			else:
				canvas.itemconfig(tkmap[i][j], fill=L[0])
				# tkmap[i][j] = L[0]				
	root.after(500, next)

root.after(1000, next)
root.mainloop()

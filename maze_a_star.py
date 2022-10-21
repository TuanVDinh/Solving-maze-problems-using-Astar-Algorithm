
# Solving maze problems using A* Algorithm
# Tuan Van Dinh
# 29.June.2021
######################################################################################

######################################################################################
# Mission: In this game, you have to find a way to move a turtle (red) to a goal (yellow circle)
# How to control the turtle:
#	W: UP
#	S: DOWN
#	A: LEFT
#	D: RIGHT

# Press 1, 2, 3 or 4 to choose a maze

# left-click if you want to show the way (displayed in blue) to the goal

# Press c if you want to clear the way to the goal 
######################################################################################

import turtle                    
import time
from queue import PriorityQueue
from math import sqrt
import timeit

wn = turtle.Screen()                      # define the turtle screen
wn.bgcolor("white")                       # set the background colour
wn.title("Turtle moving through a maze")
wn.setup(1300,700)                        # setup the dimensions of the working window

# declare system variables
start_x = 0
start_y = 0
end_x = 0
end_y = 0
width = 24

start_state = (0, 0)
goal_state = (0, 0)
id_blue = []
id_maze = []
id_yellow = []
id_red = []

choosing_h = True   # This variable used to choose Manhattan or Euclidian distance
					# to calculate heuristic
					# If True, Manhattan distance will be used, 
					# If False, Euclidian distance will be used 
				  


# use black turtle to stamp out the maze
class Maze(turtle.Turtle):               # define a Maze class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            # the turtle shape
        self.color("black")             # colour of the turtle
        self.penup()                    # lift up the pen so it do not leave a trail
        self.speed(0)                   # define the animation speed

# use blue turtle to show the frontier cells
class Blue(turtle.Turtle):              
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

# use the red turtle to represent the start position
class Red(turtle.Turtle):               
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("red")
        self.setheading(0)  # point turtle to point right
        self.penup()
        self.speed(0)

# use the yellow turtle to represent the end position and the solution path
class Yellow(turtle.Turtle):           # code as above
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.speed(0)

# use the white turtle to hide all turtles at the centre of the screen
class White(turtle.Turtle):           # code as above
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
              
def up():
	global start_y
	red.penup()
	red.setheading(90)
	if (start_x, start_y + width) not in walls:
		red.forward(width)
		start_y += width
	
def down():
	global start_y 
	red.penup()
	red.setheading(270)
	if (start_x, start_y - width) not in walls:
		red.forward(width)
		start_y -= width

def left():
	global start_x
	red.penup()
	red.setheading(180)
	if (start_x - width, start_y) not in walls:
		red.forward(width)
		start_x -= width

def right():
	global start_x
	red.penup()
	red.setheading(0)
	if (start_x + width, start_y) not in walls:
		red.forward(width)
		start_x += width
	
def update_start_pos():
	start_state = (start_x, start_y)
	return start_state

def leftclick(x, y):
	clear_stamp()
	start_pos = update_start_pos()
	a_star(start_pos, goal_state)
	
def clear_stamp():

	for idx in id_blue:
		blue.clearstamp(idx)
	blue.ht()

def h_manhattan():
	global choosing_h
	choosing_h = True
	
def h_euclid():
	global choosing_h
	choosing_h = False

# Generating different mazes (1, 2, 3, or 4)
def gen_maze1():
	
	for idx in id_maze:
		maze.clearstamp(idx)
	
	for idx in id_yellow:
		yellow.clearstamp(idx)
		
	for idx in id_blue:
		blue.clearstamp(idx)
	
	id_maze.clear()
	id_yellow.clear()
	id_blue.clear()	
	path.clear()
	walls.clear()
	
	setup_maze(grid1)

def gen_maze2():
	for idx in id_maze:
		maze.clearstamp(idx)
	
	for idx in id_yellow:
		yellow.clearstamp(idx)
		
	for idx in id_blue:
		blue.clearstamp(idx)
	
	id_maze.clear()
	id_yellow.clear()
	id_blue.clear()	
	path.clear()
	walls.clear()
	
	setup_maze(grid2)
	
def gen_maze3():
	for idx in id_maze:
		maze.clearstamp(idx)
	
	for idx in id_yellow:
		yellow.clearstamp(idx)
		
	for idx in id_blue:
		blue.clearstamp(idx)
	
	id_maze.clear()
	id_yellow.clear()
	id_blue.clear()	
	path.clear()
	walls.clear()
	
	setup_maze(grid3)

def gen_maze4():
	for idx in id_maze:
		maze.clearstamp(idx)
	
	for idx in id_yellow:
		yellow.clearstamp(idx)
		
	for idx in id_blue:
		blue.clearstamp(idx)
	
	id_maze.clear()
	id_yellow.clear()
	id_blue.clear()	
	path.clear()
	walls.clear()
	
	setup_maze(grid4)
	

turtle.listen()

turtle.onkey(gen_maze1, "1")
turtle.onkey(gen_maze2, "2")
turtle.onkey(gen_maze3, "3")
turtle.onkey(gen_maze4, "4")

turtle.onkey(up, "w")
turtle.onkey(down, "s")
turtle.onkey(left, "a")
turtle.onkey(right, "d")
turtle.onkey(clear_stamp, "c")
turtle.onkey(h_manhattan, "m") # press key "m" to choose manhattan distance
turtle.onkey(h_euclid, "e")	   # press key "e" to choose euclidian distance
turtle.onscreenclick(leftclick, 1)

# 0: walls; 1: can go; s: start position of turtle; e: goal 
grid1 = [
"000000000000000",
"0s01111111010e0",
"010000010001010",
"010101111111010",
"010111000101010",
"010101011101010",
"011101010101010",
"000001010101010",
"011111010101110",
"000000000000000",
 ]

grid2 = [
"0000000000000000000000000000000000000000000000",
"01s1111111111111011111111111111111111111111110",
"0100000000000100000000000000010000000010000010",
"0111111111110111111111111111110111111110111110",
"0010000000100000000000000100000000000000000000",
"0010011110100111111111110100111111111111111110",
"0010010010100100100000100100100000000000000010",
"0010010010100100101111100100100100111111110010",
"0010010000100100000000000100100100000100010010",
"00100111001001111111111111001111111111000100e0",
"0010000100100000000000000000100000000000000010",
"0011110100111111111111111111100111111111111110",
"0000010100000000000000000000000100000000000010",
"0010010111111111111111111100111111111100010010",
"0010010000100000000000000100100000100100010010",
"0010010011100111110111100100100111100111110010",
"0010010010000000100000100100100000000000000010",
"0011111111111111111111100100100111111111111110",
"0000010010100000000000100100100100000000000000",
"0000000000000000000000000000000000000000000000",
 ]
 

grid3 = [
"0000000000000000000000000000000000000000000000",
"0s11111111111111111110111111111111111111111110",
"0111111111111111111110111111111111111111111110",
"0111111111111111111110111111111111111111111110",
"0111111111111111111110111111111111111111111110",
"0111111111111111111111111111111111111111111110",
"0111111111111111111111111111111111101111111110",
"0111111111100000111111111111111111101111111110",
"0111111111111111100000000011111111101111111110",
"0111111111100000111111111111111111101111111110",
"0111111111111111111111111111111111101111111110",
"0111111111111111111111111111111111111111111110",
"0111111111111111111111111111111111111111111110",
"0111111111111111111111111111111111111111111110",
"0111111111111111111111111111111111101111111110",
"0111111111111111111111111111111111101111111110",
"0111111111111111111111111111111111101111111110",
"0111111111111111111110111111111111101111111110",
"0111111111111111111110111111111111101111111110",
"0111111111111111111110111111111111111111111110",
"0111111111111111111110111111111111111111111110",
"0111111111111111111110111111111111111111111110",
"0111111111111111111110111111111111111111111110",
"0111111111111111111110111111111111111111111110",
"01111111111111111111101111111111111111111111e0",
"0000000000000000000000000000000000000000000000",
 ]
 
grid4 = [
"0000000000000000000000000000000000000000000000",
"0s11111111111111111110111111111111111111111110",
"0111111111110111111110111111111001111110011110",
"0111111111111111111110110011101100111110011110",
"0111111111011111111110111111111000111111111110",
"0111111111111111111111111111011111111111111110",
"0111111111110111111111111110111111101111111110",
"0111111111100000111111111111111111101110011110",
"0111111111111111100000000011111111101111111110",
"0111111111100000111111111111111111101111111110",
"0111110111110111111111101111111111101111011110",
"0111111111111111111111111111110001111111111110",
"0111111111111111110111111111100111111110011110",
"0111111111111111111111100011111111111111111110",
"0111111111111111111111111111111111101111111110",
"0111111110011111111111111111111111101111111110",
"0111111111111111111111111111111111101111111110",
"0111111111111111111110001111111111101111111110",
"0111111111111111111110111110111111101111111110",
"0111110111111111111110111111111111111111111110",
"0111111111111110001100111111111111111111111110",
"0111111101111111111110111111111111111111111110",
"0111111100111111000100111111111111111111111110",
"0111111101111111111110111111111111111111111110",
"01111111011111111111011111111111111111111111e0",
"0000000000000000000000000000000000000000000000",
 ]
 
# this function constructs the maze based on the grid type above
def setup_maze(grid):                          # define a function called setup_maze
    global start_state, goal_state      # set up global variables for start and end locations
    global start_x, start_y, end_x, end_y
    
    for y in range(len(grid)):                 # iterate through each line in the grid
        for x in range(len(grid[y])):          # iterate through each character in the line
            character = grid[y][x]             # assign the variable character to the y and x positions of the grid
            screen_x = -588 + (x * width)         # move to the x location on the screen staring at -288
            screen_y = 288 - (y * width)          # move to the y location of the screen starting at 288

            if character == "0":                   # if character contains a '0'
                maze.goto(screen_x, screen_y)      # move pen to the x and y location and
                id0_maze = maze.stamp()                       # stamp a copy of the white turtle on the screen
                id_maze.append(id0_maze)
                walls.append((screen_x, screen_y)) # add cell to the walls list

            if character == "1":                    # if character contains a '1'
                path.append((screen_x, screen_y))   # add to path list

            if character == "e":                    # if cell contains an 'e'
                yellow.goto(screen_x, screen_y)     # move pen to the x and y location and
                id0_yellow = yellow.stamp()         # stamp a copy of the yellow turtle on the screen
                id_yellow.append(id0_yellow)
                end_x, end_y = screen_x, screen_y   # assign end locations variables to end_x and end_y
                goal_state = (end_x, end_y)
                path.append((screen_x, screen_y))   # add cell to the path list

            if character == "s":                       # if cell contains a "s"
                start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                start_state = (start_x, start_y)
                red.goto(screen_x, screen_y)           # send red turtle to start position
  
#Calculate h score using manhattan distance
def manhattan_distance(p1, p2):
	
	x1, y1 = p1
	x2, y2 = p2
	xdist = abs(x2 - x1)
	ydist = abs(y2 - y1)
	
	return (xdist + ydist)
	
#Calculate h score using euclidean distance
def euclidian_distance(p1, p2):
	
	x1, y1 = p1
	x2, y2 = p2
	xdist = x2 - x1
	ydist = y2 - y1
	distance = sqrt(xdist * xdist + ydist * ydist) 
	return distance

def add_neighbors(node):
	neighbors = []                      
	
	if(node[0], node[1] + width) in path:  # up
		cellup = (node[0], node[1] + width) 
		
		neighbors.append(cellup)
		
	if (node[0], node[1] - width) in path:  # down
		celldown = (node[0], node[1] - width)
		
		neighbors.append(celldown)
		
	if(node[0] - width, node[1]) in path:  # left
		cellleft = (node[0] - width, node[1])
		
		neighbors.append(cellleft)  

	if(node[0] + width, node[1]) in path:   # right
		cellright = (node[0] + width, node[1])
		
		neighbors.append(cellright)
	
	return neighbors
		
def a_star(start, goal):
	count = 0
	frontier = PriorityQueue()
	parent = {}
	g_score = {node: float("inf") for node in path}
	g_score[start] = 0
	f_score = {node: float("inf") for node in path}
	
	if choosing_h == True:
		#manhattan_distance
		f_score[start] = manhattan_distance(start, goal)
	else:
		#euclidean_distance
		f_score[start] = euclidian_distance(start, goal)
	
	frontier.put((f_score[start], count, start))
	frontier_hash = {start}
	
	time_start = timeit.default_timer()
	
	while not frontier.empty():
		current = frontier.get()[2]
		frontier_hash.remove(current)
	
		if current == goal:
			
			reconstruct_path(parent, goal)
			time_end = timeit.default_timer()
			print(time_end - time_start)
			print("Number of steps:", len(id_blue) + 1)
			return True

		for neighbor in add_neighbors(current):
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[neighbor]:
				parent[neighbor] = current
				g_score[neighbor] = temp_g_score
				
				if choosing_h == True:
					#manhattan_distance
					f_score[neighbor] = temp_g_score + manhattan_distance(neighbor, goal)
				else:
					#euclidean_distance
					f_score[neighbor] = temp_g_score + euclidian_distance(neighbor, goal)
				
				if neighbor not in frontier_hash:
					count += 1
					frontier.put((f_score[neighbor], count, neighbor))
					frontier_hash.add(neighbor)
	time_end = timeit.default_timer()
	print(time_end - time_start)
	return False               

def reconstruct_path(parent, current):
	id_blue.clear()
	while current in parent:
		current = parent[current]
		if current != (start_x, start_y):
			blue.goto(current[0], current[1])                      
			id0 = blue.stamp()
			id_blue.append(id0)
		
#  initialize 
maze = Maze()
red = Red()
blue = Blue()
yellow = Yellow()
walls = []
path = []

blue.ht()
maze.ht()
yellow.ht()

wn.mainloop()                   

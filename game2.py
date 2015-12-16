from meet import *
import meet
import math
import random
cells = []
i = 0
for i in range(0, 10):
	cell1 = {"x":meet.get_random_x(), "y":meet.get_random_y(), "radius":meet.random.randint(2,50), "dy":random.random() , "dx":random.random(), "color":"pink"}
	z= create_cell(cell1)
	cells.append(z)
agario1= {"x": meet.get_x_mouse(), "y": meet.get_y_mouse(), "radius": 50, "dy":0, "dx":0}
agario = create_cell(agario1)
agarios=[agario]
def border():
	right = meet.get_screen_width()
	left = -meet.get_screen_width()
	up = meet.get_screen_height()
	down = -meet.get_screen_height()
	for cell in cells:
		if cell.ycor()+cell.get_radius() >= up or cell.ycor()-cell.get_radius() <= down or cell.xcor()+cell.get_radius() >= right or cell.xcor()-cell.get_radius() <= left:
			cell.set_dx(-cell.get_dx())
			cell.set_dy(-cell.get_dy())


                        
while True : 
	meet.move_cells(cells)
	meet.move_cells(agarios)
	dx,dy=meet.get_user_direction(agario)
	agario.set_dx(dx)
	agario.set_dy(dy)
	border()

for c in cells:	
	if agario.distance(c) < 20:
		turtle.bye()

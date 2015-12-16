from meet import *
import meet
cells = []
i = 0
for i in range(0, 10):
	cell1 = {"x":meet.get_random_x(), "y":meet.get_random_y(), "radius":meet.random.randint(2,50), "dy":random.randint(-250,250) , "dx":random.randint(-400,400)}
	z= create_cell(cell1)
	cells.append(z)

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
	border()
	move_cells(cells)

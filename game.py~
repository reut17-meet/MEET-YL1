from meet import *

cells = []
i = 0
for i in range(0, 10):
	cell1 = {"x":get_random_x(), "y":get_random_y(), "radius":30, "dy":1, "dx":1 }
	z= create_cell(cell1)
	cells.append(z)

	
def border():
	for cell in cells:
		if get_screen_width() < cell.xcord():
			.set_dx(-1)
		if get_screen_height() < cell.ycord():
				
		
			
while True :			
	border()
	move_cells(cells)

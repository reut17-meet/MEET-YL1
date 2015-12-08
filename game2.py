from meet import *

cells = []
i = 0
for i in range(0, 10):
	cell1 = {"x":get_random_x(), "y":get_random_y(), "radius":30, "dy":1, "dx":1}
	z= create_cell(cell1)
	cells.append(z)
while True : 
	move_cells(cells)

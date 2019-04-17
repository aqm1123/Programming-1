"""School project that required us to finish the remaining code of
   a Tetris game"""


def default_pos_of_shape(shape):

	if shape == 'I':
		return [(0,0), (1,0), (2,0), (3,0)]

	if shape == 'O':
		return [(0,0), (0,1), (1,0), (1,1)]

	if shape == 'T':
		return [(1,0), (1,1), (0,1), (2,1)]

	if shape == 'J':
		return [(0,0), (0,1), (1,1), (2,1)]

	if shape == 'L':
		return [(0,1), (1,1), (2,0), (2,1)]

	if shape == 'S':
		return [(0,1), (1,1), (1,0), (2,0)]

	if shape == 'Z':
		return [(0,0), (1,0), (1,1), (2,1)]

def pos_if_shifted(positions, shift):

	list_to_convert_tuple = []

	#change positions dependent on shift
	for x in range(len(positions)):
		list_append = []
		for i in range(2):
			new_val = positions[x][i] + shift[i]
			list_append.append(new_val)

		list_to_convert_tuple.append(tuple(list_append))


	return list_to_convert_tuple


def pos_if_shifted_down(positions):

	return pos_if_shifted(positions, (0,1))

def pos_if_shifted_side(positions, go_left):

	if go_left:
		return pos_if_shifted(positions, (-1, 0))
	else:
		return pos_if_shifted(positions, (1,0))

def pos_if_rotated(shape, positions, loc, number_rotations):

	if shape == 'O':
		return positions

	elif shape == 'I':

		#make list of loc to make changes of it's copy
		new_positions = list(loc)
		
		#rotate from it's pivot point ###DOESN'T WORK!!!!
		for value in range(len(new_positions)):
			if value == 0:
				new_positions[value] = (1.5 + new_positions[value]) * -1
			else:
				new_positions[value] = (0.5 + new_positions[value]) * -1
		
		#convert back to tuple to use for pos_if_shifted function and turn into list
		list_rotation = list(pos_if_shifted(positions, tuple(new_positions)))[:]

		#turn the tuples of list_rotation into a list to be able to modify
		for x in range(len(list_rotation)):
			list_rotation[x] = list(list_rotation[x])
		
		#make the rotations and make a copy of previous rotatio
		
		for i in range(number_rotations):
			for x in range(len(list_rotation)):
				copy = list_rotation[x][:]
				list_rotation[x][0] = -copy[1]
				list_rotation[x][1] = copy[0]
				
		#convert each list back to tuple
		for x in range(len(list_rotation)):
			list_rotation[x] = tuple(list_rotation[x])

		return list_rotation

	else:

		#same as previous but rotations are different

		new_positions = list(loc)

		for x in range(len(new_positions)):
			new_positions[x] = (1 + new_positions[x]) * -1

		list_rotation = list(pos_if_shifted(positions, tuple(new_positions)))[:]

		for x in range(len(list_rotation)):
			list_rotation[x] = list(list_rotation[x])

		for i in range(number_rotations):
			for x in range(len(list_rotation)):
				copy = list_rotation[x][:]
				list_rotation[x][0] = -copy[1]
				list_rotation[x][1] = copy[0]
		
		for x in range(len(new_positions)):
			new_positions[x] *= -1

		list_rotation = pos_if_shifted(list_rotation, tuple(new_positions))

		for x in range(len(list_rotation)):
			list_rotation[x] = tuple(list_rotation[x])

		return list_rotation


def make_grid(width, height):

	return_list = []
	#make list of None depening on width and height
	for x in range(height):
		append_list = []
		for i in range(width):
			append_list.append(None)

		return_list.append(append_list)

	return return_list

def is_valid_pos(grid, pos):

	#use global so the copy of the grid can be used in the other functions easily
	global grid_2
	grid_2 = grid[:]
	a = 0
	b = 0
	ccd = [a, b]

	#copying grid index and values
	for x in range(len(grid)):
		grid_2[x] = grid[x][:]
	
	#setting coordinates to be able to compare to the argument pos
	for i in range(len(grid_2)):
		for x in range(len(grid_2[i])):
			tccd = tuple(ccd)
			grid_2[i][x] = tccd
			a += 1
			b = b
			ccd = [a, b]
		#skip to next row 
		a = 0
		b = b + 1
		ccd = [a,b]

	#test if the position is equivalent to the position
	for i in range(len(grid_2)):
		for x in range(len(grid_2[i])):
			if grid_2[i][x] == pos:
				return True

	return False

def is_open_pos(grid, pos): 


	if is_valid_pos(grid, pos):
		#check if there is space open 
		for i in range(len(grid)):
			for x in range(len(grid[i])):
				if grid_2[i][x] == pos and grid[i][x] == None:
					return True

		return False

def set_positions(grid, positions, value):

	#check for all positions in the lis
	for i in range(len(positions)):
		#checking if valid
		if is_valid_pos(grid, positions[i]):
			for x in range(len(grid)):

				for z in range(len(grid[x])):

					if grid_2[x][z] == positions[i]:
						grid[x][z] = value


def clear_positions(grid, positions):

	set_positions(grid, positions, None)

def can_place_at(grid, positions): 

	#check if the positions is available at...
	for i in range(len(positions)):
		if is_open_pos(grid, positions[i]):
			if is_valid_pos(grid, positions[i]):
				pass

			else:
				return False

		else:
			return False

	return True


def can_move_down(grid, positions):

	#CHECK IF positions avialable
	if can_place_at(grid, pos_if_shifted_down(positions)):
		return True
	else:
		return False

def can_move_side(grid, positions, go_left):

	#checks if position available 

	if can_place_at(grid, pos_if_shifted_side(positions, go_left)):
		return True
	else:
		return False


def can_rotate(grid, shape, positions, loc, clockwise):
	#clockwise rotation

	if clockwise:
		new_position = pos_if_rotated(shape, positions, loc, 1)

	#countervlockwise rotation
	elif clockwise == False:
		new_position = pos_if_rotated(shape, positions, loc, 3)

	#check if space available
	if can_place_at(grid, new_position):
		return True
	else:
		return False


def get_row (grid, y):

	#return row that is correct

	for i in range(len(grid)):
		if i == y:
			return grid[i]

def delete_row(grid, y):

	#check if row is none
	delete_row = get_row(grid, y)
	new_row = delete_row[:]
	for i in range(len(new_row)):
		if new_row[i] != None:
			new_row[i] = None

	

	grid.remove(delete_row)
	grid.insert(0, new_row)


def get_complete_row_indexes(grid):

	list_indexes = []

	for i in range(len(grid)):
		for x in range(len(grid[i])):
			if x == - 1 + len(grid[x]):
				list_indexes.append(i)
				break

			if grid[i][x] == None:
				break

	return list_indexes










	

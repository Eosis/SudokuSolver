#!/usr/bin/python3

example_grid = [ 
									[1, 2, 3, 4, 5, 6, 7, 8, 0],
									[4, 5, 6, 7, 8, 9, 0, 1, 0],
									[0, 0, 0, 0, 0, 0, 0, 0, 0],
									[5, 6, 7, 8, 9, 0, 1, 2, 3],
									[6, 7, 8, 9, 0, 1, 2, 3, 4],
									[7, 8, 9, 0, 1, 2, 3, 4, 5],
									[8, 9, 0, 1, 2, 3, 4, 5, 6],
									[0, 0, 0, 0, 0, 0, 0, 0, 0],
									[0, 0, 0, 0, 0, 0, 0, 0, 0]
]

really_easy_grid = [ 
									[1, 2, 3, 4, 5, 6, 7, 8, 0],
									[0, 5, 6, 7, 8, 9, 1, 2, 3],
									[7, 8, 9, 1, 2, 3, 4, 5, 6],
									[2, 3, 4, 5, 6, 7, 8, 9, 1],
									[5, 6, 7, 8, 9, 1, 2, 3, 4],
									[8, 9, 1, 2, 3, 4, 5, 6, 7],
									[9, 0, 2, 3, 4, 5, 6, 7, 8],
									[3, 4, 5, 6, 7, 8, 9, 1, 2],
									[6, 7, 8, 9, 1, 2, 3, 4, 5]
]

def get_unfilled(grid):
	ret_val = set({})
	for i in range(9):
		for j in range(9):
			if grid[i][j] == 0:
				ret_val.add((i, j,))
	return ret_val

def get_all_potentials_in_grid(grid):
	to_check = get_unfilled(grid)
	square_potentials = set({})
	for square in to_check:
		#tuple (x, y, count of potential values)
		to_add = (square[0], square[1], len(get_available(grid, square[0], square[1])),)
		square_potentials.add(to_add)
	return square_potentials

def get_next_moves(grid):
	square_potentials = get_all_potentials_in_grid(grid)
	for square in square_potentials:
		square_to_fill = min(square_potentials, key=(lambda x: x[2]))
		moves = []
		for value in get_available(grid, square_to_fill[0], square_to_fill[1]):
			moves.append((square_to_fill[0], square_to_fill[1], value))
		return moves

def get_excluded_in_box(grid, x, y):
	box_x = x//3
	box_y = y//3
	excluded = set({})
	for i in range(3):
		for j in range(3):
			if grid[box_x*3 + i][box_y*3 + j] != 0:
				excluded.add(grid[(box_x*3) + i][(box_y*3) + j])
	return excluded

def get_excluded_in_row(grid, x, y):
	row = grid[x]
	return { i for i in row if i != 0 }

def get_excluded_in_column(grid, x, y):
	excluded = set({})
	for row in grid:
		if row[y] != 0:
			excluded.add(row[y])
	return excluded


possible = {1, 2, 3, 4, 5, 6, 7, 8, 9}
def get_available(grid, x, y):
	a = get_excluded_in_column(grid, x, y)
	b = get_excluded_in_row(grid, x, y)
	c = get_excluded_in_box(grid, x, y)
	total = set({})
	total = a.union(b).union(c)
	return possible - total

def test_get_excluded_in_box():
	box_one_ans = {1, 2, 3, 4, 5, 6}
	assert box_one_ans == get_excluded_in_box(example_grid, 0, 0)
	assert box_one_ans == get_excluded_in_box(example_grid, 2, 2)

	box_nine_ans = {4, 5, 6}
	assert box_nine_ans == get_excluded_in_box(example_grid, 6, 6)
	assert box_nine_ans == get_excluded_in_box(example_grid, 8, 8)

def test_inverse_excluded():
	assert {9} == get_available(example_grid, 2, 0)

def test_get_excluded_in_column():
	column_one_ans = {1, 4, 5, 6, 7, 8}
	column_seven_ans = {7, 1, 2, 3, 4}
	assert column_one_ans == get_excluded_in_column(example_grid, 5,0)
	assert column_seven_ans == get_excluded_in_column(example_grid, 6,6)

def test_get_excluded_in_row():
	row_one_ans = {1, 2, 3, 4, 5, 6, 7, 8}
	row_five_ans = {6, 7, 8, 9, 1, 2, 3, 4}
	assert row_one_ans == get_excluded_in_row(example_grid, 0, 1)
	assert row_five_ans == get_excluded_in_row(example_grid, 4, 8)

def test_get_unfilled():
	ans = set({(0, 8), (1, 0), (6, 1)})
	assert get_unfilled(really_easy_grid) == ans

def test_get_next_moves():
	ans_list = [(8, 8, 9), (1, 0, 4), (6, 1, 1)]
	for move in get_next_moves(really_easy_grid):
		assert move in ans_list

def test_get_all_potentials_in_grid():
	potentials = get_all_potentials_in_grid(really_easy_grid)
	assert (0, 8, 1) in potentials
	assert (1, 0, 1) in potentials
	assert (6, 1, 1) in potentials
	assert (8, 8, 5) not in potentials

if __name__ == '__main__':
	import pytest
	test_inverse_excluded()
	test_get_excluded_in_column()
	test_get_excluded_in_row()
	test_get_excluded_in_box()
	print("Tests passed")

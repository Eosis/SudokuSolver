#!/usr/bin/python3
import state_tree
import sudoku_logic

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

def get_filled_spaces(grid):
	count = 0
	for i in range(9):
		for j in range(9):
			if grid[i][j] != 0:
				count += 1
	return count

def test_get_filled_spaces():
	assert get_filled_spaces(really_easy_grid) == (81 -3)

import pdb
def solve(current_move):
	grid = current_move.grid
	if get_filled_spaces(grid) == 81:
		return grid
	else:
		moves = sudoku_logic.get_next_moves(grid)
		solutions = []
		if len(moves) >= 1:
			for move in moves:
				current_move.add_potential_move(move[0], move[1], move[2])
			for state in current_move.move_list:
				solution = solve(state)
				if solution != None:
					return solution
		else:
			return None


def test_solve():
	starting_state = state_tree.build_state_from_grid(really_easy_grid)
	solution = solve(starting_state)
	import copy
	ans_solution = copy.deepcopy(really_easy_grid)
	ans_solution[0][8] = 9
	ans_solution[1][0] = 4
	ans_solution[6][1] = 1
	assert ans_solution == solution
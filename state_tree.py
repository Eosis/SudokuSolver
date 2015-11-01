#!/usr/bin/python3
from copy import deepcopy
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

class StateTree():
	def __init__(self, x, y, choice, parent):
		self.parent = parent
		self.move = (x, y, choice) #The move we chose
		self.move_list = []				 #Given we chose that, what moves are available?
		if parent != None:
			self.grid = self.recount_moves()
		else:
			self.grid = [ [ 0 for i in range(9) ] for i in range(9) ]

	def add_potential_move(self, x, y, choice):
		self.move_list.append(StateTree(x, y, choice, self))

	def recount_moves(self):
		if self.parent != None:
			self.grid = StateTree.recount_moves(self.parent)
		self.grid[self.move[0]][self.move[1]] = self.move[2]
		return deepcopy(self.grid)

def build_state_from_grid(grid):
	state = None
	for i in range(9):
		for j in range(9):
			if grid[i][j] != 0:
				if state:
					state.add_potential_move(i, j, grid[i][j])
					state = state.move_list[0]
				else:
					state = StateTree(i, j, grid[i][j], None)
	return state

def test_build_state_from_grid():
	assert build_state_from_grid(really_easy_grid).recount_moves() == really_easy_grid

def test_recount_moves():
	current_state = StateTree(0, 0, 1, None)
	current_state.add_potential_move(0, 1, 2)
	for state in current_state.move_list:
		state.add_potential_move(0, 2, 9)
	assert current_state.grid[0][0] == 1
	next_state = current_state.move_list[0]
	assert next_state.grid[0][0] == 1
	assert next_state.grid[0][1] == 2
	next_next_state = next_state.move_list[0]
	assert next_next_state.grid[0][0] == 1
	assert next_next_state.grid[0][1] == 2
	assert next_next_state.grid[0][2] == 9


def main():
	current_state = None
	current_state = StateTree(0, 0, 1, None)
	current_state.add_potential_move(0, 1, 2)
	current_state.add_potential_move(0, 1, 3)
	current_state.add_potential_move(0, 1, 4)
	for state in current_state.move_list:
		state.add_potential_move(0, 2, 9)

	for i, state in enumerate(current_state.move_list):
		print("------For State %d------" % i)
		state.recount_moves()
		print("------------------------")

	for state in current_state.move_list:
		for i, state in enumerate(state.move_list):
			print("------For StateState %d------" % i)
			state.recount_moves()
			print("------------------------")

if __name__ == '__main__':
	main()
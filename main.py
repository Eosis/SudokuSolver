#!/usr/bin/python3
from solve import *

example_grid = [ 
									[8, 0, 5, 0, 0, 0, 0, 0, 0],
									[1, 0, 0, 0, 2, 0, 8, 7, 0],
									[6, 2, 0, 9, 0, 0, 0, 0, 0],
									[0, 0, 8, 5, 0, 0, 3, 0, 0],
									[0, 0, 0, 1, 0, 6, 0, 0, 0],
									[0, 0, 2, 0, 0, 7, 9, 0, 0],
									[0, 0, 0, 0, 0, 4, 0, 8, 2],
									[0, 5, 6, 0, 1, 0, 0, 0, 3],
									[0, 0, 0, 0, 0, 0, 5, 0, 9]
]

def main():
	starting_state = state_tree.build_state_from_grid(example_grid)
	solution = solve(starting_state)
	print("Here's the solution:")
	for line in solution:
		print(line)
	return

if __name__ == '__main__':
	main()
import string
import networkx as nx
import numpy as np

from src.challenges import read_input_removing_new_line
from grid_network import GridNetwork

input_grid = read_input_removing_new_line('input.txt')

signal_strength = {'S': 'S', 'E': 'E'}
for index, letter in enumerate(string.ascii_lowercase):
    signal_strength[letter] = index + 1

input_grid = np.array([list((map(lambda letter: signal_strength[letter], row))) for row in input_grid])

starting_point = np.where(input_grid == 'S')
ending_point = np.where(input_grid == 'E')

input_grid[starting_point] = 1
input_grid[ending_point] = 26
input_grid_numeric = input_grid.astype(int)
grid_network = GridNetwork(input_grid_numeric, starting_point, ending_point)

shortest_distance = nx.dijkstra_path(grid_network.graph, grid_network.starting_position, grid_network.ending_position, weight='weight')

print(f'first solution: {len(shortest_distance) - 1}')

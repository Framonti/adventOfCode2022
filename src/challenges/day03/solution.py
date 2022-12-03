import string
from typing import Dict

from src.challenges import read_input_removing_new_line

rucksack_data = read_input_removing_new_line('input.txt')

rucksack_data_compartments_split = [[rucksack_items[:len(rucksack_items) // 2],
                                     rucksack_items[len(rucksack_items) // 2:]] for rucksack_items in rucksack_data]

common_items = [list(set(compartments[0]).intersection(compartments[1])) for compartments in
                rucksack_data_compartments_split]

priorities: Dict = dict()
for index, letter in enumerate(string.ascii_letters):
    priorities[letter] = index + 1

item_priorities = [priorities[item[0]] for item in common_items]

first_solution = sum(item_priorities)
print(f'first solution: {first_solution}')

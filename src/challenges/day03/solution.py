import string

from src.challenges import read_input_removing_new_line, split_list_into_chunks

rucksack_data = read_input_removing_new_line('input.txt')

rucksack_data_compartments_split = [[rucksack_items[:len(rucksack_items) // 2],
                                     rucksack_items[len(rucksack_items) // 2:]] for rucksack_items in rucksack_data]

common_items = [list(set(compartments[0]).intersection(compartments[1])) for compartments in
                rucksack_data_compartments_split]

priorities = dict()
for index, letter in enumerate(string.ascii_letters):
    priorities[letter] = index + 1

item_priorities = [priorities[item[0]] for item in common_items]

first_solution = sum(item_priorities)
print(f'first solution: {first_solution}')

rucksacks_data_per_team = list(split_list_into_chunks(rucksack_data, 3))

badge_items = [list(set(items[0]).intersection(items[1]).intersection(items[2])) for items in
               rucksacks_data_per_team]
badge_priorities = [priorities[badge[0]] for badge in badge_items]
second_solution = sum(badge_priorities)
print(f'second solution: {second_solution}')

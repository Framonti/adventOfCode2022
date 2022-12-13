from src.challenges import read_input_removing_new_line, group_by_separator
from pair import Pair

input_raw_data = read_input_removing_new_line('input.txt')
input_raw_pairs = group_by_separator(input_raw_data)

input_pairs = [Pair(raw_pair) for raw_pair in input_raw_pairs]

checked_pairs = [pair.check_right_order(pair.left, pair.right) for pair in input_pairs]

tot_indices = 0
for i in range(len(checked_pairs)):
    if checked_pairs[i]:
        tot_indices += i + 1

print(f'first solution: {tot_indices}')


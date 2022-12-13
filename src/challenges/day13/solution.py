from src.challenges import read_input_removing_new_line, group_by_separator
from comparator import Pair, compare_pair, DistressSignal
import numpy as np

input_raw_data = read_input_removing_new_line('input.txt')
input_raw_pairs = group_by_separator(input_raw_data)

input_pairs = [Pair(raw_pair) for raw_pair in input_raw_pairs]

checked_pairs = [compare_pair(pair.left, pair.right) for pair in input_pairs]

tot_indices = 0
for i in range(len(checked_pairs)):
    if checked_pairs[i] == -1:
        tot_indices += i + 1

print(f'first solution: {tot_indices}')

input_raw_signals = np.array(input_raw_pairs).flatten()

distress_signals = [DistressSignal(input_signal) for input_signal in input_raw_signals]
starting_marker = DistressSignal('[[2]]')
ending_marker = DistressSignal('[[6]]')
distress_signals.append(starting_marker)
distress_signals.append(ending_marker)
distress_signals.sort()

starting_marker_index = distress_signals.index(starting_marker) + 1
ending_marker_index = distress_signals.index(ending_marker) + 1

decoder_key = starting_marker_index * ending_marker_index
print(f'second solution: {decoder_key}')

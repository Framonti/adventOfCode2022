import json
from functools import total_ordering


def compare_pair(left, right, recursive=False):
    for i in range(max(len(left), len(right))):
        if i == len(left) and len(left) < len(right):
            return -1
        elif i == len(right) and len(right) < len(left):
            return 1

        # both integers
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                return -1
            elif left[i] > right[i]:
                return 1
            else:
                continue

        # both lists
        elif isinstance(left[i], list) and isinstance(right[i], list):
            recursive_result = compare_pair(left[i], right[i], recursive=True)
            if not isinstance(recursive_result, tuple):
                return recursive_result
        elif isinstance(left[i], list) and isinstance(right[i], int):
            converted = [right[i]]
            recursive_result = compare_pair(left[i], converted, recursive=True)
            if not isinstance(recursive_result, tuple):
                return recursive_result
        else:
            converted = [left[i]]
            recursive_result = compare_pair(converted, right[i], recursive=True)
            if not isinstance(recursive_result, tuple):
                return recursive_result

    if recursive:
        return 1, 'still_checking'
    return 1


class Pair:
    def __init__(self, raw_pair):
        self.left = json.loads(raw_pair[0])
        self.right = json.loads(raw_pair[1])


class DistressSignal:
    def __init__(self, input_signal):
        self.signal = json.loads(input_signal)

    @total_ordering
    def __lt__(self, other):
        return compare_pair(self.signal, other.signal) == -1

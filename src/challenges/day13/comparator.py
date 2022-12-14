import json
import math
from functools import total_ordering


def compare_pair(left, right, recursive=False):
    for i in range(max(len(left), len(right))):
        if i == len(left) and len(left) < len(right):
            return -1
        elif i == len(right) and len(right) < len(left):
            return 1

        match left[i], right[i]:
            case int(), int():
                if left[i] == right[i]:
                    continue
                return math.copysign(1, left[i] - right[i])
            case list(), list():
                recursive_result = compare_pair(left[i], right[i], recursive=True)
                if not recursive_result == 'still_checking':
                    return recursive_result
            case list(), int():
                return compare_pair(left[i], [right[i]])
            case int(), list():
                recursive_result = compare_pair([left[i]], right[i], recursive=True)
                if not recursive_result == 'still_checking':
                    return recursive_result
    if recursive:
        return 'still_checking'
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

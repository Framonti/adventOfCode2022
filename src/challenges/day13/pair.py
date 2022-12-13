import json

class Pair:
    def __init__(self, raw_pair):
        self.left = json.loads(raw_pair[0])
        self.right = json.loads(raw_pair[1])

    def check_right_order(self, left, right, recursive=False):
        for i in range(max(len(left), len(right))):
            if i == len(left) and len(left) < len(right):
                return True
            elif i == len(right) and len(right) < len(left):
                return False

            # both integers
            if isinstance(left[i], int) and isinstance(right[i], int):
                if left[i] < right[i]:
                    return True
                elif left[i] > right[i]:
                    return False
                else:
                    continue

            # both lists
            elif isinstance(left[i], list) and isinstance(right[i], list):
                recursive_result = self.check_right_order(left[i], right[i], recursive=True)
                if not isinstance(recursive_result, tuple):
                    return recursive_result
            elif isinstance(left[i], list) and isinstance(right[i], int):
                converted = [right[i]]
                recursive_result = self.check_right_order(left[i], converted, recursive=True)
                if not isinstance(recursive_result, tuple):
                    return recursive_result
            else:
                converted = [left[i]]
                recursive_result = self.check_right_order(converted, right[i], recursive=True)
                if not isinstance(recursive_result, tuple):
                    return recursive_result

        if recursive:
            return False, 'still_checking'
        return False

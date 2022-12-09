direction_movements = {'L': -1, 'R': 1, 'U': 1j, 'D': -1j}


def sign(num: complex):
    return complex((num.real > 0) - (num.real < 0), (num.imag > 0) - (num.imag < 0))


class Movement:
    def __init__(self, raw_movement):
        split_raw_movement = raw_movement.split(' ')
        self.direction, self.times = split_raw_movement[0], int(split_raw_movement[1])

    def execute_head_move(self, head_starting_position: complex):
        return head_starting_position + direction_movements[self.direction]

    def execute_knot_move(self, prev_knot_final_position: complex, current_knot_starting_position: complex):
        distance = prev_knot_final_position - current_knot_starting_position
        if abs(distance) >= 2:
            return current_knot_starting_position + sign(distance)
            # if distance < 2, knot doesn't move
        return current_knot_starting_position

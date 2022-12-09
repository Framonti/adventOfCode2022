direction_movements = {'L': -1, 'R': 1, 'U': 1j, 'D': -1j}


class Movement:
    def __init__(self, raw_movement):
        split_raw_movement = raw_movement.split(' ')
        self.direction, self.times = split_raw_movement[0], int(split_raw_movement[1])

    def execute_head_move(self, head_starting_position: complex):
        return head_starting_position + direction_movements[self.direction]

    def execute_tail_move(self, head_final_position: complex, tail_starting_position: complex):
        real_distance = abs(head_final_position.real - tail_starting_position.real)
        imaginary_distance = abs(head_final_position.imag - tail_starting_position.imag)
        if (real_distance == 2 and imaginary_distance == 0) or (real_distance == 0 and imaginary_distance == 2):
            return tail_starting_position + direction_movements[self.direction]
        if imaginary_distance == 1 and real_distance == 2:
            imaginary_sign = head_final_position.imag - tail_starting_position.imag
            return tail_starting_position + direction_movements[self.direction] + imaginary_sign * 1j
        if imaginary_distance == 2 and real_distance == 1:
            real_sign = head_final_position.real - tail_starting_position.real
            return tail_starting_position + direction_movements[self.direction] + real_sign

        # if distance < 2, tail doesn't move
        return tail_starting_position

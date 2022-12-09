from functools import reduce

from movement import Movement
from src.challenges import read_input_removing_new_line

raw_rope_movements = read_input_removing_new_line('input.txt')

rope_movements = [Movement(raw_movement) for raw_movement in raw_rope_movements]

# head and tail positions
starting_positions = [complex(0, 0)] * 2

tail_position_seen = set()


def execute_movement(positions, movement: Movement):
    head_position, tail_position = positions[0], positions[1]

    head_final_position = head_position
    tail_final_position = tail_position
    for _ in range(movement.times):
        head_final_position = movement.execute_head_move(head_position)
        tail_final_position = movement.execute_knot_move(prev_knot_final_position=head_final_position,
                                                         current_knot_starting_position=tail_position)
        tail_position_seen.add(tail_final_position)
        head_position = head_final_position
        tail_position = tail_final_position
    return [head_final_position, tail_final_position]


reduce(execute_movement, rope_movements, starting_positions)

unique_position_count = len(tail_position_seen)
print(f'first solution: {unique_position_count}')

# head and 9 knots
starting_positions = [complex(0, 0)] * 10
ninth_knot_position_seen = set()


def execute_movement_multiple_knots(positions: list, movement: Movement):
    for _ in range(movement.times):
        for i in range(len(positions)):
            if i == 0:
                current_knot_final_position = movement.execute_head_move(positions[i])
            else:
                current_knot_final_position = movement.execute_knot_move(
                    prev_knot_final_position=positions[i - 1],
                    current_knot_starting_position=positions[i]
                )
            positions[i] = current_knot_final_position
            if i == 9:
                ninth_knot_position_seen.add(current_knot_final_position)
    return positions


reduce(execute_movement_multiple_knots, rope_movements, starting_positions)
unique_position_count = len(ninth_knot_position_seen)
print(f'second solution: {unique_position_count}')

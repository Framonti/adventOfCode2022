from src.challenges import read_input_removing_new_line
from cave import Cave
from sand_movements import execute_grain_sand_movement

raw_rock_paths = read_input_removing_new_line('input.txt')


def clean_rock_path(raw_rock_path):
    split_rock_path = raw_rock_path.split(' -> ')
    starting_ending_position_split = [path.split(',') for path in split_rock_path]
    to_int = [(int(pair_couple[0]), int(pair_couple[1])) for pair_couple in starting_ending_position_split]
    return to_int


rock_paths = [clean_rock_path(raw_rock_path) for raw_rock_path in raw_rock_paths]

cave = Cave(rock_paths)

blocked_sand_grains = 0
while True:
    is_in_the_void = execute_grain_sand_movement(cave)
    if is_in_the_void:
        break
    blocked_sand_grains += 1


print(f'first solution: {blocked_sand_grains}')

a = 1

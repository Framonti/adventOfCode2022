from cave import Cave


def __execute_single_sand_movement__(cave: Cave, starting_position):
    row = starting_position[1]
    column = starting_position[0]
    try:
        bot_material = cave.grid.at[row + 1, column]
    except KeyError:
        return column, row + 1
    if bot_material == '.':
        return column, row + 1
    try:
        bottom_left_material = cave.grid.at[row + 1, column - 1]
    except KeyError:
        return column - 1, row + 1
    if bottom_left_material == '.':
        return column - 1, row + 1
    try:
        bottom_right_material = cave.grid.at[row + 1, column + 1]
    except KeyError:
        return column - 1, row + 1
    if bottom_right_material == '.':
        return column + 1, row + 1
    return starting_position


def execute_grain_sand_movement(cave: Cave):
    starting_position = (cave.SAND_SOURCE_COLUMN, cave.SAND_SOURCE_ROW)

    while True:
        new_position = __execute_single_sand_movement__(cave, starting_position)
        if new_position[0] > cave.max_column or new_position[0] < cave.min_column or new_position[1] > cave.max_row:
            return True
        if new_position == starting_position:
            cave.grid.at[new_position[1], new_position[0]] = 'o'
            return False
        starting_position = new_position

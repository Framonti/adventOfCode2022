import pandas as pd


class Cave:
    SAND_SOURCE_ROW = 0
    SAND_SOURCE_COLUMN = 500

    def __init__(self, rock_paths):
        self.min_column = min(min(pair[0] for pair in rock_path) for rock_path in rock_paths)
        self.max_column = max(max(pair[0] for pair in rock_path) for rock_path in rock_paths)
        self.max_row = max(max(pair[1] for pair in rock_path) for rock_path in rock_paths)
        self.__construct_initial_grid__(rock_paths)

    def __construct_initial_grid__(self, rock_paths):
        self.grid = pd.DataFrame(columns=range(self.min_column, self.max_column + 1), index=range(self.SAND_SOURCE_ROW, self.max_row + 1))
        self.grid[:] = '.'
        self.grid.at[self.SAND_SOURCE_ROW, self.SAND_SOURCE_COLUMN] = '+'
        [self.__set_rocks__(rock_path) for rock_path in rock_paths]

    def __set_rocks__(self, rock_path):
        for i in range(len(rock_path) - 1):
            current_path = rock_path[i]
            next_path = rock_path[i + 1]
            column_change = next_path[0] - current_path[0]
            row_change = next_path[1] - current_path[1]
            column_slicing_indices = sorted([current_path[0], current_path[0] + column_change])
            row_slicing_indices = sorted([current_path[1], current_path[1] + row_change])
            self.grid.loc[row_slicing_indices[0]: row_slicing_indices[1], column_slicing_indices[0]: column_slicing_indices[1]] = '#'

    def __str__(self):
        return f'{self.grid}'


class CaveWithFloor(Cave):
    def __init__(self, rock_paths):
        super().__init__(rock_paths)

    def __construct_initial_grid__(self, rock_paths):
        self.grid = pd.DataFrame(columns=range(200, 700),
                                 index=range(self.SAND_SOURCE_ROW, self.max_row + 3))
        self.grid[:] = '.'
        self.grid.at[self.SAND_SOURCE_ROW, self.SAND_SOURCE_COLUMN] = '+'
        [self.__set_rocks__(rock_path) for rock_path in rock_paths]
        self.grid.loc[self.max_row + 2] = '#'

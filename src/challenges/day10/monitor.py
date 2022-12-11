import numpy as np


class Monitor:
    monitor_width = 40
    monitor_height = 6

    def __init__(self):
        self.grid = np.array([['.'] * self.monitor_width] * self.monitor_height)

    def __str__(self):
        rendered_monitor = ''
        for row in self.grid:
            for pixel in row:
                rendered_monitor += f'{pixel}'
            rendered_monitor += '\n'
        return rendered_monitor

    def write_pixel(self, clock_value: int, x_registry_value: int):
        sprite_positions = [x_registry_value - 1, x_registry_value, x_registry_value + 1]
        current_row = clock_value // self.monitor_width
        current_column = clock_value % self.monitor_width
        if clock_value - (self.monitor_width * current_row) in sprite_positions:
            self.grid[current_row][current_column] = '#'

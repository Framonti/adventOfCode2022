import networkx as nx


class GridNetwork:
    def __init__(self, raw_numeric_input, starting_position, ending_position):
        self.row_number = raw_numeric_input.shape[0]
        self.column_number = raw_numeric_input.shape[1]
        self.starting_position = f'{int(starting_position[0])}, {int(starting_position[1])}'
        self.ending_position = f'{int(ending_position[0])}, {int(ending_position[1])}'

        self.graph = nx.DiGraph()

        for row_index in range(self.row_number):
            for column_index in range(self.column_number):
                current_node_value = raw_numeric_input[row_index][column_index]
                current_node_name = f'{row_index}, {column_index}'
                surrounding_values = self.extract_surrounding_points(raw_numeric_input, column_index, row_index)

                for surrounding_value in surrounding_values:
                    if surrounding_value[0] <= current_node_value + 1:
                        self.graph.add_edge(current_node_name, surrounding_value[1])

    def extract_surrounding_points(self, raw_numeric_input, column_index, row_index):
        unusable_node = (100, '')
        if column_index == 0:
            left_node = unusable_node
        else:
            left_node = (raw_numeric_input[row_index][column_index - 1], f'{row_index}, {column_index - 1}')
        if row_index == 0:
            top_node = unusable_node
        else:
            top_node = (raw_numeric_input[row_index - 1][column_index], f'{row_index - 1}, {column_index}')
        if column_index == self.column_number - 1:
            right_node = unusable_node
        else:
            right_node = (raw_numeric_input[row_index][column_index + 1], f'{row_index}, {column_index + 1}')
        if row_index == self.row_number - 1:
            bottom_node = unusable_node
        else:
            bottom_node = (raw_numeric_input[row_index + 1][column_index], f'{row_index + 1}, {column_index}')
        return left_node, right_node, top_node, bottom_node

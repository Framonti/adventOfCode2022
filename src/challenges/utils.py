def read_input_removing_new_line(path):
    with open(path, 'r') as input_file:
        input_data = input_file.readlines()
    input_data_no_new_lines = [input_data_no_new_line[:-1] for input_data_no_new_line in input_data]
    return input_data_no_new_lines

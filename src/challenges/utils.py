from itertools import islice
from itertools import groupby


def read_input_removing_new_line(path):
    with open(path, 'r') as input_file:
        input_data = input_file.readlines()
    input_data_no_new_lines = [input_data_no_new_line[:-1] for input_data_no_new_line in input_data]
    return input_data_no_new_lines


def split_list_into_chunks(list_to_split, chuck_size):
    it = iter(list_to_split)
    return iter(lambda: tuple(islice(it, chuck_size)), ())


def group_by_separator(input_data, separator=''):
    return [list(group) for is_key, group in groupby(input_data, lambda sep: sep == '') if not is_key]

from itertools import islice, groupby


def read_input_removing_new_line(path):
    with open(path, 'r') as input_file:
        input_data = input_file.readlines()
    input_data_no_new_lines = [input_data_no_new_line[:-1] for input_data_no_new_line in input_data]
    return input_data_no_new_lines


def split_list_into_chunks(list_to_split, chuck_size):
    it = iter(list_to_split)
    return iter(lambda: tuple(islice(it, chuck_size)), ())


def group_by_separator(input_data, separator=''):
    return [list(group) for is_key, group in groupby(input_data, lambda sep: sep == separator) if not is_key]


def sort_and_get_top_n_elem(list_to_sort: list, top_n: int, sorting_function=None):
    if sorting_function is None:
        sorted_list = sorted(list_to_sort, reverse=True)
    else:
        sorted_list = sorted(list_to_sort, key=sorting_function, reverse=True)
    top_n = sorted_list[:top_n]
    return top_n


def extract_and_convert_digit_from_string(string_to_convert):
    return int(''.join(i for i in string_to_convert if i.isdigit() or i == '-'))

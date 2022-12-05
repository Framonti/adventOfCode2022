from src.challenges import split_list_into_chunks
from queue import LifoQueue


def create_stacks(crate_starting_positions_raw_input):
    crate_positions_split = [list(split_list_into_chunks(crate_starting_position, 4))
                             for crate_starting_position in crate_starting_positions_raw_input]

    crate_positions_cleaned = __clean_crate_data(crate_positions_split)
    stacks = dict()
    STACK_NUMBER = 9
    for i in range(1, STACK_NUMBER + 1):
        __create_stack(stacks, crate_positions_cleaned, i)
    return stacks


def __clean_crate_data(crates_positions_split):
    crate_positions_cleaned = []
    for row in crates_positions_split:
        for data_tuple in row:
            crate_positions_cleaned.append([letter for letter in data_tuple if letter.isalpha()])
    crate_positions_cleaned = list(split_list_into_chunks(crate_positions_cleaned, 9))
    crate_positions_cleaned.pop()
    crate_positions_cleaned.reverse()
    return crate_positions_cleaned


def __create_stack(stacks, crate_positions, stack_index):
    stacks[stack_index] = LifoQueue()
    for row in crate_positions:
        if len(row[stack_index - 1]) > 0:
            stacks[stack_index].put(row[stack_index - 1][0])

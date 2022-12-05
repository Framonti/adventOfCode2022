from src.challenges import read_input_removing_new_line, group_by_separator, split_list_into_chunks
from stack_creation import create_stacks
from order_management import Order, execute_order

input_text = read_input_removing_new_line('input.txt')
split_input_text = group_by_separator(input_text, '')

crate_starting_positions, orders_raw = split_input_text[0], split_input_text[1]

stacks = create_stacks(crate_starting_positions)
orders = [Order(order_raw) for order_raw in orders_raw]

for order in orders:
    execute_order(stacks, order)


def retrieve_top_values(final_crate_positions):
    solution = f''
    for stack in final_crate_positions.values():
        solution += f'{stack.get()}'
    return solution


first_solution = retrieve_top_values(stacks)
print(f'first solution: {first_solution}')


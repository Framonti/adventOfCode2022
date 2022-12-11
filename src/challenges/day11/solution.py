import math

from monkey import Monkey
from src.challenges import read_input_removing_new_line, group_by_separator, sort_and_get_top_n_elem

monkey_input_raw_data = read_input_removing_new_line('input.txt')
monkey_input_split = group_by_separator(monkey_input_raw_data)

monkeys = [Monkey(monkey) for monkey in monkey_input_split]
modules_mcm = math.prod([monkey.test_divider for monkey in monkeys])

ROUNDS = 20
for _ in range(ROUNDS):
    [monkey.execute_turn(monkeys, modules_mcm, is_relief_active=True) for monkey in monkeys]


def retrieve_monkey_business(monkeys: list):
    top_2_monkeys = sort_and_get_top_n_elem(monkeys, top_n=2, sorting_function=lambda monkey: monkey.inspect_count)
    return math.prod([monkey.inspect_count for monkey in top_2_monkeys])


print(f'first solution: {retrieve_monkey_business(monkeys)}')

monkeys = [Monkey(monkey) for monkey in monkey_input_split]
modules_mcm = math.prod([monkey.test_divider for monkey in monkeys])

ROUNDS = 10_000
for _ in range(ROUNDS):
    [monkey.execute_turn(monkeys, modules_mcm, is_relief_active=False) for monkey in monkeys]

print(f'second solution: {retrieve_monkey_business(monkeys)}')

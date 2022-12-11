import math

from monkey import Monkey
from src.challenges import read_input_removing_new_line, group_by_separator

monkey_input_raw_data = read_input_removing_new_line('input.txt')
monkey_input_split = group_by_separator(monkey_input_raw_data)

monkeys = [Monkey(monkey) for monkey in monkey_input_split]
modules_mcm = math.prod([monkey.test_divider for monkey in monkeys])

ROUNDS = 20
for _ in range(ROUNDS):
    [monkey.execute_turn(monkeys, modules_mcm, is_relief_active=True) for monkey in monkeys]


def retrieve_monkey_business(monkeys: list):
    sorted_monkeys = sorted(monkeys, key=lambda monkey: monkey.inspect_count, reverse=True)
    top_2_monkeys = sorted_monkeys[:2]
    return math.prod([monkey.inspect_count for monkey in top_2_monkeys])


print(f'first solution: {retrieve_monkey_business(monkeys)}')

monkeys = [Monkey(monkey) for monkey in monkey_input_split]
modules_mcm = math.prod([monkey.test_divider for monkey in monkeys])

ROUNDS = 10_000
for _ in range(ROUNDS):
    [monkey.execute_turn(monkeys, modules_mcm, is_relief_active=False) for monkey in monkeys]

print(f'second solution: {retrieve_monkey_business(monkeys)}')

import math


class Monkey:
    def __init__(self, raw_monkey_input):
        self.number = int(raw_monkey_input[0][-2])
        starting_item_raw = raw_monkey_input[1].replace(',', '').split(' ')
        self.item_worry_levels = [int(i) for i in starting_item_raw if i.isnumeric()]
        operation_raw = raw_monkey_input[2].split(' ')
        self.operation = operation_raw[-2]
        self.operand = int(operation_raw[-1]) if operation_raw[-1].isnumeric() else operation_raw[-1]
        self.test_divider = int(raw_monkey_input[3].split(' ')[-1])
        self.monkey_test_true = int(raw_monkey_input[4].split(' ')[-1])
        self.monkey_test_false = int(raw_monkey_input[5].split(' ')[-1])
        self.inspect_count = 0

    def execute_turn(self, monkeys: list, modules_mcm: int, is_relief_active: bool):
        for item_worry_level in self.item_worry_levels:
            new_worry_level = self.__inspect_item__(item_worry_level)
            if is_relief_active:
                new_worry_level = self.__relief__(new_worry_level)
            new_worry_level = new_worry_level % modules_mcm
            monkey_to_throw = monkeys[self.__test__(new_worry_level)]
            self.__throw__(new_worry_level, monkey_to_throw)
            self.item_worry_levels = []

    def __inspect_item__(self, item_worry_level):
        self.inspect_count += 1
        operand = self.operand
        if self.operand == 'old':
            operand = item_worry_level
        if self.operation == '+':
            return item_worry_level + operand
        elif self.operation == '*':
            return item_worry_level * operand
        else:
            raise ValueError('operation unrecognized')

    @staticmethod
    def __relief__(item_worry_level):
        return math.floor(item_worry_level / 3)

    def __test__(self, item_worry_level):
        if item_worry_level % self.test_divider == 0:
            return self.monkey_test_true
        return self.monkey_test_false

    @staticmethod
    def __throw__(item_worry_level, monkey_to_throw):
        monkey_to_throw.item_worry_levels.append(item_worry_level)

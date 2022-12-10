from instruction import Instruction
from monitor import Monitor
from src.challenges import read_input_removing_new_line

input_instructions_raw = read_input_removing_new_line('input.txt')

input_instructions = [Instruction(raw_instruction) for raw_instruction in input_instructions_raw]

clock = 0
x_registry_values_each_clock = [(clock, 1)]

for instruction in input_instructions:
    clock += 1
    last_x_registry_value = x_registry_values_each_clock[-1][1]
    if instruction.instruction == 'noop':
        x_registry_values_each_clock.append((clock, last_x_registry_value))
    if instruction.instruction == 'add':
        x_registry_values_each_clock.append((clock, last_x_registry_value))
        clock += 1
        x_registry_values_each_clock.append((clock, last_x_registry_value + instruction.value))

signal_values = [x_registry_value_each_clock[0] * x_registry_value_each_clock[1]
                 for x_registry_value_each_clock in x_registry_values_each_clock]

interesting_signals = [20, 60, 100, 140, 180, 220]

total_interesting_signals = sum(list(signal_values[i] for i in interesting_signals))

print(f'first solution: {total_interesting_signals}')

monitor = Monitor()

[monitor.write_pixel(clock_value=x_registry_value_each_clock[0], x_registry_value=x_registry_value_each_clock[1])
 for x_registry_value_each_clock in x_registry_values_each_clock]

print(f'second solution:\n'
      f'{monitor}')

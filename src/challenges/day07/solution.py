from command_manager import TerminalIO
from file_system import FileSystem
from src.challenges import read_input_removing_new_line

input_commands_raw = read_input_removing_new_line('input.txt')

input_commands = [TerminalIO(input_command_raw) for input_command_raw in input_commands_raw]

file_system = FileSystem()

[command.execute_command(file_system) for command in input_commands]

THRESHOLD_SIZE = 100_000
smallest_directories = file_system.get_dir_by_size(THRESHOLD_SIZE)

tot_smallest_dir_size = sum([directory.tot_size for directory in smallest_directories])

print(f'first solution: {tot_smallest_dir_size}')

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

DISK_SPACE = 70_000_000
UNUSED_SPACE_REQUIRED = 30_000_000

currently_used_space = file_system.get_currently_used_space()
currently_free_space = DISK_SPACE - currently_used_space
space_to_be_freed = UNUSED_SPACE_REQUIRED - currently_free_space

all_directories = file_system.get_all_dir()

directory_to_delete_candidates = [directory for directory in all_directories if directory.tot_size >= space_to_be_freed]

directory_to_delete_candidates.sort(key=lambda directory: directory.tot_size)
directory_size = directory_to_delete_candidates[0].tot_size
print(f'second solution: {directory_size}')


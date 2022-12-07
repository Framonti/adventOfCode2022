from file_system import FileSystem


class TerminalIO:
    def __init__(self, raw_terminal_io: str):
        self.command = None
        self.argument = None
        split_terminal_io = raw_terminal_io.split(' ')
        if split_terminal_io[0] == '$':
            self.initialize_command(split_terminal_io)
        elif split_terminal_io[0] == 'dir':
            self.command = 'dir'
            self.argument = split_terminal_io[1]
        elif split_terminal_io[0].isnumeric():
            self.command = 'file'
            self.file_size = int(split_terminal_io[0])
            self.file_name = split_terminal_io[1]

    def initialize_command(self, command):
        if command[1] == 'ls':
            self.command = 'ls'
        elif command[1] == 'cd':
            self.command = 'cd'
            self.argument = command[2]

    def execute_command(self, file_system: FileSystem):
        if self.command == 'cd':
            self.execute_change_directory(file_system)
        elif self.command == 'ls':
            pass
        elif self.command == 'dir':
            file_system.add_directory(self.argument)
        elif self.command == 'file':
            file_system.add_file(self.file_name, self.file_size)

    def execute_change_directory(self, file_system: FileSystem):
        if self.argument == '/':
            file_system.move_to_root()
        elif self.argument == '..':
            file_system.move_backward()
        else:
            file_system.move_forward(self.argument)

import uuid


class File:
    def __init__(self, file_name, file_size):
        self.name = file_name
        self.file_size = file_size


class Directory:
    def __init__(self, name, parent, id):
        self.parent = parent
        self.children = []
        self.tot_size = 0
        self.name = name
        self.id = id


class FileSystem:
    def __init__(self):
        self.file_system = dict()
        self.root_id = uuid.uuid4()
        self.file_system[self.root_id] = Directory('/', None, self.root_id)
        self.current_dir: Directory = self.file_system[self.root_id]

    def add_directory(self, directory_to_add_name: str):
        dir_id = uuid.uuid4()
        directory_to_add = Directory(name=directory_to_add_name, parent=self.current_dir, id=dir_id)
        self.file_system[dir_id] = directory_to_add
        self.current_dir.children.append(directory_to_add)

    def add_file(self, file_name_to_add, file_size_to_add):
        file_to_add = File(file_name_to_add, file_size_to_add)
        self.current_dir.children.append(file_to_add)
        self.update_directories_sizes(file_size_to_add)

    def move_to_root(self):
        self.current_dir = self.file_system[self.root_id]

    def move_backward(self):
        self.current_dir = self.current_dir.parent

    def move_forward(self, dir_to_move_name):
        target_dir: Directory = [directory for directory in self.current_dir.children
                                 if directory.name == dir_to_move_name][0]
        self.current_dir = self.file_system[target_dir.id]

    def update_directories_sizes(self, file_size):
        self.current_dir.tot_size += file_size
        parent_dir = self.current_dir.parent
        while parent_dir is not None:
            parent_dir.tot_size += file_size
            parent_dir = parent_dir.parent

    def get_dir_by_size(self, threshold):
        return [directory for directory in self.file_system.values() if directory.tot_size <= threshold]

    def get_all_dir(self):
        return [directory for directory in self.file_system.values()]

    def get_currently_used_space(self):
        return self.file_system[self.root_id].tot_size

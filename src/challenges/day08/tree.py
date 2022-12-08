class Tree:
    def __init__(self, height):
        self.height = height
        self.visible = False

    def __str__(self):
        return f'{self.height} - {self.visible}'

    def is_higher(self, other_tree):
        return self.height > other_tree.height

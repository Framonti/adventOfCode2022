class Tree:
    def __init__(self, height):
        self.height = height
        self.visible = False
        self.left_visible = 0
        self.right_visible = 0
        self.top_visible = 0
        self.bottom_visible = 0

    def __str__(self):
        return f'{self.height} - {self.visible}'

    def is_higher(self, other_tree):
        return self.height > other_tree.height

    def is_shorter(self, other_tree):
        return self.height < other_tree.height

    def compute_scenic_score(self):
        return self.left_visible * self.right_visible * self.top_visible * self.bottom_visible

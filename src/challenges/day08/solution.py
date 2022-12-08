import pandas as pd

from src.challenges import read_input_removing_new_line
from tree import Tree

tree_grid_rows = read_input_removing_new_line('input.txt')
tree_grid_rows_int = [list(map(int, row)) for row in tree_grid_rows]

tree_grid_df = pd.DataFrame(tree_grid_rows_int)
tree_grid_df = tree_grid_df.applymap(lambda elem: Tree(elem))


def mark_tree_visible(tree_grid: pd.DataFrame, tree: Tree, tree_row, tree_column):
    column = tree_grid[tree_column]
    row = tree_grid.iloc[tree_row]
    top_trees = column[:tree_row]
    bottom_trees = column[tree_row + 1:]
    left_trees = row[:tree_column]
    right_trees = row[tree_column + 1:]

    top_trees_mask = [tree.is_higher(other_tree) for other_tree in top_trees]
    bottom_trees_mask = [tree.is_higher(other_tree) for other_tree in bottom_trees]
    left_trees_mask = [tree.is_higher(other_tree) for other_tree in left_trees]
    right_trees_mask = [tree.is_higher(other_tree) for other_tree in right_trees]

    tree.visible = all(top_trees_mask) or all(bottom_trees_mask) or all(left_trees_mask) or all(right_trees_mask)


tree_grid_matrix = tree_grid_df.to_numpy().tolist()

for row_index in range(len(tree_grid_matrix)):
    for column_index in range(len(tree_grid_matrix[row_index])):
        tree_to_analyze = tree_grid_matrix[row_index][column_index]
        mark_tree_visible(tree_grid_df, tree_to_analyze, row_index, column_index)

visible_trees_mask = tree_grid_df.applymap(lambda tree: tree.visible)
visible_tree_count = sum(map(sum, visible_trees_mask.to_numpy().tolist()))

print(f'first solution: {visible_tree_count}')
a = 1

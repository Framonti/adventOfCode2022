import pandas as pd
import numpy as np

from src.challenges import read_input_removing_new_line
from tree import Tree

tree_grid_rows = read_input_removing_new_line('input.txt')
tree_grid_rows_int = [list(map(int, row)) for row in tree_grid_rows]

tree_grid_df = pd.DataFrame(tree_grid_rows_int)
tree_grid_df = tree_grid_df.applymap(lambda elem: Tree(elem))


def mark_tree_visible(tree: Tree, top_trees, bottom_trees, left_trees, right_trees):
    top_trees_mask = [tree.is_higher(other_tree) for other_tree in top_trees]
    bottom_trees_mask = [tree.is_higher(other_tree) for other_tree in bottom_trees]
    left_trees_mask = [tree.is_higher(other_tree) for other_tree in left_trees]
    right_trees_mask = [tree.is_higher(other_tree) for other_tree in right_trees]

    tree.visible = all(top_trees_mask) or all(bottom_trees_mask) or all(left_trees_mask) or all(right_trees_mask)


def get_top_bottom_left_right_trees(tree_grid: pd.DataFrame, tree_row, tree_column):
    column = tree_grid[tree_column]
    row = tree_grid.iloc[tree_row]
    top_trees = column[:tree_row]
    bottom_trees = column[tree_row + 1:]
    left_trees = row[:tree_column]
    right_trees = row[tree_column + 1:]
    return top_trees, bottom_trees, left_trees, right_trees


def get_visible_trees(tree: Tree, top_trees, bottom_trees, left_trees, right_trees):
    top_trees = np.flip(top_trees.to_numpy())
    left_trees = np.flip(left_trees.to_numpy())
    tree.top_visible = get_visible_trees_count_one_side(tree, top_trees)
    tree.bottom_visible = get_visible_trees_count_one_side(tree, bottom_trees)
    tree.left_visible = get_visible_trees_count_one_side(tree, left_trees)
    tree.right_visible = get_visible_trees_count_one_side(tree, right_trees)


def get_visible_trees_count_one_side(tree: Tree, other_trees_list):
    if len(other_trees_list) == 0:
        return 0
    visible_trees = 0
    for other_tree in other_trees_list:
        if other_tree.is_shorter(tree):
            visible_trees += 1
        else:
            visible_trees += 1
            break
    return visible_trees


tree_grid_matrix: list = tree_grid_df.to_numpy().tolist()

for row_index in range(len(tree_grid_matrix)):
    for column_index in range(len(tree_grid_matrix[row_index])):
        tree_to_analyze = tree_grid_matrix[row_index][column_index]
        top_trees, bottom_trees, left_trees, right_trees = \
            get_top_bottom_left_right_trees(tree_grid_df, row_index, column_index)
        mark_tree_visible(tree_to_analyze, top_trees, bottom_trees, left_trees, right_trees)
        get_visible_trees(tree_to_analyze, top_trees, bottom_trees, left_trees, right_trees)

visible_trees_mask = tree_grid_df.applymap(lambda tree: tree.visible)
visible_tree_count = sum(map(sum, visible_trees_mask.to_numpy().tolist()))

print(f'first solution: {visible_tree_count}')

scenic_score_map = tree_grid_df.applymap(lambda tree: tree.compute_scenic_score())

max_scenic_score = scenic_score_map.max().max()

print(f'second solution: {max_scenic_score}')

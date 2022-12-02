from src.challenges import read_input_removing_new_line
from rps_enum import OpponentRPS, ShapeStrategyRPS, retrieve_shape_points, ResultStrategyRPS

rps_strategies = read_input_removing_new_line('input.txt')

predicted_matches_guide = [match.split(' ') for match in rps_strategies]
predicted_matches = [[OpponentRPS(match[0]), ShapeStrategyRPS(match[1])] for match in predicted_matches_guide]


def compute_match_scores(opponent_shape: OpponentRPS, played_shape: ShapeStrategyRPS) -> int:
    WINNING_POINTS = 6
    DRAWING_POINTS = 3
    LOSING_POINTS = 0
    if (opponent_shape == OpponentRPS.ROCK and played_shape == ShapeStrategyRPS.PAPER) or \
            (opponent_shape == OpponentRPS.PAPER and played_shape == ShapeStrategyRPS.SCISSOR) or \
            (opponent_shape == OpponentRPS.SCISSOR and played_shape == ShapeStrategyRPS.ROCK):
        return WINNING_POINTS
    if opponent_shape.name == played_shape.name:
        return DRAWING_POINTS
    return LOSING_POINTS


points_per_matches = [compute_match_scores(match[0], match[1]) + retrieve_shape_points(match[1]) for match in
                      predicted_matches]

tot_points = sum(points_per_matches)
print(f'first solution: {tot_points}')

predicted_matches = [[OpponentRPS(match[0]), ResultStrategyRPS(match[1])] for match in predicted_matches_guide]


def pick_shape_to_achieve_guide_result(opponent_shape: OpponentRPS, result_to_achieve: ResultStrategyRPS):
    if result_to_achieve == result_to_achieve.DRAWING:
        if opponent_shape == opponent_shape.ROCK:
            return ShapeStrategyRPS.ROCK
        if opponent_shape == opponent_shape.PAPER:
            return ShapeStrategyRPS.PAPER
        if opponent_shape == opponent_shape.SCISSOR:
            return ShapeStrategyRPS.SCISSOR
    if result_to_achieve == result_to_achieve.WINNING:
        if opponent_shape == opponent_shape.ROCK:
            return ShapeStrategyRPS.PAPER
        if opponent_shape == opponent_shape.PAPER:
            return ShapeStrategyRPS.SCISSOR
        if opponent_shape == opponent_shape.SCISSOR:
            return ShapeStrategyRPS.ROCK
    if result_to_achieve == result_to_achieve.LOSING:
        if opponent_shape == opponent_shape.ROCK:
            return ShapeStrategyRPS.SCISSOR
        if opponent_shape == opponent_shape.PAPER:
            return ShapeStrategyRPS.ROCK
        if opponent_shape == opponent_shape.SCISSOR:
            return ShapeStrategyRPS.PAPER


predicted_matches_moves = [[match[0], pick_shape_to_achieve_guide_result(match[0], match[1])] for match in
                           predicted_matches]

points_per_matches = [compute_match_scores(match[0], match[1]) + retrieve_shape_points(match[1]) for match in
                      predicted_matches_moves]
tot_points = sum(points_per_matches)

print(f'second solution: {tot_points}')

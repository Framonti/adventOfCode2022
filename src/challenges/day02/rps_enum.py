from enum import Enum


class OpponentRPS(Enum):
    ROCK = 'A'
    PAPER = 'B'
    SCISSOR = 'C'


class ShapeStrategyRPS(Enum):
    ROCK = 'X'
    PAPER = 'Y'
    SCISSOR = 'Z'


class ResultStrategyRPS(Enum):
    LOSING = 'X'
    DRAWING = 'Y'
    WINNING = 'Z'


def retrieve_shape_points(shape: ShapeStrategyRPS):
    if shape.name == 'ROCK':
        return 1
    if shape.name == 'PAPER':
        return 2
    if shape.name == 'SCISSOR':
        return 3

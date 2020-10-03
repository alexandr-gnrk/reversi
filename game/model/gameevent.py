from enum import IntEnum


class GameEvent(IntEnum):
    GAME_STARTED = 0
    FIELD_UPDATED = 1
    NEXT_MOVE = 2
    PLAYER_PASSES = 3
    INCORRECT_MOVE = 4
    GAME_OVER = 5
    
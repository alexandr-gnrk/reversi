from enum import IntEnum


class GameEvent(IntEnum):
    GAME_STARTED = 0
    FIELD_UPDATED = 1
    PLAYER_PASSES = 2
    GAME_OVER = 3
    
from games import game_db
from match import match
from typing import List, Tuple, Callable, Any

def get_title(game: Tuple[str, str, int, List[str]]) -> str:
    return game[0]


def get_director(game: Tuple[str, str, int, List[str]]) -> str:
    return game[1]


def get_year(game: Tuple[str, str, int, List[str]]) -> int:
    return game[2]


def get_actors(game: Tuple[str, str, int, List[str]]) -> List[str]:
    return game[3]
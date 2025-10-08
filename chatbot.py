from games import game_db
from match import match
from typing import List, Tuple, Callable, Any

def get_title(game: Tuple[str, str, int, List[str]]) -> str:
    return game[0]


def get_developer(game: Tuple[str, str, int, List[str]]) -> str:
    return game[1]


def get_year(game: Tuple[str, str, int, List[str]]) -> int:
    return game[2]


def get_characters(game: Tuple[str, str, int, List[str]]) -> List[str]:
    return game[3]

def title_by_year(matches: List[str]) -> List[str]:
    year = int(matches[0])
    result = []
    for i in game_db:
        if get_year(i)==year:
            result.append(get_title(i))
    return result

def title_by_year_range(matches: List[str]) -> List[str]:
    result=[]
    start=int(matches[0])
    end=int(matches[1])
    for i in game_db:
        year=get_year(i)
        if year>=start and year<=end:
            result.append(get_title(i))
    return result



def title_before_year(matches: List[str]) -> List[str]:
    result=[]
    before=int(matches[0])
    for i in game_db:
        year=get_year(i)
        if year<before:
            result.append(get_title(i))
    return result

def title_after_year(matches: List[str]) -> List[str]:
    result=[]
    after=int(matches[0])
    for i in game_db:
        year=get_year(i)
        if year>after:
            result.append(get_title(i))
    return result


def developer_by_title(matches: List[str]) -> List[str]:
    result=[]
    title=matches[0]
    for i in game_db:
        if get_title(i)==title:
            result.append(get_developer(i))
    return result

def title_by_developer(matches: List[str]) -> List[str]:
    result=[]
    developer=matches[0]
    for i in game_db:
        if get_developer(i)==developer:
            result.append(get_title(i))
    return result

def characters_by_title(matches: List[str]) -> List[str]:
    result=[]
    title=matches[0]
    for i in game_db:
        if get_title(i)==title:
            result = get_characters(i)
            break
    return result  

def title_by_character(matches: List[str]) -> List[str]:
    result=[]
    character=matches[0]
    for i in game_db:
        characterlist = get_characters(i)
        if character in characterlist:
            result.append(get_title(i))
    return result

def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt
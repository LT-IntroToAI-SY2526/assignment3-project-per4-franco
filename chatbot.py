from games import game_db
from match import match
from typing import List, Tuple, Callable, Any

def get_title(game: Tuple[str, str, int, List[str], List[str]]) -> str:
    return game[0]


def get_developer(game: Tuple[str, str, int, List[str], List[str]]) -> str:
    return game[1]


def get_year(game: Tuple[str, str, int, List[str], List[str]]) -> int:
    return game[2]


def get_characters(game: Tuple[str, str, int, List[str], List[str]]) -> List[str]:
    return game[3]

def get_genre(game: Tuple[str, str, int, List[str], List[str]]) -> List[str]:
    return game[4]

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

def title_by_genre(matches: List[str]) -> List[str]:
    result=[]
    genre=matches[0]
    for i in game_db:
        genrelist = get_genre(i)
        if genre in genrelist:
            result.append(get_title(i))
    return result

def genre_by_title(matches: List[str]) -> List[str]:
    result=[]
    title=matches[0]
    for i in game_db:
        if get_title(i)==title:
            result = get_genre(i)
            break
    return result  

def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt

pa_list = [
    (str.split("what games were made in _"), title_by_year),
    (str.split("what games were made before _"), title_before_year),
    (str.split("what games were made after _"), title_after_year),
    (str.split("what games were made between _ and _"), title_by_year_range),
    (str.split("who developed %"), developer_by_title),
    (str.split("what games were developed by %"), title_by_developer),
    (str.split("who are the characters in %"), characters_by_title),
    (str.split("in what games did % appear"), title_by_character),
    (str.split("what games are in the % genre"), title_by_genre),
    (str.split("what genre is %"), genre_by_title),
    (["bye"], bye_action),
]

def search_pa_list(src: List[str]) -> List[str]:
    for pattern, action in pa_list:
        matches = match(pattern, src)
        if matches != None:
            result = action(matches)
            if result == []:
                return ["No answers"]
            return result
    return ["I don't understand"]


def query_loop() -> None:
    #this is the chatbot
    
    print("Welcome to the game database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")



if __name__ == "__main__":
    # ----- TESTS -----
    # Testing title_by_year
    assert isinstance(title_by_year(["2017"]), list), "title_by_year not returning a list"
    assert sorted(title_by_year(["2017"])) == sorted(
        ["the legend of zelda: breath of the wild", "hollow knight", "super mario odyssey"]
    ), "failed title_by_year test"

    # Testing title_by_year_range
    assert isinstance(title_by_year_range(["2015", "2017"]), list), "title_by_year_range not returning a list"
    assert sorted(title_by_year_range(["2015", "2017"])) == sorted(
    [
        "the witcher 3: wild hunt",
        "undertale",
        "metal gear solid v: the phantom pain",
        "dark souls iii",
        "persona 5",
        "stardew valley",
        "the legend of zelda: breath of the wild",
        "hollow knight",
        "super mario odyssey",
    ]
    ), "failed title_by_year_range test"


    # Testing title_before_year
    assert isinstance(title_before_year(["2010"]), list), "title_before_year not returning a list"
    assert sorted(title_before_year(["2010"])) == sorted(
        ["half-life 2", "final fantasy vii", "metal gear solid 3: snake eater", "bioshock", "persona 4"]
    ), "failed title_before_year test"

    # Testing title_after_year
    assert isinstance(title_after_year(["2020"]), list), "title_after_year not returning a list"
    assert sorted(title_after_year(["2020"])) == sorted(
        ["elden ring", "god of war ragnarok", "the legend of zelda: tears of the kingdom"]
    ), "failed title_after_year test"

    # Testing developer_by_title
    assert isinstance(developer_by_title(["portal 2"]), list), "developer_by_title not returning a list"
    assert developer_by_title(["portal 2"]) == ["valve"], "failed developer_by_title test"

    # Testing title_by_developer
    assert isinstance(title_by_developer(["cd projekt red"]), list), "title_by_developer not returning a list"
    assert sorted(title_by_developer(["cd projekt red"])) == sorted(
        ["the witcher 3: wild hunt", "cyberpunk 2077", "the witcher 2: assassins of kings"]
    ), "failed title_by_developer test"

    # Testing characters_by_title
    assert isinstance(characters_by_title(["god of war"]), list), "characters_by_title not returning a list"
    assert sorted(characters_by_title(["god of war"])) == sorted(
        ["kratos", "atreus"]
    ), "failed characters_by_title test"

    # Testing title_by_character
    assert isinstance(title_by_character(["link"]), list), "title_by_character not returning a list"
    assert sorted(title_by_character(["link"])) == sorted(
        ["the legend of zelda: breath of the wild", "the legend of zelda: tears of the kingdom"]
    ), "failed title_by_character test"

    # Testing title_by_genre
    assert isinstance(title_by_genre(["open world"]), list), "title_by_genre not returning a list"
    assert "elden ring" in title_by_genre(["open world"]), "failed title_by_genre test"

    # Testing genre_by_title
    assert isinstance(genre_by_title(["hollow knight"]), list), "genre_by_title not returning a list"
    assert sorted(genre_by_title(["hollow knight"])) == sorted(
        ["metroidvania", "platformer"]
    ), "failed genre_by_title test"

    # Testing search_pa_list
    assert search_pa_list(["what", "games", "were", "made", "in", "2050"]) == ["No answers"], "failed search_pa_list test 1"
    assert search_pa_list(["random", "query"]) == ["I don't understand"], "failed search_pa_list test 2"
    assert search_pa_list(["who", "developed", "portal", "2"]) == ["valve"], "failed search_pa_list test 3"

    print("All tests passed!")

    # THEN run chatbot
    query_loop()


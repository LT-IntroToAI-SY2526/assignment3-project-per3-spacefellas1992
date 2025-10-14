# Important variables:
#     movie_db: list of 4-tuples (imported from book.py)
#     pa_list: list of pattern-action pairs (queries)
#       pattern - strings with % and _ (not consecutive)
#       action  - return list of strings

# THINGS TO ASK THE BOOK CHAT BOT:
# what books were written in _ (must be date)
# what books were written between _ and _
# what books were written before _
# what books were written after _
# who wrote %
# what books were written by %
# who appears in %
# when was % written
# in what books did % appear
# bye

from book import movie_db  # still called movie_db for simplicity
from match import match
from typing import List, Tuple, Callable, Any

# Projection functions for access to tuple elements
def get_title(book: Tuple[str, str, int, List[str]]) -> str:
    return book[0]

def get_author(book: Tuple[str, str, int, List[str]]) -> str:
    return book[1]

def get_year(book: Tuple[str, str, int, List[str]]) -> int:
    return book[2]

def get_characters(book: Tuple[str, str, int, List[str]]) -> List[str]:
    return book[3]

# Action functions
def title_by_year(matches: List[str]) -> List[str]:
    year = int(matches[0])
    return [get_title(book) for book in movie_db if get_year(book) == year]

def title_by_year_range(matches: List[str]) -> List[str]:
    start_year, end_year = int(matches[0]), int(matches[1])
    return [get_title(book) for book in movie_db if start_year <= get_year(book) <= end_year]

def title_before_year(matches: List[str]) -> List[str]:
    year = int(matches[0])
    return [get_title(book) for book in movie_db if get_year(book) < year]

def title_after_year(matches: List[str]) -> List[str]:
    year = int(matches[0])
    return [get_title(book) for book in movie_db if get_year(book) > year]

def author_by_title(matches: List[str]) -> List[str]:
    title = matches[0]
    return [get_author(book) for book in movie_db if get_title(book) == title]

def title_by_author(matches: List[str]) -> List[str]:
    author = matches[0]
    return [get_title(book) for book in movie_db if get_author(book) == author]

def characters_by_title(matches: List[str]) -> List[str]:
    title = matches[0]
    for book in movie_db:
        if get_title(book) == title:
            return get_characters(book)
    return []

def year_by_title(matches: List[str]) -> List[int]:
    title = matches[0]
    return [get_year(book) for book in movie_db if get_title(book) == title]

def title_by_character(matches: List[str]) -> List[str]:
    character = matches[0]
    return [get_title(book) for book in movie_db if character in get_characters(book)]

def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt

# Pattern-action list
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what books were written in _"), title_by_year),
    (str.split("what books were written between _ and _"), title_by_year_range),
    (str.split("what books were written before _"), title_before_year),
    (str.split("what books were written after _"), title_after_year),
    (str.split("who wrote %"), author_by_title),
    (str.split("what books were written by %"), title_by_author),
    (str.split("who appears in %"), characters_by_title),
    (str.split("when was % written"), year_by_title),
    (str.split("in what books did % appear"), title_by_character),
    (["bye"], bye_action),
]

def search_pa_list(src: List[str]) -> List[str]:
    for pat, act in pa_list:
        mat = match(pat, src)
        if mat is not None:
            ans = act(mat)
            return ans if ans else ["No answers"]
    return ["I don't understand"]

def query_loop() -> None:
    print("Welcome to the book database!\n")
    while True:
        try:
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)
        except (KeyboardInterrupt, EOFError):
            break
    print("\nSo long!\n")

if __name__ == "__main__":
    print("Book database ready to query!")

from datetime import datetime as dt
from teams.exceptions import (
    NegativeTitlesError,
    InvalidYearCupError,
    ImpossibleTitlesError,
)


def data_processing(selection):
    titles = selection.get("titles")
    first_cup = selection.get("first_cup")

    if titles < 0:
        raise NegativeTitlesError()

    first_cup_date = dt.strptime(first_cup, "%Y-%m-%d")
    first_cup = first_cup_date.year

    if (first_cup - 1930) % 4 != 0 or first_cup < 1930:
        raise InvalidYearCupError()

    max_titles = (dt.now().year - first_cup) // 4

    if titles > max_titles:
        raise ImpossibleTitlesError()

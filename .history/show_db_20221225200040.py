from functions import get_lines
from constants import DATA_BASE


def show(DAta):
    """
    Показывает базу данных.

    :return:
    """
    reader = get_lines()
    for row in reader:
        print(*row.values())

from functions import give_int
from constants import ABILITIES
activity = 'Выберите действие из списка:\n'

def get_menu_item():
    """
    Функция выводит все возможные действия с БД
    Returns:
       choice: Выбор пользователя -> int
    """
    for i, item in list(enumerate(ABILITIES, start=1)):
        print(i, item, end='\n')
    choice = give_int(activity, 1)
    return choise
def main_menu():
    print(list(enumerate(ABILITIES, start = 1)), sep='\n')

main_menu()
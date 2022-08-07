"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая вернет уникальные элементы списка
"""


def get_unique_in_list(some_list: list) -> set:
    unique = []
    unique_list = {}
    for i in some_list:
        if i not in unique:
            unique.append(i)
            unique_list = set(unique)
    return unique_list


if __name__ == '__main__':
    assert get_unique_in_list([1, 2, 3, 1, 2, 4, 5]) == {1, 2, 3, 4, 5}
    print('Решено!')

"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая вернет поверхностную копию множества
"""


def copy_set(collection: set) -> set:
    copy_set = collection.copy
    return copy_set

if __name__ == '__main__':
    some_set = {1, 2, 3}
    col_copy = copy_set(some_set)
    assert col_copy is not some_set
    print('Решено!')

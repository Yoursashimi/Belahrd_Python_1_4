"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Есть база WORKERS с днями рождений сотрудников

Написать функцию get_workers_names, которая возвращает все имена работников
"""
WORKERS = {
    'Декоратор Иван Олегович': '13.05.1980',
    'Баг Илья Андреевич': '07.09.1995',
    'Питонов Петр Сергеевич': '25.12.1991',
    'Асинхронова Алла Анатольевна': '05.01.1987',
}


def get_workers_names(workers: dict):
    name = workers.keys()
    result = name
    return result


if __name__ == '__main__':
    print('В нашей компании работают:')
    for name in get_workers_names(WORKERS):
        print(f"- {name}")

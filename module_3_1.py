# Домашняя работа по уроку "Пространство имён"


# Функция count_calls подсчитывающая вызовы остальных функций.

# Функция string_info принимает аргумент - строку и возвращает кортеж из:
# длины этой строки, строку в верхнем регистре, строку в нижнем регистре.

# Функция is_contains принимает два аргумента:
# строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует.
# Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string: str):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string: str, list_string: list[str]):
    count_calls()
    for i in list_string:
        if string.lower() == i.lower():
            return True
        else:
            continue
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
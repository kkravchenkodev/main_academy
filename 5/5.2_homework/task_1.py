"""
Написать метод, который делает поиск по словарю по неполному названию ключа.
Например, есть словарь
months = {
    "january": 31,
    "february": 28,
    "march": 31,
    # заполните, пожалуйста, дальше ;)
}
поиск по “jan”
результат - 31
посик “uary”
результат - 28, 31
"""

months = {
    "january": 31,
    "february": 28,
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
}


def partial_filter(text, dictionary):
    return [dictionary.get(key) for key in dictionary.keys() if text in key]
    # out_list = []
    # for key in dictionary.keys():
    #     if text in key:
    #         out_list.append(dictionary.get(key))
    # return out_list


print(partial_filter('un', months))

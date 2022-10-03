def dict_handler(dictionary, key, default_value):
    try:
        return dictionary[key]
    except KeyError:
        dictionary[key] = default_value
    except TypeError:
        raise TypeError("змінний key")
    return dictionary[key]


if __name__ == "__main__":
    dictionary_1 = {'Sasha': 21, 'Ivan': 23}
    print(dict_handler(dictionary_1, 'Sasha', 26))
    print(dict_handler(dictionary_1, 'Max', 19))
    print(dict_handler(dictionary_1, ['Max', 'Rita'], 25))
    print(dictionary_1)
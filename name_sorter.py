def name_sorter(names):
    """ Sort names and separate male and females

    :param list names: list of names
    :rtype: dict
    :return: dict with separate names
    """
    dict_names = {
        "female": [],
        "male": []
    }
    for word in names:
        if word[-1] == "a":
            dict_names["female"].append(word)
        else:
            dict_names["male"].append(word)
    return dict_names


if __name__ == "__main__":
    names = ["Ania", "Basia", "Marek", "Andrzej", "Helena", "Błażej", "Zenon"]
    print(name_sorter(names))
    names = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]
    print(name_sorter(names))

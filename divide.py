def div(start, end):
    """ Make list with numbers divided by 2 and not divided by 3 from start to end
    :param int start: start range
    :param int end: end range
    :return: numbers from start to end divided by 2 and not divided by 3
    """
    return [i for i in range(start, end+1) if i % 2 == 0 and i % 3 != 0]


if __name__ == "__main__":
    print(div(0, 20))
    print(div(23, 45))

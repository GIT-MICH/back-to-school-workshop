from random import shuffle


def get_numbers():
    """
    Get the numbers from player
    Try until player guess right numbers.
    :rtype: int
    :return: given numbers as int
    """
    while True:
        try:
            player_numbers = int(input(" Guess the numbers: "))
            break
        except ValueError:
            print("It's not a number!")
    return player_numbers


def check_num():
    """
    Get 6 different numbers from player between 1 and 49
    :rtype: list
    :return: list with 6 numbers provide by player
    """
    table = []
    while len(table) < 6:
        my_num = get_numbers()
        if my_num not in table and 0 < my_num <= 49:
            table.append(my_num)
    return table


def sorted_numbers(numbers):
    """Sorted given numbers with ascending order.
    :param list numbers: list of numbers
    """
    print(", ".join(str(number) for number in sorted(numbers)))


def draw_numbers():
    """ Choose 6 random numbers
    :rtype: list
    :return: list with 6 random numbers
    """
    numbers = list(range(1, 49))
    shuffle(numbers)
    return numbers[:6]


def lotto():
    """ Main function in our program."""
    my_numbers = check_num()
    print("Your numbers: ")
    sorted_numbers(my_numbers)

    comp_numbers = draw_numbers()
    print("Lotto numbers: ")
    sorted_numbers(comp_numbers)

    hits = 0
    for number in my_numbers:
        if number in comp_numbers:
            hits += 1
    print(f"You hit {hits} {'number' if hits == 1 else 'numbers'}!")


if __name__ == "__main__":
    lotto()

from random import randint


def player_num():
    """
    Get number from player.
    Try until player guess right number.
    :rtype: int
    :return: given number as int
    """
    while True:
        try:
            player_number = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number!")
    return player_number


def number():
    """ Main function with our game """
    comp_num = randint(1, 100)
    player = player_num()
    while player != comp_num:
        if player < comp_num:
            print("Too small!")
        else:
            print("Too big!")
        player = player_num()
    print("You win!")


if __name__ == "__main__":
    number()

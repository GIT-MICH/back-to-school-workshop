import random


def roll(dices, dice_type=6, modifier=0):
    """Simulate dices roll with modifier
    :param int dices: number of dices
    :param int dice_type: type of dices, default is 6
    :param int modifier: modifier values, default is 0
    :rtype: int
    :return: values of dice roll modified by modifier
    """
    if dice_type not in (3, 4, 6, 8, 10, 12, 100):
        raise Exception("No such dice !")
    return sum(random.randint(1, dice_type) for _ in range(dices)) + modifier


if __name__ == "__main__":
    print(roll(1))
    print(roll(2, 10, 20))
    print(roll(1, 100))
    print(roll(3, 6, -3))
    print(roll(3, 2, 5))

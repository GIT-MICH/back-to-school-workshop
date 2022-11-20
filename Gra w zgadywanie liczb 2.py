def user_input():
    """ Return proper value provided by user
    :rtype: str
    :return: value provided by user: ["to small", "to big", "you won"]
    """
    possible_input = ["to big", "to small", "you won"]
    while True:
        user_answer = input().lower()
        if user_answer in possible_input:
            break
        print("Input is not in ['to small', 'to big', 'you won']")
    return user_answer


def guess_the_number():
    """Main function in our program"""
    print("Imagine the number between 1 and 1000")
    print("Press 'ENTER' to continue")
    input()
    min_number = 0
    max_number = 1000
    user_answer = ""
    while user_answer != "you won":
        guess = (max_number - min_number) // 2 + min_number
        print(f"Your number is: {guess}")
        user_answer = user_input()
        if user_answer == 'to big':
            max_number = guess
        elif user_answer == 'to small':
            min_number = guess
    print("Hurra! I guess")


if __name__ == "__main__":
    guess_the_number()

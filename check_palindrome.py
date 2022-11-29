def check_palindrome(text):
    """ Check if given text is palindrome
    :param str text: text
    :rtype: bool
    :return: True if given text is palindrome and False if not
    """
    text = text.lower().replace(" ", "")
    text_pal = text[::-1]
    if text_pal == text:
        return True
    else:
        return False


if __name__ == "__main__":
    text = "ZakoPane na Pokaz"
    print(check_palindrome(text))
    text = "Palidrom to nie jest"
    print(check_palindrome(text))
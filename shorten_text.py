
def shorten(text):
    """Make text shortened.
    :param str entry: some text
    :rtype: str
    :return: shortened text
    """
    return "".join(word[0] for word in text.upper().split())


if __name__ == "__main__":
    text = "Python is the best!"
    print(shorten(text))
    text = "doN't liKE misTaKe"
    print(shorten(text))
    text = "Show Me Your Code"
    print(shorten(text))


def shorten(text):
    """Make text shortened.
    :param str entry: some text
    :rtype: str
    :return: shortened text
    """
    return "".join(word[0] for word in text.upper().split())


if __name__ == "__main__":
    entry = "Python is the best!"
    print(shorten(entry))
    entry = "doN't liKE misTaKe"
    print(shorten(entry))
    entry = "Show Me Your Code"
    print(shorten(entry))

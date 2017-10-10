import random

ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyz "


def create_text(length):
    new_text = []
    for counter in range(0, length):
        index = random.randint(0, len(ALLOWED_CHARS) - 1)
        next_char = ALLOWED_CHARS[index]
        new_text.append(next_char)

    text = "".join(new_text)

    return text


def get_random_char():
    index = random.randint(0, len(ALLOWED_CHARS) - 1)
    char = ALLOWED_CHARS[index]
    return char
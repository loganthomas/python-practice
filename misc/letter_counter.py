"""
Practice Problem:

Given a word and a letter, count the number of occurrences the given
letter has in the given word.
"""


def letter_counter(word, letter):
    """
    Count number of times a give letter occurs in a given word.

    Args:
        word (str): Word provided in which to count letter
        letter (str): Letter provided to count in word. Of length 1.

    Returns:
        count - int representing number of times a give letter occurs
                within the given word

    """
    if word.isnumeric():
        raise TypeError(f"Given word: '{word}' is a number not a word")

    if letter.isnumeric():
        raise TypeError(f"Given letter: '{letter}' is a number not a string")

    if len(letter) != 1:
        raise ValueError(f"Given letter: '{letter}' must be one character long")

    count = sum([1 for let in word if let == letter])

    print(f'{letter} occurs {count} time(s) in {word}')

    return count


if __name__ == '__main__':
    user_word = input('Please enter a word: ')
    user_letter = input('Please enter a letter: ')
    count = letter_counter(user_word, user_letter)

"""
Practice Problem:

Given a word and a letter, count the number of occurrences the given
letter has in the given word.
"""


def letter_counter(word, letter):
    """
    Count number of times a give letter occurs in a given word.

    Args:
        word   - string
        letter - string of length 1

    Returns:
        count - int representing number of times a give letter occurs
                within the given word

    """
    # Check if word is a string
    if type(word) != str:
        raise TypeError('Given word is not a string')

    # Check if letter is a string
    if type(letter) != str:
        raise TypeError('Given letter is not a string')

    # Check if letter is only one character
    if len(letter) != 1:
        raise ValueError('Enter a letter that is one character long')

    count = sum([1 for let in word if let == letter])

    print('{} occurs {} time(s) in {}'.format(letter, count, word))

    return count


if __name__ == '__main__':
    user_word = input('Please enter a word: ')
    user_letter = input('Please enter a letter: ')
    count = letter_counter(user_word, user_letter)

def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    phrase_dict = {}
    for i in phrase:
        if i not in phrase_dict:
            phrase_dict[i] = 1
        else:
            phrase_dict[i] += 1

    return phrase_dict


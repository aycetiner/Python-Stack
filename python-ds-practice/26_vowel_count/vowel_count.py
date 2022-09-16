def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!')
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    dict_of_vowels = {}

    for i in phrase:
        low_i = i.lower()
        if low_i in vowels:
            if low_i in dict_of_vowels.keys():
                dict_of_vowels[low_i] += 1
            else:
                dict_of_vowels[low_i] = 1
    return dict_of_vowels

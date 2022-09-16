def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapped_phrase = ''
    for i in phrase:
        if i.lower() == to_swap.lower():
            swapped_phrase += (i.swapcase())
        else:
            swapped_phrase += i

    return swapped_phrase

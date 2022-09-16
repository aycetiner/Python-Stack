def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase_lst = []
    phrase_condensed = phrase.replace(" ", "")

    for i in phrase_condensed:
        phrase_lst.append(i.lower())

    reversed_phrase_lst = phrase_lst[::-1]

    if reversed_phrase_lst == phrase_lst:
        return True

    return False

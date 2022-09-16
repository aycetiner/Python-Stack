def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    lst = phrase.split(' ')
    new_phrase = ''
    for i in lst:
        new_word = i.lower().capitalize()
        new_phrase = new_phrase + " " + new_word

    return new_phrase.strip()

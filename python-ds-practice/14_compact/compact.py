def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    lst_of_trues = []
    for i in lst:
        if i:
            lst_of_trues.append(i)

    return lst_of_trues

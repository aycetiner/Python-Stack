def print_upper_words(words, must_start_with):
    """Prints the words that start with a letter in must_start_with list"""

    # YOUR CODE HERE
    for word in words:
        first_letter = word[0].lower()
        if first_letter in must_start_with:
            print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                  must_start_with={"h", "y"})

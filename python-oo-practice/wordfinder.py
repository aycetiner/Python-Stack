import random


class WordFinder:
    """Word Finder: finds random words from a dictionary.

    >>> wf = WordFinder("words.txt")

    >>> random.seed(1)

    >>> rand_word = wf.random()

    >>> random.seed(1)

    >>> wf.random()
    rand_word

    """

    def __init__(self, path):
        dict_file = open(path)
        self.lines = self.parse(dict_file)
        print(f"{len(self.lines)} words read")

    def parse(self, dict_file):
        return [line.strip() for line in dict_file]

    def random(self):
        return random.choice(self.lines)


# wf = WordFinder("words.txt")
#
# print(wf.random())


class SpecialWordFinder(WordFinder):

    def parse(self, dict_file):
        return [line.strip() for line in dict_file if line.strip() and not line.startswith('#')]


# wf = SpecialWordFinder("special_words.txt")
#
# print(wf.random())

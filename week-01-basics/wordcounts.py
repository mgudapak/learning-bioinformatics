#!/usr/bin/python3

"""
Wordcount exercise
Google's Python class

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().
"""

import sys, pprint

"""
    1. For the --count flag, implement a print_words(filename) function that counts
    how often each word appears in the text and prints:
        word1 count1
        word2 count2
        ...

    Print the above list in order sorted by word (python will sort punctuation to
    come before letters -- that's fine). Store all the words as lowercase,
    so 'The' and 'the' count as the same word.
"""


def print_words(filename):
    print()
    print("Calling print_words()...")
    print()

    word_count = {}
    f = open(filename, "r")

    for line in f:
        words = line.lower().split()

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

    f.close()

    # IMP! - print() -> by default, prints the dict in the order they were inserted
    print(word_count)

    # IMP! - pprint() -> by default, prints the dict in ascending order of the keys
    # pprint.pprint(word_count)
    for k, v in sorted(word_count.items()):
        print(k, " ", v)
    return


"""
    2. For the --topcount flag, implement a print_top(filename) which is similar
    to print_words() but which prints just the top 20 most common words sorted
    so the most common word is first, then the next most common, and so on.

    Use str.split() (no arguments) to split on all whitespace.
"""


def print_top(filename):
    print()
    print("Calling print_top()...")
    print()

    word_count = {}
    f = open(filename, "r")

    for line in f:
        words = line.lower().split()

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

    f.close()

    # IMP! - print() -> by default, prints the dict in the order they were inserted
    print(word_count)

    # IMP! - pprint() -> by default, prints the dict in ascending order of the keys
    # pprint.pprint(word_count)
    for k in word_count:
        print(k, " ", word_count[k])

    for k, v in sorted(word_count.items(), key=sortByWordCount, reverse=True)[:20]:
        print(k, " ", v)

    return


def print_top_n(filename):
    print()
    print("Calling print_top_n()...")
    print()

    word_count = {}
    f = open(filename, "r")

    for line in f:
        words = line.lower().split()

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

    f.close()

    # IMP! - print() -> by default, prints the dict in the order they were inserted
    print(word_count)

    # IMP! - pprint() -> by default, prints the dict in ascending order of the keys
    # pprint.pprint(word_count)
    for k, v in sorted(word_count.items(), key=sortByWordCount, reverse=True)[:20]:
        print(k, " ", v)


def sortByWordCount(word):
    return word[1]


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print("usage: ./wordcount.py {--count | --topcount | --topn} file")
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == "--count":
        print_words(filename)
    elif option == "--topcount":
        print_top(filename)
    elif option == "--topn":
        print_top_n(filename)
    else:
        print("unknown option: " + option)
        sys.exit(1)


if __name__ == "__main__":
    main()

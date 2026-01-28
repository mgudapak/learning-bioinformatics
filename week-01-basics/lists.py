#!/usr/bin/python3

from operator import itemgetter

"""
A. match_ends
Given a list of strings, return the count of the number of
strings where the string length is 2 or more and the first
and last chars of the string are the same.
Note: python does not have a ++ operator, but += works.
"""


def match_ends(words):
    count = 0
    for word in words:
        if len(word) >= 2 and (word[:1] == word[-1:]):
            count += 1
    return count


"""
    B. front_x
    Given a list of strings, return a list with the strings
    in sorted order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    
"""


def front_x(words):
    words.sort()
    only_x = []
    non_x = []

    for word in words:
        if word[:1] == "x":
            only_x.append(word)
        else:
            non_x.append(word)

    only_x.extend(non_x)

    return only_x


"""
    C. sort_last
    Given a list of non-empty tuples, return a list sorted in increasing
    order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
"""


def sort_last(tuples):
    return sorted(tuples, key=itemgetter(-1))


"""
    D. Given a list of numbers, return a list where
    all adjacent == elements have been reduced to a single element,
    so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
    modify the passed in list.
"""


def remove_adjacent(nums):

    return


"""
    E. Given two lists sorted in increasing order, create and return a merged
    list of all the elements in sorted order. You may modify the passed in lists.
    Ideally, the solution should work in "linear" time, making a single
    pass of both lists.
"""


def linear_merge(list1, list2):
    index1 = 0
    index2 = 0
    merged_list = []

    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] <= list2[index2]:
            merged_list.append(list1[index1])
            index1 += 1
        else:
            merged_list.append(list2[index2])
            index2 += 1

    if index1 < len(list1):
        merged_list.extend(list1[index1:])

    if index2 < len(list2):
        merged_list.extend(list2[index2:])

    return merged_list


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = " OK "
    else:
        prefix = "  X "
    print("%s got: %s expected: %s" % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print("match_ends")
    test(match_ends(["aba", "xyz", "aa", "x", "bbb"]), 3)
    test(match_ends(["", "x", "xy", "xyx", "xx"]), 2)
    test(match_ends(["aaa", "be", "abc", "hello"]), 1)

    print()
    print("front_x")
    test(
        front_x(["bbb", "ccc", "axx", "xzz", "xaa"]),
        ["xaa", "xzz", "axx", "bbb", "ccc"],
    )
    test(
        front_x(["ccc", "bbb", "aaa", "xcc", "xaa"]),
        ["xaa", "xcc", "aaa", "bbb", "ccc"],
    )
    test(
        front_x(["mix", "xyz", "apple", "xanadu", "aardvark"]),
        ["xanadu", "xyz", "aardvark", "apple", "mix"],
    )

    print()
    print("sort_last")
    test(sort_last([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]), [(3, 1), (1, 2), (2, 3)])
    test(
        sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
        [(2, 2), (1, 3), (3, 4, 5), (1, 7)],
    )
    print()
    print("linear_merge")
    test(linear_merge(["aa", "xx", "zz"], ["bb", "cc"]), ["aa", "bb", "cc", "xx", "zz"])
    test(linear_merge(["aa", "xx"], ["bb", "cc", "zz"]), ["aa", "bb", "cc", "xx", "zz"])
    test(linear_merge(["aa", "aa"], ["aa", "bb", "bb"]), ["aa", "aa", "aa", "bb", "bb"])


if __name__ == "__main__":
    main()

#!/usr/bin/python3


"""
E. Given two lists (already) sorted in increasing order, create and return a merged
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

    print("")
    print("linear_merge")
    test(linear_merge([1], [4]), [1, 4])
    test(linear_merge([1, 2], [4, 5]), [1, 2, 4, 5])
    test(linear_merge([1, 2], [4]), [1, 2, 4])
    test(linear_merge([1, 2, 5, 6], [4]), [1, 2, 4, 5, 6])
    test(linear_merge([1], [2, 5, 16]), [1, 2, 5, 16])

    test(linear_merge([4], [1]), [1, 4])
    test(linear_merge([4, 5], [1, 2]), [1, 2, 4, 5])
    test(linear_merge([4], [1, 2]), [1, 2, 4])
    test(linear_merge([4], [1, 2, 5, 6]), [1, 2, 4, 5, 6])
    test(linear_merge([2, 5, 16], [1]), [1, 2, 5, 16])

    test(linear_merge([4], [1]), [1, 4])
    test(linear_merge([4, 5], [1, 2]), [1, 2, 4, 5])


if __name__ == "__main__":
    main()

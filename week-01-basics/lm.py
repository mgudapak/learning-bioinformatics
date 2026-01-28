#!/usr/bin/python3

from operator import itemgetter

"""
    E. Given two lists (already) sorted in increasing order, create and return a merged
    list of all the elements in sorted order. You may modify the passed in lists.
    Ideally, the solution should work in "linear" time, making a single
    pass of both lists.
"""


def linear_merge(list1, list2):
    print("-----")
    print(list1, list2)

    list1_len = len(list1)
    list2_len = len(list2)
    list1_index = 0

    merged_list = []

    list2_index = 0
    # iterate over List 1
    for list1_item in list1:

        while list2_index < len(list2):
            if list1_item <= list2[list2_index]:
                # ORDER IS - list1_item, list2[list2_index]
                # first check if the larger of the two (i.e. list2[list2_index]) <= last_item_of_merged_list
                if len(merged_list) > 0:
                    if list2[list2_index] <= merged_list[-1]:
                        # if Yes,
                        # insert(-1, list1_item)
                        merged_list.insert(-1, list1_item)
                        # insert(-1, list2[list2_index])
                        merged_list.insert(-1, list2[list2_index])
                        # FINAL LIST ORDER IS - list1_item, list2[list2_index], last_item_of_merged_list
                    else:
                        # if No,
                        # append(list2[list2_index])
                        merged_list.append(list2[list2_index])
                        # the ORDER IS last item of merged_list, list2[list2_index]
                        # then check if the smaller of the two (i.e. list1_item) <= last item of merged_list
                        if list1_item <= merged_list[-2]:
                            # if Yes, insert(-2, list1_item)
                            merged_list.insert(-2, list1_item)
                            # FINAL LIST ORDER IS - list1_item, last item of merged_list, list2[list2_index]
                        else:
                            # if No, insert(-1, list1_item)
                            merged_list.insert(-1, list1_item)
                            # FINAL LIST ORDER IS - last item of merged_list, list1_item, list2[list2_index]
                else:
                    merged_list.append(list1_item)
                    merged_list.append(list2[list2_index])

            else:
                # ORDER IS - list2[list2_index], list1_item
                if len(merged_list) > 0:
                    if list2[list2_index] <= merged_list[-1]:
                        # if Yes,
                        # insert(-1, list1_item)
                        merged_list.insert(-1, list1_item)
                        # insert(-1, list2[list2_index])
                        merged_list.insert(-1, list2[list2_index])
                        # FINAL LIST ORDER IS - list1_item, list2[list2_index], last_item_of_merged_list
                    else:
                        # if No,
                        # append(list2[list2_index])
                        merged_list.append(list2[list2_index])
                        # the ORDER IS last item of merged_list, list2[list2_index]
                        # then check if the smaller of the two (i.e. list1_item) <= last item of merged_list
                        if list1_item <= merged_list[-2]:
                            # if Yes, insert(-2, list1_item)
                            merged_list.insert(-2, list1_item)
                            # FINAL LIST ORDER IS - list1_item, last item of merged_list, list2[list2_index]
                        else:
                            # if No, insert(-1, list1_item)
                            merged_list.insert(-1, list1_item)
                            # FINAL LIST ORDER IS - last item of merged_list, list1_item, list2[list2_index]
                else:
                    merged_list.append(list1_item)
                    merged_list.append(list2[list2_index])

            list2_index += 1

    # at the end, iterate over any leftover items in List 2
    else:
        if list2_index < list2_len:
            # simply append those
            merged_list.extend(list2[list2_index:])

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
    # test(linear_merge([1], [4]), [1, 4])
    # test(linear_merge([1, 2], [4, 5]), [1, 2, 4, 5])
    # test(linear_merge([1, 2], [4]), [1, 2, 4])
    # test(linear_merge([1, 2, 5, 6], [4]), [1, 2, 4, 5, 6])
    # test(linear_merge([1], [2, 5, 16]), [1, 2, 5, 16])

    # test(linear_merge([4], [1]), [1, 4])
    test(linear_merge([4, 5], [1, 2]), [1, 2, 4, 5])
    test(linear_merge([4], [1, 2]), [1, 2, 4])
    test(linear_merge([4], [1, 2, 5, 6]), [1, 2, 4, 5, 6])
    # test(linear_merge([2, 5, 16], [1]), [1, 2, 5, 16])

    # test(linear_merge([4], [1]), [1, 4])
    # test(linear_merge([4, 5], [1, 2]), [1, 2, 4, 5])


# test(linear_merge(["aa", "xx", "zz"], ["bb", "cc"]), ["aa", "bb", "cc", "xx", "zz"])
# test(linear_merge(["aa", "xx"], ["bb", "cc", "zz"]), ["aa", "bb", "cc", "xx", "zz"])
# test(linear_merge(["aa", "aa"], ["aa", "bb", "bb"]), ["aa", "aa", "aa", "bb", "bb"])


if __name__ == "__main__":
    main()

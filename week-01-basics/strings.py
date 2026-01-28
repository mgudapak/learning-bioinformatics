#!/usr/bin/python3

import sys, math

"""
    A. donuts
    Given an int count of a number of donuts, return a string
    of the form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word 'many'
    instead of the actual count.
    So donuts(5) returns 'Number of donuts: 5'
    and donuts(23) returns 'Number of donuts: many'
"""


def donuts(count):
    if count >= 10:
        suffix = "many"
    elif count < 10:
        suffix = str(count)

    return "Number of donuts: %s" % suffix


"""
    B. both_ends
    Given a string s, return a string made of the first 2
    and the last 2 chars of the original string,
    so 'spring' yields 'spng'. However, if the string length
    is less than 2, return instead the empty string.
"""


def both_ends(s):
    if len(s) < 2:
        return ""
    else:
        return s[:2] + s[-2:]


"""
    C. fix_start
    Given a string s, return a string
    where all occurences of its first char have
    been changed to '*', except do not change
    the first char itself.
    e.g. 'babble' yields 'ba**le'
    Assume that the string is length 1 or more.
    
    
"""


def fix_start(s):
    start_char = s[:1]
    s = s.replace(start_char, "*")
    return start_char + s[1:]


"""
    D. MixUp
    Given strings a and b, return a single string with a and b separated
    by a space '<a> <b>', except swap the first 2 chars of each string.
    e.g.
        'mix', pod' -> 'pox mid'
        'dog', 'dinner' -> 'dig donner'
    Assume a and b are length 2 or more.
"""


def mix_up(a, b):
    return b[:2] + a[2:] + " " + a[:2] + b[2:]


"""
    D. verbing
    Given a string, if its length is at least 3,
    add 'ing' to its end.
    Unless it already ends in 'ing', in which case
    add 'ly' instead.
    If the string length is less than 3, leave it unchanged.
    Return the resulting string.
"""


def verbing(s):
    if len(s) < 3:
        return s
    else:
        if s[-3:] == "ing":
            return s + "ly"
        else:
            return s + "ing"


"""
    E. not_bad
    Given a string, find the first appearance of the
    substring 'not' and 'bad'. If the 'bad' follows
    the 'not', replace the whole 'not'...'bad' substring
    with 'good'.
    Return the resulting string.
    So 'This dinner is not that bad!' yields:
    This dinner is good!
"""


def not_bad(s):
    if s.find("bad") > s.find("not"):
        return s[: s.find("not")] + "good" + s[s.find("bad") + 3 :]
    else:
        return s


"""
    F. front_back
    Consider dividing a string into two halves.
    If the length is even, the front and back halves are the same length.
    If the length is odd, we'll say that the extra char goes in the front half.
    e.g. 'abcde', the front half is 'abc', the back half 'de'.
    Given 2 strings, a and b, return a string of the form
     a-front + b-front + a-back + b-back
"""


def front_back(a, b):
    a_front = a[: math.ceil(len(a) / 2)]
    a_back = a[math.ceil(len(a) / 2) :]
    b_front = b[: math.ceil(len(b) / 2)]
    b_back = b[math.ceil(len(b) / 2) :]

    return a_front + b_front + a_back + b_back


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = " OK "
    else:
        prefix = "  X "
    print("%s got: %s expected: %s" % (prefix, repr(got), repr(expected)))


def main():

    print("donuts")
    test(donuts(4), "Number of donuts: 4")
    test(donuts(9), "Number of donuts: 9")
    test(donuts(10), "Number of donuts: many")
    test(donuts(99), "Number of donuts: many")

    print()
    print("both_ends")
    test(both_ends("spring"), "spng")
    test(both_ends("Hello"), "Helo")
    test(both_ends("a"), "")
    test(both_ends("xyz"), "xyyz")

    print()
    print("fix_start")
    test(fix_start("babble"), "ba**le")
    test(fix_start("aardvark"), "a*rdv*rk")
    test(fix_start("google"), "goo*le")
    test(fix_start("donut"), "donut")

    print()
    print("mix_up")
    test(mix_up("mix", "pod"), "pox mid")
    test(mix_up("dog", "dinner"), "dig donner")
    test(mix_up("gnash", "sport"), "spash gnort")
    test(mix_up("pezzy", "firm"), "fizzy perm")

    print()
    print("verbing")
    test(verbing("hail"), "hailing")
    test(verbing("swiming"), "swimingly")
    test(verbing("do"), "do")

    print()
    print("not_bad")
    test(not_bad("This movie is not so bad"), "This movie is good")
    test(not_bad("This dinner is not that bad!"), "This dinner is good!")
    test(not_bad("This tea is not hot"), "This tea is not hot")
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print("front_back")
    test(front_back("abcd", "xy"), "abxcdy")
    test(front_back("abcde", "xyz"), "abcxydez")
    test(front_back("Kitten", "Donut"), "KitDontenut")


# Standard boilerplate to call the main() function.
if __name__ == "__main__":
    main()

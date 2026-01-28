#!/usr/bin/python3

# import modules used here -- sys is a very standard one
import sys


# Defines a "repeat" function that takes 2 arguments.
def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s + s + s  # can also use "s * 3" which is faster (Why?)
    if exclaim:
        result = result + "!!!"
    return result


# Gather our code in a main() function
# It's typical to def a main() function towards the bottom of the file
# with all the functions it calls above it.
def main():
    if len(sys.argv) >= 2:
        # Command line args are in sys.argv[1], sys.argv[2] ...
        # sys.argv[0] is the script name itself and can be ignored
        name = sys.argv[1]
    else:
        name = "World"

    print("Hello " + name)


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == "__main__":
    main()
    print(repeat("mahesh", True))

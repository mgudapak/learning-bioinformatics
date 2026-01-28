#!/usr/bin/python3

import os, sys
from line import Line


# utility functions
def clear_screen():
    """Clears the terminal screen for Windows, Linux, and macOS."""
    # 'nt' refers to Windows; 'posix' refers to Linux/macOS
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def calculate_gc_percent(summary):
    """
    GC% = ( (Number of Gs + Number of Cs) / Total number of bases ) * 100
    """

    gc_percent = (summary["G"] + summary["C"]) / sum(summary.values()) * 100

    return round(gc_percent, 2)


def summarize_stats(sequence) -> str:
    sequence_length = len(sequence)
    summary = parse_sequence(sequence)

    output = f"""
    Length: {sequence_length}
    A: { summary['A'] }
    C: { summary['C'] }
    G: { summary['G'] }
    T: { summary['T'] }
    N: { summary['N'] }
    GC%: { calculate_gc_percent(summary) }
    """

    return output


def parse_sequence(sequence) -> str:
    occurences = {}

    for base in sequence:
        if base in occurences:
            occurences[base] += 1
        else:
            occurences[base] = 1

    return occurences


def main():
    # clear_screen()

    print("Running sequence-stats-cli-tool.py script ...")

    filename = "./sample-dirty-input-file-00.txt"
    sanitized_file_content = ""

    with open(filename, "r") as f:

        for line in f:

            if "#" in line:
                line = Line(line).strip_comments()

            line = line.strip()
            line = line.upper()

            sanitized_file_content += line

    print(sanitized_file_content)

    print(summarize_stats(sanitized_file_content))


# Standard boilerplate to call the main() function.
if __name__ == "__main__":
    main()

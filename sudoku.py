'''
Jennifer Briere
Porfolio Project - Sudoku
CS 325 Winter 2021
'''

import numpy as np

puzzle = np.array([[" ", " ", " ", " ", " ", 7, 4, " ", 9],
                  [" ", 4, " ", 3, " ", " ", 2, " ", " "],
                  [" ", 9, " ", " ", 8, 4, " ", " ", 5],
                  [6, 1, 3, " ", " ", " ", " ", 7, " "],
                  [" ", " ", " ", 6, " ", " ", 5, " ", " "],
                  [2, " ", " ", " ", 3, " ", " ", 9, " "],
                  [3, " ", " ", 4, 1, 5, " ", 2, " "],
                  [4, " ", 9, 7, 6, " ", " ", " ", 8],
                  [" ", " ", " ", " ", " ", " ", " ", " ", 7]])

# these are the location of the starting numbers and will be immutable
# row: [filled column spots]
starting_numbers = {0: [5, 6, 8],
                    1: [1, 3, 6],
                    2: [1, 4, 5, 8],
                    3: [0, 1, 2, 7],
                    4: [3, 6],
                    5: [0, 4, 7],
                    6: [0, 3, 4, 5, 7],
                    7: [0, 2, 3, 4, 8],
                    8: [8]}

# for testing, be sure to change the value of empty
# puzzle = np.array([[" ", 3, 2, 1, 5, 7, 4, 6, 9],
#                     [7, 4, 5, 3, 9, 6, 2, 8, 1],
#                     [1, 9, 6, 2, 8, 4, 7, 3, 5],
#                     [6, 1, 3, 5, " ", 9, 8, 7, 2],
#                     [9, 8, 4, 6, 7, 2, 5, 1, 3],
#                     [2, 5, 7, 8, 3, 1, 6, 9, 4],
#                     [3, 7, 8, 4, 1, 5, " ", 2, 6],
#                     [4, 2, 9, 7, 6, 3, 1, 5, 8],
#                     [5, 6, 1, 9, 2, 8, 3, 4, 7]])

# for reference
# solved_puzzle =    [[8, 3, 2, 1, 5, 7, 4, 6, 9],
#                     [7, 4, 5, 3, 9, 6, 2, 8, 1],
#                     [1, 9, 6, 2, 8, 4, 7, 3, 5],
#                     [6, 1, 3, 5, 4, 9, 8, 7, 2],
#                     [9, 8, 4, 6, 7, 2, 5, 1, 3],
#                     [2, 5, 7, 8, 3, 1, 6, 9, 4],
#                     [3, 7, 8, 4, 1, 5, 9, 2, 6],
#                     [4, 2, 9, 7, 6, 3, 1, 5, 8],
#                     [5, 6, 1, 9, 2, 8, 3, 4, 7]]


# code to print the board adapted from
# https://towardsdatascience.com/solve-sudokus-automatically-4032b2203b64
def print_puzzle(puzzle):
    print("\n")
    for row in range(len(puzzle)):
        line = ""
        if row == 3 or row == 6:
            print("---------------------")
        for column in range(len(puzzle[row])):
            if column == 3 or column == 6:
                line += "| "
            line += str(puzzle[row][column])+" "
        print(line)


def verify_rows(puzzle):
    for row in range(9):
        r = puzzle[row, 0:9]
        # check that each row has 9 unique numbers
        if len(np.unique(r)) != 9:
            return False
        else:
            # check that those 9 unique numbers are all 1-9
            for x in r:
                if int(x) < 1 or int(x) > 9:
                    return False
    return True


def verify_columns(puzzle):
    for column in range(9):
        c = puzzle[0:9, column]
        # check that each column has 9 unique numbers
        if len(np.unique(c)) != 9:
            return False
        else:
            # check that those 9 unique numbers are all 1-9
            for x in c:
                if int(x) < 1 or int(x) > 9:
                    return False
    return True


def verify_segments(puzzle):
    # divide puzzle into 3 columns of 3
    cols_3 = np.hsplit(puzzle, 3)                   # 1
    for col in cols_3:                              # n/3
        # divide each column of 3 into 3 rows of 3
        subs_3 = np.vsplit(col, 3)                  # 1
        # this results in 9 3x3 segments
        for segment in subs_3:                      # (n/3)/3
            # verify 9 unique numbers in the segment
            if len(np.unique(segment)) == 9:          # 1
                for x in segment:
                    for y in x:                  # n/9
                        # verify each value is 1-9
                        if int(y) < 1 or int(y) > 9:        # 1
                            return False
    return True


def verify_puzzle(puzzle):
    if verify_rows(puzzle):
        if verify_columns(puzzle):
            if verify_segments(puzzle):
                return True


def main():
    # print board on screen
    print_puzzle(puzzle)

    # this is the number of starting empty spots
    # once all are filled the completed board will be verified
    empty = 51

    while empty > 0:
        # ask user for row, column and value to change
        print("Which cell do you want to change?")
        row = int(input("Row (1-9): ")) - 1
        column = int(input("column (1-9): ")) - 1
        val = int(input("Value to assign to the space (1-9): "))

        # users cannot change the starting numbers
        if column in starting_numbers[row]:
            print("That number can't be changed, try again.")
        else:
            # if the spot is empty, decrease the count of empty
            # this allows for changing previously filled spots
            # without affecting the game play loop
            if puzzle[row][column] == " ":
                empty -= 1
            # assign value to selected spot
            puzzle[row][column] = val

        # reprint the puzzle after the spot filled
        print_puzzle(puzzle)

    # loop will exit after all empty spots filled and verify the solution
    if verify_puzzle(puzzle):
        print("Solved! Congratulations!\n")
    else:
        print("Not solved, better luck next time!\n")


if __name__ == "__main__":
    main()

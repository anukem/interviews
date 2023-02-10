def print_2d_array(arr):
    for lst in arr:
        print(lst)


def has_duplicates(arr):
    filtered_list = list(filter(lambda x: x != ".", arr))
    unique_values = set(filtered_list)
    return len(filtered_list) != len(unique_values)


def is_valid_sudoku(puzzle):
    # check horizontal
    for lst in puzzle:
        if has_duplicates(lst):
            return False

    # check vertical
    vertical_lists = [[x[y] for x in puzzle] for y in range(len(puzzle))]

    for lst in vertical_lists:
        if has_duplicates(lst):
            return False

    # check sub boxes
    for sub_box in range(9):
        section = (sub_box // 3) * 3
        group = sub_box % 3
        start = group * 3

        first_three = puzzle[section][start : start + 3]
        second_three = puzzle[section + 1][start : start + 3]
        last_three = puzzle[section + 2][start : start + 3]

        if has_duplicates(first_three + second_three + last_three):
            return False

    return True


puzzle = [[""] * 10 for x in range(10)]

puzzle[1][1] = 1
puzzle[0][0] = 2
puzzle[1][0] = 3

assert is_valid_sudoku(puzzle) is True

puzzle[2][2] = 2
assert is_valid_sudoku(puzzle) is False

assert has_duplicates([1, "", 1]) is True
assert has_duplicates([1, "", 2]) is False

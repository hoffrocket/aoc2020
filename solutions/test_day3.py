from typing import List


def get_input() -> List[List[str]]:
    with open("inputs/day3input.txt", "r") as file:
        return [list(line.strip()) for line in file.readlines()]


def slope_counter(grid: List[List[str]], x_slope: int, y_slope: int) -> int:
    x = 0
    y = 0

    tree_count = 0
    while y < len(grid) - 1:
        x += x_slope
        y += y_slope
        row = grid[y]
        cell_value = row[x % len(row)]
        if cell_value == "#":
            tree_count += 1
    return tree_count


def test_day3_part1():
    grid = get_input()
    assert slope_counter(grid, 3, 1) == 265


def test_day3_part2():
    grid = get_input()
    tree_multiple = (
        slope_counter(grid, 1, 1)
        * slope_counter(grid, 3, 1)
        * slope_counter(grid, 5, 1)
        * slope_counter(grid, 7, 1)
        * slope_counter(grid, 1, 2)
    )
    assert tree_multiple == 3154761400

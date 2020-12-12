from typing import List


def get_input() -> List[int]:
    with open("inputs/day11input.txt", "r") as file:
        return file.read()


def part1(grid_str) -> int:
    grid = [list(row.strip()) for row in grid_str.strip().split()]
    was_flipped = True
    adjacent_index = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    round_count = 0
    print(adjacent_index)
    while was_flipped:
        was_flipped = False
        round_count += 1
        # print("old grid\n", "\n".join([str(row) for row in grid]))
        new_grid = [list(row) for row in grid]
        for row_index, row in enumerate(grid):
            for col_index, value in enumerate(row):
                if value != ".":
                    occ_count = 0
                    for xoff, yoff in adjacent_index:
                        adjrow = row_index + xoff
                        adjcol = col_index + yoff
                        if adjrow in range(0, len(grid)) and adjcol in range(0, len(row)):
                            if grid[adjrow][adjcol] == "#":
                                occ_count += 1
                    if value == "L" and occ_count == 0:
                        new_grid[row_index][col_index] = "#"
                        was_flipped = True
                    if value == "#" and occ_count >= 4:
                        new_grid[row_index][col_index] = "L"
                        was_flipped = True
        # print("new grid\n", "\n".join([str(row) for row in new_grid]))
        grid = new_grid
    return sum(row.count("#") for row in grid)


def test_day1_part1_ex():
    result = part1(
        """
        L.LL.LL.LL
        LLLLLLL.LL
        L.L.L..L..
        LLLL.LL.LL
        L.LL.LL.LL
        L.LLLLL.LL
        ..L.L.....
        LLLLLLLLLL
        L.LLLLLL.L
        L.LLLLL.LL
    """
    )
    assert result == 37


def test_day11_part1():
    result = part1(get_input())
    assert result == 2470


def part2(grid_str) -> int:
    grid = [list(row.strip()) for row in grid_str.strip().split()]
    was_flipped = True
    adjacent_index = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    round_count = 0
    print(adjacent_index)
    while was_flipped:
        was_flipped = False
        round_count += 1
        # print("old grid\n", "\n".join([str(row) for row in grid]))
        new_grid = [list(row) for row in grid]
        for row_index, row in enumerate(grid):
            for col_index, value in enumerate(row):
                if value != ".":
                    occ_count = 0
                    for xoff, yoff in adjacent_index:
                        adjrow = row_index + xoff
                        adjcol = col_index + yoff
                        while adjrow in range(0, len(grid)) and adjcol in range(0, len(row)):
                            adj_value = grid[adjrow][adjcol]
                            if adj_value == "#":
                                occ_count += 1
                                break
                            if adj_value == "L":
                                break
                            adjrow += xoff
                            adjcol += yoff
                    if value == "L" and occ_count == 0:
                        new_grid[row_index][col_index] = "#"
                        was_flipped = True
                    if value == "#" and occ_count >= 5:
                        new_grid[row_index][col_index] = "L"
                        was_flipped = True
        # print("new grid\n", "\n".join([str(row) for row in new_grid]))
        grid = new_grid
    return sum(row.count("#") for row in grid)


def test_day11_part2_ex():
    result = part2(
        """
        L.LL.LL.LL
        LLLLLLL.LL
        L.L.L..L..
        LLLL.LL.LL
        L.LL.LL.LL
        L.LLLLL.LL
        ..L.L.....
        LLLLLLLLLL
        L.LLLLLL.L
        L.LLLLL.LL
    """
    )
    assert result == 26


def test_day11_part2():
    result = part2(get_input())
    assert result == 2259

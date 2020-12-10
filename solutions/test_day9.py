import itertools
from typing import List


def get_input() -> List[int]:
    with open("inputs/day9input.txt", "r") as file:
        return [int(line.strip()) for line in file.readlines()]


def test_day9_part1():
    lines = get_input()

    def is_not_valid(index: int) -> bool:
        current = lines[index]
        return not any((i for i in range(index - 25, index) if current - lines[i] in itertools.islice(lines, i, index)))

    bad_index = next(index for index in range(25, len(lines)) if is_not_valid(index))

    print(f"found invalid on line {bad_index}: {lines[bad_index]}")

    assert bad_index == 564
    assert lines[bad_index] == 105950735


def test_day9_part2():
    lines = get_input()
    target = 105950735
    start_index = 0
    end_index = 0
    while start_index < len(lines) - 1:
        acc = lines[start_index]
        end_index = start_index + 1
        while end_index < len(lines) and acc < target:
            acc += lines[end_index]
            end_index += 1
        if acc == target:
            break
        start_index += 1
    window = lines[start_index:end_index]
    end_sum = min(window) + max(window)
    print(window)
    assert sum(window) == target
    assert start_index == 448
    assert end_index == 465
    assert end_sum == 13826915

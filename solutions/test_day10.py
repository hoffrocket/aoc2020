from typing import List


def get_input() -> List[int]:
    with open("inputs/day10input.txt", "r") as file:
        return [int(line.strip()) for line in file.readlines()]


def test_day10_part1():
    lines = get_input()
    assert len(lines) == len(set(lines))  # adapters are unique
    lines.append(0)
    lines.sort()
    max_joltage = lines[-1] + 3
    lines.append(max_joltage)
    assert max_joltage == 171
    diffs = [lines[index + 1] - jolt for index, jolt in enumerate(lines[0 : len(lines) - 1])]
    assert set(diffs) == {1, 3}
    one_count = diffs.count(1)
    assert one_count == 69
    three_count = diffs.count(3)
    assert three_count == 34
    assert one_count * three_count == 2346


def get_path_count(lines: List[int]) -> int:
    lines.append(0)
    lines.sort()
    lines.append(lines[-1] + 3)
    print(lines)

    item_count = len(lines)
    cache = [0] * item_count

    def option_count(index: int) -> int:
        if index == item_count - 1:
            return 1
        cached_val = cache[index]
        if cache[index]:
            return cached_val
        jolt = lines[index]
        path_indexes = [i for i in range(index + 1, min(index + 4, len(lines))) if lines[i] - jolt <= 3]

        result = sum(option_count(i) for i in path_indexes)
        cache[index] = result
        return result

    return option_count(0)


def test_day10_part2_ex1():
    lines = [
        16,
        10,
        15,
        5,
        1,
        11,
        7,
        19,
        6,
        12,
        4,
    ]
    assert get_path_count(lines) == 8


def test_day10_part2_ex2():
    lines = [
        28,
        33,
        18,
        42,
        31,
        14,
        46,
        20,
        48,
        47,
        24,
        23,
        49,
        45,
        19,
        38,
        39,
        11,
        1,
        32,
        25,
        35,
        8,
        17,
        7,
        9,
        4,
        2,
        34,
        10,
        3,
    ]
    assert get_path_count(lines) == 19208


def test_day10_part2():
    assert get_path_count(get_input()) == 6044831973376

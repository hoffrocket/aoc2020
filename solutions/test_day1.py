from typing import Set


def find_sum_return_product(sum_to_find: int, count: int, integers: Set[int], product: int = 1) -> int:
    if count <= 1:
        if sum_to_find in integers:
            return product * sum_to_find
    else:
        for i in integers:
            result = find_sum_return_product(sum_to_find - i, count - 1, integers, product * i)
            if result:
                return result
    return 0


def get_input() -> Set[int]:
    with open("inputs/day1input.txt", "r") as file:
        return set([int(i) for i in file.readlines()])


def test_day1_part1():
    lines = get_input()
    sum_to_find = 2020
    for i in lines:
        remainder = sum_to_find - i
        if remainder in lines:
            product = i * remainder
            assert product == 538464


def test_day1_part2():
    lines = get_input()
    sum_to_find = 2020
    for first in lines:
        remainder = sum_to_find - first
        for second in lines:
            third = remainder - second
            if third in lines:
                assert first + second + third == sum_to_find
                product = first * second * third
                assert product == 278783190


def test_day1_part1_recurse():
    assert find_sum_return_product(2020, 2, get_input()) == 538464


def test_day1_part2_recurse():
    assert find_sum_return_product(2020, 3, get_input()) == 278783190

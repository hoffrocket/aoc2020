"""
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

"""
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

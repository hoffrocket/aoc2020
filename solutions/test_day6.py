from typing import List


def get_input() -> List[str]:
    with open("inputs/day6input.txt", "r") as file:
        return [line.strip() for line in file.read().strip().split("\n\n")]


def test_day6_part1():
    lines = get_input()
    result = sum([len(set(line.replace("\n", ""))) for line in lines])
    assert result == 6437


def test_day6_part2():
    lines = get_input()
    result = sum([len(set.intersection(*[set(person) for person in line.split("\n")])) for line in lines])
    assert result == 3229

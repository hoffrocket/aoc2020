from collections import namedtuple
from typing import List

Password = namedtuple("Password", "min max letter password")


def get_input() -> List[Password]:
    passwords = []
    with open("inputs/day2input.txt", "r") as file:
        for line in file.readlines():
            space_parts = line.split(" ")
            range_parts = space_parts[0].split("-")
            letter = space_parts[1][0]
            password = space_parts[2].strip()
            passwords.append(Password(int(range_parts[0]), int(range_parts[1]), letter, password))
    return passwords


def test_day2_part1():
    assert len([p for p in get_input() if p.password.count(p.letter) in range(p.min, p.max + 1)]) == 517


def test_day2_part2():
    assert (
        len([p for p in get_input() if (p.password[p.min - 1] == p.letter) != (p.password[p.max - 1] == p.letter)])
        == 284
    )

from typing import List


def get_input() -> str:
    with open("inputs/day12input.txt", "r") as file:
        return file.read()


def part1(dir_str) -> int:
    lines = [dir.strip() for dir in dir_str.strip().split()]
    start_x = 0
    start_y = 0

    dirs = ["E", "S", "W", "N"]
    start_dir = 0

    def turn(dir: int, inst: str, value: int):
        assert value % 90 == 0
        turns = int(value / 90)
        direction = 1 if inst == "R" else -1
        dir = (dir + turns * direction) % 4
        return dir

    def move_dir(x: int, y: int, inst: str, value: int):
        if inst == "N":
            y += value
        elif inst == "S":
            y -= value
        elif inst == "E":
            x += value
        elif inst == "W":
            x -= value
        return x, y

    for line in lines:
        print(start_x, start_y)
        inst = line[0]
        value = int(line[1:])
        if inst == "L":
            start_dir = turn(start_dir, inst, value)
        elif inst == "R":
            start_dir = turn(start_dir, inst, value)
        elif inst == "F":
            start_x, start_y = move_dir(start_x, start_y, dirs[start_dir], value)
        else:
            start_x, start_y = move_dir(start_x, start_y, inst, value)

    return abs(start_x) + abs(start_y)


def test_day1_part1_ex():
    result = part1(
        """
    F10
    N3
    F7
    R90
    F11
    """
    )
    assert result == 25


def test_day12_part1():
    result = part1(get_input())
    assert result == 2458


def part2(dir_str) -> int:
    lines = [dir.strip() for dir in dir_str.strip().split()]
    start_x = 0
    start_y = 0
    way_x = 10
    way_y = 1

    def turn(x: int, y: int, inst: str, value: int):
        assert value % 90 == 0
        turns = int(value / 90)
        direction = 1 if inst == "R" else -1
        rotations = (turns * direction) % 4
        if rotations == 0:
            return x, y
        elif rotations == 1:
            return y, -x
        elif rotations == 2:
            return -x, -y
        elif rotations == 3:
            return -y, x

    def move_dir(x: int, y: int, inst: str, value: int):
        if inst == "N":
            y += value
        elif inst == "S":
            y -= value
        elif inst == "E":
            x += value
        elif inst == "W":
            x -= value
        return x, y

    for line in lines:
        print(line, start_x, start_y, way_x, way_y)
        inst = line[0]
        value = int(line[1:])
        if inst == "L":
            way_x, way_y = turn(way_x, way_y, inst, value)
        elif inst == "R":
            way_x, way_y = turn(way_x, way_y, inst, value)
        elif inst == "F":
            start_x, start_y = (start_x + way_x * value, start_y + way_y * value)
        else:
            way_x, way_y = move_dir(way_x, way_y, inst, value)
        print(line, start_x, start_y, way_x, way_y)
    return abs(start_x) + abs(start_y)


def test_day12_part2_ex():
    result = part2(
        """
    F10
    N3
    F7
    R90
    F11
    """
    )
    assert result == 286


def test_day12_part2():
    result = part2(get_input())
    assert result == 145117

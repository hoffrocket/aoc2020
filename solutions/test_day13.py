def get_input() -> str:
    with open("inputs/day13input.txt", "r") as file:
        return file.read()


def part1(dir_str) -> int:
    start_time_str, bus_str = dir_str.strip().split()
    start_time = int(start_time_str)
    buses = [int(bus) for bus in bus_str.split(",") if bus != "x"]
    buses_rem = [
        (
            bus,
            bus - start_time % bus,
        )
        for bus in buses
    ]
    min_wait_bus, wait_time = min(buses_rem, key=lambda p: p[1])

    return min_wait_bus * wait_time


def test_day1_part1_ex():
    result = part1(
        """
    939
    7,13,x,x,59,x,31,19
    """
    )
    assert result == 295


def test_day13_part1():
    result = part1(get_input())
    assert result == 6559


def part2(dir_str) -> int:
    """
    Brute force solution. Not working for the input, but works for examples
    """
    buses = list(enumerate(int(bus) for bus in dir_str.strip().split()[1].replace("x", "1").split(",")))
    bus_indexes = [bus_index for bus_index in buses if bus_index[1] != 1]
    first_bus = buses[0][1]

    def check_times(st: int):
        for index, bus in bus_indexes:
            is_zeroth = index == 0 and st % bus == 0
            if not is_zeroth and (bus - st % bus) != index:
                return False
        return True

    start_time = next(st for st in range(0, 10000000, first_bus) if check_times(st))

    return start_time


def test_day13_part2_ex():
    result = part2(
        """
    939
    7,13,x,x,59,x,31,19
    """
    )
    assert result == 1068781


def part2_a(dir_str) -> int:
    """
    Optimized solution
    Note that I copied this solution directly out of a reddit thread. No way I was figuring this out myself :-/
    Apparently based on https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    """
    buses = [int(bus) for bus in dir_str.strip().split()[1].replace("x", "0").split(",")]
    timestamp = 0
    step = buses[0]
    for index, bus in filter(lambda x: x[1] != 0, enumerate(buses[1:], start=1)):
        while (timestamp + index) % bus != 0:
            timestamp += step
        step *= bus
    return timestamp


def test_day13_part2():
    result = part2_a(get_input())
    assert result == 626670513163231

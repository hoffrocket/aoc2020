import itertools
from typing import Dict, List, Tuple


def get_input() -> str:
    with open("inputs/day14input.txt", "r") as file:
        return file.read()


def part1(mem_str) -> int:
    instructions: List[Tuple[str, str]] = [
        (
            inst[0],
            inst[1],
        )
        for inst in [line.strip().split(" = ") for line in mem_str.strip().split("\n")]
    ]
    memory: Dict[int, int] = {}
    or_mask = 1
    and_mask = 0
    for command, value in instructions:
        if command == "mask":
            # print(value)
            or_mask = int(value.replace("X", "0"), base=2)
            and_mask = int(value.replace("X", "1"), base=2)
        else:
            location = int(command[4:-1])
            value_int = int(value)
            masked_value = or_mask | value_int & and_mask
            # print(bin(value_int), bin(masked_value), masked_value)
            memory[location] = masked_value

    return sum(memory.values())


def test_day1_part1_ex():
    result = part1(
        """
    mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
    mem[8] = 11
    mem[7] = 101
    mem[8] = 0
    """
    )
    assert result == 165


def test_day14_part1():
    result = part1(get_input())
    assert result == 7817357407588


def part2(mem_str) -> int:
    instructions: List[Tuple[str, str]] = [
        (
            inst[0],
            inst[1],
        )
        for inst in [line.strip().split(" = ") for line in mem_str.strip().split("\n")]
    ]
    memory: Dict[int, int] = {}
    current_mask = ""
    for command, value in instructions:
        if command == "mask":
            current_mask = value
        else:
            location = int(command[4:-1])
            value_int = int(value)
            location_bin = bin(location)[2:]
            floating_bits = [index for index, char in enumerate(current_mask) if char == "X"]
            overwrite_bits = [index for index, char in enumerate(current_mask) if char == "1"]
            # print(floating_bits, overwrite_bits)

            value_buf = ["0"] * (len(current_mask) - len(location_bin)) + list(location_bin)
            for offset in overwrite_bits:
                value_buf[offset] = "1"

            for options in itertools.product(range(2), repeat=len(floating_bits)):
                for index, offset in enumerate(floating_bits):
                    value_buf[offset] = str(options[index])
                new_value_bin = "".join(value_buf)
                new_value_int = int(new_value_bin, base=2)
                # print(value, location_bin, new_value_bin, new_value_int)
                memory[new_value_int] = value_int

    return sum(memory.values())


def test_day14_part2_ex():
    result = part2(
        """
    mask = 000000000000000000000000000000X1001X
    mem[42] = 100
    mask = 00000000000000000000000000000000X0XX
    mem[26] = 1
    """
    )
    assert result == 208


def test_day14_part2():
    result = part2(get_input())
    assert result == 4335927555692

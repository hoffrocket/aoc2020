from typing import Dict, List, Set, Tuple


def get_input() -> List[str]:
    with open("inputs/day8input.txt", "r") as file:
        return [line.strip() for line in file.readlines()]


def test_day8_part1():
    lines = get_input()
    seen_lines = set()
    accumulator = 0
    line_pointer = 0
    while line_pointer < len(lines):
        if line_pointer in seen_lines:
            print(f"infinite loop. already seen {line_pointer}. acc {accumulator}")
            break
        seen_lines.add(line_pointer)
        inst, value_str = lines[line_pointer].split(" ")
        value = int(value_str)
        if inst == "acc":
            accumulator += value
            line_pointer += 1
        elif inst == "jmp":
            line_pointer += value
        elif inst == "nop":
            line_pointer += 1
        else:
            raise Exception(f"Invalid instruction: {inst} at {line_pointer}")
    assert accumulator == 1420


def test_day8_part2():
    lines = get_input()
    lines_with_jmp = [index for index, line in enumerate(lines) if "jmp" in line]
    accumulator = 0
    for jmp_index in lines_with_jmp:
        accumulator = 0
        line_pointer = 0
        seen_lines = set()
        while line_pointer < len(lines):
            if line_pointer in seen_lines:
                # print(f"infinite loop. already seen {line_pointer}. acc {accumulator}")
                break
            seen_lines.add(line_pointer)
            inst, value_str = lines[line_pointer].split(" ")
            value = int(value_str)
            if inst == "acc":
                accumulator += value
                line_pointer += 1
            elif inst == "jmp":
                if line_pointer == jmp_index:
                    print(f"converting jmp at {line_pointer} to nop")
                    line_pointer += 1
                else:
                    line_pointer += value
            elif inst == "nop":
                line_pointer += 1
            else:
                raise Exception(f"Invalid instruction: {inst} at {line_pointer}")
        if line_pointer == len(lines):
            print(f"Got to end with jmp_index {jmp_index} line_counter {line_pointer} and acc {accumulator}")
            break

    assert accumulator == 1245

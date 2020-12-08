from typing import List


def get_input() -> List[str]:
    with open("inputs/day5input.txt", "r") as file:
        return [line.strip() for line in file.readlines()]


def test_day5_part1():
    seats = get_input()
    max_seat_id = 0
    for line in seats:
        seat_id = int(line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2)
        max_seat_id = max(max_seat_id, seat_id)
    assert max_seat_id == 848


def test_day5_part2():
    seats = get_input()
    max_seat_id = 0
    seat_id_array = [0] * 1024
    for line in seats:
        seat_id = int(line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2)
        max_seat_id = max(max_seat_id, seat_id)
        seat_id_array[seat_id] = 1
    max_not_present_id = 0
    for seat_id, is_present in enumerate(seat_id_array):
        if not is_present and seat_id < max_seat_id:
            max_not_present_id = max(max_not_present_id, seat_id)

    assert max_not_present_id == 682

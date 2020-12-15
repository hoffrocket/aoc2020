from collections import defaultdict, deque
from typing import Deque, Dict


def solution(mem_str, num_turns=2020) -> int:
    nums = [int(n) for n in mem_str.split(",")]
    spoke_dict: Dict[int, Deque[int]] = defaultdict(lambda: deque(maxlen=2))
    for turn, num in enumerate(nums, start=1):
        spoke_dict[num].append(turn)
    prior_turns = spoke_dict[nums[-1]]
    for turn in range(len(nums) + 1, num_turns + 1):
        new_num = 0
        if len(prior_turns) > 1:
            new_num = prior_turns[-1] - prior_turns[-2]
        prior_turns = spoke_dict[new_num]
        prior_turns.append(turn)
        last_num = new_num
    print(spoke_dict)
    return last_num


def test_day14_part1_ex():
    assert solution("0,3,6") == 436
    assert solution("2,3,1") == 78
    assert solution("3,1,2") == 1836


def test_day14_part1():
    result = solution("14,8,16,0,1,17")
    assert result == 240


def test_day14_part2():
    result = solution("14,8,16,0,1,17", 30000000)
    assert result == 505

from typing import Dict, List, Set, Tuple


def get_input() -> List[str]:
    with open("inputs/day7input.txt", "r") as file:
        return [line.strip() for line in file.readlines()]


def get_rules() -> Dict[str, List[Tuple[int, str]]]:
    lines = get_input()
    return {
        " ".join(line.split(" ")[0:2]): [
            (
                int(content.split(" ")[0]),
                " ".join(content.split(" ")[1:3]),
            )
            for content in line.split(" contain ")[1].replace(".", "").split(", ")
            if not content.startswith("no")
        ]
        for line in lines
    }


def test_day7_part1():
    rules = get_rules()

    def find_deps(dep_name: str, all_roots: Set[str]) -> Set[str]:
        new_roots = (
            set([bag_name for bag_name, contents in rules.items() if dep_name in [p[1] for p in contents]]) - all_roots
        )
        for root in new_roots:
            all_roots.add(root)
        for root in new_roots:
            find_deps(root, all_roots)
        return all_roots

    deps = find_deps("shiny gold", set())
    print(deps)
    assert len(deps) == 355


def test_day7_part2():
    rules = get_rules()

    def count_deps(dep_name: str) -> int:
        deps = rules.get(dep_name)
        total_count = 0
        if deps:
            for count, bag_name in deps:
                total_count += count + (count * count_deps(bag_name))
        return total_count

    count = count_deps("shiny gold")
    assert count == 5312

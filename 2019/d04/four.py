def numbers():
    yield from range(109165, 576723)


def different_passwords():
    for number in numbers():
        yield from match_criterias(str(number))


def match_criterias(number):
    reversed_number = number[::-1]

    never_decrease = all(
        elem >= reversed_number[ind + 1]
        for ind, elem in enumerate(reversed_number, 0)
        if ind + 1 < len(reversed_number)
    )

    two_adjacent_digts_are_the_same = any(
        elem == reversed_number[ind + 1]
        for ind, elem in enumerate(reversed_number, 0)
        if ind + 1 < len(reversed_number)
    )

    if never_decrease and two_adjacent_digts_are_the_same:
        yield number


def match_criteria(number):
    return bool(next((pwd for pwd in match_criterias(number)), False))


if __name__ == "__main__":
    print("Day 4 exercise...")

    print(sum(1 for _ in different_passwords()))

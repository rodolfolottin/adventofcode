def possible_passwords():
    for number in range(109165, 576723):
        yield match_criterias(number)


def match_criterias(number):
    reversed_number = str(number)[::-1]

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

    return never_decrease and two_adjacent_digts_are_the_same


if __name__ == "__main__":
    print("Day 4 exercise...")

    print(sum(1 for _ in possible_passwords()))

def possible_passwords(match_criteria_func):
    for number in range(109165, 576723):
        if match_criteria_func(number):
            yield number


def never_decrease(reversed_number):
    return all(
        elem >= reversed_number[ind + 1]
        for ind, elem in enumerate(reversed_number, 0)
        if ind + 1 < len(reversed_number)
    )


def has_doubles(reversed_number):
    return any(
        elem == reversed_number[ind + 1]
        for ind, elem in enumerate(reversed_number, 0)
        if ind + 1 < len(reversed_number)
    )


def match_criterias(number):
    reversed_number = str(number)[::-1]
    return never_decrease(reversed_number) and has_doubles(reversed_number)


def has_strict_doubles(reversed_number):
    return any(num for num in reversed_number if list(reversed_number).count(num) == 2)


def match_criterias_part_2(number):
    reversed_number = str(number)[::-1]
    return never_decrease(reversed_number) and has_strict_doubles(reversed_number)


if __name__ == "__main__":
    print("Day 4 exercise...")

    print(sum(1 for _ in possible_passwords(match_criterias)))
    print(sum(1 for _ in possible_passwords(match_criterias_part_2)))

def fully_contains(assignment_one, assignment_two):
    if assignment_two[0] >= assignment_one[0] \
            and assignment_two[1] <= assignment_one[1]:
        return True
    else:
        return False


if __name__ == "__main__":
    with open('inputs/puzzle_1.txt') as f:
        lines = f.readlines()

    counter = 0

    for line in lines:
        line = line.replace("\n", '')

        assignments = line.split(',')

        assignment_one_lower = int(assignments[0].split('-')[0])
        assignment_one_upper = int(assignments[0].split('-')[1])

        assignment_two_lower = int(assignments[1].split('-')[0])
        assignment_two_upper = int(assignments[1].split('-')[1])

        if fully_contains([assignment_one_lower, assignment_one_upper], [assignment_two_lower, assignment_two_upper]) \
                or fully_contains([assignment_two_lower, assignment_two_upper],
                                  [assignment_one_lower, assignment_one_upper]):
            counter += 1

    print(counter)

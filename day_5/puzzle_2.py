def get_stacks(lines):
    global stacks

    for line in lines:

        line = line.replace("\n", '')

        if line == " 1   2   3   4   5   6   7   8   9":
            return stacks

        split_points = [i for i in range(0, len(line), 4)]

        crates = [line[ind:ind + 4].replace(" ", "").replace("[", "").replace("]", "") for ind in split_points]

        for i in range(0, len(crates)):
            if crates[i] != '':
                stacks[i].append(crates[i])


def do_move(move):
    global stacks

    split_move = move.split(" ")
    number_to_move, start, end = [split_move[i] for i in [1, 3, 5]]

    num_moved = 0

    for i in range(0, int(number_to_move)):
        crate = stacks[int(start)-1].pop(0)
        stacks[int(end)-1].insert(num_moved, crate)
        num_moved += 1


if __name__ == "__main__":
    with open('inputs/puzzle_1.txt') as f:
        lines = f.readlines()

    first_move = 10
    stacks = [[] for i in range(0, 9)]

    get_stacks(lines)

    for i in range(first_move, len(lines)):
        do_move(lines[i].replace("\n", ''))

    print(''.join([stacks[i][0] for i in range(0, 9)]))

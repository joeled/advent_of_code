cavern = [['.' for col in range(0, 9)] for row in range(0, 5)]
cavern[4] = ['#' for col in range(0, 9)]
for row in range(0, 5):
    cavern[row][0] = '#'
    cavern[row][8] = '#'

shapes = [
    [['#', '#', '#', '#']],
    [['.', '#', '.'], ['#', '#', '#'], ['.', '#', '.']],
    [['.', '.', '#'], ['.', '.', '#'], ['#', '#', '#']],
    [['#'], ['#'], ['#'], ['#']],
    [['#', '#'], ['#', '#']]
]
downward_contact_points = [
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[1, 0], [2, 1], [1, 2]],
    [[2, 0], [2, 1], [2, 2]],
    [[3, 0]],
    [[1, 0], [1, 1]]
]
left_contact_points = [
    [[0, 0]],
    [[0, 1], [1, 0], [2, 1]],
    [[0, 2], [1, 2], [2, 0]],
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    [[0, 0], [1, 0]]
]
right_contact_points = [
    [[0, 3]],
    [[0, 1], [1, 2], [2, 1]],
    [[0, 2], [1, 2], [2, 2]],
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    [[0, 1], [1, 1]]
]
jet_count = 0
curr_highest = len(cavern)
heights = []
clipped_height = 0


def clip_cavern(rock, top_left):
    global clipped_height, cavern

    rock_height = len(shapes[rock % 5])

    for row in range(top_left[0], top_left[0] + rock_height):
        if cavern[row] == ['#', '#', '#', '#', '#', '#', '#', '#', '#']:
            clipped_height += len(cavern) - row - 1
            cavern = cavern[0:row + 1]
            break


def grow_cavern(next_rock):
    global curr_highest

    new_rock_height = len(shapes[next_rock % 5])
    if curr_highest < 3 + new_rock_height:
        while curr_highest < 3 + new_rock_height:
            cavern.insert(0, ['#', '.', '.', '.', '.', '.', '.', '.', '#'])
            curr_highest += 1
    elif curr_highest > 3 + new_rock_height:
        while curr_highest > 3 + new_rock_height:
            cavern.pop(0)
            curr_highest -= 1


def erase_fallen_rock(top_left, curr_rock):
    shape = shapes[curr_rock % 5]
    for row in range(0, len(shape)):
        for col in range(0, len(shape[row])):
            if shape[row][col] == '#':
                cavern[row + top_left[0]][col + top_left[1]] = '.'


def draw_fallen_rock(top_left, curr_rock):
    shape = shapes[curr_rock % 5]
    for row in range(0, len(shape)):
        for col in range(0, len(shape[row])):
            if shape[row][col] == '#':
                cavern[row + top_left[0]][col + top_left[1]] = '#'


def push_gas(top_left, curr_rock, jet):
    global jet_count

    if jet == '<' and not touching(top_left, left_contact_points[curr_rock % 5], 0, -1):
        top_left[1] -= 1
    elif jet == '>' and not touching(top_left, right_contact_points[curr_rock % 5], 0, 1):
        top_left[1] += 1

    jet_count += 1

    return top_left


def touching(top_left, contact_points, row_modifier, col_modifier):
    for contact_point in contact_points:
        if cavern[contact_point[0] + top_left[0] + row_modifier][contact_point[1] + top_left[1] + col_modifier] == '#':
            return True

    return False


def drop_rock(curr_rock, jets):
    global jet_count, curr_highest

    top_left = [0, 3]

    while True:
        top_left = push_gas(top_left, curr_rock, jets[jet_count % len(jets)])

        if not touching(top_left, downward_contact_points[curr_rock % 5], 1, 0):
            top_left[0] += 1
        else:
            break

    draw_fallen_rock(top_left, curr_rock)
    curr_highest = min(curr_highest, top_left[0])

    return top_left


def run_simulation(jets):
    rock = 0
    while rock < 1000000000000:
        top_left = drop_rock(rock, jets)
        clip_cavern(rock, top_left)
        grow_cavern(rock + 1)

        rock += 1

        if rock % 100000 == 0:
            print(rock)

    print(len(cavern) + clipped_height - curr_highest - 1)


def process_input():
    global heights

    with open('inputs/puzzle_1.txt') as f:
        lines = f.readlines()

    with open('inputs/heights.txt') as f:
        heights = f.readlines()

    jets = lines[0].replace('\n', '')

    run_simulation(jets)


if __name__ == "__main__":
    process_input()

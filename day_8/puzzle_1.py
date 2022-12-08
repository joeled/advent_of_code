max_top = []
max_left = []
max_right = []
max_bottom = []
trees = []


def process_input():
    with open('inputs/puzzle_1.txt') as f:
        lines = f.readlines()

    for line in lines:
        line = line.replace("\n", "")

        trees.append([int(c) for c in line])
        max_top.append([0 for c in line])
        max_left.append([0 for c in line])
        max_right.append([0 for c in line])
        max_bottom.append([0 for c in line])

    pass


def process_top_left():
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[0]) - 1):
            max_top[i][j] = max(max_top[i - 1][j], trees[i - 1][j])
            max_left[i][j] = max(max_left[i][j - 1], trees[i][j - 1])


def process_right_bottom():
    for i in range(len(trees) - 2, 0, -1):
        for j in range(len(trees[0]) - 2, 0, -1):
            max_bottom[i][j] = max(max_bottom[i + 1][j], trees[i + 1][j])
            max_right[i][j] = max(max_right[i][j + 1], trees[i][j + 1])


def count_visible_interior():
    num_visible = 0

    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[0]) - 1):
            # print(str(i) + " " + str(j))
            if trees[i][j] > max_top[i][j] \
                    or trees[i][j] > max_left[i][j] \
                    or trees[i][j] > max_bottom[i][j] \
                    or trees[i][j] > max_right[i][j]:
                num_visible += 1

    return num_visible


if __name__ == "__main__":
    process_input()
    process_top_left()
    process_right_bottom()

    visible = count_visible_interior()
    print(visible + (len(trees)*2) + (len(trees[0])*2) - 4)

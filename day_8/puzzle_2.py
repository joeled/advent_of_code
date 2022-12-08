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


def calculate_score(i, j):
    top_score = 1
    left_score = 1
    right_score = 1
    bottom_score = 1

    if max_top[i][j] < trees[i][j]:
        top_score = i
    else:
        temp_i = i - 1
        while temp_i >= 0 and trees[temp_i][j] < trees[i][j]:
            top_score += 1
            temp_i -= 1

    if max_left[i][j] < trees[i][j]:
        left_score = j
    else:
        temp_j = j - 1
        while temp_j >= 0 and trees[i][temp_j] < trees[i][j]:
            left_score += 1
            temp_j -= 1

    if max_right[i][j] < trees[i][j]:
        right_score = len(trees[0]) - j - 1
    else:
        temp_j = j - 1
        while temp_j <= len(trees[0]) - 1 and trees[i][temp_j] < trees[i][j]:
            right_score += 1
            temp_j += 1

    if max_bottom[i][j] < trees[i][j]:
        bottom_score = len(trees) - i - 1
    else:
        temp_i = i + 1
        while temp_i <= len(trees) - 1 and trees[temp_i][j] < trees[i][j]:
            bottom_score += 1
            temp_i += 1

    score = top_score * left_score * right_score * bottom_score

    return score


def get_highest_score():
    highest_score = 0

    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[0]) - 1):
            score = calculate_score(i, j)
            highest_score = max(highest_score, score)

    return highest_score


if __name__ == "__main__":
    process_input()
    process_top_left()
    process_right_bottom()

    answer = get_highest_score()
    print(answer)

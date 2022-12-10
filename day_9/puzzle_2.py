t_pos = [[0, 0] for i in range(0, 10)]
t_visited = set(["0_0"])


# h_pos[0] = row
# h_pos[1] = col

def touching(idx):
    if abs(t_pos[idx - 1][0] - t_pos[idx][0]) <= 1 and abs(t_pos[idx-1][1] - t_pos[idx][1]) <= 1:
        return True
    else:
        return False


def readjust_tail():
    for idx in range(1, 10):
        if not touching(idx):
            # adjust col
            if t_pos[idx][1] < t_pos[idx - 1][1]:
                t_pos[idx][1] = t_pos[idx][1] + 1
            elif t_pos[idx][1] > t_pos[idx - 1][1]:
                t_pos[idx][1] = t_pos[idx][1] - 1

            # adjust row
            if t_pos[idx][0] < t_pos[idx - 1][0]:
                t_pos[idx][0] = t_pos[idx][0] + 1
            elif t_pos[idx][0] > t_pos[idx - 1][0]:
                t_pos[idx][0] = t_pos[idx][0] - 1


def process_move(move_dir):
    if move_dir == "D":
        t_pos[0][0] = t_pos[0][0] - 1
    elif move_dir == "U":
        t_pos[0][0] = t_pos[0][0] + 1
    elif move_dir == "R":
        t_pos[0][1] = t_pos[0][1] + 1
    elif move_dir == "L":
        t_pos[0][1] = t_pos[0][1] - 1

    readjust_tail()


def process_moves(move_info):
    move_dir = move_info[0]
    num = int(move_info[1])

    for i in range(0, num):
        process_move(move_dir)
        t_visited.add(str(t_pos[9][0]) + "_" + str(t_pos[9][1]))


def process_input():
    with open('inputs/puzzle_1.txt') as f:
        lines = f.readlines()

    for line in lines:
        line = line.replace("\n", "")

        process_moves(line.split(" "))


if __name__ == "__main__":
    process_input()

    print(len(t_visited))

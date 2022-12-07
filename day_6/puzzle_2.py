import time

i, j = 0, 13
line = ''
currWindow = {}


def init_window():
    for itr in range(0, 14):
        currWindow.update({line[itr]: currWindow.get(line[itr], 0) + 1})


def move_pointers():
    global i, j

    currWindow.update({line[i]: currWindow.get(line[i], 0) - 1})
    if currWindow.get(line[i]) == 0:
        currWindow.pop(line[i])
    i += 1

    j += 1
    currWindow.update({line[j]: currWindow.get(line[j], 0) + 1})


if __name__ == "__main__":
    t0 = time.time()

    with open('inputs/puzzle_1.txt') as f:
        line = f.readline()

    init_window()

    while j < len(line):
        if len(currWindow.keys()) == 14:
            print(j + 1)
            break
        else:
            move_pointers()

    t1 = time.time()

    print(str((t1-t0)*1000) + "ms")
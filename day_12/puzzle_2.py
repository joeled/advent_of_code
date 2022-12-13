grid = []
possible_starts = []
end = []
visited = set()


def can_move(element, new_element):
    return grid[new_element[0]][new_element[1]] - grid[element[0]][element[1]] <= 1


def in_bounds(element):
    return len(grid) > element[0] >= 0 and len(grid[0]) > element[1] >= 0


def add_neighbors_to_queue(element, queue):
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for dir in dirs:
        new_element = [element[0] + dir[0], element[1] + dir[1]]
        if in_bounds(new_element) and can_move(element, new_element) \
                and str(new_element[0]) + " " + str(new_element[1]) not in visited \
                and new_element not in queue:
            queue.append(new_element)

    return queue


def bfs(possible_start):
    global visited

    visited = set()
    queue = [possible_start]

    iteration = 0
    while len(queue) > 0:
        queue_size = len(queue)
        # print("Iteration: " + str(iteration) + " Queue size: " + str(queue_size))
        for idx in range(0, queue_size):
            element = queue.pop(0)
            visited.add(str(element[0]) + " " + str(element[1]))
            if element[0] == end[0] and element[1] == end[1]:
                return iteration
            else:
                add_neighbors_to_queue(element, queue)
        iteration += 1

    return 10000


def parse_square(row, col, square):
    global start, end
    if square == 'S' or square == 'a':
        possible_starts.append([row, col])
        return ord('a')
    elif square == 'E':
        end = [row, col]
        return ord('z')
    else:
        return ord(square)


def process_input():
    with open('inputs/puzzle_1.txt') as f:
        lines = f.readlines()

    for row in range(0, len(lines)):
        line = lines[row]
        line = line.replace("\n", "")
        grid.append([parse_square(row, col, square) for col, square in enumerate(line)])

    min_path = 10000

    for possible_start in possible_starts:
        path = bfs(possible_start)
        min_path = min(min_path, path)

    print(min_path)


if __name__ == "__main__":
    process_input()

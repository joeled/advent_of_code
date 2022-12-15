visited = set()


def add_neighbors_to_queue(element, queue):
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for dir in dirs:
        new_element = [element[0] + dir[0], element[1] + dir[1]]
        if str(new_element[0]) + " " + str(new_element[1]) not in visited \
                and new_element not in queue:
            queue.append(new_element)

    return queue


def mark_impossible_locations(grid, pair, grid_radius):
    global visited

    queue = [pair[0]]
    visited = set()
    beacon = pair[1]
    found_beacon = False

    while len(queue) > 0:

        if found_beacon:
            break

        queue_size = len(queue)
        for idx in range(0, queue_size):
            element = queue.pop(0)
            visited.add(str(element[0]) + " " + str(element[1]))
            add_neighbors_to_queue(element, queue)

            if element[0] == beacon[0] and element[1] == beacon[1]:
                found_beacon = True
            elif grid[element[0] + grid_radius-1][element[1] + grid_radius+1] == '.':
                grid[element[0] + grid_radius-1][element[1] + grid_radius+1] = '#'


def process_input():
    with open('inputs/puzzle_1.txt') as f:
        lines = f.readlines()

    grid_radius = 100000

    grid = [['.' for col in range(-grid_radius, grid_radius)] for row in range(-grid_radius, grid_radius)]

    sensor_beacon_pairs = []

    for line in lines:
        line = line.replace('\n', '')
        split_line = line.split(":")

        sensor = [int(split_line[0].split("=")[2]), int(split_line[0].split("=")[1].split(",")[0])]
        beacon = [int(split_line[1].split("=")[2]), int(split_line[1].split("=")[1].split(",")[0])]

        sensor_beacon_pairs.append([sensor, beacon])

        grid[sensor[0] + grid_radius][sensor[1] + grid_radius] = 'S'
        grid[beacon[0] + grid_radius][beacon[1] + grid_radius] = 'B'

    # for pair in sensor_beacon_pairs:
    for pair in sensor_beacon_pairs:
        mark_impossible_locations(grid, pair, grid_radius)
        print('finished a bfs')

    print(grid[2000000+grid_radius-1].count('#'))


if __name__ == "__main__":
    process_input()

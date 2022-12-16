from interval import interval


def manhattan_distance(vertex_one, vertex_two):
    return abs(vertex_one[0] - vertex_two[0]) + abs(vertex_one[1] - vertex_two[1])


def process_input():
    with open('inputs/puzzle_1.txt') as f:
        lines = f.readlines()

    rows = {}
    min_val = 0
    max_val = 4000000

    sensors = []
    beacons = []

    line_idx = 1
    for line in lines:
        print("Processing line: " + str(line_idx))
        line_idx += 1
        line = line.replace('\n', '')
        split_line = line.split(":")

        sensor = [int(split_line[0].split("=")[2]), int(split_line[0].split("=")[1].split(",")[0])]
        beacon = [int(split_line[1].split("=")[2]), int(split_line[1].split("=")[1].split(",")[0])]

        if sensor not in sensors:
            sensors.append(sensor)
        if beacon not in beacons:
            beacons.append(beacon)

        distance = manhattan_distance(sensor, beacon)

        for row in range(sensor[0] - distance, sensor[0] + distance + 1):
            if min_val <= row <= max_val:
                curr_interval = rows.get(row, interval())
                if len(curr_interval) == min_val or curr_interval[0].inf != 0 or curr_interval[0].sup != max_val:
                    interval_radius = distance - (abs(sensor[0] - row))
                    inf = max(min_val, sensor[1] - interval_radius)
                    sup = min(max_val, sensor[1] + interval_radius)
                    curr_interval = curr_interval | interval([inf, sup])
                    rows.update({row: curr_interval})

    for row in range(min_val, max_val+1):
        test_interval = rows.get(row, interval())
        contiguous = True
        for idx in range(1, len(test_interval)):
            if test_interval[idx - 1].sup != (test_interval[idx].inf - 1):
                contiguous = False
        if len(test_interval) > 1 and not contiguous:
            print(row)
            print(rows.get(row))


if __name__ == "__main__":
    process_input()
    print((4000000 * 3131431) + 2647448)

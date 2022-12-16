from interval import interval


def manhattan_distance(vertex_one, vertex_two):
    return abs(vertex_one[0] - vertex_two[0]) + abs(vertex_one[1] - vertex_two[1])


def process_input():
    with open('inputs/puzzle_1.txt') as f:
        lines = f.readlines()

    answer_row = 2000000

    rows = {}

    sensors = []
    beacons = []

    for line in lines:
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
            if row == answer_row:
                curr_interval = rows.get(row, interval())
                interval_radius = distance - (abs(sensor[0] - row))
                curr_interval = curr_interval | interval([sensor[1] - interval_radius, sensor[1] + interval_radius])
                rows.update({row: curr_interval})

    interval_sums = 0
    for intrvl in rows.get(answer_row):
        interval_sums += intrvl.sup - intrvl.inf + 1
        for sensor in sensors:
            if sensor[0] == answer_row and sensor[1] in interval[intrvl.sup, intrvl.inf]:
                interval_sums -= 1
        for beacon in beacons:
            if beacon[0] == answer_row and beacon[1] in interval[intrvl.sup, intrvl.inf]:
                interval_sums -= 1

    print(interval_sums)


if __name__ == "__main__":
    process_input()

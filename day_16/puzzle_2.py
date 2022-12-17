import bisect
import copy

dp = {}
neighbors = {}
flow = {}


def max_releasable_pressure(curr_valve, opened_valves, time_left, players_left):
    if time_left == 0:
        if players_left == 1:
            return max_releasable_pressure('AA', opened_valves, 26, 0)
        else:
            return 0

    key = str(curr_valve) + " " + str(opened_valves) + " " + str(time_left) + " " + str(players_left)
    if dp.get(key, 0) > 0:
        return dp.get(key)

    state_max = 0

    if curr_valve not in opened_valves and flow.get(curr_valve) > 0:
        opened_valves_copy = copy.copy(opened_valves)
        bisect.insort(opened_valves_copy, curr_valve)
        state_max = (flow.get(curr_valve) * (time_left - 1)) + max_releasable_pressure(curr_valve, opened_valves_copy,
                                                                                       time_left - 1, players_left)

    for neighbor_valve in neighbors.get(curr_valve, []):
        state_max = max(state_max, max_releasable_pressure(neighbor_valve, opened_valves, time_left - 1, players_left))

    dp.update({key: state_max})

    return state_max


def process_input():
    with open('inputs/puzzle_1.txt') as f:
        lines = f.readlines()

    for line in lines:
        line = line.replace('\n', '')
        valve = line.split(" ")[1]
        flow_rate = int(line.split("=")[1].split(";")[0])
        neighbors_split = line.split("valves ")[1].split(", ")

        flow.update({valve: flow_rate})
        neighbors.update({valve: neighbors_split})

    print(max_releasable_pressure('AA', [], 26, 1))


if __name__ == "__main__":
    process_input()

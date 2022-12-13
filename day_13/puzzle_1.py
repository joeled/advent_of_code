import json


def parse_packet(packet_str):
    return json.loads(packet_str)


# Returns 1 if left smaller, 0 if left and right are equal and -1 if right is smaller
def compare(left, right):
    left_len = len(left)
    right_len = len(right)

    for idx in range(0, left_len):
        if idx == right_len:
            return -1

        left_val = left[idx]
        right_val = right[idx]

        if type(left_val) == int and type(right_val) == int:
            if right_val < left_val:
                return -1
            elif left_val < right_val:
                return 1
        else:
            if type(left_val) == int:
                left_val = [left_val]
            elif type(right_val) == int:
                right_val = [right_val]

            in_order = compare(left_val, right_val)

            if in_order != 0:
                return in_order

    if left_len < right_len:
        return 1

    return 0


def process_input():
    with open('inputs/puzzle_1.txt') as f:
        lines = f.readlines()

    correct_idx_sum = 0
    pair_idx = 1

    for row in range(0, len(lines), 3):
        left_str = lines[row]
        right_str = lines[row + 1]
        left = parse_packet(left_str)
        right = parse_packet(right_str)

        in_order = compare(left, right)
        if in_order == 1:
            correct_idx_sum += pair_idx

        pair_idx += 1

    print(correct_idx_sum)


if __name__ == "__main__":
    process_input()

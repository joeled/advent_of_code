curr_cycle = 1
instruction_cycle_count = 1
signal_strength_sum = 0
x = 1


def process_input():
    global curr_cycle, instruction_cycle_count, x, signal_strength_sum

    with open('inputs/puzzle_1.txt') as f:
        lines = f.readlines()

    instruction_num = 0

    while instruction_num < len(lines):
        instruction = lines[instruction_num].replace("\n", "")

        if curr_cycle == 20 or (curr_cycle - 20) % 40 == 0:
            signal_strength_sum += x * curr_cycle
            # print(curr_cycle)
            # print(x * curr_cycle)
            # print()

        if instruction == 'noop':
            instruction_cycle_count = 1
            instruction_num += 1
        else:
            if instruction_cycle_count == 2:
                x += int(instruction.split(" ")[1])
                instruction_cycle_count = 1
                instruction_num += 1
            else:
                instruction_cycle_count += 1

        curr_cycle += 1


if __name__ == "__main__":
    process_input()
    print(signal_strength_sum)
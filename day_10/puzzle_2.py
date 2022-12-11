curr_cycle = 1
instruction_cycle_count = 1
signal_strength_sum = 0
x = 1
pixels = ""


def process_input():
    global curr_cycle, instruction_cycle_count, x, signal_strength_sum, pixels

    with open('inputs/puzzle_1.txt') as f:
        lines = f.readlines()

    instruction_num = 0

    while instruction_num < len(lines):
        instruction = lines[instruction_num].replace("\n", "")

        # draw_curr_pixel
        if x - 1 <= (curr_cycle - 1) % 40 <= x + 1:
            pixels += '#'
        else:
            pixels += '.'

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
    pixel_arrays = [pixels[i:i + 40] for i in range(0, len(pixels), 40)]
    for arr in pixel_arrays:
        print(arr)

curr_full_path = ""
dir_top_level_sizes = {}
dir_parents = {}
answer_dir_sum = 0
dir_names = set("/")


def process_command(line):
    global curr_full_path, dir_names

    command_split = line.split(" ")

    if command_split[1] == 'cd':
        if command_split[2] == '..':
            full_path_split = curr_full_path.split("/")
            curr_full_path = "/".join(full_path_split[0:len(full_path_split)-2]) + "/"
        elif command_split[2] == '/':
            curr_full_path = "/"
        else:
            curr_dir = command_split[2]
            curr_full_path += curr_dir + "/"
            dir_names.add(curr_full_path)


def process_file_or_dir(line):
    line_split = line.split(" ")

    dir_top_level_sum = dir_top_level_sizes.get(curr_full_path, 0)

    if line_split[0] != 'dir':
        dir_top_level_sum += int(line_split[0])

    dir_top_level_sizes.update({curr_full_path: dir_top_level_sum})


def process_line(line):
    if line.startswith("$"):
        process_command(line)
    else:
        process_file_or_dir(line)


def process_input():
    with open('inputs/puzzle_1.txt') as f:
        lines = f.readlines()

    for line in lines:
        line = line.replace("\n", "")
        process_line(line)


def get_answer():
    global answer_dir_sum

    top_level_size = 0
    for dir_name_two in dir_top_level_sizes:
        top_level_size += dir_top_level_sizes.get(dir_name_two)

    size_needed = 30000000 - (70000000 - top_level_size)

    min_curr = 70000000
    min_name = ""

    for dir_name in dir_names:
        dir_sum = 0
        for dir_name_two in dir_top_level_sizes:
            if dir_name_two.startswith(dir_name):
                dir_sum += dir_top_level_sizes.get(dir_name_two)
        if size_needed <= dir_sum < min_curr:
            min_curr = dir_sum
            min_name = dir_name

    print(min_curr)


if __name__ == "__main__":
    process_input()
    get_answer()

curr_full_path = ""
dir_top_level_sizes = {}
dir_parents = {}
answer_dir_sum = 0
dir_names = ["/"]


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
            dir_names.append("/"+curr_dir+"/")
    else:
        # ls - Initialize dir size
        dir_top_level_sizes.update({curr_full_path: 0})


def process_file_or_dir(line):
    line_split = line.split(" ")

    dir_top_level_sum = 0

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

    for dir_name in dir_names:
        dir_sum = 0
        for dir_size in dir_top_level_sizes:
            if dir_name in dir_size:
                dir_sum += dir_top_level_sizes.get(dir_size)
        if dir_sum <= 100000:
            answer_dir_sum += dir_sum


if __name__ == "__main__":
    process_input()
    get_answer()
    print(answer_dir_sum)

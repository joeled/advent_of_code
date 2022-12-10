def process_input():
    with open('inputs/puzzle_1.txt') as f:
        lines = f.readlines()

    for line in lines:
        line = line.replace("\n", "")


if __name__ == "__main__":
    process_input()

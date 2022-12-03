if __name__ == "__main__":
    with open('inputs/puzzle_1.txt') as f:
        lines = f.readlines()

    duplicated_item_list = []

    for line in lines:
        line = line.replace("\n","")
        line_len = len(line)
        first_compartment = line[0:int(line_len/2)]
        second_compartment = line[int(line_len/2):line_len]

        common = list(set(first_compartment).intersection(second_compartment))[0]
        duplicated_item_list.append(common)

    priority_sum = 0

    for c in duplicated_item_list:
        if c.isupper():
            priority_sum += ord(c)-64+26
        else:
            priority_sum += ord(c)-96

    print(priority_sum)
if __name__ == "__main__":
    with open('inputs/puzzle_1.txt') as f:
        lines = f.readlines()

    duplicated_item_list = []

    num_groups = int(len(lines)/3)

    for i in range(0,num_groups):
        first_rucksack = lines[i*3].replace("\n","")
        second_rucksack = lines[(i*3)+1].replace("\n","")
        third_rucksack = lines[(i * 3) + 2].replace("\n","")

        common = list(set(first_rucksack).intersection(second_rucksack).intersection(third_rucksack))[0]
        duplicated_item_list.append(common)

    priority_sum = 0

    print(duplicated_item_list)

    for c in duplicated_item_list:
        if c.isupper():
            priority_sum += ord(c)-64+26
        else:
            priority_sum += ord(c)-96

    print(priority_sum)
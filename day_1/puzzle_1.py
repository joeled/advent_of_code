if __name__ == "__main__":
    with open('inputs/puzzle_1.txt') as f:
        lines = f.readlines()

    curr = 0
    max_calories = 0
    counts = []
    for line in lines:
        line = line.replace("\n", "")
        if len(line) == 0:
            curr += 1
        else:
            if len(counts) <= curr:
                counts.append(0)
            counts[curr] += int(line)
            max_calories = max(max_calories, counts[curr])

    print(max_calories)

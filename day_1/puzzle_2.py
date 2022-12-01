from heapq import heappop, heappush, heapify

if __name__ == "__main__":
    with open('inputs/puzzle_1.txt') as f:
        lines = f.readlines()

    curr = 0
    heap = []
    heapify(heap)
    counts = []
    for line in lines:
        line = line.replace("\n", "")
        if len(line) == 0:
            heappush(heap, counts[curr]*-1)
            curr += 1
        else:
            if len(counts) <= curr:
                counts.append(0)
            counts[curr] += int(line)

    sum = 0
    for i in range(3):
        sum += heappop(heap)*-1

    print(sum)

class Monkey:
    items = []
    operation = lambda x: x
    test = 0
    true_throw = 0
    false_throw = 0
    monkey_idx = 0

    def __init__(self, items, operation, test, true_throw, false_throw, monkey_idx):
        self.items = items
        self.operation = operation
        self.test = test
        self.true_throw = true_throw
        self.false_throw = false_throw
        self.monkey_idx = monkey_idx


# monkeys = [
#     Monkey([79, 98], lambda x: x*19, 23, 2, 3, 0),
#     Monkey([54, 65, 75, 74], lambda x: x+6, 19, 2, 0, 1),
#     Monkey([79, 60, 97], lambda x: x*x, 13, 1, 3, 2),
#     Monkey([74], lambda x: x+3, 17, 0, 1, 3)
# ]
# num_inspects = [0, 0, 0, 0]
# multiple = 23*19*13*17


monkeys = [
    Monkey([64], lambda x: x * 7, 13, 1, 3, 0),
    Monkey([60, 84, 84, 65], lambda x: x + 7, 19, 2, 7, 1),
    Monkey([52, 67, 74, 88, 51, 61], lambda x: x * 3, 5, 5, 7, 2),
    Monkey([67, 72], lambda x: x + 3, 2, 1, 2, 3),
    Monkey([80, 79, 58, 77, 68, 74, 98, 64], lambda x: x * x, 17, 6, 0, 4),
    Monkey([62, 53, 61, 89, 86], lambda x: x + 8, 11, 4, 6, 5),
    Monkey([86, 89, 82], lambda x: x + 2, 7, 3, 0, 6),
    Monkey([92, 81, 70, 96, 69, 84, 83], lambda x: x + 4, 3, 4, 5, 7)
]
num_inspects = [0, 0, 0, 0, 0, 0, 0, 0]
multiple = 13*19*5*2*17*11*7*3


def do_monkey_business(monkey):
    for i in range(0, len(monkey.items)):
        item = monkey.items.pop()
        inspected_item = monkey.operation(item)
        relief_item = inspected_item % multiple
        if relief_item % monkey.test == 0:
            monkeys[monkey.true_throw].items.append(relief_item)
        else:
            monkeys[monkey.false_throw].items.append(relief_item)
        num_inspects[monkey.monkey_idx] += 1


def process_input():
    for round in range(0, 10000):
        for monkey in monkeys:
            do_monkey_business(monkey)


if __name__ == "__main__":
    process_input()
    print(num_inspects)

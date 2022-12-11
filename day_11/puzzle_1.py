class Monkey:
    items = []
    operation = ''
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

    def do_operation(self, item):
        curr_op = self.operation.replace("old", str(item))
        new_item = eval(curr_op)
        return new_item


test_monkeys = [
    Monkey([79, 98], 'old*19', 23, 2, 3, 0),
    Monkey([54, 65, 75, 74], 'old + 6', 19, 2, 0, 1),
    Monkey([79, 60, 97], 'old*old', 13, 1, 3, 2),
    Monkey([74], 'old+3', 17, 0, 1, 3)
]
test_num_inspects = [0, 0, 0, 0]

monkeys = [
    Monkey([64], 'old * 7', 13, 1, 3, 0),
    Monkey([60, 84, 84, 65], 'old + 7', 19, 2, 7, 1),
    Monkey([52, 67, 74, 88, 51, 61], 'old * 3', 5, 5, 7, 2),
    Monkey([67, 72], 'old + 3', 2, 1, 2, 3),
    Monkey([80, 79, 58, 77, 68, 74, 98, 64], 'old * old', 17, 6, 0, 4),
    Monkey([62, 53, 61, 89, 86], 'old + 8', 11, 4, 6, 5),
    Monkey([86, 89, 82], 'old + 2', 7, 3, 0, 6),
    Monkey([92, 81, 70, 96, 69, 84, 83], 'old + 4', 3, 4, 5, 7)
]
num_inspects = [0, 0, 0, 0, 0, 0, 0, 0]


def do_monkey_business(monkey):
    for i in range(0, len(monkey.items)):
        item = monkey.items.pop()
        inspected_item = monkey.do_operation(item)
        relief_item = inspected_item // 3
        if relief_item % monkey.test == 0:
            monkeys[monkey.true_throw].items.append(relief_item)
        else:
            monkeys[monkey.false_throw].items.append(relief_item)
        num_inspects[monkey.monkey_idx] += 1


def process_input():
    for round in range(0, 20):
        for monkey in monkeys:
            do_monkey_business(monkey)


if __name__ == "__main__":
    process_input()
    print(num_inspects)

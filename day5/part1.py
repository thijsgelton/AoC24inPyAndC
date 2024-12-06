from collections import defaultdict


with open(r"input.txt") as f:
    order_map = defaultdict(list)
    page_ordering, ordering = f.read().split("\n\n")
    for f in page_ordering.split("\n"):
        first, second = f.strip().split("|")
        order_map[first].append(second)

    ordering = [order.split(",") for order in ordering.split("\n")]
    print(ordering)
    middle_numbers_to_add = []
    for order in ordering:
        if all(
            [
                len(set(order[i + 1 :]) - set(order_map.get(order[i], []))) == 0
                for i in range(len(order) - 1)
            ]
        ):
            middle_numbers_to_add.append(order[len(order) // 2])

    print(sum(map(int, middle_numbers_to_add)))

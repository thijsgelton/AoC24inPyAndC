from collections import defaultdict


def correct_the_ordering(order):
    for i in range(len(order) - 1):
        wrong_order = set(order[i + 1 :]) - set(order_map.get(order[i], []))
        if len(wrong_order) == 0:
            continue
        else:
            other_numbers = [order.pop(order.index(n)) for n in wrong_order]
            order = list(other_numbers) + order
            order = correct_the_ordering(order)
    return order


with open(r"C:\Users\tgelton\Projects\Persoonlijk\AoC24inPyAndC\day5\input.txt") as f:
    order_map = defaultdict(list)
    page_ordering, ordering = f.read().split("\n\n")
    for f in page_ordering.split("\n"):
        first, second = f.strip().split("|")
        order_map[first].append(second)

    ordering = [order.split(",") for order in ordering.split("\n")]
    middle_numbers_to_add = []
    incorrect_orderings = []
    for order in ordering:
        if not all(
            [
                len(set(order[i + 1 :]) - set(order_map.get(order[i], []))) == 0
                for i in range(len(order) - 1)
            ]
        ):
            incorrect_orderings.append(order)
    for order in incorrect_orderings:
        order = correct_the_ordering(order)
        middle_numbers_to_add.append(order[len(order) // 2])
    print(sum(map(int, middle_numbers_to_add)))

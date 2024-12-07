from itertools import product

with open(r"C:\Users\thijs\Programming\AoC24inPyAndC\day7\input.txt") as f:
    output, numbers = zip(*[l.strip().split(": ") for l in f.readlines()])
    correct = []
    for i in range(len(output)):
        permutations = product(["+", "*", "||"], repeat=numbers[i].count(" "))
        splitted_numbers = numbers[i].split(" ")
        for permutation in permutations:
            result = int(splitted_numbers[0])
            for j, number in enumerate(splitted_numbers[1:]):
                operator = permutation[j]
                if operator == "+":
                    result += int(number)
                if operator == "*":
                    result *= int(number)
                if operator == "||":
                    result = int(f"{result}{number}")
            if result == int(output[i]):
                correct.append(int(output[i]))
                break
    print(sum(correct))

import re


def mul(x1, x2):
    return x1 * x2


with open("input.txt") as f:
    regex_pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    input_str = f.read()
    print(sum([eval(mul_str) for mul_str in regex_pattern.findall(input_str)]))

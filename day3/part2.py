import re


def mul(x1, x2):
    return x1 * x2


with open("input.txt") as f:
    regex_pattern = re.compile(r"don't\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)")
    input_str = f.read()
    keywords = regex_pattern.findall(input_str)
    mult_list = []
    disabled = False
    for kw in keywords:
        if "mul" in kw and not disabled:
            mult_list.append(kw)
        elif "mul" in kw and disabled:
            continue
        if "don" in kw:
            disabled = True
        if "do()" in kw:
            disabled = False
    print(sum([eval(mul_str) for mul_str in mult_list]))

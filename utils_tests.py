from utils import *

reversed_input_outputs = [
    [8, -8],
    ["8", -8],
    [12.0, -12],
    [-11.0, 11],
    ["-12.0", 12],

]

def test_reversed():
    for pair in reversed_input_outputs:
        if (reversed(pair[0]) == pair[1]):
            continue
        else:
            print("FAIL TEST")
            print("fail at: ", pair[0], pair[1])
            break

test_reversed()

formatter_input_outputs = [
    [8, ['0b1000', '0o10']],
    ["8", ['0b1000', '0o10']],
    [12.0, ['0b1100', '0o14']],
    [-11.0, ['-0b1011', '-0o13']],
    [-8, ['-0b1000', '-0o10']],
    ["-12.0", ['-0b1100', '-0o14']],
]

def test_formatter():
    for pair in formatter_input_outputs:
        if (formatter(pair[0]) == pair[1]):
            continue
        else:
            print("FAIL TEST")
            print("fail at: ", pair[0], pair[1])
            break


test_formatter()

print("PASSED ALL TESTS")
#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')
def unreachable(): return False

snafu_map = { '2': 2, '1': 1, '0': 0, '-': -1, '=': -2 }
snafu_inv_map = { 4: '2', 3: '1', 2: '0', 1: '-', 0: '=' }
def conv(x):
    n = 0; exp = 1
    for ch in reversed(x):
        n += exp * snafu_map[ch]
        exp *= 5
    return n

def conv_base5(x):
    res = []
    while x > 0:
        res.append(x % 5)
        x //= 5
    res.reverse()
    return res

def conv_back(x):
    addi = 0
    len_base5 = len(conv_base5(x))
    for _ in range(len_base5):
        addi = addi * 5 + 2
    actual = conv_base5(x + addi)
    for _ in range(len(actual) - len_base5):
        addi = addi * 5 + 2
    actual = conv_base5(x + addi)
    return "".join([snafu_inv_map[x] for x in actual])

sum = 0
for line in lines:
    sum += conv(line)

snafu = conv_back(sum)
assert conv(snafu) == sum
print(snafu)

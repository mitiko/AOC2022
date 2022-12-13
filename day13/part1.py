#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n\n')

def parse(l):
    root = []
    curr = root
    prev = []
    num = None

    if l.startswith('[') and l.endswith(']'):
        l = l[1:-1]

    for chr in l:
        if chr == '[':
            next = []
            curr.append(next)
            prev.append(curr)
            curr = next
        elif chr == ']':
            if num != None:
                curr.append(num)
                num = None
            curr = prev.pop()
        
        if ord(chr) >= ord('0') and ord(chr) <= ord('9'):
            if num != None:
                num *= 10
                num += ord(chr) - ord('0')
            else:
                num = ord(chr) - ord('0')
        else:
            if num != None:
                curr.append(num)
            num = None
    if num != None:
        curr.append(num)
    return root

def cm(a, b):
    if a < b:
        return -1
    elif a == b:
        return 0
    else:
        return 1

def cmp(a, b):
    if type(a) == type(b) and type(a) == type(0):
        return cm(a, b)
    if type(a) == type(0):
        return cmp([a], b)
    elif type(b) == type(0):
        return cmp(a, [b])
    l = min(len(a), len(b))
    if l == 0:
        return cm(len(a), len(b))
    
    for i in range(l):
        x = a[i]
        y = b[i]
        res = cmp(x, y)
        if res != 0:
            return res
    return cm(len(a), len(b))


total = 0
for index, ins in enumerate(lines):
    [left, right] = ins.split('\n')
    
    a = parse(left)
    b = parse(right)
    if cmp(a, b) <= 0:
        total += index + 1

print("total:", total)

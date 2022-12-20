#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().split('\n')
vals = [int(x) for x in lines]
n = len(vals)

class Node():
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    
    def move(self):
        # detach
        self.prev.next, self.next.prev = self.next, self.prev

        lo, hi = self.prev, self.next
        if self.data > 0:
            for _ in range(self.data % (n - 1)):
                hi = hi.next
                lo = lo.next
        elif self.data < 0:
            for _ in range(abs(self.data) % (n - 1)):
                hi = hi.prev
                lo = lo.prev

        # insert
        self.prev, self.next = lo, hi
        lo.next, hi.prev = self, self

    def nth(self, offset):
        assert offset >= 0

        node = self
        for _ in range(offset):
            node = node.next
        return node

    def print_all(self):
        list = []
        node = self
        for _ in range(n):
            list.append(node.data)
            node = node.next
        print(list)

root = Node(vals[0])
zero = None
nodes = [root]

node = root
for val in vals[1:]:
    curr = Node(val)
    if val == 0:
        zero = curr

    curr.prev = node
    node.next = curr

    node = curr
    nodes.append(curr)

node.next = root
root.prev = node

for node in nodes:
    node.move()

a, b, c = zero.nth(1000 % n), zero.nth(2000 % n), zero.nth(3000 % n)
print(a.data + b.data + c.data)

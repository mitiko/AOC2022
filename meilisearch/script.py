#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

kid_paths = [[x.strip() for x in line.split('-')] for line in lines]
kids = [x[0] for x in kid_paths]
paths = [x[1] for x in kid_paths]

def lcp(a, b):
    l = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]: l += 1
        else: return l
    return l

def slcp(a, b):
    if len(a) == 0 or len(b) == 0:
        return 0
    return int(a[0] == b[0])

class Node:
    def __init__(self, data, left=None, right=None, index=-1):
        self.left = left
        self.right = right
        self.data = data
        self.index = index
    
    def insert(self, data, index):
        # print(f"Inserting {data} in {self.data}, idx={self.index}")
        l = lcp(self.data, data)
        radix = data[:l]
        node = Node(data[l:], index=index)

        if len(node.data) == 0:
            if self.index == -1:
                self.index = node.index
            return

        # if no children, then either appaned down, or do a switcheroo
        if self.left == None:
            assert self.index != -1

            if l == len(self.data):
                self.left = node
                return

            modi = Node(self.data[l:], index=self.index)
            self.data = radix; self.index = -1

            if modi.data < node.data:
                self.left, self.right = modi, node
            else:
                self.left, self.right = node, modi
            return
        
        # if one child, then either append to left, append to right, or switcheroo
        if self.right == None:
            assert self.index != -1

            if l == len(self.data):
                if slcp(self.left.data, node.data) == 0:
                    self.right = node
                    if self.right.data < self.left.data:
                        self.left, self.right = self.right, self.left
                else:
                    self.left.insert(node.data, node.index)
                return

            modi = Node(self.data[l:], left=self.left, index=self.index)
            self.data = radix; self.index = -1

            if modi.data < node.data:
                self.left, self.right = modi, node
            else:
                self.left, self.right = node, modi
            return

        if l == len(self.data):
            ll = slcp(self.left.data, node.data)
            lr = slcp(self.right.data, node.data)
            if lr == 0:
                if ll == 0:
                    if self.index != -1:
                        self.index = self.left.index
                    self.left = node
                    return
                self.left.insert(node.data, node.index)
            elif ll == 0:
                self.right.insert(node.data, node.index)
            else:
                print("Unreachable")
                assert False
            return

        modi = Node(self.data[l:], self.left, self.right, self.index)
        self.data = radix; self.index = -1

        if modi.data < node.data:
            self.left, self.right = modi, node
        else:
            self.left, self.right = node, modi


    
    # def walk(self, term=False):
    def walk(self):
        bfs = [(0, self.left), (0, self.right)]
        # bfs = [self.left, self.right]
        while len(bfs) != 0:
            # depth, node = bfs.pop() # for dfs
            depth, node = bfs[0]; bfs = bfs[1:]
            # node = bfs[0]; bfs = bfs[1:]
            app = "-"*depth
            if node != None:
                # print(node, node.left, node.right)
                # dd = node.data if len(node.data) > 0 else "x"
                # print(f"{node.index :>2} {app}{dd}")
                # if node.index != -1 and term == True:
                if node.index != -1:
                    return node.index
                bfs.append((depth+1, node.left))
                bfs.append((depth+1, node.right))
                # bfs.append(node.left)
                # bfs.append(node.right)
        # no visited bc tree

# radix_tree = Node(data="root", left=Node("l", left=Node("ll")), right=Node("r", left=Node("rl", right=Node("rlr", index=2))))

radix_tree = Node("", index=len(paths))
for i, path in enumerate(paths):
    # print()
    # print(paths)
    # print(f"Adding '{path}'")
    radix_tree.insert(path, i)
    # radix_tree.walk()
    # radix_tree.walk()

idx = radix_tree.walk()
if idx != None:
    print(idx, kids[idx])


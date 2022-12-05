#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

kid_paths = [[x.strip() for x in line.split('-')] for line in lines]
kids = [x[0] for x in kid_paths]
paths = [x[1] for x in kid_paths]
# paths = [''.join(['1' if (ord(c)-ord('L')) > 0 else '0' for c in path]) for path in paths]

def lcp(a, b):
    l = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            l += 1
        else:
            return l
    return l

class Node:
    def __init__(self, data=None, left=None, right=None, index=-1):
        self.left = left
        self.right = right
        self.data = data
        self.index = index
    
    def insert(self, data, index):
        if self.left == None:
            if self.data == None:
                self.left = Node(data, index=index)
                return

            l = lcp(self.data, data)
            # assert l > 0
            if l == len(self.data):
                self.left = Node(self.data[l:], index=self.index)
                self.right = Node(data, index=index)
                self.index = -1
            else:
                node_a = Node(data[l:], index=index)
                node_b = Node(self.data[l:], index=self.index)
                self.index = -1; self.data = data[:l]
                if node_a.data < node_b.data:
                    self.left, self.right = node_a, node_b
                else:
                    self.left, self.right = node_b, node_a
            return
        if self.right == None:
            l = lcp(self.left.data, data)
            if l == 0:
                if self.left.data < data:
                    self.right = Node(data, index=index)
                else:
                    self.right = self.left
                    self.left = Node(data, index=index)
                return
            if self.left.index == -1:
                if l == len(self.left.data):
                    return self.left.insert(data[l:], index)
                else:
                    radix = data[:l]
                    node = Node(data[l:], index=index)
                    self.left.data = self.left.data[l:]

                    if self.left.data < node.data:
                        self.left = Node(radix, self.left, node)
                    else:
                        self.left = Node(radix, node, self.left)
                    return

            radix = data[:l]
            node_a = Node(self.left.data[l:], index=self.left.index)
            node_b = Node(data[l:], index=index)
            if node_a.data < node_b.data:
                self.left = Node(radix, node_a, node_b)
            else:
                self.left = Node(radix, node_b, node_a)
            return

        assert self.index == -1
        # maybe?
        # assert(len(self.left.data) > 0 and len(self.right.data) > 0)

        # find if we should insert under left or right
        l0 = lcp(self.left.data, data)
        l1 = lcp(self.right.data, data)
        if l0 > l1:
            if l0 == len(self.left.data) and self.left.index == -1:
                self.left.insert(data[l0:], index)
            else:
                radix = data[:l0]
                node_a = Node(data[l0:], index=index)
                node_b = Node(self.left.data[l0:], index=self.left.index)
                if node_a.data < node_b.data:
                    self.left = Node(radix, node_a, node_b)
                else:
                    self.left = Node(radix, node_b, node_a)
        elif l0 < l1:
            if l1 == len(self.right.data) and self.right.index == -1:
                self.right.insert(data[l1:], index)
            else:
                # rem = "" if self.data == None else self.data[l1:]
                # node_b = Node(rem, index=self.right.index)
                radix = data[:l1]
                node_a = Node(data[l1:], index=index)
                node_b = Node(self.right.data[l1:], index=self.right.index)
                if node_a.data < node_b.data:
                    self.right = Node(radix, node_a, node_b)
                else:
                    self.right = Node(radix, node_b, node_a)
        elif l0 == 0 and l1 == 0:

            pass
        else:
            print("Unreachable")
            assert False
    
    # def walk(self, term=False):
    def walk(self):
        if self.index != -1:
            print("Started at non root")
        
        bfs = [(0, self.left), (0, self.right)]
        # bfs = [self.left, self.right]
        while len(bfs) != 0:
            # node = bfs.pop() # for dfs
            depth, node = bfs[0]; bfs = bfs[1:]
            # node = bfs[0]; bfs = bfs[1:]
            app = "-"*depth
            if node != None and node.data != None:
                print(f"{node.index :>2} {app}{node.data}")
            if node != None:
                # if node.index != -1 and term == True:
                if node.index != -1:
                    return node.index
                bfs.append((depth+1, node.left))
                bfs.append((depth+1, node.right))
                # bfs.append(node.left)
                # bfs.append(node.right)
        # no visited bc tree

# radix_tree = Node(data="root", left=Node("l", left=Node("ll")), right=Node("r", left=Node("rl", right=Node("rlr", index=2))))

radix_tree = Node()
for i, path in enumerate(paths):
    # print()
    # print(paths)
    # print(f"Adding '{path}'")
    radix_tree.insert(path, i)
    # radix_tree.walk()

idx = radix_tree.walk()
if idx != None:
    print(idx, kids[idx])


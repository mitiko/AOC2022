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

def share_prefix(a, b):
    if len(a) == 0 or len(b) == 0:
        return False
    return a[0] == b[0]

class Node:
    def __init__(self, data, left=None, right=None, index=-1, parent=None):
        self.left = left
        self.right = right
        self.data = data
        self.index = index
        self.parent = parent
    
    def insert(self, data, index):
        l = lcp(self.data, data)
        radix = data[:l]
        node = Node(data[l:], index=index)
        modi = Node(self.data[l:], self.left, self.right, self.index)

        if len(node.data) == 0:
            if l == len(self.data):
                if self.index == -1:
                    self.index = node.index
                return

            # not full match => switcharoo
            assert len(radix) > 0
            self.data = radix; self.index = node.index
            self.left = modi; self.right = None
            return

        if l == len(self.data):
            if self.left == None:
                # empty, so put in left
                self.left = node
            elif self.right == None:
                # check if in left
                if share_prefix(self.left.data, node.data):
                    self.left.insert(node.data, node.index)
                    return

                # insert in correct order
                if self.left.data < node.data:
                    self.right = node
                else:
                    self.left, self.right = node, self.left
            else:
                # check if in left or in right 
                a = share_prefix(self.left.data, node.data)
                b = share_prefix(self.right.data, node.data)
                assert a ^ b

                g = self.left if a else self.right
                g.insert(node.data, node.index)                
            return
        
        # Switcharoo
        # len(node.data) != 0
        # len(self.data) > l
        self.data = radix; self.index = -1
        if modi.data < node.data:
            self.left, self.right = modi, node
        else:
            self.left, self.right = node, modi

    def set_parents(self):
        # root node doesn't have a parent
        bfs = [(self, self.left), (self, self.right)]
        while len(bfs) != 0:
            parent, node = bfs[0]; bfs = bfs[1:]
            if node == None: continue
            node.parent = parent
            bfs.append((node, node.left))
            bfs.append((node, node.right))
        # no visited bc tree

    def walk_and_search(self):
        bfs = [(1, self.left), (1, self.right)]
        visited = set()
        total_stops = 0
        while len(bfs) != 0:
            stops, node = bfs[0]; bfs = bfs[1:]
            if node == None or node in visited: continue
            visited.add(node)

            if node.index == -1:
                bfs.append((stops+1, node.left))
                bfs.append((stops+1, node.right))
                bfs.append((stops+1, node.parent))
                continue

            node.index = -1 # disable node
            total_stops += stops
            bfs = [(0, node)]
            visited = set()
        # yes visited bc tree but we're visting parents
        return total_stops

radix_tree = Node("", index=len(paths))

for i, path in enumerate(paths):
    radix_tree.insert(path, i)

radix_tree.index = -1 # disable root node
radix_tree.set_parents()

total_stops = radix_tree.walk_and_search()
print("Total:", total_stops)

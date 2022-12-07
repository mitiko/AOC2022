#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

class Node:
    def __init__(self, name, is_dir=False, size=None, children=None, parent=None):
        self.name = name
        self.is_dir = is_dir
        self.size = size
        self.children = children
        self.parent = None

    def insert(self, node):
        node.parent = self
        if self.children == None:
            self.children = []
        self.children.append(node)
    
    def cd(self, arg):
        if arg == "..":
            return self.parent
        
        if self.children != None:
            for child in self.children:
                if child.name == arg:
                    return child

        new_dir = Node(arg, is_dir=True)
        self.insert(new_dir)
        return new_dir

    def set_size(self):
        if not self.is_dir:
            return self.size
        if self.size == None:
            self.size = 0
        for child in self.children:
            self.size += child.set_size()
        return self.size

    def walk(self):
        dfs = self.children.copy()
        self.set_size()
        used = self.size
        unused = 70_000_000 - used
        to_free = 30_000_000 - unused
        assert unused > 0 and to_free > 0
        outs = []

        while(len(dfs) != 0):
            node = dfs.pop()
            if node.is_dir and node.size > to_free:
                outs.append(node.size)
            if node.children != None:
                dfs.extend(node.children)

        return min(outs)
    
    def get_root(self):
        if self.parent == None:
            return self
        else:
            return self.parent.get_root()
        print("Not found root")

node = Node(".", is_dir=True)
for line in lines:
    args = line.split(" ")
    if line.startswith("$"):
        command = args[1]
        if command == "cd":
            arg = args[2]
            node = node.cd(arg)
        continue
    if line.startswith("dir"):
        name = args[1]
        node.insert(Node(name, is_dir=True))
    else:
        size = int(args[0])
        name = args[1]
        node.insert(Node(name, is_dir=False, size=size))

root = node.get_root()
print(root.walk())

#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

monkeys = []
m = {}

total = 0
for line in lines:
    print(line)
    if line == "":
        monkeys.append(m)
        m = {}
        continue
    if not line.startswith("  "):
        m["id"] = int(line.split(" ")[1][:-1])
        continue

    if line.startswith("  Starting items:"):
        items = line.split(":")[1].split(",")
        m["items"] = [int(x) for x in items]
        continue
    
    if line.startswith("  Test"):
        m["test"] = int(line.split(":")[1].split(" ")[3])
        continue
    
    if line.startswith("    If true"):
        m["true"] = int(line.split(":")[1].split(" ")[4])
        continue
    elif line.startswith("    If false"):
        m["false"] = int(line.split(":")[1].split(" ")[4])
        continue

    if line.startswith("  Operation"):
        args = line.split("= old")[1].split(" ")
        assert len(args) > 0
        m["op"] = args[1]
        m["arg"] = args[2]

monkeys.append(m)
inspected = [0]*len(monkeys)

# simulate
for round in range(20):
    for m_id in range(len(monkeys)):
        m = monkeys[m_id]
        items = m["items"]
        m["items"] = []
        inspected[m_id] += len(items)

        for item in items:
            arg = item if m["arg"] == "old" else int(m["arg"])

            if m["op"] == "+":
                item += arg
            elif m["op"] == "*":
                item *= arg

            item //= 3

            if item % m["test"] == 0:
                monkeys[m["true"]]["items"].append(item)
            else:
                monkeys[m["false"]]["items"].append(item)

a = max(inspected)
inspected.remove(a)
b = max(inspected)

print(a * b)

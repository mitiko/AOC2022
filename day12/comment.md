# Day 12

Funny, cause when I woke up I thought to myself "I've never done Dijkstra, what if we have graphs today?"
And then BAM! Dijkstra! Pretty cool.

Writing this in python was quite easy. Much more so than radix trees (from the meili branch) for sure.

For part 2 I tried starting backwards but I wasn't reversing the node's connections initially,
so I wouldn't find a path.. My initial instinct was maybe we can bruteforce the search trying all
possible start positions but that was too slow (>20-ish seconds on PyPy), maybe bc of copying
the dist and prev dicts. Then I saw the bug.

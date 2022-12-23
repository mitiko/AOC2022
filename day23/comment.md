# Day 23

This one was pretty awesome! I had some issues correctly understanding the examples because
the instructions were'n as clear as to what the actual actions were, I guess that'd've exposed
the solution a bit.  
First, I completely missed the stationary check, then I was confused by the "or" in "N, NE, or NW"
which led me to believe I should use `any` instead of `all` for a while, but my intuition took over,
plus the example was clearly using `all`.
Then I didn't really understand what at the end of the list meant and didn't wanna change my data structure so I just
did modulo 4 and repeated the checks twice which would simulate a list (and is probably faster (in assembly) tbh).

Part 2 was absolutely fabolous today! It's maybe.. 3-4 lines change in total? I loved it.  
CPython takes around 6.6s and PyPy around 3.9s on my machine, I'm guessing on Rust
if I preallocated memory for the set and kept track of elves explicitly (rather than checking the intersection)
it'd be faster but the current solution fits in the 15s limit, so I'm good with it.

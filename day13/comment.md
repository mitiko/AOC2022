# Day 13

My naive solution didn't deal with empty arrays properly:
```python
a = [int(x) for x in re.findall('\d+', left)]
b = [int(y) for y in re.findall('\d+', right)]

if a < b:
    total += index
```

So I wrote my own parse and compare function.  
For part 2 I was about to push them all in a list and sort it but  
then I remembered there's this more efficient O(N) solution.

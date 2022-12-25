# Day 25

Indeed, working outside of home was difficult. W GitHub Codespaces though!
(It was a bit of a pain to setup, especially when it took forever to fetch all the extensions
and even got some extra that I didn't quite need.)  
I love my math but this solution is probably a bit more hacky than it needs to be.
Basically my thinking is, converted to base 5, we can just substract 222...22_5 to get snafu.
Then we can use conjugates (from Rubik's cubes) X -> Y -> X^-1, where we know X^-1 is substracting 222...22_5.
Therefore, X is adding 222...22_5. The only issue that remains is checking the number of digits matches.
For that, I convert to base 5 the original number; and if the digit count matches, we're all gucci;
otherwise, we add more 2s for the diff in digit count. Finally, just to be safe, I assert the conversion is a bijection.

Overall, loved doing the AOC, def got me in the spirit for some efficient work and I learned some cool python
tricks, also debugged at least a million off-by-one bugs. The community was great! Coming back next year to try
and get a leaderboard result.

# adventofcode2019
My answers to the Advent of Code Challenge, 2019


# Day 1

Timing the vital line in both the pure python and the numpy solution, we see that numpy is faster.
```
In: %timeit sum([calculate_fuel(int(mass)) for mass in lines])              
34.9 µs ± 235 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

In: %timeit calculate_fuel(data).sum()                                      
5.29 µs ± 84.6 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```
# very-simple-gen-algorithm

Runs a very simple genetic algorithm to match a string input by the user.

First runs a brute force attempt - randomly guessing characters as a benchmark.

Next generates a population of 100 strings and runs an algorithm to find a match using a simple fitness function and 10% mutation rate.

Output at the end of a run looks something like:

Example for the word "juice"
```
Genetic algorithm evaluated fewer options - 1100 vs 47504930 options.
Genetic algorithm was faster - 0:00:00.027177 vs 0:18:00.596868.
```
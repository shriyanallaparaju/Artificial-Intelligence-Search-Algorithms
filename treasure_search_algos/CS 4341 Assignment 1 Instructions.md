# CS 4341 Assignment 1

---

## Overview

In this assignment you will demonstrate your understanding of global and local search algorithms by implementing a variety of search algorithms in the context of a pirate crew exploring for treasure.

---

## Part A: Global Search Algorithms

Your AI agent has just become captain of a pirate ship! Given a map of islands and routes between them (a graph). Your task is to impliment the **uniform cost**, **greedy best-first**, and **A\*** global search algorithms to enable the captain to find the best path from their starting island to the island with buried treasure. To accomplish this, the following files are provided:

- `map.json`: The treasure map in dictionary form.
- `hunch.py`: A class used to calculate the hunch (heuristic) value for greedy best-first and A* search. You must impliment the `__init__` and `__call__` methods.
- `captain.py`: A class representing your agent. You must impliment the `__init__`, `uniform_cost_search`, `greedy_best_first_search`, and `a_star_search` methods.
- `test.py`: A python script containing the 5 test cases you will be graded on. Once you impliment all the functions in `hunch.py` and `captain.py`, you can run `test.py` to see what your grade will be. Additionally, `test.py` will calculate how effectively your captain was able to navigate to the treasure. Effectiveness = Path Cost + (# of Islands Visited × 1000). **The student with the most effective captain will receive a prize.**

### The Map

The map dictionary consists of two primary keys: `islands` and `routes`.

- `islands` is a dictionary where the keys are the names of the different islands and the values are dictionaries of island features to be used to inform your captain's hunch (the heuristic used by greedy best-first and A*). The islands have the following features:
    - `latitude`: The islands latitude.
    - `longitude`: The islands longitude.
    - `area`: The area of the island in Km.
    - `coast`: The description of the island's coast (`calm`, `choppy`, or `reef`).
    - `shore`: The description of the island's shore (`cliff`, `marshy`, `port`,`rocky`, or `sandy`).
    - `terrain`: The description of the island's terrain (`desert`, `jungle`, `mountain`,`savanna`, `swamp`, or `volcano`).
- `routes` is a dictionary where the keys are the island at the origin of the route and the values are dictionaries of destinations, where each key is the name of a destination island and each value is the cost to sail from the origin island to the destination island. For example, `map['routes']['Siverrock']['Siren Cove']` would return the cost to sail from Siverrock to Siren Cove.

## Part B: Local Search Algorithms

Now that your captain has made it to the island, the crew must search for the treasure! Without a map of the island, you must impliment the **hill-climbing**, **stochastic hill-climbing**, and **simulated annealing** local search algorithms to enable your captain's crew of AI agents to find the best path to the treasure. To accomplish this, you are provided with the following files:

- `island.json`: The regions of the island in the form of a list of lists of dictionaries.
- `orders.py`: A class used to calculate the orders (value) of a given region (state) for the local search algorithms. You must impliment the `__call__` method.
- `whimsy.py`: A class used to calculate the whimsy (tempurature) of a given timestep (t) for simulated annealing. You must impliment the `__call__` method.
- `pirate.py`: A class representing your agent. You must impliment the `__init__`, `hill_climbing_search`, `stochastic_hill_climbing_search`, and `boltzmann_simulated_annealing_search` methods.
- `test.py`: A python script containing the 3 test cases you will be graded on. Once you impliment all the functions in `orders.py`, `whimsy.py`, and `pirate.py`, you can run `test.py` to see what your grade will be. Additionally, `test.py` will calculate your pirate's path to find the treasure. **The student who's pirate reaches the treasure with the shortest path will recieve a prize.**

### The Island

The island is a grid regions, represented as a list of lists of dictionaries.

- The index of each sub-list in the super-list represents the x-coordinate of the regions in that sub-list.
- Each index in the sub-list represents the y-coordinate of the region.
- Each dictionary in the sublist contains the features for the region in at corresponding row and column.
- Pirates can move up, down, left, or right, as long as there is a corresponding region at that coordinate.
- Each region has the following features:
    - `x_coordinate`: The x_coordinate of the region and its index in the super-list.
    - `y_coordinate`: The x_coordinate of the region and its index in its sub-list.
    - `elevation`: The elevation of the region in meters.
    - `terrain`: The terrain of the region (`jungle` or `desert`).
    - `treasure`: A boolean indication of whether or not the treasure is in the region. Your pirate should stop searching if they enter the region with treasure in it.

---

## Submission Instructions

- Each student must individually upload a .zip file to Canvas.
- The name of the .zip file must be your WPI username, e.g., ebprihar.
- The zip file must contain the following files in the main directory:
    - captain.py
    - hunch.py
    - orders.py
    - pirate.py
    - whimsy.py
- When implementing the functions in the files:
    - Additional imports cannot be used.
    - Function parameters cannot be changed.
    - Avoid redundancies and comment your code.

---

## Grading (Out of 100 Total Points)

|Part|Test|Points|
|-|-|-|
|A|Uniform Cost Search|10|
|A|Greedy Best-First Search|10|
|A|A* Search|10|
|A|A* Search w/ Heuristic Weight = 0|10|
|A|A* search w/ Heuristic Weight -> Infinity|10|
|B|Hill Climbing Search|10|
|B|Stochastic Hill Climbing Search|10|
|B|Simulated Annealing Search|10|
|A & B|Code Cleanlyness|20|

---

## Rubric

### Test Cases

|Metric|100%|0%|
|-|-|-|
Test Passed|Yes|No

### Code Cleanlyness

|Metric|100%|80%|60%|40%|0%|
|-|-|-|-|-|-|
|Structure|Clear, modular functions; no redundancy|Mostly modular; minimal redundancy|Some modularity; some repeated code|Functions are disorganized or too long|No structure; hard to follow|
|Comments|Thorough and helpful throughout|Mostly helpful; a few sections unclear|Sparse or generic comments|Few comments; code is hard to follow|No comments|
|Formatting|Consistent indentation, spacing, naming|Mostly consistent formatting|Minor formatting issues|Several formatting problems|Poor formatting; unreadable|

---

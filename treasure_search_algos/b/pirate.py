import math
import random
from typing import List, Tuple
from orders import Orders
from whimsy import Whimsy

class Pirate:
    def __init__(self, island: List[List[dict]]) -> None:
        '''
        Initialize the pirate (agent). Store the island here, even though the search algorithms you impliment won't know about the whole island.

        Parameters:
            island (List[List[dict]]): A list of lists, where the elements of the nested lists are dictionaries that correspond to regions of an island.
        '''
        self.island = island
        self.longitude = len(island) # number of columns in island

    def in_bounds(self, x: int, y: int) -> bool:
        '''
        Check if the given coordinates are within the island

        Parameters:
            self
            x (int): the x-coordinate of a certain location
            y (int): the y-coordinate of a certain location
        
        Returns:
            bool: True means that the coordinates are within the area of the island,
                False indicated that the coordinates are outside the bounds of the island
        '''
        
        # checks if coordinate is within island
        return (0 <= x < len(self.island)) and (0 <= y < len(self.island[x]))
    
    def neighbors(self, x: int, y: int) -> List[Tuple[int, int]]:
        '''
        Provides all the valid neighbors of a certain coordinate point

        Parameters:
            self
            x (int): the x-coordinate of a certain location
            y (int): the y-coordinate of a certain location

        Returns:
            List[Tuple[int, int]]: all the coordinates that are considered neighbors to the given coordinate point
        '''
        
        # all valid neighbors of node (x,y)
        candidates = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        return [(nx, ny) for nx, ny in candidates if self.in_bounds(nx, ny)]
    
    def cell(self, coord: Tuple[int, int]) -> dict:
        '''
        Finds the region dictionary at a given coordinate

        Parameters:
            self
            coord (Tuple[int, int]): a coordinate point whose region dictionary we want

        Returns:
            dict: the region dictionary of coord
        '''

        x, y = coord
        return self.island[x][y]

    def hill_climbing_search(self, orders: Orders, start: Tuple[int, int]) -> List[Tuple[int, int]]:
        '''
        This method should implement the hill climbing search algorithm.

        Parameters:
            orders (Orders): A callable object that estimates the value of a region (state).

        Returns:
            List[Tuple[int, int]]: A list of coordinates representing the path taken from the starting region to the final region.
        '''

        path = [start]
        current = start
        curr_score = orders(self.cell(current))

        # if the current cell is the one with the treasure, return path
        if (self.cell(current).get("treasure", False)):
            return path
        
        while True:
            neighbors = self.neighbors(*current)
            best_neighbor = current
            best_score = curr_score

            # picking the neighbor with the best score
            for n in neighbors:
                s = orders(self.cell(n))
                if (s > best_score):
                    best_score = s
                    best_neighbor = n

            # stops the loop if we reached the local max
            if (best_neighbor == current):
                break

            # setting the current node as the best neighbor
            current = best_neighbor
            path.append(current)

            curr_score = best_score

            # stops the loop if we find the treasure
            if (self.cell(current).get("treasure", False)):
                break
            
        return path

    def stochastic_hill_climbing_search(self, orders: Orders, start: Tuple[int, int]) -> List[Tuple[int, int]]:
        '''
        This method should implement the stochastic hill climbing search algorithm.

        Parameters:
            orders (Orders): A callable object that estimates the value of a region (state).

        Returns:
            List[Tuple[int, int]]: A list of coordinates representing the path taken from the starting region to the final region.
        '''

        path = [start]
        current = start
        curr_score = orders(self.cell(current))

        # immediately return if we start on the treasure
        if (self.cell(current).get("treasure", False)):
            return path
        
        while True:

            neighbors = self.neighbors(*current)
            better = [n for n in neighbors if orders(self.cell(n)) > curr_score] # only takes in list of all the neighbors that have a better score than the current node

            # break when we reach local max
            if not better:
                break

            # randomly choose from the better neighbors
            current = random.choice(better)
            path.append(current)
            curr_score = orders(self.cell(current)) # update score
            
            # break if we find the score
            if (self.cell(current).get("treasure", False)):
                break

        return path

    def boltzmann_simulated_annealing_search(self, orders: Orders, whimsy: Whimsy, start: Tuple[int, int]) -> List[Tuple[int, int]]:
        '''
        This method should implement the simulated annealing search algorithm using the boltzmann equation to determine the annealing rate.

        Parameters:
            orders (Orders): A callable object that estimates the value of a region (state).
            whimsy (Whimsy): A callable object that returns the pirates willingess to go off on a whim as a function of how long they've been exploring (the tempurature as a function of t)

        Returns:
            List[Tuple[int, int]]: A list of coordinates representing the path taken from the starting region to the final region.
        '''

        path = [start]
        current = start
        curr_score = orders(self.cell(current))

        # immediately return if we start on the treasure
        if (self.cell(current).get("treasure", False)):
            return path
        
        t = 0
        while t < 1000:            

            # picking random neighbor
            x, y = current
            neighbors = [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]
            neighbors = [(nx, ny) for nx, ny in neighbors if self.in_bounds(nx, ny)]

            # break if we can't move anywhere
            if not neighbors:
                break

            candidate = random.choice(neighbors)
            candidate_score = orders(self.cell(candidate))
            
            # find if the candidate score if better than current score
            delta = candidate_score - curr_score

            # if candidate score is better, take it
            if delta >= 0:
                accept = True
            else:
                # moving to next choice with probability e^(diff in scores / temperature)
                T = whimsy(t)
                accept = (T > 0) and (random.random() < math.exp(delta / T))

            if accept:
                # update the current candidate if we accepted it
                current = candidate
                curr_score = candidate_score

                path.append(current)
                if self.cell(current).get("treasure", False):
                    break
            
            # add 1 to the timestep
            t += 1

        return path

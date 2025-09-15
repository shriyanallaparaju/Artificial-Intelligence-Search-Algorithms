from typing import Dict, List
from hunch import Hunch

class Captain:
    def __init__(self, map: Dict) -> None:
        '''
        Initialize the captian (agent) with a map (graph).

        Parameters:
            map (Map): The map (a graph), including all known islands and routes.
        '''

        self.map = map

    '''
    Helper function that performs best first search

    Parameters:
        self
        start (str): the starting node of the graph that we will explore
        goal (str): the node of the graph that we would like to reacj
        f_func: the evaluation function (f(n))

    Returns:
        tuple[list[str], int, int]: tuples of the path that we have taken so far, the cost of the path, 
        and the number of nodes expanded
    '''
    def best_first_search(self, start: str, goal: str, f_func) -> tuple[list[str], int, int]:
         class Node:
              def __init__(self, state: str, parent=None, cost=None) -> None:
                   '''
                   Intiialize the node class

                   Parameters:
                        self
                        state (str): contains the current state of the node
                            start - at the starting node
                            goal - reached the goal node
                            neighbor - exploring the a neighbor node
                        parent: the parent node of the node
                        cost: the cost of the path (g(n))
                   '''
                   
                   self.state = state
                   self.parent = parent
                   self.cost = cost

              def path(self) -> list[str]:
                   '''
                   Reconstructing the path from the root node to the current node

                   Parameters:
                        self

                   Returns
                        list[str]: a list of the nodes' states from the root to the current node
                   '''
                   
                   # result is a list of strings that will store the states of the nodes
                   node, result = self, []

                   while node is not None:
                        # work from the current node up the graph to find the path
                        result.append(node.state)
                        node = node.parent

                   # reverse result so that you get the path from the root to the current node,
                   # not the current node to the root
                   return list(reversed(result))
              
         start_node = Node(state=start, cost=0)
         frontier = [(f_func(start, 0), start_node)] # intiializing frontier with the evaluation function and starting node
         reached = {start: start_node} # the list that stores all the nodes we expanded

         while frontier:
              frontier.sort(key=lambda x: x[0]) # order the frontier from lowest to highest f(n) value
              _, node = frontier.pop(0) # take the starting node off the frontier

              # when we reach our goal, return the path that we took, its cost, and the number of nodes we expanded
              if node.state == goal:
                   return node.path(), int(node.cost), len(reached)
              
              # exploring all of the neighbors of the current node
              for neighbor, travel_cost in self.map['routes'][node.state].items():
                   new_cost = node.cost + travel_cost
                   
                   # make the neighbor a child node of the current node
                   child = Node(state=neighbor, parent=node, cost=new_cost)

                   # if the state is new or we found a cheaper path, add to frontier
                   if neighbor not in reached or new_cost < reached[neighbor].cost:
                        reached[neighbor] = child
                        frontier.append((f_func(neighbor, new_cost), child))   

         
         # default return if we weren't able to reach any other nodes
         return [], 0, len(reached)         

    
    def uniform_cost_search(self, starting_island_name: str, treasure_island_name: str) -> List[str]:
        '''
        This method should implement the uniform cost search algorithm.

        Parameters:
            starting_island_name (str): The name of the starting island.
            treasure_island_name (str): The name of the island with treasure (goal).
            hunch (Hunch): A callable object that estimates cost to the treasure (goal).

        Returns:
            List[str]: A list of island names representing the path taken from the starting island to the treasure island. If no valid path exists, return an empty list.
            int: The cost of the path. If no valid path exits, return 0.
            int: The number of islands (nodes) visited.
        '''

        # using path cost g to get from starting island to treasure island
        # call to best first search
        return self.best_first_search(starting_island_name, treasure_island_name, f_func=lambda n, g: g)
        
    def greedy_best_first_search(self, starting_island_name: str, treasure_island_name: str, hunch: Hunch) -> List[str]:
        '''
        This method should implement the greedy best-first search algorithm.

        Parameters:
            start (str): The name of the starting island.
            goal (str): The name of the goal island.

        Returns:
            List[str]: A list of island names representing the path taken from the starting island to the treasure island. If no valid path exists, return an empty list.
            int: The cost of the path. If no valid path exits, return 0.
            int: The number of islands (nodes) visited.

        This method should implement Greedy Best-First Search, using only the heuristic
        estimate to choose which island to explore next.
        '''
        
        # uses only hunch value to get to the treasure island
        # call to best first search
        return self.best_first_search(starting_island_name, treasure_island_name, f_func=lambda n, g: hunch(n, treasure_island_name))

    def a_star_search(self, starting_island_name: str, treasure_island_name: str, hunch: Hunch, stubbornness: float) -> List[str]:
        '''
        This method should implement the A* search algorithm.

        Parameters:
            starting_island_name (str): The name of the starting island.
            treasure_island_name (str): The name of the goal island.
            hunch (Hunch): A callable object that estimates cost to the treasure (goal).
            stubbornness (float): A multiplier on the hunch's influence, equivalent to heuristic weight.

        Returns:
            List[str]: A list of island names representing the path taken from the starting island to the treasure island. If no valid path exists, return an empty list.
            int: The cost of the path. If no valid path exits, return 0.
            int: The number of islands (nodes) visited.
        '''

        # uses the hunch value, stubborness (the weight for the heuristic), and the path cost to get to treasure island
        return self.best_first_search(starting_island_name, treasure_island_name, f_func=lambda n, g: g + stubbornness * hunch(n, treasure_island_name))

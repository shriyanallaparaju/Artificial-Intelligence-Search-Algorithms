import math
from typing import Any, Dict

class Hunch:
    def __init__(self, map: Dict) -> None:
        '''
        Initialize the hunch (the heuristic) with access to the treasure map.
        Use this map to help calculate heuristic values, i.e., estimate the cost to reach the treasure (the goal).

        Parameters:
            map (Map): The map (a graph), including all known islands and routes.
        '''
        self.map = map
        ##raise NotImplementedError()

    def __call__(self, hunch_island_name: str, treasure_island_name: Any) -> float:
        '''
        Return an estimated cost from the given island to the treasure (the goal).
        Design your own heuristic logic based on the various island properties.

        Parameters:
            hunch_island_name (str): The name of the island from which to estimate the cost to the treasure island (goal).
            goal_island_name (str): The treasure island's name.

        Returns:
            float: An estimate of the remaining cost to reach the treasure (the goal).
        '''

        # note for all variable names:
        # 1 corresponds to the hunch island
        # 2 corresponds to the treasure island
        
        lat1 = self.map['islands'][hunch_island_name]['latitude']
        lon1 = self.map['islands'][hunch_island_name]['longitude']
        lat2 = self.map['islands'][treasure_island_name]['latitude']
        lon2 = self.map['islands'][treasure_island_name]['longitude']

        dist = math.sqrt(pow((lat2 - lat1), 2) + pow((lon2 - lon1), 2)) # linear distance btwn islands

        # the difficulty of the trip
        # will be updated later in the function
        # the more difficult it is to get to and/or traverse the island, the higher the difficulty
        difficulty1 = 0
        difficulty2 = 0
        
        # the type of coast that each island has
        coast1 = self.map['islands'][hunch_island_name]['coast']
        coast2 = self.map['islands'][treasure_island_name]['coast']

        # incrementing difficulty based on the type of coast the islands have
        if (coast1 == "calm"):
            difficulty1 += 1
        elif (coast1 == "choppy"):
            difficulty1 += 2
        elif (coast1 == "reef"):
            difficulty1 += 3

        if (coast2 == "calm"):
            difficulty2 += 1
        elif (coast2 == "choppy"):
            difficulty2 += 2
        elif (coast2 == "reef"):
            difficulty2 += 3

        # the type of terrain each island has
        terrain1 = self.map['islands'][hunch_island_name]['terrain']
        terrain2 = self.map['islands'][treasure_island_name]['terrain']

        # updating the difficulty values according to the type of terrain each island has
        if (terrain1 == "savanna"):
            difficulty1 += 1
        elif (terrain1 == "desert"):
            difficulty1 += 2
        elif (terrain1 == "jungle"):
            difficulty1 += 2.5
        elif (terrain1 == "swamp" or terrain1 == "moutain"):
            difficulty1 += 3
        elif (terrain1 == "volcano"):
            difficulty1 += 3.5

        if (terrain2 == "savanna"):
            difficulty2 += 1
        elif (terrain2 == "desert"):
            difficulty2 += 2
        elif (terrain2 == "jungle"):
            difficulty2 += 2.5
        elif (terrain2 == "swamp" or terrain2 == "moutain"):
            difficulty2 += 3
        elif (terrain2 == "volcano"):
            difficulty2 += 3.5

        # the type of shore that each island has
        shore1 = self.map['islands'][hunch_island_name]['shore']
        shore2 = self.map['islands'][treasure_island_name]['shore']

        # updating the difficulty values based on the type of shore each island has
        if (shore1 == "port"):
            difficulty1 += 1
        elif (shore1 == "sandy"):
            difficulty1 +=1.5
        elif (shore1 == "marshy"):
            difficulty1 += 2
        elif ((shore1 == "cliff") or (shore1 == "rocky")):
            difficulty1 += 3

        if (shore2 == "port"):
            difficulty2 += 1
        elif (shore2 == "sandy"):
            difficulty2 +=1.5
        elif (shore2 == "marshy"):
            difficulty2 += 2
        elif ((shore2 == "cliff") or (terrain2 == "rocky")):
            difficulty2 += 3

        # the trip factor is the average difficulty across both islands
        trip_factor = (difficulty1 + difficulty2) / 2

        area1 = self.map['islands'][hunch_island_name]['area']
        area2 = self.map['islands'][treasure_island_name]['area']

        #the area factor is the average area of both islands
        area_factor = (area1 + area2) / 2
        area_weight = 0.01 #adding this so that the area of the islands doesn't influence the heuristic as much as the distance

        heuristic = dist * (trip_factor + (area_factor * area_weight))
        return heuristic

        ## raise NotImplementedError()

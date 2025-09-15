import json
import math
from typing import Dict, Any
from hunch import Hunch
from captain import Captain

class TestHunch:
    def __init__(self, map: Dict) -> None:
        self.map = map

    def __call__(self, hunch_island_name: str, treasure_island_name: Any) -> float:
        lat1 = self.map['islands'][hunch_island_name]['latitude']
        lon1 = self.map['islands'][hunch_island_name]['longitude']
        lat2 = self.map['islands'][treasure_island_name]['latitude']
        lon2 = self.map['islands'][treasure_island_name]['longitude']
        return math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)

with open('map.json', 'r') as f:
    treasure_map = json.load(f)

results = []

# Configuration with different results for all three searches.
hunch = TestHunch(treasure_map)
captain = Captain(treasure_map)

# Uniform Cost Search
results.append(
    captain.uniform_cost_search(
        'Mutiny',
        'Fogshore'
    ) == (
        ['Mutiny', 'Scabbard', 'Cutlass', 'Bonefire', 'Marauder', 'Saltspire', 'Bloodspike', 'Blackreef', 'Dagger', 'Saltwind', 'Fogshore'],
        77836,
        100
    )
)

# Greedy Best-First Search
results.append(
    captain.greedy_best_first_search(
        'Mutiny',
        'Fogshore',
        hunch
    ) == (
        ['Mutiny', 'Wraith', 'Cannonshot', 'Stormspire', 'Leviathan', 'Blackreef', 'Smuggler', 'Saltwind', 'Fogshore'],
        96175,
        56
    )
)

# A* Search
results.append(
    captain.a_star_search(
        'Mutiny',
        'Fogshore',
        hunch,
        2500
    ) == (
        ['Mutiny', 'Scabbard', 'Cutlass', 'Bonefire', 'Marauder', 'Saltspire', 'Bloodspike', 'Blackreef', 'Dagger', 'Saltwind', 'Fogshore'],
        77836,
        81
    )
)

# A* Search w/ Heuristic Weight = 0
results.append(
    captain.a_star_search(
        'Mutiny',
        'Fogshore',
        hunch,
        0
    ) == (
        ['Mutiny', 'Scabbard', 'Cutlass', 'Bonefire', 'Marauder', 'Saltspire', 'Bloodspike', 'Blackreef', 'Dagger', 'Saltwind', 'Fogshore'],
        77836,
        100
    )
)

# A* search w/ Heuristic Weight -> Infinity
results.append(
    captain.a_star_search(
        'Mutiny',
        'Fogshore',
        hunch,
        1000000
    ) == (
        ['Mutiny', 'Wraith', 'Cannonshot', 'Stormspire', 'Leviathan', 'Blackreef', 'Smuggler', 'Saltwind', 'Fogshore'],
        96175,
        56
    )
)

# Perform search with the provided hunch
hunch = Hunch(treasure_map)
captain = Captain(treasure_map)
search = captain.a_star_search('Mutiny', 'Fogshore', hunch, 1)

# Print results
print(results, search)

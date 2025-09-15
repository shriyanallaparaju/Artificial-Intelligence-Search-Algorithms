import json
import random
from orders import Orders
from whimsy import Whimsy
from pirate import Pirate

class TestOrders:
    def __call__(self, region: dict) -> float:
        return region['elevation']

class TestWhimsy:
    def __call__(self, step: int) -> float:
        return 10 - step

with open('island.json', 'r') as f:
    island = json.load(f)

orders = TestOrders()
whimsy = TestWhimsy()
pirate = Pirate(island)

results = []

# Hill Climbing Search
results.append(
    pirate.hill_climbing_search(orders, (14, 0)) == [(14, 0), (13, 0), (12, 0), (12, 1)]
)

# Stochastic Hill Climbing Search
random.seed(1234)
results.append(
    pirate.stochastic_hill_climbing_search(orders, (14, 0)) == [(14, 0), (14, 1), (13, 1), (12, 1)]
)

# Simulated Annealing Search
random.seed(5678)
results.append(
    pirate.boltzmann_simulated_annealing_search(orders, whimsy, (14, 0)) == [(14, 0), (13, 0), (12, 0), (12, 1), (12, 2), (12, 1)]
)

# Get search path
random.seed(0)
search = pirate.boltzmann_simulated_annealing_search(Orders(), Whimsy(), (14, 14))

print(results, search)
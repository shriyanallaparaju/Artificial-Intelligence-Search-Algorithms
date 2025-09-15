import math

class Orders:
    def __call__(self, region: dict) -> float:
        '''
        Return the value of the current region (state) dictionary.
        Design your own logic to determine the value of a state given the following hint:
        "The treasure lies at the highest point in the island's northern jungle."
        (Each region is at a particular index in the nested lists ([x_coordinate][y_coordinate]), lower x_coordinate is more north.)

        Parameters:
            step (int): The timestep (t) for which to generate the temperature (T).

        Returns:
            float: The temperature of the given timestamp.
        '''
        # if the region has the treasure make sure it always gets picked
        if region.get("treasure", False):
            return float("inf")
        
        x = region.get("x_coordinate", 0)
        elevation = region.get("elevation", 0)
        terrain = region.get("terrain", "desert")

        # make the score so that the higher elevations are given a better score
        score = float(elevation)

        # increase the score significantly if the terrain of the island is jungle
        if terrain == "jungle":
            score += 1000
        else:
            # decrease it significantly otherwise
            score -= 1000
        
        score -= 10 * x
        return score
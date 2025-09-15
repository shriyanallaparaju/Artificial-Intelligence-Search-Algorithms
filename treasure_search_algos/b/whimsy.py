import math

class Whimsy:
    def __call__(self, step: int) -> float:
        '''
        Return the temperature (T) corresponding to the provided timestep (t).
        Design your own temperature logic for simulated annealing.

        Parameters:
            step (int): The timestep (t) for which to generate the temperature (T).

        Returns:
            float: The temperature of the given timestamp.
        '''
        
        # initial temperature
        T_init = 10.0
        
        # alpha represents cooling factor
        alpha = 0.01

        # calculating final temperature
        return T_init * math.exp(-alpha * step)
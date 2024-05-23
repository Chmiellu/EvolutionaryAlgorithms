import numpy as np
from parameters import n, min_value, max_value, decimal_places
class Individual:
    def __init__(self):
        self.genotyp = np.round(np.random.uniform(min_value, max_value, n), decimal_places)

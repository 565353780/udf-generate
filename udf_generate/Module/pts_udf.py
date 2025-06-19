import numpy as np
from scipy.spatial import cKDTree


class PtsUDF:
    def __init__(self, surface_points: np.ndarray) -> None:
        self.kdtree = cKDTree(surface_points)
        return

    def query(self, query_points: np.ndarray) -> np.ndarray:
        dists = self.kdtree.query(query_points)[0]
        return dists

import numpy as np


def getSamplePointMatrix(sample_num):
    assert sample_num > 0

    sample_unit_length = 1.0 / sample_num
    sample_start_length = sample_unit_length / 2.0 - 0.5

    coords = sample_start_length + np.arange(sample_num) * sample_unit_length

    z_grid, x_grid, y_grid = np.meshgrid(coords, coords, coords, indexing="ij")

    sample_point_matrix = np.stack([z_grid, x_grid, y_grid], axis=-1)

    return sample_point_matrix

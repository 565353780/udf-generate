import numpy as np
import open3d as o3d
from copy import deepcopy

from udf_generate.Config.sample import (
    SAMPLE_NUM,
    SAMPLE_POINT_ARRAY,
    SAMPLE_POINT_CLOUD,
)
from udf_generate.Module.pts_udf import PtsUDF


def toPtsUDF(point_array: np.ndarray) -> np.ndarray:
    copy_point_array = deepcopy(point_array)

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(copy_point_array)

    dist_array = np.array(SAMPLE_POINT_CLOUD.compute_point_cloud_distance(pcd))

    udf = dist_array.reshape(SAMPLE_NUM, SAMPLE_NUM, SAMPLE_NUM)
    return udf


def toPtsUDFKDTree(point_array: np.ndarray) -> np.ndarray:
    copy_point_array = deepcopy(point_array)

    pts_udf = PtsUDF(copy_point_array)

    dist_array = pts_udf.query(SAMPLE_POINT_ARRAY)

    udf = dist_array.reshape(SAMPLE_NUM, SAMPLE_NUM, SAMPLE_NUM)
    return udf

import numpy as np
import open3d as o3d

from udf_generate.Config.sample import SAMPLE_POINT_MATRIX


def toUDFPcd(udf: np.ndarray, dist_max: float = 0.02) -> o3d.geometry.PointCloud:
    udf_points = SAMPLE_POINT_MATRIX[np.where(udf <= dist_max)].reshape(-1, 3)

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(udf_points)

    pcd.paint_uniform_color([1, 0, 0])
    return pcd


def renderUDF(udf: np.ndarray, dist_max: float = 0.02) -> bool:
    udf_pcd = toUDFPcd(udf, dist_max)
    o3d.visualization.draw_geometries([udf_pcd])
    return True

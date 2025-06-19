import torch
import numpy as np
import open3d as o3d
from copy import deepcopy

import udf_cpp

from udf_generate.Config.sample import (
    SAMPLE_NUM,
    SAMPLE_POINT_MATRIX,
    SAMPLE_POINT_ARRAY,
)


def createRaycastingScene(
    mesh: o3d.geometry.TriangleMesh,
) -> o3d.t.geometry.RaycastingScene:
    mesh = o3d.t.geometry.TriangleMesh.from_legacy(mesh)
    scene = o3d.t.geometry.RaycastingScene()
    scene.add_triangles(mesh)
    return scene


def toMeshDists(
    scene: o3d.t.geometry.RaycastingScene, points_array: np.ndarray
) -> np.ndarray:
    query_points_array = o3d.core.Tensor(points_array, dtype=o3d.core.Dtype.Float32)
    unsigned_distance_array = scene.compute_distance(query_points_array).numpy()
    return unsigned_distance_array


def toMeshUDF(mesh: o3d.geometry.TriangleMesh) -> np.ndarray:
    copy_mesh = deepcopy(mesh)

    scene = createRaycastingScene(copy_mesh)

    udf = toMeshDists(scene, SAMPLE_POINT_MATRIX)
    return udf


def toMeshUDFCPP(mesh: o3d.geometry.TriangleMesh) -> np.ndarray:
    copy_mesh = deepcopy(mesh)

    vertices = np.asarray(copy_mesh.vertices)
    triangles = np.asarray(copy_mesh.triangles)

    dists = udf_cpp.point_mesh_udf(SAMPLE_POINT_ARRAY, vertices, triangles)

    udf = np.asarray(dists).reshape(SAMPLE_NUM, SAMPLE_NUM, SAMPLE_NUM)

    return udf

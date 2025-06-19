import os
import numpy as np
import open3d as o3d

from udf_generate.Method.trans import normalizeGeometry
from udf_generate.Module.udf_manager import UDFManager


def demo_pcd():
    home = os.environ["HOME"]
    mesh_file_path = home + "/chLi/Dataset/vae-eval/mesh/000.obj"
    save_udf_file_path = home + "/chLi/Dataset/vae-eval/udf/000.npy"
    dist_max = 0.005
    overwrite = True

    mesh = o3d.io.read_triangle_mesh(mesh_file_path)

    vertex_num = np.asarray(mesh.vertices).shape[0]

    pcd = mesh.sample_points_uniformly(4 * vertex_num)

    normalizeGeometry(pcd)

    udf = UDFManager.toPcdUDF(pcd)

    UDFManager.renderUDF(udf, dist_max)

    UDFManager.saveUDF(udf, save_udf_file_path, overwrite)
    return True


def demo_mesh():
    home = os.environ["HOME"]
    mesh_file_path = home + "/chLi/Dataset/vae-eval/mesh/000.obj"
    save_udf_file_path = home + "/chLi/Dataset/vae-eval/udf/000.npy"
    dist_max = 0.001
    overwrite = True

    mesh = o3d.io.read_triangle_mesh(mesh_file_path)

    normalizeGeometry(mesh)

    udf = UDFManager.toMeshUDF(mesh)

    UDFManager.renderUDF(udf, dist_max)

    UDFManager.saveUDF(udf, save_udf_file_path, overwrite)
    return True

import os
import numpy as np
import open3d as o3d
from typing import Union

from udf_generate.Method.io import loadUDF, saveUDF
from udf_generate.Method.pts_udf import toPtsUDF, toPtsUDFKDTree
from udf_generate.Method.mesh_udf import toMeshUDF, toMeshUDFCPP
from udf_generate.Method.render import toUDFPcd, renderUDF


class UDFManager(object):
    @staticmethod
    def loadUDF(udf_file_path: str) -> Union[np.ndarray, None]:
        return loadUDF(udf_file_path)

    @staticmethod
    def saveUDF(
        udf: np.ndarray, save_udf_file_path: str, overwrite: bool = False
    ) -> bool:
        return saveUDF(udf, save_udf_file_path, overwrite)

    @staticmethod
    def toPtsUDF(pts: np.ndarray) -> np.ndarray:
        return toPtsUDF(pts)

    @staticmethod
    def toPtsUDFKDTree(pts: np.ndarray) -> np.ndarray:
        return toPtsUDFKDTree(pts)

    @staticmethod
    def toPcdUDF(pcd: o3d.geometry.PointCloud) -> np.ndarray:
        pts = np.asarray(pcd.points)
        return UDFManager.toPtsUDF(pts)

    @staticmethod
    def toPcdUDFKDTree(pcd: o3d.geometry.PointCloud) -> np.ndarray:
        pts = np.asarray(pcd.points)
        return UDFManager.toPtsUDFKDTree(pts)

    @staticmethod
    def toMeshUDF(mesh: o3d.geometry.TriangleMesh) -> np.ndarray:
        return toMeshUDF(mesh)

    @staticmethod
    def toMeshUDFCPP(mesh: o3d.geometry.TriangleMesh) -> np.ndarray:
        return toMeshUDFCPP(mesh)

    @staticmethod
    def toUDFPcd(udf: np.ndarray, dist_max: float = 0.02) -> np.ndarray:
        return toUDFPcd(udf, dist_max)

    @staticmethod
    def renderUDF(udf: np.ndarray, dist_max: float = 0.02) -> bool:
        return renderUDF(udf, dist_max)

    @staticmethod
    def toPcdFileUDF(pcd_file_path: str) -> Union[np.ndarray, None]:
        if not os.path.exists(pcd_file_path):
            print("[ERROR][UDFManager::toPcdFileUDF]")
            print("\t pcd file not exist!")
            print("\t pcd_file_path:", pcd_file_path)
            return None

        pcd = o3d.io.read_point_cloud(pcd_file_path)
        pts = np.asarray(pcd.points)
        return UDFManager.toPtsUDF(pts)

    @staticmethod
    def toMeshFileUDF(mesh_file_path: str) -> Union[np.ndarray, None]:
        if not os.path.exists(mesh_file_path):
            print("[ERROR][UDFManager::toMeshFileUDF]")
            print("\t mesh file not exist!")
            print("\t mesh_file_path:", mesh_file_path)
            return None

        mesh = o3d.io.read_triangle_mesh(mesh_file_path)
        return UDFManager.toMeshUDF(mesh)

    @staticmethod
    def toUDFFilePcd(
        udf_file_path: str, dist_max: float = 0.02
    ) -> Union[o3d.geometry.PointCloud, None]:
        udf = loadUDF(udf_file_path)

        if udf is None:
            print("[ERROR][UDFManager::toUDFFilePcd]")
            print("\t loadUDF failed!")
            return None

        return UDFManager.toUDFPcd(udf, dist_max)

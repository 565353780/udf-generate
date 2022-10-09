#!/usr/bin/env python
# -*- coding: utf-8 -*-

from udf_generate.Config.sample import \
    SAMPLE_POINT_MATRIX, SAMPLE_Z_ANGLE_LIST, \
    SAMPLE_X_ANGLE_LIST, SAMPLE_Y_ANGLE_LIST

from udf_generate.Method.paths import createFileFolder, getFilePath
from udf_generate.Method.udfs import \
    loadMesh, normalizeMesh, rotateMesh, \
    getRaycastingScene, getPointDistListToMesh, \
    saveUDF


class UDFGenerator(object):

    def __init__(self, mesh_file_path=None):
        self.mesh_file_path = mesh_file_path

        self.mesh = None

        if mesh_file_path is not None:
            self.loadMesh(mesh_file_path)
        return

    def loadMesh(self, mesh_file_path):
        self.mesh = loadMesh(mesh_file_path)

        assert self.mesh is not None

        normalizeMesh(self.mesh)
        return True

    def getUDF(self, z_angle=0, x_angle=0, y_angle=0):
        assert self.mesh is not None

        rotateMesh(self.mesh, z_angle, x_angle, y_angle)

        scene = getRaycastingScene(self.mesh)
        udf = getPointDistListToMesh(scene, SAMPLE_POINT_MATRIX)

        rotateMesh(self.mesh, -z_angle, -x_angle, -y_angle)
        return udf

    def generateUDF(self, udf_save_file_basepath):
        createFileFolder(udf_save_file_basepath)

        for z_angle in SAMPLE_Z_ANGLE_LIST:
            for x_angle in SAMPLE_X_ANGLE_LIST:
                for y_angle in SAMPLE_Y_ANGLE_LIST:
                    udf = self.getUDF(z_angle, x_angle, y_angle)
                    assert udf is not None

                    param_name_value_list = []
                    if z_angle != 0:
                        param_name_value_list.append(['rotz', z_angle])
                    if x_angle != 0:
                        param_name_value_list.append(['rotx', x_angle])
                    if y_angle != 0:
                        param_name_value_list.append(['roty', y_angle])

                    udf_save_file_path = getFilePath(udf_save_file_basepath,
                                                     param_name_value_list)
                    saveUDF(udf, udf_save_file_path)
        return True

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from udf_generate.Module.udf_generate_manager import UDFGenerateManager


def demo():
    mesh_root_folder_path = "/home/chli/scan2cad/im3d/data/pix3d/metadata/model/"
    udf_save_root_folder_path = "/home/chli/scan2cad/im3d_udf/"

    udf_generate_manager = UDFGenerateManager(mesh_root_folder_path)
    udf_generate_manager.generateAllUDF(udf_save_root_folder_path)
    return True

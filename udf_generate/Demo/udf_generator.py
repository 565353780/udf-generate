#!/usr/bin/env python
# -*- coding: utf-8 -*-

from udf_generate.Module.udf_generator import UDFGenerator


def demo():
    mesh_file_path = "/home/chli/scan2cad/im3d/data/pix3d/metadata/model/bed/IKEA_BEDDINGE/model.obj"
    udf_save_file_basepath = "/home/chli/scan2cad/im3d_udf/bed/IKEA_BEDDINGE/udf"

    udf_generator = UDFGenerator(mesh_file_path)
    udf_generator.generateUDF(udf_save_file_basepath)
    return True

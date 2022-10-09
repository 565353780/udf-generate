#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from multiprocessing import Pool
from tqdm import tqdm

from udf_generate.Module.udf_generator import UDFGenerator


class UDFGenerateManager(object):

    def __init__(self, mesh_root_folder_path, processes=os.cpu_count()):
        self.processes = processes

        self.mesh_root_folder_path = mesh_root_folder_path

        self.mesh_file_path_list = []

        self.loadMeshFilePathList()
        return

    def loadMeshFilePathList(self):
        assert os.path.exists(self.mesh_root_folder_path)

        print("[INFO][UDFGenerateManager::loadMeshFilePathList]")
        print("\t start load mesh file path list...")
        for root, _, files in os.walk(self.mesh_root_folder_path):
            for file_name in files:
                if file_name[-4:] != ".obj":
                    continue

                file_path = root + "/" + file_name
                if not os.path.exists(file_path):
                    continue

                self.mesh_file_path_list.append(file_path)
        return True

    def generateSingleUDF(self, inputs):
        '''
        inputs: [mesh_file_path, udf_save_file_basepath]
        '''
        assert len(inputs) == 2

        mesh_file_path, udf_save_file_basepath = inputs
        udf_generator = UDFGenerator(mesh_file_path)
        udf_generator.generateUDF(udf_save_file_basepath)
        return True

    def generateAllUDF(self, udf_save_root_folder_path):
        inputs_list = []
        for mesh_file_path in self.mesh_file_path_list:
            mesh_file_name = mesh_file_path.split("/")[-1]
            mesh_file_basename = mesh_file_name[:-4]
            mesh_label_path = mesh_file_path.replace(
                self.mesh_root_folder_path, "").replace(mesh_file_name, "")
            udf_save_file_basepath = udf_save_root_folder_path + \
                mesh_label_path + mesh_file_basename + "/udf"
            inputs_list.append([mesh_file_path, udf_save_file_basepath])

        print("[INFO][UDFGenerateManager::generateAllUDF]")
        print("\t start running generateSingleUDF...")
        for inputs in tqdm(inputs_list):
            self.generateSingleUDF(inputs)
        return True

        pool = Pool(processes=self.processes)
        print("[INFO][UDFGenerateManager::generateAllUDF]")
        print("\t start running generateSingleUDF with pool...")
        _ = list(
            tqdm(pool.imap(self.generateSingleUDF, inputs_list),
                 total=len(inputs_list)))
        pool.close()
        pool.join()
        return True

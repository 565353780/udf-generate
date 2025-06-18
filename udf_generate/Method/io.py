import os
import numpy as np
from typing import Union

from udf_generate.Method.path import createFileFolder, removeFile, renameFile


def saveUDF(udf: np.ndarray, save_udf_file_path: str, overwrite: bool = False) -> bool:
    if os.path.exists(save_udf_file_path):
        if not overwrite:
            return True

        removeFile(save_udf_file_path)

    createFileFolder(save_udf_file_path)

    tmp_save_udf_file_path = save_udf_file_path[:-4] + "_tmp.npy"

    np.save(tmp_save_udf_file_path, udf)

    renameFile(tmp_save_udf_file_path, save_udf_file_path)
    return True


def loadUDF(udf_file_path: str) -> Union[np.ndarray, None]:
    if not os.path.exists(udf_file_path):
        print("[ERROR][io::loadUDF]")
        print("\t udf file not exist!")
        print("\t udf_file_path:", udf_file_path)
        return None

    udf = np.load(udf_file_path)

    return udf

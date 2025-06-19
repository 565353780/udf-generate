import os
import glob
import torch
from platform import system
from setuptools import find_packages, setup
from torch.utils.cpp_extension import CUDAExtension, CppExtension, BuildExtension


SYSTEM = system()

udf_lib_path = os.getcwd() + "/udf_generate/Lib/"
udf_root_path = os.getcwd() + "/udf_generate/Cpp/"
udf_src_path = udf_root_path + "src/"
udf_sources = glob.glob(udf_src_path + "*.cpp")
udf_include_dirs = [
    udf_lib_path + "libigl/include",
    "/usr/include/eigen3",
    "/opt/homebrew/include/eigen3",
    udf_root_path + "include",
]

udf_extra_compile_args = [
    "-O3",
    "-DCMAKE_BUILD_TYPE Release",
    "-D_GLIBCXX_USE_CXX11_ABI=0",
    "-DTORCH_USE_CUDA_DSA",
]

if SYSTEM == "Darwin":
    udf_extra_compile_args.append("-std=c++17")
elif SYSTEM == "Linux":
    udf_extra_compile_args.append("-std=c++17")

if torch.cuda.is_available():
    cc = torch.cuda.get_device_capability()
    arch_str = f"{cc[0]}.{cc[1]}"
    os.environ["TORCH_CUDA_ARCH_LIST"] = arch_str

    udf_sources += glob.glob(udf_src_path + "*.cu")

    extra_compile_args = {
        "cxx": udf_extra_compile_args
        + [
            "-DUSE_CUDA",
            "-DTORCH_USE_CUDA_DSA",
        ],
        "nvcc": [
            "-O3",
            "-Xfatbin",
            "-compress-all",
            "-DUSE_CUDA",
            "-std=c++17",
            "-DTORCH_USE_CUDA_DSA",
        ],
    }

    udf_module = CUDAExtension(
        name="udf_cpp",
        sources=udf_sources,
        include_dirs=udf_include_dirs,
        extra_compile_args=extra_compile_args,
    )

else:
    udf_module = CppExtension(
        name="udf_cpp",
        sources=udf_sources,
        include_dirs=udf_include_dirs,
        extra_compile_args=udf_extra_compile_args,
    )

setup(
    name="UDF-CPP",
    version="1.0.0",
    author="Changhao Li",
    packages=find_packages(),
    ext_modules=[udf_module],
    cmdclass={"build_ext": BuildExtension},
    include_package_data=True,
)

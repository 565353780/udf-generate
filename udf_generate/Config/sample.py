import open3d as o3d

from udf_generate.Method.samples import getSamplePointMatrix

SAMPLE_NUM = 256

SAMPLE_POINT_MATRIX = getSamplePointMatrix(SAMPLE_NUM)

SAMPLE_POINT_ARRAY = SAMPLE_POINT_MATRIX.reshape(-1, 3)

SAMPLE_POINT_CLOUD = o3d.geometry.PointCloud()
SAMPLE_POINT_CLOUD.points = o3d.utility.Vector3dVector(SAMPLE_POINT_ARRAY)

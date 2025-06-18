from udf_generate.Method.angle import toRad


def getGeometryBBox(geometry):
    bbox = geometry.get_axis_aligned_bounding_box()

    max_bound = bbox.get_max_bound()
    min_bound = bbox.get_min_bound()
    return min_bound, max_bound


def getGeometryBBoxCenter(geometry):
    min_bound, max_bound = getGeometryBBox(geometry)

    center = [
        (min_bound[0] + max_bound[0]) / 2.0,
        (min_bound[1] + max_bound[1]) / 2.0,
        (min_bound[2] + max_bound[2]) / 2.0,
    ]
    return center


def getGeometryBBoxDiff(geometry):
    min_bound, max_bound = getGeometryBBox(geometry)

    diff = [
        max_bound[0] - min_bound[0],
        max_bound[1] - min_bound[1],
        max_bound[2] - min_bound[2],
    ]
    return diff


def translateGeometry(geometry, z_diff=0.0, x_diff=0.0, y_diff=0.0):
    if z_diff == 0.0 and x_diff == 0.0 and y_diff == 0.0:
        return True

    geometry.translate((z_diff, x_diff, y_diff))
    return True


def rotateGeometry(geometry, z_angle=0.0, x_angle=0.0, y_angle=0.0):
    if z_angle == 0.0 and x_angle == 0.0 and y_angle == 0.0:
        return True

    z_rad = toRad(z_angle)
    x_rad = toRad(x_angle)
    y_rad = toRad(y_angle)

    R = geometry.get_rotation_matrix_from_xyz((z_rad, x_rad, y_rad))
    geometry.rotate(R, center=geometry.get_center())
    return True


def invRotateGeometry(geometry, z_angle=0.0, x_angle=0.0, y_angle=0.0):
    if z_angle != 0.0:
        z_rad = toRad(z_angle)
        R = geometry.get_rotation_matrix_from_xyz((-z_rad, 0.0, 0.0))
        geometry.rotate(R, center=geometry.get_center())
    if x_angle != 0.0:
        x_rad = toRad(x_angle)
        R = geometry.get_rotation_matrix_from_xyz((0.0, -x_rad, 0.0))
        geometry.rotate(R, center=geometry.get_center())
    if y_angle != 0.0:
        y_rad = toRad(y_angle)
        R = geometry.get_rotation_matrix_from_xyz((0.0, 0.0, -y_rad))
        geometry.rotate(R, center=geometry.get_center())
    return True


def scaleGeometry(geometry, scale=1):
    if scale == 1:
        return True

    geometry.scale(scale, center=geometry.get_center())
    return True


def normalizeGeometry(geometry):
    diff = getGeometryBBoxDiff(geometry)
    diff_max = max(diff)
    scaleGeometry(geometry, 1.0 / diff_max)

    bbox_center = getGeometryBBoxCenter(geometry)
    translateGeometry(geometry, -bbox_center[0], -bbox_center[1], -bbox_center[2])
    return True

import numpy as np


def toRad(angle: float) -> float:
    rad = angle * np.pi / 180.0
    return rad


def toAngle(rad: float) -> float:
    angle = rad * 180.0 / np.pi
    return angle

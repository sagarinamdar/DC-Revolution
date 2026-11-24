"""
Rigid-body spatial transformations and coordinate projection helpers for DC-Revolution.
Adheres strictly to the ISO 1151 right-handed datum coordinate standard.
"""

from typing import Tuple
import numpy as np


def create_translation_matrix(dx: float, dy: float, dz: float) -> np.ndarray:
    """Creates a 4x4 homogeneous translation matrix."""
    t_mat = np.eye(4, dtype=np.float64)
    t_mat[0, 3] = dx
    t_mat[1, 3] = dy
    t_mat[2, 3] = dz
    return t_mat


def create_rotation_matrix_xyz(roll_rad: float, pitch_rad: float, yaw_rad: float) -> np.ndarray:
    """
    Creates a 3x3 direction cosine rotation matrix for extrinsic XYZ rotations.
    """
    cx, sx = np.cos(roll_rad), np.sin(roll_rad)
    cy, sy = np.cos(pitch_rad), np.sin(pitch_rad)
    cz, sz = np.cos(yaw_rad), np.sin(yaw_rad)

    rx = np.array([[1.0, 0.0, 0.0], [0.0, cx, -sx], [0.0, sx, cx]], dtype=np.float64)
    ry = np.array([[cy, 0.0, sy], [0.0, 1.0, 0.0], [-sy, 0.0, cy]], dtype=np.float64)
    rz = np.array([[cz, -sz, 0.0], [sz, cz, 0.0], [0.0, 0.0, 1.0]], dtype=np.float64)

    return rz @ ry @ rx


def transform_points(points: np.ndarray, transform_matrix_4x4: np.ndarray) -> np.ndarray:
    """
    Applies a 4x4 homogeneous transformation matrix to an (N, 3) array of 3D points.
    """
    if points.ndim == 1:
        points = points.reshape(1, 3)
    n_pts = points.shape[0]
    homog_pts = np.hstack([points, np.ones((n_pts, 1), dtype=np.float64)])
    transformed = (transform_matrix_4x4 @ homog_pts.T).T
    return transformed[:, :3]

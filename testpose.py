import numpy as np
import os
import math
def ReturnOula(T):
    #根据T得出rx,ry,rz,tx,ty,tz
    R=T[:3,:3]
    rx,ry,rz=RTorxryrz(R)
    tx,ty,tz=T[0,3],T[1,3],T[1,3]
    return rx,ry,rz,tx,ty,tz
def pose_vec2mat(vec, rotation_mode='euler'):
    """
    Convert 6DoF parameters to transformation matrix.

    Args:s
        vec: 6DoF parameters in the order of tx, ty, tz, rx, ry, rz -- [B, 6]
    Returns:
        A transformation matrix -- [B, 3, 4]
    """
    translation = vec[:, :3].unsqueeze(-1)  # [B, 3, 1]
    rot = vec[:, 3:]
    if rotation_mode == 'euler':
        rot_mat = euler2mat(rot)  # [B, 3, 3]
    elif rotation_mode == 'quat':
        rot_mat = quat2mat(rot)  # [B, 3, 3]
    transform_mat = torch.cat([rot_mat, translation], dim=2)  # [B, 3, 4]
    return transform_mat
vec=np.array([0.0008898282560896466, -0.00014086114888360588 ,0.0026683749481627955, -0.0176657959348017 ,-0.11381199462249153 ,-0.11381199462249153])
print(vec.shape)
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/12/1 17:52
# @Author  : xelawk@gmail.com
# @FileName: test.py

import numpy as np
import open3d as o3d
from mesh2pcd import PcdSampler


def unit_test():
    mesh = o3d.io.read_triangle_mesh("assets/data/Tombstone1.obj")
    xyzs = np.asarray(mesh.vertices)
    nxyzs = np.asarray(mesh.vertex_normals)
    uvs = np.asarray(mesh.triangle_uvs)
    faces = np.asarray(mesh.triangles)

    # creating mesh_file and face_file self-defined
    mesh_file = "assets/data/mesh_file"
    face_file = "assets/data/face_file"

    with open(mesh_file, 'w') as f:
        for xyz, nxyz, uv in zip(xyzs, nxyzs, uvs):
            xyz_str = " ".join([str(x) for x in xyz.tolist()])
            nxyz_str = " ".join([str(x) for x in nxyz.tolist()])
            uv_str = " ".join([str(x) for x in uv.tolist()])
            data_str = [xyz_str, nxyz_str, uv_str]
            line = ','.join(data_str)
            f.write(line+'\n')

    with open("assets/data/face_file", 'w') as f:
        for face in faces:
            data = face.tolist()
            data_str = [str(x) for x in data]
            line = ' '.join(data_str)
            f.write(line+'\n')

    pcd_obj = PcdSampler(
        mesh_file=mesh_file,
        face_file=face_file,
        img_file="assets/data/Tombstone1_low.jpg"
    )
    pcd, colors = pcd_obj.sample_surface_even(100000)  # given sampling points you want
    pcd_obj.show_points_cloud(pcd, colors)  # show pointcloud wiht color sampling


if __name__ == '__main__':
    unit_test()

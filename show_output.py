import open3d as o3d

test_ply = o3d.io.read_point_cloud("output/RGB_10000000.ply")
o3d.visualization.draw_geometries([test_ply])
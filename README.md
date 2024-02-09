# 3D-point-cloud-generation
A Computer Vision project involving generation of a 3D point cloud using voxel reconstruction.

## Dataset
The input images, silhouettes and calibration parameters have been generated and made available by the Morpheo team at INRIA, Grenoble, France. 

## Methodology
To achieve a 3D point cloud, I followed these steps:

1. **Voxel Grid Definition:** I started by defining a voxel grid covering a specific volume around the subject. The dimensions and resolution of the grid were chosen based on my computer's memory capacity, ensuring efficient processing and development speed. Adjustments to the grid's resolution and volume were made as needed to optimize the balance between detail and performance.

2. **Visual Hull Construction:** Next, I labeled all voxels as empty and projected the center of each voxel onto all silhouette images. Only voxels whose projections fell within all silhouettes were labeled as occupied, forming the visual hull. I calculated the total number of voxels in the visual hull and their proportion relative to the entire grid.

3. **Surface Voxels Identification:** I identified surface voxels as those occupied voxels adjacent to at least one empty voxel. This step was crucial for distinguishing the object's surface within the visual hull. I reported the total number and proportion of surface voxels relative to the whole grid.

4. **PLY Point Cloud Output:** From the identified surface voxels, I generated a PLY point cloud by including the center point of each voxel face adjacent to an empty voxel. The output was formatted according to the PLY standard, with all points initially assigned the same color. I compared the number of points in the model to the number of surface voxels and explored the correlation between them.

5. **Textured PLY Point Cloud:** Finally, I added texture to the model by assigning color values based on the median RGB values of pixels from images where the voxel was visible and not occluded. Visibility from different camera perspectives was tested to ensure accurate texture mapping.

Throughout the project, I utilized various programming and computational geometry techniques to efficiently process the voxel grid, silhouette images, and generate the final 3D model. This approach allowed me to effectively reconstruct the scene from the provided data, combining technical skills with creative problem-solving.

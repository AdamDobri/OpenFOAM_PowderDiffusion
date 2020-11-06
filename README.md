# PowderDiffusionInOpenFOAM
Meshing (salome and gmsh) of the interparticle space and simulation of steady state diffusion using OpenFOAM

This folder contains the files necessary to generate meshes that represent
porous powders. Rectangualar prisim domains have hard spheres removed from and
the interparticle space is meshed using gmsh. The diffusivity can be determined
via "lapacianFOAM" solver simulations in OpenFOAM v5 (via blueCFD). Two methods
for the mesh generatation are presented, either gmsh or salome + gmsh.

This work was carried out with support from Grant Award Number 090118FD5313 
under the “Structure-Property Correlations in Multi-Scale Composites” 
project at Nazarbayev University. In the context of this project, these codes
are shared online.

%%%%%%%%%%%%%% General Overview %%%%%%%%%%%%%
Two different methods are used to generate the meshes:

Option A uses only gmsh to complete the boolean operations that remove the hard spheres 
from the matrix. This works for a few hundred particles, as gmsh cannot handle thousands
of boolean operations.

Option B uses salome to generate the geometries my making subgroups of a few hundred particles,
then subtracting those subgroups from the matrix. The geometry is exported as a *.brep file,
this can be read in gmsh and the mesh can be generated.

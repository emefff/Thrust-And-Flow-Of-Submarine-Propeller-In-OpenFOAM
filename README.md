# Thrust-And-Flow-Of-Submarine-Propeller-In-OpenFOAM
Modern submarines rely on efficient and silent propellers. To achieve these goals all measures are taken, from development of very special blade shapes to tailored alloys with increased vibration damping (like Sonoston). The question again is, can we use open-source software for simulation of the flow of such a propeller? Granted, OpenFOAM is not a 'click and run' type of CFD software, but with proper meshing and definition of rotating and static zone, this is even possible on limited hardware. 
There are many sayings in CFD, most of them imply the importance of the mesh for good results. When, like here, an AMI must be defined to catch all the effects, the mesh involves around 80% of the work of setting up the simulation. At first, we've tried CfMesh. It's a very good mesher with high stability but for some reason unknown to us, with multiple regions, we couldn't make it work. Even splitting the mesh in rotor and stator resulted in two meshes that had too many mismatching regions at the AMI borders. So again, we chose snappyHexMesh. Meshing with snappy was very tedious too, many iterations were needed but it was possible even without splitting and merging the mesh of rotating and static parts. In the end we found a mesh that worked for thousands of timesteps, but even that has turned out to be not entirely enough. Even the mesh shown below has led to 4 or 5 crashes over the whole simulation time of 2 seconds. With CFD you never know!
The geometry of the boat is a simplified version of an existing boat, propeller and diffuser were designed an experienced designer (the model of both propeller and diffuser can be downloaded from grabCAD). The experienced CFD engineer will immediately know that meshing of the whole boat with enough water body around it is crucial. The total length of 120m down to the details on propeller and diffuser (a few cm of resolution needed) is not an easy task, even if the mesh was static. And indeed, the needed AMI (arbitrary mesh interface) complicates this even further. There are a few compromises to be made:

-) we want to keep overall cell count low

-) we want to keep cell count at the AMI interface itself low

-) we need high detail at the propeller and diffuser

-) we need some detail on the edges of the boat

-) we need some detail before and after the AMI (like when sieving we need to get finer and finer, but have to allow some cells in every refinement step)

-) we have to stay away with the rotating geometry/patch from the borders of the AMI 

As always, the result could be better, but still around 50 iterations of the mesh were needed to make the simulation work. 


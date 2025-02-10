# Thrust-And-Flow-Of-Submarine-Propeller-In-OpenFOAM
Modern submarines rely on efficient and silent propellers. To achieve these goals all measures are taken, from development of very special blade shapes to tailored alloys with increased vibration damping (like Sonoston). The question again is, can we use open-source software for simulation of the flow of such a propeller? Granted, OpenFOAM is not a 'click and run' type of CFD software, but with proper meshing and definition of rotating and static zone, this is even possible on limited hardware. 
There are many sayings in CFD, most of them imply the importance of the mesh for good results. When, like here, an AMI must be defined to catch all the effects, the mesh involves around 80% of the work of setting up the simulation. At first, we've tried CfMesh. It's a very good mesher with high stability but for some reason unknown to us, with multiple regions, we couldn't make it work. Even splitting the mesh in rotor and stator resulted in two meshes that had too many mismatching regions at the AMI borders. So again, we chose snappyHexMesh. Meshing with snappy was very tedious too, many iterations were needed but it was possible even without splitting and merging the mesh of rotating and static parts. In the end we found a mesh that worked for thousands of timesteps, but even that has turned out to be not entirely enough. Even the mesh shown below has led to 4 or 5 crashes over the whole simulation time of 2 seconds. With CFD you never know!
The geometry of the boat is a simplified version of an existing boat, propeller and diffuser were designed an experienced designer (the model of both propeller and diffuser can be downloaded from grabCAD). The experienced CFD engineer will immediately know that meshing of the whole boat with enough water body around it is crucial. The total length of 120m down to the details on propeller and diffuser (a few cm of resolution needed) is not an easy task, even if the mesh was static. And indeed, the needed AMI (arbitrary mesh interface) complicates this even further. There are a few compromises to be made:

-) we want to keep overall cell count low

-) we want to keep cell count at the AMI interface itself low

-) we need high detail at the propeller and diffuser

-) we need some detail on the edges of the boat

-) we need some detail before and after the AMI (like when sieving we need to get finer and finer coming from the coarse mesh, but have to allow some cells in every refinement step)

-) we have to stay away with the rotating geometry/patch from the borders of the AMI 

As always, the result could be better, but still around 50 iterations of the mesh were needed to make the simulation work. In total, this mesh has aorund 3.6M cells. We think a lower cell count is probably not possible with the given parameters. The turning speed of the propeller was set at a constant 50rpm (5.236 rad/s). We use a transient simulation with pimpleFoam, this allows us to judge and see the development of the flow behind the turning propeller. Full simulation time is 2s, that is 1.66 rotations of the screw. At t=2s we still find that the flow behind the boat is not fully developed, so we still have to add a few revolutions, perhaps around 5 are enough. With deltaT = 1e-4s and writeInterval = 0.01s around 400GB of data are generated. One timeStep took about 11s, thus 20000 iterations in total took around 61 hours on 24 cores. OpenFOAM allows for calculating the forces and moment on the propeller patch, we can directly use these data for thrust and power calculations. In principle, the forces on the hull may be calculated in similar fashion directly in OpenFOAM to estimate the drag of the boat itself. Let's take a look at the basic setup and the stls used:

Overview of model for simualtion, inlet is at the left-hand side, outlet at the right (walls, inlet and outlet are set to transparent):
![Bildschirmfoto vom 2025-02-10 09-14-43](https://github.com/user-attachments/assets/762b047c-20b9-4457-8052-8d0411ee42d4)

Detail of propeller, diffuser and simplified rudders:
![Bildschirmfoto vom 2025-02-10 09-15-19](https://github.com/user-attachments/assets/77645da3-f229-4771-9541-a61d0cf5d6eb)

The inlet velocity is set to 1m/s to have some flow, the outlet is at constant pressure. A slice through the mesh in the interesting regions is shown below (basic mesh without boundary layers to keep it simple):
![Bildschirmfoto vom 2025-02-10 09-20-30](https://github.com/user-attachments/assets/f6c2545d-48da-4134-958e-4cdfa99fbe44)

Let's take a look at the pressure results behind the prop at t=2s. For a better understanding the boat is also shown:
![U_mag_stream_p_slices_t2](https://github.com/user-attachments/assets/1cdae970-b23d-4997-9083-122e7e3febf1)

The velocity componentent moving the boat is obviously Uz, let's visualize it:
![Uz_t2](https://github.com/user-attachments/assets/9b2b600a-a2b5-4842-9b0b-3d094506b004)

It's obvious, we need to give it more simulation time, but the results are more than satisfactory. So far we are getting around 4m/s with omega = 50rpm. In the repo, also a video of Uz over the whole 2s is shown.




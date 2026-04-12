# Gravitational Lensing Simulation (Alpha Version)

This project is an attempt to provide a visual aid to the study of gravitational lensing. The phenonmena of lensing in astrophysics is perhaps one of the most exciting, and *mind bending*, demonstrations of the consequences of General Relativity. Arthur Eddington, in 1920, published his observations based on the bending of light during a total solar eclipse in 1919. The results were the first novel prediction in Einstein's new gravitational regime. The deflection of light due to the presence of gravitational mass is truly exicting.

This current working proof-of-concept is an attempt to visualize the effects of gravitational lensing. Currently, the simulation provides a plot of source objects and their corresponding lensed images. The eventual aim of this project is to bring alive various lensing effects for students of General Relativity and astrophysics. 

# Installation

The current model runs using an entry `main.py` script. Once the full repo is locally pulled the script can be run using two modes, switched by modifying the `SIM_MODE` variable. The two modes are:

- `SIM_MODE = "image"`: this simulation mode uses the `image_ingest` module; a source field is built off of an imported image. Currently defined in the `/assets~ directory, astronomical images of source stars and galaxies can be lensed to demonstrate the approximate effect of macrolensing on known sources.

- `SIM_MODE = "image"`: this simulation mode uses the `source_objects` module. It takes a list of simulation objects, currently defined in the method `generate_demo_sourcelist()`. This provides a pseudo-sandbox mode. A user can define a list of source objects in a field (or by modifying `/models/source_objects.py` define more simulated astrophysical sources). 
 #
 # QTop
 #
 # Copyright (c) 2016 Jacob Marks (jacob.marks@yale.edu)
 #
 # This file is part of QTop.
 #
 # QTop is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.
import numpy as np
import sys
sys.path.append('../')
from src import common, simulation, error_models
sys.path.append('../src')
from decoders import rg
################## Surface Code Simulation ##################

path_to = str(sys.argv[1])
model = error_models.CodeCapacity()
decoder = rg.HDRG_decoder()
L_vals = [3,5,9,11,15]
p_vals = np.linspace(0.18,0.32,13)
num_trials = 10000
d = 5001
sim = simulation.simulation(d, 'Surface Code', [model, 'Code Capacity'], [decoder, 'RG'], path_to)
simulation.run(sim, L_vals, p_vals, num_trials)

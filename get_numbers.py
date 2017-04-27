###To run SKIRT on a selection of halos, you will need a list of the halo ID #'s. 
###These correspond to the halo ID in the pynbody database, sorted from most massive to least.
###Adjust the code below for your own criteria, or use what is here. 

import fnmatch
import os 
import pynbody
import tangos as db
import numpy as np
import sys


step = sys.argv[1] 
z = pynbody.load('/oasis/scratch/comet/mjt29/temp_project/Romulus25/cosmo25p.768sg1bwK1BHe75.' + str(step))
halos = z.halos(dosort=True)
sim = db.get_timestep('cosmo25%/%' + str(step))

numbers_pynbody = []
numbers_db = []

for i in range(len(halos)):
    dark = len(halos[i].dark)
    stars = len(halos[i].stars)
    gas = len(halos[i].gas)
    if (dark >= 100000) and (stars + gas >= 100000) and (gas >= 10000):
        numbers_pynbody.append(i)
    else:
        print 'halo ', halos[i], ' is not resolved.'
        continue

np.savetxt('num_' + str(step) + '.dat', numbers_pynbody)

'''
for j in range(len(sim.halos)):
    ndm = len(sim.halos[j].NDM)
    ngas = len(sim.halos[j].Ngas)
    nstars = len(sim.halos[j].Nstars)
    if (ndm >= 100000) and (nstars + ngas >= 100000) and (ngas >= 5000):
        numbers_db.append(j)
    else:
        continue
np.savetxt('database_numbers.dat', numbers_db)
'''

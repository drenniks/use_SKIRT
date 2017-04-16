###To run SKIRT on a selection of halos, you will need a list of the halo ID #'s. 
###These correspond to the halo ID in the pynbody database, sorted from most massive to least.
###I will also provide code to generate ID numbers from the database. 
###The database and pynbody should have the same halo numbers for each halo. The database may be faster.
###Adjust the code below for your own criteria, or use what is here. 
###The requirements below are that the halo must have at least 100,000 dark matter particles, at least 100,000 star and gas particles, and at least 5,000 gas particles.
###Output: a file titled '*_numbers.dat', which lists the halo numbers. There is one for pynbody and the database.

###python get_numbers.py step#
import fnmatch
import os 
import pynbody
import tangos as db
import numpy as np
import sys

#Load in pynbody data
step = sys.argv[1] 

for file in os.listdir('/oasis/scratch/comet/mjt29/temp_project/Romulus25/'):
    if fnmatch.fnmatch(file, '*' + str(step) + '*'):
        z = pynbody.load('/oasis/scratch/comet/mjt29/temp_project/Romulus25/cosmo25p.768sg1bwK1BHe75.' + str(step))
halos = z.halos(dosort=True)

#Load in simulation database
sim = db.get_timestep('cosmo25%/%' + str(step))

#Empty lists
numbers_pynbody = []
numbers_db = []

#Get numbers via pynbody for z
for i in range(len(halos)):
    dark = len(halos[i].dark)
    stars = len(halos[i].stars)
    gas = len(halos[i].gas)
    if (dark >= 100000) and (stars + gas >= 100000) and (gas >= 10000):
        numbers_pynbody.append(i)
    else:
        continue
np.savetxt('num_' + str(step) + '.dat', numbers_pynbody)

#Get numbers via the simulation database for z
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

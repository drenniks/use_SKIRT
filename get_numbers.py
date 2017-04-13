###To run SKIRT on a selection of halos, you will need a list of the halo ID #'s. 
###These correspond to the halo ID in the pynbody database, sorted from most massive to least.
###I will also provide code to generate ID numbers from the database. 
###The database and pynbody should have the same halo numbers for each halo. The database may be faster.
###Adjust the code below for your own criteria, or use what is here. 
###The requirements below are that the halo must have at least 100,000 dark matter particles, at least 100,000 star and gas particles, and at least 5,000 gas particles.
###Output: a file titled '*_numbers.dat', which lists the halo numbers. There is one for pynbody and the database.

import pynbody
import tangos as db
import numpy as np

#Load in pynbody data
z_2 = pynbody.load('/oasis/scratch/comet/mjt29/temp_project/Romulus25/cosmo25p.768sg1bwK1BHe75.001945')
halos_2 = z_2.halos(dosort=True)

#Load in simulation database
db_2 = db.get_timestep('cosmo25%/%1945')

#Empty lists
numbers_2_pynbody = []
numbers_2_db = []

#Get numbers via pynbody for z_2
for i in range(len(halos_2)):
    darkm = len(halos_2[i].dark)
    starsm = len(halos_2[i].stars)
    gasm = len(halos_2[i].gas)
    if (darkm >= 100000) and (starsm + gasm >= 100000) and (gasm >= 5000):
        numbers_2_pynbody.append(i)
    else:
        continue
np.savetxt('pynbody_numbers.dat', numbers_2_pynbody)

#Get numbers via the simulation database for z_2
'''
for j in range(len(db_2.halos)):
    ndm = len(db_2.halos[j].NDM)
    ngas = len(db_2.halos[j].Ngas)
    nstars = len(db_2.halos[j].Nstars)
    if (ndm >= 100000) and (nstars + ngas >= 100000) and (ngas >= 5000):
        numbers_2_db.append(j)
    else:
        continue
np.savetxt('database_numbers.dat', numbers_2_db)
'''

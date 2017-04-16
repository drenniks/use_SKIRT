###This will pull the necessary particle information from the simulation from pynbody.
###SKIRT needs (particular to Bruzual-Charlot): x position, y pos., z pos., smoothing length (pc), initial mass (solar masses), the metallicity (dimensionless), and the age (years)
import fnmatch
import os
import sys
import pynbody
import numpy as np
import gc

#Designate a single thread.
pynbody.config['number_of_threads'] = 1

#Load in the simulation data from pynbody, then the halos themselves.
step = sys.argv[1]

for file in os.listdir('/oasis/scratch/comet/mjt29/temp_project/Romulus25/'):
    if fnmatch.fnmatch(file, '*' + str(step) + '*'):
        sim = pynbody.load('/oasis/scratch/comet/mjt29/temp_project/Romulus25/cosmo25p.768sg1bwK1BHe75.' + str(step))
halos = sim.halos(dosort=True)

#Load in the numbers pulled via the 'get_numbers.py' script.
numbers = np.loadtxt('num_' + str(step) + '.dat')

#Cycle through the halos pulling relevent particle information and print it to a single text file for each individual halo.
for i in numbers:
    try:
        #Load halo and center faceon
        hn = halos.load_copy(i)
        hn.physical_units()
        stars = hn.stars[hn.stars['tform'] >=0.] #Excludes blackholes.
        pynbody.analysis.angmom.faceon(hn)
    
        #Load properties
        x = stars['x'].in_units('pc')
        y = stars['y'].in_units('pc')
        z = stars['z'].in_units('pc')
        h = stars['smooth'].in_units('pc')
        mass = np.zeros(len(x)) + 42416.4033
        metals = stars['metals']
        age = stars['age'].in_units('yr')
        allarrays = np.vstack((x, y, z, h,  mass, metals, age)).T
        
        #Save txt file with star data for each halo
        np.savetxt('particle_data/stars_' + str(step) + '_' + str(i) + '.dat', allarrays, delimiter=' ', fmt = '%1.6f')
        del hn
        gc.collect()

    #If a Value Error arises, print a statement and the halo number. The halo will not be included.
    except ValueError as e:
        print(e)
        pass

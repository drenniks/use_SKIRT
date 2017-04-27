import fnmatch
import os
import sys
import pynbody
import numpy as np
import gc

pynbody.config['number_of_threads'] = 1

step = sys.argv[1]

sim = pynbody.load('/oasis/scratch/comet/mjt29/temp_project/Romulus25/cosmo25p.768sg1bwK1BHe75.' + str(step))
halos = sim.halos(dosort=True)

numbers = np.loadtxt('num_' + str(step) + '.dat')

for i in numbers:
    try:
        hn = halos.load_copy(i)
        hn.physical_units()
        stars = hn.stars[hn.stars['tform'] >=0.]
        pynbody.analysis.angmom.faceon(hn)
    
        x = stars['x'].in_units('pc')
        y = stars['y'].in_units('pc')
        z = stars['z'].in_units('pc')
        h = stars['smooth'].in_units('pc')
        mass = np.zeros(len(x)) + 42416.4033
        metals = stars['metals']
        age = stars['age'].in_units('yr')
        allarrays = np.vstack((x, y, z, h,  mass, metals, age)).T
        
        np.savetxt('particle_data/stars_' + str(step) + '_' + str(i) + '.dat', allarrays, delimiter=' ', fmt = '%1.6f')
        del hn
        gc.collect()

    except ValueError as e:
        print(e)
        print 'halo ', i, ' failed'
        pass

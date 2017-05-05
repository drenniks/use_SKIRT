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

numbers = np.loadtxt('../num_' + str(step) + '.dat')

for i in range(len(numbers)):
    try:
        hn = halos.load_copy(numbers[i])
        hn.physical_units()
        pynbody.analysis.angmom.faceon(hn)

        x = hn.gas['x'].in_units('pc')
        y = hn.gas['y'].in_units('pc')
        z = hn.gas['z'].in_units('pc')
        h = hn.gas['smooth'].in_units('pc')
        mass = hn.gas['mass'].in_units('Msol')
        metals = hn.gas['metals']
        temp = hn.gas['temp'].in_units('K')
        allarrays = np.vstack((x, y, z, h,  mass, metals, temp)).T

        np.savetxt('gas_' + str(step) + '_' + str(numbers[i]) + '.dat', allarrays, delimiter=' ', fmt = '%1.6f')
        del hn
        gc.collect()

    except ValueError as e:
        print(e)
        print 'halo ' , i, ' failed'
        pass

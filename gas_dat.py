###This will pull the necessary particle information from the simulation from pynbody. 
###SKIRT needs: x position, y pos., z pos., smoothing length (pc), mass (solar masses), the metallicity (dimensionless), and the gas temperature (kelvin)

import pynbody
import numpy as np
import gc

#Designate a single thread.
pynbody.config['number_of_threads'] = 1

#Load in the simulation data from pynbody, then the halos themselves.
sim = pynbody.load('/oasis/scratch/comet/mjt29/temp_project/Romulus25/cosmo25p.768sg1bwK1BHe75.001945')
halos = sim.halos(dosort=True)

#Load in the numbers pulled via the 'get_numbers.py' script.
numbers = np.loadtxt('pynbody_numbers.dat')

#Cycle through the halos pulling relevent particle information and print it to a single text file for each individual halo.
for i in range(len(numbers)):
    try:
        #Load halo and center faceon
        hn = halos.load_copy(numbers[i])
        hn.physical_units()
        pynbody.analysis.angmom.faceon(hn)

        #Load properties
        x = hn.gas['x'].in_units('pc')
        y = hn.gas['y'].in_units('pc')
        z = hn.gas['z'].in_units('pc')
        h = hn.gas['smooth'].in_units('pc')
        mass = hn.gas['mass'].in_units('Msol')
        metals = hn.gas['metals']
        temp = hn.gas['temp'].in_units('K')
        
        #Check if the halo has less than 10,000. If it does, print a notice. These halos will not be included (I could skip this by adding it into the get_numbers.py
        if len(hn.gas) < 10000:
            print 'Number of gas particles in halo ', numbers[i] , ' = ', len(hn.gas)
            continue 
        
        allarrays = np.vstack((x, y, z, h,  mass, metals, temp)).T
        #Save txt file with gas data for each halo
        np.savetxt('particle_data/gas_' + str(numbers[i]) + '.dat', allarrays, delimiter=' ', fmt = '%1.6f')
        del hn
        gc.collect()

    #If a Value Error arises, print a statement and the halo number. The halo will not be included. 
    except ValueError:
        print 'not enough gas in halo ', numbers[i], '!'
        pass
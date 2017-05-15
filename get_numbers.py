import config
import fnmatch
import os 
import pynbody
import numpy as np
import sys

step = config.step_number
z = pynbody.load(config.sim_location)
halos = z.halos(dosort=True)

numbers_pynbody = []
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

###This will create a images_faceon_*.ski file for every halo for SKIRT to run on.

import fileinput
import sys
from shutil import copyfile
import gc
import numpy as np

#Load pynbody halo numbers
step = sys.argv[1]
numbers = np.loadtxt('num_' + str(step) + '.dat')

#Generate the files in the 'run' folder.
for i in range(len(numbers)):
    copyfile('images.ski', 'run/images_' + str(step) + '_' + str(numbers[i]) + '.ski')
    for line in fileinput.input('run/images_'+ str(step) + '_' + str(numbers[i]) +'.ski', inplace=1):
        if 'stars_#.dat' in line:
            line = line.replace('stars_#.dat', 'particle_data/stars_' + str(step) + '_' + str(numbers[i]) + '.dat')
        sys.stdout.write(line)
        del line
        gc.collect()

    for line in fileinput.input('run/images_'+ str(step) + '_' + str(numbers[i]) +'.ski', inplace=1):
        if 'gas_#.dat' in line:
            line = line.replace('gas_#.dat', 'particle_data/gas_' + str(step) + '_' + str(numbers[i]) + '.dat')
        sys.stdout.write(line)
        del line
        gc.collect()

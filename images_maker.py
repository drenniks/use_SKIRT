###This will create a images_faceon_*.ski file for every halo for SKIRT to run on.

import fileinput
import sys
from shutil import copyfile
import gc

#Load pynbody halo numbers
numbers = np.loadtxt('pynbody_numbers.dat')

#Generate the files in the 'run' folder.
for i in range(len(numbers)):
    copyfile('images_faceon.ski', 'run/images_faceon_' +str(numbers[i])+ '.ski')
    for line in fileinput.input('run/images_faceon_'+str(numbers[i])+'.ski', inplace=1):
        if 'stars_#.dat' in line:
            line = line.replace('stars_#.dat', 'stars_' +str(numbers[i])+ '.dat')
        sys.stdout.write(line)
        del line
        gc.collect()

    for line in fileinput.input('run/images_faceon_'+str(numbers[i])+'.ski', inplace=1):
        if 'gas_#.dat' in line:
            line = line.replace('gas_#.dat', 'gas_' +str(numbers[i])+ '.dat')
        sys.stdout.write(line)
        del line
        gc.collect()

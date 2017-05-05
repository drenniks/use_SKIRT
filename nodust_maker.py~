import fileinput
import sys
from shutil import copyfile
import gc
import numpy as np

step = sys.argv[1]
numbers = np.loadtxt('../num_' + str(step) + '.dat')

for i in range(len(numbers)):
    copyfile('nodust.ski', 'nodust_' + str(step) + '_' + str(numbers[i]) + '.ski')
    for line in fileinput.input('nodust_'+ str(step) + '_' + str(numbers[i]) +'.ski', inplace=1):
        if 'stars_#.dat' in line:
            line = line.replace('stars_#.dat', '../particle_data/stars_' + str(step) + '_' + str(numbers[i]) + '.dat')
        sys.stdout.write(line)
        del line
        gc.collect()        

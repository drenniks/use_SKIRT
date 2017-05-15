import config
import fileinput
import sys
from shutil import copyfile
import gc
import numpy as np

step = config.step_number
numbers = np.loadtxt('num_' + str(step) + '.dat')

for i in range(len(numbers)):
    copyfile('run/nodust.ski', 'run/nodust_' + str(step) + '_' + str(numbers[i]) + '.ski')
    for line in fileinput.input('run/nodust_'+ str(step) + '_' + str(numbers[i]) +'.ski', inplace=1):
        if 'stars_#.dat' in line:
            line = line.replace('stars_#.dat', 'particle_data/stars_' + str(step) + '_' + str(numbers[i]) + '.dat')
        sys.stdout.write(line)
        del line
        gc.collect()     

    for line in fileinput.input('run/nodust_'+ str(step) + '_' + str(numbers[i]) +'.ski', inplace=1):
        if 'minWavelength="0.1 micron"' in line:
            line = line.replace('minWavelength="0.1 micron"', 'minWavelength="' + config.min_wavelength + '"')
        sys.stdout.write(line)
        del line
        gc.collect()

    for line in fileinput.input('run/nodust_'+ str(step) + '_' + str(numbers[i]) +'.ski', inplace=1):
        if 'maxWavelength="1000 micron"' in line:
            line = line.replace ('maxWavelength="1000 micron"', 'maxWavelength="' + config.max_wavelength + '"')
        sys.stdout.write(line)
        del line
        gc.collect()

    for line in fileinput.input('run/nodust_'+ str(step) + '_' + str(numbers[i]) +'.ski', inplace=1):
        if 'points="3000"' in line:
            line = line.replace('points="3000"', 'points="' + config.points + '"')
        sys.stdout.write(line)
        del line
        gc.collect()

    for line in fileinput.input('run/nodust_'+ str(step) + '_' + str(numbers[i]) +'.ski', inplace=1):
        print line,
        if line.startswith('        <instruments type="Instrument">'):
            for j in np.arange(int(config.detector_count)):
                print '          <SEDInstrument instrumentName="'+config.names[j]+'" distance="'+config.distances[j]+'" inclination="'+config.inclinations[j]+'" azimuth="'+config.azimuths[j]+'" positionAngle="'+config.positionAngles[j]+'"/>'   

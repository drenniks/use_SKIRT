import config
import fileinput
import sys
from shutil import copyfile
import gc
import numpy as np

step = config.step_number
numbers = np.loadtxt('num_' + str(step) + '.dat')

for i in range(len(numbers)):
    copyfile('run/images.ski', 'run/images_' + str(step) + '_' + str(numbers[i]) + '.ski')
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

    for line in fileinput.input('run/images_'+ str(step) + '_' + str(numbers[i]) +'.ski', inplace=1):
        if '"0.365 micron, 0.551 micron, 0.806 micron"' in line:
            list = ', '.join(config.wavelengths)
            line = line.replace('"0.365 micron, 0.551 micron, 0.806 micron"', '"'+list+'"')
        sys.stdout.write(line)
        del line
        gc.collect()

    for line in fileinput.input('run/images_'+ str(step) + '_' + str(numbers[i]) +'.ski', inplace=1):
        print line,
        if line.startswith('        <instruments type="Instrument">'):
            for j in np.arange(int(config.detector_count)):
                print '          <FrameInstrument instrumentName="'+config.names[j]+'" distance="'+config.distances[j]+'" inclination="'+config.inclinations[j]+'" azimuth="'+config.azimuths[j]+'" positionAngle="'+config.positionAngles[j]+'" pixelsX="'+config.pixelsX+'" pixelsY="'+config.pixelsY+'" fieldOfViewX="'+config.fieldOfViewX+'" fieldOfViewY="'+config.fieldOfViewY+'"/>'

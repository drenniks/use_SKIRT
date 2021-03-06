import config
import sys
import gc
import fileinput 
from shutil import copyfile 
import numpy as np

step = config.step_number
numbers = np.loadtxt('num_' + str(step) + '.dat')

for i in range(len(numbers)):
    copyfile('submit/skirt_example_images.sh', 'submit/images_' + str(step) + '_' + str(numbers[i]) + '.sh')
    for line in fileinput.input('submit/images_' + str(step) + '_' + str(numbers[i]) + '.sh', inplace = 1):
        if 'images_faceon_0.ski' in line:
            line = line.replace('images_faceon_0.ski', 'run/images_' + str(step) + '_' + str(numbers[i]) + '.ski')
        sys.stdout.write(line)
        del line
        gc.collect()

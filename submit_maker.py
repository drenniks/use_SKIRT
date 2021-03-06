import config
import sys
import gc
import fileinput 
from shutil import copyfile 
import numpy as np

step = config.step_number
numbers = np.loadtxt('num_' + str(step) + '.dat')

for i in range(len(numbers)):
    copyfile('submit/skirt_example.sh', 'submit/skirt_' + str(step) + '_' + str(numbers[i]) + '.sh')
    for line in fileinput.input('submit/skirt_' + str(step) + '_' + str(numbers[i]) + '.sh', inplace = 1):
        if 'Zubko_0.ski' in line:
            line = line.replace('Zubko_0.ski', 'Zubko_' + str(step) + '_' + str(numbers[i]) + '.ski')
        sys.stdout.write(line)
        del line
        gc.collect()

    for line in fileinput.input('submit/skirt_' + str(step) + '_' + str(numbers[i]) + '.sh', inplace = 1):
        if 'nodust_0.ski' in line:
            line = line.replace('nodust_0.ski', 'nodust_' + str(step) + '_' + str(numbers[i]) + '.ski')
        sys.stdout.write(line)
        del line
        gc.collect()
    
    for line in fileinput.input('submit/skirt_' + str(step) + '_' + str(numbers[i]) + '.sh', inplace = 1):
        if 'skirt_halo' in line:
            line = line.replace('skirt_halo', 'skirt_' + str(step) + '_' + str(numbers[i]) + '.ski')
        sys.stdout.write(line)
        del line
        gc.collect()

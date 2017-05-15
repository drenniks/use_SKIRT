import config
import numpy as np
import sys

step = config.step_number
numbers = np.loadtxt('num_' + str(step) + '.dat')

f = open('submit_images.sh','a')
f.write('#!/bin/bash \n')
f.write('#SBATCH --job-name="submit_all_images" \n')
f.write('#SBATCH --output="submit_all_images.%j.%N.out" \n')
f.write('#SBATCH --partition=compute \n')
f.write('#SBATCH --nodes=1 \n')
f.write('#SBATCH --ntasks-per-node=1 \n')
f.write('#SBATCH --export=ALL \n')
f.write('#SBATCH -t 00:20:00 \n')

for i in range(len(numbers)):
    f = open('submit_images.sh','a')
    f.write('sbatch submit/images_' + str(step) + '_' +str(numbers[i]) + '.sh' + '\n')
    f.close()

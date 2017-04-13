###This file will create a master submit file for the images.

import numpy as np

numbers = np.loadtxt('pynbody_numbers.dat')

f = open('submit_images.sh','a')
f.write('#!/bin/bash \n')
f.write('#SBATCH --job-name="submit_all_images" \n')
f.write('#SBATCH --output="submit_all_images.%j.%N.out" \n')
f.write('#SBATCH --partition=compute \n')
f.write('#SBATCH --nodes=1 \n')
f.write('#SBATCH --ntasks-per-node=1 \n')
f.write('#SBATCH --export=ALL \n')
f.write('#SBATCH -t 00:20:00 \n')
f.write('#SBATCH --mail-type=END,FAIL \n')
f.write('#SBATCH --mail-user=daniellerenniks@gmail.com \n')

for i in range(len(numbers)):
    f = open('submit_images.sh','a')
    f.write('sbatch submit/images_' + str(numbers[i]) + '.sh' + '\n')
    f.close()

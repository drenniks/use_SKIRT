#!/bin/bash
#SBATCH --job-name="numbers"
#SBATCH --output="numbers.%j.%N.out"
#SBATCH --partition=debug
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --export=ALL
#SBATCH -t 00:30:00
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=daniellerenniks@gmail.com

module load python
module load scipy
cd $SLURM_SUBMIT_DIR

python get_numbers.py 008192
 
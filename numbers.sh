#!/bin/bash
#SBATCH --job-name="numbers"
#SBATCH --output="numbers.%j.%N.out"
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --export=ALL
#SBATCH -t 48:00:00

module load python
module load scipy
cd $SLURM_SUBMIT_DIR

python get_numbers.py
 
#!/bin/bash
#SBATCH --job-name="skirt_halo"
#SBATCH --output="skirt_halo.%j.%N.out"
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --export=ALL
#SBATCH -t 25:00:00
#SBATCH --mail-type=END,FAIL

module load python
module load scipy
cd $SLURM_SUBMIT_DIR


/home/u14266/src/SKIRT/release/SKIRTmain/skirt run/Zubko_0.ski

/home/u14266/src/SKIRT/release/SKIRTmain/skirt run/nodust_0.ski
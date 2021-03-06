#!/bin/bash
#SBATCH --job-name="multi_images"
#SBATCH --output="multi_images.%j.%N.out"
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --export=ALL
#SBATCH -t 00:20:00
#SBATCH --checkpoint-dir=outputs

module load python
module load scipy
cd $SLURM_SUBMIT_DIR

/home/u14266/src/SKIRT/release/SKIRTmain/skirt images_faceon_0.ski




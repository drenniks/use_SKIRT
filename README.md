# Use SKIRT on Comet
Run SKIRT on many different halos at once. See the companion [documentation](https://docs.google.com/document/d/1t1_jGyQKJ_RiFOV3Mu_I850_acKTB7qFlnFJ3rdz5g0/edit?usp=sharin) for more details.

Steps (here STEP = step number with six numbers, ex. 008192, 000909):
1. `git clone https://github.com/drenniks/use_SKIRT.git STEP`
2. Add STEP to numbers.sh
3. `sbatch numbers.sh`
4. Add STEP number to particle.sh
5. `sbatch particle.sh`
6. `python create.py STEP`
7. `sbatch submit_images.sh`
8. `sbatch submit.sh`

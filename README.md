# use_SKIRT
Run SKIRT on many different halos at once!
https://docs.google.com/document/d/1t1_jGyQKJ_RiFOV3Mu_I850_acKTB7qFlnFJ3rdz5g0/edit?usp=sharing

Steps (here STEP = step number with six numbers, ex. 008192, 000909):
1. git clone https://github.com/drenniks/use_SKIRT.git STEP
2. add step numbers to numbers.sh
3. sbatch numbers.sh
4. add step number to particle.sh
5. sbatch particle.sh
6. python Zubko_maker.py STEP
7. python nodust_maker.py STEP
8. python images_maker.py STEP
9. python images_submit_maker.py STEP
10. python submit_maker.py STEP
11. python master_images_submit.py STEP
12. python master_submit.py STEP
13. sbatch submit_images.sh
14. sbatch submit.sh

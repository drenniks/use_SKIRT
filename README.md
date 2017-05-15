# Use SKIRT on Comet
Steps:
1. `git clone https://github.com/drenniks/use_SKIRT.git STEP`
2. Adjust the parameters in the config.py file
3. `sbatch numbers.sh` (This will print a batch job number, copy and paste this number into the line below. JobID)
5. `sbatch --dependency=afterok:JobID particle.sh`
6. `python create.py` (This can only be done one numbers.sh has completed)
Once particle.sh has completed, submit the .sh files below to run SKIRT.
7. `sbatch submit_images.sh`
8. `sbatch submit.sh`

Run SKIRT, a radiative transfer code, on the Romulus25 simulation for many halos at once. Produce spectral energy distributions and images at your choice of wavelengths. The beginning of this is general information related to SKIRT. The documentation associated with the use_SKIRT git repo comes after.

### Installing/Verifying SKIRT
Follow the [hyperlink](http://www.skirt.ugent.be/skirt/_installation_guide.html) for instructions about how to install and verify SKIRT on your computer.

SKIRT is installed already on Comet and is the one that I use throughout this process (executable: /home/u14266/src/SKIRT/release/SKIRTmain/skirt). This belongs to Tom Quinn and is version 7.0. Everything in this document is for version 7.0 (https://github.com/SKIRT/SKIRT7). (Check back for 8.0 soon)

### Running SKIRT - Tutorial
Once SKIRT is installed, there are a few tutorials provided by the SKIRT developers that are useful to go through to understand how SKIRT works. Their tutorials can be found [here](http://www.skirt.ugent.be/tutorials/_tutorial_basics_mono.html). There may be a few differences in the query questions since they are referencing version 8.0, but it should be largely the same.

### Using SPH output files - Formatting
In order to run SKIRT on SPH output files, the data needs to be put into a format SKIRT can read. SKIRT needs two files: stellar particle data and gas particle data.

The format for the stellar particle data can be found [here](http://www.skirt.ugent.be/skirt/class_s_p_h_stellar_comp.html#a8a1d1564e85e99835f5fbdba98117022).

The format for the gas particle data can be found [here](http://www.skirt.ugent.be/skirt/class_s_p_h_dust_distribution.html#a964174a920512ff57421d8d7bcb223a3).

### Visualizing Results - PTS
SKIRT comes with a nice package called the Python Tool Kit (PTS) which allows you to visualize the data from the outputs of SKIRT quickly and with ease. It can be installed via this [link](http://www.skirt.ugent.be/pts/_installation_guide.html). 

To generate the images and SEDs in my process below, you will need PTS to plot the data (or you can plot it yourself!). 

## use_SKIRT Documentation
This repository is set up so that you can set the parameters and values that you want in the config.py file to run SKIRT. The current Romulus25 simulations are located on Comet, courtesy of Michael Tremmel,  here: `/oasis/scratch/comet/mjt29/temp_project/Romulus25`. If something doesn't appear to be working properly, please email me, Danielle Skinner, at daniellerenniks@gmail.com for any questions you may have.



The config file is where you can adjust the parameters of the radiative transfer simulations. There is a section for the SED instrument and a section for the image Frame instrument. The config file is alread filled out to show how the parameters should be set. I will comment on each parameter below. The following are parameters for simulating radiative transfer and producing SEDs:
- `step_number`: the particular step number you are analyzing (in general this can be a name for this SKIRT run that you are doing).
-`sim_location`: path to the sph output
-`detector_count`: the number of detectors you want to use. It is currently set at 2 detectors. You will need one detector for each position you want to "observe" the halo at.
-`names`: these are the names of the detectors, they will end up in your output labels. The SKIRT developers label them 'i90' or 'i00', according to the inclination.
-`distances`: distance from the halo to the detector. It is currently set at 10 Megaparsecs for each detecor.
-`inclinations`: the inclination of each detector with repect to the halo, set at 0 degrees (faceon) and 90 degrees (sideon).
-`azimuths`: the azimuth of each detector with respect to the halo, set at 0 degrees for both detectors.
-`positionAngles`: the position angles of each detector, set at 0 degrees for both detectors.
-`min_wavelength`: the minimum wavelength of the observed spectrum, set at 0.1 micron.
-`max_wavelength`: the maximum wavelength of the observed spectrum, set at 1000 mciron.
-`points`: resolution of the wavelength grid, set at 100 grid points. This can be increased for finer resolution. 

The following parameters are for running radiative transfer and producing images of the halos:
-`frame count`: the number of frame detectors you want to use. It is set at 2 detectors. You will need one for each position you want to "observe" the halo at.
-`names_img`: like `names` above but for the image simulation.
-`distances_img`: like `distances` above
-`inclinations_img`: like `inclinations` above
-`azimuths_img`: like `azimuths` above
-`positionAngles_img`: like `positionAngles` above
-`pixelsX`: the dimension of the x-axis in pixels for the final image. It is currently set at 600.
-`pixelsY`: the dimension of the y-axis in pixels for the final image. It is set at 600.
-`fieldOfViewX`: the dimension of the field of view in the x direction for the frame, set at 40,000 parsecs.
-`fieldOfViewY`: the dimension of the field of view in the y direction for the frame, set at 40,000 parsecs. 
-`wavelengths`: the desired wavelengths of the image. Currently set at red, green and blue.

These parameters will produce faceon and side SEDs between 0.1 micron and 1000 microns from 10 Mpc away. They will also produce RGB, faceon and sideon images at 10 Mpc away for each halo. 

Once you have set the parameters to your liking, you need a list of halos you want to observe. The files numbers.sh and get_numbers.py will do this. Currently, get_numbers.py is set up to grab all of the resolved halos which have at least 100,000 dark matter particles, 100,000 gas and star particles, and at least 10,000 gas particles. Get_numbers.py creates a num_STEP.dat file (where STEP is the step number you are looking at) which simply contains the pynbody halo id (ordered by halo mass) of each halo. 

Submit the numbers.sh file by typing `sbatch numbers.sh`. This will print a batch job number. Copy this number. Once you have the number file, particle.sh, gas_dat.py and stars_dat.py will generate the particle data for each halo in the particle_data directory. You can submit particle.sh right after you submit the numbers.sh file by typing `sbatch --dependency=afterok:JobID particle.sh`, where JobID is the batch job number you copied earlier from submitting numbers.sh. The `--dependency` simply tells the scheduling system to submit particle.sh once numbers.sh has completed. These particle files are specifically for the Bruzual-Charlot SED family. If you wish to use a different family, you will have to adjust the gas_dat.py and stars_dat.py files to match SKIRTs necessary output.

Next the simulation files (.ski) and submission files (.sh) need to be created for each halo. The script called "create.py" will do just this. Simply type `python create.py` and the directories run/ and submit/ will be filled with .ski files and .sh files, respectively, for each halo. "submit.sh" and "submit_images.sh" are the master submit files and are the last files that need to be submitted. If you type `squeue -u` followed by your username, copy and paste the job ID number associated with particle.sh that you previously submitted. Submit "submit.sh" and "submit_images.sh"  using the dependency keyword again: `sbatch --dependency=afterok:jobID submit.sh` and `sbatch --dependency=afterok:jobID submit_images.sh`. This will submit the SKIRT simulations after the particle data has been created. 

Once all of the halos have completed running, type `pts plotseds` and `pts makergb` to create SEDs and RGB images for each halo. Other outputs are explained in the official SKIRT tutorials.

### Possible Errors
A possible error may come up when you are generating the particle files. Sometimes, a halo doesn’t have enough particles for the pynbody to center on the halo. If you type the command ‘grep ‘Could not open’ *.out’ it will print all the locations where SKIRT could not open the necessary particle files, since they do not exist. I would recommend removing these halo numbers from you num.dat file.

I have found that on the largest halos in Romulus, I have had to run them on the large-shared partition with 1000 Gbs of memory. The time it takes will vary depending on your parameters.
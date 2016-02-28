# makeCMSSWCrabConfigs
# generates CMSSW config and CRAB configs for one mass point (several seeds)
# by replacing mass and seed strings in template files:
# the string '<mSTOP>' is changed to mSTOP
# <mNLSP>, <mLSP>, <seed> similarly
# output files placed in own directory, renamed with seed
#
# future -- discover seeds in filenames, typically the only 5 digit string in filename

import sys 
import os 
import subprocess

templates = ["crabSubmitStep1Template.py", "submitStep1Template_cfg.py",
             "crabSubmitStep2Template.py", "submitStep2Template_cfg.py", 
             "crabSubmitStep3Template.py", "submitStep3Template_cfg.py"]
#change seeds and masses
seeds = [41718, 43487, 49191, 51509, 54323, 54577, 58147]
mSTOP = 500
mNLSP = 250
mLSP = 1
#seeds = [36280, 60676, 55383, 50631, 37358, 60178, 53294]
#mSTOP = 550
#mNLSP = 275
#mLSP = 1

# make output dir for the configs for this mass point
directory = "mSTOP" + str(mSTOP) + "_mNLSP" + str(mNLSP) + "_mLSP" + str(mLSP)
if not os.path.exists(directory):
  os.makedirs(directory)

# for each seed
#   for each template file
#     execute sed on template files to produce output files

for iSeed, seed in enumerate(seeds):
  for iTemplate, templateFile in enumerate(templates):
    with open(templateFile, "r" ) as source:
      with open(directory+'/'+str(seed)+'_'+templateFile.replace('Template',""), "w" ) as target:
        data = source.read()
        #replace seed and masses       
        changed = data.replace('<seed>', str(seed))
        changed = changed.replace('<mLSP>', str(mLSP))
        changed = changed.replace('<mNLSP>', str(mNLSP))
        changed = changed.replace('<mSTOP>', str(mSTOP))
        target.write(changed)

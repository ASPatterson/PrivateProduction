# Private production
Private production of SUSY samples, centered on T2bW Fastsim made in Feb 2016.
Includes Fullsim instructions and files (the new Fastsim scripts in this repo would also help out) Full_Fastsim.instructions.txt and the Fullsim attachments tarball.

## LHE and LHE decay:
See Full_Fastsim.instructions.txt to find then decay LHE files (ie inject them with desired decays, branching fractions, and masses). Follows this github tutorial closely (which also shows how to generate LHE files):

https://github.com/CMS-SUS-XPAG/GenLHEfiles/blob/master/Run2Mechanism/README.md

## LHE to miniAODv2:
For my *.sh scripts run 'source X.sh', and for *.py run 'python X.py'. Look over and defuse bash scripts before running, they're dangerous in some places (eg 'for i in $(ls *)')

First use makeCmsDriver*, to initialize the CMSSW repos necessary for CRAB, and to generate the basic cmssw scripts, *_cfg.py, using cmsDriver commands. 

Edit the *_cfg.py to make template scripts (see *Template*_cfg.py), valid for any mass point

Edit the two template scripts (one each for cmssw & crab) as necessary for white/blacklists, events/job, filein and fileout. Careful not to forget to whitelist T2_US_* if you must.

Run makeCMSSWCrabConfigs.py for (all steps and) a specific mass point to generate crab (crabSubmit*.py) and cmssw (submit*_cfg.py) scripts

Run batchCrab.sh for a specific step and mass point (remember to voms-proxy-init [see below], and to first cmsenv inside the correct CMSSW directory [see makeCmsDriver* to determine which]) to submit jobs to crab

Check status at dashboard url [0], delay is typically < 30 minutes, or via 'crab status <projectDir>'

Between steps, and for each mass point, run makeJobRootLists.sh to generate a txt listing of roots outputted from (successful) previous step's jobs. Used as input to next step. See eg input settings in crabSubmitStep2Template.py.

Submit next step using batchCrab again. 

After last step, ntuplize (yes, there are eg 100 files per mass point from last step)

## Useful commands
to cmsenv in correct CMSSW repo

source  /afs/cern.ch/cms/cmsset_default.sh

source /cvmfs/cms.cern.ch/crab3/crab.sh

voms-proxy-init --voms cms --valid 168:00

[0]
http://dashb-cms-job.cern.ch/dashboard/templates/task-analysis

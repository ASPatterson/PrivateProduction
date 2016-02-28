# T2bW-Fastsim-privateprod
Private production of SUSY T2bW Fastsim samples

## To do private production:
For *.sh run 'source X.sh', and for *.py run 'python X.py'

makeCmsDriver*, to initialize the CMSSW repos necessary for CRAB, and to generate the basic cmssw scripts, *_cfg.py

Edit the *_cfg.py to make template scripts (see *Template*_cfg.py), valid for any mass point

Edit the two template scripts (two per step, cmssw & crab) as necessary for white/blacklists, events/job, filein and fileout

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

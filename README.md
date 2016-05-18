# Private production
Instructions for private production (Fast & Fullsim) of SUSY samples, valid Feb/March 2016, done on LXPLUS and LPC.
Mainly instructions from here were followed. I'll call it [0], [https://github.com/CMS-SUS-XPAG/GenLHEfiles/blob/master/Run2Mechanism/README.md](https://github.com/CMS-SUS-XPAG/GenLHEfiles/blob/master/Run2Mechanism/README.md)

Two main separable steps: LHE production and decay (same for Fast/Full), and CMSSW steps (different for Fast/Full). For us (stop pair production) LHE exist and just need to be decayed. This takes ~ 2 hrs & 10GB per mass point (typical 5 seeds * 100k events/seed) in an interactive session, or [0] might have scripts to export the jobs.

## LHE and LHE decay:
See `LHE_README.txt` for instructions on finding existing LHE and decaying (ie inject them with desired decays, branching fractions, and masses). See [0] for details I omit. `LHE_README.txt` is sufficient for T2tb, T2bW, and T2tt decays. I copy the undecayed LHE from LXPLUS to LPC, decay them at LPC interactively, and store them at FNAL EOS. This can be done in an independent directory from the CMSSW steps (it's just a few py scripts).

## CMSSW steps:
See [0] for updated details on Fast/Fullsim. See `FASTSIM_README.txt` for my notes on Fastsim (and `FULLSIM_README` for fullsim). The difference between the two lies in the CMSSW py configs and the CRAB3 py configs, because Fast and Fullsim require different number of steps and CMSSW settings. Also, Fastsim requires a lower #events/job in CRAB3 due to RAM constraints and higher memory use than Fullsim.

### Copy files
Start a directory in which to do the CMSSW steps. It'll need minimal space (a few GB should be fine), assuming the decayed LHE are accessible over xrootd. This dir will eventually have a few CMSSW distributions, some bash scripts to generate the CMSSW py configs, some CRAB3 py configs, and a couple dirs to store file lists and intermediate scripts.

### generator fragment 
If you have an official production sample in mind, backtrack it in MCM and DAS a few steps until you come to the LHE step. You'll see a 'curl' instruction which fetches the genfragment. Example is [https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_setup/SUS-RunIISpring15FSPremix-00218](https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_setup/SUS-RunIISpring15FSPremix-00218). 
Do this, and place the genfragment exactly at `CMSSW_(for first step)/src/Configuration/GenProduction/python/genfragment.py`. When running cmsDriver in the next paragraph, you MUST (my script does it automatically; be sure it does) 'scram b' under the src/ of the correct CMSSW distro, or else cmsDriver won't pick up on your genfragment. The genfragment is injected into the first step's CMSSW py config; see the examples in my dir and make sure it's injected into yours. See [0] for tuning the qcut (note xqcut is listed in the LHE files, and was used in their production) and more about genfragments. If you get it from a similar official production sample, you should be OK. 

### CMSSW py configs
Copy the cmsDriver bash scripts (which generate CMSSW py configs) and CRAB3 templates from my directory `FastsimScripts/` or `FullsimScripts/`. Running the cmsDriver scripts (`./cmsDriver...`) will pull the appropriate CMSSW distributions. Check them over and compare the CMSSW versions they pull to [0]. Also check the cmsDriver flags used, especially the `--conditions` flag with [0] or humans for correctness. Run the cmsDriver bash scripts to generate the CMSSW py configs and pull the CMSSW distributions. For the next few sentences, compare to the `submitStepNTemplate_cfg.py` in my dir. Edit the first step to use xrootd to input the LHE files, and edit each step's output filenames to be `file:sensical.root`. Comment out each non-first step's input filename (it'll come via the CRAB3 config). Use placeholders such as <mSTOP> and rename the files as eg `submitStep0Template_cfg.py`. A further step will inject the placeholders and use the `*Template_cfg.py` for many seeds.
** NOTE: This step can be simplified by using arguments to crab submit in the submission script `batchCrab.sh`. See [https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters](https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters)

### CRAB3 py configs
Copy the CRAB3 py configs (eg `crabSubmitStep*Template.py`) from my Fast or Full directory. For the next few sentences, compare to the `crabSubmitStepNTemplate.py` in my dir. Edit them to use appropriate filenames, dataset names, events/job, and white/blacklists. I find 1000 evts/job (250 evts/job) to work for Fullsim (Fastsim). Note the `config.JobType.pluginName` must be `PrivateMC` for EventBased splitting and `Analysis` for FileBased splitting. Here are the CRAB3 resources I use:
[https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile](https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile)
[https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial)

### turning Templates into configs
Copy the `makeCMSSWCrabConfigs.py` from my Fast or Full dir and edit it to match your naming conventions. At the moment, for each mass point, you must type in the seeds manually. Running it (`python makeCMSSWCrabConfigs.py`)  will then inject the masses and seeds into the <mSTOP> or <seed> fields in the template CMSSW py config and CRAB3 py config files, placing the injected files into a unique directory for each mass point. This automates the submitting of multiple seeds for each mass point to CRAB, done by batchCrab.sh later. 

### try a few events
Copy a sample chain of the injected CMSSW config files (eg `NNNNN_submitStep{0-3}_cfg.py`) out of the directory made in the last step and edit them to access the LHE properly (first step), and to use local (`file:X.root`) filenames for the input/output of each step. Also change the `maxEvents` to 100. Use cmsRun interactively starting from the first step (`cmsRun -p NNNNN_submitStep0_cfg.py`). After the last, it should be in miniAODv2 format ready for ntuplization and testing. 

### submitting to CRAB
Copy also `batchCrab.sh` from my dir and edit it for your conventions, and to use the right CMSSW distributions depending on the step number. Check it is set to the right step number. Run `source batchCrab.sh` to submit all seeds of the mass point to CRAB3. The CRAB project directories are in a (local) subdir from the injected config files, eg
`/private-T2bW-generation/mSTOP500_mNLSP250_mLSP1/T2bW_500_250_1_step0/crab_T2bW_mSTOP500_mNLSP250_mLSP1_seed41718_step2`. Section on proxy troubles below.

### checking CRAB status
The dashboard!
[http://dashb-cms-job.cern.ch/dashboard/templates/task-analysis/](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial)
Or `crab status --verboseErrors crab_T2bW_mSTOP500_mNLSP250_mLSP1_seed41718_step2`, where crab_X is the crab project directory. 
### between steps 
Between steps (eg 1,2,3) you'll modify the step # in, and then run, `makeJobRootLists.sh` to assemble the roots of the finished step; then you'll modify the step # in, and then run, `batchCrab.sh` to submit the tasks. Be sure to run `makeJobRootLists.sh` again after Step 3 and copy by hand those Step 3 root lists somewhere else as inputs to ntuplizing.

Since the LHE from the first step was split into many jobs, and thus input/output files for later steps, between each step one must assemble a txt list of the output roots of the previous step. Copy `makeJobRootLists.sh` from my dir and edit it for your naming convention. Run with `source makeJobRootLists.sh` and, for this mass point and step, it'll assemble a txt list with redirectors under `fileLists/` ready for the next CRAB submission. See my crab submission pys for how these txt lists are used as inputs to each subsequent step.

### between mass points
Between mass points you'll modify the mass point numbers (remove the decimals! 312.5 should be 3125) in all three of `makeJobRootLists.sh`, `makeCMSSWCrabConfigs.py`, and `batchCrab.sh`. You'll also revert the step numbers in each of those to 1. Then, run `makeCMSSWCrabConfigs.py` to turn the templates into actionable crab configs specific to the new mass point, and run `batchCrab.sh` to start step 1. Be sure your proxy is up `voms-proxy-init --voms cms --valid 168:00` or you'll get an error. If something goes wrong when submitting, `rm -rf` the crab submission directory made by `makeCMSSWCrabConfigs.py` before resubmitting (a common thing to do with crab). For me it's eg `mSTOP550_mNLSP325_mLSP100/T2bW_550_325_100_step1/`, different for each step, and encompassing all seeds for that mass point. 

### splitting across usernames
We submitted T2bW under both apatters and ocolegro usernames. To do this, get the production working under one username, then copy the production directories in full to some location in the other username. We had production out of `/uscms_data/d3/ocolegro/private-T2bW-generation` and `/afs/cern.ch/work/a/apatters/private/private-T2bW-generation`. You'll need to modify most instances of the username in the Template files (eg crabSubmitStep2Template.py). You might consider leaving the LHE location (input to Step 1) unchanged so that LHE production stays in the eos of one username for simplicity. There's nothing to change in `batchCrab.sh`, one thing (userLFN) to change in `makeJobRootLists.sh`, and nothing to change in `makeCMSSWCrabConfigs.py`.

## Proxy troubles
At fnal one can pivot to another username (we all set access lists in our `~/.krb5` or somewhere similar last summer) using `ksu <new username>`. Then renew the proxy with the usual `voms-proxy-init --voms cms --valid 168:00`. If you get the below error while submitt CRAB jobs:
```
Problems delegating My-proxy. It seems your proxy has not been delegated to myproxy. Pl
ease check the logfile for the exact error (it might simply you typed a wrong password)
```
then follow these instructions to destroy your old proxy from MyProxy and to submit a new one. A latest post on HyperNews by someone else solved this problem for me. References: 
[https://egee-uig.web.cern.ch/egee-uig/production_pages/ProxyRenewal.html](https://egee-uig.web.cern.ch/egee-uig/production_pages/ProxyRenewal.html)
[https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#crab_command_fails_with_Impossib](https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#crab_command_fails_with_Impossib)

Grep a failed project directory's crab.log for 'myproxy', copy the argument of the -l switch (long hash, it's a username), and use it to destroy the old proxy:
```
myproxy-destroy -l <long hash> -s myproxy.cern.ch
```
And then re-initialize the proxy in myproxy (no long has req'd):
```
myproxy-init -s myproxy.cern.ch -d -n
```

## Ntuplize
Last summer I edited the nuplization code to handle the many roots (100? 400?) outputted per mass point by the last CMSSW step (conversion to miniAODv2). See `ntuplize_README.txt` for ntuplization instructions.

## Links
Tutorial for everything (Full and Fast, and even making LHE)
[0] https://github.com/CMS-SUS-XPAG/GenLHEfiles/blob/master/Run2Mechanism/README.md

A long presentation on generators, jet matching, (x)qcut
[1] https://cp3.irmp.ucl.ac.be/projects/madgraph/attachment/wiki/FHEP/Mattelaer_parton_shower_matching_merging.pdf

CRAB3
[2] https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial
    https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile
    https://twiki.cern.ch/twiki/bin/view/CMSPublic/Crab3DataHandling
    https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3AdvancedTutorial
	see exercise 2 for file-based splitting in crab config

CRAB job monitoring (delay < about 1hour)
http://dashb-cms-job.cern.ch/dashboard/templates/task-analysis/

Short description of (x)qcut
[3] http://hep.ucsb.edu/people/cag/Matching.pdf

How to tell if you got qcut correct
[4] https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideSubgroupMC#Measure_proper_value_of_qCut

Global tags reference
[5] https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFrontierConditions#Special_Global_Tags_for_Run2_MC

FastSim twiki
[6] https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFastSimulationExamples#Run2_Spring15_recipe

A mention about a certain ignorable Pythia8 error message ... 
[7] https://twiki.cern.ch/twiki/bin/view/MPGD/DisplacedEMuHLTStudy

Defines Premixing, also see [6]
[8] https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideSimulation#Pre_Mixing_Instructions

cmsDriver
[9] https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFastSimulation

Twiki on specific RunIISpring15DR74 campaign
[10] https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmVMCcampaignRunIISpring15DR74x

Our miniaod sources
[11] https://github.com/UCSBSusy/13TeVAnalysis/blob/74X_prod_v2/AnalysisBase/Analyzer/run/datasets.conf

mcm
[12] https://cms-pdmv.cern.ch/mcm/requests?produce=%2FTTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8%2FRunIIWinter15GS-MCRUN2_71_V1-v2%2FGEN-SIM&page=0&shown=17516725375

das
[13] https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fglobal&input=dataset%3D%2F*%2F*RunIISpring15DR74*%2FMINIAODSIM

cmsDriver common error solution (VtxSmeared)
[14] https://twiki.cern.ch/twiki/bin/view/Main/RobinCMSSWErrors

LHE decay block format
[15] http://xxx.lanl.gov/pdf/hep-ph/0311123v4.pdf

SUSY xsecs
[20]
https://twiki.cern.ch/twiki/bin/view/LHCPhysics/
https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom

Small notes / problems encountered during Fastsim production

Table of contents is below. Here's an easter egg I found. Try killing it.
edmMakePhDThesis
Here's its code if you want to cheat:
https://github.com/ggovi/cmssw-old/blob/45003bdb1fdf7a9a497f9be727e6b8218cdbd330/PhysicsTools/PythonAnalysis/scripts/edmMakePhDThesis

Here's the help for the edm tools I reference:
https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookEdmUtilities

Contents:
1) DAS queries timeout
2) Missing modules in between steps (Zero products found matching all criteria)
3) Process() name of each step causes conflicts if not changed
4) Excessive memory use errors
5) Recent CRAB error which fails postjobs, but output & publishing work (about to be patched)
6) Ignorable errors and warnings at each step

1) DAS queries (eg NeutrinoGun files for mixing, or LHE steps) when running cmsDriver often timeout. Find the files for the dataset on the DAS website, https://cmsweb.cern.ch/das/, and plug enough of them in, without redirector, into the empty [] string array in the CMSSW py cmsDriver makes when failing the DAS query. They should start with /store/ but may start with the redirector. When running the steps with cmsRun interactively, you'll see just how many (say, NeutrinoGun) files are needed.

2) Error dump is at [0]. Twiki tech description:
https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookTroubleShooting#Error_Found_zero_products_matchi
The modules (eg famosSimHits or ak8GenJets) passed from step to step through the output roots can be listed using edmDumpEventContent. Also try edmProvDump's options.
edmDumpEventContent --all T2bW_500_seed43487_decayed_1000024_250__1000022_1_step3_97.root > eventDumpStep3.txt
When doing Fastsim it might be necessary (was for me) to tweak the modules between steps, so that each step's processes find teh collections they need to fill their outputs. Put another way, modifying a step's output module list can cause it to want more input modules. If you see 'Found zero products matching all criteria' when cmsRun'ing your few test events, add the missing module to the previous step's output list as follows. 
2a) Find the 'LabelName' in the error message, not the Modulename. Example is FamosSimHits.
2b) Check for it in the previous step's root with edmDumpEventContent as above. 
2c) If it's there, maybe something quite closely named is missing, so try to be more inclusive with wildcarding in the next step. If it's not there, ...
2d) Add the module to the previous step's output by opening up that CMSSW py (eg submitStep1Template.py in my files) and doing the following:
- Find in the OutputModule constructor call the outputCommands parameter being passed:
(blah,
outputCommands = process.MINIAODSIMEventContent.outputCommands,
blah)
- Move this just before the call, ie with no indentation, like so:
myOutputCommands = process.MINIAODSIMEventContent.outputCommands
And of course replace the constructor line:
(blah,
outputCommands = myOutputCommands,
blah)
- Get a feel for it with 'print myOutputCommands' and running 'python submitStep1Template.py' instead of 'cmsRun ...'.
- Add to it (format described below):
myOutputCommands.extend(['keep *TriggerResults*_*_*_*',
                         'keep *_reducedEcalRecHits*_*_*',  
                         'keep *_offlinePrimaryVertices_*_*',
                        ])
If for some terrible reason you must keep everything, one can do
myOutputCommands = cms.untracked.vstring(['keep *'])
- Rerun with cmsRun. The missing module error should be gone, or it should now say another modules is missing. Repeat until blue. Some wildcards break things (see above comment on a new output requiring a new input module), eg 'keep *reco*Jet*_*_*_*' caused me problems and had to be restricted. 

The output file size should be increased a bit with every module you decide to keep, so keep that in mind before you wildcard too much. Repeat edmDumpEventContent and diffs to see what you've added with those wildcards. I had to add ~ 20 such wildcards in my submitStep2Template.py for some reason.

The format of the modules is type_label_instance_process, with wildcards possible as / inside of every field, but you need the underscores (except if you do 'keep *' or 'drop *'). See example lines above. The Type/Label/Instance/Process you can explore with the '--all' flag to edmDumpEventContent. You want to figure out the module label from the error, and include this using 'keep *_<label>_*_*, and possible wildcards if you get many related (eg genJetsA, genJetsB, ...) missing modules.

use edmDumpEventContent on a root from an official production (last step only is kept, it seems) to see if you're missing any modules in the output of the final step. My only way of knowing if intermediate steps are missing modules is if the processes throw that 'missing Module' error.

See #3 about how process names can throw a similar error to missing module.

3) At the top of each step's CMSSW config (eg submitStep1Template.py in my files) is the process name definition ( process = cms.Process('HLT') ). It's arbitrary. If this string is the same for two steps in a row (eg the PAT step and the AOD->miniAOD step were both called 'PAT' when I downloaded the Fastsim configs from production) you'll get a conflict error
The process string you can see in 'edmDumpEventContent --all X.root'.
To match (see #2 above) the final root's modules with production module names, I found necessary to label my Fastsim steps: 'HLT', 'PATstep2', 'PAT'. The 'PATstep2' is arbitrary in my case as those don't make it to the final output, which is a mixture of the 'HLT' and 'PAT' modules. 

4) See this HN post and the ones to which it refers for data on excessive memory use by Fastsim, and how it's not linear with #events (there are spikes which can kill a job):
https://hypernews.cern.ch/HyperNews/CMS/get/famos/670.html
[0] https://hypernews.cern.ch/HyperNews/CMS/get/famos/612.html
[1] https://hypernews.cern.ch/HyperNews/CMS/get/famos/532.html

The CRAB jobs fail with error 50660. The usual RAM available to user CRAB jobs is 2GB (official production is allowed more, Lukas tells me). There's a CRAB config option to request a queue with more RAM but I've never used it, see eg crabSubmitStep1Template.py in my files. 
Solution 1: Reduce number of events per step (starting from the LHE step, since afterwards it's file-based splitting) until not many fail. For Fullsim I did 1000 events/job (thus 100 jobs per seed, since each is 100k events before decay matching). For Fastsim I needed to reduce this to 250 events/job, since 1000 caused a 50% failure rate (mem exceeded). 
Solution 2: Split the first Fastsim step (it does everything in this one step) into two, a GEN,SIM followed by everything else. I couldn't get this to work.

5) There's a recent CRAB bug failing all my postjobs for steps 2 & 3 (not step 1). The output roots are written to EOS and published in DAS, but something fails to parse in the postjob. CRAB exit code is 80001, and the HN topic I started (a few people hit similar bugs at the same time) is
https://hypernews.cern.ch/HyperNews/CMS/get/computing-tools/1413.html

6) 







[0] Example error dump for 'Zero products matching all criteria ...'. 
Begin processing the 1st record. Run 1, Event 3, LumiSection 1 at 29-Feb-2016 10:28:43.977 CET
----- Begin Fatal Exception 29-Feb-2016 10:28:44 CET-----------------------
An exception of category 'ProductNotFound' occurred while
   [0] Processing run: 1 lumi: 1 event: 3
   [1] Running path 'reconstruction_befmix_step'
   [2] Calling event method for module SiTrackerGaussianSmearingRecHitConverter/'siTrackerGaussianSmearingRecHits'
Exception Message:
Principal::getByToken: Found zero products matching all criteria
Looking for type: std::vector<PSimHit>
Looking for module label: famosSimHits
Looking for productInstanceName: TrackerHits

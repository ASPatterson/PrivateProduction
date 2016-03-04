#!/bin/bash
#T2bW fullsim cmsDriver settings, step 3
#from https://github.com/CMS-SUS-XPAG/GenLHEfiles/blob/master/Run2Mechanism/README.md

source  /afs/cern.ch/cms/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc491
if [ -r CMSSW_7_4_14/src ] ; then
 echo release CMSSW_7_4_14 already exists
else
scram p CMSSW CMSSW_7_4_14
fi
cd CMSSW_7_4_14/src
eval `scram runtime -sh`

#[ -s Configuration/GenProduction/python/SUS-RunIISpring15FSPremix-00218-fragment.py ] || exit $?;

#need to scram so cmsDriver sees the fragment
scram b
cd ../../

cmsDriver.py \
step1 \
--mc \
--eventcontent MINIAODSIM \
--runUnscheduled \
--customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 \
--datatier MINIAODSIM \
--conditions 74X_mcRun2_asymptotic_v2 \
--step PAT \
--filein file:AOD.root \
--fileout file:miniaodv2.root \
-n -1 \
--python_filename submitStep3_untemplated_cfg.py \
--no_exec

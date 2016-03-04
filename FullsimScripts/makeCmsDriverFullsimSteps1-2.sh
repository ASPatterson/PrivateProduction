#!/bin/bash
#T2bW fullsim cmsDriver settings, steps 1,2
#from https://github.com/CMS-SUS-XPAG/GenLHEfiles/blob/master/Run2Mechanism/README.md

source  /afs/cern.ch/cms/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc491
if [ -r CMSSW_7_4_1_patch4/src ] ; then
 echo release CMSSW_7_4_1_patch4 already exists
else
scram p CMSSW CMSSW_7_4_1_patch4
fi
cd CMSSW_7_4_1_patch4/src
eval `scram runtime -sh`

#[ -s Configuration/GenProduction/python/SUS-RunIISpring15FSPremix-00218-fragment.py ] || exit $?;

#need to scram so cmsDriver sees the fragment
scram b
cd ../../

cmsDriver.py \
step1 \
--pileup_input "dbs:/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIIWinter15GS-MCRUN2_71_V1-v1/GEN-SIM" \
--mc \
--eventcontent RAWSIM \
--pileup 2015_25ns_Startup_PoissonOOTPU \
--customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 \
--datatier GEN-SIM-RAW \
--conditions MCRUN2_74_V9 \
--step DIGI,L1,DIGI2RAW,HLT:@frozen25ns \
--magField 38T_PostLS1 \
--filein file:GEN.root \
--fileout file:DIGI.root \
-n -1 \
--python_filename submitStep1_untemplated_cfg.py \
--no_exec

cmsDriver.py \
step2 \
--mc \
--eventcontent AODSIM \
--customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 \
--datatier AODSIM \
--conditions MCRUN2_74_V9 \
--step RAW2DIGI,L1Reco,RECO \
--magField 38T_PostLS1 \
--filein file:DIGI.root \
--fileout file:AOD.root \
-n -1 \
--python_filename submitStep2_untemplated_cfg.py \
--no_exec

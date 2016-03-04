#!/bin/bash
#T2bW fullsim cmsDriver settings, step 0
#from https://github.com/CMS-SUS-XPAG/GenLHEfiles/blob/master/Run2Mechanism/README.md

source  /afs/cern.ch/cms/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc491
if [ -r CMSSW_7_1_20_patch3/src ] ; then
 echo release CMSSW_7_1_20_patch3 already exists
else
scram p CMSSW CMSSW_7_1_20_patch3
fi
cd CMSSW_7_1_20_patch3/src
eval `scram runtime -sh`

#[ -s Configuration/GenProduction/python/genfragment.py ] || exit $?;

#need to scram so cmsDriver sees the fragment
scram b
cd ../../

cmsDriver.py Configuration/Generator/python/genfragment.py \
--mc \
--eventcontent RAWSIM \
--customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 \
--datatier GEN-SIM \
--conditions MCRUN2_71_V1::All \
--beamspot NominalCollision2015 \
--step GEN,SIM \
--magField 38T_PostLS1  \
--filein file:mylhe.lhe \
--fileout file:GEN.root \
-n -1 \
--python_filename submitStep0_untemplated_cfg.py \
--no_exec

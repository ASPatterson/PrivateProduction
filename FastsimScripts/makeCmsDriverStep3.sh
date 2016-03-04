#!/bin/bash
#T2bW cmsDriver settings
#AODSIM to miniAODv2 step
#from https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_setup/SUS-RunIISpring15MiniAODv2-00330
# only change: nevents, filein, fileout names

source  /afs/cern.ch/cms/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc491
if [ -r CMSSW_7_4_14/src ] ; then 
 echo release CMSSW_7_4_14 already exists
else
scram p CMSSW CMSSW_7_4_14
fi
cd CMSSW_7_4_14/src
eval `scram runtime -sh`

#export X509_USER_PROXY=$HOME/private/personal/voms_proxy.cert

scram b
cd ../../

#create miniAOD_v2
cmsDriver.py step1 \
--filein "file:meow.root" \
--fileout file:SUS-RunIISpring15MiniAODv2-00330.root \
--mc \
--eventcontent MINIAODSIM \
--runUnscheduled \
--fast \
--customise SLHCUpgradeSimulations/Configuration/postLS1CustomsPreMixing.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring \
--datatier MINIAODSIM \
--conditions 74X_mcRun2_asymptotic_v2 \
--step PAT \
--python_filename testStep3_cfg.py \
--no_exec -n -1 || exit $? ; 



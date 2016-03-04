#!/bin/bash
#T2bW cmsDriver settings
#LHE to AODSIM steps -- fastsim
#from https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_setup/SUS-RunIISpring15FSPremix-00218
#only change: nevents, filein, fileout names
# also split GEN,SIM from other steps per recommendation of hypernews (FASTSIM excessive memory usage due to pileup)

source  /afs/cern.ch/cms/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc491
if [ -r CMSSW_7_4_4/src ] ; then 
 echo release CMSSW_7_4_4 already exists
else
scram p CMSSW CMSSW_7_4_4
fi
cd CMSSW_7_4_4/src
eval `scram runtime -sh`

#export X509_USER_PROXY=$HOME/private/personal/voms_proxy.cert
curl -s --insecure https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/SUS-RunIISpring15FSPremix-00218 --retry 2 --create-dirs -o Configuration/GenProduction/python/SUS-RunIISpring15FSPremix-00218-fragment.py 
[ -s Configuration/GenProduction/python/SUS-RunIISpring15FSPremix-00218-fragment.py ] || exit $?;

#need to scram so cmsDriver sees the fragment
scram b
cd ../../

#mix lhe with neutrino gun and do GEN to RECO
#big note: das queries fail for me, so I lookup the neutrino gun files on MCM and manually fill in the empty [] filed in _cfg.py
#next note: they eventually succeeded (must be days that don't end in y).

cmsDriver.py \
Configuration/GenProduction/python/SUS-RunIISpring15FSPremix-00218-fragment.py \
--filein "file:/afs/cern.ch/work/a/apatters/private/decayedLHE/T2bW_500_LSP0-run41718_decayed_1000024_250__1000022_1.lhe" \
--fileout file:T2bW_500_LSP0-run41718_decayed_1000024_250__1000022_1_step1.root \
--mc \
--eventcontent RECOSIM \
--fast \
--customise SLHCUpgradeSimulations/Configuration/postLS1CustomsPreMixing.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring \
--datatier GEN-SIM \
--conditions MCRUN2_74_V9 \
--beamspot NominalCollision2015 \
--step GEN,SIM \
--magField 38T_PostLS1 \
--python_filename submitStep0_untemplated_cfg.py \
--no_exec -n -1 || exit $? ;

cmsDriver.py \
Configuration/GenProduction/python/SUS-RunIISpring15FSPremix-00218-fragment.py \
--filein "file:/afs/cern.ch/work/a/apatters/private/decayedLHE/T2bW_500_LSP0-run41718_decayed_1000024_250__1000022_1.lhe" \
--fileout file:T2bW_500_LSP0-run41718_decayed_1000024_250__1000022_1_step1.root \
--pileup_input "dbs:/Neutrino_E-10_gun/RunIISpring15PrePremix-MCRUN2_74_V9-v1/GEN-SIM-DIGI-RAW" \
--mc \
--eventcontent AODSIM \
--fast \
--customise SLHCUpgradeSimulations/Configuration/postLS1CustomsPreMixing.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring \
--datatier AODSIM \
--conditions MCRUN2_74_V9 \
--beamspot NominalCollision2015 \
--step RECOBEFMIX,DIGIPREMIX_S2:pdigi_valid,DATAMIX,L1,L1Reco,RECO,HLT:@frozen25ns \
--magField 38T_PostLS1 \
--datamix PreMix \
--python_filename submitStep1_untemplated_cfg.py \
--no_exec -n -1 || exit $? ; 

#run premixed stuff thru PAT
cmsDriver.py \
Configuration/GenProduction/python/SUS-RunIISpring15FSPremix-00218-fragment.py \
--filein file:T2bW_500_LSP0-run41718_decayed_1000024_250__1000022_1_step1.root \
--fileout file:SUS-RunIISpring15FSPremix-00218.root \
--mc \
--eventcontent MINIAODSIM \
--fast \
--runUnscheduled \
--customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring \
--datatier MINIAODSIM \
--conditions MCRUN2_74_V9 \
--step PAT \
--python_filename submitStep2_untemplated_cfg.py \
--no_exec -n -1 || exit $? ;

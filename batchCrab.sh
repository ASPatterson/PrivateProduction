#!/bin/bash
# run as 'source batchCrab.sh'
# submits all crab jobs for a mass point, using CMSSW and crab configs
# produced by makeCMSSWCrabConfigs.py
#
# batch file for the command: 'crab submit -c crabSubmitStep2.py' 

# change masses and step here
mSTOP="500"
mNLSP="250"
mLSP="1"
step="0" # 0 thru 3

dir="mSTOP"$mSTOP"_mNLSP"$mNLSP"_mLSP"$mLSP
crabString="crabSubmitStep"$step".py"

source /cvmfs/cms.cern.ch/cmsset_default.sh
source /cvmfs/cms.cern.ch/crab3/crab.sh
voms-proxy-init --voms cms --valid 168:00

if [[ $step = "0" || $step = "1" || $step = "2" ]]; then
  cd CMSSW_7_4_4/src/
  cmsenv
  scram b
  cd ../..
  echo "CMSSW_7_4_4"
elif [[ $step = "3" ]]; then
  cd CMSSW_7_4_14/src/
  cmsenv
  scram b
  cd ../..
  echo "CSMSW_7_4_14"
else
  echo "troubles wit steps, plz halp"
  return;
fi

echo "Submitting CRAB3 jobs for step "$step" in " $dir
cd $dir

# dryrun for testing
#crab submit -c 41718_crabSubmitStep1.py --dryrun

for ii in $(ls *$crabString); do
  echo "Submitting " $ii
  crab submit -c $ii
#  echo "Submitted with exit status " $?
  if [ "$?" != "0" ]; then
    echo "Last exit code was not zero"
  fi
done

cd ..

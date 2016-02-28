#!/bin/bash
# run as 'source batchCrab.sh'
# submits all crab jobs for a mass point
#   eg mSTOP500_mNLSP250_mLSP1/ has CMSSW and crab configs
#      54323_submitStep2_cfg.py, 54323_crabSubmitStep2.py
#      so 'crab submit -c 54323_crabSubmitStep2.py' is executed
#      (it references the submitStep2 file)

# change masses and step here
mSTOP="500"
mNLSP="250"
mLSP="1"
step="1" #1-3

dir="mSTOP"$mSTOP"_mNLSP"$mNLSP"_mLSP"$mLSP
crabString="crabSubmitStep"$step".py"

source /cvmfs/cms.cern.ch/cmsset_default.sh
source /cvmfs/cms.cern.ch/crab3/crab.sh
#voms-proxy-init --voms cms --valid 168:00

if [ $step = "1" ]; then
  cd CMSSW_7_4_4/src/
  cmsenv
  cd ../..
  echo "CMSSW_7_4_4"
elif [[ $step = "2" || $step = "3" ]]; then
  cd CMSSW_7_4_14/src/
  cmsenv
  cd ../..
  echo "CSMSW_7_4_14"
else
  echo "step 1,2,3 please"
  return;
fi

echo "Submitting crab jobs for step " $step " in " $dir
cd $dir

# dryrun for testing
#crab submit -c 41718_crabSubmitStep1.py --dryrun

for ii in $(ls *$crabString); do
  echo "Submitting " $ii
  crab submit -c $ii
#  echo "Submitted with exit status " $?
  if [ "$?" != "0" ]; then
    echo "Last exit code not zero"
  fi
done

cd ..

#!/bin/bash
# but run as 'source makeJobRootLists.sh'
# steps after the first take inputs as a text file list of roots with redirectors, since first step split work into many jobs

# change masses and step here
mSTOP="500"
mNLSP="250"
mLSP="1"
step="1" #1-3

dirMassStep="T2bW_"$mSTOP"_"$mNLSP"_"$mLSP"_step"$step
listName="mSTOP"$mSTOP"_mNLSP"$mNLSP"_mLSP"$mLSP"_step"$step".txt"
projectDir="T2bW"
jobNamePrefix="T2bW"
userLFN="/store/user/apatters"
redirector="root://cmseos.fnal.gov//"
globalRedir="root://cms-xrd-global.cern.ch//"

# crab organizes things like:
#   crab project/ (eg T2bW-mass)
#     crab job/ (eg T2bW-mass-seed)
#       date of job/ (format yymmdd-hhmmss)
#         0000/ (never seen different)
#           job-NN.root
echo "Looking in " $userLFN/$projectDir/$dirMassStep/
for dirSeed in $(eos $redirector ls $userLFN/$projectDir/$dirMassStep/|grep $jobNamePrefix); do
  echo "Found seed subdir " $dirSeed
  touch fileLists/$dirSeed".txt"
  for dirDate in $(eos $redirector ls $userLFN/$projectDir/$dirMassStep/$dirSeed/|grep 16*); do
    echo "Found date subdir " $dirDate
    echo "Looking for roots in " $userLFN/$projectDir/$dirMassStep/$dirSeed/$dirDate/0000/
    # list files (eos ls has no regex option?), separate by newlines, roots only, prepend redirector, remove newlines
    echo $(eos $redirector ls $userLFN/$projectDir/$dirMassStep/$dirSeed/$dirDate/0000/) | \
           sed -e 's| |\n|g'| \
           grep root| \
           sed -e "s|^|$redirector/$userLFN/$projectDir/$dirMassStep/$dirSeed/$dirDate/0000/|g" >> fileLists/$dirSeed".txt"| \
           sed '/^\s*$/d'
  done
done

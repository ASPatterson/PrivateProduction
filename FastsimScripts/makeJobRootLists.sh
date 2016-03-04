#!/bin/bash
# but run as 'source makeJobRootLists.sh'
# intermediate production steps input many roots per seed (because first step splits one seed, 100k evts say, into many jobs)
# this file collects into fileLists
# steps after the first take inputs as a text file list of roots with redirectors, since first step split work into many jobs
# NOTE: due to limitations with LPC EOS's ls utility, I make heavy use of 'for i in $(ls ...)'. This fails bad for filenames with spaces or symbols.
#   Be careful your paths are safe for this script.

# change masses and step here
mSTOP="500"
mNLSP="250"
mLSP="1"
step="0" 

dirMassStep="T2bW_"$mSTOP"_"$mNLSP"_"$mLSP"_step"$step
listName="mSTOP"$mSTOP"_mNLSP"$mNLSP"_mLSP"$mLSP"_step"$step".txt"
projectDir="T2bW"
jobNamePrefix="T2bW"
userLFN="/store/user/apatters"
redirector="root://cmseos.fnal.gov/"
globalRedir="root://cms-xrd-global.cern.ch//"

mkdir -p fileLists

# CRAB3 output directory layout: (the outputs, not the local place with logs)
#   crab project/ (eg T2bW-mass)
#     crab job/ (eg T2bW-mass-seed)
#       date of job/ (format yymmdd-hhmmss)
#         0000/ (never seen different)
#           job-NN.root
# Don't want to double-count jobs, so trust only the most recent job. If double-count, later steps would anonymize -> problem!
# if sure not double-counting, uncomment the ## below, and comment relevant lines.

echo "Looking in mass point dir " $userLFN/$projectDir/$dirMassStep/
for dirSeed in $(eos $redirector ls $userLFN/$projectDir/$dirMassStep/|grep $jobNamePrefix); do
  echo "Found seed subdir " $dirSeed
##   for dirDate in $(eos $redirector ls $userLFN/$projectDir/$dirMassStep/$dirSeed/|grep 16*); do
##     echo "Found a date subdir " $dirData
  dirDate=$(eos $redirector ls $userLFN/$projectDir/$dirMassStep/$dirSeed/|sed '$!d')
    echo "Found most recent date subdir " $dirDate
    echo "Looking for roots in " $userLFN/$projectDir/$dirMassStep/$dirSeed/$dirDate/0000/
    # list filenames (eos ls has no regex option?), separate with newlines, roots only, prepend redirector, remove excess newlines
    echo $(eos $redirector ls $userLFN/$projectDir/$dirMassStep/$dirSeed/$dirDate/0000/) | \
           sed -e 's| |\n|g'| \
           grep root| \
           sed -e "s|^|$redirector/$userLFN/$projectDir/$dirMassStep/$dirSeed/$dirDate/0000/|g"| \
           sed '/^\s*$/d' \
           > fileLists/$dirSeed"_step"$step".txt"
##          >> fileLists/$dirSeed".txt" ## if combining roots from multiple dates, append, don't overwrite txt list
##done
done

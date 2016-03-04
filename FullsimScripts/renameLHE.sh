# renames LHE, eg
#   stop_stop550_LSP0_run36280_unwgt.lhe.gz
# to the necessary format for decaying LHE: <name>_<mSTOP>_<anything-with-underscores>_undecayed.lhe.gz, eg
#   stopstop_500_seed54323_undecayed.lhe.gz

#for old in $(eos root://cmseos.fnal.gov// ls /store/user/apatters/undecayedLHE/|grep stop_stop*); do
for old in $(ls stop*); do
  new=$(echo $old | sed -e 's|stop_stop|stopstop_|') #our name is stopstop
  new=$(echo $new | sed -e 's|_run|-seed|') #need underscore convention right
  new=$(echo $new | sed -e 's|unwgt|undecayed|') #convention
  new=$(echo $new | sed -E 's|LSP[0-9]{1,3}-||') #decay to multiple LSP masses, so this field is redundant/wrong and removable
#  new=$(echo $new | sed -e 's|-seed|_seed|') # hack with this one
  echo $old
  echo $new
  mv $old $new
#  eos root://cmseos.fnal.gov// mv /store/user/apatters/undecayedLHE/$old /store/user/apatters/decayedLHE/$new
done


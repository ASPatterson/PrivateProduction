Ntuplization instructions
(last updated Summer 2015)

Set up a CMSSW distribution. Check that 
	AnalysisBase/Analyzer/plugins/TestAnalyzer.cc
doesn't have that print(genparticles) line. 
Copy
	AnalysisBase/Analyzer/run/datasets.conf
to a new file, say t2bw_datasets.conf,
with entries which point to your (local) miniAODs, resulting from step3 above. 
Also include
the xsecs and a signal name which can be used with the find command to 
discover your miniAODs in that directory. The xsecs are at [20]. 
Move the miniAODs to their own directory, as the find command basically
looks for any roots in the directory (starting with the name you list)
 and assumes they're for that signal point. For example, one entry might be 

signal custom_600_1875 0.174599 /eos/uscms/store/user/apatters/13TeV/t2bw_miniAODs/t2bw_600_1875_50/

Make sure not to leave blank lines in your conf file. Then produceex the 
ntupling submission script, and be sure to specify using '-a local' that the
miniAODs are local, not being pulled from DAS.

./makejobs.py -o /eos/uscms/store/user/apatters/13TeV/t2bw_ntuples_nonmerged/ -t condor -a local -i t2bw_datasets.conf -s submit_t2bw

Execute the script, wait for them to be ntuplized (<1 hr/500 events), and 
then run interactive merging of all those small ntuples:

./makejobs.py --runmerge --inputdir /eos/uscms/store/user/apatters/13TeV/t2bw_ntuples_nonmerged/ -o /eos/uscms/store/user/apatters/13TeV/t2bw_merged/ -i t2bw_datasets.conf 

The script will be named submitmerge.sh. It's quick (10 mins/600k events).
Then run postprocessing, which takes the xsecs from the conf file, the
lumi from the command line (see --lumi), and makes branches with weights in 
the trees. weight = xsec*lumi/events. The folder name is renamed to Events
from TestAnalyzer/Events.

./makejobs.py --postprocess --inputdir /eos/uscms/store/user/apatters/13TeV/t2bw_merged/ -o /eos/uscms/store/user/apatters/13TeV/t2bw_merged/ -i t2bw_datasets.conf -t condor --postsuffix postproc


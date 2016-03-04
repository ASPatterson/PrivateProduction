LHE production and decay

See [0] for LHE production, and for details I omit here. This document is enough for T2tt, T2tb, T2bW processs. Plans for Fast/Fullsim makes no difference yet. I use preexisting LHE for stop pair production.

The preexisting LHE I use are at CERN EOS, under /store/group/phys_susy/LHE/13TeV/stop_stop_v2/. Ignore the LSP mass; it doesn't affect the files' physics tables, and it's injected in the decay step with a different LSP mass. I copy them to /tmp/ and then to my afs:
  eos cp /eos/cms/store/group/phys_susy/LHE/13TeV/stop_stop_v2/stop_stop800_LSP450_run62131_unwgt.lhe.gz /tmp/
  cp /tmp/stop_stop800_LSP450_run62131_unwgt.lhe.gz my_LHE_undecayed/
  
Leave them zipped for the decay py script. Compressed are 200 MB, uncompressed 1.2 GB, with 100k events each, and 5-10 seeds per mass point typically.

The decay py wants a formatted name. See my Fast/Fullsim dir for a renaming script to be run with 'source renameLHE.sh' ready to be run locally. I scp the undecayed LHE from lxplus to lpc and decay there, to make shuttling the decayed (much larger) LHE to my only EOS at FNAL quicker. 

Grab the git repo [0] for its decaying scripts. You won't need the CMSSW repo or to install generator code. You'll use these three scripts, located in GenLHEfiles/Run2Mechanism under
the LHE git bundle you install in 'Getting Started' from the git tutorial:
	update_header.py, create_update_header_config.py, makeMassDict.py

Unzip an LHE (gzip -dc X.lhe.gz > X.lhe) to check a few things.
Check if the undecayed files have an LSP mass (will be found & injected by 
the decay py later)
	head -n 5000 stopstop_650_LSP325x58113_undecayed.lhe|grep DECAY
If you see "DECAY  1000022  0.0" or similar then you're OK. 
If not, remember to pass the flag --stableLSP to update_header.py later.

Open create_update_header_config.py and manually change the option block at 
bottom. Here is an example for T2tt. If you're not doing T2tt or T1qqqq 
(see the comments above the option block for possible preset decays), eg T2bW,
you'll leave decay blank and specify a decaystring explicitely. For T2tt you 
can leave decaystring empty.
Note 'name' must match the start of your LHE filenames.
    options = {"name": "stopstop",
               "pdg": "1000006",
               "nevents": "-1",
               "inputdir": "/afs/cern.ch/work/a/apatters/private/LHE_undecayed",
               "outputdir": "/afs/cern.ch/work/a/apatters/private/LHE_decayed",
               "model": "",
               "slha": "",
               "mass": "mass_dict.py",
               "decay": "T2tt",
               "decaystring": ""
               }

If you're doing T2tt, skip this paragraph on decaystring, it's one of the defaults.
If T2tb or T2bw, stay.
The tutorial on github [0] gives a decaystring example. It's injected into the 
LHE file, so you can look straight at the DECAY block format for LHE files 
at [15], pages 21-22, for the clearest definitions.
Here's a decay string for T2bW (all one line) to be put in 
create_update_header_config.py. Keep the spacing, newlines,etc. Format is below
>>>
	"decaystring" : "\"DECAY 1000006 0.1\"\n  \"   1.0  2  5  1000024\"\n  \"DECAY 1000024 0.5\"\n  \"  1.0  2  24  1000022\"\n",
>>>
In english it says
	1000006 (~t) 		->  5 (b) + 1000024 (~chi+_1) with BR 1.0
	1000024	(~chi+_1) 	-> 24 (W) + 1000022 (~chi0_1) with BR 1.0

And one for T2tb (all one line):
>>>
"decaystring" : "\"DECAY 1000006 0.1\"\n  \"   0.5  2  5  1000024\"\n    \"   0.5  2  6  1000022\"\n  \"DECAY 1000024 0.5\"\n  \"  1.0  2  24  1000022\"\n",
>>>
The antiparticle decays are implied. The numbers 0.1 and 0.5 are the total 
decay widths; I took those values from the git tutorial. The format of the
decay block in LHE files is given in [15]. Its format (eg in tutorial.cfg 
which you'll generate) is
	DECAY <mother pdgid> <mother decay width>
	<BR to first mode> <# daughters> <pdgid daughter 1> <pdg daughter 2> 
	<BR to second mode> <# daughters> <pdgid daughter 1> <pdg daughter 2> 

Run the script to make the header config file
	python create_update_header_config.py
Output will be tutorial.cfg. Check it over.
If you're doing a custom (not T2tt, T1tttt, etc) job, change 'model' to a good 
name for the files, 'T2bw', 'T2tb', etc, or else they'll all say 'custom' for
the first step.

The decaystring in tutorial.cfg for T2bW looks like:
>>>
	decaystring = "DECAY 1000006 0.1"
		  "   1.0  2  5  1000024"
		  "DECAY 1000024 0.5"
		  "  1.0  2  24  1000022"	
>>>
And for T2tt looks like (from memory, it's done automatically so don't worry):
>>>
	decaystring = "DECAY 1000006 0.1"
		  "   1.0  2  6  1000022"
>>>
And for T2tb:
>>>
decaystring = "DECAY 1000006 0.1"
          "   0.5  2  5  1000024"
          "   0.5  2  6  1000022"
          "DECAY 1000024 0.5"
          "  1.0  2  24  1000022"
>>>

Now use makeMassDict.py to create the mass dictionary file, mass_dict.py.
I made them myself since they were simple.
Here's for the three usual T2tt mass points:
>>>
mass_dict = {'850': [{'1000022': 100}],
             '650': [{'1000022': 325}],
             '500': [{'1000022': 325}]}
>>>
See the tutorial on github for more complicated cases. 
Here's mass_dict.py for T2bW with mass points 700/100 and 600/50 (stop/lsp) 
with x=0.25, 0.50, 0.75. This causes the LHE processing py to process the 
input LHE (which says only the stop mass) for each condition you list here:
>>>
# Configuration dictionary for three different configurations
conf1 = {"1000024" : 250,
         "1000022" : 100}
conf2 = {"1000024" : 400,
         "1000022" : 100}
conf3 = {"1000024" : 550,
         "1000022" : 100}
conf4 = {"1000024" : 187.5,
         "1000022" : 50}
conf5 = {"1000024" : 325,
         "1000022" : 50}
conf6 = {"1000024" : 462.5,
         "1000022" : 50}
# Required mass dictionary.
mass_dict = {"700" : [conf1, conf2, conf3],
             "600" : [conf4, conf5, conf6]}
>>>

With tutorial.cfg and mass_dict.py created and checked,
Process the LHE files using update_header.py. For 30 LHE files it takes an 
hour or two. 
	python update_header.py tutorial.cfg
If you get the error
	ImportError: No module named argparse
then you need to cmsenv.
Watch progress:
	watch -n 10 -d 'ls /eos/uscms/store/user/apatters/mcproduction/decay/CMSSW_7_4_7/prod/GenLHEfiles/Run2Mechanism/decayed/'

NOTE: I ran a series of tests to determine what influence the LSP mass has on
the undecayed LHE files. First: grabbed two different LSP mass samples 
(different seeds as well),
	T2tt(800,400), T2tt(800,100)
and diff'ed their LHE files. The only differences are in the LSP mass entry 
in the mass spectrum block, and everything depending just on the random seed. 
The mixing matrices and branch fractions were the SAME between these two LHE 
files coming to us with different LSP masses. Second test: Diff two LHE files 
with same LSP mass but different random seed, to see what exactly is 
affected by it. Result is exactly those entries which were different when using
two different LSP masses in the first test. Thus, the LSP mass changes one 
thing: the LSP mass entry in the mass spectrum block. That's it.
The difference between processed LHE files which, using update_header.py, were 
set to two different LSP masses (same seed), is only in the mass spectrum block 
and the model strings. Thus, it's as minimal as can be -- we're free to use
these unprocessed LHE files and change the LSP masses without physical effect. 
** this assumes the official LHE files were made without the obvious error of 
forgetting to take into account LSP masses when making mixing matrices, BRs,...

; -----------------------------------------------------------------------------
;
; Verify the decayed LHE
; -----------------------------------------------------------------------------

	head -n 5000 T2tt_850_LSP100x67254_decayed_1000022_100.lhe|grep DECAY
Do you see the DECAY string for stop:
	DECAY  1000006  0.1 
and, if charginos present,
	DECAY 1000024 0.5
Now pipe instead into less and search ("/<search string>") for its decay:
(for T2tt)
	DECAY  1000006  0.1
   	   1.0  2  1000022 6      # t1 -> ~chi_10 t 
(for T2bW)
	DECAY 1000006 0.1
	   1.0  2  5  1000024
	DECAY 1000024 0.5
	   1.0  2  24  1000022
(for T2tb)
	DECAY 1000006 0.1
	   0.5  2  5  1000024
	   0.5  2  6  1000022
	DECAY 1000024 0.5
	  1.0  2  24  1000022
The DECAY block was changed properly.

Now check the mass spectrum block:
	head -n 5000 T2tt_850_LSP100x67254_decayed_1000022_100.lhe|less
Page down to the mass spectrum block ("BLOCK MASS  # Mass Spectrum"). Is there
(for T2tt, 850/100 mass splitting STOP/LSP)
	1000006     850       # ~t_1
	1000022     100       #
(for T2bW, 600/187.5/50 mass splitting STOP/CHARGINO/LSP)
   1000006     600       # ~t_1
      1000022     50       # 
      1000024     187.5       # 
If so, good.

Now check the event "model strings" are present (wording from tutorial [0]).
	head -n 5000 T2tt_850_LSP100x67254_decayed_1000022_100.lhe|grep '# model'
You should see for each event the comment
(for T2tt)
	# model T2tt_850_100
(for T2bW, unless you changed the 'model' string when updating the header)
	# model custom_600_187.5_50
(for T2tb, where I did change the 'model' string to model=t2tb)
	# model t2tb_700_250_100

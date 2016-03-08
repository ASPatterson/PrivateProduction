# CRAB3 config py for T2bW Fastsim jobs Feb 2016

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.section_("General")
# task name is timestamp:crab_<requestName>
config.General.requestName = 'T2bW_mSTOP<mSTOP>_mNLSP<mNLSP>_mLSP<mLSP>_seed<seed>_step1'
# project directory is <submission dir>/workArea/
config.General.workArea = 'T2bW_<mSTOP>_<mNLSP>_<mLSP>_step1'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_('JobType')
# use "PrivateMC" for event-based splitting, "Analysis" for file-based (later steps)
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '<seed>_submitStep1_cfg.py'
# request nodes with > 2GB mem; helps mitigate fastsim excessive mem use
#config.JobType.maxMemoryMB = 2500
# set to "lhe" when running the step inputting LHE files
config.JobType.generator = 'lhe'
# extra options/params for cmsRun
#config.JobType.pyCfgParams = ['myOption','param1=value1','param2=value2']
#config.JobType.maxJobRuntimeMin = 1315 #default ~ 22 hrs

config.section_('Data')
# output name appended to LFN
config.Data.outputPrimaryDataset = 'T2bW_<mSTOP>_<mNLSP>_<mLSP>_step1'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 250
NJOBS = 400
# Total events to process, if pluginName is PrivateMC (EventBased splitting).
# Total files to process, if Analysis with FileBased splitting
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
# needs trailing slash, can have subdir appended
#config.Data.outLFNDirBase = '/store/user/apatters/T2bW/'
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.publication = False
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter'
config.Data.outputDatasetTag = 'T2bW_mSTOP<mSTOP>_mNLSP<mNLSP>_mLSP<mLSP>_seed<seed>'

config.Data.ignoreLocality = True

config.section_('Site')
config.Site.whitelist = ["T2_US*"]
#config.Site.blacklist = ['T2_US_Vanderbilt']
#config.Site.whitelist = ['T2_US_Nebraska','T2_US_Purdue','T2_US_Vanderbilt','T2_US_Florida','T2_US_Wisconsin','T2_US_MIT']
config.Site.storageSite = 'T3_US_FNALLPC'

config.section_('User')

config.section_('Debug')
#config.Debug.oneEventMode = True

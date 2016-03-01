# CRAB3 config py for T2bW Fastsim jobs Feb 2016

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'T2bW_mSTOP<mSTOP>_mNLSP<mNLSP>_mLSP<mLSP>_seed<seed>_step1'
config.General.workArea = 'T2bW_<mSTOP>_<mNLSP>_<mLSP>_step1'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = 'T2bW_step1_cfg.py'
config.JobType.psetName = '<seed>_submitStep1_cfg.py'

config.JobType.generator = 'lhe'

config.Data.outputPrimaryDataset = 'T2bW_<mSTOP>_<mNLSP>_<mLSP>_step1'

config.Data.userInputFiles = open('/afs/cern.ch/work/a/apatters/private/private-T2bW-generation/fileLists/T2bW_mSTOP<mSTOP>_mNLSP<mNLSP>_mLSP<mLSP>_seed<seed>_step0.txt').readlines()

config.Data.splitting='FileBased'
config.Data.unitsPerJob = 1

config.Data.outLFNDirBase = '/store/user/apatters/T2bW/'
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.publication = False
config.Data.publishDBS = 'phys03'
config.Data.outputDatasetTag = 'T2bW_mStop<mSTOP>_mNLSP<mNLSP>_mLSP<mLSP>_seed<seed>'

config.Data.ignoreLocality = True
config.Site.blacklist = ['T2_US_Florida','T2_US_Wisconsin']
config.Site.whitelist = ['T2_US_Nebraska','T2_US_Purdue','T2_US_Vanderbilt']
#config.Site.whitelist = ['T2_US_Nebraska']
#config.Site.whitelist = ['T2_US_MIT']
#config.Site.whitelist = ["T2_US*"]
#config.Site.blacklist = ['T2_US_Vanderbilt','T2_US_Purdue','T2_US_Caltech','T2_US_Nebraska']
config.Site.storageSite = 'T3_US_FNALLPC'

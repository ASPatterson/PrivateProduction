# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/SUS-RunIISpring15FSPremix-00218-fragment.py --filein file:T2bW_500_LSP0-run41718_decayed_1000024_250__1000022_1_step1.root --fileout file:SUS-RunIISpring15FSPremix-00218.root --mc --eventcontent MINIAODSIM --fast --runUnscheduled --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --conditions MCRUN2_74_V9 --step PAT --python_filename T2bW_500_LSP0-run41718_decayed_1000024_250__1000022_1_2_cfg.py --no_exec -n 1092
import FWCore.ParameterSet.Config as cms

process = cms.Process('PATstep2')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('FastSimulation.Configuration.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('FastSimulation.Configuration.Geometries_MC_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring('file:T2bW_<mSTOP>_seed<seed>_decayed_1000024_<mNLSP>__1000022_<mLSP>_step1.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/SUS-RunIISpring15FSPremix-00218-fragment.py nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

myOutputCommands = process.MINIAODSIMEventContent.outputCommands
#myOutputCommands = cms.untracked.vstring(['keep *'])
myOutputCommands.extend(['keep *TriggerResults*_*_*_*',
                         'keep *_reducedEcalRecHits*_*_*',
                         'keep *_offlinePrimaryVertices_*_*',
                         'keep *_particleBasedIsolation_*_*',
                         'keep *_gedPhotons_*_*',
                         'keep *_PhotonIDProdGED_*_*',
                         'keep *_photonEcalPFClusterIsolationProducer_*_*',
                         'keep *_photonHcalPFClusterIsolationProducer_*_*',
                         'keep *_*photon*_*_*',
                         'keep *_*Photon*_*_*',
                         'keep *SuperCluster*_*_*_*',
                         'keep *_*GsfElectrons*_*_*',
                         'keep *_*idLoose_*_*',
                         'keep *_eid*_*_*',
                         'keep *_*Isolation*_*_*',
                         'keep *GsfElectronCore*_*_*_*',
                         'keep *_allConversions_*_*',
                         'keep *_particleFlow*_*_*',
                         'keep *reco*Track*_*_*_*',
                         'keep *reco*Electron*_*_*_*',
                         'keep *reco*Muon*_*_*_*',
#                         'keep *reco*Jet*_*_*_*',
                         'keep *_genParticles_*_*',
                         'keep *_*slimmed*_*_*',
                         'keep *_*selected*_*_*',
                         'keep *_*pat*_*_*',
                         'keep *_*Vertices_*_*',
                         'keep *_*Pileup*_*_*',
                         'keep *_*ak*Jet*_*_*',
                         'keep *_cmsTopTag*_*_*',
                         'keep *_*pat*Jet*_*_*',
                         'keep *_pfMet_*_*', ##pfMet
                         'keep *_genMet*_*_*', ##genMetTrue
                         'keep *_generalV0Candidates_*_*', ##generalV0Candidates
                         'keep *_*caloMet*_*_*',##caloMetM
])


process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAODSIM'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('file:T2bW_<mSTOP>_seed<seed>_decayed_1000024_<mNLSP>__1000022_<mLSP>_step2.root'),
    outputCommands = myOutputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')

# Path and EndPath definitions
process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.endjob_step,process.MINIAODSIMoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from FastSimulation.Configuration.MixingModule_Full2Fast
from FastSimulation.Configuration.MixingModule_Full2Fast import prepareDigiRecoMixing 

#call to customisation function prepareDigiRecoMixing imported from FastSimulation.Configuration.MixingModule_Full2Fast
process = prepareDigiRecoMixing(process)

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)
process.load('Configuration.StandardSequences.PATMC_cff')

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllMC 

#call to customisation function miniAOD_customizeAllMC imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllMC(process)

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.metFilterPaths_cff
from PhysicsTools.PatAlgos.slimming.metFilterPaths_cff import miniAOD_customizeMETFiltersFastSim 

#call to customisation function miniAOD_customizeMETFiltersFastSim imported from PhysicsTools.PatAlgos.slimming.metFilterPaths_cff
process = miniAOD_customizeMETFiltersFastSim(process)

# End of customisation functions

# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/SUS-RunIISpring15FSPremix-00218-fragment.py --filein file:/afs/cern.ch/work/a/apatters/private/decayedLHE/T2bW_500_LSP0-run41718_decayed_1000024_250__1000022_1.lhe --fileout file:T2bW_500_LSP0-run41718_decayed_1000024_250__1000022_1_step1.root --pileup_input dbs:/SMS-T2bW_X05_mStop-300to400_mLSP-0to275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15FSPremix-MCRUN2_74_V9-v1/AODSIM --mc --eventcontent AODSIM --fast --customise SLHCUpgradeSimulations/Configuration/postLS1CustomsPreMixing.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --conditions MCRUN2_74_V9 --beamspot NominalCollision2015 --step GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2:pdigi_valid,DATAMIX,L1,L1Reco,RECO,HLT:@frozen25ns --magField 38T_PostLS1 --datamix PreMix --python_filename T2bW_500_LSP0-run41718_decayed_1000024_250__1000022_1_1_cfg.py --no_exec -n 1092
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('FastSimulation.Configuration.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('FastSimulation.Configuration.Geometries_MC_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedNominalCollision2015_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('FastSimulation.Configuration.SimIdeal_cff')
process.load('FastSimulation.Configuration.Reconstruction_BefMix_cff')
process.load('FastSimulation.Configuration.DigiDMPreMix_cff')
process.load('SimGeneral.MixingModule.digi_MixPreMix_cfi')
process.load('FastSimulation.Configuration.DataMixerPreMix_cff')
process.load('FastSimulation.Configuration.SimL1Emulator_cff')
process.load('FastSimulation.Configuration.L1Reco_cff')
process.load('FastSimulation.Configuration.Reconstruction_AftMix_cff')
process.load('HLTrigger.Configuration.HLT_25ns14e33_v1_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("LHESource",
    fileNames = cms.untracked.vstring('root://cmseos.fnal.gov//store/user/apatters/decayedLHE/T2bW_<mSTOP>_seed<seed>_decayed_1000024_<mNLSP>__1000022_<mLSP>.lhe')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/SUS-RunIISpring15FSPremix-00218-fragment.py nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('AODSIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fileName = cms.untracked.string('file:T2bW_<mSTOP>_seed<seed>_decayed_1000024_<mNLSP>__1000022_<mLSP>_step1.root'),
    
    outputCommands = process.AODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
process.mix.digitizers = cms.PSet(process.theDigitizersMixPreMixValid)

#did by hand when dbs query failed:
#process.mixData.input.fileNames = cms.untracked.vstring(['root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/0021F46D-ED25-E511-9376-0025905B8576.root','root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/0040E519-2226-E511-A1C9-002618FDA277.root','root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00458809-B226-E511-952B-002354EF3BE0.root','root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00946A66-4726-E511-BA1E-0025905A60F2.root','root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/009FA86E-5F26-E511-A542-003048FFD732.root','root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00AE3880-B826-E511-9B01-00261894394F.root','root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00AF43F2-2B26-E511-BC56-0025905A6088.root','root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00B5E935-3C26-E511-A7DF-0025905B85D6.root','root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00CC8235-3C26-E511-8D60-0025905A60F4.root','root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00D70232-4126-E511-B79A-0025905938A4.root','root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00FB46CC-AC26-E511-A5E9-0025905A48C0.root','root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00FE5356-B326-E511-92FA-002590593878.root','root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/025DDF31-4126-E511-A90C-002618943961.root','root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/0293A6EC-6A26-E511-BC88-0025905964CC.root','root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/02B5EA66-B726-E511-8144-0026189438ED.root','root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/02F3BCCA-AC26-E511-B821-0025905A60B8.root','root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/04046678-5C26-E511-8574-003048FF9AC6.root','root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/04057621-2F26-E511-8DFA-0025905A6104.root','root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/04313C90-AA26-E511-B70A-002618FDA265.root','root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/045AE45D-2F26-E511-924A-0025905A60A8.root'])
#and automatic, when dbs query eventually succeeded:
process.mixData.input.fileNames = cms.untracked.vstring(['/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/0021F46D-ED25-E511-9376-0025905B8576.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/0040E519-2226-E511-A1C9-002618FDA277.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00458809-B226-E511-952B-002354EF3BE0.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00946A66-4726-E511-BA1E-0025905A60F2.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/009FA86E-5F26-E511-A542-003048FFD732.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00AE3880-B826-E511-9B01-00261894394F.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00AF43F2-2B26-E511-BC56-0025905A6088.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00B5E935-3C26-E511-A7DF-0025905B85D6.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00CC8235-3C26-E511-8D60-0025905A60F4.root', '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCRUN2_74_V9-v1/20000/00D70232-4126-E511-B79A-0025905938A4.root'])

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    PythiaParameters = cms.PSet(
        JetMatchingParameters = cms.vstring('JetMatching:setMad = off', 
            'JetMatching:scheme = 1', 
            'JetMatching:merge = on', 
            'JetMatching:jetAlgorithm = 2', 
            'JetMatching:etaJetMax = 5.', 
            'JetMatching:coneRadius = 1.', 
            'JetMatching:slowJetPower = 1', 
            'JetMatching:qCut = 57', 
            'JetMatching:nQmatch = 5', 
            'JetMatching:nJetMax = 2', 
            'JetMatching:doShowerKt = off'),
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CUEP8M1Settings', 
            'JetMatchingParameters'),
        pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:pT0Ref=2.4024', 
            'MultipartonInteractions:ecmPow=0.25208', 
            'MultipartonInteractions:expPow=1.6'),
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on')
    ),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.reconstruction_befmix_step = cms.Path(process.reconstruction_befmix)
process.digitisation_step = cms.Path(process.pdigi_valid)
process.datamixing_step = cms.Path(process.pdatamix)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.reconstruction_befmix_step,process.digitisation_step,process.datamixing_step,process.L1simulation_step,process.L1Reco_step,process.reconstruction_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.AODSIMoutput_step])
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from FastSimulation.Configuration.MixingModule_Full2Fast
from FastSimulation.Configuration.MixingModule_Full2Fast import prepareDigiRecoMixing 

#call to customisation function prepareDigiRecoMixing imported from FastSimulation.Configuration.MixingModule_Full2Fast
process = prepareDigiRecoMixing(process)

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1CustomsPreMixing
from SLHCUpgradeSimulations.Configuration.postLS1CustomsPreMixing import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1CustomsPreMixing
process = customisePostLS1(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforFastSim 

#call to customisation function customizeHLTforFastSim imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforFastSim(process)

# End of customisation functions

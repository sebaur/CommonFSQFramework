import FWCore.ParameterSet.Config as cms
import CommonFSQFramework.Core.Util
import os

isData = True

process = cms.Process("Treemaker")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

# Source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/data/Run2015A/ZeroBias8/RECO/27Jan2016-v1/50000/0E267E61-19C8-E511-B23F-0CC47A4DEDF0.root'
        )
)

# Geometry and Detector Conditions
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '76X_dataRun2_v19', '')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")

# in data produce Tracker RecHits
process.PixelRecHits = cms.Path(process.siPixelRecHits)
process.StripMatchedRecHits = cms.Path(process.siStripMatchedRecHits)

# Here starts the CFF specific part
import CommonFSQFramework.Core.customizePAT
process = CommonFSQFramework.Core.customizePAT.customize(process)

# GT customization
process = CommonFSQFramework.Core.customizePAT.customizeGT(process)

# define treeproducer
process.CFFTree = cms.EDAnalyzer("CFFTreeProducer")

import CommonFSQFramework.Core.VerticesViewsConfigs
import CommonFSQFramework.Core.CaloRecHitViewsConfigs
import CommonFSQFramework.Core.CaloTowerViewsConfigs
import CommonFSQFramework.Core.CastorViewsConfigs
import CommonFSQFramework.Core.PFObjectsViewsConfigs
import CommonFSQFramework.Core.TriggerResultsViewsConfigs

process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.VerticesViewsConfigs.get(["VerticesView","ZeroTeslaVertexView_Pixel_noPreSplitting"]))

process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.CaloTowerViewsConfigs.get(["CaloTowerView"]))
process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.CastorViewsConfigs.get(["CastorRecHitViewFull","CastorTowerView","ak5CastorJetView"]))
process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.TriggerResultsViewsConfigs.get(["CastorSpecialJetTriggerResultsView","L1GTriggerResultsView"]))

process.CFFTree._Parameterizable__setParameters(CommonFSQFramework.Core.TriggerResultsViewsConfigs.get(["ZeroBiasTriggerResultsViewWithPS"]))

process = CommonFSQFramework.Core.customizePAT.addPath(process, process.PixelRecHits)
process = CommonFSQFramework.Core.customizePAT.addPath(process, process.StripMatchedRecHits)

process = CommonFSQFramework.Core.customizePAT.addTreeProducer(process, process.CFFTree)

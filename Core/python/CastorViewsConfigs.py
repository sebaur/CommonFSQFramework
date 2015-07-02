import FWCore.ParameterSet.Config as cms

def get(todo):
    defs = {}

    defs["ak5CastorJetView"]= cms.PSet(   
        miniView = cms.string("CastorJetView"),
        branchPrefix = cms.untracked.string("ak5CastorJets"),
        minCastorJetEnergy = cms.double(100.),
        jetRadius = cms.double(0.5)
    )

    defs["ak7CastorJetView"]= cms.PSet(   
        miniView = cms.string("CastorJetView"),
        branchPrefix = cms.untracked.string("ak7CastorJets"),
        minCastorJetEnergy = cms.double(100.),
        jetRadius = cms.double(0.7)
    )

    defs["CastorRecHitViewFull"]= cms.PSet(   
        miniView = cms.string("CastorRecHitView"),
        branchPrefix = cms.untracked.string("CastorRecHit"),
        onlyGoodRecHits = cms.bool(False),
        writeSaturationInfo = cms.bool(True),        
    )   

    defs["CastorRecHitViewBasic"]= cms.PSet(   
        miniView = cms.string("CastorRecHitView"),
        branchPrefix = cms.untracked.string("CastorRecHit"),
        onlyGoodRecHits = cms.bool(True),
        writeSaturationInfo = cms.bool(False),        
    )   
    defs["TriggerResultsView"] = cms.PSet(
         miniView = cms.string("TriggerResultsView"),
         branchPrefix = cms.untracked.string("trg"),
         process = cms.string("HLT"), # usually HLT
         triggers = cms.vstring("randoms","noBPTX","zeroBias"),
         randoms =  cms.vstring("HLT_Random_v2*"),
         noBPTX =  cms.vstring("HLT_L1Tech7_NoBPTX_v1*"),
         zeroBias =  cms.vstring("HLT_ZeroBias_part0_v1*"),
     )
    defs["VerticesView"]= cms.PSet(
        miniView = cms.string("VerticesView"),
        branchPrefix = cms.untracked.string("Vtx"),
        src = cms.InputTag("offlinePrimaryVertices"),
    )

    defs["CastorTowerView"]  = cms.PSet(
        miniView = cms.string("CastorTowerView"),
        branchPrefix = cms.untracked.string("CastorTower"),
        inputcoll = cms.InputTag("CastorTowerReco")
    )

    ret = {}
    for t in todo:
        if t not in defs:
            raise Exception("miniView def not known "+t)

        ret[t] = defs[t]
    return ret



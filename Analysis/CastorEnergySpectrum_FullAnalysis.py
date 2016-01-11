#!/usr/bin/env python

# ------------------------------------------------------------
# ------------------------------------------------------------
#
#  This file produces histograms to further analyze the CASTOR
#  Energy Spectra during LHC Run II
#  --------------
#  The corresponding CFF dictionary file is
#  Skim/python/
#
# ------------------------------------------------------------
# ------------------------------------------------------------


import CommonFSQFramework.Core.ExampleProofReader

import sys, os, time, math
sys.path.append(os.path.dirname(__file__))

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import edm

from array import *

class CastorEnergySpectrum_FullAnalysis(CommonFSQFramework.Core.ExampleProofReader.ExampleProofReader):

    def init( self):
    
        self.selections = ["_SDenhanced","_NSD","_CASTOR"]
        self.composition = ["_all","_had","_em"]
        self.variations = ["_down","_central","_up"]

        # CASTOR Energy Scale uncertainty in Run2015A: 17%
        self.CastorEnergyScaleVariation = {}
        self.CastorEnergyScaleVariation["_down"] = 0.83
        self.CastorEnergyScaleVariation["_central"] = 1.
        self.CastorEnergyScaleVariation["_up"] = 1.17

        # additional parameters
        self.emParticles = [11,-11,22,111]
        self.excludeParticles = [12,13,14,16,18,-12,-13,-14,-16,-18] # exclude muons and neutrinos
 
        self.hist = {}
        # MC histograms
        if not self.isData:
            for s in self.selections:
                for c in self.composition:
                    self.hist["EnergyRatio"+s+c] = ROOT.TH1D("EnergyRatio"+s+c,"EnergyRatio"+s+c,100,0,3)
                    self.hist["CastorTotalEnergyResponse"+s+c] = ROOT.TH2D("CastorTotalEnergyResponse"+s+c,"CastorTotalEnergyResponse"+s+c,101,-100,10000,101,-100,10000)
                    self.hist["RecoSpectrum"+s+c] = ROOT.TH1D("RecoSpectrum"+s+c,"RecoSpectrum"+s+c,101,-100,10000)
                    self.hist["GenSpectrum"+s+c] = ROOT.TH1D("GenSpectrum"+s+c,"GenSpectrum"+s+c,101,-100,10000)
                    self.hist["RecoSpectrum_response"+s+c] = ROOT.TH1D("RecoSpectrum_response"+s+c,"RecoSpectrum_response"+s+c,101,-100,10000)
                    self.hist["GenSpectrum_response"+s+c] = ROOT.TH1D("GenSpectrum_response"+s+c,"GenSpectrum_response"+s+c,101,-100,10000)

                # control plots
                self.hist["RecHitSpectrum"+s] = ROOT.TH1D("RecHitSpectrum"+s,"RecHitSpectrum"+s,101,-10,1000)
                self.hist["TowerSpectrum"+s] = ROOT.TH1D("TowerSpectrum"+s,"TowerSpectrum"+s,101,-40,4000)
                self.hist["PhiProfile"+s] = ROOT.TProfile("PhiProfile"+s,"PhiProfile"+s,100,-4,4)

                self.hist["Purity"+s] = ROOT.TH1D("Purity"+s,"Purity"+s,2,-0.5,1.5)
                self.hist["Efficiency"+s] = ROOT.TH1D("Efficiency"+s,"Efficiency"+s,2,-0.5,1.5)

        # Data histograms
        if self.isData:
            for s in self.selections:
                for c in self.composition:
                    for v in self.variations:
                        self.hist["CastorTotalEnergy"+s+c+v] = ROOT.TH1D("CastorTotalEnergy"+s+c+v,"CastorTotalEnergy"+s+c+v,101,-100,10000)

                # control plots
                self.hist["RecHitSpectrum"+s] = ROOT.TH1D("RecHitSpectrum"+s,"RecHitSpectrum"+s,101,-10,1000)
                self.hist["TowerSpectrum"+s] = ROOT.TH1D("TowerSpectrum"+s,"TowerSpectrum"+s,101,-40,4000)
                self.hist["PhiProfile"+s] = ROOT.TProfile("PhiProfile"+s,"PhiProfile"+s,100,-4,4)
    
    	# add error treatment and add histograms to output
    	for h in self.hist:
            self.hist[h].Sumw2()
            self.GetOutputList().Add(self.hist[h])

    def analyze(self):

        # ------------------------------------------------------------
        # ------------------------------------------------------------
        # ------ check if event is accepted --------------------------
        # ------------------------------------------------------------

        GenSelection = {}
        RecoSelection = {}
        for s in self.selections:
            GenSelection[s] = False
            RecoSelection[s] = False

        # gen level selection
        if not self.isData:
            if self.fChain.XiSD >1e-6: GenSelection["_SDenhanced"] = True

        # reco level selections
        castor = False
        for i in xrange(0, self.fChain.CastorTowerp4.size()):
            if self.fChain.CastorTowerp4.size() > 0:
                castor = True
                break
        HFplus = False
        HFminus = False
        for i in xrange(0, self.fChain.CaloTowersp4.size()):
            if self.fChain.CaloTowersp4.at(i).energy() > 5. and self.fChain.CaloTowershasHF.at(i):
                if self.fChain.CaloTowersp4.at(i).eta() > 2.964 and self.fChain.CaloTowersp4.at(i).eta() < 4.889:
                    HFplus=True
                if self.fChain.CaloTowersp4.at(i).eta() < -2.964 and self.fChain.CaloTowersp4.at(i).eta() > -4.889:
                    HFminus=True

        if HFplus or HFminus: RecoSelection["_SDenhanced"] = True
        if HFplus and HFminus: RecoSelection["_NSD"] = True
        if castor: RecoSelection["_CASTOR"] = True

        # require exactly one vertex
        vertexSelection = True
        # add vertex requirement once it is available

        # trigger and event requirements
        triggerSelection = False
        if self.isData and self.fChain.trgZeroBias and self.fChain.run==247324 and self.fChain.bx in [208]: triggerSelection = True
        #if self.isData and self.fChain.trgZeroBias and self.fChain.run==247920: dataSelection = True
        #if self.isData and self.fChain.run==247324 and self.fChain.bx not in [208]: dataSelection = True

        # ------------------------------------------------------------
        # ------------------------------------------------------------
        # ------ calculate energies ----------------------------------
        # ------------------------------------------------------------            

        totGenEnergy = {}
        totTowerEnergy = {}
        weightedGenPhi = {}
        weightedRecoPhi = {}

        for s in self.selections:
            totGenEnergy[s] = {}
            totTowerEnergy[s] = {}
            weightedGenPhi[s] = 0.
            weightedRecoPhi[s] = 0.

            for c in self.composition:
                totGenEnergy[s][c] = 0.
                totTowerEnergy[s][c] = 0.

        for s in self.selections:
            # Gen level
            if not self.isData and GenSelection[s]:
                for i in xrange(0, self.fChain.genParticlesp4.size()):
                    if self.fChain.genParticlesp4.at(i).eta() > -6.6 and self.fChain.genParticlesp4.at(i).eta() < -5.2 and self.fChain.genParticlespdg.at(i) not in self.excludeParticles:
                        totGenEnergy[s]["_all"]+= self.fChain.genParticlesp4.at(i).energy()
                        if self.fChain.genParticlespdg.at(i) in self.emParticles:
                            totGenEnergy[s]["_em"] += self.fChain.genParticlesp4.at(i).energy()
                        if self.fChain.genParticlespdg.at(i) not in self.emParticles:
                            totGenEnergy["_had"] += self.fChain.genParticlesp4.at(i).energy()

                        weightedGenPhi[s] += self.fChain.genParticlesp4.at(i).energy()*self.fChain.genParticlesp4.at(i).phi()
            
            # reco level both data and MC
            if RecoSelection[s]:
                for i in xrange(0, self.fChain.CastorTowerp4.size()):
                    totTowerEnergy[s]["_all"] += self.fChain.CastorTowerp4.at(i).energy()
                    totTowerEnergy[s]["_em"] += self.fChain.CastorToweremEnergy.at(i)
                    totTowerEnergy[s]["_had"] += self.fChain.CastorTowerhadEnergy.at(i)

                    weightedRecoPhi[s] += self.fChain.CastorTowerp4.at(i).energy()*self.fChain.CastorTowerp4.at(i).phi()

        # ------------------------------------------------------------
        # ------------------------------------------------------------
        # ------- fill histograms if event is accepted ---------------
        # ------------------------------------------------------------      

        for s in self.selections:
            if self.isData and RecoSelection[s] and triggerSelection and vertexSelection:
                for c in self.composition:
                    for v in self.variations:
                        self.hist["CastorTotalEnergy"+s+c+v].Fill(self.CastorEnergyScaleVariation[v]*totTowerEnergy[s][c])

                for i in xrange(0, self.fChain.CastorTowerp4.size()):
                    self.hist["TowerSpectrum"+s].Fill(self.fChain.CastorTowerp4.at(i).energy())
                    self.hist["PhiProfile"+s].Fill(self.fChain.CastorTowerp4.at(i).phi())
                for i in xrange(0, self.fChain.CastorRecHitEnergy.size()):
                    self.hist["RecHitSpectrum"+s].Fill(self.fChain.CastorRecHitEnergy.at(i))

            if not self.isData and vertexSelection:
                if RecoSelection[s] and GenSelection[s]:
                    self.hist["Efficiency"+s].Fill(1)
                    self.hist["Purity"+s].Fill(1)
                if not RecoSelection[s] and GenSelection[s]:
                    self.hist["Efficiency"+s].Fill(0)
                if RecoSelection[s] and not GenSelection[s]:
                    self.hist["Purity"+s].Fill(0)

                for c in self.composition:
                    if RecoSelection[s] and GenSelection[s] and self.fChain.event%2 ==1:
                        self.hist["CastorTotalEnergyResponse"+s+c].Fill(totTowerEnergy[s][c],totGenEnergy[s][c])
                
                    if RecoSelection[s] and self.fChain.event%2 ==1:
                        self.hist["RecoSpectrum_response"+s+c].Fill(totTowerEnergy[s][c])
                    if GenSelection[s] and self.fChain.event%2 ==1:
                        self.hist["GenSpectrum_response"+s+c].Fill(totGenEnergy[s][c])
        
                    if RecoSelection[s] and self.fChain.event%2 ==0:
                        self.hist["RecoSpectrum"+s+c].Fill(totTowerEnergy[s][c])
                    if GenSelection[s] and self.fChain.event%2 ==0:
                        self.hist["GenSpectrum"+s+c].Fill(totGenEnergy[s][c])
    
                    if totGenEnergy[s][c] > 0. and RecoSelection[s] and GenSelection[s]:
                        self.hist["EnergyRatio"+s+c].Fill(totTowerEnergy[s][c]/totGenEnergy[s][c])

                if RecoSelection[s]:
                    for i in xrange(0, self.fChain.CastorTowerp4.size()):
                        self.hist["TowerSpectrum"+s].Fill(self.fChain.CastorTowerp4.at(i).energy())
                        self.hist["PhiProfile"+s].Fill(self.fChain.CastorTowerp4.at(i).phi())
                    for i in xrange(0, self.fChain.CastorRecHitEnergy.size()):
                        self.hist["RecHitSpectrum"+s].Fill(self.fChain.CastorRecHitEnergy.at(i))

        return 1

    # this function will be executed after all events are processed, on each worker node separately
    def finalize(self):
        print "Finalize:"
	   
    # this function will be executed after all events are processed, and after the results of all workers are merged/added
    # use it to e.g. correct mean values in histograms etc. for the number of workers that you used	   
    def finalizeWhenMerged(self):
        print "Final calculations after merging workers..."	   
	   

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    ROOT.gSystem.Load("libFWCoreFWLite.so")
    ROOT.AutoLibraryLoader.enable()

    sampleList = None # run through all samples in the dictionary
    maxFilesMC = None # run through all files found
    maxFilesData = None # same but for data samples
    maxNevents = -1 # run on all events, change this to some positive value to restrict the number of events you want to process
    nWorkers = None # Use all cpu cores

    # debug/test config:
    # Run printTTree.py alone to get the samples list
    sampleList = []
    #sampleList.append("MinBias_TuneZ2star_13TeV-pythia6_MagnetOff")
    sampleList.append("MinBias_TuneMonash13_13TeV-pythia8_MagnetOff")
    #sampleList.append("data_ZeroBias1_Run2015A_Run247324")
    sampleList.append("ReggeGribovPartonMC_13TeV-EPOS_MagnetOff")
    #sampleList.append("ReggeGribovPartonMC_13TeV-QGSJetII_MagnetOff")
    #sampleList.append("data_ZeroBias1")
    #sampleList.append("data_ZeroBias1_latestConditions")
    #sampleList.append("data_EmptyBX")
    #sampleList.append("data_L1TechBPTXQuiet")
    #sampleList.append("data_L1TechBPTXPlusOnly")
    #sampleList.append("data_L1TechBPTXMinusOnly")
    #sampleList.append("data_ZeroBias1_Run2015A_LHCf_lastruns")
    #sampleList.append("data_ZeroBias1_Run2015A_LHCf_Run247324_newCastorCond")
    #sampleList.append("MinBias_TuneEE5C_13TeV-herwigpp_MagnetOff")
    #sampleList.append("MinBias_TuneMBR_13TeV-pythia8_MagnetOff")

    #sampleList.append("ReggeGribovPartonMC_13TeV-EPOS_MagnetOff_sysMinus")
    #sampleList.append("ReggeGribovPartonMC_13TeV-EPOS_MagnetOff_sysPlus")
    #sampleList.append("ReggeGribovPartonMC_13TeV-EPOS_MagnetOff_nominal")
    #sampleList.append("ReggeGribovPartonMC_13TeV-EPOS_MagnetOff_measured")

    #maxFilesMC = 1
    #maxFilesData = 1
    maxNevents = 50000
    nWorkers = 12


    slaveParams = {}


    # use printTTree.py <sampleName> to see what trees are avaliable inside the skim file
    CastorEnergySpectrum_FullAnalysis.runAll(treeName="EflowTree",
           slaveParameters=slaveParams,
           sampleList=sampleList,
           maxFilesMC = maxFilesMC,
           maxFilesData = maxFilesData,
	       maxNevents = maxNevents,
           nWorkers=nWorkers,
           outFile = "CastorEnergySpectrum_FullAnalysis_out.root" )

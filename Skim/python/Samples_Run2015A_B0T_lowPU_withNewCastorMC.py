anaVersion="Run2015A_B0T_lowPU_withNewcastorMC"
anaType="Run2015A_B0T_lowPU"

cbSmartCommand="smartCopy"
cbSmartBlackList=""
cbWMS="https://wmscms.cern.ch:7443/glite_wms_wmproxy_server"
skimEfficiencyMethod="getSkimEff"

sam = {}

##################################################
##################################################
##################################################
##################################################
## A) MC Samples 
##################################################
##################################################
##################################################
##################################################

########################################################################
## 1) MC Samples with Hans' noise fix and relistic position
########################################################################

sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]={}
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["crabJobs"]=99
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["GT"]='76X_mcRun2_asymptotic_v14'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["name"]='MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["isData"]=False
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["numEvents"]=4917500
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newCASTORnoise_CFF/160513_124612/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newCASTORnoise_CFF/160513_124612/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["json"]=''
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["lumiMinBias"]=6.88821963860484642e-05
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["XS"]=71.39e+09
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newCASTORnoise_CFF/160513_124612/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["DS"]='/MinBias_CUETP8M1_13TeV-pythia8/sbaur-MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORmeasured_newCASTORnoise_RECO-288ab5be9a42aa4a7ffd90fa253c6744/USER'

sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]={}
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["crabJobs"]=98
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["GT"]='76X_mcRun2_asymptotic_v14'
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["name"]='MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise'
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["isData"]=False
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["numEvents"]=4862000
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/MinBias_TuneMBR_13TeV-pythia8/MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newCASTORnoise_CFF_2/160610_100853/0000/'
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/MinBias_TuneMBR_13TeV-pythia8/MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newCASTORnoise_CFF_2/160610_100853/0000/'
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["json"]=''
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["lumiMinBias"]=6.20007549248645671e-05
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["XS"]=78418400000.0
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/MinBias_TuneMBR_13TeV-pythia8/MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newCASTORnoise_CFF_2/160610_100853/0000/'
sam["MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newNoise"]["DS"]='/MinBias_TuneMBR_13TeV-pythia8/sbaur-MinBias_TuneMBR_13TeV-pythia8_MagnetOff_CASTORmeasured_newCASTORnoise_fix_RECO-288ab5be9a42aa4a7ffd90fa253c6744/USER'

sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]={}
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["crabJobs"]=100
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["GT"]='76X_mcRun2_asymptotic_v14'
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["name"]='MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise'
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["isData"]=False
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["numEvents"]=4978400
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/MinBias_EPOS_13TeV/MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newCASTORnoise_CFF/160518_072336/0000/'
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/MinBias_EPOS_13TeV/MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newCASTORnoise_CFF/160518_072336/0000/'
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["json"]=''
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["lumiMinBias"]=-1
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["XS"]=-1
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/MinBias_EPOS_13TeV/MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newCASTORnoise_CFF/160518_072336'
sam["MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newNoise"]["DS"]='/MinBias_EPOS_13TeV/sbaur-MinBias_EPOS_13TeV_MagnetOff_CASTORmeasured_newCASTORnoise_RECO-288ab5be9a42aa4a7ffd90fa253c6744/USER'


######################################################
## 2) Various positions for systematics
######################################################

sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]={}
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["crabJobs"]=13
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["GT"]='76X_mcRun2_asymptotic_v14'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["name"]='MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["isData"]=False
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["numEvents"]=960000
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus_CFF/160210_161831/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus_CFF/160210_161831/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["json"]=''
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["lumiMinBias"]=1.34472615212214589e-05
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["XS"]=71.39e+09
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus_CFF/160210_161831/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus"]["DS"]='/MinBias_CUETP8M1_13TeV-pythia8/katkov-MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystPlus_RECO-ea75752f65bd25232845285a23f93f6b/USER'

sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]={}
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["crabJobs"]=14
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["GT"]='76X_mcRun2_asymptotic_v14'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["name"]='MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["isData"]=False
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["numEvents"]=980000
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus_CFF/160210_161855/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus_CFF/160210_161855/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["json"]=''
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["lumiMinBias"]=1.37274128029135739e-05
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["XS"]=71.39e+09
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/MinBias_CUETP8M1_13TeV-pythia8/MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus_CFF/160210_161855/0000/'
sam["MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus"]["DS"]='/MinBias_CUETP8M1_13TeV-pythia8/katkov-MinBias_CUETP8M1_13TeV-pythia8_MagnetOff_CASTORsystMinus_RECO-ea75752f65bd25232845285a23f93f6b/USER'

##################################################
##################################################
##################################################
##################################################
## B) Data
##################################################
##################################################
##################################################
##################################################

##################################################
## 1) dN/deta Run
##################################################

sam["data_ZeroBias1_May2016_dNdeta"]={}
sam["data_ZeroBias1_May2016_dNdeta"]["crabJobs"]=0
sam["data_ZeroBias1_May2016_dNdeta"]["GT"]='74X_dataRun2_Prompt_v2_dNdeta'
sam["data_ZeroBias1_May2016_dNdeta"]["name"]='data_ZeroBias1'
sam["data_ZeroBias1_May2016_dNdeta"]["isData"]=True
sam["data_ZeroBias1_May2016_dNdeta"]["numEvents"]=-1
sam["data_ZeroBias1_May2016_dNdeta"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/ZeroBias1/ZeroBias-ReReco_Run2015A_lowPU_intercalibMay2016_HFcorrection_dNdeta/160503_080304/0000'
sam["data_ZeroBias1_May2016_dNdeta"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/ZeroBias1/ZeroBias-ReReco_Run2015A_lowPU_intercalibMay2016_HFcorrection_dNdeta/160503_080304/0000'
sam["data_ZeroBias1_May2016_dNdeta"]["json"]='CommonFSQFramework/Skim/lumi/Run2015A_lowPU_B0T.json'
sam["data_ZeroBias1_May2016_dNdeta"]["lumiMinBias"]=-1
sam["data_ZeroBias1_May2016_dNdeta"]["XS"]=-1
sam["data_ZeroBias1_May2016_dNdeta"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/ZeroBias1/ZeroBias-ReReco_Run2015A_lowPU_intercalibMay2016_HFcorrection_dNdeta/160503_080304/0000'
sam["data_ZeroBias1_May2016_dNdeta"]["DS"]='/ZeroBias1/Run2015A-v1/RAW'

##################################################
## 2) dN/deta Run, Noise samples
##################################################

sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]={}
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["crabJobs"]=0
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["GT"]='74X_dataRun2_Prompt_v2'
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["name"]='data_L1TechBPTXMinusOnly_Feb2016_dNdeta'
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["isData"]=True
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["numEvents"]=-1
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/L1TechBPTXMinusOnly/L1TechBPTXMinusOnly-PromptReco_Run2015A_lowPU_intercalibFeb2016_dNdeta/160304_142319/0000/'
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/L1TechBPTXMinusOnly/L1TechBPTXMinusOnly-PromptReco_Run2015A_lowPU_intercalibFeb2016_dNdeta/160304_142319/0000/'
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["json"]='CommonFSQFramework/Skim/lumi/Run2015A_lowPU_B0T_247324.json'
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["lumiMinBias"]=-1
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["XS"]=-1
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/L1TechBPTXMinusOnly/L1TechBPTXMinusOnly-PromptReco_Run2015A_lowPU_intercalibFeb2016_dNdeta/160304_142319/0000/'
sam["data_L1TechBPTXMinusOnly_Feb2016_dNdeta"]["DS"]='/L1TechBPTXMinusOnly/Run2015A-PromptReco-v1/RECO'

sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]={}
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["crabJobs"]=0
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["GT"]='74X_dataRun2_Prompt_v2'
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["name"]='data_L1TechBPTXPlusOnly_Feb2016_dNdeta'
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["isData"]=True
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["numEvents"]=-1
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/L1TechBPTXPlusOnly/L1TechBPTXPlusOnly-PromptReco_Run2015A_lowPU_intercalibFeb2016_dNdeta/160304_142250/0000'
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/L1TechBPTXPlusOnly/L1TechBPTXPlusOnly-PromptReco_Run2015A_lowPU_intercalibFeb2016_dNdeta/160304_142250/0000/'
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["json"]='CommonFSQFramework/Skim/lumi/Run2015A_lowPU_B0T_247324.json'
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["lumiMinBias"]=-1
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["XS"]=-1
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/L1TechBPTXPlusOnly/L1TechBPTXPlusOnly-PromptReco_Run2015A_lowPU_intercalibFeb2016_dNdeta/160304_142250/0000/'
sam["data_L1TechBPTXPlusOnly_Feb2016_dNdeta"]["DS"]='/L1TechBPTXPlusOnly/Run2015A-PromptReco-v1/RECO'

sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]={}
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["crabJobs"]=0
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["GT"]='74X_dataRun2_Prompt_v2'
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["name"]='data_L1TechBPTXQuiet_dNdeta'
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["isData"]=True
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["numEvents"]=-1
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/L1TechBPTXQuiet/L1TechBPTXQuiet-PromptReco_Run2015A_lowPU_intercalibFeb2016_dNdeta/160304_142346/0000/'
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/L1TechBPTXQuiet/L1TechBPTXQuiet-PromptReco_Run2015A_lowPU_intercalibFeb2016_dNdeta/160304_142346/0000/'
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["json"]='CommonFSQFramework/Skim/lumi/Run2015A_lowPU_B0T_247324.json'
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["lumiMinBias"]=-1
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["XS"]=-1
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/L1TechBPTXQuiet/L1TechBPTXQuiet-PromptReco_Run2015A_lowPU_intercalibFeb2016_dNdeta/160304_142346/0000/'
sam["data_L1TechBPTXQuiet_Feb2016_dNdeta"]["DS"]='/L1TechBPTXQuiet/Run2015A-PromptReco-v1/RECO'


########################################################
## 3) Run2015A rereco dataset, ZeroBias(1-8), tracking like in MC
## Details on processed lumisections in files "CommonFSQFramework/Skim/lumi/Run2015A-27Jan2016-v2_processedLumi_ZeroBias(1-8).json"
########################################################

sam["data_ZeroBias1_Run2015A-27Jan2016-v2"]={}
sam["data_ZeroBias1_Run2015A-27Jan2016-v2"]["crabJobs"]=0
sam["data_ZeroBias1_Run2015A-27Jan2016-v2"]["GT"]=''
sam["data_ZeroBias1_Run2015A-27Jan2016-v2"]["name"]='ddata_ZeroBias1_Run2015A-27Jan2016-v2'
sam["data_ZeroBias1_Run2015A-27Jan2016-v2"]["isData"]=True
sam["data_ZeroBias1_Run2015A-27Jan2016-v2"]["numEvents"]=-1
sam["data_ZeroBias1_Run2015A-27Jan2016-v2"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/ZeroBias1/ZeroBias1-27Jan2016-v2_Run2015A_TrackingLikeMC_Dec17_CFF/171204_154624/0000/'
sam["data_ZeroBias1_Run2015A-27Jan2016-v2"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/ZeroBias1/ZeroBias1-27Jan2016-v2_Run2015A_TrackingLikeMC_Dec17_CFF/171204_154624/0000/'
sam["data_ZeroBias1_Run2015A-27Jan2016-v2"]["json"]=''
sam["data_ZeroBias1_Run2015A-27Jan2016-v2"]["lumiMinBias"]=-1
sam["data_ZeroBias1_Run2015A-27Jan2016-v2"]["XS"]=-1
sam["data_ZeroBias1_Run2015A-27Jan2016-v2"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/ZeroBias1/ZeroBias1-27Jan2016-v2_Run2015A_TrackingLikeMC_Dec17_CFF/171204_154624/0000/'
sam["data_ZeroBias1_Run2015A-27Jan2016-v2"]["DS"]='/ZeroBias1/Run2015A-27Jan2016-v2/RECO'

sam["data_ZeroBias2_Run2015A-27Jan2016-v2"]={}
sam["data_ZeroBias2_Run2015A-27Jan2016-v2"]["crabJobs"]=0
sam["data_ZeroBias2_Run2015A-27Jan2016-v2"]["GT"]=''
sam["data_ZeroBias2_Run2015A-27Jan2016-v2"]["name"]='ddata_ZeroBias2_Run2015A-27Jan2016-v2'
sam["data_ZeroBias2_Run2015A-27Jan2016-v2"]["isData"]=True
sam["data_ZeroBias2_Run2015A-27Jan2016-v2"]["numEvents"]=-1
sam["data_ZeroBias2_Run2015A-27Jan2016-v2"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/ZeroBias2/ZeroBias2-27Jan2016-v2_Run2015A_TrackingLikeMC_Dec17_CFF/171204_162553/0000/'
sam["data_ZeroBias2_Run2015A-27Jan2016-v2"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/ZeroBias2/ZeroBias2-27Jan2016-v2_Run2015A_TrackingLikeMC_Dec17_CFF/171204_162553/0000/'
sam["data_ZeroBias2_Run2015A-27Jan2016-v2"]["json"]=''
sam["data_ZeroBias2_Run2015A-27Jan2016-v2"]["lumiMinBias"]=-1
sam["data_ZeroBias2_Run2015A-27Jan2016-v2"]["XS"]=-1
sam["data_ZeroBias2_Run2015A-27Jan2016-v2"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/ZeroBias2/ZeroBias2-27Jan2016-v2_Run2015A_TrackingLikeMC_Dec17_CFF/171204_162553/0000/'
sam["data_ZeroBias2_Run2015A-27Jan2016-v2"]["DS"]='/ZeroBias2/Run2015A-27Jan2016-v2/RECO'

sam["data_ZeroBias3_Run2015A-27Jan2016-v2"]={}
sam["data_ZeroBias3_Run2015A-27Jan2016-v2"]["crabJobs"]=0
sam["data_ZeroBias3_Run2015A-27Jan2016-v2"]["GT"]=''
sam["data_ZeroBias3_Run2015A-27Jan2016-v2"]["name"]='ddata_ZeroBias3_Run2015A-27Jan2016-v2'
sam["data_ZeroBias3_Run2015A-27Jan2016-v2"]["isData"]=True
sam["data_ZeroBias3_Run2015A-27Jan2016-v2"]["numEvents"]=-1
sam["data_ZeroBias3_Run2015A-27Jan2016-v2"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/ZeroBias3/ZeroBias3-27Jan2016-v2_Run2015A_TrackingLikeMC_Dec17_CFF/171204_163100/0000/'
sam["data_ZeroBias3_Run2015A-27Jan2016-v2"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/ZeroBias3/ZeroBias3-27Jan2016-v2_Run2015A_TrackingLikeMC_Dec17_CFF/171204_163100/0000/'
sam["data_ZeroBias3_Run2015A-27Jan2016-v2"]["json"]=''
sam["data_ZeroBias3_Run2015A-27Jan2016-v2"]["lumiMinBias"]=-1
sam["data_ZeroBias3_Run2015A-27Jan2016-v2"]["XS"]=-1
sam["data_ZeroBias3_Run2015A-27Jan2016-v2"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/ZeroBias3/ZeroBias3-27Jan2016-v2_Run2015A_TrackingLikeMC_Dec17_CFF/171204_163100/0000/'
sam["data_ZeroBias3_Run2015A-27Jan2016-v2"]["DS"]='/ZeroBias3/Run2015A-27Jan2016-v2/RECO'

sam["data_ZeroBias4_Run2015A-27Jan2016-v2"]={}
sam["data_ZeroBias4_Run2015A-27Jan2016-v2"]["crabJobs"]=0
sam["data_ZeroBias4_Run2015A-27Jan2016-v2"]["GT"]=''
sam["data_ZeroBias4_Run2015A-27Jan2016-v2"]["name"]='ddata_ZeroBias4_Run2015A-27Jan2016-v2'
sam["data_ZeroBias4_Run2015A-27Jan2016-v2"]["isData"]=True
sam["data_ZeroBias4_Run2015A-27Jan2016-v2"]["numEvents"]=-1
sam["data_ZeroBias4_Run2015A-27Jan2016-v2"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/ZeroBias4/ZeroBias4-27Jan2016-v2_Run2015A_TrackingLikeMC_Dec17_CFF_Dec17/171204_163212/0000/'
sam["data_ZeroBias4_Run2015A-27Jan2016-v2"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/ZeroBias4/ZeroBias4-27Jan2016-v2_Run2015A_TrackingLikeMC_Dec17_CFF_Dec17/171204_163212/0000/'
sam["data_ZeroBias4_Run2015A-27Jan2016-v2"]["json"]=''
sam["data_ZeroBias4_Run2015A-27Jan2016-v2"]["lumiMinBias"]=-1
sam["data_ZeroBias4_Run2015A-27Jan2016-v2"]["XS"]=-1
sam["data_ZeroBias4_Run2015A-27Jan2016-v2"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/ZeroBias4/ZeroBias4-27Jan2016-v2_Run2015A_TrackingLikeMC_Dec17_CFF_Dec17/171204_163212/0000/'
sam["data_ZeroBias4_Run2015A-27Jan2016-v2"]["DS"]='/ZeroBias4/Run2015A-27Jan2016-v2/RECO'

sam["data_ZeroBias5_Run2015A-27Jan2016-v2"]={}
sam["data_ZeroBias5_Run2015A-27Jan2016-v2"]["crabJobs"]=0
sam["data_ZeroBias5_Run2015A-27Jan2016-v2"]["GT"]=''
sam["data_ZeroBias5_Run2015A-27Jan2016-v2"]["name"]='ddata_ZeroBias5_Run2015A-27Jan2016-v2'
sam["data_ZeroBias5_Run2015A-27Jan2016-v2"]["isData"]=True
sam["data_ZeroBias5_Run2015A-27Jan2016-v2"]["numEvents"]=-1
sam["data_ZeroBias5_Run2015A-27Jan2016-v2"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/ZeroBias5/ZeroBias5-27Jan2016-v2_Run2015A_TrackingLikeMC_CFF_Dec17/171204_163336/0000/'
sam["data_ZeroBias5_Run2015A-27Jan2016-v2"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/ZeroBias5/ZeroBias5-27Jan2016-v2_Run2015A_TrackingLikeMC_CFF_Dec17/171204_163336/0000/'
sam["data_ZeroBias5_Run2015A-27Jan2016-v2"]["json"]=''
sam["data_ZeroBias5_Run2015A-27Jan2016-v2"]["lumiMinBias"]=-1
sam["data_ZeroBias5_Run2015A-27Jan2016-v2"]["XS"]=-1
sam["data_ZeroBias5_Run2015A-27Jan2016-v2"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/ZeroBias5/ZeroBias5-27Jan2016-v2_Run2015A_TrackingLikeMC_CFF_Dec17/171204_163336/0000/'
sam["data_ZeroBias5_Run2015A-27Jan2016-v2"]["DS"]='/ZeroBias5/Run2015A-27Jan2016-v2/RECO'

sam["data_ZeroBias6_Run2015A-27Jan2016-v2"]={}
sam["data_ZeroBias6_Run2015A-27Jan2016-v2"]["crabJobs"]=0
sam["data_ZeroBias6_Run2015A-27Jan2016-v2"]["GT"]=''
sam["data_ZeroBias6_Run2015A-27Jan2016-v2"]["name"]='ddata_ZeroBias6_Run2015A-27Jan2016-v2'
sam["data_ZeroBias6_Run2015A-27Jan2016-v2"]["isData"]=True
sam["data_ZeroBias6_Run2015A-27Jan2016-v2"]["numEvents"]=-1
sam["data_ZeroBias6_Run2015A-27Jan2016-v2"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/ZeroBias6/ZeroBias6-27Jan2016-v2_Run2015A_TrackingLikeMC_Dec17_CFF/171205_202216/0000/'
sam["data_ZeroBias6_Run2015A-27Jan2016-v2"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/ZeroBias6/ZeroBias6-27Jan2016-v2_Run2015A_TrackingLikeMC_Dec17_CFF/171205_202216/0000/'
sam["data_ZeroBias6_Run2015A-27Jan2016-v2"]["json"]=''
sam["data_ZeroBias6_Run2015A-27Jan2016-v2"]["lumiMinBias"]=-1
sam["data_ZeroBias6_Run2015A-27Jan2016-v2"]["XS"]=-1
sam["data_ZeroBias6_Run2015A-27Jan2016-v2"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/ZeroBias6/ZeroBias6-27Jan2016-v2_Run2015A_TrackingLikeMC_Dec17_CFF/171205_202216/0000/'
sam["data_ZeroBias6_Run2015A-27Jan2016-v2"]["DS"]='/ZeroBias6/Run2015A-27Jan2016-v2/RECO'

sam["data_ZeroBias7_Run2015A-27Jan2016-v2"]={}
sam["data_ZeroBias7_Run2015A-27Jan2016-v2"]["crabJobs"]=0
sam["data_ZeroBias7_Run2015A-27Jan2016-v2"]["GT"]=''
sam["data_ZeroBias7_Run2015A-27Jan2016-v2"]["name"]='ddata_ZeroBias7_Run2015A-27Jan2016-v2'
sam["data_ZeroBias7_Run2015A-27Jan2016-v2"]["isData"]=True
sam["data_ZeroBias7_Run2015A-27Jan2016-v2"]["numEvents"]=-1
sam["data_ZeroBias7_Run2015A-27Jan2016-v2"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/ZeroBias7/ZeroBias7-27Jan2016-v2_Run2015A_TrackingLikeMC_CFF_Dec17/171204_163553/0000/'
sam["data_ZeroBias7_Run2015A-27Jan2016-v2"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/ZeroBias7/ZeroBias7-27Jan2016-v2_Run2015A_TrackingLikeMC_CFF_Dec17/171204_163553/0000/'
sam["data_ZeroBias7_Run2015A-27Jan2016-v2"]["json"]=''
sam["data_ZeroBias7_Run2015A-27Jan2016-v2"]["lumiMinBias"]=-1
sam["data_ZeroBias7_Run2015A-27Jan2016-v2"]["XS"]=-1
sam["data_ZeroBias7_Run2015A-27Jan2016-v2"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/ZeroBias7/ZeroBias7-27Jan2016-v2_Run2015A_TrackingLikeMC_CFF_Dec17/171204_163553/0000/'
sam["data_ZeroBias7_Run2015A-27Jan2016-v2"]["DS"]='/ZeroBias7/Run2015A-27Jan2016-v2/RECO'

sam["data_ZeroBias8_Run2015A-27Jan2016-v2"]={}
sam["data_ZeroBias8_Run2015A-27Jan2016-v2"]["crabJobs"]=0
sam["data_ZeroBias8_Run2015A-27Jan2016-v2"]["GT"]=''
sam["data_ZeroBias8_Run2015A-27Jan2016-v2"]["name"]='ddata_ZeroBias8_Run2015A-27Jan2016-v2'
sam["data_ZeroBias8_Run2015A-27Jan2016-v2"]["isData"]=True
sam["data_ZeroBias8_Run2015A-27Jan2016-v2"]["numEvents"]=-1
sam["data_ZeroBias8_Run2015A-27Jan2016-v2"]["pathSE"]='srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/sbaur/ZeroBias8/ZeroBias8-27Jan2016-v2_Run2015A_TrackingLikeMC_CFF_Dec17/171204_163717/0000/'
sam["data_ZeroBias8_Run2015A-27Jan2016-v2"]["pathTrees"]='/XXXTMFTTree/store/user/sbaur/ZeroBias8/ZeroBias8-27Jan2016-v2_Run2015A_TrackingLikeMC_CFF_Dec17/171204_163717/0000/'
sam["data_ZeroBias8_Run2015A-27Jan2016-v2"]["json"]=''
sam["data_ZeroBias8_Run2015A-27Jan2016-v2"]["lumiMinBias"]=-1
sam["data_ZeroBias8_Run2015A-27Jan2016-v2"]["XS"]=-1
sam["data_ZeroBias8_Run2015A-27Jan2016-v2"]["pathPAT"]='/XXXTMFPAT/store/user/sbaur/ZeroBias8/ZeroBias8-27Jan2016-v2_Run2015A_TrackingLikeMC_CFF_Dec17/171204_163717/0000/'
sam["data_ZeroBias8_Run2015A-27Jan2016-v2"]["DS"]='/ZeroBias8/Run2015A-27Jan2016-v2/RECO'


def fixLocalPaths(sam):
        import os,imp
        if "SmallXAnaDefFile" not in os.environ:
            print "Please set SmallXAnaDefFile environment variable:"
            print "export SmallXAnaDefFile=FullPathToFile"
            raise Exception("Whooops! SmallXAnaDefFile env var not defined")

        anaDefFile = os.environ["SmallXAnaDefFile"]
        mod_dir, filename = os.path.split(anaDefFile)
        mod, ext = os.path.splitext(filename)
        f, filename, desc = imp.find_module(mod, [mod_dir])
        mod = imp.load_module(mod, f, filename, desc)

        localBasePathPAT = mod.PATbasePATH
        localBasePathTrees = mod.TTreeBasePATH

        for s in sam:
            if "pathPAT" in sam[s]:
                sam[s]["pathPAT"] = sam[s]["pathPAT"].replace("XXXTMFPAT", localBasePathPAT)
            if "pathTrees" in sam[s]:
                sam[s]["pathTrees"] = sam[s]["pathTrees"].replace("XXXTMFTTree", localBasePathTrees)
            #print sam[s]["pathPAT"]
            #print sam[s]["pathTrees"]
        return sam
sam = fixLocalPaths(sam)

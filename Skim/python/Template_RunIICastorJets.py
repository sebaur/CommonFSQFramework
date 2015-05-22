anaType="CastorJets"

# root path needs proper XXX
# some stuff needed for crab configuration, e.g. blacklisting
preamble='''
cbSmartCommand="smartCopy"
cbSmartBlackList=""
cbWMS="https://wmscms.cern.ch:7443/glite_wms_wmproxy_server"
skimEfficiencyMethod="getSkimEff"
'''

# point towards your list of samples you want
dsFile="CommonFSQFramework/Skim/python/ds_RunIICastorJets.txt"

# define the util decorator. Functions marked with this wont turn into ds attribute
def util(func):
    setattr(func, "ignore", 1)
    return func
setattr(util, "ignore", 1) # for this function only


def DS(ds):
    return ds

def name(ds):
    split=ds.split("/") 
    if len(split) == 0: return None

    if isData(ds):
        ret = "data_"+split[1]
    else:
        ret = split[1]
    return ret

def isData(ds):
    realData = False
    if "Run201" in ds: realData = True
    return realData

def json(ds):
    realData = isData(ds)
    # they are no data samples yet, no json needed here
    return ""

def crabJobs(ds):
    dsName = name(ds)
    # define to run 100 crab jobs
    # make something more clever, based on number of events in the dataset
    return 100

def numEvents(ds):
    evts = -1
    # list all datasets in ds_RunIICastorJets.txt file
    if "QCD_Pt-15to3000_castorJet_TuneCUETP8M1_Flat_13TeV-pythia8" in ds: evts = 4897399 # from DAS
    if "ReggeGribovPartonMC_castorJet_13TeV-QGSJetII" in ds: evts = 5702011 # from DAS
    if "ReggeGribovPartonMC_castorJet_13TeV-EPOS" in ds: evts = 5702011 # from DAS
    if "MinBias_TuneCUETP8M1_13TeV-pythia8" in ds: evts = 996650 # from DAS 
    return evts

def GT(ds):
    # no data, just get GT from GEN-SIM samples
    return "MCRUN2_74_V8::All"

def XS(ds):
    '''
    Note: all cross sections given in pb
    # http://iopscience.iop.org/0295-5075/96/2/21002
    LHCtotal= 73.5 mili b

    conversion factors cheatsheet:
    nano = 10^-6 mili
    nano = 10^-3 micro
    nano = 10^3 pico
    '''
    # if real data return nothing, not needed here but keep for other Templates
    realData = isData(ds)
    if realData:
        return -1

    # list all datasets in ds_RunIICastorJets.txt
    # Give all XS in pb
    s = {}
    s["QCD_Pt-15to3000_castorJet_TuneCUETP8M1_Flat_13TeV-pythia8"] = 986200000.0*0.15 # from McM * filter efficiency from McM
    s["ReggeGribovPartonMC_castorJet_13TeV-EPOS"] = 72970000000.0*0.0253 # from Config File * filter efficiency from McM
    s["ReggeGribovPartonMC_castorJet_13TeV-QGSJetII"] = 74610000000.0*0.0189 # from Config File * filter efficiency from McM
    s["MinBias_TuneCUETP8M1_13TeV-pythia8"] = 78418400000.0 # from McM

    dsName = name(ds)
    if dsName in s:
        return s[dsName]
    else:
        print "FIXME - XS missing for", dsName
        print '    s["'+dsName+'"] = '
    return -1

@util
def getLumi(ds, trg):
    '''
    all lumi values here should be given in picob
    '''
    s = {}
    s.setdefault("QGSJetII", {})
    s.setdefault("EPOS", {})
    s.setdefault("Pythia8QCD", {})
    s.setdefault("Pythia8MinBias", {})

    # add all MC and data samples - for data get from json file in future?
    s["QGSJetII"]["ReggeGribovPartonMC_castorJet_13TeV-QGSJetII"] = numEvents(ds)/XS(ds) # pb, Nevents/XS
    s["EPOS"]["ReggeGribovPartonMC_castorJet_13TeV-EPOS"] = numEvents(ds)/XS(ds) # pb, Nevents/XS
    s["Pythia8QCD"]["QCD_Pt-15to3000_castorJet_TuneCUETP8M1_Flat_13TeV-pythia8"] = numEvents(ds)/XS(ds) # pb, Nevents/XS
    s["Pythia8MinBias"]["MinBias_TuneCUETP8M1_13TeV-pythia8"] = numEvents(ds)/XS(ds) # pb, Nevents/XS

    dsName = name(ds)
    if dsName in s[trg]:
        return float(s[trg][dsName])

    print "Problem with lumi!", ds
    return "crashMe"

#def lumiMinBias(ds):
#    return getLumi(ds,"minbias")


# could useful in the future
@util
def onTheFlyCustomization():
    ret = ""

    return ret
#setattr(onTheFlyCustomization, "ignore", 1)


fun = {}
import copy,types
glob = copy.copy(globals())
for f in glob:
    if type(glob[f])==types.FunctionType:
        if hasattr(glob[f],"ignore"): 
            print "Skip", f
            continue
        #print f
        fun[f]=glob[f]





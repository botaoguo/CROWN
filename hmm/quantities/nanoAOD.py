from code_generation.quantity import NanoAODQuantity

run = NanoAODQuantity("run")
luminosityBlock = NanoAODQuantity("luminosityBlock")
event = NanoAODQuantity("event")
LHE_Njets = NanoAODQuantity("LHE_Njets")
prefireWeight = NanoAODQuantity("L1PreFiringWeight_Nom")

Tau_pt = NanoAODQuantity("Tau_pt")
Tau_eta = NanoAODQuantity("Tau_eta")
Tau_phi = NanoAODQuantity("Tau_phi")
Tau_mass = NanoAODQuantity("Tau_mass")
Tau_dz = NanoAODQuantity("Tau_dz")
Tau_dxy = NanoAODQuantity("Tau_dxy")
Tau_charge = NanoAODQuantity("Tau_charge")
Tau_decayMode = NanoAODQuantity("Tau_decayMode")
Tau_genMatch = NanoAODQuantity("Tau_genPartFlav")
Tau_IDraw = NanoAODQuantity("Tau_rawDeepTau2017v2p1VSjet")
Tau_indexToGen = NanoAODQuantity("Tau_genPartIdx")
Tau_associatedJet = NanoAODQuantity("Tau_jetIdx")
Tau_ID_vsJet = NanoAODQuantity("Tau_idDeepTau2017v2p1VSjet")
Tau_ID_vsEle = NanoAODQuantity("Tau_idDeepTau2017v2p1VSe")
Tau_ID_vsMu = NanoAODQuantity("Tau_idDeepTau2017v2p1VSmu")

Muon_pt = NanoAODQuantity("Muon_pt")
Muon_eta = NanoAODQuantity("Muon_eta")
Muon_phi = NanoAODQuantity("Muon_phi")
Muon_mass = NanoAODQuantity("Muon_mass")
Muon_dz = NanoAODQuantity("Muon_dz")
Muon_dxy = NanoAODQuantity("Muon_dxy")
Muon_charge = NanoAODQuantity("Muon_charge")
Muon_genMatch = NanoAODQuantity("Muon_genPartFlav")
Muon_indexToGen = NanoAODQuantity("Muon_genPartIdx")
Muon_sip3d = NanoAODQuantity("Muon_sip3d") # vh
Muon_pfRelIso04_all = NanoAODQuantity("Muon_pfRelIso04_all") # vh
Muon_mvaTTH = NanoAODQuantity("Muon_mvaTTH")

Electron_pt = NanoAODQuantity("Electron_pt")
Electron_eta = NanoAODQuantity("Electron_eta")
Electron_dxy = NanoAODQuantity("Electron_dxy")
Electron_dz = NanoAODQuantity("Electron_dz")
Electron_phi = NanoAODQuantity("Electron_phi")
Electron_mass = NanoAODQuantity("Electron_mass")
Electron_iso = NanoAODQuantity("Electron_pfRelIso03_all")
Electron_charge = NanoAODQuantity("Electron_charge")
Electron_indexToGen = NanoAODQuantity("Electron_genPartIdx")
# write by botao
Electron_sip3d = NanoAODQuantity("Electron_sip3d")
Electron_mvaFall17V2noIso_WP90 = NanoAODQuantity("Electron_mvaFall17V2noIso_WP90")
Electron_convVeto = NanoAODQuantity("Electron_convVeto")
Electron_lostHits = NanoAODQuantity("Electron_lostHits")
Electron_mvaTTH = NanoAODQuantity("Electron_mvaTTH")
Electron_pdgId = NanoAODQuantity("Electron_pdgId")
Muon_pdgId = NanoAODQuantity("Muon_pdgId")
# end write

GenJet_pt = NanoAODQuantity("GenJet_pt")
GenJet_eta = NanoAODQuantity("GenJet_eta")
GenJet_phi = NanoAODQuantity("GenJet_phi")

Jet_eta = NanoAODQuantity("Jet_eta")
Jet_phi = NanoAODQuantity("Jet_phi")
Jet_pt = NanoAODQuantity("Jet_pt")
Jet_mass = NanoAODQuantity("Jet_mass")
Jet_area = NanoAODQuantity("Jet_area")
Jet_flavor = NanoAODQuantity("Jet_hadronFlavour")
Jet_rawFactor = NanoAODQuantity("Jet_rawFactor")
Jet_ID = NanoAODQuantity("Jet_jetId")
Jet_PUID = NanoAODQuantity("Jet_puId")
Jet_associatedGenJet = NanoAODQuantity("Jet_genJetIdx")
#BJet_discriminator = NanoAODQuantity("Jet_btagDeepFlavB") # DeepFlavour
BJet_discriminator = NanoAODQuantity("Jet_btagDeepB") # vh DeepCSV

Pileup_nTrueInt = NanoAODQuantity("Pileup_nTrueInt")
rho = NanoAODQuantity("Pileup_pudensity")

GenParticle_eta = NanoAODQuantity("GenPart_eta")
GenParticle_phi = NanoAODQuantity("GenPart_phi")
GenParticle_pt = NanoAODQuantity("GenPart_pt")
GenParticle_mass = NanoAODQuantity("GenPart_mass")
GenParticle_pdgId = NanoAODQuantity("GenPart_pdgId")
GenParticle_status = NanoAODQuantity("GenPart_status")
GenParticle_statusFlags = NanoAODQuantity("GenPart_statusFlags")
GenParticle_motherid = NanoAODQuantity("GenPart_genPartIdxMother")

## Trigger Objects
TriggerObject_bit = NanoAODQuantity("TrigObj_filterBits")
TriggerObject_pt = NanoAODQuantity("TrigObj_pt")
TriggerObject_eta = NanoAODQuantity("TrigObj_eta")
TriggerObject_phi = NanoAODQuantity("TrigObj_phi")
TriggerObject_id = NanoAODQuantity("TrigObj_id")

## HTXS quantities
HTXS_Higgs_pt = NanoAODQuantity("HTXS_Higgs_pt")
HTXS_Higgs_y = NanoAODQuantity("HTXS_Higgs_y")
HTXS_njets30 = NanoAODQuantity("HTXS_njets30")
HTXS_stage_0 = NanoAODQuantity("HTXS_stage_0")
HTXS_stage_1_pTjet30 = NanoAODQuantity("HTXS_stage_1_pTjet30")
HTXS_stage1_1_fine_cat_pTjet30GeV = NanoAODQuantity("HTXS_stage1_1_fine_cat_pTjet30GeV")
HTXS_stage1_2_cat_pTjet30GeV = NanoAODQuantity("HTXS_stage1_2_cat_pTjet30GeV")
HTXS_stage1_2_fine_cat_pTjet30GeV = NanoAODQuantity("HTXS_stage1_2_fine_cat_pTjet30GeV")

## MET quantities
## TODO Swich to Puppi versions for METCOV and Signifiance as soon as they are in the nanoAOD
MET_covXX = NanoAODQuantity("MET_covXX")
MET_covXY = NanoAODQuantity("MET_covXY")
MET_covYY = NanoAODQuantity("MET_covYY")
MET_significance = NanoAODQuantity("MET_significance")

MET_phi = NanoAODQuantity("PuppiMET_phi")
MET_pt = NanoAODQuantity("PuppiMET_pt")
MET_sumEt = NanoAODQuantity("PuppiMET_sumEt")

PFMET_phi = NanoAODQuantity("MET_phi")
PFMET_pt = NanoAODQuantity("MET_pt")
PFMET_sumEt = NanoAODQuantity("MET_sumEt")

## Embedding Quantities
genWeight = NanoAODQuantity("genWeight")
TauEmbedding_initialMETEt = NanoAODQuantity("TauEmbedding_initialMETEt")
TauEmbedding_initialMETphi = NanoAODQuantity("TauEmbedding_initialMETphi")
TauEmbedding_initialPuppiMETEt = NanoAODQuantity("TauEmbedding_initialPuppiMETEt")
TauEmbedding_initialPuppiMETphi = NanoAODQuantity("TauEmbedding_initialPuppiMETphi")
TauEmbedding_isMediumLeadingMuon = NanoAODQuantity("TauEmbedding_isMediumLeadingMuon")
TauEmbedding_isMediumTrailingMuon = NanoAODQuantity("TauEmbedding_isMediumTrailingMuon")
TauEmbedding_isTightLeadingMuon = NanoAODQuantity("TauEmbedding_isTightLeadingMuon")
TauEmbedding_isTightTrailingMuon = NanoAODQuantity("TauEmbedding_isTightTrailingMuon")
TauEmbedding_InitialPairCandidates = NanoAODQuantity(
    "TauEmbedding_nInitialPairCandidates"
)
TauEmbedding_SelectionOldMass = NanoAODQuantity("TauEmbedding_SelectionOldMass")
TauEmbedding_SelectionNewMass = NanoAODQuantity("TauEmbedding_SelectionNewMass")

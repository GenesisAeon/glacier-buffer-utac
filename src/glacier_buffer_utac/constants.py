"""Verified constants for glacial hydrological buffer / downstream cascade science."""

PACKAGE_ID = 99

# --- Peak water: the glacial hydrological buffer itself ------------------

HUSS_HOCK_2018_CITATION = (
    "Huss, M., Hock, R. (2018). Global-scale hydrological response to "
    "future glacier mass loss. Nature Climate Change, 8, 135-140. "
    "DOI: 10.1038/s41558-017-0049-x"
)
HUSS_HOCK_2018_DOI = "10.1038/s41558-017-0049-x"

PEAK_WATER_NOTE = (
    "Peak water: as glaciers lose mass under warming, annual glacier "
    "runoff in a drainage basin first rises (a temporary bonus from "
    "accelerated melt) before reaching a maximum ('peak water') and then "
    "declining as the shrinking ice mass can no longer sustain the same "
    "melt volume. Huss & Hock (2018) model this for 56 large-scale "
    "glacierized basins to 2100: peak water occurs later, and the "
    "post-peak decline is more severe, in basins with larger glaciers and "
    "higher ice-cover fractions. Runoff typically increases in early "
    "summer but decreases in late summer even before the basin-wide "
    "annual peak is reached -- glacier wastage measurably affects "
    "streamflow even in basins with limited glacier cover."
)

# --- Downstream cascade: synthesis --------------------------------------

MILNER_2017_CITATION = (
    "Milner, A.M., Khamis, K., Battin, T.J., Brittain, J.E., Barrand, "
    "N.E., Fureder, L., Cauvy-Fraunie, S., Gislason, G.M., Jacobsen, D., "
    "Hannah, D.M., Hodson, A.J., Hood, E., Lencioni, V., Olafsson, J.S., "
    "Robinson, C.T., Tranter, M., Brown, L.E. (2017). Glacier shrinkage "
    "driving global changes in downstream systems. PNAS, 114(37), "
    "9770-9778. DOI: 10.1073/pnas.1619807114"
)
MILNER_2017_DOI = "10.1073/pnas.1619807114"

CASCADE_SYNTHESIS_NOTE = (
    "Milner et al. (2017) synthesize how glacier shrinkage propagates "
    "into downstream systems through multiple, linked pathways: altered "
    "hydrological regimes (timing/magnitude of flow), sediment transport, "
    "and biogeochemical/contaminant fluxes -- with consequences for river, "
    "wetland and near-shore marine biota. This is a real, multi-author "
    "review synthesis, not a single measured end-to-end causal chain: the "
    "strength of each link is basin-specific and not uniform globally."
)

# --- Downstream cascade: quantified experimental/field evidence ---------

CAUVY_FRAUNIE_2016_CITATION = (
    "Cauvy-Fraunie, S., Andino, P., Espinosa, R., Calvez, R., Jacobsen, "
    "D., Dangles, O. (2016). Ecological responses to experimental "
    "glacier-runoff reduction in alpine rivers. Nature Communications, "
    "7, 12025. DOI: 10.1038/ncomms12025"
)
CAUVY_FRAUNIE_2016_DOI = "10.1038/ncomms12025"

# Experimental flow reduction applied in the manipulated stream channel, percent
EXPERIMENTAL_FLOW_REDUCTION_PCT = 31.0

# Benthic fauna density increase in the flow-reduced channel, factor (mean +/- SD)
FAUNA_DENSITY_INCREASE_FACTOR = 6.5
FAUNA_DENSITY_INCREASE_UNCERTAINTY = 1.8

# Time for the faunal community to return to its pre-perturbation composition, months
RECOVERY_TIME_MONTHS_MIN = 14
RECOVERY_TIME_MONTHS_MAX = 16

# Glacier-cover threshold (percent of catchment) below which the 33-site field
# survey found an abrupt increase in algal and herbivore biomass
GLACIER_COVER_THRESHOLD_PCT = 11.0

CAUVY_FRAUNIE_CAVEAT_NOTE = (
    "Cauvy-Fraunie et al. (2016) combine a single experimental flow-"
    "reduction channel with a 33-site field survey in Ecuadorian Andes "
    "catchments. The 11% glacier-cover threshold and the 14-16 month "
    "recovery time are specific to that study system; they are reported "
    "here as documented data points, not as universal constants for all "
    "glacier-fed rivers."
)

# --- Downstream cascade: desynchronization of seasonal resource dynamics -

DUNKLE_2025_CITATION = (
    "Dunkle, M.R., Bellmore, J.R., Fellman, J.B., Hood, E.W., Caudill, "
    "C.C. (2025). Loss of meltwater from glaciers and snowpack may "
    "increase synchrony of river habitats and resources in mountain "
    "watersheds. Ecology, 106(4), e70023. DOI: 10.1002/ecy.70023"
)
DUNKLE_2025_DOI = "10.1002/ecy.70023"

DESYNCHRONY_LOSS_NOTE = (
    "Dunkle et al. (2025) show that glacier-, snow- and rain-fed streams "
    "normally have distinct, asynchronous seasonal patterns of "
    "temperature, flow and resource production (detritus, biofilm, "
    "invertebrates, fish biomass). As meltwater contributions decline, "
    "this natural desynchronization is lost: streams across a watershed "
    "converge toward the same seasonal timing, which can reduce overall "
    "ecological stability -- especially for mobile consumers that "
    "otherwise track resource waves across a landscape."
)

# --- Wetland-specific spatial heterogeneity -------------------------------

XUAN_2026_CITATION = (
    "Xuan, D., Becker, R., Vargas Valverde, M., Davies, B.J., Ely, J.C., "
    "King, O. et al. (2026). Spatial Patterns of Glacier-Wetland "
    "Hydrological Connectivity in the Rapidly Deglaciating Peruvian "
    "Andes. Earth's Future. DOI: 10.1029/2026EF008149"
)
XUAN_2026_DOI = "10.1029/2026EF008149"

WETLAND_DEPENDENCE_NOTE = (
    "High-altitude Andean wetlands (bofedales/HAWA) are not uniformly "
    "glacier-dependent. Xuan et al. (2026) show the dependence is "
    "spatially heterogeneous: wetlands close to a glacier margin are "
    "strongly sustained by meltwater, particularly during dry seasons and "
    "droughts, while glacier influence on hydrology decreases within a "
    "few kilometers downstream as precipitation, groundwater recharge and "
    "catchment storage increasingly dominate. Wetlands far from glaciers "
    "are primarily precipitation- and groundwater-fed and show little "
    "direct response to glacier retreat."
)

CASCADE_HONESTY_NOTE = (
    "The four-stage chain glacier -> wetland -> vegetation -> fauna is "
    "directionally supported by the cited literature at each individual "
    "link, but no single study measures the full chain end-to-end. "
    "Treat it as a well-motivated hypothesis network, not a validated "
    "single causal pathway -- see DISCLAIMER.md."
)

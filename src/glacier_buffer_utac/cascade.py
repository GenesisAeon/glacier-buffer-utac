"""Glacial hydrological buffer state and downstream buffer-loss cascade."""

from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    CAUVY_FRAUNIE_2016_CITATION,
    DUNKLE_2025_CITATION,
    EXPERIMENTAL_FLOW_REDUCTION_PCT,
    FAUNA_DENSITY_INCREASE_FACTOR,
    FAUNA_DENSITY_INCREASE_UNCERTAINTY,
    GLACIER_COVER_THRESHOLD_PCT,
    MILNER_2017_CITATION,
    RECOVERY_TIME_MONTHS_MAX,
    RECOVERY_TIME_MONTHS_MIN,
    XUAN_2026_CITATION,
)


@dataclass(frozen=True)
class CascadeStage:
    """One documented link in the glacier -> wetland -> vegetation -> fauna chain."""

    name: str
    mechanism: str
    citation: str


ALL_CASCADE_STAGES: tuple[CascadeStage, ...] = (
    CascadeStage(
        name="glacier_hydrology",
        mechanism=(
            "Glacial melt buffers summer/drought low flow; buffer capacity "
            "declines once a basin passes 'peak water'."
        ),
        citation=MILNER_2017_CITATION,
    ),
    CascadeStage(
        name="wetland",
        mechanism=(
            "Wetlands near a glacier margin depend on meltwater for dry-"
            "season base flow; dependence fades with distance from the "
            "glacier as precipitation/groundwater dominate."
        ),
        citation=XUAN_2026_CITATION,
    ),
    CascadeStage(
        name="vegetation_and_fauna",
        mechanism=(
            "Reduced/altered meltwater flow shifts algal, herbivore and "
            "benthic invertebrate biomass and composition, with multi-"
            "month recovery lags after a perturbation."
        ),
        citation=CAUVY_FRAUNIE_2016_CITATION,
    ),
    CascadeStage(
        name="seasonal_desynchronization",
        mechanism=(
            "Loss of meltwater synchronizes the seasonal resource dynamics "
            "of previously asynchronous glacier-, snow- and rain-fed "
            "streams, reducing watershed-scale ecological stability."
        ),
        citation=DUNKLE_2025_CITATION,
    ),
)


def is_below_glacier_cover_threshold(glacier_cover_pct: float) -> bool:
    """Return True if catchment glacier cover is below the field-survey threshold.

    Cauvy-Fraunie et al. (2016) found an abrupt increase in algal/herbivore
    biomass below 11% glacier cover across a 33-site field survey.
    """
    if not 0.0 <= glacier_cover_pct <= 100.0:
        raise ValueError(f"glacier_cover_pct must be in [0, 100], got {glacier_cover_pct}")
    return glacier_cover_pct < GLACIER_COVER_THRESHOLD_PCT


def recovery_time_months_range() -> tuple[int, int]:
    """Return the documented (min, max) faunal-community recovery time in months."""
    return (RECOVERY_TIME_MONTHS_MIN, RECOVERY_TIME_MONTHS_MAX)


@dataclass(frozen=True)
class ExperimentalFlowReduction:
    """The single documented experimental data point from Cauvy-Fraunie et al. (2016)."""

    flow_reduction_pct: float
    density_increase_factor: float
    density_increase_uncertainty: float
    citation: str


DOCUMENTED_FLOW_REDUCTION_EXPERIMENT = ExperimentalFlowReduction(
    flow_reduction_pct=EXPERIMENTAL_FLOW_REDUCTION_PCT,
    density_increase_factor=FAUNA_DENSITY_INCREASE_FACTOR,
    density_increase_uncertainty=FAUNA_DENSITY_INCREASE_UNCERTAINTY,
    citation=CAUVY_FRAUNIE_2016_CITATION,
)


def buffer_sensitivity_multiplier(ice_mass_fraction: float) -> float:
    """Illustrative sensitivity of downstream flow to a drought/heat anomaly.

    NOT a fitted or literature-derived equation. This is a simplified,
    monotonic stand-in for the qualitative relationship described in
    Huss & Hock (2018) and the GenesisAeon-Diskurs dialogue: as remaining
    glacier ice mass (relative to a baseline, 1.0 = undiminished) shrinks,
    the basin's runoff becomes more sensitive to a given drought/heat
    anomaly (partial d Q / d D increases). Returns 1.0 at full ice mass and
    grows without bound as ice_mass_fraction approaches 0.
    """
    if not 0.0 < ice_mass_fraction <= 1.0:
        raise ValueError(
            f"ice_mass_fraction must be in (0, 1], got {ice_mass_fraction}"
        )
    return 1.0 / ice_mass_fraction


def wetland_dependence_category(near_glacier_margin: bool) -> str:
    """Categorize a wetland's meltwater dependence per Xuan et al. (2026).

    Returns 'glacier_meltwater_dominated' for wetlands near a glacier
    margin, or 'precipitation_groundwater_dominated' for wetlands beyond
    the (basin-specific) few-kilometer zone where glacier influence fades.
    This is a coarse two-category simplification of a continuous, basin-
    specific spatial pattern -- see DISCLAIMER.md.
    """
    if near_glacier_margin:
        return "glacier_meltwater_dominated"
    return "precipitation_groundwater_dominated"

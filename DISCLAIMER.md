# DISCLAIMER — Real Science, No Framework Bridge

> **Why no UTAC/CREP/AFET bridge:** not only because the cited literature
> already provides the necessary quantitative structure -- a deliberate
> choice. This project's highly speculative AFET/UTAC experiments must
> never stand in the way of climate/ecology topics being accessible and
> usable to people who don't work inside that construct and aren't
> looking for renormalization groups. Real, checkable science, without
> the burden of an unproven framework. See `PACKAGE_REGISTRY.md`'s "Why
> no UTAC/CREP/AFET bridge in the climate/ecology series" (2026-08-31) in
> the GenesisAeon workspace root for the full canonical note.


**Status: Real, verified science + NO UTAC/CREP/AFET bridge**

## What this is

- **Peak water** (Huss & Hock 2018, *Nature Climate Change*): a real,
  quantitatively modeled phenomenon in glacier hydrology. As glaciers
  lose mass, basin-scale glacier runoff first rises, then reaches a
  maximum, then declines. The decline phase is what removes the
  hydrological buffer that dampened summer/drought low-water periods —
  exactly the mechanism described in the GenesisAeon-Diskurs dialogue
  this package is built from.
- **A real, quantified downstream ecological response** (Cauvy-Fraunie
  et al. 2016, *Nature Communications*): an experimental 31% flow
  reduction produced a 6.5x (±1.8) increase in benthic fauna density
  within two weeks, and a 33-site field survey found an abrupt shift in
  algal/herbivore biomass below 11% catchment glacier cover. Recovery to
  pre-perturbation community composition took 14–16 months.
- **A real synthesis review** (Milner et al. 2017, *PNAS*) of how
  glacier shrinkage propagates into downstream hydrology, sediment
  transport, biogeochemistry and biota.
- **A real, very recent finding on wetland spatial heterogeneity** (Xuan
  et al. 2026, *Earth's Future*): glacier-meltwater dependence of
  high-altitude Andean wetlands is not uniform — it is strong near a
  glacier margin and fades within a basin-specific distance as
  precipitation and groundwater take over.
- **A real desynchronization effect** (Dunkle et al. 2025, *Ecology*):
  losing meltwater removes the natural seasonal asynchrony between
  glacier-, snow- and rain-fed streams, potentially reducing
  watershed-scale ecological stability.

## What this is NOT

- **Not a single, end-to-end measured causal chain.** The dialogue this
  package originates from (`Gletscher_resilienzpuffer_Wasserpegel.txt`)
  describes a cascade: glacier → wetland → vegetation/forest → fauna.
  Each individual link is literature-supported (see `ALL_CASCADE_STAGES`
  in `cascade.py`), but no single study traces glacier mass loss all the
  way through to a specific fauna outcome in one measurement. Treat the
  cascade as a well-motivated hypothesis network assembled from several
  papers, not a validated single pathway.
- **`buffer_sensitivity_multiplier()` is illustrative, not fitted.** It
  is a simplified `1 / ice_mass_fraction` stand-in for the qualitative
  "smaller buffer → more sensitive to drought/heat anomalies"
  relationship discussed in the source dialogue and consistent with Huss
  & Hock (2018)'s findings. It is not a regression coefficient or
  equation taken from any cited paper.
- **The 11% glacier-cover threshold and 14–16 month recovery time are
  study-specific**, not universal constants. They come from Ecuadorian
  Andes catchments (Cauvy-Fraunie et al. 2016) and may not transfer
  directly to, say, Alpine or Himalayan basins.
- **No UTAC/CREP/AFET bridge.** This is a real, standalone glacial-
  hydrology and downstream-ecology topic; the cited papers already
  provide the relevant quantitative structure without this ecosystem's
  cross-domain vocabulary.

## References

- Huss, M., Hock, R. (2018). *Nature Climate Change*, 8, 135-140. DOI:
  10.1038/s41558-017-0049-x.
- Milner, A.M. et al. (2017). *PNAS*, 114(37), 9770-9778. DOI:
  10.1073/pnas.1619807114.
- Cauvy-Fraunie, S. et al. (2016). *Nature Communications*, 7, 12025.
  DOI: 10.1038/ncomms12025.
- Dunkle, M.R. et al. (2025). *Ecology*, 106(4), e70023. DOI:
  10.1002/ecy.70023.
- Xuan, D. et al. (2026). *Earth's Future*. DOI: 10.1029/2026EF008149.

All verified directly (2026-08-10) via WebSearch/WebFetch against the
publisher/PMC record for each paper. Originating dialogue:
`Gletscher_resilienzpuffer_Wasserpegel.txt` (Johann + ChatGPT + Grok,
GenesisAeon resilience-buffer discussion).

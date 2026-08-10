# glacier-buffer-utac

GenesisAeon Package 99 — real glacial hydrological buffer ("peak water")
and downstream buffer-loss cascade science. **Deliberately has no
UTAC/CREP/AFET bridge** — see [DISCLAIMER.md](DISCLAIMER.md).

## What's real here

- Huss & Hock (2018, *Nature Climate Change*): "peak water" — glacier
  runoff rises, peaks, then declines as ice mass shrinks; the decline
  removes a real hydrological buffer against summer/drought low water.
- Cauvy-Fraunie et al. (2016, *Nature Communications*): experimental
  31% flow reduction → 6.5x (±1.8) benthic fauna density increase within
  2 weeks; 14–16 months to recover; an 11% glacier-cover threshold for
  abrupt algal/herbivore biomass shifts (33-site field survey).
- Milner et al. (2017, *PNAS*): synthesis review of glacier shrinkage
  propagating into downstream hydrology, sediment and biogeochemistry.
- Dunkle et al. (2025, *Ecology*): loss of meltwater desynchronizes
  previously asynchronous glacier-/snow-/rain-fed stream resource
  dynamics.
- Xuan et al. (2026, *Earth's Future*): wetland glacier-meltwater
  dependence is spatially heterogeneous — strong near the glacier
  margin, fading with distance.
- The full glacier → wetland → vegetation → fauna cascade is honestly
  represented as a **literature-supported hypothesis network**, not a
  single measured causal chain — see [DISCLAIMER.md](DISCLAIMER.md).

## Quickstart

```bash
pip install glacier-buffer-utac
```

```python
from glacier_buffer_utac import (
    ALL_CASCADE_STAGES,
    is_below_glacier_cover_threshold,
    buffer_sensitivity_multiplier,
    recovery_time_months_range,
)

for stage in ALL_CASCADE_STAGES:
    print(stage.name, "--", stage.mechanism)

print(is_below_glacier_cover_threshold(8.0))   # True
print(buffer_sensitivity_multiplier(0.3))       # 3.33... -- more sensitive as ice shrinks
print(recovery_time_months_range())             # (14, 16)
```

## Development

```bash
pip install -e ".[dev]"
pre-commit install
ruff check src tests
mypy src
pytest
```

## Citation

See [CITATION.cff](CITATION.cff) and [.zenodo.json](.zenodo.json).

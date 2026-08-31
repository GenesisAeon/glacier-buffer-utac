"""Tests for glacier-buffer-utac."""

import pytest

from glacier_buffer_utac import (
    ALL_CASCADE_STAGES,
    DOCUMENTED_FLOW_REDUCTION_EXPERIMENT,
    GLACIER_COVER_THRESHOLD_PCT,
    PACKAGE_ID,
    RECOVERY_TIME_MONTHS_MAX,
    RECOVERY_TIME_MONTHS_MIN,
    __version__,
    buffer_sensitivity_multiplier,
    is_below_glacier_cover_threshold,
    recovery_time_months_range,
    wetland_dependence_category,
)


def test_version():
    assert __version__ == "1.0.1"


def test_package_id():
    assert PACKAGE_ID == 99


def test_all_cascade_stages_has_four_entries():
    assert len(ALL_CASCADE_STAGES) == 4


def test_cascade_stage_names_in_order():
    names = [stage.name for stage in ALL_CASCADE_STAGES]
    assert names == [
        "glacier_hydrology",
        "wetland",
        "vegetation_and_fauna",
        "seasonal_desynchronization",
    ]


def test_every_cascade_stage_has_a_citation():
    for stage in ALL_CASCADE_STAGES:
        assert stage.citation
        assert stage.mechanism


def test_is_below_glacier_cover_threshold_true():
    assert is_below_glacier_cover_threshold(5.0) is True


def test_is_below_glacier_cover_threshold_false():
    assert is_below_glacier_cover_threshold(50.0) is False


def test_is_below_glacier_cover_threshold_uses_constant():
    assert is_below_glacier_cover_threshold(GLACIER_COVER_THRESHOLD_PCT) is False


def test_is_below_glacier_cover_threshold_rejects_out_of_range():
    with pytest.raises(ValueError, match=r"must be in \[0, 100\]"):
        is_below_glacier_cover_threshold(-1.0)
    with pytest.raises(ValueError, match=r"must be in \[0, 100\]"):
        is_below_glacier_cover_threshold(101.0)


def test_recovery_time_months_range():
    assert recovery_time_months_range() == (14, 16)
    assert recovery_time_months_range() == (
        RECOVERY_TIME_MONTHS_MIN,
        RECOVERY_TIME_MONTHS_MAX,
    )


def test_documented_flow_reduction_experiment_values():
    exp = DOCUMENTED_FLOW_REDUCTION_EXPERIMENT
    assert exp.flow_reduction_pct == 31.0
    assert exp.density_increase_factor == 6.5
    assert exp.density_increase_uncertainty == 1.8
    assert exp.citation


def test_buffer_sensitivity_multiplier_at_full_ice_mass():
    assert buffer_sensitivity_multiplier(1.0) == 1.0


def test_buffer_sensitivity_multiplier_increases_as_ice_shrinks():
    low_loss = buffer_sensitivity_multiplier(0.8)
    high_loss = buffer_sensitivity_multiplier(0.2)
    assert high_loss > low_loss > 1.0


def test_buffer_sensitivity_multiplier_rejects_zero_and_negative():
    with pytest.raises(ValueError, match=r"must be in \(0, 1\]"):
        buffer_sensitivity_multiplier(0.0)
    with pytest.raises(ValueError, match=r"must be in \(0, 1\]"):
        buffer_sensitivity_multiplier(-0.5)


def test_buffer_sensitivity_multiplier_rejects_above_one():
    with pytest.raises(ValueError, match=r"must be in \(0, 1\]"):
        buffer_sensitivity_multiplier(1.5)


def test_wetland_dependence_category_near_glacier():
    assert wetland_dependence_category(True) == "glacier_meltwater_dominated"


def test_wetland_dependence_category_far_from_glacier():
    assert wetland_dependence_category(False) == "precipitation_groundwater_dominated"

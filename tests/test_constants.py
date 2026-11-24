"""
Unit tests validating centralized constants, material integrity, and physical invariants.
"""

import pytest
from pathlib import Path

from config.constants import (
    PROJECT_ROOT,
    SPECS_DIR,
    CAD_DIR,
    SIM_DIR,
    SRC_DIR,
    TESTS_DIR,
    MATERIAL_AL_7075_T6,
    MATERIAL_CFRP_T700,
    MATERIAL_TI_6AL_4V,
    MATERIAL_STEEL_4130,
    FACTOR_OF_SAFETY_YIELD,
    FACTOR_OF_SAFETY_ULTIMATE,
    BUS_VOLTAGE_NOMINAL_V,
    BUS_VOLTAGE_MIN_V,
    BUS_VOLTAGE_MAX_V,
    CRUISE_POWER_DRAW_W,
    PEAK_POWER_DRAW_W,
    SIM_TIME_STEP_S,
    NUMERICAL_CONVERGENCE_REL_TOL,
)


def test_workspace_paths_exist():
    """Verify that all anchored workspace paths exist on the filesystem."""
    for path in [PROJECT_ROOT, SPECS_DIR, CAD_DIR, SIM_DIR, SRC_DIR, TESTS_DIR]:
        assert path.exists(), f"Path {path} does not exist."
        assert path.is_dir(), f"Path {path} is not a directory."


def test_material_property_invariants():
    """Verify physical sanity of materials in database."""
    materials = [
        MATERIAL_AL_7075_T6,
        MATERIAL_CFRP_T700,
        MATERIAL_TI_6AL_4V,
        MATERIAL_STEEL_4130,
    ]
    for mat in materials:
        assert mat.density_kg_m3 > 0.0, f"{mat.name}: density must be positive."
        assert mat.youngs_modulus_gpa > 0.0, f"{mat.name}: Young's modulus must be positive."
        assert 0.0 < mat.poissons_ratio < 0.5, f"{mat.name}: Poisson's ratio out of physical range."
        assert mat.yield_strength_mpa > 0.0, f"{mat.name}: yield strength must be positive."
        assert mat.ultimate_strength_mpa >= mat.yield_strength_mpa, (
            f"{mat.name}: ultimate strength must be >= yield strength."
        )


def test_factors_of_safety():
    """Verify factors of safety comply with aerospace structural standards."""
    assert FACTOR_OF_SAFETY_YIELD >= 1.25, "Yield FoS must be >= 1.25."
    assert FACTOR_OF_SAFETY_ULTIMATE >= 1.50, "Ultimate FoS must be >= 1.50."
    assert FACTOR_OF_SAFETY_ULTIMATE > FACTOR_OF_SAFETY_YIELD


def test_power_bus_envelope():
    """Verify electrical bus voltage and power margins."""
    assert BUS_VOLTAGE_MIN_V < BUS_VOLTAGE_NOMINAL_V < BUS_VOLTAGE_MAX_V
    assert CRUISE_POWER_DRAW_W > 0.0
    assert PEAK_POWER_DRAW_W > CRUISE_POWER_DRAW_W


def test_simulation_numerical_tolerances():
    """Verify simulation time step and convergence tolerances."""
    assert 0.0 < SIM_TIME_STEP_S <= 0.005, "Simulation time step must be <= 5 ms."
    assert 0.0 < NUMERICAL_CONVERGENCE_REL_TOL <= 1e-4

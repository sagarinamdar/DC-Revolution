"""
Unit tests validating system compliance against specifications in specs/system_requirements.md.
"""

import pytest
import numpy as np

from config.constants import (
    CHASSIS_LENGTH_M,
    CHASSIS_WIDTH_M,
    CHASSIS_HEIGHT_M,
    ENVELOPE_LENGTH_MAX_M,
    ENVELOPE_WIDTH_MAX_M,
    ENVELOPE_HEIGHT_MAX_M,
    MAX_GROSS_MASS_KG,
    MASS_CONTINGENCY_MARGIN_FRACTION,
    CG_X_MIN_M,
    CG_X_MAX_M,
    CG_Y_TOLERANCE_M,
    CG_Z_MIN_M,
    CG_Z_MAX_M,
)
from src.physics.mass_properties import compute_system_mass_properties
from sim.analysis.run_baseline_sim import run_baseline_dynamics


def test_req_sys_001_geometric_envelope():
    """REQ-SYS-001: Assembly dimensions must not exceed maximum bounding envelope."""
    assert CHASSIS_LENGTH_M <= ENVELOPE_LENGTH_MAX_M
    assert CHASSIS_WIDTH_M <= ENVELOPE_WIDTH_MAX_M
    assert CHASSIS_HEIGHT_M <= ENVELOPE_HEIGHT_MAX_M


def test_req_sys_002_gross_mass():
    """REQ-SYS-002: Maximum gross operational mass must not exceed 45.000 kg."""
    mass_props = compute_system_mass_properties(include_payload=True, apply_contingency=False)
    assert mass_props.total_mass_kg <= MAX_GROSS_MASS_KG, (
        f"Gross mass {mass_props.total_mass_kg} kg exceeds limit {MAX_GROSS_MASS_KG} kg"
    )


def test_req_sys_003_mass_contingency_margin():
    """REQ-SYS-003: Dry mass design must maintain at least 15% contingency margin."""
    assert MASS_CONTINGENCY_MARGIN_FRACTION >= 0.15


def test_req_sys_004_and_005_center_of_gravity():
    """
    REQ-SYS-004: X_CG must be within [0.500, 0.650] m.
    REQ-SYS-005: |Y_CG| must be <= 0.025 m (symmetric).
    """
    for incl_payload in [True, False]:
        mass_props = compute_system_mass_properties(include_payload=incl_payload)
        cg = mass_props.center_of_mass_m

        assert CG_X_MIN_M <= cg[0] <= CG_X_MAX_M, (
            f"X_CG {cg[0]:.4f} m outside allowable window [{CG_X_MIN_M}, {CG_X_MAX_M}] m "
            f"(Payload={incl_payload})"
        )
        assert abs(cg[1]) <= CG_Y_TOLERANCE_M, (
            f"Y_CG {cg[1]:.4f} m violates symmetry tolerance {CG_Y_TOLERANCE_M} m "
            f"(Payload={incl_payload})"
        )
        assert CG_Z_MIN_M <= cg[2] <= CG_Z_MAX_M, (
            f"Z_CG {cg[2]:.4f} m outside allowable vertical window [{CG_Z_MIN_M}, {CG_Z_MAX_M}] m"
        )


def test_req_sys_010_simulation_stability():
    """REQ-SYS-010: Baseline dynamics must be numerically stable with conserved energy."""
    states, is_stable = run_baseline_dynamics(duration_s=0.5, dt_s=0.001)
    assert is_stable, "Dynamic simulation exhibited excessive numerical energy drift."
    assert len(states) == 500

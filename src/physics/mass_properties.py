"""
Analytical Mass Properties & Center of Gravity (CG) Calculator for DC-Revolution.
Computes total mass, roll-up centers of mass, and the full 3x3 inertia tensor.
"""

from dataclasses import dataclass, field
from typing import List, Tuple
import numpy as np

from config.constants import (
    CHASSIS_LENGTH_M,
    CHASSIS_WIDTH_M,
    CHASSIS_HEIGHT_M,
    TARGET_EMPTY_MASS_KG,
    MAX_PAYLOAD_MASS_KG,
    MASS_CONTINGENCY_MARGIN_FRACTION,
)


@dataclass
class ComponentMassItem:
    name: str
    mass_kg: float
    center_of_mass_m: np.ndarray  # [x, y, z] in datum frame
    inertia_principal_kg_m2: np.ndarray  # [Ixx, Iyy, Izz] about component CG


@dataclass
class SystemMassProperties:
    total_mass_kg: float
    center_of_mass_m: np.ndarray
    inertia_tensor_kg_m2: np.ndarray
    components: List[ComponentMassItem] = field(default_factory=list)


def build_nominal_subsystems() -> List[ComponentMassItem]:
    """Builds the nominal subsystem mass breakdown per DAED-SPEC-BDG-001."""
    # Chassis box: centered along width/height, spanning 0 to CHASSIS_LENGTH_M
    chassis = ComponentMassItem(
        name="Chassis Primary Structure",
        mass_kg=8.200,
        center_of_mass_m=np.array([CHASSIS_LENGTH_M * 0.5, 0.0, CHASSIS_HEIGHT_M * 0.45], dtype=np.float64),
        inertia_principal_kg_m2=np.array([0.45, 1.20, 1.40], dtype=np.float64),
    )

    actuators = ComponentMassItem(
        name="Actuator Subsystem Assembly",
        mass_kg=6.800,
        center_of_mass_m=np.array([0.580, 0.0, 0.160], dtype=np.float64),
        inertia_principal_kg_m2=np.array([0.25, 0.50, 0.60], dtype=np.float64),
    )

    battery = ComponentMassItem(
        name="Energy Storage Pack",
        mass_kg=9.500,
        center_of_mass_m=np.array([0.550, 0.0, 0.120], dtype=np.float64),
        inertia_principal_kg_m2=np.array([0.15, 0.35, 0.40], dtype=np.float64),
    )

    avionics = ComponentMassItem(
        name="Avionics & Flight Computer",
        mass_kg=2.500,
        center_of_mass_m=np.array([0.480, 0.0, 0.220], dtype=np.float64),
        inertia_principal_kg_m2=np.array([0.02, 0.05, 0.06], dtype=np.float64),
    )

    thermal_hardware = ComponentMassItem(
        name="Thermal & Hardware",
        mass_kg=1.500,
        center_of_mass_m=np.array([0.600, 0.0, 0.180], dtype=np.float64),
        inertia_principal_kg_m2=np.array([0.01, 0.03, 0.03], dtype=np.float64),
    )

    payload = ComponentMassItem(
        name="Mission Payload Package",
        mass_kg=MAX_PAYLOAD_MASS_KG,
        center_of_mass_m=np.array([0.620, 0.0, 0.150], dtype=np.float64),
        inertia_principal_kg_m2=np.array([0.30, 0.40, 0.50], dtype=np.float64),
    )

    return [chassis, actuators, battery, avionics, thermal_hardware, payload]


def compute_system_mass_properties(
    include_payload: bool = True,
    apply_contingency: bool = False,
) -> SystemMassProperties:
    """
    Computes total mass, system CG, and system inertia tensor via Parallel Axis Theorem:
    I_system = sum(I_i + m_i * ( (d_i . d_i)*E - d_i outer d_i ))
    """
    subsystems = build_nominal_subsystems()
    if not include_payload:
        subsystems = [s for s in subsystems if "Payload" not in s.name]

    total_mass = sum(s.mass_kg for s in subsystems)
    if apply_contingency:
        total_mass *= (1.0 + MASS_CONTINGENCY_MARGIN_FRACTION)

    # First moment of mass: sum(m_i * r_i)
    first_moment = np.zeros(3, dtype=np.float64)
    for s in subsystems:
        first_moment += s.mass_kg * s.center_of_mass_m

    cg = first_moment / total_mass

    # Inertia tensor about system CG using parallel axis theorem
    inertia_total = np.zeros((3, 3), dtype=np.float64)
    eye = np.eye(3, dtype=np.float64)

    for s in subsystems:
        i_diag = np.diag(s.inertia_principal_kg_m2)
        d = s.center_of_mass_m - cg  # Distance vector from system CG
        d_sq = float(np.dot(d, d))
        parallel_axis_shift = s.mass_kg * (d_sq * eye - np.outer(d, d))
        inertia_total += i_diag + parallel_axis_shift

    return SystemMassProperties(
        total_mass_kg=total_mass,
        center_of_mass_m=cg,
        inertia_tensor_kg_m2=inertia_total,
        components=subsystems,
    )

"""
Centralized engineering constants, physical dimensions, material properties,
and operational envelopes for DC-Revolution.

All physical dimensions are in SI units unless explicitly annotated.
Zero-hardcoding invariant: All algorithmic models, CAD generators, simulation
engines, and test assertions must reference these central definitions.
"""

from dataclasses import dataclass
from pathlib import Path

# ==============================================================================
# 1. Workspace & Path Anchors
# ==============================================================================
CONFIG_DIR: Path = Path(__file__).resolve().parent
PROJECT_ROOT: Path = CONFIG_DIR.parent
SPECS_DIR: Path = PROJECT_ROOT / "specs"
CAD_DIR: Path = PROJECT_ROOT / "cad"
SIM_DIR: Path = PROJECT_ROOT / "sim"
SRC_DIR: Path = PROJECT_ROOT / "src"
TESTS_DIR: Path = PROJECT_ROOT / "tests"

# ==============================================================================
# 2. System Nomenclature & Coordinate Conventions
# ==============================================================================
SYSTEM_NAME: str = "DC-Revolution"
SYSTEM_CODE: str = "DAED"
SYSTEM_VERSION: str = "0.1.0"

# Coordinate Frame: Right-Handed Cartesian
# X-Axis: Longitudinal / Forward (+X points along primary thrust/longitudinal axis)
# Y-Axis: Lateral / Starboard (+Y points to the right of primary forward axis)
# Z-Axis: Vertical / Up (+Z points vertically upwards opposite to standard gravity)
GRAVITY_ACCELERATION_M_S2: float = 9.80665

# ==============================================================================
# 3. Material Properties Database
# ==============================================================================
@dataclass(frozen=True)
class MaterialProperty:
    name: str
    density_kg_m3: float
    youngs_modulus_gpa: float
    poissons_ratio: float
    yield_strength_mpa: float
    ultimate_strength_mpa: float


MATERIAL_AL_7075_T6: MaterialProperty = MaterialProperty(
    name="Aluminum 7075-T6",
    density_kg_m3=2810.0,
    youngs_modulus_gpa=71.7,
    poissons_ratio=0.33,
    yield_strength_mpa=503.0,
    ultimate_strength_mpa=572.0,
)

MATERIAL_CFRP_T700: MaterialProperty = MaterialProperty(
    name="Carbon Fiber Epoxy Quasi-Isotropic (T700)",
    density_kg_m3=1550.0,
    youngs_modulus_gpa=70.0,
    poissons_ratio=0.30,
    yield_strength_mpa=600.0,
    ultimate_strength_mpa=900.0,
)

MATERIAL_TI_6AL_4V: MaterialProperty = MaterialProperty(
    name="Titanium Grade 5 (Ti-6Al-4V)",
    density_kg_m3=4430.0,
    youngs_modulus_gpa=113.8,
    poissons_ratio=0.342,
    yield_strength_mpa=880.0,
    ultimate_strength_mpa=950.0,
)

MATERIAL_STEEL_4130: MaterialProperty = MaterialProperty(
    name="Chromoly Structural Steel 4130",
    density_kg_m3=7850.0,
    youngs_modulus_gpa=205.0,
    poissons_ratio=0.29,
    yield_strength_mpa=435.0,
    ultimate_strength_mpa=670.0,
)

# ==============================================================================
# 4. Mechanical Envelopes & Nominal Dimensions (Baseline)
# ==============================================================================
# Overall outer geometric bounding box constraints [m]
ENVELOPE_LENGTH_MAX_M: float = 2.400
ENVELOPE_WIDTH_MAX_M: float = 1.600
ENVELOPE_HEIGHT_MAX_M: float = 0.850

# Primary structural chassis dimensions [m]
CHASSIS_LENGTH_M: float = 1.200
CHASSIS_WIDTH_M: float = 0.600
CHASSIS_HEIGHT_M: float = 0.350
CHASSIS_WALL_THICKNESS_M: float = 0.003  # 3 mm nominal wall

# Structural Factors of Safety (FoS) per aerospace standards
FACTOR_OF_SAFETY_YIELD: float = 1.25
FACTOR_OF_SAFETY_ULTIMATE: float = 1.50

# ==============================================================================
# 5. Mass & Center of Gravity (CG) Budgets
# ==============================================================================
MAX_GROSS_MASS_KG: float = 45.000
TARGET_EMPTY_MASS_KG: float = 28.500
MAX_PAYLOAD_MASS_KG: float = 12.000
MASS_CONTINGENCY_MARGIN_FRACTION: float = 0.15  # 15% reserve margin

# Allowable Center of Gravity Window relative to Datum Origin [m]
CG_X_MIN_M: float = 0.500
CG_X_MAX_M: float = 0.650
CG_Y_TOLERANCE_M: float = 0.025  # Symmetry constraint: |CG_Y| <= 25 mm
CG_Z_MIN_M: float = 0.120
CG_Z_MAX_M: float = 0.200

# ==============================================================================
# 6. Electrical, Power & Thermal Envelopes
# ==============================================================================
BUS_VOLTAGE_NOMINAL_V: float = 48.0
BUS_VOLTAGE_MIN_V: float = 42.0
BUS_VOLTAGE_MAX_V: float = 54.6
PEAK_POWER_DRAW_W: float = 3200.0
CRUISE_POWER_DRAW_W: float = 650.0

AMBIENT_TEMP_MIN_C: float = -20.0
AMBIENT_TEMP_MAX_C: float = 55.0
MAX_JUNCTION_TEMP_C: float = 85.0

# ==============================================================================
# 7. Simulation & Verification Parameters
# ==============================================================================
SIM_TIME_STEP_S: float = 0.001  # 1 kHz physics integration
SIM_DURATION_DEFAULT_S: float = 10.0
NUMERICAL_CONVERGENCE_REL_TOL: float = 1e-6
NUMERICAL_CONVERGENCE_ABS_TOL: float = 1e-9

# Geometric manufacturing tolerances [m]
TOLERANCE_MACHINING_FINE_M: float = 0.00005   # 50 micrometers
TOLERANCE_FABRICATION_GENERAL_M: float = 0.0005 # 0.5 millimeters

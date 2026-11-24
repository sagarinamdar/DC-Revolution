"""
Parametric CAD Model Generation and Bounding Box Verification for DC-Revolution.
Generates baseline parametric components based on centralized constants in config/constants.py.
"""

import json
from pathlib import Path
from typing import Dict, Any

from config.constants import (
    CHASSIS_LENGTH_M,
    CHASSIS_WIDTH_M,
    CHASSIS_HEIGHT_M,
    CHASSIS_WALL_THICKNESS_M,
    ENVELOPE_LENGTH_MAX_M,
    ENVELOPE_WIDTH_MAX_M,
    ENVELOPE_HEIGHT_MAX_M,
    CAD_DIR,
    MATERIAL_AL_7075_T6,
    MATERIAL_CFRP_T700,
)


def generate_baseline_cad_manifest() -> Dict[str, Any]:
    """Generates the baseline parametric CAD definition and verifies envelope compliance."""
    manifest = {
        "assembly_id": "DAED-ASM-TOP-001",
        "description": "DC-Revolution Top-Level System Assembly Baseline",
        "coordinate_system": "ISO 1151 Right-Handed (X-Aft, Y-Starboard, Z-Up)",
        "bounding_box_meters": {
            "x_length": CHASSIS_LENGTH_M,
            "y_width": CHASSIS_WIDTH_M,
            "z_height": CHASSIS_HEIGHT_M,
        },
        "envelope_compliance": {
            "x_fits": CHASSIS_LENGTH_M <= ENVELOPE_LENGTH_MAX_M,
            "y_fits": CHASSIS_WIDTH_M <= ENVELOPE_WIDTH_MAX_M,
            "z_fits": CHASSIS_HEIGHT_M <= ENVELOPE_HEIGHT_MAX_M,
        },
        "primary_subassemblies": [
            {
                "id": "DAED-ASM-STR-001",
                "name": "Primary Chassis Box",
                "material": MATERIAL_CFRP_T700.name,
                "nominal_dimensions_m": [CHASSIS_LENGTH_M, CHASSIS_WIDTH_M, CHASSIS_HEIGHT_M],
                "wall_thickness_m": CHASSIS_WALL_THICKNESS_M,
            },
            {
                "id": "DAED-ASM-ACT-001",
                "name": "Actuator Perimeter Brackets (4x)",
                "material": MATERIAL_AL_7075_T6.name,
                "pcd_bolt_circle_m": 0.065,
            },
        ],
    }

    # Export manifest to cad/exports
    export_path = CAD_DIR / "exports" / "baseline_cad_manifest.json"
    export_path.parent.mkdir(parents=True, exist_ok=True)
    with open(export_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    return manifest


if __name__ == "__main__":
    result = generate_baseline_cad_manifest()
    print(f"Generated baseline CAD manifest for {result['assembly_id']}")
    print(f"Envelope compliance: {result['envelope_compliance']}")

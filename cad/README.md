# DC-Revolution: CAD Architecture & Modeling Guidelines

**Reference Specifications:** [specs/system_requirements.md](file:///c:/SAGAR/MyProjectRepos/Industrial CPS Benchmark/DC-Revolution/specs/system_requirements.md)  
**Reference Constants:** [config/constants.py](file:///c:/SAGAR/MyProjectRepos/Industrial CPS Benchmark/DC-Revolution/config/constants.py)

---

## 1. Directory Structure
- `assemblies/`: Top-level and sub-assembly models (e.g. `DAED-ASM-TOP-001`, `DAED-ASM-CHASSIS-001`).
- `parts/`: Individual component parts (e.g. bulkheads, brackets, mounting plates).
- `exports/`: Standard interchange files for production and analysis (`.step` AP242, `.stl` high-res meshes, `.obj`).
- `scripts/`: Parametric CAD generation and automated validation scripts.

---

## 2. Coordinate System & Datum
All parts and assemblies MUST be modeled in the master coordinate system:
- **Origin (0, 0, 0):** Forward structural bulkhead at centerline, lower mounting baseline.
- **+X:** Longitudinal aft axis.
- **+Y:** Starboard (right) lateral axis.
- **+Z:** Upward vertical axis (normal to mounting plane).

Never build assemblies with ungrounded floating parts or arbitrary coordinate offsets. Every sub-assembly datum must explicitly locate to the top-level origin via defined transformation matrices in [src/geometry/transforms.py](file:///c:/SAGAR/MyProjectRepos/Industrial CPS Benchmark/DC-Revolution/src/geometry/transforms.py).

---

## 3. Part Numbering Standard
- Assemblies: `DAED-ASM-<SUBSYSTEM>-<INDEX>` (e.g., `DAED-ASM-STR-001`)
- Parts: `DAED-PRT-<SUBSYSTEM>-<INDEX>` (e.g., `DAED-PRT-STR-010`)
- Subsystem Codes:
  - `STR`: Structure
  - `ACT`: Actuation
  - `PWR`: Power & Battery
  - `AVI`: Avionics & Sensors
  - `PLD`: Payload

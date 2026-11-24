# DC-Revolution

Autonomous Cyber-Physical Platform Engineering: Specifications, Parametric CAD Synthesis, and Multi-Physics Simulation.

---

## 1. Executive Summary
**DC-Revolution** establishes an end-to-end aerospace/robotics engineering platform designed with rigorous mechanical specifications, zero-hardcoding architectural discipline, parametric CAD models, and high-fidelity physics simulations.

---

## 2. Directory Layout & Architecture

```mermaid
flowchart TD
    %% Root Node
    Root["📁 DC-Revolution/"]

    %% Primary Top-Level Children
    Root --> D_Config["📁 config/"]
    Root --> D_Specs["📁 specs/"]
    Root --> D_CAD["📁 cad/"]
    Root --> D_Sim["📁 sim/"]
    Root --> D_Src["📁 src/"]
    Root --> D_Tests["📁 tests/"]
    Root --> F_Pyproject["⚙️ pyproject.toml"]
    Root --> F_Readme["📘 README.md"]

    %% config Subtree (Vertical Stack)
    subgraph SG_Config [" "]
        direction TB
        D_Config --> CFG_Init["🐍 __init__.py"]
        CFG_Init --> CFG_Const["🐍 constants.py<br/><i>(Physical constants, materials, FoS, tolerances)</i>"]
    end

    %% specs Subtree (Vertical Stack)
    subgraph SG_Specs [" "]
        direction TB
        D_Specs --> SPC_SRS["📄 system_requirements.md<br/><i>(SRS: Geometric, mass, thermal requirements)</i>"]
        SPC_SRS --> SPC_ICD["📄 interface_control.md<br/><i>(ICD: Mechanical, electrical, thermal schemas)</i>"]
        SPC_ICD --> SPC_Budget["📊 engineering_budget.md<br/><i>(Mass roll-up, CG travel, power budget)</i>"]
        SPC_Budget --> SPC_RVTM["📋 verification_matrix.md<br/><i>(RVTM: Verification traceability matrix)</i>"]
    end

    %% cad Subtree (Vertical Stack)
    subgraph SG_CAD [" "]
        direction TB
        D_CAD --> CAD_Readme["📘 README.md<br/><i>(Coordinate datum, modeling rules)</i>"]
        CAD_Readme --> CAD_Assemblies["📁 assemblies/<br/><i>(Top-level & subsystem assembly models)</i>"]
        CAD_Assemblies --> CAD_Parts["📁 parts/<br/><i>(Discrete component models)</i>"]
        CAD_Parts --> CAD_Exports["📦 exports/<br/><i>(Standard formats .step AP242, .stl, .obj)</i>"]
        CAD_Exports --> CAD_Scripts["🐍 scripts/<br/><i>(Parametric CAD generators & validation)</i>"]
    end

    %% sim Subtree (Vertical Stack)
    subgraph SG_Sim [" "]
        direction TB
        D_Sim --> SIM_Readme["📘 README.md<br/><i>(Physics engine setup, RK4, solvers)</i>"]
        SIM_Readme --> SIM_Envs["📁 environments/<br/><i>(Simulation worlds, boundary conditions)</i>"]
        SIM_Envs --> SIM_Models["🤖 models/<br/><i>(Kinematic URDF & MuJoCo MJCF models)</i>"]
        SIM_Models --> SIM_Analysis["📈 analysis/<br/><i>(Baseline solvers, stability & telemetry)</i>"]
    end

    %% src Subtree (Vertical Stack)
    subgraph SG_Src [" "]
        direction TB
        D_Src --> SRC_Geom["📐 geometry/<br/><i>(3D spatial transforms, rotations & projections)</i>"]
        SRC_Geom --> SRC_Phys["⚛️ physics/<br/><i>(Mass properties roll-up, CG & inertia)</i>"]
    end

    %% tests Subtree (Vertical Stack)
    subgraph SG_Tests [" "]
        direction TB
        D_Tests --> TST_Const["🧪 test_constants.py<br/><i>(Material sanity, FoS & physical invariants)</i>"]
        TST_Const --> TST_Spec["🧪 test_spec_compliance.py<br/><i>(Automated requirement compliance audits)</i>"]
    end

    %% Modern Theme Styling
    classDef dirStyle fill:#1e293b,stroke:#3b82f6,stroke-width:2px,color:#f8fafc,text-align:left;
    classDef pyStyle fill:#172554,stroke:#60a5fa,stroke-width:1.5px,color:#93c5fd,text-align:left;
    classDef docStyle fill:#1e1b4b,stroke:#818cf8,stroke-width:1.5px,color:#c7d2fe,text-align:left;
    classDef testStyle fill:#064e3b,stroke:#34d399,stroke-width:1.5px,color:#a7f3d0,text-align:left;
    classDef rootStyle fill:#1d4ed8,stroke:#93c5fd,stroke-width:2.5px,color:#ffffff,font-weight:bold,text-align:left;

    class Root rootStyle;
    class D_Config,D_Specs,D_CAD,D_Sim,D_Src,D_Tests,CAD_Assemblies,CAD_Parts,CAD_Exports,CAD_Scripts,SIM_Envs,SIM_Models,SIM_Analysis,SRC_Geom,SRC_Phys dirStyle;
    class CFG_Init,CFG_Const,CAD_Scripts,SRC_Geom,SRC_Phys,SIM_Analysis pyStyle;
    class F_Pyproject,F_Readme,CAD_Readme,SIM_Readme,SPC_SRS,SPC_ICD,SPC_Budget,SPC_RVTM docStyle;
    class TST_Const,TST_Spec testStyle;
```

---

## 3. Engineering Specifications & Key Invariants
All design parameters and test assertions are anchored in [config/constants.py](file:///c:/SAGAR/MyProjectRepos/Industrial CPS Benchmark/DC-Revolution/config/constants.py):
- **Datum Coordinate Frame:** ISO 1151 Right-Handed Cartesian (+X Aft/Longitudinal, +Y Starboard/Right, +Z Upward).
- **Max Gross Mass:** 45.000 kg (with a minimum 15% unallocated mass contingency on dry structure).
- **Allowable CG Envelope:** $0.500\text{ m} \le X_{CG} \le 0.650\text{ m}$, $|Y_{CG}| \le 0.025\text{ m}$, $0.120\text{ m} \le Z_{CG} \le 0.200\text{ m}$.
- **Structural Safety Factors:** $\text{FoS}_{yield} \ge 1.25$, $\text{FoS}_{ult} \ge 1.50$.
- **Simulation Time Step:** $\Delta t = 0.001\text{ s}$ (1 kHz) with energy drift $< 0.01\%$/min.

---

## 4. Quick Start & Verification

### 4.1 Running the Automated Compliance Suite
Run the full test suite locally using `pytest`:
```bash
pytest tests/ -v
```

### 4.2 Generating Parametric CAD Manifest
```bash
python cad/scripts/generate_parametric_model.py
```

### 4.3 Running Dynamic Baseline Simulation
```bash
python sim/analysis/run_baseline_sim.py
```

---

## 5. Specification Documents
- [System Requirements Specification (SRS)](file:///c:/SAGAR/MyProjectRepos/Industrial CPS Benchmark/DC-Revolution/specs/system_requirements.md)
- [Interface Control Document (ICD)](file:///c:/SAGAR/MyProjectRepos/Industrial CPS Benchmark/DC-Revolution/specs/interface_control.md)
- [Engineering Mass & Power Budget](file:///c:/SAGAR/MyProjectRepos/Industrial CPS Benchmark/DC-Revolution/specs/engineering_budget.md)
- [Requirements Verification Traceability Matrix (RVTM)](file:///c:/SAGAR/MyProjectRepos/Industrial CPS Benchmark/DC-Revolution/specs/verification_matrix.md)

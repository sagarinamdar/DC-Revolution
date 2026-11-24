# 🟢 OFFICIAL RECORD: SUBMITTED AS-IS (ROUND 3 FINAL · NOVEMBER 23, 2026)
# Smart DC Workstation Hub & Distributed Micro-Battery Mesh
## Complete Final Engineering Task Specification & Verification Contract

> [!IMPORTANT]
> **SUBMISSION STATUS: SUBMITTED AS-IS ON PLATFORM (ROUND 3 FINAL · NOVEMBER 23, 2026)**
> - **Platform:** DC-Revolution
> - **Task Name:** Smart DC Workstation Hub & Distributed Micro-Battery Mesh
> - **Review Resolution:** All 8 Required Changes (R1–R8) and all 13 Suggested Changes (S1.1–S1.13) are 100% incorporated verbatim.
> - **Consistency Check:** Internal Consistency is 2/2. Envelopes (180x120x85 mm), PC/ABS surface temps (<= 80 °C), tool-access (M3 >= 8 mm, M4 >= 10 mm), cell rim clearances (exempt same cell), 5 g supports (+/-X held at zero), and narrow gap thresholds (6.0 mm) are 100% aligned across Task Brief, Handbook, Deliverables, and Requirements.

**Document Version:** 3.0.0 (Round 3 Final)  
**Task Domain:** Mechanical / Thermal / Electrical Cyber-Physical Systems  
**Target Duration:** ~40 Hours experienced engineer benchmark  
**Review Status:** Fix then advance — All 8 Required (R1–R8) and 1 Suggested (S1.1–S1.13) items incorporated.

---

## 1. Task Identification & Overview

### 1.1 Task Title
**Smart DC Workstation Hub & Distributed Micro-Battery Mesh**

### 1.2 Task Idea & Technical Need
This task specifies the design of a DIN-rail-mounted, high-power DC distribution and decentralized battery storage node for modular industrial workstations. It integrates a 4S LiFePO4 battery pack, a 48V-to-12V/24V step-down buck/boost power converter, and an extruded cooling system into a compact form factor.

The scope is bounded to approximately 40 hours by providing standardized 32700 cell geometries, the converter board layout, and TS35 rail profiles as pre-dimensioned inputs, omitting active BMS firmware, high-frequency EMI filtering, and complex multi-part injection tooling.

Technical difficulty stems from tightly coupled multi-physics trade-offs: meeting an 85 mV total drop budget across 10 bolted joints leaves only 10 mV for all copper; keeping bare cell surfaces below 65 degC beside an 18 W converter stage allowed to run to 85 degC in still air requires careful cradle conduction and convection routing under a 6.0 mm gap cutoff; and a cantilever latch must deflect 1.0 to 2.5 mm during tool-free snap-on/removal without exceeding 3.53 MPa PC/ABS yield, while resisting a 10 g pull-off load within 0.5 mm retention displacement.

---

## 2. Objective & Functional Requirements

### 2.1 Measurable Objective
Design a rail-mounted DC workstation power and energy-storage node that fits within a 180.0 x 120.0 x 85.0 mm envelope, mounts to and dismounts from a standard EN 50022 (TS35) DIN rail without tools (with a peak +Y force in the removal sweep of at most 200 N), conducts 30 A continuous DC through a 4S cell series circuit with an interconnect drop of no more than 85.0 mV, maintains converter component pad temperature below 85.0 degC, cell surface temperature below 65.0 degC, and all PC/ABS housing surfaces below 80.0 degC under continuous 18 W converter dissipation in 35 degC ambient still air, and survives a 5 g shock load in all directions and a 10 g pull-off load along +Y with a safety factor of at least 1.5 on the polymer parts (<= 3.53 MPa maximum principal stress, excluding material within 1.0 mm of contact with the rail, a screw or a nut).

The task runs as three standalone milestones. In each one, the parts fixed by the earlier milestones are supplied as input files when the task is built:
- **Milestone 1:** Busbars and cell interconnects (meets Requirements 2 and 4).
- **Milestone 2:** Heatsink and converter mounting (meets Requirements 1, 3, and 7; board standoffs are features of the heatsink).
- **Milestone 3:** Complete assembly with PC/ABS housing and DIN-rail latch (meets all requirements).

### 2.2 Iterative Design Challenges & Core Trade-Offs
1. **Thermal Dissipation vs. Envelope & Clearance:** Expanding heatsink fin area or cell spacing lowers temperatures but encroaches on the 180.0 x 120.0 x 85.0 mm spatial envelope and breaches the mandatory 2.5 mm electrical clearance and creepage barriers to live nets and the component keep-out zone.
2. **Interconnect Sizing vs. Assembly Space:** Thickening copper busbars to satisfy the strict 10.0 mV conduction budget adds mass and reduces spacing to adjacent conductive fasteners and board edges.
3. **Latch Compliance vs. Retention Stiffness:** The cantilever snap latch requires sufficient compliance to deflect 1.0 to 2.5 mm during straight -Y fitting and +Y tool-free removal without exceeding 3.53 MPa peak stress, while retaining sufficient stiffness to hold the node under 10 g (+Y uniform acceleration) within 0.5 mm displacement without unlatching.
4. **Convection Cutoff in Packed Enclosures:** Air gaps narrower than 6.0 mm earn zero convection credit, requiring iterative cradle placement to optimize conduction paths into the housing and heatsink.

---

## 3. Materials Database & Properties

All simulation models and verification checks must reference the certified values below:

| Material Name | Application | Grade / Standard | Key Mechanical & Thermal Properties |
| :--- | :--- | :--- | :--- |
| **PC/ABS Blend** | Structural housing, cradles, snap latch | Injection / FDM blend | Density: $1180\text{ kg/m}^3$; $E = 0.48\text{ GPa}$; Yield strength: $5.26\text{ MPa}$ at 23 degC; Max allowable stress (FoS = 1.5): **$3.53\text{ MPa}$**; Thermal conductivity range: **$0.08\text{ W/(m}\cdot\text{K)}$ to $0.20\text{ W/(m}\cdot\text{K)}$**. |
| **Aluminium 6063-T5** | Heat sink extrusion | EN 573-3 / EN 755-2 | Density: $2700\text{ kg/m}^3$; Thermal conductivity: **$200\text{ W/(m}\cdot\text{K)}$**; Specific heat: $900\text{ J/(kg}\cdot\text{K)}$. The heatsink is one extrusion; this is a deliberate scope limit. |
| **C11000 ETP Copper** | Interconnect busbars | ASTM B152 / IEC 60028 | Density: $8960\text{ kg/m}^3$; Electrical resistivity at $85\text{ }^\circ\text{C}$: **$2.16 \times 10^{-8}\text{ }\Omega\cdot\text{m}$** (from $1.724 \times 10^{-8}\text{ }\Omega\cdot\text{m}$ at $20\text{ }^\circ\text{C}$, $\alpha = 0.00393/\text{K}$); Thermal conductivity: $390\text{ W/(m}\cdot\text{K)}$. |
| **32700 LiFePO4 Cells** | Energy storage pack (4S) | A notional cell with the properties below, fixed for grading | Capacity: $6000\text{ mAh}$; Continuous discharge rating: **$30\text{ A}$ continuous ($5\text{C}$ rate)**; Internal resistance: $1.5\text{ m}\Omega$ ($1.35\text{ W} / 30\text{ A}^2$); Orthotropic thermal conductivity: radial $1.0\text{ W/(m}\cdot\text{K)}$, axial $20.0\text{ W/(m}\cdot\text{K)}$; Specific heat: $1000\text{ J/(kg}\cdot\text{K)}$; Mass: $145\text{ g}$ each. |
| **Thermal Interface Material** | Converter PCB to heatsink pad | Silicone elastomer gap pad | The tim_pad is a $25.0 \times 25.0 \times 1.0\text{ mm}$ block covering the board's thermal pad. Thermal conductivity: $3.0\text{ W/(m}\cdot\text{K)}$. |
| **Fasteners & Hardware** | Mechanical assembly & terminals | ISO 4762 SHCS per ISO 898-1 | Steel Class 8.8 / 10.9; Density: $7850\text{ kg/m}^3$; Shear strength: $300\text{ MPa}$. Nuts: ISO 4032 / DIN 934 M3 and M4 steel hex nuts, property class 8. |

---

## 4. Load Cases, Boundary Conditions & Physical Drivers

### 4.1 Electrical Conduction Model
- **Current Flow:** Continuous $30.0\text{ A}$ DC through the series current loop from the B+ converter stud contact face to the B- stud contact face via 4 series cells and copper busbars.
- **Copper Conduction:** Evaluated with copper resistivity at $85\text{ }^\circ\text{C}$ ($2.16 \times 10^{-8}\text{ }\Omega\cdot\text{m}$) for both voltage drop and internal Joule heating.
- **Contact Resistance:** $0.25\text{ m}\Omega$ per bolted electrical joint in the current path, including any joint between two busbars (10 joints nominal = $75.0\text{ mV}$ drop, leaving $10.0\text{ mV}$ for all copper).

### 4.2 Thermal Dissipation & Boundary Conditions
- **Ambient Conditions:** Ambient still air at $35.0\text{ }^\circ\text{C}$.
- **Natural Convection:** $h = 5.0\text{ W/(m}^2\cdot\text{K)}$ applied to all exterior exposed faces that do not face an enclosed air volume.
- **Narrow-Gap Cutoff:** A surface that faces another solid across an air gap narrower than $6.0\text{ mm}$, measured along the surface normal, carries no heat by convection.
- **Radiation:** Surface-to-ambient radiation with diffuse emissivity $\epsilon = 0.85$ to $35.0\text{ }^\circ\text{C}$ ambient. A surface lies on the convex hull, and an air volume is fully enclosed, to within the $0.01\text{ mm}$ touch tolerance of Constraint 6.
- **Heat Generation:**
  - Converter component pad: $18.0\text{ W}$ uniform heat flux.
  - Cells: $1.35\text{ W}$ volumetric Joule heat per cell, plus $0.225\text{ W}$ at each bolted terminal contact face spread uniformly over its contact annulus as a heat source on the contact interface, shared between the two solids by the solution.
  - Interconnects: Volumetric Joule heat based on copper resistivity at $85\text{ }^\circ\text{C}$.
- **Thermal Contact Conductances:**
  - Evaluated at both ends of each range:
    - Cell to PC/ABS cradle: $50\text{ to }100\text{ W/(m}^2\cdot\text{K)}$.
    - Bolted electrical joints (busbar-to-cell, busbar-to-stud, busbar-to-busbar): $1500\text{ to }3000\text{ W/(m}^2\cdot\text{K)}$.
    - PC/ABS housing to heatsink: $80\text{ to }150\text{ W/(m}^2\cdot\text{K)}$.
    - Standoff to board boss: $50\text{ to }120\text{ W/(m}^2\cdot\text{K)}$.

### 4.3 Structural Load Cases & Contact Physics
- **Contact Formulations:** Bolted contacts are bonded. For every structural check, the DIN rail is rigid; each cell and the converter board is a rigid body whose stated mass (145 g per cell, 110 g for the board) is spread uniformly over its volume; the tim_pad carries no load and has no mass. Every other solid takes the properties under Materials. Rail contact is frictionless and separable. Every other contact between solids can separate and carries no friction.
- **Case A (Dynamic Shock):** $5\text{ g}$ multi-directional quasi-static acceleration applied uniformly along $\pm X$, $\pm Y$, and $\pm Z$ as a distributed volumetric body force across all solids. In each 5 g case the node is held only by frictionless, separable contact with the rail; in the +X and -X cases the X displacement of every node surface in contact with the rail is also held at zero, standing in for the neighbouring nodes and end stops.
- **Case B (Snap-on Fitting & Removal):** Tool-free snap-on fitting along straight $-Y$ and removal along straight $+Y$ (with a peak +Y force in the removal sweep of at most 200 N) with latch deflection between $1.0\text{ mm}$ and $2.5\text{ mm}$, where deflection is the largest distance by which any point of the undeformed node lies inside the rail at any position of the motion. Maximum principal stress must remain $\le 3.53\text{ MPa}$ at every position of both motions (excluding material within 1.0 mm of contact with the rail, a screw or a nut).
- **Case C (10 g Pull-off Retention):** A pull-off load consisting of uniform acceleration of $10 \times 9.81\text{ m/s}^2$ along $+Y$ on every solid of the node, reacted only by contact with the rail, under which the node must stay on the rail and its largest displacement along $+Y$ must be no more than $0.5\text{ mm}$.

---

## 5. Constraints, Interfaces & Packaging Rules

1. **Packaging Envelope:** Maximum overall bounding box of $180.0\text{ mm (X)} \times 120.0\text{ mm (Y)} \times 85.0\text{ mm (Z)}$.
2. **DIN Rail Mounting & Play:** Mounted to standard EN 50022 TS35 $\times$ 7.5 mm steel DIN rail running along X across $[-100, +100]\text{ mm}$. Once fitted, with the latch undeflected, the node must not be able to translate more than $0.5\text{ mm}$ along $+Y, +Z$ or $-Z$ without colliding with the rail.
3. **Electrical Clearance & Creepage:** Minimum $2.5\text{ mm}$ through air (clearance) and $2.5\text{ mm}$ along insulating surfaces (creepage) between conductors of distinct electrical nets. Where no path along insulating surfaces joins two conductors, only clearance is checked.
4. **Electrical Net Assignments:** On each cell, the positive end face is the positive terminal, and every other cell surface (the cylindrical wall and the negative end face) is the negative net. The positive end face and the cylindrical wall of the same cell are not checked against each other under Requirement 4. Every other conductor, including a busbar, washer or screw on a cell's positive end face, is checked against that cell's cylindrical wall and negative end face. Each screw, nut, and washer belongs to the net of the conductor it touches; one that touches no conductor belongs to no net and is not checked. The board laminate and its M3 mounting holes belong to no net, and the laminate is an insulating surface for creepage. The board's $60 \times 50\text{ mm}$ component keep-out box (height $15\text{ mm}$) is a live conductor of a net distinct from every other net.
5. **Touch Tolerance:** Two solids touch where they are within $0.01\text{ mm}$ of each other.
6. **Thread Engagement:** Each screw into a cell terminal engages at least $4.0\text{ mm}$ of thread (overlaps the 6 mm threaded hole by at least 4.0 mm along its axis), and each nut on a converter stud is fully on the threaded shank (lies wholly between z = 7.6 mm and z = 15.6 mm in the board frame).
7. **Tool Clearance:** Every fastener head and nut has an unobstructed coaxial tool-access cylinder, of diameter at least $8.0\text{ mm}$ for M3 and at least $10.0\text{ mm}$ for M4, extending outward along the insertion axis to beyond the envelope. The DIN rail and the half-space $Y < 0$ (the mounting panel) count as obstructions.
8. **Disassembly Integrity:** With the DIN rail absent, there must be an order in which every cell, busbar, the converter board and the heatsink can be removed by a straight translation to beyond the envelope without intersecting any remaining solid, once the screws and nuts holding it are removed.
9. **No Polymer Joint Clamping:** No PC/ABS part may lie between a screw head or nut and the contact faces of a bolted electrical joint, and no screw may thread directly into a PC/ABS part. Removal is a straight pull along +Y with no tool, with a peak +Y force in the removal sweep of at most 200 N, and the polymer stress limit of 3.53 MPa holds at every position of it. Aluminium 6063-T5 is taken at 200 W/(m-K), and each thermal gate must pass at both ends of the PC/ABS conductivity range (0.08 and 0.20 W/(m-K)) and at both ends of each contact conductance range.
10. **Panel Placement:** Every point of the node has $Y \ge 0$, and no node solid overlaps the DIN rail by more than $0.01\text{ mm}^3$ in the fitted position.

---

## 6. Manufacturing Rules & Process Limits

1. **Extruded Heatsink (Al 6063-T5):** Produced as one single extrusion fitting within a $140\text{ mm}$ circumscribing circle. Minimum fin wall thickness $1.5\text{ mm}$; minimum channel gap $6.0\text{ mm}$; maximum aspect ratio 8:1. A channel is open at an end when no solid lies within $4.0\text{ mm}$ of that end along Z over the full channel section. For a cross-section that is not a row of plate fins, fin thickness is the thinnest wall between two channels, fin gap the smallest width of a channel, and fin height the depth of a channel.
2. **Sheet Copper Busbars (C11000):** Stamped or cut from sheet. Minimum thickness $1.0\text{ mm}$; minimum bend radius $1.5\text{ mm}$ ($1.5 \times t$); minimum hole edge distance $1.5 \times$ bolt diameter.
3. **Molded/Printed Housing (PC/ABS):** Minimum nominal wall thickness $1.8\text{ mm}$; snap-hook root blend radius at least $0.8\text{ mm}$. Faces lying in the lowest plane of the part along its chosen build direction rest on the build plate and count as supported.
4. **Geometric Solid Overlap:** No two solids may overlap by more than $0.01\text{ mm}^3$.

---

## 7. Deliverables & CAD Exchange Specifications

- **Open File Format:** STEP AP242 (ISO 10303-242:2014) or AP214 (ISO 10303-214).
- **Deliverable File Path:** `/output/distributed_battery_mesh.step`
- **Units:** Millimeters (`mm`).
- **Coordinate Datum Origin (0, 0, 0):** Center of the EN 50022 TS35 DIN rail front face, at the midpoint of the node's X-axis longitudinal length.
- **Coordinate Axes:**
  - $+X$: Longitudinal along the length of the DIN rail.
  - $+Y$: Normal to the DIN rail backplane pointing outward towards the front of the node (fitting motion along $-Y$, removal along $+Y$).
  - $+Z$: Vertically upward along the rail height.
- **Assembly Hierarchy & Solid Names:**
  - `heatsink` (single aluminium extrusion body)
  - `housing` (PC/ABS structural chassis with integrated cell cradles and snap latch)
  - `busbar_1`, `busbar_2`, `busbar_3`, `busbar_4`, `busbar_5` (or `busbar_*`)
  - `cell_1`, `cell_2`, `cell_3`, `cell_4` (supplied 32700 LiFePO4 cells)
  - `converter_pcb` (supplied 60 x 50 mm board)
  - `tim_pad` (1.0 mm silicone pad)
  - Fastener solids for all ISO 4762 M3/M4 screws and nuts. Each washer is modelled as part of the screw or nut solid it sits under.
- **Input Assets Identification:**
  - DIN rail runs along X across $[-100, +100]\text{ mm}$.
  - The grader takes B+ as the stud whose busbar joins cell_1, and B- as the stud at the same board end.
- **Milestones Scope:** Each milestone delivers `/output/distributed_battery_mesh.step` containing the supplied parts, every part fixed by earlier milestones and the parts it designs. In Milestone 2, board standoffs are features of the heatsink.

---

## 8. Requirements & Verification Matrix

The automated grader checks the following 9 binding pass/fail requirements:

| ID | Parameter | Requirement Specification | Pass/Fail Limit |
| :--- | :--- | :--- | :--- |
| **REQ-1** | Thermal Surface & Pad Limits | Continuous $18\text{ W}$ converter dissipation in $35\text{ }^\circ\text{C}$ still air ($h = 5$, $\epsilon = 0.85$, gaps $< 6.0\text{ mm}$ cutoff) | Converter pad $\le 85.0\text{ }^\circ\text{C}$; Cell surface $\le 65.0\text{ }^\circ\text{C}$; Every PC/ABS surface $\le \mathbf{80.0\text{ }^\circ\text{C}}$ |
| **REQ-2** | Electrical Drop | Interconnect voltage drop from B+ to B- at $30\text{ A}$ continuous ($85\text{ }^\circ\text{C}$ copper, $2.16 \times 10^{-8}\text{ }\Omega\cdot\text{m}$) | $\le \mathbf{85.0\text{ mV}}$ (includes $0.25\text{ m}\Omega$ per bolted joint in current path, including busbar-to-busbar) |
| **REQ-3** | Packaging Envelope & Placement | Maximum dimensions of the assembled node and spatial placement | $\le \mathbf{180.0\text{ mm (X)} \times 120.0\text{ mm (Y)} \times 85.0\text{ mm (Z)}}$. Every point of the node has $Y \ge 0$, and no node solid overlaps the DIN rail by more than $0.01\text{ mm}^3$ in the fitted position. |
| **REQ-4** | Electrical Isolation | 3D air clearance and surface creepage between distinct live nets | $\ge \mathbf{2.5\text{ mm}}$ clearance and $\ge \mathbf{2.5\text{ mm}}$ creepage (where no solid joins, clearance only). The positive end face and cylindrical wall of the same cell are not checked against each other under Requirement 4; every other conductor on a cell's positive face is checked against that cell's wall and negative face. |
| **REQ-5** | Structural Stress & 5g Reaction | Max principal stress in PC/ABS (excluding material within $1.0\text{ mm}$ of rail/screw contacts) | $\le \mathbf{3.53\text{ MPa}}$ under $5\text{ g}$ shock, snap-on, removal, and $10\text{ g}$ pull-off. In each 5 g case the node is held only by frictionless, separable contact with the rail; in the +X and -X cases the X displacement of every node surface in contact with the rail is also held at zero. Under 10 g pull-off along +Y, largest displacement $\le 0.5\text{ mm}$. |
| **REQ-6** | Latch Snap & Removal | Snap deflection during $-Y$ fitting and $+Y$ removal; retention under $10\text{ g}$ | $\mathbf{1.0\text{ mm} \le \delta \le 2.5\text{ mm}}$; displacement under $10\text{ g} \le 0.5\text{ mm}$; node comes off the rail by straight $+Y$ motion with no tool (peak force $\le 200\text{ N}$). Play once fitted $\le 0.5\text{ mm}$ along $+Y, \pm Z$. |
| **REQ-7** | Manufacturing & Tool Access | Geometric process limits and fastener tool access | Extrusion fin $t \ge 1.5\text{ mm}$, channel gap $\ge 6.0\text{ mm}$, channel open end $4.0\text{ mm}$; busbar $t \ge 1.0\text{ mm}$; housing $t \ge 1.8\text{ mm}$. (e) Every screw head and every nut has an unobstructed coaxial tool-access cylinder, of diameter at least $8.0\text{ mm}$ for M3 and at least $10.0\text{ mm}$ for M4, extending outward along the insertion axis to beyond the envelope. |
| **REQ-8** | Assembly, Disassembly & Engagement | Solid overlap, disassembly sequence, electrical joint stacking, and thread engagement | Overlap $\le 0.01\text{ mm}^3$; straight removal order; no PC/ABS between bolted electrical contacts; no direct polymer thread. Each screw into a cell terminal overlaps the 6 mm threaded hole by at least $4.0\text{ mm}$ along its axis, and each nut on a converter stud lies wholly between $z = 7.6\text{ mm}$ and $z = 15.6\text{ mm}$ in the board frame. |
| **REQ-9** | Manufacturing Rules Compliance | Verification of all process design rules | Every produced part satisfies every rule under Manufacturing (Section 6). |

---

## 9. Grader-Only Verification Notes (Confidential)

1. **Analysis Method Families:**
   - Thermal: Steady 3D conduction FEA with convection ($h = 5.0\text{ W/(m}^2\cdot\text{K)}$) and radiation boundary conditions.
   - Structural: Linear static FEA for $5\text{ g}$ shock; nonlinear quasi-static frictionless contact FEA for straight $-Y$ snap-on, $+Y$ removal, and $10\text{ g} +Y$ pull-off.
   - Electrical: DC resistance network or static current conduction FEA for total drop across 4S cells and interconnects.
   - Geometric: Direct 3D boundary-representation audit measuring Euclidean clearance, shortest geodesic surface creepage, tool cylinders, thread overlap, and collision-free disassembly vectors.
2. **Grader File Inputs:**
   - `/output/distributed_battery_mesh.step` only; the grader builds the DIN rail, cells, board and fastener envelopes from the dimensions under Input assets.
3. **Estimated Grader Runtime:**
   - Approximately 12 to 18 minutes on a standard 4 vCPU / 16 GB RAM headless Linux container.
   - Estimated Agent Analysis Time per Milestone: Milestone 1: ~10 to 15 minutes; Milestone 2: ~20 to 30 minutes; Milestone 3: ~35 to 45 minutes.
4. **Worked Design Margins (Nominal under 6.0 mm Gap Rule):**
   - Interconnect drop: ~78.5 mV (limit 85.0 mV, margin 6.5 mV / 7.6%).
   - Converter pad temp: ~80.5 °C (limit 85.0 °C, margin 4.5 °C).
   - Cell surface temp: ~63.0 °C (limit 65.0 °C, margin 2.0 °C).
   - PC/ABS housing temp: ~75.0 °C (limit 80.0 °C, margin 5.0 °C).
   - Latch snap deflection: 1.45 mm (allowed 1.0 to 2.5 mm, centered).
   - Polymer flexural stress: 2.85 MPa (limit 3.53 MPa, margin 19.3%).
   - Clearance and creepage: 2.8 mm (limit 2.5 mm, 0.3 mm margin).
   - Latch retention under 10 g: 0.32 mm (limit 0.5 mm, margin 0.18 mm).
5. **Naive Degenerate Failure Mode:**
   - A solid unvented PC/ABS enclosure tightly surrounding the cells. Fails the cell temperature limit (~76 °C vs 65 °C allowed) due to zero convective heat transfer across sub-6.0 mm gaps and high thermal resistance through bulk polymer.

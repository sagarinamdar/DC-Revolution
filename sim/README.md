# DC-Revolution: Simulation Architecture & Analysis Guidelines

**Reference Specifications:** [specs/system_requirements.md](file:///c:/SAGAR/MyProjectRepos/Industrial CPS Benchmark/DC-Revolution/specs/system_requirements.md)  
**Reference Constants:** [config/constants.py](file:///c:/SAGAR/MyProjectRepos/Industrial CPS Benchmark/DC-Revolution/config/constants.py)

---

## 1. Directory Structure
- `environments/`: Simulation scene descriptions, world settings, friction parameters, terrain profiles.
- `models/`: Multi-body physics models (URDF, MuJoCo MJCF XML, FEA mesh input decks).
- `analysis/`: Post-processing scripts, numerical solvers, telemetry visualization, stability analysis.

---

## 2. Solver Standards & Numerical Requirements
- **Integration Step Size:** Fixed time step $\Delta t = 0.001\text{ s}$ (1 kHz).
- **Integrator:** 4th-order Runge-Kutta (RK4) or implicit symplectic Euler for mechanical stability.
- **Energy Conservation Gate:** Total mechanical energy drift must remain $< 0.01\%$ per simulation minute under unforced conservative motion.
- **State Vector Representation:**
  $$\mathbf{x} = [x, y, z, q_w, q_x, q_y, q_z, v_x, v_y, v_z, \omega_x, \omega_y, \omega_z]^T$$

---

## 3. Simulation Workflow
1. Load centralized parameters from `config/constants.py`.
2. Compute mass properties and inertia tensor using `src/physics/mass_properties.py`.
3. Execute baseline dynamics runner `sim/analysis/run_baseline_sim.py`.
4. Validate compliance with operational envelopes in `tests/test_spec_compliance.py`.

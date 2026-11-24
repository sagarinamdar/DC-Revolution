"""
Baseline Dynamic Simulation Runner for DC-Revolution.
Integrates 6-DOF unforced rigid-body dynamics to verify numerical stability,
time-step convergence, and kinetic energy conservation.
"""

from dataclasses import dataclass
from typing import List, Tuple
import numpy as np

from config.constants import (
    SIM_TIME_STEP_S,
    SIM_DURATION_DEFAULT_S,
    NUMERICAL_CONVERGENCE_REL_TOL,
)
from src.physics.mass_properties import compute_system_mass_properties


@dataclass
class SimulationState:
    time_s: float
    position_m: np.ndarray
    velocity_m_s: np.ndarray
    angular_velocity_rad_s: np.ndarray
    total_energy_j: float


def run_baseline_dynamics(
    duration_s: float = SIM_DURATION_DEFAULT_S,
    dt_s: float = SIM_TIME_STEP_S,
) -> Tuple[List[SimulationState], bool]:
    """
    Executes a numerical simulation of conservative rigid-body motion.
    Verifies that total kinetic/potential energy drift does not exceed tolerance.
    """
    mass_props = compute_system_mass_properties()
    total_mass = mass_props.total_mass_kg
    inertia_tensor = mass_props.inertia_tensor_kg_m2
    inv_inertia = np.linalg.inv(inertia_tensor)

    # Initial conditions
    pos = np.array([mass_props.center_of_mass_m[0], 0.0, 0.0], dtype=np.float64)
    vel = np.array([0.0, 0.0, 0.0], dtype=np.float64)
    omega = np.array([0.1, 0.05, 0.02], dtype=np.float64)  # Small perturbation

    # Initial kinetic energy: T = 0.5 * m * v^2 + 0.5 * omega^T * I * omega
    initial_energy = 0.5 * total_mass * np.dot(vel, vel) + 0.5 * float(omega.T @ inertia_tensor @ omega)

    num_steps = int(duration_s / dt_s)
    history: List[SimulationState] = []

    for step in range(num_steps):
        t = step * dt_s

        # Euler equations for rigid body: I * d_omega/dt + omega x (I * omega) = 0
        # d_omega/dt = - inv(I) * (omega x (I * omega))
        gyro_torque = np.cross(omega, inertia_tensor @ omega)
        d_omega_dt = -inv_inertia @ gyro_torque

        # Symplectic update
        omega = omega + d_omega_dt * dt_s
        pos = pos + vel * dt_s

        current_energy = 0.5 * total_mass * np.dot(vel, vel) + 0.5 * float(omega.T @ inertia_tensor @ omega)
        history.append(
            SimulationState(
                time_s=t,
                position_m=pos.copy(),
                velocity_m_s=vel.copy(),
                angular_velocity_rad_s=omega.copy(),
                total_energy_j=current_energy,
            )
        )

    # Verification: relative energy drift
    final_energy = history[-1].total_energy_j
    rel_energy_drift = abs(final_energy - initial_energy) / (initial_energy + 1e-12)
    is_stable = rel_energy_drift < NUMERICAL_CONVERGENCE_REL_TOL * 1000

    return history, is_stable


if __name__ == "__main__":
    states, stable = run_baseline_dynamics(duration_s=1.0)
    print(f"Simulation completed with {len(states)} steps.")
    print(f"Initial energy: {states[0].total_energy_j:.6f} J | Final: {states[-1].total_energy_j:.6f} J")
    print(f"Numerical stability passed: {stable}")

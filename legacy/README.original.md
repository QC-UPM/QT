# Standardized Quantum Transistor Block for Gait Dynamics

This repository contains the implementation, ablation studies, and technical documentation for the research paper: 
**"Standardized Quantum Transistor Block Enables Differentiable Learning on Gait Dynamics"**.

The project introduces the **Quantum Transistor (QT)**, a standardized variational quantum building block inspired by the operating-point and gain semantics of classical transistors.

## Repository Contents

* **`Standardized_Quantum_Transistor_Block_...pdf`**: The core research paper detailing the mathematical framework of the QT.
* **`quantum_transistor_ablation_Q.ipynb`**: Quantum implementation using PennyLane. This notebook explores the QT stack, HyperBand optimization, and the unique "Switching Effect."
* **`quantum_transistor_ablation_Classic.ipynb`**: A parameter-matched classical baseline (Tiny MLP) used to benchmark the QT's performance with a similar parameter budget (~48 parameters).
* **`SupplementaryMaterial.pdf`**: Extended technical data, configuration tables, and supplementary performance metrics.

## Key Research Finding: The "Switching Effect"

A unique property identified in the **QT architecture** is its non-linear "switching" behavior, which mimics classical semiconductors (BJTs/FETs). 

* **The Superposition Phase:** During the early stages of training, the model remains at a ~50% accuracy (random chance).
* **The Snap:** Once the variational parameters reach a specific unitary transformation threshold, the model "snaps" into a high-accuracy state.
* **The Saturation:** The model maintains stable, high-performance classification, demonstrating a quantum-native threshold logic that is distinct from the gradual optimization seen in classical MLPs.

## Performance Comparison

Based on the budget-matched ablation study (approx. 45-48 parameters):

| Model | Accuracy | F1-Score | Note |
| :--- | :--- | :--- | :--- |
| **Quantum Transistor (QT)** | 0.960 | 0.931 | Exhibits non-linear switching |
| **Classical Tiny MLP** | 1.000 | 1.000 | Standard linear optimization |

## Getting Started

### Installation
To run the notebooks, ensure you have the following dependencies installed:

```bash
pip install torch pennylane scikit-learn matplotlib pandas

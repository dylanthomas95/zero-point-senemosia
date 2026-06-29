"""Hilbert Space Module for Organizational States"""

import numpy as np
from typing import Tuple


class HilbertSpace:
    """N-dimensional Hilbert space for organizational quantum states."""
    
    def __init__(self, n_qubits: int):
        self.n_qubits = n_qubits
        self.dimension = 2 ** n_qubits
        
    def tensor_product_basis(self) -> np.ndarray:
        """Generate complete tensor product basis."""
        basis = []
        for i in range(self.dimension):
            state = np.zeros(self.dimension)
            state[i] = 1.0
            basis.append(state)
        return np.array(basis)
    
    def create_superposition(self, probabilities: np.ndarray) -> np.ndarray:
        """Create superposition state."""
        if len(probabilities) != self.dimension:
            raise ValueError(f"Expected {self.dimension} probabilities")
        
        state = np.zeros(self.dimension)
        for i, p in enumerate(probabilities):
            state[i] = np.sqrt(p)
        return state / np.linalg.norm(state)

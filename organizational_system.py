"""Organizational System Module"""

import numpy as np
from typing import List, Dict, Any


class Agent:
    """Organizational agent representing a department or individual."""
    
    def __init__(self, agent_id: int, energy: float = 1.0):
        self.id = agent_id
        self.energy = energy
        self.state = np.array([1.0, 0.0])  # |0⟩ and |1⟩ basis
        
    def get_potential(self) -> float:
        return self.energy


class OrganizationalSystem:
    """Complex organizational system as quantum system."""
    
    def __init__(self, n_agents: int, connection_density: float = 0.3):
        self.n_agents = n_agents
        self.agents = [Agent(i) for i in range(n_agents)]
        self.adjacency = self._generate_network(connection_density)
        
    def _generate_network(self, density: float) -> np.ndarray:
        """Generate organizational network."""
        adj = np.random.rand(self.n_agents, self.n_agents) < density
        adj = adj.astype(float)
        adj = (adj + adj.T) / 2  # Make symmetric
        np.fill_diagonal(adj, 0)
        return adj
    
    def get_adjacency_matrix(self) -> np.ndarray:
        return self.adjacency.copy()
    
    def get_state_vector(self) -> np.ndarray:
        states = np.array([agent.state for agent in self.agents])
        return np.concatenate(states)


class HilbertSpace:
    """N-dimensional Hilbert space for organizational states."""
    
    def __init__(self, n_qubits: int):
        self.n_qubits = n_qubits
        self.dimension = 2 ** n_qubits
        
    def tensor_product_basis(self) -> np.ndarray:
        """Generate tensor product basis states."""
        basis = []
        for i in range(self.dimension):
            binary = format(i, f'0{self.n_qubits}b')
            state = np.zeros(self.dimension)
            state[i] = 1.0
            basis.append(state)
        return np.array(basis)

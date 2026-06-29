"""Basic Energy Extraction Example"""

import sys
sys.path.insert(0, '..')

from src.framework import Framework
from src.organizational_system import OrganizationalSystem

# Create organizational system
print("Creating organizational system with 50 agents...")
org = OrganizationalSystem(n_agents=50, connection_density=0.3)

# Initialize framework
print("Initializing ZPS Framework...")
zps = Framework()

# Extract zero point energy
print("Extracting zero point energy...")
result = zps.extract_zero_point_energy(org)

# Print results
print("\n" + "="*50)
print("ZERO POINT ENERGY EXTRACTION RESULTS")
print("="*50)
print(f"ZPE Index:              {result['zpe_index']:.2f} / 100")
print(f"Coherence Field Ratio:  {result['coherence_field_ratio']:.4f}")
print(f"Entanglement Fraction:  {result['entanglement_fraction']:.4f}")
print(f"Method:                 {result['method']}")
print("="*50)

# Detect topological defects
print("\nDetecting topological defects...")
defects = zps.detect_topological_defects(org)
print(f"Defect Nodes:           {len(defects['defect_nodes'])}")
print(f"Tension Index:          {defects['tension_index']:.4f}")

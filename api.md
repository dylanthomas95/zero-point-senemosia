# API Reference - ZPS Framework

## Framework Class

### `Framework(regularization_type='ramanujan')`

Main class per l'estrazione di energia.

#### Metodi

##### `extract_zero_point_energy(system, method='graph_rnn')`

Estrae l'energia di punto zero dal sistema.

**Parametri:**
- `system` (OrganizationalSystem): Sistema organizzativo
- `method` (str): 'graph_rnn', 'direct', 'variational'

**Ritorna:**
- `dict`: Contiene zpe_index, coherence_field_ratio, entanglement_fraction

**Esempio:**
```python
zps = Framework()
org = OrganizationalSystem(n_agents=50)
result = zps.extract_zero_point_energy(org)
print(f"ZPE Index: {result['zpe_index']}")
```

##### `detect_topological_defects(system)`

Rileva i difetti topologici (stringhe cosmiche).

**Parametri:**
- `system` (OrganizationalSystem): Sistema organizzativo

**Ritorna:**
- `dict`: Contiene defect_nodes, defect_count, tension_index

## OrganizationalSystem Class

### `OrganizationalSystem(n_agents, connection_density=0.3)`

Modella un sistema organizzativo complesso.

**Parametri:**
- `n_agents` (int): Numero di agenti/dipartimenti
- `connection_density` (float): Densità di connessioni (0-1)

#### Metodi

##### `get_adjacency_matrix()`

Ritorna la matrice di adiacenza.

##### `get_state_vector()`

Ritorna il vettore di stato del sistema.

## HilbertSpace Class

### `HilbertSpace(n_qubits)`

Spazio di Hilbert per stati organizzativi.

#### Metodi

##### `tensor_product_basis()`

Genera la base di prodotto tensoriale.

##### `create_superposition(probabilities)`

Crea uno stato di sovrapposizione.

## EnergyExtractor Class

### `EnergyExtractor()`

Estrae e analizza metriche energetiche.

#### Metodi

##### `extract(system)`

Estrae metriche energetiche.

**Ritorna:**
- `dict`: total_energy, spectral_radius, average_degree, density

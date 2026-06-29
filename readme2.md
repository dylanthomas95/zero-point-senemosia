# ZPS-RNN Module

Graph RNN specializzato per estrazione di energia in sistemi complessi.

## 🎯 Features

- **Graph LSTM**: LSTM modificate per nodi in grafi
- **Cosine Embedding Loss**: Minimizzazione distanza coseno
- **Dimensionality Reduction**: PCA-based filtering
- **Privacy**: zk-SNARKs per computazioni

## 📦 Installazione

```bash
git clone https://github.com/zps-framework/zps-rnn-module.git
cd zps-rnn-module
pip install -r requirements.txt
```

## 🚀 Utilizzo

```python
from zps_rnn import GraphRNN, CosineEmbeddingLoss
import torch

model = GraphRNN(input_dim=4, hidden_dim=32)
loss_fn = CosineEmbeddingLoss()
optimizer = torch.optim.Adam(model.parameters())
```

## 📚 Documentazione

Vedi `/docs` per la documentazione completa.

## 📄 Citazione

```bibtex
@article{sichetti2026zps,
  title={Zero Point Senemosì̀a},
  author={Sichetti, L. and Naressi, F.L.},
  year={2026},
  doi={10.5281/zenodo.21015386}
}
```

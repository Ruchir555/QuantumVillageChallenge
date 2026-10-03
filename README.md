# Quantum Village QKD Challenge

This repository contains a notebook solution to a quantum key distribution
challenge. Alice and Bob publicly compare their measurement bases, keep the
positions where their bases match, and use Alice's corresponding measurement
bits as the shared key material. The key bits are packed into bytes and XORed
with the supplied ciphertext.

[Open the notebook in Google Colab](https://colab.research.google.com/github/Ruchir555/QuantumVillageChallenge/blob/main/QuantumVillageChallenge.ipynb)

## Method

1. Compare Alice's and Bob's basis strings position by position.
2. Retain Alice's bits only where the bases match.
3. Pack each group of eight key bits into a byte, most significant bit first.
4. XOR the key bytes with the Base64-decoded ciphertext.
5. Decode the resulting plaintext as UTF-8.

The supplied data contains 368 measurements. Basis reconciliation retains 189
bits, which provides enough key material for the 19-byte ciphertext.

## Run

The solution uses only the Python standard library. Open the notebook in Colab,
or run it locally with Jupyter:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install jupyterlab
jupyter lab QuantumVillageChallenge.ipynb
```

## Tests and continuous integration

The pure functions in `qkd_solution.py` implement basis reconciliation, bit
packing and XOR decryption without notebook state. Run their tests with:

```bash
python -m unittest discover -s tests -v
```

GitHub Actions runs these tests on Python 3.11 and 3.13 for every push and
pull request. The regression suite includes the known challenge plaintext.

## Attribution and licensing status

The basis strings, measurement bits and ciphertext were supplied as challenge
material. The notebook history does not identify the original challenge page
or a licence for that material, and a search using the distinctive ciphertext
did not locate an authoritative source. A repository-wide open-source licence
has therefore not been added. The solution code is by Ruchir Tullu; the
challenge data remains attributable to its original authors.

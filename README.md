# 🔐 project-2025

A graphical desktop application built with PyGTK (GTK 3) for multi-layered message encryption and decryption. The project implements a modified Vigenere cipher architecture featuring dynamic secret key generation, cryptographic salting (noise-buffering), and local `.env` session synchronization.

The environment and runtimes are fully managed and automated using **uv**.

---

## ✨ Features

* **Multi-Layered Cipher:** Protects payloads through three distinct passes of encryption/decryption utilizing separate public and dynamically generated secret keys.
* **Cryptographic Salting:** Appends a random 97-character noise-buffer to message payloads before full-pass encryption to mitigate frequency analysis vulnerabilities.
* **Local Key Manager:** Automatically provisions a cryptographically secure 20-character session key locally stored as an encrypted variable via `python-dotenv`.
* **Reusable UI Interface:** Features a modular `CryptoInterface` (GTK 3) component inside `ui.py` that dynamically accepts button labels and handles hot-swapped cryptographic action triggers.
* **Bilingual Support:** Fully operational across both Latin (ASCII), digits, punctuation marks, and Cyrillic alphabet structures.

---

## 📁 Repository Structure

* `core.py` — Core cryptographic matrix handling Vigenere rounds, layering, and salting arrays.
* `storage.py` — Local key manager synchronizing runtime bytes with a filesystem `.env` database.
* `ui.py` — Abstracted PyGTK window container rendering fields and linking callback triggers.
* `encryptor.py` — Application entryway initializing the encryption pipeline and dynamic key staging.
* `decryptor.py` — Symmetrical desktop interface performing state reversing, character trimming, and payload recovery.
* `pyproject.toml` — Configuration file defining project metadata and managed dependencies for `uv`.
* `.env` — Local persistent database managing encrypted session keys (generated automatically).

---

## 🚀 Quick Start

To launch the application, execute these commands in your terminal:

```bash
# 1. Clone the repository and navigate into the application root
git clone https://github.com/lifer-x/simple-crypto
cd simple-crypto

# 2. Run the encryption workspace
uv run python encryptor.py

# 3. Or run the decryption workspace
uv run python decryptor.py
```

---

## 🎮 How It Works

* **Encryption (`encryptor.py`):** Enter raw string data and click **Encrypt**. The system automatically seeds an encrypted `_secret_key` hook inside `.env` (if no active session data exists), appends a 97-character salt tail, and returns the final cipher-text block directly into the entry field.
* **Decryption (`decryptor.py`):** Paste the cipher-text array block and click **Decrypt**. The underlying logic fetches token records via `storage`, strips the 97-character salt tail, and returns the original message into the entry field.

---
_Engineered for lightweight, secure, and clean desktop cryptography execution._

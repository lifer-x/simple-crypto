# 🔐 PyGTK Cryptor Suite

A secure, desktop-based graphical application for multi-layered message encryption and decryption. Built with **Python 3**, **PyGTK (GTK 3)**, and **python-dotenv**, this suite leverages an enhanced, multi-pass Vigenere cipher architecture with dynamic key generation, cryptographic salting, and local `.env` session synchronization.

## ✨ Features
* **Multi-Layered Cipher**: Protects payloads through 3 distinct passes of encryption/decryption utilizing separate public and dynamically generated secret keys.
* **Cryptographic Salting**: Appends a random 97-character noise-buffer to message payloads before full-pass encryption to mitigate frequency analysis vulnerabilities.
* **Dynamic Key Management**: Automatically provisions cryptographically secure 24-character session keys locally stored as encrypted variables using `python-dotenv`.
* **Native Cross-Platform GUI**: Built with PyGTK (GTK 3) widgets featuring responsive window scaling and input/output handlers.
* **Bilingual Support**: Fully operational across both Latin (26-character) and Cyrillic (32-character) alphabetic structures.

## 📁 Repository Structure
* `encrypt.py` — Graphical entryway containing core UI elements and routines to handle message encryption and dynamic key staging.
* `decrypt.py` — Symmetrical desktop interface performing state reversing, character trimming, and payload recovery.
* `.env` — Local persistent database managing encrypted session keys.

## 🚀 Getting Started

### Prerequisites
Ensure your local environment runs **Python 3.8+** with native GTK 3 system libraries.

*On Ubuntu/Debian:*
```bash
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
```

### Installation
1. Clone the repository workspace:
   ```bash
   git clone https://github.com
   ```
2. Navigate into the application root:
   ```bash
   cd your-repo-name
   ```
3. Install required runtime packaging dependencies:
   ```bash
   pip install python-dotenv
   ```

## 🎮 How It Works

### Encryption
1. Launch the encryption pipeline:
   ```bash
   python3 encrypt.py
   ```
2. Enter your raw text string and hit **Encrypt**.
3. The engine generates a unique `secret_key`, encrypts it against the system `PUBLIC_KEY`, saves it to `.env`, salts your text with 97 characters, and encodes the complete block.

### Decryption
1. Launch the decryption pipeline:
   ```bash
   python3 decrypt.py
   ```
2. Paste the encrypted cipher-text block and click **Decrypt**.
3. The system maps matching key indicators, removes the 97-character noise block, and prints the recovered plaintext message into the input field.

---
🔐 *Engineered for lightweight, secure, and clean desktop cryptography execution.*

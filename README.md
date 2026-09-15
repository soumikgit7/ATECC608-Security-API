<div align="center">

# 🔐 ATECC608 Security API

### Modular Cryptographic REST API for IoT & Blockchain Applications

<p>
  <img src="https://img.shields.io/badge/Python-3.12+-blue?logo=python">
  <img src="https://img.shields.io/badge/FastAPI-REST%20API-009688?logo=fastapi">
  <img src="https://img.shields.io/badge/Cryptography-ECC-orange">
  <img src="https://img.shields.io/badge/Status-Under%20Development-yellow">
</p>

**A software-based security API inspired by the cryptographic capabilities of the ATECC608 secure element.**

</div>

---

## 📌 About

**ATECC608 Security API** is a modular REST API designed to provide cryptographic services for **IoT, blockchain, and security-focused applications**.

The current implementation uses software-based cryptography and is designed with a future architecture that can support **ATECC608 hardware integration**.

---

## 🏗️ Architecture

<div align="center">

```text
┌─────────────────────────────┐
│   IoT / Blockchain Apps     │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       REST API (FastAPI)    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      Security Services      │
│                             │
│  ECC │ SHA-256 │ RNG        │
│  ECDSA │ ECDH (Planned)     │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│   Software Crypto Backend   │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│   Future ATECC608 Backend   │
└─────────────────────────────┘
```

</div>

---

## ⚡ Features

<table>
<tr>
<th>Feature</th>
<th>Description</th>
<th>Status</th>
</tr>

<tr>
<td>🔑 ECC Key Generation</td>
<td>Generate ECC key pairs using SECP256R1</td>
<td>✅ Implemented</td>
</tr>

<tr>
<td>🔐 Public Key Retrieval</td>
<td>Retrieve public keys using a unique Key ID</td>
<td>✅ Implemented</td>
</tr>

<tr>
<td>🎲 Secure RNG</td>
<td>Generate cryptographically secure random bytes</td>
<td>✅ Implemented</td>
</tr>

<tr>
<td>#️⃣ SHA-256</td>
<td>Generate SHA-256 hashes for input data</td>
<td>✅ Implemented</td>
</tr>

<tr>
<td>✍️ ECDSA</td>
<td>Digital signature generation and verification</td>
<td>🔜 Planned</td>
</tr>

<tr>
<td>🤝 ECDH</td>
<td>Secure shared-secret derivation</td>
<td>🔜 Planned</td>
</tr>

<tr>
<td>🔌 ATECC608 Hardware</td>
<td>Hardware-backed cryptographic operations</td>
<td>🔜 Future</td>
</tr>

</table>

---

## 🌐 API Endpoints

| Method | Endpoint                      | Description                    |
| :----: | ----------------------------- | ------------------------------ |
| `POST` | `/api/v1/keys/generate`       | Generate ECC key pair          |
|  `GET` | `/api/v1/keys/{key_id}`       | Retrieve public key            |
| `POST` | `/api/v1/random/generate`     | Generate secure random bytes   |
| `POST` | `/api/v1/hash/sha256`         | Generate SHA-256 hash          |
| `POST` | `/api/v1/signatures/sign`     | ECDSA signing *(planned)*      |
| `POST` | `/api/v1/signatures/verify`   | ECDSA verification *(planned)* |
| `POST` | `/api/v1/key-exchange/derive` | ECDH key exchange *(planned)*  |

---

## 📁 Project Structure

```text
ATECC608-Security-API/
│
├── app/
│   ├── main.py
│   │
│   ├── api/
│   │   └── routes/
│   │       ├── keys.py
│   │       ├── random.py
│   │       └── hashing.py
│   │
│   ├── services/
│   │   ├── key_service.py
│   │   ├── random_service.py
│   │   └── hash_service.py
│   │
│   ├── schemas/
│   │   └── hash_schema.py
│   │
│   └── core/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

<div align="center">

| Technology          | Purpose                         |
| ------------------- | ------------------------------- |
| 🐍 **Python**       | Core development                |
| ⚡ **FastAPI**       | REST API framework              |
| 🚀 **Uvicorn**      | ASGI server                     |
| 🔒 **Cryptography** | Cryptographic operations        |
| 📋 **Pydantic**     | Data validation                 |
| 🐙 **GitHub**       | Version control & collaboration |

</div>

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ATECC608-Security-API.git
cd ATECC608-Security-API
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

<div align="center">

### Swagger UI

`http://127.0.0.1:8000/docs`

### ReDoc

`http://127.0.0.1:8000/redoc`

</div>

---

## 🔑 Example

### Generate ECC Key Pair

```http
POST /api/v1/keys/generate
```

Example response:

```json
{
  "key_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "algorithm": "ECC",
  "curve": "secp256r1",
  "public_key": "-----BEGIN PUBLIC KEY-----..."
}
```

> 🔒 The private key is kept internally and is not exposed through the API response.

---

## 🔄 Development Roadmap

```text
✅ FastAPI Project Setup
       ↓
✅ ECC Key Generation
       ↓
✅ Public Key Retrieval
       ↓
✅ Secure Random Number Generation
       ↓
✅ SHA-256 Hashing
       ↓
🔲 ECDSA Signing
       ↓
🔲 ECDSA Verification
       ↓
🔲 ECDH Key Exchange
       ↓
🔲 Security Engine
       ↓
🔲 Crypto Backend Interface
       ↓
🔲 ATECC608 Hardware Backend
       ↓
🔲 Testing & Security Hardening
```

---

## 🔒 Security

The project follows several security-oriented principles:

* Private keys are not returned through API responses.
* Cryptographic operations rely on established cryptographic libraries.
* API routes and cryptographic services are separated.
* Input validation is used for API requests.
* The architecture allows future hardware-backed cryptography.

### Current Limitation

The development version currently uses an **in-memory key store**.

Therefore, generated keys are lost when the server restarts.

Secure persistent key management will be addressed in a later development stage.

---

## 🎯 Project Goal

The long-term goal is to create a **single modular security API** through which IoT and blockchain applications can access essential cryptographic operations without implementing every operation independently.

```text
          IoT Application
                 │
                 ▼
       ┌───────────────────┐
       │ ATECC608 Security │
       │        API        │
       └─────────┬─────────┘
                 │
       ┌─────────┴─────────┐
       ▼                   ▼
 Software Crypto      ATECC608
    Backend            Hardware
```

---

## 📌 Project Status

<div align="center">

**🚧 Active Development**

Core API infrastructure and initial cryptographic services are implemented.

More security features are currently being developed.

</div>

---

## 👨‍💻 Author

<div align="center">

### Soumik Ghosh

**B.Tech — Computer Science & Engineering**

Interested in **Cybersecurity • Cryptography • IoT • Blockchain • Software Engineering**

</div>

---


---

<div align="center">

### ⭐ If you find this project interesting, consider giving it a star!

</div>

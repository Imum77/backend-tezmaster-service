# 🌐 backend-tezmaster-service

Backend service for managing home internet connection requests for **Teznet** internet provider.

---

## 📋 About

"""
When a customer visits the office and requests a home internet installation (router setup), 
an admin creates a request in the system. Field technicians can view requests, update statuses, 
attach photos and add comments. The backend integrates with external Teznet services via HTTP and uses OracleDB + MySQL for data storage.
"""

---

## ✨ Features

- 📝 Create and manage internet connection requests
- 📸 Attach photos and documents to requests
- 💬 Add comments to requests
- 🔄 Track and update request statuses
- 👤 Reassign requests to other users
- 📱 OTP-based authentication (SMS)
- 🔐 JWT access token authorization
- 🔌 Device management (add/remove routers)
- 🔍 Subscriber search

---

## 🔄 Request Statuses

| Status | Description |
|--------|-------------|
| 🔀 **Перенаправить** | Request redirected to another specialist |
| 🔧 **Ведётся работа** | Work is in progress |
| ✅ **Решено** | Request resolved |
| ⏸️ **Отложено** | Request postponed |

---

## 🛠️ Tech Stack

- **Framework:** FastAPI
- **Database:** MySQL + OracleDB
- **Auth:** OTP (SMS) + JWT
- **HTTP Client:** aiohttp
- **Language:** Python 3.11
- **Mobile Client:** Android

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- MySQL
- OracleDB
- Docker (optional)

### Installation

```bash
# Clone the repository
git clone https://github.com/Imum77/backend-tezmaster-service.git
cd backend-tezmaster-service

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=mysql+aiomysql://user:password@localhost:3306/tezmaster
ORACLE_DSN=your_oracle_dsn
SECRET_KEY=your_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Run

```bash
uvicorn app.main:app --reload
```

API: `http://localhost:8000`  
Swagger docs: `http://localhost:8000/docs`

---

## 🐳 Docker

```bash
docker compose up -d
```

---

## 📡 API Endpoints

### 🔐 Auth

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/otp` | Send OTP code to phone number |
| POST | `/auth/verify` | Verify OTP and get JWT token |
| GET | `/auth/history` | Get auth history by phone |
| GET | `/auth/logout` | Logout and deactivate session |

### 📋 Teznet Requests

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/teznet/get-user/` | Get user info by token |
| GET | `/teznet/teznet-requests/` | Get list of requests (pagination) |
| GET | `/teznet/teznet-status/` | Get request history/status |
| POST | `/teznet/req-detail/` | Get request details by case ID |
| POST | `/teznet/change-req-status/` | Update request status |
| POST | `/teznet/change-req-user/` | Reassign request to another user |

### 💬 Comments & Documents

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/teznet/add-comment/` | Add comment with optional photo |
| POST | `/teznet/add-document/` | Upload document to request |

### 🔌 Device Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/teznet/add-device/` | Add new device (router) |
| POST | `/teznet/del-device/` | Remove device |
| POST | `/teznet/find-subs/` | Search subscriber |

---

## 📱 Mobile Client

This backend powers an **Android** mobile application where field technicians can:
- View and manage assigned requests
- Update request status on the go
- Attach photos directly from their phone
- Add comments to requests
- Search subscribers and manage devices

---

## 👤 Author

**Imomnazar** — [github.com/Imum77](https://github.com/Imum77)

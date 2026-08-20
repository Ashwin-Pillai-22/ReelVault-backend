# ReelVault Backend

This is the backend script that fetches the metadata of the instagram reel.

## 🛠️ Tech Stack

- **Language:** Python
- **Backend:** FastAPI

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ashwin-Pillai-22/ReelVault-backend
cd ReelVault-backend
```

### 2. Install requirements

```bash
pip3 install -r requirements.txt
```

### 3. Start server

#### (i). Running the server locally
```bash
uvicorn FetchData:app --reload
```

#### (ii). Host the server
```bash
uvicorn FetchData:app --host 0.0.0.0 --port $PORT
```

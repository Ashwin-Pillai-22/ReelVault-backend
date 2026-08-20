# ReelVault Backend

Backend service for ReelVault that fetches and extracts metadata from Instagram Reel URLs.

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Server:** Uvicorn

## 🌟 Features
- Fetch Instagram Reel metadata
- Extract Reel information from a URL
- REST API built with FastAPI
- Supports local development and cloud deployment

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ashwin-Pillai-22/ReelVault-backend
cd ReelVault-backend
```

### 2. Install dependencies

```bash
pip3 install -r requirements.txt
```
Note: Use pip instead of pip3 if not installed.

### 3. Start the server

#### (i). Run locally
```bash
uvicorn FetchData:app --reload
```
The API will be available at: 
http://127.0.0.1.8000

FastAPI's interactive API documentation: 
http://127.0.0.1.8000/docs

#### (ii). Run for deployment
```bash
uvicorn FetchData:app --host 0.0.0.0 --port $PORT
```
## 📡 API

### Fetch Reel Metadata

Send an Instagram Reel URL to the API to retrieve its metadata.

Example request:

```bash
POST /scrape-reel
```

```bash
Request body:
{
  "url": "http://www.instagram.com/reel/example/"
}
```

The API returns the available metadata for the Reel.
```bash
{
  "username": username,
  "caption": caption,
  "tags": tags,
  "thumbnail_url": thumbnail_url,
  "reel_url": reel_url
}
```

## 📁 Project Structure
```bash
ReelVault-backend/
|- FetchData.py
|- requirements.txt
|- README.md
```

## 🔗 Related Project
This backend is part of ReelVault, a local Instagram Reel storage application.

## 👨‍💻 Author
Ashwin Pillai

GitHub: [Ashwin-Pillai-22](https://github.com/Ashwin-Pillai-22)

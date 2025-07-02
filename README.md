# 🎵 FastAPI Song API

A backend application built using **FastAPI** and **SQLAlchemy** that allows users to manage songs, simulate purchases with gateway logic, and create/shuffle playlists.

> 📌 Submitted as part of the OpsWerks Academy backend technical assessment.

---

## 🚀 Features

### Song API
- Create, retrieve, update, and delete songs
- Each song includes:
  - `title` (string)
  - `length` (int in seconds)
  - `date_released` (datetime)
  - `price` (positive decimal)

### 💳 Purchase Endpoint
- Accepts a list of song IDs
- Determines the payment gateway based on total price:
  - **CheapPaymentGateway** if total < 10
  - **ExpensivePaymentGateway** if total ≥ 10
- Returns a success message after simulated payment

### 🎶 Playlist API _(Bonus)_
- Create a playlist containing multiple songs
- Shuffle the order of songs within the playlist

---

## 🧰 Tech Stack

- Python 3.11+
- FastAPI
- SQLAlchemy
- Pydantic v2
- SQLite (dev environment)
- Pytest (testing framework)

---

## 📁 Project Structure
├── app/ <br>
├── main.py<br>
├── app/ <br>
│ ├── main.py<br>
│ ├── models.py<br>
│ ├── schemas.py<br>
│ ├── database.py<br>
│ └── routers/<br>
│ ├── songs.py<br>
│ ├── purchase.py<br>
│ └── playlist.py<br>
├── tests/<br>
│ ├── test_songs.py<br>
│ ├── test_purchase.py<br>
│ └── test_playlist.py<br>
├── requirements.txt<br>
└── README.md<br>

## 🛠 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Sweep76/fastapi-song-api.git
cd fastapi-song-api
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the development server
```bash 
uvicorn app.main:app --reload
```

### 5. Open the Swagger UI
Visit: http://127.0.0.1:8000/docs

## Running Tests
Make sure you're in the root folder and run:
```bash
pytest
```

## Sample JSON Payloads

### Create Song
```json
POST /songs
{
  "title": "Sample Song",
  "length": 240,
  "date_released": "2024-01-01T00:00:00",
  "price": 5.99
}
```
### Purchase Songs
```json
POST /purchase
{
  "song_ids": [1, 2, 3]
}
```
### Create Playlist
```json
POST /playlists
{
  "name": "My Favorite Tracks",
  "song_ids": [1, 2, 3]
}
```

### Shuffle Playlist
```bash
POST /playlists/{playlist_id}/shuffle
```






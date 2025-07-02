# 🎵 FastAPI Song API

A backend service built with **FastAPI** and **SQLAlchemy** that allows users to manage songs, simulate purchases, and organize playlists.

> 📌 Submitted as part of the OpsWerks internship backend assessment.

---

## 🚀 Features

### ✅ Song API
- Create, read, update, and delete songs
- Each song has a title, length, price, and release date

### 💳 Purchase Endpoint
- Accepts a list of song IDs
- Automatically routes payment to:
  - `CheapPaymentGateway` if total < 10
  - `ExpensivePaymentGateway` if total ≥ 10

### 🎶 Playlist API _(Bonus)_
- Create a playlist with selected songs
- Shuffle the song order

---

## 🛠 Tech Stack

- **Python 3.11+**
- **FastAPI**
- **SQLAlchemy**
- **Pydantic v2**
- **SQLite (dev)** / PostgreSQL/MySQL (production ready)
- **Pytest** for testing

---

## 🧪 Run Tests

```bash
pytest

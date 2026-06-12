# 🚀 Learning Python API with FastAPI

A beginner-friendly FastAPI project demonstrating the fundamentals of building REST APIs using Python. This repository explores FastAPI concepts such as route creation, request handling, path and query parameters, request body validation using Pydantic, and implementing basic CRUD operations with an in-memory data store.

> **Note:** This project is intended for learning purposes and uses an in-memory list instead of a persistent database.

---

## 📌 Features

* Build REST APIs using FastAPI
* Define GET, POST, and DELETE endpoints
* Create and validate request bodies using Pydantic models
* Work with path parameters and query parameters
* Implement a simple Todo CRUD API
* Understand FastAPI route ordering behavior
* Load environment variables using python-dotenv
* Explore asynchronous endpoint definitions

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Framework:** FastAPI
* **Validation:** Pydantic
* **Environment Variables:** python-dotenv
* **ASGI Server:** Uvicorn

---

## 📂 Project Structure

```text
Learning-Python-API/
├── .gitignore
├── api.py
├── crudAPI.py
└── main.py
```

### File Overview

| File         | Purpose                                                                                            |
| ------------ | -------------------------------------------------------------------------------------------------- |
| `main.py`    | Demonstrates FastAPI basics, routing, path parameters, query parameters, and request body handling |
| `api.py`     | Implements a simple Todo API with in-memory CRUD operations                                        |
| `crudAPI.py` | Extends the Todo API and demonstrates loading environment variables using dotenv                   |
| `.gitignore` | Excludes sensitive and unnecessary files from version control                                      |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Learning-Python-API.git
cd Learning-Python-API
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn pydantic python-dotenv
```

---

## ▶️ Running the Applications

### Run `main.py`

```bash
uvicorn main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

---

### Run `api.py`

```bash
uvicorn api:app --reload
```

---

### Run `crudAPI.py`

```bash
uvicorn crudAPI:app --reload
```

---

## 📖 API Endpoints

### Main Application (`main.py`)

#### Ping Endpoint

```http
GET /ping
```

Response:

```json
{
    "message": "Hello World..."
}
```

---

#### Root Endpoint

```http
GET /
```

Response:

```json
{
    "Welcome.."
}
```

---

#### Blog Comments

```http
GET /blogs/comments
```

Response:

```json
{
    "comments": "No Comments yet!"
}
```

---

#### Blog Details

```http
GET /blogs/{blog_id}
```

Example:

```http
GET /blogs/1?q=python
```

Request Body:

```json
{
    "name": "John",
    "age": 25
}
```

Response:

```json
{
    "blog_id": 1
}
```

---

## 📝 Todo API Endpoints

### Get All Todos

```http
GET /todos
```

---

### Get Todo by ID

```http
GET /todos/{todo_id}
```

Example:

```http
GET /todos/1
```

---

### Create Todo

```http
POST /todos
```

Request Body:

```json
{
    "id": 1,
    "title": "Learn FastAPI",
    "description": "Study CRUD operations",
    "completed": false
}
```

Response:

```json
{
    "id": 1,
    "title": "Learn FastAPI",
    "description": "Study CRUD operations",
    "completed": false
}
```

---

### Delete Todo

```http
DELETE /todos/{todo_id}
```

Example:

```http
DELETE /todos/1
```

Response:

```json
{
    "message": "Todo deleted"
}
```

---

## 🔐 Environment Variables

The `crudAPI.py` file demonstrates how to load environment variables using `python-dotenv`.

Create a `.env` file:

```env
FOO2=example_value
```

Access variables in Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("FOO2"))
```

---

## 📚 Learning Outcomes

By completing this project, you will understand:

* FastAPI application setup
* Defining API routes
* Request validation using Pydantic
* Handling path and query parameters
* Creating simple CRUD APIs
* Using in-memory storage
* Loading environment variables
* Running FastAPI applications with Uvicorn

---

## 🚧 Future Improvements

* Add PUT/PATCH endpoints
* Implement proper HTTP status codes
* Use `HTTPException` for error handling
* Integrate SQLite or PostgreSQL
* Introduce SQLAlchemy ORM
* Add JWT Authentication
* Write unit tests using Pytest
* Containerize the application using Docker
* Add CI/CD using GitHub Actions

---

## ⚠️ Disclaimer

This repository is just a learning project wriiten to explore FastAPI fundamentals from youtube.

---

## 👨‍💻 Author

**Bikramjit Roy** – DevOps & Cloud Engineering Enthusiast passionate about automation, CI/CD, cloud-native practices, and building reliable software delivery pipelines.

GitHub: https://github.com/Bikramjit2212

⭐ If you found this project useful, consider giving it a star.

# 🎓 CampusSphere AI — Student Database Application System

An AI-powered Student Database Application System built with **FastAPI, SQLite, Gemini API, LangGraph and ChromaDB**.

## 🚀 Live Demo

* **Dashboard:** https://campussphere-ai-aqxw.onrender.com/
* **Swagger API:** https://campussphere-ai-aqxw.onrender.com/docs
* **ReDoc:** https://campussphere-ai-aqxw.onrender.com/redoc
* **Health Check:** https://campussphere-ai-aqxw.onrender.com/health

## ✨ Features

* Student, Course and Enrollment CRUD
* FastAPI REST APIs
* Interactive Swagger documentation
* Responsive web dashboard
* Gemini-powered AI chatbot
* LangGraph chatbot workflow
* ChromaDB vector search
* SQLite database
* API health monitoring
* Render deployment
* Docker support

## 🛠️ Tech Stack

**Backend:** Python, FastAPI, SQLAlchemy
**Database:** SQLite
**AI:** Gemini API, LangGraph
**Vector Database:** ChromaDB
**Frontend:** HTML, CSS, JavaScript
**Deployment:** Render
**Documentation:** Swagger / OpenAPI, ReDoc

## 📁 Project Structure

```text
CampusSphere-AI/
├── app/
│   ├── routers/
│   ├── services/
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── main.py
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── scripts/
│   └── seed_data.py
├── data/
├── .env.example
├── Dockerfile
├── render.yaml
├── requirements.txt
└── README.md
```

## ⚙️ Run Locally

### 1. Clone

```bash
git clone https://github.com/Mehak486/CampusSphere-AI.git
cd CampusSphere-AI
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Create `.env`:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.6-flash
```

### 5. Seed Database

```bash
python scripts/seed_data.py
```

### 6. Start Server

```bash
python -m uvicorn app.main:app --reload --port 8000
```

Open:

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/docs
```

## 🔗 Main API Endpoints

```text
GET    /api/students
POST   /api/students
GET    /api/students/{id}
PUT    /api/students/{id}
DELETE /api/students/{id}

GET    /api/courses
POST   /api/courses
PUT    /api/courses/{id}
DELETE /api/courses/{id}

GET    /api/enrollments
POST   /api/enrollments
PUT    /api/enrollments/{id}
DELETE /api/enrollments/{id}

POST   /api/chat
GET    /health
```

## 🤖 AI Chatbot

The integrated AI chatbot uses:

* **Gemini API** for natural-language responses
* **LangGraph** for chatbot workflow
* **ChromaDB** for student information retrieval

Example queries:

```text
How many students are in Computer Science?
Show students with CGPA above 8.
Which courses are available?
Show student enrollment information.
```

## 🌐 Deployment

The application is deployed on **Render** and provides:

* Live Dashboard
* REST APIs
* Swagger documentation
* AI chatbot
* Health monitoring

## 👩‍💻 Developer

**Mehak Sharma**

B.Tech Computer Science Engineering Graduate

* GitHub: https://github.com/Mehak486
* LinkedIn: https://linkedin.com/in/mehak-112704300

## 📄 Project

**Final Year Internship Project — Student Database Application System**

Built using modern backend, AI and database technologies.

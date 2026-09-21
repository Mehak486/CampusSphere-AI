# 🎓 CampusSphere AI

AI-powered **Student Database Application System** built with FastAPI, Gemini API, LangGraph and ChromaDB.

## 🚀 Live Demo

* **Dashboard:** [CampusSphere AI](https://campussphere-ai-aqxw.onrender.com/?utm_source=chatgpt.com)
* **Swagger API:** [API Documentation](https://campussphere-ai-aqxw.onrender.com/docs?utm_source=chatgpt.com)
* **ReDoc:** [ReDoc](https://campussphere-ai-aqxw.onrender.com/redoc?utm_source=chatgpt.com)
* **Health Check:** [Health Check](https://campussphere-ai-aqxw.onrender.com/health?utm_source=chatgpt.com)

## ✨ Features

* Student, Course & Enrollment CRUD
* FastAPI REST APIs
* Swagger/OpenAPI documentation
* Responsive student dashboard
* Gemini-powered AI chatbot
* LangGraph AI workflow
* ChromaDB vector search
* SQLite database
* Render deployment

## 🛠️ Tech Stack

**Backend:** Python, FastAPI, SQLAlchemy
**Database:** SQLite
**AI:** Gemini API, LangGraph
**Vector DB:** ChromaDB
**Frontend:** HTML, CSS, JavaScript
**Deployment:** Render

## ⚙️ Run Locally

```bash
git clone https://github.com/Mehak486/CampusSphere-AI.git
cd CampusSphere-AI
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env`:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.6-flash
```

Run:

```bash
python scripts/seed_data.py
python -m uvicorn app.main:app --reload --port 8000
```

## 🤖 AI Chatbot

The chatbot uses **Gemini + LangGraph + ChromaDB** to answer questions about students, courses and enrollments.

## 👩‍💻 Developer

**Mehak Sharma**
B.Tech Computer Science Engineering Graduate

GitHub: [Mehak486](https://github.com/Mehak486?utm_source=chatgpt.com)


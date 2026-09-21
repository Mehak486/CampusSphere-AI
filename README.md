# CampusSphere AI — Student Database Application System

A professional Final Year Internship Project built around a modular FastAPI backend and an aesthetic web dashboard.

## ✨ Project requirements covered

- Modular backend architecture
- Student, Course and Enrollment CRUD
- FastAPI REST APIs
- Swagger / OpenAPI + ReDoc
- Deployable Docker + Render configuration
- Gemini API integration
- LangGraph AI chatbot
- ChromaDB vector database for semantic student retrieval
- Dashboard UI with analytics and responsive design
- Seed data and one-command startup workflow

## 🧠 AI architecture

`User question → LangGraph → ChromaDB semantic retrieval → Gemini → grounded response`

The chatbot is instructed to use retrieved database context and avoid inventing student records.

## 🛠 Tech stack

**Backend:** Python, FastAPI, SQLAlchemy, Pydantic  
**Database:** SQLite (portable default)  
**AI:** Gemini API, LangGraph  
**Vector DB:** ChromaDB  
**Frontend:** HTML, CSS, JavaScript  
**Deployment:** Docker, Render

## ▶ Run locally on Windows CMD

```cmd
cd /d C:\Users\mehak\Downloads\CampusSphere-AI\student-database-backend
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
python scripts\seed_data.py
python -m uvicorn app.main:app --reload --port 8000
```

Open:
- Dashboard: http://127.0.0.1:8000/
- Swagger: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- Health: http://127.0.0.1:8000/health

### Gemini setup

Edit `.env` and set:

```env
GEMINI_API_KEY=your_real_key
GEMINI_MODEL=gemini-2.5-flash
```

Without a Gemini key, the dashboard and CRUD APIs still work; only AI chat requires the key.

## 📁 Structure

```text
student-database-backend/
├── app/
│   ├── routers/             # Students, courses, enrollments
│   ├── services/
│   │   ├── chatbot/         # LangGraph workflow
│   │   ├── gemini_service.py
│   │   └── vector_service.py
│   ├── crud.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── main.py
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── scripts/
│   └── seed_data.py
├── data/
├── Dockerfile
├── render.yaml
├── requirements.txt
└── README.md
```

## 🔌 API highlights

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/students` | List students |
| POST | `/api/students` | Create student |
| GET | `/api/students/{id}` | Get student |
| PUT | `/api/students/{id}` | Update student |
| DELETE | `/api/students/{id}` | Delete student |
| GET/POST | `/api/courses` | Course management |
| GET/POST | `/api/enrollments` | Enrollment management |
| POST | `/api/chat` | AI student database assistant |
| GET | `/api/dashboard/stats` | Dashboard analytics |

## ☁️ Deployment

The included `Dockerfile` and `render.yaml` are ready for a Render web service. Add `GEMINI_API_KEY` as a secret environment variable before using the AI chatbot in production.

## 📌 Submission checklist

1. Test `/`, `/docs`, CRUD endpoints and `/api/chat`.
2. Add your `.env` to `.gitignore` and never commit the real API key.
3. Push the complete project to GitHub.
4. Confirm the repository is accessible.
5. Submit the GitHub repository link through the official Google Form before the assigned deadline.

## 👩‍💻 Author

**Mehak Sharma**  
B.Tech Computer Science Graduate  
GitHub: https://github.com/Mehak486  
LinkedIn: https://linkedin.com/in/mehak-112704300

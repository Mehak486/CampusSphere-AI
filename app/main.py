
from contextlib import asynccontextmanager

from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import func

from .database import Base, engine, get_db
from .models import Student, Course, Enrollment
from .schemas import ChatRequest, ChatResponse
from .routers import students, courses, enrollments
from .services.chatbot.graph import build_chat_graph
from .services.vector_service import VectorService


# ============================================================
# API TAGS
# ============================================================

TAGS = [
    {
        "name": "System",
        "description": "Health, dashboard and API information."
    },
    {
        "name": "Students",
        "description": "Complete student CRUD operations."
    },
    {
        "name": "Courses",
        "description": "Complete course CRUD operations."
    },
    {
        "name": "Enrollments",
        "description": "Student-course enrollment management."
    },
    {
        "name": "AI Chatbot",
        "description": "LangGraph + ChromaDB + Gemini student database assistant."
    },
]


# ============================================================
# APPLICATION LIFESPAN
# ============================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup and shutdown lifecycle.

    Startup:
    - Creates database tables
    - Indexes students into ChromaDB
    - Builds LangGraph chatbot

    Shutdown:
    - FastAPI automatically handles application cleanup
    """

    print("\n" + "=" * 60)
    print("🚀 Starting CampusSphere AI...")
    print("=" * 60)

    try:
        # ----------------------------------------------------
        # Create database tables
        # ----------------------------------------------------
        Base.metadata.create_all(bind=engine)

        print("✅ Database initialized")

        # ----------------------------------------------------
        # Index existing students into ChromaDB
        # ----------------------------------------------------
        db = next(get_db())

        try:
            records = db.query(Student).all()

            if records:
                try:
                    VectorService().index_students(records)
                    print(
                        f"✅ ChromaDB indexed {len(records)} student records"
                    )
                except Exception as vector_error:
                    print(
                        f"⚠️ ChromaDB indexing skipped: {vector_error}"
                    )
            else:
                print("ℹ️ No students found for ChromaDB indexing")

        finally:
            db.close()

        # ----------------------------------------------------
        # Build LangGraph chatbot
        # ----------------------------------------------------
        try:
            app.state.chat_graph = build_chat_graph()
            print("✅ LangGraph chatbot initialized")
        except Exception as graph_error:
            print(
                f"⚠️ LangGraph initialization failed: {graph_error}"
            )
            app.state.chat_graph = None

        print("=" * 60)
        print("✅ CampusSphere AI is ready")
        print("📚 Swagger: http://127.0.0.1:8000/docs")
        print("🏠 Dashboard: http://127.0.0.1:8000/")
        print("=" * 60 + "\n")

    except Exception as startup_error:
        print("\n❌ Startup error:")
        print(startup_error)
        print()

    yield

    # --------------------------------------------------------
    # Shutdown
    # --------------------------------------------------------
    print("\n🛑 CampusSphere AI stopped.")


# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    lifespan=lifespan,

    title="CampusSphere AI — Student Database Application System",

    summary=(
        "Professional Final Year Internship Backend "
        "with FastAPI, Gemini, LangGraph and ChromaDB"
    ),

    description="""
# CampusSphere AI

Student Database Application System developed as a final-year
internship project.

## Main Features

- Student CRUD
- Course CRUD
- Enrollment management
- Dashboard analytics
- FastAPI REST APIs
- Swagger documentation
- Gemini AI integration
- LangGraph AI chatbot
- ChromaDB vector database
- Semantic student search
- SQLite database
- Deployable backend
- Professional web dashboard

## AI Assistant

The AI assistant can answer questions about the student database,
including students, departments, semesters and CGPA.
""",

    version="2.0.0",

    openapi_tags=TAGS,

    docs_url="/docs",

    redoc_url="/redoc",

    openapi_url="/openapi.json",
)


# ============================================================
# STATIC FRONTEND
# ============================================================

app.mount(
    "/static",
    StaticFiles(directory="frontend"),
    name="static"
)


# ============================================================
# API ROUTERS
# ============================================================

app.include_router(students.router)
app.include_router(courses.router)
app.include_router(enrollments.router)


# ============================================================
# DASHBOARD
# ============================================================

@app.get(
    "/",
    include_in_schema=False
)
def dashboard():
    """
    Serve the CampusSphere AI dashboard.
    """

    return FileResponse(
        "frontend/index.html"
    )


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get(
    "/health",
    tags=["System"]
)
def health():
    """
    Check whether the backend is running.
    """

    return {
        "status": "healthy",
        "service": "CampusSphere AI",
        "version": "2.0.0"
    }


# ============================================================
# DASHBOARD STATISTICS
# ============================================================

@app.get(
    "/api/dashboard/stats",
    tags=["System"]
)
def dashboard_stats():
    """
    Return dashboard statistics.
    """

    db = next(get_db())

    try:

        # ----------------------------------------------------
        # Basic counts
        # ----------------------------------------------------

        students_count = (
            db.query(
                func.count(Student.id)
            ).scalar() or 0
        )

        courses_count = (
            db.query(
                func.count(Course.id)
            ).scalar() or 0
        )

        enrollments_count = (
            db.query(
                func.count(Enrollment.id)
            ).scalar() or 0
        )

        # ----------------------------------------------------
        # Average CGPA
        # ----------------------------------------------------

        avg_cgpa = (
            db.query(
                func.avg(Student.cgpa)
            ).scalar()
        )

        # ----------------------------------------------------
        # Students by department
        # ----------------------------------------------------

        departments = (
            db.query(
                Student.department,
                func.count(Student.id)
            )
            .group_by(Student.department)
            .all()
        )

        # ----------------------------------------------------
        # Recent students
        # ----------------------------------------------------

        recent = (
            db.query(Student)
            .order_by(Student.id.desc())
            .limit(5)
            .all()
        )

        # ----------------------------------------------------
        # Response
        # ----------------------------------------------------

        return {
            "students": students_count,

            "courses": courses_count,

            "enrollments": enrollments_count,

            "avg_cgpa": (
                round(float(avg_cgpa), 2)
                if avg_cgpa is not None
                else 0
            ),

            "departments": [
                {
                    "name": department,
                    "count": count
                }
                for department, count in departments
            ],

            "recent_students": [
                {
                    "id": student.id,
                    "name": student.name,
                    "email": student.email,
                    "department": student.department,
                    "semester": student.semester,
                    "cgpa": student.cgpa
                }
                for student in recent
            ]
        }

    finally:

        db.close()


# ============================================================
# AI CHATBOT
# ============================================================

@app.post(
    "/api/chat",
    response_model=ChatResponse,
    tags=["AI Chatbot"]
)
def chat(request: ChatRequest):
    """
    Ask the CampusSphere AI assistant a question.

    Example:

    {
        "message": "How many students are in Computer Science?"
    }
    """

    # --------------------------------------------------------
    # Make sure LangGraph exists
    # --------------------------------------------------------

    if not hasattr(app.state, "chat_graph"):
        try:
            app.state.chat_graph = build_chat_graph()
        except Exception as error:
            return ChatResponse(
                answer=(
                    "AI chatbot could not be initialized. "
                    f"Error: {str(error)}"
                ),
                sources=[]
            )

    # --------------------------------------------------------
    # If graph failed during startup
    # --------------------------------------------------------

    if app.state.chat_graph is None:
        try:
            app.state.chat_graph = build_chat_graph()
        except Exception as error:
            return ChatResponse(
                answer=(
                    "AI chatbot is currently unavailable. "
                    f"Error: {str(error)}"
                ),
                sources=[]
            )

    # --------------------------------------------------------
    # Run LangGraph
    # --------------------------------------------------------

    try:

        result = app.state.chat_graph.invoke(
            {
                "question": request.message
            }
        )

        return ChatResponse(
            answer=result.get(
                "answer",
                "I could not generate an answer."
            ),

            sources=result.get(
                "sources",
                []
            )
        )

    except Exception as error:

        print("\n❌ Chatbot error:")
        print(error)
        print()

        return ChatResponse(
            answer=(
                "I could not process your question right now. "
                "Please check the backend terminal for details."
            ),
            sources=[]
        )

from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.database import Base, engine, SessionLocal
from app.models import Student, Course, Enrollment
from app.services.vector_service import VectorService

Base.metadata.create_all(bind=engine)
db = SessionLocal()
try:
    if db.query(Student).count() == 0:
        students = [
            Student(name="Aarav Sharma", email="aarav@example.com", department="Computer Science", semester=8, cgpa=8.9, phone="9876543210"),
            Student(name="Riya Verma", email="riya@example.com", department="Information Technology", semester=7, cgpa=8.4, phone="9876543211"),
            Student(name="Kabir Singh", email="kabir@example.com", department="Electronics", semester=6, cgpa=7.8, phone="9876543212"),
            Student(name="Ananya Gupta", email="ananya@example.com", department="Computer Science", semester=8, cgpa=9.2, phone="9876543213"),
            Student(name="Dev Patel", email="dev@example.com", department="Mechanical", semester=5, cgpa=7.6, phone="9876543214"),
            Student(name="Mehak Sharma", email="mehak@example.com", department="Computer Science", semester=8, cgpa=8.7, phone="9876543215"),
        ]
        db.add_all(students)
        db.flush()
    if db.query(Course).count() == 0:
        courses = [
            Course(code="CS401", name="Machine Learning", credits=4),
            Course(code="CS402", name="Database Systems", credits=4),
            Course(code="CS403", name="Web Engineering", credits=3),
            Course(code="AI404", name="Generative AI", credits=3),
        ]
        db.add_all(courses)
        db.flush()
    if db.query(Enrollment).count() == 0:
        students = db.query(Student).all()
        courses = db.query(Course).all()
        grades = ["A+","A","B+","A","B+","A+"]
        for i, s in enumerate(students):
            db.add(Enrollment(student_id=s.id, course_id=courses[i % len(courses)].id, grade=grades[i]))
    db.commit()
    VectorService().index_students(db.query(Student).all())
    print("CampusSphere AI seed completed successfully.")
finally:
    db.close()

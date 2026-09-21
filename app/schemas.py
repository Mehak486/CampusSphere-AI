from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentBase(BaseModel):
    name: str = Field(min_length=2, max_length=120, examples=["Mehak Sharma"])
    email: EmailStr = Field(examples=["mehak@example.com"])
    department: str = Field(min_length=2, max_length=100, examples=["Computer Science"])
    semester: int = Field(ge=1, le=12, examples=[8])
    cgpa: float = Field(ge=0, le=10, examples=[8.75])
    phone: str | None = Field(default=None, max_length=30, examples=["9876543210"])


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=120, examples=["Updated Name"])
    email: EmailStr | None = Field(default=None, examples=["updated@example.com"])
    department: str | None = Field(default=None, min_length=2, max_length=100, examples=["Information Technology"])
    semester: int | None = Field(default=None, ge=1, le=12, examples=[7])
    cgpa: float | None = Field(default=None, ge=0, le=10, examples=[9.1])
    phone: str | None = Field(default=None, max_length=30, examples=["9876500000"])


class StudentOut(StudentBase):
    id: int = Field(examples=[1])
    model_config = ConfigDict(from_attributes=True)


class CourseBase(BaseModel):
    code: str = Field(min_length=2, max_length=30, examples=["CS401"])
    name: str = Field(min_length=2, max_length=120, examples=["Machine Learning"])
    credits: int = Field(ge=1, le=10, examples=[4])


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    code: str | None = Field(default=None, min_length=2, max_length=30, examples=["CS405"])
    name: str | None = Field(default=None, min_length=2, max_length=120, examples=["Advanced Python"])
    credits: int | None = Field(default=None, ge=1, le=10, examples=[3])


class CourseOut(CourseBase):
    id: int = Field(examples=[1])
    model_config = ConfigDict(from_attributes=True)


class EnrollmentCreate(BaseModel):
    student_id: int = Field(examples=[1])
    course_id: int = Field(examples=[1])
    grade: str | None = Field(default=None, max_length=5, examples=["A+"])


class EnrollmentOut(EnrollmentCreate):
    id: int = Field(examples=[1])
    model_config = ConfigDict(from_attributes=True)


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000, examples=["Which students have a CGPA above 8?"])


class ChatResponse(BaseModel):
    answer: str
    sources: list[str] = []

from pydantic import BaseModel, Field, ValidationError


class Student(BaseModel):
    sName: str = Field(min_length=2)
    sAge: int = Field(ge=5, le=100)
    aGrade: str = Field(min_length=1)


class Teacher(BaseModel):
    tName: str = Field(min_length=2)
    tAge: int = Field(ge=18, le=100)
    subject: str = Field(min_length=2)


class School(BaseModel):
    schoolName: str = Field(min_length=2)
    schoolID: int = Field(gt=0)
    students: list[Student]
    teachers: list[Teacher]


try:
    student1 = Student(sName="John", sAge="20", aGrade="A")
    student2 = Student(sName="Emma", sAge=18, aGrade="A+")

    teacher1 = Teacher(tName="Alice", tAge=30, subject="Math")
    teacher2 = Teacher(tName="Robert", tAge=42, subject="Science")

    school = School(
        schoolName="Greenwood High",
        schoolID=101,
        students=[student1, student2],
        teachers=[teacher1, teacher2],
    )

    print("Student:")
    print(student1)
    print(student1.sName)
    print(student1.sAge)  # "20" was converted to integer 20

    print("\nTeacher:")
    print(teacher1)

    print("\nSchool:")
    print(school)

    print("\nSchool as dictionary:")
    print(school.model_dump())

    print("\nClass names:")
    print(type(school).__name__)    # School
    print(type(student1).__name__)  # Student
    print(type(teacher1).__name__)  # Teacher

    print("\n== Error Scenario ==\n")

    # This fails because sAge must be 5 or more.
    invalid_student = Student(sName="John", sAge=4, aGrade="A")
    print(invalid_student)

except ValidationError as error:
    print("Validation error:")
    print(error)
from pydantic import BaseModel, Field, ValidationError


class Student(BaseModel):
    first_name: str = Field(
        description="Student's first name",
        min_length=2,
        max_length=100,
    )
    middle_name: str | None = Field(
        default=None,
        description="Student's middle name, if available",
        min_length=2,
        max_length=100,
    )
    last_name: str | None = Field(
         default=None,
        description="Student's last name, if available",
        min_length=2,
        max_length=100,
    )
    age: int = Field(
        description="Student's age in years",
        ge=5,
        le=100,
    )
    grade: str = Field(
        description="Student's academic grade",
        min_length=1,
        max_length=10,
    )


class Teacher(BaseModel):
    name: str = Field(
        description="Teacher's name",
        min_length=2,
        max_length=100,
    )
    age: int = Field(
        description="Teacher's age in years",
        ge=18,
        le=100,
    )
    subject: str = Field(
        description="Subject taught by the teacher",
        min_length=2,
        max_length=100,
    )


class School(BaseModel):
    name: str = Field(
        description="School's name",
        min_length=2,
        max_length=150,
    )
    school_id: int = Field(
        default=100,
        description="Unique school identification number",
        gt=99,
    )
    students: list[Student]
    teachers: list[Teacher]


def main() -> None:
    try:
        student1 = Student(
            first_name="Ankit",
            middle_name="Kumar",
            last_name="Gupta",
            age="20",  # Pydantic converts this string to integer 20.
            grade="A",
        )

        student2 = Student(
            first_name="Sumit",
            age=18,
            grade="A+",
        )

        teacher1 = Teacher(name="DurgaSoft", age=30, subject="Programming")
        teacher2 = Teacher(name="Rahul", age=42, subject="Science")

        school = School(
            name="DurgaClasses",
            school_id=101,
            students=[student1, student2],
            teachers=[teacher1, teacher2],
        )

        # school_id is omitted, so its default value is 100.
        school_with_default_id = School(
            name="DurgaClasses",
            students=[student1, student2],
            teachers=[teacher1, teacher2],
        )

        print("Student:")
        print(student1)

        print("\nSchool as dictionary:")
        print(school.model_dump())

        print("\nSchool with default ID:")
        print(school_with_default_id.school_id)  # 100

        print("\nClass names:")
        print(type(school).__name__)    # School
        print(type(student1).__name__)  # Student
        print(type(teacher1).__name__)  # Teacher

        print("\n== Validation Error Scenario ==")
        Student(first_name="Ankit", age=4, grade="A")

    except ValidationError as error:
        print(error)


if __name__ == "__main__":
    main()
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table

DATABASE_URL = 'sqlite:///students.db'
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# define the students table
student_table = Table('students', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(50), nullable=False),
    Column('age', Integer, nullable=False),
    Column('grade', String(10), nullable=False)
)

# create the table
metadata.create_all(engine)

# insert data
with engine.connect() as connection:
    connection.execute(student_table.insert(), [
        {"name": "Alice", "age": 20, "grade": "A"},
        {"name": "Bob", "age": 22, "grade": "B"}
    ])
    connection.commit()
print("Students added successfully!")

insert_student1 = student_table.insert().values(name="Charlie", age=23, grade="C")
with engine.connect() as connection:
    connection.execute(insert_student1)
    connection.commit()
print("Student Charlie added successfully!")

delete_charlie = student_table.delete().where(student_table.c.name == "Charlie")
with engine.connect() as connection:
    connection.execute(delete_charlie)
    connection.commit()
print("Student Charlie deleted successfully!")
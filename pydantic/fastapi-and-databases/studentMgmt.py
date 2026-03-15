#assignment Question: Create a Student Management System using SQLAlchemy Core with MySQL having the following requirements:
# Column Name	Data Type	Constraints
# id	Integer	Primary Key
# name	String	Not Null
# age	Integer	18+
# city	String	Nullable

# You have to perform following operations:

# Create database connection
# Create students table
# Insert 3 student records
# Fetch all students
# Update city of student whose name = "Rahul"
# Delete student whose age < 20

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, CheckConstraint
from sqlalchemy.sql import select, insert, update, delete

# Create engine and metadata
engine = create_engine('sqlite:///student_mgmt.db')  # Using SQLite for simplicity; replace with MySQL connection string as needed
metadata = MetaData()

# Define the students table
students = Table('students', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(100), nullable=False),
    Column('age', Integer, nullable=False),
    Column('city', String(50), nullable=True),
    CheckConstraint('age > 18', name='age_check'),
    CheckConstraint('LENGTH(name) > 10', name='name_not_empty')
)

# Ensure the table exists in the database
metadata.create_all(engine)

# insert_stmt = insert(students).values(name='Virat Kohli', age=37, city='Bangalore')
# with engine.connect() as conn:
#     conn.execute(insert_stmt)
#     conn.commit()
    
        
# update_stmt = update(students).where(students.c.name == 'Rahul Yadav').values(city='Jaipur')
# with engine.connect() as conn:
#     conn.execute(update_stmt)
#     conn.commit()

delete_stmt = delete(students).where(students.c.id == 6)
with engine.connect() as conn:
    conn.execute(delete_stmt)
    conn.commit()

# delete_table_stmt = students.delete()
# with engine.connect() as conn:
#     conn.execute(delete_table_stmt)
#     conn.commit()

select_stmt = select(students)
with engine.connect() as conn:
    result = conn.execute(select_stmt)
    for row in result:
        print(row)
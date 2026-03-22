from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///students.db')
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    grade = Column(String(10), nullable=False)
    
# create the table
Base.metadata.create_all(engine)

# create a session
Session = sessionmaker(bind=engine)
session = Session()

# insert data
student = Student(name="Alice", age=20, grade="A")
session.add(student)
session.commit()

print("Student added successfully!")
session.close()
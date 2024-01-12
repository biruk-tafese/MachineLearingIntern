# models/medical_database.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    symptoms = relationship('Symptom', back_populates='patient')
    medical_history = Column(String)
    treatment_plan = Column(String)

class Symptom(Base):
    __tablename__ = 'symptoms'

    id = Column(Integer, primary_key=True)
    code = Column(String)
    name = Column(String)
    description = Column(String)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    patient = relationship('Patient', back_populates='symptoms')

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

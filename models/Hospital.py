# models/hospital.py
class Hospital:
    def __init__(self, name, patients):
        self.name = name
        self.patients = patients

class Patient:
    def __init__(self, name, symptoms, medical_history, treatment_plan):
        self.name = name
        self.symptoms = symptoms
        self.medical_history = medical_history
        self.treatment_plan = treatment_plan

class Symptom:
    def __init__(self, code, name, description):
        self.code = code
        self.name = name
        self.description = description

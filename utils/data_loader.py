# utils/data_loader.py
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def load_courses_data():
    return load_data('data/courses_data.csv')

def load_student_data():
    return load_data('data/student_data.csv')


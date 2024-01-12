# utils/academic_plan_generator.py
def generate_academic_plan(recommended_courses):
    academic_plan = {"Semester 1": recommended_courses[:2], "Semester 2": recommended_courses[2:]}
    return academic_plan


# models/recommendation_engine.py
from models.collabFilter import train_collaborative_filtering, evaluate_collaborative_filtering, get_collaborative_filtering_recommendations
from models.contentFilter import train_content_based_filtering, get_content_based_recommendations

def train_recommendation_models(df, courses_data):
    collaborative_model = train_collaborative_filtering(df)
    content_based_model = train_content_based_filtering(courses_data)
    return collaborative_model, content_based_model

def evaluate_models(collaborative_model, testset):
    evaluate_collaborative_filtering(collaborative_model, testset)

def get_personalized_recommendations(user_id, collaborative_model, content_based_model, courses_data):
    collaborative_recommendations = get_collaborative_filtering_recommendations(collaborative_model, user_id)
    content_based_recommendations = get_content_based_recommendations(user_selected_course, content_based_model, courses_data)
    personalized_recommendations = collaborative_recommendations + content_based_recommendations
    return personalized_recommendations


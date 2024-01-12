# models/medical_diagnostic_rephrasing.py
from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import train_test_split
from surprise import accuracy

def train_medical_diagnostic_rephrasing(patient_data):
    patient_reader = Reader(rating_scale=(1, 5))
    patient_set = Dataset.load_from_df(patient_data[['patient_id', 'symptom_id', 'severity']], patient_reader)
    similarity_options = {'name': 'cosine', 'user_based': False}
    diagnostic_rephrasing_model = KNNBasic(sim_options=similarity_options)
    training_set = patient_set.build_full_trainset()
    diagnostic_rephrasing_model.fit(training_set)
    return diagnostic_rephrasing_model

def evaluate_medical_diagnostic_rephrasing(diagnostic_rephrasing_model, test_set):
    predictions = diagnostic_rephrasing_model.test(test_set)
    root_mean_squared_error = accuracy.rmse(predictions)
    print(f'Root Mean Squared Error: {root_mean_squared_error}')

def get_medical_diagnostic_rephrasing_recommendations(diagnostic_rephrasing_model, patient_identifier, num_recommendations=3):
    all_symptom_identifiers = diagnostic_rephrasing_model.trainset.all_items()
    patient_severities = diagnostic_rephrasing_model.trainset.ur[patient_identifier]
    predictions = [diagnostic_rephrasing_model.predict(str(patient_identifier), str(symptom_id)) for symptom_id in all_symptom_identifiers if symptom_id not in patient_severities]
    sorted_predictions = sorted(predictions, key=lambda x: x.est, reverse=True)
    top_recommendations = [prediction.iid for prediction in sorted_predictions[:num_recommendations]]

    return top_recommendations

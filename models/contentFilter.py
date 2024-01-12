# models/medical_diagnosis_system.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def train_medical_diagnosis_system(symptoms_data):
    symptom_descriptions = symptoms_data['description'].fillna('')
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(symptom_descriptions)
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

    return cosine_similarities

def get_medical_diagnosis_recommendations(symptom_name, cosine_similarities, symptoms_data, n=3):
    symptom_index = symptoms_data[symptoms_data['name'] == symptom_name].index[0]
    similarity_scores = list(enumerate(cosine_similarities[symptom_index]))
    sorted_symptoms = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    recommended_symptoms = [symptoms_data.iloc[idx]['name'] for idx, _ in sorted_symptoms if idx != symptom_index]
    top_n_recommendations = recommended_symptoms[:n]

    return top_n_recommendations

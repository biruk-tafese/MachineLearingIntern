# main.py
from models.hospital import Hospital, Patient, Symptom
from models.diagnostic import train_diagnostic_models, evaluate_diagnostic_models, get_personalized_diagnosis
from utils.data_loader import load_patient_data, load_symptoms_data
from utils.preprocessing import split_data

def main():
    patient_data = load_patient_data()
    symptoms_data = load_symptoms_data()

    hospital = Hospital("Sample Hospital", [
        Patient("John Doe", [
            Symptom("SYM101", "Fever", "Elevated body temperature."),
            Symptom("SYM201", "Cough", "Persistent coughing.")
        ], "Patient's medical history goes here.", "Treatment plan details.")
    ])

    # Split data into training and testing sets
    train_data, test_data = split_data(patient_data)

    # Train diagnostic models
    diagnostic_model = train_diagnostic_models(train_data, symptoms_data)

    # Evaluate the model
    evaluate_diagnostic_models(diagnostic_model, test_data)

    patient_id = 1
    diagnosis = get_personalized_diagnosis(patient_id, diagnostic_model, symptoms_data)

    print(f"Personalized Diagnosis for Patient {patient_id}: {diagnosis}")

if __name__ == "__main__":
    main()

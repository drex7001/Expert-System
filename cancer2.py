# import numpy as np
# import skfuzzy as fuzz
# from skfuzzy import control as ctrl
# import pandas as pd
# from sklearn.metrics import confusion_matrix, classification_report

# # Define the fuzzy variables and the fuzzy rules (as previously described)
# def setup_fuzzy_system():
#     age = ctrl.Antecedent(np.arange(20, 81, 1), 'age')
#     bmi = ctrl.Antecedent(np.arange(15, 41, 1), 'bmi')
#     smoking = ctrl.Antecedent(np.arange(0, 2, 1), 'smoking')
#     genetic_risk = ctrl.Antecedent(np.arange(0, 3, 1), 'genetic_risk')
#     physical_activity = ctrl.Antecedent(np.arange(0, 11, 1), 'physical_activity')
#     alcohol_intake = ctrl.Antecedent(np.arange(0, 6, 1), 'alcohol_intake')
#     cancer_history = ctrl.Antecedent(np.arange(0, 2, 1), 'cancer_history')

#     diagnosis = ctrl.Consequent(np.arange(0, 2, 1), 'diagnosis')

#     age.automf(3)
#     bmi.automf(3)
#     physical_activity.automf(3)
#     alcohol_intake.automf(3)

#     smoking['no'] = fuzz.trimf(smoking.universe, [0, 0, 1])
#     smoking['yes'] = fuzz.trimf(smoking.universe, [0, 1, 1])

#     genetic_risk['low'] = fuzz.trimf(genetic_risk.universe, [0, 0, 1])
#     genetic_risk['medium'] = fuzz.trimf(genetic_risk.universe, [0, 1, 2])
#     genetic_risk['high'] = fuzz.trimf(genetic_risk.universe, [1, 2, 2])

#     cancer_history['no'] = fuzz.trimf(cancer_history.universe, [0, 0, 1])
#     cancer_history['yes'] = fuzz.trimf(cancer_history.universe, [0, 1, 1])

#     diagnosis['no_cancer'] = fuzz.trimf(diagnosis.universe, [0, 0, 1])
#     diagnosis['cancer'] = fuzz.trimf(diagnosis.universe, [0, 1, 1])

#     rules = [
#         ctrl.Rule(cancer_history['yes'], diagnosis['cancer']),
#         ctrl.Rule((age['poor'] & genetic_risk['high']) | 
#                   (bmi['poor'] & smoking['yes']) | 
#                   (physical_activity['poor'] & alcohol_intake['good']), diagnosis['cancer']),
#         ctrl.Rule((age['average'] & genetic_risk['medium']) |
#                   (bmi['average'] & smoking['yes']) |
#                   (physical_activity['average'] & alcohol_intake['average']), diagnosis['cancer']),
#         ctrl.Rule(~cancer_history['yes'] & (age['good'] | genetic_risk['low'] | 
#                                             bmi['good'] | smoking['no'] |
#                                             physical_activity['good'] | alcohol_intake['poor']), diagnosis['no_cancer'])
#     ]

#     cancer_ctrl = ctrl.ControlSystem(rules)
#     cancer_diagnosis = ctrl.ControlSystemSimulation(cancer_ctrl)

#     return cancer_diagnosis

# def diagnose_cancer(cancer_diagnosis, patient_data):
#     cancer_diagnosis.input['age'] = patient_data['age']
#     cancer_diagnosis.input['bmi'] = patient_data['bmi']
#     cancer_diagnosis.input['smoking'] = patient_data['smoking']
#     cancer_diagnosis.input['genetic_risk'] = patient_data['genetic_risk']
#     cancer_diagnosis.input['physical_activity'] = patient_data['physical_activity']
#     cancer_diagnosis.input['alcohol_intake'] = patient_data['alcohol_intake']
#     cancer_diagnosis.input['cancer_history'] = patient_data['cancer_history']

#     cancer_diagnosis.compute()
#     diagnosis_result = cancer_diagnosis.output['diagnosis']
#     return 1 if diagnosis_result >= 0.5 else 0

# def process_csv(file_path):
#     data = pd.read_csv(file_path)
#     cancer_diagnosis = setup_fuzzy_system()

#     y_true = data['Diagnosis']
#     y_pred = []

#     for _, row in data.iterrows():
#         patient_data = {
#             'age': row['Age'],
#             'bmi': row['BMI'],
#             'smoking': row['Smoking'],
#             'genetic_risk': row['GeneticRisk'],
#             'physical_activity': row['PhysicalActivity'],
#             'alcohol_intake': row['AlcoholIntake'],
#             'cancer_history': row['CancerHistory']
#         }
#         prediction = diagnose_cancer(cancer_diagnosis, patient_data)
#         y_pred.append(prediction)

#     return y_true, y_pred

# def main(file_path):
#     y_true, y_pred = process_csv(file_path)
#     cm = confusion_matrix(y_true, y_pred)
#     report = classification_report(y_true, y_pred)

#     print("Confusion Matrix:\n", cm)
#     print("\nClassification Report:\n", report)

# # Example usage
# file_path = 'cancer_data.csv'  # Replace with your CSV file path
# main(file_path)


import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split

# Define the fuzzy variables and the fuzzy rules (as previously described)
def setup_fuzzy_system():
    age = ctrl.Antecedent(np.arange(20, 81, 1), 'age')
    bmi = ctrl.Antecedent(np.arange(15, 41, 1), 'bmi')
    smoking = ctrl.Antecedent(np.arange(0, 2, 1), 'smoking')
    genetic_risk = ctrl.Antecedent(np.arange(0, 3, 1), 'genetic_risk')
    physical_activity = ctrl.Antecedent(np.arange(0, 11, 1), 'physical_activity')
    alcohol_intake = ctrl.Antecedent(np.arange(0, 6, 1), 'alcohol_intake')
    cancer_history = ctrl.Antecedent(np.arange(0, 2, 1), 'cancer_history')

    diagnosis = ctrl.Consequent(np.arange(0, 2, 1), 'diagnosis')

    age.automf(3)
    bmi.automf(3)
    physical_activity.automf(3)
    alcohol_intake.automf(3)

    smoking['no'] = fuzz.trimf(smoking.universe, [0, 0, 1])
    smoking['yes'] = fuzz.trimf(smoking.universe, [0, 1, 1])

    genetic_risk['low'] = fuzz.trimf(genetic_risk.universe, [0, 0, 1])
    genetic_risk['medium'] = fuzz.trimf(genetic_risk.universe, [0, 1, 2])
    genetic_risk['high'] = fuzz.trimf(genetic_risk.universe, [1, 2, 2])

    cancer_history['no'] = fuzz.trimf(cancer_history.universe, [0, 0, 1])
    cancer_history['yes'] = fuzz.trimf(cancer_history.universe, [0, 1, 1])

    diagnosis['no_cancer'] = fuzz.trimf(diagnosis.universe, [0, 0, 1])
    diagnosis['cancer'] = fuzz.trimf(diagnosis.universe, [0, 1, 1])

    rules = [
        ctrl.Rule(cancer_history['yes'], diagnosis['cancer']),
        ctrl.Rule((age['poor'] & genetic_risk['high']) | 
                  (bmi['poor'] & smoking['yes']) | 
                  (physical_activity['poor'] & alcohol_intake['good']), diagnosis['cancer']),
        ctrl.Rule((age['average'] & genetic_risk['medium']) |
                  (bmi['average'] & smoking['yes']) |
                  (physical_activity['average'] & alcohol_intake['average']), diagnosis['cancer']),
        ctrl.Rule(~cancer_history['yes'] & (age['good'] | genetic_risk['low'] | 
                                            bmi['good'] | smoking['no'] |
                                            physical_activity['good'] | alcohol_intake['poor']), diagnosis['no_cancer'])
    ]

    cancer_ctrl = ctrl.ControlSystem(rules)
    cancer_diagnosis = ctrl.ControlSystemSimulation(cancer_ctrl)

    return cancer_diagnosis

def diagnose_cancer(cancer_diagnosis, patient_data):
    cancer_diagnosis.input['age'] = patient_data['age']
    cancer_diagnosis.input['bmi'] = patient_data['bmi']
    cancer_diagnosis.input['smoking'] = patient_data['smoking']
    cancer_diagnosis.input['genetic_risk'] = patient_data['genetic_risk']
    cancer_diagnosis.input['physical_activity'] = patient_data['physical_activity']
    cancer_diagnosis.input['alcohol_intake'] = patient_data['alcohol_intake']
    cancer_diagnosis.input['cancer_history'] = patient_data['cancer_history']

    cancer_diagnosis.compute()
    diagnosis_result = cancer_diagnosis.output['diagnosis']
    return diagnosis_result

def process_csv(file_path):
    data = pd.read_csv(file_path)
    cancer_diagnosis = setup_fuzzy_system()

    y_true = data['Diagnosis']
    y_prob = []

    for _, row in data.iterrows():
        patient_data = {
            'age': row['Age'],
            'bmi': row['BMI'],
            'smoking': row['Smoking'],
            'genetic_risk': row['GeneticRisk'],
            'physical_activity': row['PhysicalActivity'],
            'alcohol_intake': row['AlcoholIntake'],
            'cancer_history': row['CancerHistory']
        }
        prob = diagnose_cancer(cancer_diagnosis, patient_data)
        y_prob.append(prob)

    return data.drop(columns=['Diagnosis']), y_true, np.array(y_prob)

def main(file_path):
    X, y, y_prob = process_csv(file_path)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test, y_prob_train, y_prob_test = train_test_split(
        X, y, y_prob, test_size=0.2, random_state=42, stratify=y
    )

    # Define an optimal threshold
    optimal_threshold = 0.34
    y_pred_final = (y_prob_test >= optimal_threshold).astype(int)

    # Final evaluation
    final_test_accuracy = accuracy_score(y_test, y_pred_final)
    final_test_precision = precision_score(y_test, y_pred_final)
    final_test_recall = recall_score(y_test, y_pred_final)
    final_test_f1 = f1_score(y_test, y_pred_final)
    conf_matrix = confusion_matrix(y_test, y_pred_final)

    print(f"Final Test Accuracy: {final_test_accuracy}")
    print(f"Final Test Precision: {final_test_precision}")
    print(f"Final Test Recall: {final_test_recall}")
    print(f"Final Test F1 Score: {final_test_f1}")
    print(f"Confusion Matrix:\n{conf_matrix}")

# Example usage
file_path = 'cancer_data.csv'  # Replace with your CSV file path
main(file_path)

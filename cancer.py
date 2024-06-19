import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define the fuzzy variables
age = ctrl.Antecedent(np.arange(20, 81, 1), 'age')
bmi = ctrl.Antecedent(np.arange(15, 41, 1), 'bmi')
smoking = ctrl.Antecedent(np.arange(0, 2, 1), 'smoking')
genetic_risk = ctrl.Antecedent(np.arange(0, 3, 1), 'genetic_risk')
physical_activity = ctrl.Antecedent(np.arange(0, 11, 1), 'physical_activity')
alcohol_intake = ctrl.Antecedent(np.arange(0, 6, 1), 'alcohol_intake')
cancer_history = ctrl.Antecedent(np.arange(0, 2, 1), 'cancer_history')

diagnosis = ctrl.Consequent(np.arange(0, 2, 1), 'diagnosis')

# Auto-membership function population
age.automf(3)
bmi.automf(3)
physical_activity.automf(3)
alcohol_intake.automf(3)

# Custom membership functions
smoking['no'] = fuzz.trimf(smoking.universe, [0, 0, 1])
smoking['yes'] = fuzz.trimf(smoking.universe, [0, 1, 1])

genetic_risk['low'] = fuzz.trimf(genetic_risk.universe, [0, 0, 1])
genetic_risk['medium'] = fuzz.trimf(genetic_risk.universe, [0, 1, 2])
genetic_risk['high'] = fuzz.trimf(genetic_risk.universe, [1, 2, 2])

cancer_history['no'] = fuzz.trimf(cancer_history.universe, [0, 0, 1])
cancer_history['yes'] = fuzz.trimf(cancer_history.universe, [0, 1, 1])

diagnosis['no_cancer'] = fuzz.trimf(diagnosis.universe, [0, 0, 1])
diagnosis['cancer'] = fuzz.trimf(diagnosis.universe, [0, 1, 1])

# Define the fuzzy rules
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

# Create control system
cancer_ctrl = ctrl.ControlSystem(rules)
cancer_diagnosis = ctrl.ControlSystemSimulation(cancer_ctrl)

# Input data
patient_data = {
    'age': 55,
    'bmi': 32,
    'smoking': 1,
    'genetic_risk': 2,
    'physical_activity': 1,
    'alcohol_intake': 4,
    'cancer_history': 0
}

# Pass inputs to the ControlSystemSimulation
cancer_diagnosis.input['age'] = patient_data['age']
cancer_diagnosis.input['bmi'] = patient_data['bmi']
cancer_diagnosis.input['smoking'] = patient_data['smoking']
cancer_diagnosis.input['genetic_risk'] = patient_data['genetic_risk']
cancer_diagnosis.input['physical_activity'] = patient_data['physical_activity']
cancer_diagnosis.input['alcohol_intake'] = patient_data['alcohol_intake']
cancer_diagnosis.input['cancer_history'] = patient_data['cancer_history']

# Compute the result
cancer_diagnosis.compute()

# Get the output
diagnosis_result = cancer_diagnosis.output['diagnosis']
print("Cancer Diagnosis:", "Cancer" if diagnosis_result >= 0.5 else "No Cancer")
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define the fuzzy variables (inputs and output)
age = ctrl.Antecedent(np.arange(20, 81, 1), 'age')
bmi = ctrl.Antecedent(np.arange(15, 41, 1), 'bmi')
smoking = ctrl.Antecedent(np.arange(0, 2, 1), 'smoking')
genetic_risk = ctrl.Antecedent(np.arange(0, 3, 1), 'genetic_risk')
physical_activity = ctrl.Antecedent(np.arange(0, 11, 1), 'physical_activity')
alcohol_intake = ctrl.Antecedent(np.arange(0, 6, 1), 'alcohol_intake')
cancer_history = ctrl.Antecedent(np.arange(0, 2, 1), 'cancer_history')
family_history = ctrl.Antecedent(np.arange(0, 2, 1), 'family_history')  # New risk factor
diet_quality = ctrl.Antecedent(np.arange(0, 101, 1), 'diet_quality')  # New risk factor (0-100 scale)
diagnosis = ctrl.Consequent(np.arange(0, 101, 1), 'diagnosis')  # Diagnosis range: 0-100

# Auto-membership function population (automatic generation of membership functions)
age.automf(names=['young', 'middle_aged', 'old'])
bmi.automf(names=['underweight', 'normal', 'overweight', 'obese'])
physical_activity.automf(names=['sedentary', 'moderate', 'active'])
alcohol_intake.automf(names=['low', 'moderate', 'high'])
diet_quality.automf(names=['poor', 'average', 'good'])

# Custom membership functions for binary and categorical variables
smoking['no'] = fuzz.trimf(smoking.universe, [0, 0, 1])
smoking['yes'] = fuzz.trimf(smoking.universe, [0, 1, 1])
genetic_risk['low'] = fuzz.trimf(genetic_risk.universe, [0, 0, 1])
genetic_risk['medium'] = fuzz.trimf(genetic_risk.universe, [0, 1, 2])
genetic_risk['high'] = fuzz.trimf(genetic_risk.universe, [1, 2, 2])
cancer_history['no'] = fuzz.trimf(cancer_history.universe, [0, 0, 1])
cancer_history['yes'] = fuzz.trimf(cancer_history.universe, [0, 1, 1])
family_history['no'] = fuzz.trimf(family_history.universe, [0, 0, 1])
family_history['yes'] = fuzz.trimf(family_history.universe, [0, 1, 1])
diagnosis['no_cancer'] = fuzz.trapmf(diagnosis.universe, [0, 0, 20, 40])
diagnosis['low_risk'] = fuzz.trimf(diagnosis.universe, [20, 40, 60])
diagnosis['high_risk'] = fuzz.trimf(diagnosis.universe, [40, 60, 80])
diagnosis['cancer'] = fuzz.trapmf(diagnosis.universe, [60, 80, 100, 100])

# Define the fuzzy rules
rules = [
    ctrl.Rule(cancer_history['yes'] | family_history['yes'], diagnosis['high_risk']),
    ctrl.Rule((age['old'] & genetic_risk['high']) |
              (bmi['obese'] & smoking['yes']) |
              (physical_activity['sedentary'] & alcohol_intake['high'] & diet_quality['poor']),
              diagnosis['high_risk']),
    ctrl.Rule((age['middle_aged'] & genetic_risk['medium']) |
              (bmi['overweight'] & smoking['yes']) |
              (physical_activity['moderate'] & alcohol_intake['moderate'] & diet_quality['average']),
              diagnosis['low_risk']),
    ctrl.Rule((age['young'] & genetic_risk['low']) |
              (bmi['normal'] & smoking['no']) |
              (physical_activity['active'] & alcohol_intake['low'] & diet_quality['good']),
              diagnosis['no_cancer'])
]

# Create control system
cancer_ctrl = ctrl.ControlSystem(rules)
cancer_diagnosis = ctrl.ControlSystemSimulation(cancer_ctrl)

# Input patient data
patient_data = {
    'age': 45,
    'bmi': 28,
    'smoking': 0,
    'genetic_risk': 1,
    'physical_activity': 3,
    'alcohol_intake': 2,
    'cancer_history': 0,
    'family_history': 1,
    'diet_quality': 60
}

# Pass inputs to the ControlSystemSimulation
for input_var, value in patient_data.items():
    cancer_diagnosis.input[input_var] = value

# Compute the result
cancer_diagnosis.compute()

# Get the output
diagnosis_result = cancer_diagnosis.output['diagnosis']
print("Cancer Diagnosis Risk Score:", diagnosis_result)

# Interpret the result
if diagnosis_result < 40:
    print("Diagnosis: No Cancer")
elif diagnosis_result < 60:
    print("Diagnosis: Low Risk of Cancer")
elif diagnosis_result < 80:
    print("Diagnosis: High Risk of Cancer")
else:
    print("Diagnosis: Cancer")
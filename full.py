from typing import List, Dict, Any
import numpy as np


# Knowledge Base
class KnowledgeBase:
    def __init__(self):
        self.facts = []
        self.rules = []

    def add_fact(self, fact: Dict[str, Any]):
        self.facts.append(fact)

    def add_rule(self, rule: Dict[str, Any]):
        self.rules.append(rule)


# Fuzzy Membership Functions
def fuzzify_age(age):
    if age <= 20:
        return {"young": 1.0, "middle-aged": 0.0, "old": 0.0}
    elif 20 < age <= 40:
        return {"young": (40 - age) / 20, "middle-aged": (age - 20) / 20, "old": 0.0}
    elif 40 < age < 60:
        return {"young": 0.0, "middle-aged": (60 - age) / 20, "old": (age - 40) / 20}
    else:
        return {"young": 0.0, "middle-aged": 0.0, "old": 1.0}


def fuzzify_bmi(bmi):
    if bmi <= 18.5:
        return {"underweight": 1.0, "normal": 0.0, "overweight": 0.0, "obese": 0.0}
    elif 18.5 < bmi <= 24.9:
        return {
            "underweight": (24.9 - bmi) / 6.4,
            "normal": (bmi - 18.5) / 6.4,
            "overweight": 0.0,
            "obese": 0.0,
        }
    elif 24.9 < bmi <= 29.9:
        return {
            "underweight": 0.0,
            "normal": (29.9 - bmi) / 5.0,
            "overweight": (bmi - 24.9) / 5.0,
            "obese": 0.0,
        }
    else:
        return {"underweight": 0.0, "normal": 0.0, "overweight": 0.0, "obese": 1.0}


# Additional membership functions would be defined similarly for other variables.
def fuzzify_physical_activity(activity):
    if activity <= 3:
        return {"low": 1.0, "medium": 0.0, "high": 0.0}
    elif 3 < activity <= 7:
        return {"low": (7 - activity) / 4, "medium": (activity - 3) / 4, "high": 0.0}
    else:
        return {"low": 0.0, "medium": (10 - activity) / 3, "high": (activity - 7) / 3}


def fuzzify_alcohol_intake(intake):
    if intake <= 2:
        return {"low": 1.0, "medium": 0.0, "high": 0.0}
    elif 2 < intake <= 5:
        return {"low": (5 - intake) / 3, "medium": (intake - 2) / 3, "high": 0.0}
    else:
        return {"low": 0.0, "medium": (10 - intake) / 5, "high": (intake - 5) / 5}


# Additional membership functions would be defined similarly for other variables.


# Inference Engine
class InferenceEngine:
    def __init__(self, knowledge_base: KnowledgeBase):
        self.knowledge_base = knowledge_base

    def infer(self, input_data: Dict[str, Any]) -> str:
        max_degree = 0
        best_conclusion = None
        for rule in self.knowledge_base.rules:
            degree = self.match_rule(input_data, rule["conditions"])
            print(f"Rule: {rule['conclusion']}, Degree: {degree}")
            if degree > max_degree:
                max_degree = degree
                best_conclusion = rule["conclusion"]
        if best_conclusion is None:
            return "No conclusion could be drawn."
        else:
            return best_conclusion
    def match_rule(self, input_data: Dict[str, Any], conditions: Dict[str, Any]) -> float:
        degrees = []
        for key, value in conditions.items():
            if key in input_data:
                if key == "Age":
                    age_degrees = fuzzify_age(input_data[key])
                    degrees.append(age_degrees.get(value, 0))
                elif key == "BMI":
                    bmi_degrees = fuzzify_bmi(input_data[key])
                    degrees.append(bmi_degrees.get(value, 0))
                elif key == "PhysicalActivity":
                    activity_degrees = fuzzify_physical_activity(input_data[key])
                    if isinstance(value, tuple) and len(value) == 2:
                        if value[0] <= input_data[key] <= value[1]:
                            degrees.append(1)
                        else:
                            degrees.append(activity_degrees.get("low", 0) if input_data[key] < value[0] else activity_degrees.get("high", 0))
                    else:
                        degrees.append(activity_degrees.get(value, 0))
                elif key == "AlcoholIntake":
                    alcohol_degrees = fuzzify_alcohol_intake(input_data[key])
                    if isinstance(value, tuple) and len(value) == 2:
                        if value[0] <= input_data[key] <= value[1]:
                            degrees.append(1)
                        else:
                            degrees.append(alcohol_degrees.get("low", 0) if input_data[key] < value[0] else alcohol_degrees.get("high", 0))
                    else:
                        degrees.append(alcohol_degrees.get(value, 0))
                elif isinstance(value, tuple) and len(value) == 2:
                    if value[0] <= input_data[key] <= value[1]:
                        degrees.append(1)
                    else:
                        degrees.append(0)
                else:
                    if input_data[key] == value:
                        degrees.append(1)
                    else:
                        degrees.append(0)
            else:
                degrees.append(0)
        if not degrees:
            return 0
        return np.prod(degrees)


# Explanation Facility
class ExplanationFacility:
    def explain(self, input_data: Dict[str, Any], rule: Dict[str, Any]) -> str:
        explanation = f"The system inferred that the patient has {rule['conclusion']} based on the following conditions:\n"
        for key, value in rule["conditions"].items():
            explanation += f" - {key}: {input_data[key]} matched {value}\n"
        return explanation


# Knowledge Acquisition Module
class KnowledgeAcquisition:
    def acquire(self, knowledge_base: KnowledgeBase):
        # Example rule acquisition (this would be more sophisticated in a real system)
        rules = [
            {
                "conditions": {
                    "Age": "middle-aged",
                    "Smoking": 1,
                    "GeneticRisk": 2,
                    "BMI": "obese",
                    "PhysicalActivity": (0, 10),
                    "AlcoholIntake": (0, 5),
                    "CancerHistory": 0,
                },
                "conclusion": "Cancer",
            },
            {
                "conditions": {
                    "Age": "young",
                    "Smoking": 0,
                    "GeneticRisk": 1,
                    "BMI": "normal",
                    "PhysicalActivity": (5, 10),
                    "AlcoholIntake": (0, 2),
                    "CancerHistory": 1,
                },
                "conclusion": "No Cancer",
            },
            {
                "conditions": {
                    "Age": "old",
                    "Smoking": 1,
                    "GeneticRisk": 2,
                    "BMI": "obese",
                    "PhysicalActivity": (0, 3),
                    "AlcoholIntake": (4, 5),
                    "CancerHistory": 1,
                },
                "conclusion": "Cancer",
            },
            {
                "conditions": {
                    "Age": "middle-aged",
                    "Smoking": 0,
                    "GeneticRisk": 0,
                    "BMI": "normal",
                    "PhysicalActivity": (7, 10),
                    "AlcoholIntake": (0, 2),
                    "CancerHistory": 0,
                },
                "conclusion": "No Cancer",
            },
            {
                "conditions": {
                    "Age": "old",
                    "Smoking": 1,
                    "GeneticRisk": 1,
                    "BMI": "overweight",
                    "PhysicalActivity": (3, 7),
                    "AlcoholIntake": (2, 4),
                    "CancerHistory": 1,
                },
                "conclusion": "Cancer",
            },
            {
                "conditions": {
                    "Age": "young",
                    "Smoking": 0,
                    "GeneticRisk": 0,
                    "BMI": "underweight",
                    "PhysicalActivity": (8, 10),
                    "AlcoholIntake": (0, 1),
                    "CancerHistory": 0,
                },
                "conclusion": "No Cancer",
            },
            {
                "conditions": {
                    "Age": "middle-aged",
                    "Smoking": 1,
                    "GeneticRisk": 2,
                    "BMI": "overweight",
                    "PhysicalActivity": (0, 5),
                    "AlcoholIntake": (3, 5),
                    "CancerHistory": 1,
                },
                "conclusion": "Cancer",
            },
            # Add more rules as needed
        ]
        for rule in rules:
            knowledge_base.add_rule(rule)

    def add_rule(
        self, knowledge_base: KnowledgeBase, conditions: Dict[str, Any], conclusion: str
    ):
        rule = {"conditions": conditions, "conclusion": conclusion}
        knowledge_base.add_rule(rule)


# User Interface (simplified)
def user_interface():
    input_data = {
        "Age": 60,
        "Gender": 1,
        "BMI": 40,
        "Smoking": 1,
        "GeneticRisk": 1,
        "PhysicalActivity": 0,
        "AlcoholIntake": 9,
        "CancerHistory": 1,
    }
    return input_data


# Main System
knowledge_base = KnowledgeBase()
knowledge_acquisition = KnowledgeAcquisition()

# Add rules statically
knowledge_acquisition.acquire(knowledge_base)

# Add a new rule dynamically
new_conditions = {
    "Age": "middle-aged",
    "Smoking": 1,
    "GeneticRisk": 1,
    "BMI": "overweight",
    "PhysicalActivity": (0, 5),
    "AlcoholIntake": (3, 5),
    "CancerHistory": 0,
}
new_conclusion = "Possible Cancer"
knowledge_acquisition.add_rule(knowledge_base, new_conditions, new_conclusion)

inference_engine = InferenceEngine(knowledge_base)
explanation_facility = ExplanationFacility()

input_data = user_interface()
diagnosis = inference_engine.infer(input_data)

print("Diagnosis:", diagnosis)

for rule in knowledge_base.rules:
    degree = inference_engine.match_rule(input_data, rule["conditions"])
    if degree > 0:
        explanation = explanation_facility.explain(input_data, rule)
        print(explanation)

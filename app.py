# # Knowledge Base (Simulated with dictionaries for simplicity)
# nutritional_info = {
#     "vegetarian": {
#         "low_calorie": ["Salad", "Smoothie"],
#         "high_protein": ["Tofu", "Lentils"]
#     },
#     "non_vegetarian": {
#         "low_calorie": ["Grilled Chicken", "Fish"],
#         "high_protein": ["Chicken Breast", "Eggs"]
#     }
# }

# exercise_routines = {
#     "beginner": ["Walking", "Yoga"],
#     "intermediate": ["Jogging", "Cycling"],
#     "advanced": ["Running", "Weightlifting"]
# }

# mental_wellness_techniques = {
#     "stress_reduction": ["Meditation", "Deep Breathing"],
#     "focus_improvement": ["Mindfulness", "Puzzles"]
# }


# # import numpy as np
# # import skfuzzy as fuzz
# # from skfuzzy import control as ctrl

# # # Define fuzzy variables
# # age = ctrl.Antecedent(np.arange(0, 101, 1), 'age')
# # bmi = ctrl.Antecedent(np.arange(0, 51, 1), 'bmi')
# # stress_level = ctrl.Antecedent(np.arange(0, 11, 1), 'stress_level')
# # focus_level = ctrl.Antecedent(np.arange(0, 11, 1), 'focus_level')

# # nutrition_advice = ctrl.Consequent(np.arange(0, 11, 1), 'nutrition_advice')
# # exercise_advice = ctrl.Consequent(np.arange(0, 11, 1), 'exercise_advice')
# # mental_wellness_advice = ctrl.Consequent(np.arange(0, 11, 1), 'mental_wellness_advice')

# # # Define membership functions
# # age.automf(3)
# # bmi['low'] = fuzz.trimf(bmi.universe, [0, 10, 20])
# # bmi['medium'] = fuzz.trimf(bmi.universe, [15, 25, 35])
# # bmi['high'] = fuzz.trimf(bmi.universe, [30, 40, 50])

# # stress_level.automf(3)
# # focus_level.automf(3)

# # nutrition_advice.automf(3)
# # exercise_advice.automf(3)
# # mental_wellness_advice.automf(3)

# # # Define fuzzy rules
# # rule1 = ctrl.Rule(age['poor'] & bmi['high'], nutrition_advice['poor'])
# # rule2 = ctrl.Rule(age['average'] & bmi['medium'], nutrition_advice['average'])
# # rule3 = ctrl.Rule(age['good'] & bmi['low'], nutrition_advice['good'])

# # rule4 = ctrl.Rule(stress_level['poor'], exercise_advice['poor'])
# # rule5 = ctrl.Rule(stress_level['average'], exercise_advice['average'])
# # rule6 = ctrl.Rule(stress_level['good'], exercise_advice['good'])

# # rule7 = ctrl.Rule(stress_level['poor'], mental_wellness_advice['good'])
# # rule8 = ctrl.Rule(stress_level['average'], mental_wellness_advice['average'])
# # rule9 = ctrl.Rule(stress_level['good'], mental_wellness_advice['poor'])

# # rule10 = ctrl.Rule(focus_level['poor'], mental_wellness_advice['good'])
# # rule11 = ctrl.Rule(focus_level['average'], mental_wellness_advice['average'])
# # rule12 = ctrl.Rule(focus_level['good'], mental_wellness_advice['poor'])

# # # Create control systems
# # nutrition_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
# # exercise_ctrl = ctrl.ControlSystem([rule4, rule5, rule6])
# # mental_wellness_ctrl = ctrl.ControlSystem([rule7, rule8, rule9, rule10, rule11, rule12])

# # nutrition = ctrl.ControlSystemSimulation(nutrition_ctrl)
# # exercise = ctrl.ControlSystemSimulation(exercise_ctrl)
# # mental_wellness = ctrl.ControlSystemSimulation(mental_wellness_ctrl)




# # def get_nutritional_advice(user_profile):
# #     dietary_preferences = user_profile['dietary_preferences']
# #     goal = user_profile['goal']
    
# #     # Example fuzzy inputs
# #     nutrition.input['age'] = user_profile['age']
# #     nutrition.input['bmi'] = user_profile['bmi']
# #     nutrition.compute()
    
# #     advice_level = nutrition.output['nutrition_advice']
    
# #     if advice_level > 7:
# #         if goal == 'weight loss':
# #             return nutritional_info[dietary_preferences]['low_calorie']
# #         elif goal == 'muscle gain':
# #             return nutritional_info[dietary_preferences]['high_protein']
# #     elif advice_level > 4:
# #         return nutritional_info[dietary_preferences]['high_protein'] if goal == 'muscle_gain' else nutritional_info[dietary_preferences]['low_calorie']
# #     else:
# #         return nutritional_info[dietary_preferences]['low_calorie']

# # def get_exercise_routine(user_profile):
# #     fitness_level = user_profile['fitness_level']
    
# #     exercise.input['stress_level'] = user_profile['stress_level']
# #     exercise.compute()
    
# #     advice_level = exercise.output['exercise_advice']
    
# #     if advice_level > 7:
# #         return exercise_routines[fitness_level]
# #     elif advice_level > 4:
# #         return exercise_routines['intermediate']
# #     else:
# #         return exercise_routines['beginner']

# # def get_mental_wellness_tips(user_profile):
# #     mental_wellness.input['stress_level'] = user_profile['stress_level']
# #     mental_wellness.input['focus_level'] = user_profile['focus_level']
# #     mental_wellness.compute()
    
# #     advice_level = mental_wellness.output['mental_wellness_advice']
    
# #     if advice_level > 7:
# #         return mental_wellness_techniques['stress_reduction']
# #     elif advice_level > 4:
# #         return mental_wellness_techniques['focus_improvement']
# #     else:
# #         return mental_wellness_techniques['stress_reduction']

# # def generate_wellness_plan(user_profile):
# #     nutrition = get_nutritional_advice(user_profile)
# #     exercise = get_exercise_routine(user_profile)
# #     mental_wellness = get_mental_wellness_tips(user_profile)
# #     return {
# #         'nutrition': nutrition,
# #         'exercise': exercise,
# #         'mental_wellness': mental_wellness
# #     }

# # # Example user profile
# # user_profile = {
# #     'age': 30,
# #     'weight': 70,
# #     'height': 170,
# #     'bmi': 24.2,  # BMI calculated as weight (kg) / (height (m)^2)
# #     'goal': 'weight loss',
# #     'dietary_preferences': 'vegetarian',
# #     'fitness_level': 'beginner',
# #     'stress_level': 8,
# #     'focus_level': 5
# # }

# # # Generate personalized wellness plan
# # wellness_plan = generate_wellness_plan(user_profile)
# # print(wellness_plan)
#                             # from flask import Flask, request, jsonify
#                             # import numpy as np
#                             # import skfuzzy as fuzz
#                             # from skfuzzy import control as ctrl

#                             # app = Flask(__name__)

#                             # # Define fuzzy variables
#                             # age = ctrl.Antecedent(np.arange(0, 101, 1), 'age')
#                             # bmi = ctrl.Antecedent(np.arange(0, 51, 1), 'bmi')
#                             # stress_level = ctrl.Antecedent(np.arange(0, 11, 1), 'stress_level')
#                             # focus_level = ctrl.Antecedent(np.arange(0, 11, 1), 'focus_level')

#                             # nutrition_advice = ctrl.Consequent(np.arange(0, 11, 1), 'nutrition_advice')
#                             # exercise_advice = ctrl.Consequent(np.arange(0, 11, 1), 'exercise_advice')
#                             # mental_wellness_advice = ctrl.Consequent(np.arange(0, 11, 1), 'mental_wellness_advice')

#                             # # Define membership functions
#                             # age.automf(3)
#                             # bmi['low'] = fuzz.trimf(bmi.universe, [0, 10, 20])
#                             # bmi['medium'] = fuzz.trimf(bmi.universe, [15, 25, 35])
#                             # bmi['high'] = fuzz.trimf(bmi.universe, [30, 40, 50])

#                             # stress_level.automf(3)
#                             # focus_level.automf(3)

#                             # nutrition_advice.automf(3)
#                             # exercise_advice.automf(3)
#                             # mental_wellness_advice.automf(3)

#                             # # Define fuzzy rules
#                             # rule1 = ctrl.Rule(age['poor'] & bmi['high'], nutrition_advice['poor'])
#                             # rule2 = ctrl.Rule(age['average'] & bmi['medium'], nutrition_advice['average'])
#                             # rule3 = ctrl.Rule(age['good'] & bmi['low'], nutrition_advice['good'])

#                             # rule4 = ctrl.Rule(stress_level['poor'], exercise_advice['poor'])
#                             # rule5 = ctrl.Rule(stress_level['average'], exercise_advice['average'])
#                             # rule6 = ctrl.Rule(stress_level['good'], exercise_advice['good'])

#                             # rule7 = ctrl.Rule(stress_level['poor'], mental_wellness_advice['good'])
#                             # rule8 = ctrl.Rule(stress_level['average'], mental_wellness_advice['average'])
#                             # rule9 = ctrl.Rule(stress_level['good'], mental_wellness_advice['poor'])

#                             # rule10 = ctrl.Rule(focus_level['poor'], mental_wellness_advice['good'])
#                             # rule11 = ctrl.Rule(focus_level['average'], mental_wellness_advice['average'])
#                             # rule12 = ctrl.Rule(focus_level['good'], mental_wellness_advice['poor'])

#                             # # Create control systems
#                             # nutrition_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
#                             # exercise_ctrl = ctrl.ControlSystem([rule4, rule5, rule6])
#                             # mental_wellness_ctrl = ctrl.ControlSystem([rule7, rule8, rule9, rule10, rule11, rule12])

#                             # nutrition = ctrl.ControlSystemSimulation(nutrition_ctrl)
#                             # exercise = ctrl.ControlSystemSimulation(exercise_ctrl)
#                             # mental_wellness = ctrl.ControlSystemSimulation(mental_wellness_ctrl)

#                             # # Knowledge Base
#                             # nutritional_info = {
#                             #     "vegetarian": {
#                             #         "low_calorie": ["Salad", "Smoothie"],
#                             #         "high_protein": ["Tofu", "Lentils"]
#                             #     },
#                             #     "non_vegetarian": {
#                             #         "low_calorie": ["Grilled Chicken", "Fish"],
#                             #         "high_protein": ["Chicken Breast", "Eggs"]
#                             #     }
#                             # }

#                             # exercise_routines = {
#                             #     "beginner": ["Walking", "Yoga"],
#                             #     "intermediate": ["Jogging", "Cycling"],
#                             #     "advanced": ["Running", "Weightlifting"]
#                             # }

#                             # mental_wellness_techniques = {
#                             #     "stress_reduction": ["Meditation", "Deep Breathing"],
#                             #     "focus_improvement": ["Mindfulness", "Puzzles"]
#                             # }

#                             # def get_nutritional_advice(user_profile):
#                             #     dietary_preferences = user_profile['dietary_preferences']
#                             #     goal = user_profile['goal']
                                
#                             #     nutrition.input['age'] = user_profile['age']
#                             #     nutrition.input['bmi'] = user_profile['bmi']
#                             #     nutrition.compute()
                                
#                             #     advice_level = nutrition.output['nutrition_advice']
                                
#                             #     if advice_level > 7:
#                             #         if goal == 'weight loss':
#                             #             return nutritional_info[dietary_preferences]['low_calorie']
#                             #         elif goal == 'muscle gain':
#                             #             return nutritional_info[dietary_preferences]['high_protein']
#                             #     elif advice_level > 4:
#                             #         return nutritional_info[dietary_preferences]['high_protein'] if goal == 'muscle_gain' else nutritional_info[dietary_preferences]['low_calorie']
#                             #     else:
#                             #         return nutritional_info[dietary_preferences]['low_calorie']

#                             # def get_exercise_routine(user_profile):
#                             #     fitness_level = user_profile['fitness_level']
                                
#                             #     exercise.input['stress_level'] = user_profile['stress_level']
#                             #     exercise.compute()
                                
#                             #     advice_level = exercise.output['exercise_advice']
                                
#                             #     if advice_level > 7:
#                             #         return exercise_routines[fitness_level]
#                             #     elif advice_level > 4:
#                             #         return exercise_routines['intermediate']
#                             #     else:
#                             #         return exercise_routines['beginner']

#                             # def get_mental_wellness_tips(user_profile):
#                             #     mental_wellness.input['stress_level'] = user_profile['stress_level']
#                             #     mental_wellness.input['focus_level'] = user_profile['focus_level']
#                             #     mental_wellness.compute()
                                
#                             #     advice_level = mental_wellness.output['mental_wellness_advice']
                                
#                             #     if advice_level > 7:
#                             #         return mental_wellness_techniques['stress_reduction']
#                             #     elif advice_level > 4:
#                             #         return mental_wellness_techniques['focus_improvement']
#                             #     else:
#                             #         return mental_wellness_techniques['stress_reduction']

#                             # def generate_wellness_plan(user_profile):
#                             #     nutrition = get_nutritional_advice(user_profile)
#                             #     exercise = get_exercise_routine(user_profile)
#                             #     mental_wellness = get_mental_wellness_tips(user_profile)
#                             #     return {
#                             #         'nutrition': nutrition,
#                             #         'exercise': exercise,
#                             #         'mental_wellness': mental_wellness
#                             #     }

#                             # @app.route('/get_wellness_plan', methods=['POST'])
#                             # def get_wellness_plan():
#                             #     user_profile = request.json
#                             #     wellness_plan = generate_wellness_plan(user_profile)
#                             #     return jsonify(wellness_plan)

#                             # if __name__ == '__main__':
#                             #     app.run(debug=True)


# from flask import Flask, request, jsonify, render_template
# import numpy as np
# import skfuzzy as fuzz
# from skfuzzy import control as ctrl

# app = Flask(__name__)

# # Define fuzzy variables
# age = ctrl.Antecedent(np.arange(0, 101, 1), 'age')
# bmi = ctrl.Antecedent(np.arange(0, 51, 1), 'bmi')
# stress_level = ctrl.Antecedent(np.arange(0, 11, 1), 'stress_level')
# focus_level = ctrl.Antecedent(np.arange(0, 11, 1), 'focus_level')

# nutrition_advice = ctrl.Consequent(np.arange(0, 11, 1), 'nutrition_advice')
# exercise_advice = ctrl.Consequent(np.arange(0, 11, 1), 'exercise_advice')
# mental_wellness_advice = ctrl.Consequent(np.arange(0, 11, 1), 'mental_wellness_advice')

# # Define membership functions
# age.automf(3)
# bmi['low'] = fuzz.trimf(bmi.universe, [0, 10, 20])
# bmi['medium'] = fuzz.trimf(bmi.universe, [15, 25, 35])
# bmi['high'] = fuzz.trimf(bmi.universe, [30, 40, 50])

# stress_level.automf(3)
# focus_level.automf(3)

# nutrition_advice.automf(3)
# exercise_advice.automf(3)
# mental_wellness_advice.automf(3)

# # Define fuzzy rules
# rule1 = ctrl.Rule(age['poor'] & bmi['high'], nutrition_advice['poor'])
# rule2 = ctrl.Rule(age['average'] & bmi['medium'], nutrition_advice['average'])
# rule3 = ctrl.Rule(age['good'] & bmi['low'], nutrition_advice['good'])

# rule4 = ctrl.Rule(stress_level['poor'], exercise_advice['poor'])
# rule5 = ctrl.Rule(stress_level['average'], exercise_advice['average'])
# rule6 = ctrl.Rule(stress_level['good'], exercise_advice['good'])

# rule7 = ctrl.Rule(stress_level['poor'], mental_wellness_advice['good'])
# rule8 = ctrl.Rule(stress_level['average'], mental_wellness_advice['average'])
# rule9 = ctrl.Rule(stress_level['good'], mental_wellness_advice['poor'])

# rule10 = ctrl.Rule(focus_level['poor'], mental_wellness_advice['good'])
# rule11 = ctrl.Rule(focus_level['average'], mental_wellness_advice['average'])
# rule12 = ctrl.Rule(focus_level['good'], mental_wellness_advice['poor'])

# # Create control systems
# nutrition_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
# exercise_ctrl = ctrl.ControlSystem([rule4, rule5, rule6])
# mental_wellness_ctrl = ctrl.ControlSystem([rule7, rule8, rule9, rule10, rule11, rule12])

# nutrition = ctrl.ControlSystemSimulation(nutrition_ctrl)
# exercise = ctrl.ControlSystemSimulation(exercise_ctrl)
# mental_wellness = ctrl.ControlSystemSimulation(mental_wellness_ctrl)

# # Knowledge Base
# nutritional_info = {
#     "vegetarian": {
#         "low_calorie": ["Salad", "Smoothie"],
#         "high_protein": ["Tofu", "Lentils"]
#     },
#     "non_vegetarian": {
#         "low_calorie": ["Grilled Chicken", "Fish"],
#         "high_protein": ["Chicken Breast", "Eggs"]
#     }
# }

# exercise_routines = {
#     "beginner": ["Walking", "Yoga"],
#     "intermediate": ["Jogging", "Cycling"],
#     "advanced": ["Running", "Weightlifting"]
# }

# mental_wellness_techniques = {
#     "stress_reduction": ["Meditation", "Deep Breathing"],
#     "focus_improvement": ["Mindfulness", "Puzzles"]
# }

# def get_nutritional_advice(user_profile):
#     dietary_preferences = user_profile['dietary_preferences']
#     goal = user_profile['goal']
    
#     nutrition.input['age'] = user_profile['age']
#     nutrition.input['bmi'] = user_profile['bmi']
#     nutrition.compute()
    
#     advice_level = nutrition.output['nutrition_advice']
    
#     if advice_level > 7:
#         if goal == 'weight loss':
#             return nutritional_info[dietary_preferences]['low_calorie']
#         elif goal == 'muscle gain':
#             return nutritional_info[dietary_preferences]['high_protein']
#     elif advice_level > 4:
#         return nutritional_info[dietary_preferences]['high_protein'] if goal == 'muscle_gain' else nutritional_info[dietary_preferences]['low_calorie']
#     else:
#         return nutritional_info[dietary_preferences]['low_calorie']

# def get_exercise_routine(user_profile):
#     fitness_level = user_profile['fitness_level']
    
#     exercise.input['stress_level'] = user_profile['stress_level']
#     exercise.compute()
    
#     advice_level = exercise.output['exercise_advice']
    
#     if advice_level > 7:
#         return exercise_routines[fitness_level]
#     elif advice_level > 4:
#         return exercise_routines['intermediate']
#     else:
#         return exercise_routines['beginner']

# def get_mental_wellness_tips(user_profile):
#     mental_wellness.input['stress_level'] = user_profile['stress_level']
#     mental_wellness.input['focus_level'] = user_profile['focus_level']
#     mental_wellness.compute()
    
#     advice_level = mental_wellness.output['mental_wellness_advice']
    
#     if advice_level > 7:
#         return mental_wellness_techniques['stress_reduction']
#     elif advice_level > 4:
#         return mental_wellness_techniques['focus_improvement']
#     else:
#         return mental_wellness_techniques['stress_reduction']

# def generate_wellness_plan(user_profile):
#     nutrition = get_nutritional_advice(user_profile)
#     exercise = get_exercise_routine(user_profile)
#     mental_wellness = get_mental_wellness_tips(user_profile)
#     return {
#         'nutrition': nutrition,
#         'exercise': exercise,
#         'mental_wellness': mental_wellness
#     }

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/get_wellness_plan', methods=['POST'])
# def get_wellness_plan():
#     user_profile = request.json
#     wellness_plan = generate_wellness_plan(user_profile)
#     return jsonify(wellness_plan)

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, request, jsonify, render_template
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

app = Flask(__name__)

# Define fuzzy variables
age = ctrl.Antecedent(np.arange(0, 101, 1), 'age')
bmi = ctrl.Antecedent(np.arange(0, 51, 1), 'bmi')
stress_level = ctrl.Antecedent(np.arange(0, 11, 1), 'stress_level')
focus_level = ctrl.Antecedent(np.arange(0, 11, 1), 'focus_level')

nutrition_advice = ctrl.Consequent(np.arange(0, 11, 1), 'nutrition_advice')
exercise_advice = ctrl.Consequent(np.arange(0, 11, 1), 'exercise_advice')
mental_wellness_advice = ctrl.Consequent(np.arange(0, 11, 1), 'mental_wellness_advice')

# Define membership functions
age.automf(3)
bmi['low'] = fuzz.trimf(bmi.universe, [0, 10, 20])
bmi['medium'] = fuzz.trimf(bmi.universe, [15, 25, 35])
bmi['high'] = fuzz.trimf(bmi.universe, [30, 40, 50])

stress_level.automf(3)
focus_level.automf(3)

nutrition_advice.automf(3)
exercise_advice.automf(3)
mental_wellness_advice.automf(3)

# Define fuzzy rules
rule1 = ctrl.Rule(age['poor'] & bmi['high'], nutrition_advice['poor'])
rule2 = ctrl.Rule(age['average'] & bmi['medium'], nutrition_advice['average'])
rule3 = ctrl.Rule(age['good'] & bmi['low'], nutrition_advice['good'])

rule4 = ctrl.Rule(stress_level['poor'], exercise_advice['poor'])
rule5 = ctrl.Rule(stress_level['average'], exercise_advice['average'])
rule6 = ctrl.Rule(stress_level['good'], exercise_advice['good'])

rule7 = ctrl.Rule(stress_level['poor'] & focus_level['poor'], mental_wellness_advice['good'])
rule8 = ctrl.Rule(stress_level['average'] & focus_level['average'], mental_wellness_advice['average'])
rule9 = ctrl.Rule(stress_level['good'] & focus_level['good'], mental_wellness_advice['poor'])

# Add additional rules to ensure coverage
rule10 = ctrl.Rule(stress_level['poor'] & focus_level['average'], mental_wellness_advice['good'])
rule11 = ctrl.Rule(stress_level['poor'] & focus_level['good'], mental_wellness_advice['good'])
rule12 = ctrl.Rule(stress_level['average'] & focus_level['poor'], mental_wellness_advice['average'])
rule13 = ctrl.Rule(stress_level['average'] & focus_level['good'], mental_wellness_advice['average'])
rule14 = ctrl.Rule(stress_level['good'] & focus_level['poor'], mental_wellness_advice['poor'])
rule15 = ctrl.Rule(stress_level['good'] & focus_level['average'], mental_wellness_advice['poor'])

# Create control systems
nutrition_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
exercise_ctrl = ctrl.ControlSystem([rule4, rule5, rule6])
mental_wellness_ctrl = ctrl.ControlSystem([rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15])

nutrition = ctrl.ControlSystemSimulation(nutrition_ctrl)
exercise = ctrl.ControlSystemSimulation(exercise_ctrl)
mental_wellness = ctrl.ControlSystemSimulation(mental_wellness_ctrl)

# Knowledge Base
nutritional_info = {
    "vegetarian": {
        "low_calorie": ["Salad", "Smoothie"],
        "high_protein": ["Tofu", "Lentils"]
    },
    "non_vegetarian": {
        "low_calorie": ["Grilled Chicken", "Fish"],
        "high_protein": ["Chicken Breast", "Eggs"]
    }
}

exercise_routines = {
    "beginner": ["Walking", "Yoga"],
    "intermediate": ["Jogging", "Cycling"],
    "advanced": ["Running", "Weightlifting"]
}

mental_wellness_techniques = {
    "stress_reduction": ["Meditation", "Deep Breathing"],
    "focus_improvement": ["Mindfulness", "Puzzles"]
}

def get_nutritional_advice(user_profile):
    dietary_preferences = user_profile['dietary_preferences']
    goal = user_profile['goal']
    
    nutrition.input['age'] = user_profile['age']
    nutrition.input['bmi'] = user_profile['bmi']
    nutrition.compute()
    
    advice_level = nutrition.output['nutrition_advice']
    
    if advice_level > 7:
        if goal == 'weight loss':
            return nutritional_info[dietary_preferences]['low_calorie']
        elif goal == 'muscle gain':
            return nutritional_info[dietary_preferences]['high_protein']
    elif advice_level > 4:
        return nutritional_info[dietary_preferences]['high_protein'] if goal == 'muscle_gain' else nutritional_info[dietary_preferences]['low_calorie']
    else:
        return nutritional_info[dietary_preferences]['low_calorie']

def get_exercise_routine(user_profile):
    fitness_level = user_profile['fitness_level']
    
    exercise.input['stress_level'] = user_profile['stress_level']
    exercise.compute()
    
    advice_level = exercise.output['exercise_advice']
    
    if advice_level > 7:
        return exercise_routines[fitness_level]
    elif advice_level > 4:
        return exercise_routines['intermediate']
    else:
        return exercise_routines['beginner']

def get_mental_wellness_tips(user_profile):
    mental_wellness.input['stress_level'] = user_profile['stress_level']
    mental_wellness.input['focus_level'] = user_profile['focus_level']
    mental_wellness.compute()
    
    advice_level = mental_wellness.output['mental_wellness_advice']
    
    if advice_level > 7:
        return mental_wellness_techniques['stress_reduction']
    elif advice_level > 4:
        return mental_wellness_techniques['focus_improvement']
    else:
        return mental_wellness_techniques['stress_reduction']

def generate_wellness_plan(user_profile):
    nutrition = get_nutritional_advice(user_profile)
    exercise = get_exercise_routine(user_profile)
    mental_wellness = get_mental_wellness_tips(user_profile)
    return {
        'nutrition': nutrition,
        'exercise': exercise,
        'mental_wellness': mental_wellness
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_wellness_plan', methods=['POST'])
def get_wellness_plan():
    user_profile = request.json
    wellness_plan = generate_wellness_plan(user_profile)
    return jsonify(wellness_plan)

if __name__ == '__main__':
    app.run(debug=True)

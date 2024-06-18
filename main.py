from flask import Flask, request, jsonify, render_template
from rules import WellnessRules

app = Flask(__name__)

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
    
    # Create a new instance of the rules engine
    engine = WellnessRules()
    
    # Reset the engine
    engine.reset()
    
    # Declare facts
    engine.declare(Fact(age=user_profile['age']),
                   Fact(bmi=user_profile['bmi']))
    
    # Run the engine
    engine.run()
    
    # Get the nutrition advice
    nutrition_advice = engine.facts.get('nutrition_advice')
    
    if nutrition_advice == "good":
        if goal == 'weight loss':
            return nutritional_info[dietary_preferences]['low_calorie']
        elif goal == 'muscle gain':
            return nutritional_info[dietary_preferences]['high_protein']
    elif nutrition_advice == "average":
        return nutritional_info[dietary_preferences]['high_protein'] if goal == 'muscle_gain' else nutritional_info[dietary_preferences]['low_calorie']
    else:
        return nutritional_info[dietary_preferences]['low_calorie']

def get_exercise_routine(user_profile):
    fitness_level = user_profile['fitness_level']
    
    # Create a new instance of the rules engine
    engine = WellnessRules()
    
    # Reset the engine
    engine.reset()
    
    # Declare facts
    engine.declare(Fact(stress_level=user_profile['stress_level']))
    
    # Run the engine
    engine.run()
    
    # Get the exercise advice
    exercise_advice = engine.facts.get('exercise_advice')
    
    if exercise_advice == "good":
        return exercise_routines[fitness_level]
    elif exercise_advice == "average":
        return exercise_routines['intermediate']
    else:
        return exercise_routines['beginner']

def get_mental_wellness_tips(user_profile):
    # Create a new instance of the rules engine
    engine = WellnessRules()
    
    # Reset the engine
    engine.reset()
    
    # Declare facts
    engine.declare(Fact(stress_level=user_profile['stress_level']),
                   Fact(focus_level=user_profile['focus_level']))
    
    # Run the engine
    engine.run()
    
    # Get the mental wellness advice
    mental_wellness_advice = engine.facts.get('mental_wellness_advice')
    
    if mental_wellness_advice == "good":
        return mental_wellness_techniques['stress_reduction']
    elif mental_wellness_advice == "average":
        return mental_wellness_techniques['focus_improvement']
    else:
        return mental_wellness_techniques['stress_reduction']
    
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
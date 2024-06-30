import sqlite3
from pyke/pyke import knowledge_engine, krb_traceback

class SriLankaTourismExpertSystem:
    def __init__(self, db_path='sri_lanka_attractions.db'):
        self.db_path = db_path
        self.engine = knowledge_engine.engine(__file__)

    def load_attractions(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name, description, province, type, image_url, budget FROM attractions")
        attractions = cursor.fetchall()
        conn.close()

        with open('tourism_facts.kfb', 'w') as f:
            for attraction in attractions:
                name, description, province, interest, image_url, budget = attraction
                f.write(f"attraction({name!r}, {description!r}, {province!r}, {interest!r}, {image_url!r}, {budget!r})\n")

    def get_recommendations(self, budget, interest, province):
        self.load_attractions()
        self.engine.reset()
        self.engine.activate('tourism_rules')

        fact_budget = budget.lower()
        fact_interest = interest.lower()
        fact_province = province if province != 'Any' else None

        self.engine.assert_('tourism_facts', 'user_preference',
                            (fact_budget, fact_interest, fact_province))

        recommendations = []
        try:
            with self.engine.prove_goal('tourism_rules.recommend_attraction($name, $description, $province, $interest, $image_url, $budget, $cf)') as gen:
                for vars, plan in gen:
                    recommendations.append((
                        vars['name'], vars['description'], vars['province'],
                        vars['interest'], vars['image_url'], vars['budget'],
                        vars['cf']
                    ))
        except Exception:
            krb_traceback.print_exc()

        recommendations.sort(key=lambda x: x[6], reverse=True)
        return recommendations[:5]  # Return top 5 recommendations

    def get_explanation(self, user_prefs, attraction):
        budget, interest, province = user_prefs
        name, description, attr_province, attr_type, image_url, attr_budget, cf = attraction

        explanation = f"Recommendation: {name}\n"
        explanation += f"Certainty Factor: {cf:.2f}\n\n"
        explanation += "Factors considered:\n"

        # Budget explanation
        budget_match = "perfectly" if budget == attr_budget else "reasonably well" if abs(ord(budget[0]) - ord(attr_budget[0])) == 1 else "not very well"
        explanation += f"1. Budget: Your {budget} budget matches {budget_match} with the attraction's {attr_budget} budget.\n"

        # Interest explanation
        explanation += f"2. Interest: This attraction matches your interest in {interest} activities.\n"

        # Province explanation
        if province == 'Any':
            explanation += f"3. Province: You didn't specify a preferred province, so all provinces were considered.\n"
        elif province == attr_province:
            explanation += f"3. Province: This attraction is in your preferred province of {province}.\n"
        else:
            explanation += f"3. Province: Although this isn't in your preferred province of {province}, it's a strong match in other areas.\n"

        return explanation

# Flask app setup (similar to the original code)
# ...

if __name__ == '__main__':
    expert_system = SriLankaTourismExpertSystem()
    app.run(debug=True)
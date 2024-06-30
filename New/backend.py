from flask import Flask, render_template, request, send_file
import sqlite3
import graphviz

app = Flask(__name__)

class SriLankaTourismExpertSystem:
    def __init__(self, db_path='sri_lanka_attractions.db'):
        self.db_path = db_path

    def get_recommendations(self, budget, interest, province):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        query = '''
        SELECT name, description, province, type, image_url, budget
        FROM attractions
        WHERE type = ?
        '''
        params = [interest]

        if province != 'Any':
            query += ' AND province = ?'
            params.append(province)

        cursor.execute(query, params)
        attractions = cursor.fetchall()
        conn.close()

        recommendations = []
        print(recommendations)
        for attraction in attractions:
            cf = self.calculate_certainty_factor(budget, interest, province, attraction)
            if cf > 0:
                recommendations.append(attraction + (cf,))

        recommendations.sort(key=lambda x: x[6], reverse=True)
        return recommendations[:5]  # Return top 5 recommendations

    def calculate_certainty_factor(self, user_budget, user_interest, user_province, attraction):
        name, description, province, interest, image_url, budget = attraction
        cf = 1.0  # Start with full certainty

        # Budget factor
        budget_factor = {
            ('Low', 'Low'): 1.0,
            ('Low', 'Medium'): 0.7,
            ('Low', 'High'): 0.3,
            ('Medium', 'Low'): 0.8,
            ('Medium', 'Medium'): 1.0,
            ('Medium', 'High'): 0.8,
            ('High', 'Low'): 0.5,
            ('High', 'Medium'): 0.9,
            ('High', 'High'): 1.0
        }
        cf *= budget_factor.get((user_budget, budget), 0.5)

        # Interest factor (already filtered in SQL query)
        cf *= 1.0 
        # cf = cf * 1.0

        # Province factor
        if user_province != 'Any' and province != user_province:
            cf *= 0.7  # Reduce certainty if not in preferred province

        return cf

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
    
    # def generate_decision_tree(self):
    #     dot = graphviz.Digraph(comment='Sri Lanka Tourism Expert System')
    #     dot.attr(rankdir='TB', size='8,8')

    #     # Root
    #     dot.node('A', 'User Preferences')

    #     # Budget
    #     dot.node('B', 'Budget')
    #     dot.edge('A', 'B')
    #     dot.node('B1', 'Low')
    #     dot.node('B2', 'Medium')
    #     dot.node('B3', 'High')
    #     dot.edge('B', 'B1')
    #     dot.edge('B', 'B2')
    #     dot.edge('B', 'B3')

    #     # Interest
    #     dot.node('C', 'Interest')
    #     dot.edge('A', 'C')
    #     dot.node('C1', 'Culture')
    #     dot.node('C2', 'Nature')
    #     dot.node('C3', 'Adventure')
    #     dot.edge('C', 'C1')
    #     dot.edge('C', 'C2')
    #     dot.edge('C', 'C3')

    #     # Province
    #     dot.node('D', 'Province')
    #     dot.edge('A', 'D')
    #     provinces = ['Central', 'Eastern', 'North Central', 'Northern', 'North Western', 
    #                     'Sabaragamuwa', 'Southern', 'Uva', 'Western']
    #     for i, province in enumerate(provinces):
    #         dot.node(f'D{i+1}', province)
    #         dot.edge('D', f'D{i+1}')

    #     # Certainty Factor Calculation
    #     dot.node('E', 'Calculate Certainty Factor')
    #     dot.edge('B', 'E')
    #     dot.edge('C', 'E')
    #     dot.edge('D', 'E')

    #     # Recommendations
    #     dot.node('F', 'Generate Top 5 Recommendations')
    #     dot.edge('E', 'F')

    #     return dot
    # def generate_decision_tree_html(self):
        tree_html = """
        <div class="tree">
            <ul>
                <li>
                    <a href="#">User Preferences</a>
                    <ul>
                        <li>
                            <a href="#">Budget</a>
                            <ul>
                                <li><a href="#">Low</a></li>
                                <li><a href="#">Medium</a></li>
                                <li><a href="#">High</a></li>
                            </ul>
                        </li>
                        <li>
                            <a href="#">Interest</a>
                            <ul>
                                <li><a href="#">Culture</a></li>
                                <li><a href="#">Nature</a></li>
                                <li><a href="#">Adventure</a></li>
                            </ul>
                        </li>
                        <li>
                            <a href="#">Province</a>
                            <ul>
                                <li><a href="#">Central</a></li>
                                <li><a href="#">Eastern</a></li>
                                <li><a href="#">North Central</a></li>
                                <li><a href="#">Northern</a></li>
                                <li><a href="#">North Western</a></li>
                                <li><a href="#">Sabaragamuwa</a></li>
                                <li><a href="#">Southern</a></li>
                                <li><a href="#">Uva</a></li>
                                <li><a href="#">Western</a></li>
                            </ul>
                        </li>
                    </ul>
                </li>
            </ul>
            <div class="decision-nodes">
                <div class="node">Calculate Certainty Factor</div>
                <div class="node">Generate Top 5 Recommendations</div>
            </div>
        </div>
        """
        return tree_html

expert_system = SriLankaTourismExpertSystem()

# @app.route('/decision_tree')
# def decision_tree():
#     dot = expert_system.generate_decision_tree()
#     dot.render('decision_tree', format='png', cleanup=True)
#     return send_file('decision_tree.png', mimetype='image/png')

@app.route('/decision_tree')
def decision_tree():
    tree_html = expert_system.generate_decision_tree_html()
    return render_template('decision_tree.html', tree_html=tree_html)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        budget = request.form['budget']
        interest = request.form['interest']
        province = request.form['province']
        
        recommendations = expert_system.get_recommendations(budget, interest, province)
        explanations = [expert_system.get_explanation((budget, interest, province), rec) for rec in recommendations]
        
        return render_template('results.html', recommendations=recommendations, explanations=explanations, zip=zip)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template
from rule_engine import create_rule, combine_rules, evaluate_rule
from database import save_rule, get_rules
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_rule', methods=['POST'])
def create_rule_api():
    rule_string = request.json.get('rule_string')
    if not rule_string:
        return jsonify({'error': 'Rule string is required'}), 400
    try:
        save_rule(rule_string)
        return jsonify({'message': 'Rule created successfully'})
    except Exception as e:
        print(f"Error saving rule: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/combine_rules', methods=['POST'])
def combine_rules_api():
    try:
        rules = request.json.get('rules')
        if not rules or not isinstance(rules, list):
            return jsonify({'error': 'Rules are required'}), 400
        combined_rule = combine_rules(rules)
        return jsonify({'combined_rule': combined_rule.__repr__(), 'rules': rules})
    except Exception as e:
        print(f"Error combining rules: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    try:
        user_data = request.json.get('data')
        if not user_data:
            return jsonify({'error': 'User data is required'}), 400
        # Assuming you have a function that can evaluate the rule based on user_data
        result = evaluate_rule(create_rule("(age > 30 AND department == 'Sales')"), user_data)
        return jsonify({'result': result})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)

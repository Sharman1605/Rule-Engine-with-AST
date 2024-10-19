from flask import Flask, request, jsonify, render_template
from models import db, Rule, RuleMetadata
import json
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data', 'rules.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Initialize the database
with app.app_context():
    db.create_all()

# Helper function to build AST (this can be customized further)
def create_rule(rule_string):
    # Dummy function to simulate AST creation, you can expand on this
    return {"type": "operator", "value": "AND", "left": {}, "right": {}}

# Route to display UI for rule creation
@app.route('/')
def index():
    return render_template('index.html')

# API to create a rule
@app.route('/api/create_rule', methods=['POST'])
def create_rule_api():
    rule_string = request.form['rule_string']
    description = request.form['description']
    created_by = request.form['created_by']

    ast = create_rule(rule_string)  # Simulate AST creation

    # Save rule and metadata to the DB
    rule = Rule(rule_string=rule_string, ast=json.dumps(ast))
    db.session.add(rule)
    db.session.commit()

    # Save the metadata associated with the rule
    metadata = RuleMetadata(rule_id=rule.id, description=description, created_by=created_by)
    db.session.add(metadata)
    db.session.commit()

    return jsonify({"status": "success", "rule_id": rule.id, "metadata_id": metadata.id})

# API to combine rules
@app.route('/api/combine_rules', methods=['POST'])
def combine_rules():
    rule_ids = request.form.getlist('rule_ids[]')
    rules = Rule.query.filter(Rule.id.in_(rule_ids)).all()

    # Dummy logic for combining rules (In practice, this should combine their ASTs)
    combined_ast = {"type": "operator", "value": "AND", "left": {}, "right": {}}

    return jsonify({"combined_ast": combined_ast})

# API to evaluate a rule
@app.route('/api/evaluate_rule', methods=['POST'])
def evaluate_rule():
    rule_id = request.form['rule_id']
    rule = Rule.query.get(rule_id)
    
    # Dummy evaluation based on the AST
    data = request.json  # Data to evaluate
    ast = json.loads(rule.ast)
    result = evaluate_ast(ast, data)  # Simulate AST evaluation
    
    return jsonify({"result": result})

def evaluate_ast(ast, data):
    # Dummy evaluation logic
    return True if data.get("age", 0) > 30 else False

if __name__ == '__main__':
    app.run(debug=True)

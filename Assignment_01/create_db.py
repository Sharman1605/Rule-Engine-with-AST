from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the Flask app
app = Flask(__name__)

# Set up the database path
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'data', 'rules.db')

# Ensure the 'data' directory exists
if not os.path.exists(os.path.join(basedir, 'data')):
    os.makedirs(os.path.join(basedir, 'data'))

# Configure the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database object
db = SQLAlchemy(app)

# Define a sample model for the rules
class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    condition = db.Column(db.String(200), nullable=False)

# Route to check if the app is running
@app.route('/')
def index():
    return "Welcome to the Rule Engine!"

# Run the application and create the database/tables if they don't exist
if __name__ == "__main__":
    # Create the database and tables
    with app.app_context():
        db.create_all()  # This will create the .db file and tables

    print(f"Database file created at: {db_path}")
    
    # Start the Flask server
    app.run(debug=True)


# Rule Management System

A Flask-based web application for creating, combining, and evaluating rules using Abstract Syntax Trees (AST). The system allows users to enter rules, store them in a database, and evaluate them based on provided data.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Structure](#database-structure)
- [UI](#ui)
- [License](#license)

## Features
- **Create Rules**: Users can create rules by entering a string, which is then stored in the database.
- **Combine Rules**: Combines multiple rules into a single Abstract Syntax Tree (AST) for evaluation.
- **Evaluate Rules**: Evaluates a given rule using a dummy data set for demonstration purposes.
- **UI for Rule Creation**: Simple user interface to enter and manage rules, built with Flask and HTML/CSS.
  
## Installation

### Prerequisites
- Python 3.8 or higher
- `pip` (Python package manager)
- A virtual environment is recommended.

### Steps
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # For Linux/Mac
    .venv\Scripts\activate     # For Windows
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:
    ```bash
    python app.py
    ```

5. Access the application at `http://127.0.0.1:5000`.

### Directory Structure
```bash
.
├── app.py                  # Main Flask app
├── models.py               # SQLAlchemy models for Rule and RuleMetadata
├── templates/
│   └── index.html          # Frontend HTML template
├── static/
│   └── style.css           # CSS file for styling
├── data/
│   └── rules.db            # SQLite database file
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Usage

### Running the Server
After installing the dependencies, run the following command to start the development server:
```bash
python app.py
```

You can access the UI at `http://127.0.0.1:5000`, where you can create, view, and delete rules.

### API Endpoints

#### 1. **Create a Rule**
   - **URL**: `/api/create_rule`
   - **Method**: `POST`
   - **Parameters**: 
     - `rule_string` (form-data): The rule string to create.
   - **Response**:
     - `status`: success or failure
     - `rule_id`: ID of the newly created rule.
  
#### 2. **Combine Rules**
   - **URL**: `/api/combine_rules`
   - **Method**: `POST`
   - **Parameters**:
     - `rule_ids[]` (form-data): List of rule IDs to combine.
   - **Response**: 
     - `combined_ast`: A dummy combined AST object.

#### 3. **Evaluate a Rule**
   - **URL**: `/api/evaluate_rule`
   - **Method**: `POST`
   - **Parameters**:
     - `rule_id` (form-data): The ID of the rule to evaluate.
     - Data (JSON): The data to evaluate the rule against.
   - **Response**: 
     - `result`: The evaluation result (True/False based on dummy logic).

## Database Structure

The app uses **SQLite** for persistent storage. It stores two main entities:

- **Rule**: Stores the rule string and the corresponding AST.
    - `id` (Integer, Primary Key)
    - `rule_string` (String): The rule text provided by the user.
    - `ast` (Text): Serialized AST (in JSON format).
    - `created_at` (DateTime): Timestamp of when the rule was created.
    - `updated_at` (DateTime): Timestamp of when the rule was last updated.

- **RuleMetadata**: Metadata associated with each rule.
    - `id` (Integer, Primary Key)
    - `rule_id` (Foreign Key): Reference to the `rules` table.
    - `description` (String): Short description of the rule.
    - `active` (Boolean): Whether the rule is active or not.
    - `created_by` (String): Name of the person who created the rule.

## UI

The user interface is built using HTML and CSS, providing a simple form for rule creation and listing existing rules. The UI includes:
- **Form**: To create a new rule.
- **Rule List**: Displays existing rules with the option to delete them.

To enhance the UI, custom styles have been added to ensure a modern look and feel, using Google Fonts and CSS for responsiveness.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

### Key Sections in the README:
1. **Features**: Lists out the main features of the project.
2. **Installation**: Explains how to set up the project locally.
3. **Usage**: Instructions on running the server and accessing the UI.
4. **API Endpoints**: Details the API routes available for rule creation, combination, and evaluation.
5. **Database Structure**: Explains the database models.
6. **UI**: Describes the user interface and its functionality.


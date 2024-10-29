from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for flash messages

# Database configuration
db_config = {
    'user': 'root',
    'password': 'shamanth@06',
    'host': 'localhost',
    'database': 'farmer_registration1'
}

# Route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/register-problem', methods=['POST'])
def register_problem():
    name = request.form.get('name')
    contact = request.form.get('contact')
    crop = request.form.get('crop')
    issue = request.form.get('issue')
    additional_info = request.form.get('additionalInfo')

    # Insert data into MySQL
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        query = """
            INSERT INTO problems1 (name, contact, crop, issue, additional_info)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, contact, crop, issue, additional_info))
        connection.commit()
        flash('Problem registered successfully!', 'success')
    except mysql.connector.Error as err:
        print(f"Error while inserting data: {err}")
        flash('Failed to register problem. Please try again.', 'error')
    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Initialize database connection
def init_db():
    conn = sqlite3.connect('golf.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            par INTEGER NOT NULL,
            slope_rating REAL NOT NULL,
            course_rating REAL NOT NULL
        );
    ''')
    conn.commit()
    conn.close()

# Add some example courses to the database
def add_courses():
    courses = [
        ('Pebble Beach', 72, 145, 74.5),
        ('Augusta National', 72, 137, 75.6),
        ('St. Andrews', 72, 140, 73.2)
    ]
    conn = sqlite3.connect('golf.db')
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO courses (name, par, slope_rating, course_rating) 
        VALUES (?, ?, ?, ?);
    ''', courses)
    conn.commit()
    conn.close()

# Fetch courses from the database
def get_courses():
    conn = sqlite3.connect('golf.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()
    conn.close()
    return courses

# Calculate strokes over par
def calculate_strokes(score, par):
    return score - par

# Calculate difficulty index
def calculate_difficulty(handicap, slope_rating, course_rating):
    return (handicap * slope_rating / 113) + (course_rating - 72)

# Route for the main page
@app.route('/')
def index():
    courses = get_courses()
    return render_template('index.html', courses=courses)

# Route for handling form submission
@app.route('/submit', methods=['POST'])
def submit():
    course_id = request.form['course']
    score = int(request.form['score'])
    handicap = float(request.form['handicap'])
    
    # Get course details from the database
    conn = sqlite3.connect('golf.db')
    cursor = conn.cursor()
    cursor.execute("SELECT par, slope_rating, course_rating FROM courses WHERE id = ?", (course_id,))
    course = cursor.fetchone()
    conn.close()
    
    par = course[0]
    slope_rating = course[1]
    course_rating = course[2]
    
    # Calculate results
    strokes_over_par = calculate_strokes(score, par)
    difficulty_index = calculate_difficulty(handicap, slope_rating, course_rating)
    
    # Display results
    return f"Strokes over par: {strokes_over_par}, Difficulty Index: {difficulty_index}"

if __name__ == '__main__':
    init_db()
    add_courses()
    app.run(debug=True)

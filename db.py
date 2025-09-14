import sqlite3
from datetime import datetime

DB_NAME = "habits.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_tables():
    db = connect()
    cursor = db.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS habits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        type TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        habit_id INTEGER,
        date TEXT,
        FOREIGN KEY (habit_id) REFERENCES habits (id)
    )
    """)

    db.commit()
    db.close()

# ----------------- HABIT FUNCTIONS -----------------

def add_habit(name, habit_type):
    """Add a new habit with its type (daily/weekly/monthly)."""
    db = connect()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO habits (name, type) VALUES (?, ?)", (name, habit_type))
        db.commit()
        print(f"✅ Habit '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"⚠️ Habit '{name}' already exists.")
    db.close()

def list_habits():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT name, type FROM habits")
    habits = cursor.fetchall()
    db.close()
    return habits

def log_habit(habit_name):
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT id FROM habits WHERE name = ?", (habit_name,))
    result = cursor.fetchone()
    if result:
        habit_id = result[0]
        today = datetime.today().strftime("%Y-%m-%d")
        cursor.execute("INSERT INTO logs (habit_id, date) VALUES (?, ?)", (habit_id, today))
        db.commit()
        print(f"✅ Logged '{habit_name}' for today!")
    else:
        print(f"⚠️ Habit '{habit_name}' does not exist.")
    db.close()

def get_progress(habit_name):
    db = connect()
    cursor = db.cursor()
    cursor.execute("""
        SELECT COUNT(*)
        FROM logs l
        JOIN habits h ON l.habit_id = h.id
        WHERE h.name = ?
    """, (habit_name,))
    count = cursor.fetchone()[0]
    db.close()
    return count

def get_timeline(habit_name):
    db = connect()
    cursor = db.cursor()
    cursor.execute("""
        SELECT l.date
        FROM logs l
        JOIN habits h ON l.habit_id = h.id
        WHERE h.name = ?
        ORDER BY l.date
    """, (habit_name,))
    dates = [row[0] for row in cursor.fetchall()]
    db.close()
    return dates

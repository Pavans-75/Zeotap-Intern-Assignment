import sqlite3

DATABASE = 'rules.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS rules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rule_string TEXT NOT NULL
            )
        ''')
        conn.commit()

def save_rule(rule_string):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO rules (rule_string) VALUES (?)", (rule_string,))
        conn.commit()

def get_rules():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT rule_string FROM rules")
        return [row['rule_string'] for row in cursor.fetchall()]

create_table()

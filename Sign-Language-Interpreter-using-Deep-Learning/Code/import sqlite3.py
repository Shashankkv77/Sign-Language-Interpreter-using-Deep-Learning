import sqlite3

# Use a raw string literal for the path
conn = sqlite3.connect(r'C:\Users\Dell\Downloads\Sign-Language-Interpreter-using-Deep-Learning-master\Sign-Language-Interpreter-using-Deep-Learning-master\Code\gesture_db.db')
cursor = conn.cursor()

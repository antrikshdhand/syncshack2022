
import sqlite3

connection = sqlite3.connect('database.db')

subjects = ("INFO1113", "ELEC1601", "MATH1023", "MATH1005")

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()


#NOTE MAKE SURE TO ADD SUBJECTS
cur.execute("INSERT INTO users (FirstName, LastName, PrefName, Email, Passw, UserStatus, Course, Faculty) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ('Jack', 'Quinlan', 'Jack', 'jqui7275@uni.sydney.edu.au', 'Password123!', 1, 'Software Engineering', 'School of Electrical Engineering'))

for subject in subjects:
    cur.execute("INSERT INTO enrolled (Email, UnitOfStudy) VALUES (?, ?)", 
                ("jqui7275@uni.sydney.edu.au", subject))

cur.execute("SELECT * FROM enrolled")

result = cur.fetchall()

for row in result:
    print(row, "\n")




connection.commit()
connection.close()

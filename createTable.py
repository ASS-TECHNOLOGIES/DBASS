import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    port=4306,
    user="root",
    passwd="password",
    database="StudyAssDB"
)

cursorObject = dataBase.cursor()

student = """CREATE TABLE IF NOT EXISTS Student (
    EMAIL VARCHAR(50) NOT NULL,
    NAME VARCHAR(50) NOT NULL,
    PASSWORD VARCHAR(255) NOT NULL,
    COURSE VARCHAR(70) NOT NULL,
    AVAILABILITY1 DATETIME NOT NULL,
    AVAILABILITY2 DATETIME,
    AVAILABILITY3 DATETIME,
    MODULE1 VARCHAR(50) NOT NULL,
    MODULE2 VARCHAR(50),
    MODULE3 VARCHAR(50),
    MODULE4 VARCHAR(50),
    MODULE5 VARCHAR(50),
    MODULE6 VARCHAR(50),
    FRIENDS1 VARCHAR(50),
    FRIENDS2 VARCHAR(50),
    FRIENDS3 VARCHAR(50),
    PRIMARY KEY (EMAIL)
)"""

registration = """CREATE TABLE IF NOT EXISTS Registration (
    REGISTRATIONID INT NOT NULL AUTO_INCREMENT,
    EMAIL VARCHAR(50) NOT NULL,
    MODULE VARCHAR(50) NOT NULL,
    PRIMARY KEY (REGISTRATIONID),
    CONSTRAINT fk_registration_student
        FOREIGN KEY (EMAIL) REFERENCES Student(EMAIL)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)"""

attendance = """
CREATE TABLE IF NOT EXISTS Attendance (
    ATTENDANCEID INT NOT NULL AUTO_INCREMENT,
    REGISTRATIONID INT NOT NULL,
    EMAIL VARCHAR(50) NOT NULL,
    NAME VARCHAR(50) NOT NULL,
    MODULE VARCHAR(100) NOT NULL,
    TOPIC VARCHAR(100) NOT NULL,
    SESSION_TIME DATETIME NOT NULL,
    PRIMARY KEY (ATTENDANCEID),
    CONSTRAINT fk_attendance_registration
        FOREIGN KEY (REGISTRATIONID) REFERENCES Registration(REGISTRATIONID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_attendance_student
        FOREIGN KEY (EMAIL) REFERENCES Student(EMAIL)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
"""

cursorObject.execute(student)
cursorObject.execute(registration)
cursorObject.execute(attendance)

print("Tables created successfully")

# Clear existing data
cursorObject.execute("DELETE FROM Attendance")
cursorObject.execute("DELETE FROM Registration")
cursorObject.execute("DELETE FROM Student")

cursorObject.execute("ALTER TABLE Attendance AUTO_INCREMENT = 1")
cursorObject.execute("ALTER TABLE Registration AUTO_INCREMENT = 1")

# Insert Students
studentData = [
    (
        "sarah@lancashire.ac.uk", "Sarah", "password123", "Software Engineering",
        "2026-03-20 14:00:00", "2026-03-22 11:00:00", "2026-03-24 15:00:00",
        "CSC101", "CSC202", None, None, None, None,
        "mia@lancashire.ac.uk", None, None
    ),
    (
        "mia@lancashire.ac.uk", "Mia", "password123", "Software Engineering",
        "2026-03-20 14:00:00", "2026-03-23 09:00:00", "2026-03-25 13:00:00",
        "CSC101", "CSC202", None, None, None, None,
        "sarah@lancashire.ac.uk", None, None
    ),
    (
        "adam@lancashire.ac.uk", "Adam", "password123", "Computer Science",
        "2026-03-20 14:00:00", "2026-03-22 14:00:00", None,
        "CSC101", None, None, None, None, None,
        None, None, None
    ),
    (
        "zara@lancashire.ac.uk", "Zara", "password123", "Computer Science",
        "2026-03-21 10:00:00", "2026-03-24 10:00:00", "2026-03-26 16:00:00",
        "CSC202", None, None, None, None, None,
        "noah@lancashire.ac.uk", None, None
    ),
    (
        "noah@lancashire.ac.uk", "Noah", "password123", "Software Engineering",
        "2026-03-21 10:00:00", "2026-03-23 12:00:00", None,
        "CSC202", None, None, None, None, None,
        "zara@lancashire.ac.uk", None, None
    )
]

studentInsert = """
INSERT INTO Student (
    EMAIL, NAME, PASSWORD, COURSE,
    AVAILABILITY1, AVAILABILITY2, AVAILABILITY3,
    MODULE1, MODULE2, MODULE3, MODULE4, MODULE5, MODULE6,
    FRIENDS1, FRIENDS2, FRIENDS3
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

cursorObject.executemany(studentInsert, studentData)

# Insert Registrations
registrationData = [
    ("sarah@lancashire.ac.uk", "CSC101"),
    ("mia@lancashire.ac.uk", "CSC101"),
    ("adam@lancashire.ac.uk", "CSC101"),
    ("zara@lancashire.ac.uk", "CSC202"),
    ("noah@lancashire.ac.uk", "CSC202")
]

registrationInsert = """
INSERT INTO Registration (EMAIL, MODULE)
VALUES (%s, %s)
"""

cursorObject.executemany(registrationInsert, registrationData)

dataBase.commit()

print("Tables created and dummy students + registrations inserted (Attendance empty).")

alexStudent = (
    "atdenton@lancashire.ac.uk",
    "Alex",
    "password123",
    "Software Engineering",
    "2026-03-20 14:00:00",
    "2026-03-22 11:00:00",
    "2026-03-24 15:00:00",
    "CSC101",
    "CSC202",
    None,
    None,
    None,
    None,
    "sarah@lancashire.ac.uk",
    None,
    None
)

studentInsert = """
INSERT INTO Student (
    EMAIL, NAME, PASSWORD, COURSE,
    AVAILABILITY1, AVAILABILITY2, AVAILABILITY3,
    MODULE1, MODULE2, MODULE3, MODULE4, MODULE5, MODULE6,
    FRIENDS1, FRIENDS2, FRIENDS3
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

cursorObject.execute(studentInsert, alexStudent)

dataBase.commit()

print("Added atdenton@lancashire.ac.uk to student table.")

dataBase.close()
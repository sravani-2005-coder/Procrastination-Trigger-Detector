from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize Database
def init_db():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT,
            task_type TEXT,
            planned_time TEXT,
            actual_time TEXT,
            mood TEXT,
            location TEXT,
            phone_nearby TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        subject = request.form["subject"]
        task_type = request.form["task_type"]
        planned_time = request.form["planned_time"]
        actual_time = request.form["actual_time"]
        mood = request.form["mood"]
        location = request.form["location"]
        phone_nearby = request.form["phone_nearby"]

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO tasks
            (subject, task_type, planned_time, actual_time, mood, location, phone_nearby)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (subject, task_type, planned_time, actual_time, mood, location, phone_nearby))

        conn.commit()
        conn.close()

        return redirect("/")

    # GET method
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    raw_tasks = cur.fetchall()
    conn.close()

    tasks = []
    total_delay = 0
    high_count = 0

    for task in raw_tasks:
        planned = task[3]
        actual = task[4]

        p_h, p_m = map(int, planned.split(":"))
        a_h, a_m = map(int, actual.split(":"))

        planned_minutes = p_h * 60 + p_m
        actual_minutes = a_h * 60 + a_m

        delay = max(0, actual_minutes - planned_minutes)

        if delay > 20:
            risk = "HIGH 🔴"
            high_count += 1
        elif delay > 5:
            risk = "MEDIUM 🟡"
        else:
            risk = "LOW 🟢"

        total_delay += delay
        tasks.append(task + (delay, risk))

    avg_delay = round(total_delay / len(tasks), 2) if tasks else 0
    delays = [task[8] for task in tasks]
    return render_template(
        "index.html",
        tasks=tasks,
        avg_delay=avg_delay,
        high_count=high_count,
        delays=delays
    )


if __name__ == "__main__":
    app.run(debug=True)

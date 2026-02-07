# Procrastination-Trigger-Detector
A system that identifies conditions under which a student delays starting tasks and actively suggests small interventions to reduce procrastination.
--> It collects small daily inputs 
When you plan a task, the project stores:
   - Subject name
   - Planned start time
   - Actual start time (or skipped)
   - Mood (good / ok / tired)
   - Location (home / hostel / library)
   - Task type (theory / problems)
   - No pressure. Just data.
--> It calculates delays
     - delay = actual_start_time − planned_start_time
This delay is called procrastination data.

<img width="450" height="577" alt="image" src="https://github.com/user-attachments/assets/f310f91d-58de-41ef-981f-02f64c25ea13" />

procrastination-detector/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── database.db

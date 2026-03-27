import sqlite3
from datetime import datetime

class TaskDatabase:
    def __init__(self, db_name='advanced_tasks.db'):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    status TEXT DEFAULT 'Pending',
                    deadline DATE
                )
            ''')
            db.commit()

    def add_task(self, title, deadline):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute('INSERT INTO tasks (title, deadline) VALUES (?, ?)', (title, deadline))
            db.commit()
            print(f"✅ Added: {title} (Due: {deadline})")

    def update_status(self, task_id, new_status='Completed'):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute('UPDATE tasks SET status = ? WHERE id = ?', (new_status, task_id))
            db.commit()
            print(f"🔄 Task #{task_id} updated to {new_status}.")

    def get_all_tasks(self):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM tasks ORDER BY deadline ASC')
            print("\n--- CURRENT TASK LIST ---")
            for row in cursor.fetchall():
                status_icon = "🟢" if row[2] == 'Completed' else "🟡"
                print(f"{status_icon} ID:{row[0]} | {row[1]} | Deadline: {row[3]}")
            print("------------------------\n")

if __name__ == "__main__":
    manager = TaskDatabase()
    manager.add_task("Send CV to Minsk IT companies", "2026-04-01")
    manager.add_task("Finish Python Portfolio", "2026-03-30")
    manager.get_all_tasks()
    # manager.update_status(1) # Раскомментируй, чтобы завершить задачу

import json
import os

TASKS_FILE = "todo.json"
HISTORY_FILE = "history.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Błąd odczytu pliku z zadaniami, zaczynam z pustą listą.")
            return []
    return []

def save_tasks(tasks):
    try:
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Błąd zapisu pliku z zadaniami: {e}")

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Błąd odczytu pliku historii, zaczynam z pustą historią.")
            return []
    return []

def save_history(history):
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Błąd zapisu pliku historii: {e}")

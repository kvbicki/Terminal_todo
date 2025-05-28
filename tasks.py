from datetime import datetime

PRIORITIES = ["niski", "średni", "wysoki"]

def list_tasks(tasks):
    if not tasks:
        print("Brak zadań na liście.")
        return
    print("\nTwoje zadania (posortowane wg wykonania i priorytetu):")
    # Sortowanie: najpierw niewykonane, potem wykonane, a w środku wg priorytetu i daty dodania
    sorted_tasks = sorted(
        tasks,
        key=lambda t: (t["done"], PRIORITIES.index(t["priority"]), t["created_at"])
    )
    for i, task in enumerate(sorted_tasks, 1):
        status = "[x]" if task["done"] else "[ ]"
        done_at = f", ukończono: {task['done_at']}" if task["done"] else ""
        print(f"{i}. {status} ({task['priority']}) {task['text']} (dodano: {task['created_at']}{done_at})")

def add_task(tasks):
    text = input("Podaj treść zadania: ").strip()
    if not text:
        print("Nie podano treści zadania.")
        return
    print("Priorytety do wyboru:")
    for i, p in enumerate(PRIORITIES, 1):
        print(f"{i}. {p}")
    try:
        p_choice = int(input("Wybierz priorytet (1-3): "))
        priority = PRIORITIES[p_choice - 1]
    except (ValueError, IndexError):
        print("Nieprawidłowy wybór priorytetu, ustawiam na 'średni'.")
        priority = "średni"

    task = {
        "text": text,
        "done": False,
        "priority": priority,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "done_at": None,
    }
    tasks.append(task)
    print(f'Dodano zadanie: "{text}" z priorytetem "{priority}".')

def complete_task(tasks, tasks_list, history):
    if not tasks:
        print("Brak zadań do oznaczenia.")
        return
    list_tasks(tasks)
    try:
        index = int(input("Podaj numer zadania do oznaczenia jako wykonane: ")) - 1
        if 0 <= index < len(tasks):
            if tasks[index]["done"]:
                print("To zadanie jest już oznaczone jako wykonane.")
                return
            tasks[index]["done"] = True
            tasks[index]["done_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Dodaj do historii
            history.append(tasks[index])
            print(f'Oznaczono zadanie "{tasks[index]["text"]}" jako wykonane.')
        else:
            print("Nieprawidłowy numer zadania.")
    except ValueError:
        print("Proszę podać prawidłowy numer.")

def delete_task(tasks):
    if not tasks:
        print("Brak zadań do usunięcia.")
        return
    list_tasks(tasks)
    try:
        index = int(input("Podaj numer zadania do usunięcia: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f'Usunięto zadanie: "{removed["text"]}".')
        else:
            print("Nieprawidłowy numer zadania.")
    except ValueError:
        print("Proszę podać prawidłowy numer.")

def edit_task(tasks):
    if not tasks:
        print("Brak zadań do edycji.")
        return
    list_tasks(tasks)
    try:
        index = int(input("Podaj numer zadania do edycji: ")) - 1
        if 0 <= index < len(tasks):
            task = tasks[index]
            print(f"Aktualna treść: {task['text']}")
            new_text = input("Podaj nową treść (enter, aby zostawić bez zmian): ").strip()
            if new_text:
                task['text'] = new_text
            print(f"Aktualny priorytet: {task['priority']}")
            print("Priorytety do wyboru:")
            for i, p in enumerate(PRIORITIES, 1):
                print(f"{i}. {p}")
            p_choice = input("Wybierz nowy priorytet (enter, aby zostawić): ").strip()
            if p_choice:
                try:
                    task['priority'] = PRIORITIES[int(p_choice) - 1]
                except (ValueError, IndexError):
                    print("Nieprawidłowy priorytet, pozostawiono stary.")
            print("Zadanie zaktualizowane.")
        else:
            print("Nieprawidłowy numer zadania.")
    except ValueError:
        print("Proszę podać prawidłowy numer.")

def list_history(history):
    if not history:
        print("Brak wykonanych zadań w historii.")
        return
    print("\nHistoria wykonanych zadań:")
    for i, task in enumerate(history, 1):
        print(f"{i}. {task['text']} (ukończono: {task['done_at']})")

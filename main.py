from tasks import (
    add_task, list_tasks, complete_task,
    delete_task, edit_task, list_history
)
from storage import load_tasks, save_tasks, load_history, save_history

def main():
    tasks = load_tasks()
    history = load_history()

    while True:
        print("\n To-do lista - MENU GŁÓWNE")
        print("1. Wyświetl zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz jako wykonane")
        print("4. Usuń zadanie")
        print("5. Edytuj zadanie")
        print("6. Historia wykonanych zadań")
        print("7. Wyjście")

        choice = input("Wybierz opcję (1-7): ").strip()

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            complete_task(tasks, tasks, history)
            save_tasks(tasks)
            save_history(history)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            edit_task(tasks)
            save_tasks(tasks)
        elif choice == "6":
            list_history(history)
        elif choice == "7":
            print("Do zobaczenia!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()

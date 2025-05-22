import json
import os

FILE_NAME = 'todo.json'

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def save_data(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=2)

def add_task(task):
    tasks = load_data()
    tasks.append({"task": task, "done": False})
    save_data(tasks)
    print(f'Tugas "{task}" Ditambahkan.')

def list_tasks():
    tasks = load_data()
    if not tasks:
        print("No tasks found.")
    for idx, t in enumerate(tasks):
        status = "Selesai" if t["done"] else "Tidak selesai"
        print(f"{idx+1}. {t['task']} - {status}")

def mark_done(index):
    tasks = load_data()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_data(tasks)
        print(f'Tugas "{tasks[index]["task"]}" Telah selesai.')
    else:
        print("Invalid task index.")

def delete_task(index):
    tasks = load_data()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_data(tasks)
        print(f'Tugas "{removed["task"]}" dihapus.')
    else:
        print("Invalid task index.")

def menu():
    while True:
        print("\nTo-Do List Menu")
        print("1. Tambahkan tugas")
        print("2. List Tugas")
        print("3. Tandai tugas selesai")
        print("4. Hapus tugas")
        print("5. Keluar")

        choice = input("Pilih Opsi Angka (1-5): ")
        if choice == '1':
            task = input("Masukan tugas: ")
            add_task(task)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            index = int(input("Masukan No tugas yang telah selesai: ")) - 1
            mark_done(index)
        elif choice == '4':
            index = int(input("Masukan No tugas yang akan dihapus: ")) - 1
            delete_task(index)
        elif choice == '5':
            print("Terima Kasih!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
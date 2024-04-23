import json
import os
from datetime import datetime

NOTES_FILE = "notes.json"
DATETIME_FORMAT = "%d.%m.%Y, %H:%M:%S"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    else:
        return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, ensure_ascii=False, indent=4)

def add_note(title, body):
    notes = load_notes()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "created_at": datetime.now().strftime(DATETIME_FORMAT),
        "last_modified": datetime.now().strftime(DATETIME_FORMAT)
    }
    notes.append(note)
    save_notes(notes)
    return note

def list_notes():
    notes = load_notes()
    if notes:
        print("Список заметок:")
        for note in notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Создана: {note['created_at']}")
    else:
        print("Заметок нет.")

def read_note(note_id):
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['body']}")
            print(f"Создана: {note['created_at']}")
            print(f"Последнее изменение: {note['last_modified']}")
            return note
    print("Заметка не найдена.")
    return None

def edit_note(note_id, title, body):
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            note['title'] = title
            note['body'] = body
            note['last_modified'] = datetime.now().strftime(DATETIME_FORMAT)
            save_notes(notes)
            return note
    print("Заметка не найдена.")
    return None

def delete_note(note_id):
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            return
    print("Заметка не найдена.")

if __name__ == "__main__":
    while True:
        print("Доступные команды: add(добавить), list(список), read(прочитать), edit(редактировать), delete(удалить), exit(выход)")
        command = input("Введите команду: ").strip().lower()

        if command == "add":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            add_note(title, body)
            print("Заметка успешно добавлена.")
        elif command == "list":
            list_notes()
        elif command == "read":
            note_id = int(input("Введите ID заметки: "))
            read_note(note_id)
        elif command == "edit":
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок: ")
            body = input("Введите новый текст: ")
            edit_note(note_id, title, body)
            print("Заметка успешно отредактирована.")
        elif command == "delete":
            note_id = int(input("Введите ID заметки для удаления: "))
            delete_note(note_id)
        elif command == "exit":
            print("Выход...")
            break
        else:
            print("Некорректная команда.")
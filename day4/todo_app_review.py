import sqlite3

DB_NAME = 'todo.db'

def create_db():
    with sqlite3.connect(DB_NAME) as conn:
        pass

def create_table():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS TODO("
            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "name TEXT,"
            "fin INTEGER)"
        )
        conn.commit()

def select_table():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM TODO")
        for row in cur:
            print(row)

def insert_table(task):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO TODO (name, fin) VALUES (?, 0)", (task,))
        conn.commit()

def update_table(task_id):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("UPDATE TODO SET fin = 1 WHERE id = ?", (task_id,))
        conn.commit()

def delete_table(task_id):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM TODO WHERE id = ?", (task_id,))
        conn.commit()

def main():
    create_db()
    create_table()

    loop = True
    while loop:
        print('ToDoApp')
        print('/show : タスク一覧表示')
        print('/add : タスク追加')
        print('/fin : タスク終了')
        print('/del : タスク削除')
        print('/end : アプリ終了')
        command = input('どの操作をしますか？')
        if command == '/show':
            select_table()
        elif command == '/add':
            task = input("タスク名: ")
            insert_table(task)
        elif command == '/fin':
            task_id = input("終了したIDを入力してください: ")
            update_table(task_id)
        elif command == '/del':
            task_id = input("削除するIDを入力してください: ")
            delete_table(task_id)
        elif command == "/end":
            print('Byebye')
            loop = False

if __name__ == "__main__":
    main()

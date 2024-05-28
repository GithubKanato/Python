import sqlite3

def create_db():
    dbname = 'todo.db'
    conn = sqlite3.connect(dbname)
    conn.close()

def create_table():
    dbname = 'todo.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS TODO(id INTEGER PRIMARY KEY AUTOINCREMENT,name STRING,fin INTEGER)")
    conn.commit()
    conn.close()

def select_table():
    dbname = 'todo.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("SELECT * FROM TODO")
    # 取得したデータを出力
    for row in cur:
        print(row)
    cur.close()
    conn.close()

def insert_table():
    dbname = 'todo.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    task = input("タスク名")
    cur.execute(f"INSERT INTO TODO(name,fin) VALUES('{task}',0)")
    conn.commit()
    cur.close()
    conn.close()

def update_table():
    dbname = 'todo.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    id = input("終了したIDを入力してください")
    cur.execute(f"UPDATE TODO SET fin = 1 WHERE id ={id}")
    conn.commit()
    cur.close()
    conn.close()

def delete_table():
    dbname = 'todo.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    id = input("削除するIDを入力してください")
    cur.execute(f"DELETE FROM TODO WHERE id ={id}")
    conn.commit()
    cur.close()
    conn.close()

def main():
    create_db()
    create_table()

    loop = True
    while loop == True:
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
            insert_table()
        elif command == '/fin':
            update_table()
        elif command == '/del':
            delete_table()
        elif command == "/end":
            print('Byebye')
            loop = False

if __name__ == "__main__":
    main()

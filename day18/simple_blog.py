from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, title TEXT, content TEXT) ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute('SELECT * FROM posts')
    posts = c.fetchall()
    conn.close()
    return render_template('index.html',posts=posts)

@app.route('/add', methods=['GET','POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conn = sqlite3.connect('blog.db')
        c = conn.cursor()
        c.execute('INSERT INTO posts (title, content) VALUES (?, ?)',(title,content))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_post.html')

@app.route('/delete/<int:id>')
def delete_post(id):
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute('DELETE FROM posts WHERE id = ?',(id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
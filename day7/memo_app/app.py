from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

# メモのリストを初期化
memo_list = []

@app.route('/')
def index():
    return render_template('index.html',memos=memo_list)

@app.route('/add',methods=['POST'])
def add_memo():
    memo = request.form.get('memo')
    if memo:
        memo_list.append(memo)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_memo(index):
    if 0 <= index < len(memo_list):
        del memo_list[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
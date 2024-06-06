import os
import time
import smtplib
import requests
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
import difflib

site_contents = 'day9/site_contents.txt'

def scraping():
    # スクレイピング対象のURLにリクエストを送る
    res = requests.get('https://news.yahoo.co.jp/')
    # レスポンスのHTMLからBeautifulSoupオブジェクトを作る
    soup = BeautifulSoup(res.text, 'html.parser')

    result = ""

    #テキスト取得
    for number in range(9):
        if number == 0:
            continue
        selector = f'#uamods-topics > div > div > div > ul > li:nth-child({number})'
        author_names = [n.get_text() for n in soup.select(selector)]
        result += str(author_names)
    
    return result
    
def has_content_changed(constents):
    f = open(site_contents, 'r',encoding='utf-8')
    data = f.read()
    f.close()

    diff = difflib.Differ()
    output_diff = diff.compare(constents.split(), data.split())
    f = open(site_contents, 'w',encoding='utf-8')
    f.write(constents)
    f.close()
    return output_diff
    
def createMIMEText(mail_from, mail_to, message, subject):
    message_str = ''.join(message)
    # MIMETextを作成
    msg = MIMEText(message_str, "html")
    # msg = MIMEText(message)
    # msg = MIMEText(message, "plain", 'utf-8')

    msg["Subject"] = subject
    msg["From"] = mail_from
    msg["To"] = mail_to
    msg['Date'] = formatdate()

    return msg

# メールの送り主
from_email = "detectiveboys710@gmail.com"
from_password = 'tmkr fkfb qtwp mcxc'

# メール送信先
to_email = "detectiveboys@outlook.com"

# メール件名とメール本文
subject = "差分"

def send_mail(msg):
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, from_password)
        server.send_message(msg)

def main():
    # ウェブサイトの取得と解析
    constents = scraping()
    # 変更の検出
    diff_content = has_content_changed(constents)

    mime = createMIMEText(from_email, to_email, diff_content, subject)
    send_mail(mime)

if __name__ == "__main__":
    main()
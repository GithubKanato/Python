import requests
from bs4 import BeautifulSoup


def scraping():
    # スクレイピング対象のURLにリクエストを送る
    res = requests.get('https://news.yahoo.co.jp/')
    # レスポンスのHTMLからBeautifulSoupオブジェクトを作る
    soup = BeautifulSoup(res.text, 'html.parser')

    #テキスト取得
    for number in range(9):
        if number == 0:
            continue
        selector = f'#uamods-topics > div > div > div > ul > li:nth-child({number})'
        author_names = [n.get_text() for n in soup.select(selector)]
        print(author_names)
    

def main():
    scraping()


if __name__ == "__main__":
    main()
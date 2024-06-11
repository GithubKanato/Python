import requests
import json

url = 'https://query1.finance.yahoo.com/v8/finance/chart/'
code_back = '.T'

def scrap_code():
    input_code = input("4桁の銘柄コードを入力してください: ")
    request_url = url + input_code + code_back
    
    try:
        response = requests.get(request_url)
        response.raise_for_status()  # HTTPエラーを確認
        data = response.json()
        
        price = data['chart']['result'][0]['meta']['regularMarketPrice']
        print("現在値:", price)

    except requests.exceptions.RequestException as e:
        print(f"HTTPリクエストエラー: {e}")
    except json.JSONDecodeError:
        print("レスポンスのJSONデコードエラー")
    except (KeyError, IndexError) as e:
        print(f"データの解析エラー: {e}")

def main():
    scrap_code()

if __name__ == "__main__":
    main()

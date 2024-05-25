def display_menu():
    print("連絡先管理アプリ")
    print("1. 連絡先の追加")
    print("2. 連絡先の表示")
    print("3. 連絡先の検索")
    print("4. 連絡先の削除")
    print("5. プログラムの終了")

def add_contact(contact):
    name = input("氏名:")
    tel = input("電話番号:")


def main():
    contact = {}
    display_menu()
    val = input("何をしますか？")
    while val != 5:
        if val == 1:
            add_contact(contact)
    

if __name__ == "__main__":
    main()
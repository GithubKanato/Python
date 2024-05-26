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
    contact[name] = tel
    return contact

def disp_contact(contact):
    if contact:
        for name, tel in contact.items():
            print(f"氏名：{name} , 電話番号：{tel}")
    else:
        print("連絡先は登録されていません")
    return contact

def search_contact(contact):
    search_word = input("誰の電話番号を知りたいですか？")
    if search_word in contact:
        print(f"{search_word}の電話番号は{contact[search_word]}です")
    else:
        print("登録されていません")

def delete_contact(contact):
    delete_name = input("誰の情報を消去しますか？")
    if delete_name in contact:
        contact.pop(delete_name)
        print(f"{delete_name}の連絡先を削除しました")
    else:
        print("登録されていません")
    return contact

def main():
    contact = {}
    loop_cnt = True
    while loop_cnt:
        display_menu()
        val = input("何をしますか？")
        if val == "1":
            contact = add_contact(contact)
        elif val == "2":
            contact = disp_contact(contact)
        elif val == "3":
            search_contact(contact)
        elif val == "4":
            contact = delete_contact(contact)
        elif val == "5":
            loop_cnt = False
        else:
            print("無効な選択です。もう一度お試しください。")

if __name__ == "__main__":
    main()

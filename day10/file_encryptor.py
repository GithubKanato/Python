from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    fernet = Fernet(key)
    return fernet

def encrypt_file(file_path,secret_key):
    with open(file_path,'rb') as file:
        original_data = file.read()
    encrypt_data = secret_key.encrypt(original_data)
    
    with open(file_path,'wb') as encrypt_file:
        encrypt_file.write(encrypt_data)

def decrypt_file(file_path,secret_key):
    with open(file_path,'rb') as file:
        encrypted_data = file.read()
    decrypt_data = secret_key.decrypt(encrypted_data)
    
    with open(file_path,'wb') as decrypt_file:
        decrypt_file.write(decrypt_data)

def main():
    # 秘密鍵の生成
    secret_key = generate_key()

    while True:
        print("\nオプションを選択してください:")
        print("1. ファイルを暗号化")
        print("2. ファイルを復号化")
        print("3. 終了")

        choice = input("選択肢を入力してください: ")

        if choice == "1":
            file_path = input("暗号化するファイルのパスを入力してください: ")
            if os.path.exists(file_path):
                encrypt_file(file_path, secret_key)
            else:
                print("ファイルが存在しません。")
        elif choice == "2":
            file_path = input("復号化するファイルのパスを入力してください: ")
            if os.path.exists(file_path):
                decrypt_file(file_path, secret_key)
            else:
                print("ファイルが存在しません。")
        elif choice == "3":
            print("プログラムを終了します。")
            break
        else:
            print("無効な選択肢です。")

if __name__=="__main__":
    main()
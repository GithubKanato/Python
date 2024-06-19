import random
import secrets
import string


def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    chars = ''
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += '%&$#()'
    
    return ''.join(secrets.choice(chars) for x in range(length))

def main():
    length = int(input("パスワードの長さを入力してください: "))
    use_uppercase = input("英大文字を含めますか？ (y/n): ").lower() == 'y'
    use_lowercase = input("英小文字を含めますか？ (y/n): ").lower() == 'y'
    use_digits = input("数字を含めますか？ (y/n): ").lower() == 'y'
    use_special = input("特殊文字を含めますか？ (y/n): ").lower() == 'y'
    
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        print(f"生成されたパスワード: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
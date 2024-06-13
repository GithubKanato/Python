import re

def count_words(text):
    pattern = r'\b\w+\b'
    repatter = re.compile(pattern)
    word = repatter.findall(text)
    for data in word:
        print(data,':',word.count(data))

def main():
    input_word = input("テキストを入力してください")
    count_words(input_word)

if __name__ == "__main__":
    main()
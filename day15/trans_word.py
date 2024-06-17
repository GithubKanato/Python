import googletrans

def trans(text):
    translator = googletrans.Translator()
    text_en = translator.translate(text,src='ja',dest='en').text
    print(text_en)

def main():
    input_word = input("翻訳したいテキストを入力してください\n")
    trans(input_word)

if __name__ == "__main__":
    main()
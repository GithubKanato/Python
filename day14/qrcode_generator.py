# ユーザーにQRコードに変換したいテキストまたはURLの入力を促す。
# qrcode ライブラリを使用してQRコードを生成。
# 生成したQRコードを画像ファイルとして保存。
# 保存先のファイル名をユーザーに通知。

import qrcode
import qrcode.constants

def generate_qrcode(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")

def main():
    input_data = input("urlを入力してください")
    generate_qrcode(input_data)


if __name__ == "__main__":
    main()

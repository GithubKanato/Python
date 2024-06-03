###
### 指定したフォルダ内のすべてのファイル名を一括で変更するスクリプト
###

import os
from tkinter import filedialog
import glob

def main():
    print("すべてのファイル名を変更するフォルダを指定してください。")
    input_folder = select_folder()
    if input_folder == '' :
        exit
    prefix = input("追加するプレフィックスを入力してください: ")
    for file in glob.glob(input_folder + "/*"):
        rename_file = os.path.basename(file)
        folder_name = os.path.dirname(file)
        os.rename(file,os.path.join(folder_name, prefix + rename_file))

def select_folder():
    dir = 'C:\\'
    fld = filedialog.askdirectory(initialdir = dir) 
    return fld

if __name__ == "__main__":
    main()
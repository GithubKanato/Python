# tkinterライブラリの読み込み
import tkinter

prev_number = ""
next_number = ""
operator = ""

def press_number_button(number):
    if label_disp["text"] == "Err":
        label_disp["text"] = number
    if operator != "":
        global next_number
        next_number = next_number + number
        label_disp["text"] = next_number
    else:
        global prev_number
        prev_number = str(prev_number) + number
        label_disp["text"] = prev_number    

def press_calc_button(calc):
    global operator
    operator = calc
    label_disp["text"] = ""

def press_calculation():
    result = 0
    if operator == "+":
        result = int(prev_number) + int(next_number)
    elif operator == "-":
        result = int(prev_number) - int(next_number)
    elif operator == "/":
        if int(next_number) == 0:
            label_disp["text"] = "Err"
        else:
            result = int(prev_number) / int(next_number)
    elif operator == "*":
        result = int(prev_number) * int(next_number)
    label_disp["text"] = result
    
def press_clear_button():
    global next_number 
    next_number = ""
    global prev_number
    prev_number = ""
    global operator
    operator = ""
    label_disp["text"] = ""

# ウィンドウの作成、Tkinterオブジェクトの取得
window = tkinter.Tk()

# ウィンドウのサイズだけを設定
width   = 300   # 横幅
height  = 450   # 高さ
window.geometry(f"{width}x{height}")

# 計算結果表示部
label_disp = tkinter.Label(text='',font=('Arial',20),background='white',width=10,height=2)
label_disp.grid(row=0,column=0,columnspan=4)

# クリアボタン
btn_clear =tkinter.Button(window, text="C",width=14,height=4,command=lambda:press_clear_button()).grid(row=1,column=0,columnspan=2)

# ボタンサイズ
btn_width = 7
btn_height = 4

# ウィンドウのボタンを設定
grid_row = 2
grid_col = 0
btn7 = tkinter.Button(window, text="7",width=btn_width,height=btn_height,command=lambda:press_number_button('7')).grid(row=grid_row,column=grid_col)
grid_col = grid_col + 1
btn8 = tkinter.Button(window, text="8",width=btn_width,height=btn_height,command=lambda:press_number_button('8')).grid(row=grid_row,column=grid_col)
grid_col = grid_col + 1
btn9 = tkinter.Button(window, text="9",width=btn_width,height=btn_height,command=lambda:press_number_button('9')).grid(row=grid_row,column=grid_col)
grid_col = grid_col + 1
btn_add =tkinter.Button(window, text="+",width=btn_width,height=btn_height,command=lambda:press_calc_button('+')).grid(row=grid_row,column=grid_col)
grid_col = 0
grid_row = grid_row + 1
btn4 = tkinter.Button(window, text="4",width=btn_width,height=btn_height,command=lambda:press_number_button('4')).grid(row=grid_row,column=grid_col)
grid_col = grid_col + 1
btn5 = tkinter.Button(window, text="5",width=btn_width,height=btn_height,command=lambda:press_number_button('5')).grid(row=grid_row,column=grid_col)
grid_col = grid_col + 1
btn6 = tkinter.Button(window, text="6",width=btn_width,height=btn_height,command=lambda:press_number_button('6')).grid(row=grid_row,column=grid_col)
grid_col = grid_col + 1
btn_sub =tkinter.Button(window, text="-",width=btn_width,height=btn_height,command=lambda:press_calc_button('-')).grid(row=grid_row,column=grid_col)
grid_col = 0
grid_row = grid_row + 1
btn1 = tkinter.Button(window, text="1",width=btn_width,height=btn_height,command=lambda:press_number_button('1')).grid(row=grid_row,column=grid_col)
grid_col = grid_col + 1
btn2 = tkinter.Button(window, text="2",width=btn_width,height=btn_height,command=lambda:press_number_button('2')).grid(row=grid_row,column=grid_col)
grid_col = grid_col + 1
btn3 = tkinter.Button(window, text="3",width=btn_width,height=btn_height,command=lambda:press_number_button('3')).grid(row=grid_row,column=grid_col)
grid_col = grid_col + 1
btn_multi =tkinter.Button(window, text="*",width=btn_width,height=btn_height,command=lambda:press_calc_button('*')).grid(row=grid_row,column=grid_col)
grid_col = 0
grid_row = grid_row + 1
btn0 = tkinter.Button(window, text="0",width=btn_width,height=btn_height,command=lambda:press_number_button('0')).grid(row=grid_row,column=grid_col)
grid_col = grid_col + 1
btn_equal =tkinter.Button(window, text="=",width=btn_width*2,height=btn_height,command=lambda:press_calculation()).grid(row=grid_row,column=grid_col,columnspan=2)
grid_col = grid_col + 1
grid_col = grid_col + 1
btn_div =tkinter.Button(window, text="/",width=btn_width,height=btn_height,command=lambda:press_calc_button('/')).grid(row=grid_row,column=grid_col)










# ウィンドウのループ処理
window.mainloop()
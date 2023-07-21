#1 calculator

import customtkinter
import tkinter
class Calculator(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #フォームサイズ設定
        self.geometry("400x500")
        self.title("Calculator")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.setup_form()

    def setup_form(self):
        #customtkinterのフォームデザイン
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        #計算用の文字列
        self.calc_str = '' 
        self.calc_var = customtkinter.StringVar()
        self.ans_var = customtkinter.StringVar()

        #数字表示エリア
        self.display_frame = customtkinter.CTkFrame(self)
        self.display_frame.grid(row=0, column=0, padx=10, pady=(20,10), sticky="wen")

        #数字表示
        self.display_label = customtkinter.CTkLabel(master=self.display_frame,textvariable=self.calc_var,font=("",55))
        self.display_label.pack(anchor=tkinter.E)

        #ボタンエリア
        self.button_frame = customtkinter.CTkFrame(self)
        self.button_frame.grid(row=1, column=0, padx=10, pady=10, sticky="wes")

        #ボタン設定
        button_width = 80
        button_height = 70
        row_num = 1
        self.button9 = customtkinter.CTkButton(master=self.button_frame,width=button_width,height=button_height,text="9",font=("",40),command= lambda:self.button_click("9"))
        self.button9.grid(row=row_num, column=2, padx=5, pady=5, sticky="we")
        self.button8 = customtkinter.CTkButton(master=self.button_frame,width=button_width,height=button_height,text="8",font=("",40),command= lambda:self.button_click("8"))
        self.button8.grid(row=row_num, column=1, padx=5, pady=5, sticky="we")
        self.button7 = customtkinter.CTkButton(master=self.button_frame,width=button_width,height=button_height,text="7",font=("",40),command= lambda:self.button_click("7"))
        self.button7.grid(row=row_num, column=0, padx=5, pady=5, sticky="we")
        row_num += 1
        self.button6 = customtkinter.CTkButton(master=self.button_frame,width=button_width,height=button_height ,text="6",font=("",40),command= lambda:self.button_click("6"))
        self.button6.grid(row=row_num, column=2, padx=5, pady=5, sticky="we")
        self.button5 = customtkinter.CTkButton(master=self.button_frame,width=button_width,height=button_height,text="5",font=("",40),command= lambda:self.button_click("5"))
        self.button5.grid(row=row_num, column=1, padx=5, pady=5, sticky="we")
        self.button4 = customtkinter.CTkButton(master=self.button_frame,width=button_width,height=button_height,text="4",font=("",40),command= lambda:self.button_click("4"))
        self.button4.grid(row=row_num, column=0, padx=5, pady=5, sticky="we")
        row_num += 1
        self.button3 = customtkinter.CTkButton(master=self.button_frame,width=button_width,height=button_height ,text="3",font=("",40),command= lambda:self.button_click("3"))
        self.button3.grid(row=row_num, column=2, padx=5, pady=5, sticky="we")
        self.button2 = customtkinter.CTkButton(master=self.button_frame,width=button_width,height=button_height,text="2",font=("",40),command= lambda:self.button_click("2"))
        self.button2.grid(row=row_num, column=1, padx=5, pady=5, sticky="we")
        self.button1 = customtkinter.CTkButton(master=self.button_frame,width=button_width,height=button_height,text="1",font=("",40),command= lambda:self.button_click("1"))
        self.button1.grid(row=row_num, column=0, padx=5, pady=5, sticky="we")
        row_num += 1
        self.button0 = customtkinter.CTkButton(master=self.button_frame,width=(button_width*2+10),height=button_height,text="0",font=("",40),command= lambda:self.button_click("0"))
        self.button0.grid(columnspan=2,row=row_num, column=0, padx=5, pady=5, sticky="w")
        self.buttondot = customtkinter.CTkButton(master=self.button_frame,width=button_width,height=button_height,text=".",font=("",40),command= lambda:self.button_click("."))
        self.buttondot.grid(row=row_num, column=2, padx=5, pady=5, sticky="w")

        self.button_clear= customtkinter.CTkButton(master=self.button_frame,width=(button_width*2+10),height=button_height,text="C",font=("",40),fg_color="lightblue",text_color="black",command= lambda:self.button_click("C"))
        self.button_clear.grid(columnspan=2,row=0, column=0, padx=5, pady=5, sticky="w")
        self.button_percent= customtkinter.CTkButton(master=self.button_frame,width=button_width,height=button_height,text="%",font=("",40),fg_color="lightblue",text_color="black",command= lambda:self.button_click("%"))
        self.button_percent.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        
        self.button_div= customtkinter.CTkButton(master=self.button_frame,width=button_width,height=button_height,text="÷",font=("",40),fg_color="orange",command= lambda:self.button_click("÷"))
        self.button_div.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        self.button_multi= customtkinter.CTkButton(master=self.button_frame,width=button_width,height=button_height,text="x",font=("",40),fg_color="orange",command= lambda:self.button_click("x"))
        self.button_multi.grid(row=1, column=3, padx=5, pady=5, sticky="w")
        self.button_sub= customtkinter.CTkButton(master=self.button_frame,width=button_width,height=button_height,text="-",font=("",40),fg_color="orange",command= lambda:self.button_click("-"))
        self.button_sub.grid(row=2, column=3, padx=5, pady=5, sticky="w")
        self.button_add= customtkinter.CTkButton(master=self.button_frame,width=button_width,height=button_height,text="+",font=("",40),fg_color="orange",command= lambda:self.button_click("+"))
        self.button_add.grid(row=3, column=3, padx=5, pady=5, sticky="w")
        self.button_eq= customtkinter.CTkButton(master=self.button_frame,width=button_width,height=button_height,text="=",font=("",40),fg_color="orange",command= lambda:self.button_click("="))
        self.button_eq.grid(row=4, column=3, padx=5, pady=5, sticky="w")

    def button_click(self, e):
        try:
            if str(e) == "=":
                answer = self.calc_str.replace("÷","/").replace("x","*")
                self.calc_str = str(eval(answer))
            elif str(e) == "C":
                self.calc_str = ""
            elif str(e) == "%":
                self.calc_str += str(e)
                answer = self.calc_str.replace("%","/100")
                self.calc_str = str(eval(answer))
            else:
                self.calc_str += str(e)
            self.calc_var.set(self.calc_str)
        except:
            self.calc_str = "Err"

#アプリケーション実行
if __name__=="__main__":
    app = Calculator()
    app.mainloop()

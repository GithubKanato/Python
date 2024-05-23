import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.prev_number = ""
        self.next_number = ""
        self.operator = ""
        self.label_disp = tk.Label(root, text='', font=('Arial', 20), background='white', width=10, height=2)
        self.label_disp.grid(row=0, column=0, columnspan=4)
        self.create_buttons(root)

    def press_number_button(self, number):
        if self.label_disp["text"] == "Err":
            self.label_disp["text"] = number
        if self.operator:
            self.next_number += number
            self.label_disp["text"] = self.next_number
        else:
            self.prev_number += number
            self.label_disp["text"] = self.prev_number    

    def press_calc_button(self, calc):
        self.operator = calc
        self.label_disp["text"] = ""

    def press_calculation(self):
        try:
            if self.operator == "+":
                result = float(self.prev_number) + float(self.next_number)
            elif self.operator == "-":
                result = float(self.prev_number) - float(self.next_number)
            elif self.operator == "/":
                if float(self.next_number) == 0:
                    self.label_disp["text"] = "Err"
                    return
                else:
                    result = float(self.prev_number) / float(self.next_number)
            elif self.operator == "*":
                result = float(self.prev_number) * float(self.next_number)
            self.label_disp["text"] = str(result)
        except ValueError:
            self.label_disp["text"] = "Err"
        self.prev_number = ""
        self.next_number = ""
        self.operator = ""

    def press_clear_button(self):
        self.prev_number = ""
        self.next_number = ""
        self.operator = ""
        self.label_disp["text"] = ""

    def create_buttons(self, root):
        btn_clear = tk.Button(root, text="C", width=14, height=4, command=self.press_clear_button)
        btn_clear.grid(row=1, column=0, columnspan=2)

        btn_texts = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3),
            ('0', 5, 0), ('=', 5, 1, 2), ('/', 5, 3)
        ]

        for (text, row, col, *colspan) in btn_texts:
            btn = tk.Button(root, text=text, width=7 if text != '=' else 14, height=4, 
                            command=lambda t=text: self.press_number_button(t) if t.isdigit() else self.press_calc_button(t) if t in '+-*/' else self.press_calculation())
            btn.grid(row=row, column=col, columnspan=colspan[0] if colspan else 1)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x450")
    app = Calculator(root)
    root.mainloop()

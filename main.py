import tkinter
from tkinter import *
from roman_to_integer import RomanToInteger


def user_interface():
    window = tkinter.Tk()
    window.title("Roman Numeral Converter")
    window.minsize(width=400, height=400)
    window.config(padx=50, pady=50)

    #  girdi yazısı
    roman_label = tkinter.Label(text="Enter the roman numeral:", font=("Arial", 18, "bold"))
    roman_label.grid(row=0, column=0, columnspan=2, pady=20)

    #  kullanıcı girişini alır
    text = tkinter.Entry(window, width=40)
    text.grid(row=1, column=0, columnspan=2, pady=10)

    #  sonuç yazısı
    result_label = tkinter.Label(window, text="Result:", font=("Arial", 18, "bold"))
    result_label.grid(row=3, column=0, columnspan=2, pady=20)

    converter = RomanToInteger()

    def calculate():
        roman_numeral = text.get()  # kullanıcıdan girilen rakamı alır ve class ile sonucu hesaplar
        result = converter.roman_to_integer(roman_numeral)
        if result is not None:
            result_label.config(text=f"{result}")
        else:
            result_label.config(text="Invalid Roman Numeral")

    calculate_button = tkinter.Button(text="Calculate", command=calculate)
    calculate_button.grid(row=2, column=1, padx=10, pady=5)

    def clear_text():
        text.delete(0, END)

    clear_button = tkinter.Button(text="Clear", command=clear_text)
    clear_button.grid(row=2, column=0, padx=10, pady=5)
    window.mainloop()


if __name__ == '__main__':
    user_interface()

import tkinter
from tkinter import END, W

FONT_TITLE = ("sans-seriff", 20, "bold")
FONT_GENERAL = ("sans_serif", 12, "normal")
result = ""


# def chose():
#     if (x.get() == 0):
#         print("You are Male")
#     elif (x.get() == 1):
#         print("You are Female")


def calculate():

    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())

        bmi = weight / (height**2)

        if bmi < 16:
            result_label.config(
                text=f"Result\nBMI : {round(bmi, 2)}\nSevere Thinness")
        elif bmi >= 16 and bmi <= 17:
            result_label.config(
                text=f"Result\nBMI : {round(bmi, 2)}\nModerate Thinness")
        elif bmi >= 17.5 and bmi <= 18.5:
            result_label.config(
                text=f"Result\nBMI : {round(bmi, 2)}\nMild Thinness")
        elif bmi >= 19 and bmi <= 25:
            result_label.config(text=f"Result\nBMI : {round(bmi, 2)}\nNormal")
        elif bmi >= 26 and bmi <= 30:
            result_label.config(
                text=f"Result\nBMI : {round(bmi, 2)}\nOverweight")
        elif bmi >= 31 and bmi <= 35:
            result_label.config(
                text=f"Result\nBMI : {round(bmi, 2)}\nObesse Class 1")
        elif bmi >= 36 and bmi <= 40:
            result_label.config(
                text=f"Result\nBMI : {round(bmi, 2)}\nObesse Class 2")
        elif bmi > 40:
            result_label.config(
                text=f"Result\nBMI : {round(bmi, 2)}\nObesse Class 3")

    except ValueError:
        pass


window = tkinter.Tk()
window.minsize(400, 400)
window.title("BMI Calculator")
window.config(padx=20, pady=20)

x = tkinter.IntVar()

# gender = ["male", "female"]

# for index in range(len(gender)):
#     gender_button = tkinter.Radiobutton(
#         window, text=gender[index], variable=x, value=index, padx=15, command=chose)
#     gender_button.pack(anchor=W)

# Label
title_label = tkinter.Label(text="BMI Calculator", font=FONT_TITLE)
age_label = tkinter.Label(text="Age")
ages_label = tkinter.Label(text="ages: 2-120")
gender_label = tkinter.Label(text="Gender")
height_label = tkinter.Label(text="Height")
weight_label = tkinter.Label(text="Weight")
result_label = tkinter.Label(text=f"Result\n{result}", font=FONT_TITLE)

title_label.grid(row=0, column=1, columnspan=2, pady=10)
age_label.grid(row=1, column=0, sticky=W, padx=10)
ages_label.grid(row=1, column=3, sticky=W, padx=10)
gender_label.grid(row=2, column=0, sticky=W, padx=10)
height_label.grid(row=3, column=0, sticky=W, padx=10)
weight_label.grid(row=4, column=0, sticky=W, padx=10)
result_label.grid(row=6, column=1, columnspan=2, pady=10)

# Radio Button
male_button = tkinter.Radiobutton(window, text="Male", variable=x, value=0)
female_button = tkinter.Radiobutton(window, text="Female", variable=x, value=1)
male_button.grid(row=2, column=1, pady=5)
female_button.grid(row=2, column=2, pady=5)

# Entry
age_entry = tkinter.Entry(width=34)
height_entry = tkinter.Entry(width=48)
weight_entry = tkinter.Entry(width=48)

age_entry.grid(row=1, column=1, columnspan=2, pady=5)
height_entry.grid(row=3, column=1, columnspan=3)
weight_entry.grid(row=4, column=1, columnspan=3)

# Button
calculate_button = tkinter.Button(
    text="Calculate", width=40, command=calculate)
clear_button = tkinter.Button(text="Clear", width=10)

calculate_button.grid(row=5, column=0, columnspan=3, pady=10)
clear_button.grid(row=5, column=3, pady=10)


window.mainloop()

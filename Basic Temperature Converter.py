import tkinter
from tkinter import *

start_temperature = ""
final_temperature = ""
temperature = 0


def from_celsius():
    global start_temperature
    start_temperature = "Celsius"

    text_temperature_from.delete(1.0, END)
    text_temperature_from.insert(INSERT, "FROM CELSIUS")


def from_fahrenheit():
    global start_temperature
    start_temperature = "Fahrenheit"

    text_temperature_from.delete(1.0, END)
    text_temperature_from.insert(INSERT, "FROM FAHRENHEIT")


def from_kelvin():
    global start_temperature
    start_temperature = "Kelvin"

    text_temperature_from.delete(1.0, END)
    text_temperature_from.insert(INSERT, "FROM KELVIN")


def to_celsius():
    global final_temperature
    final_temperature = "Celsius"

    text_temperature_to.delete(1.0, END)
    text_temperature_to.insert(INSERT, "TO CELSIUS")


def to_fahrenheit():
    global final_temperature
    final_temperature = "Fahrenheit"

    text_temperature_to.delete(1.0, END)
    text_temperature_to.insert(INSERT, "TO FAHRENHEIT")


def to_kelvin():
    global final_temperature
    final_temperature = "Kelvin"

    text_temperature_to.delete(1.0, END)
    text_temperature_to.insert(INSERT, "TO KELVIN")


def label_temperature_conversion():
    label_converted_temperature.pack()
    text_converted_temperature.pack()

    input_temperature = temperature_entry.get()

    text_converted_temperature.delete(1.0, END)

    global temperature

    if start_temperature == "Celsius" and final_temperature == "Celsius":
        temperature = float(input_temperature)
    elif start_temperature == "Celsius" and final_temperature == "Fahrenheit":
        temperature = float(input_temperature) * 1.8 + 32
    elif start_temperature == "Celsius" and final_temperature == "Kelvin":
        temperature = float(input_temperature) + 273.15

    if start_temperature == "Fahrenheit" and final_temperature == "Fahrenheit":
        temperature = float(input_temperature)
    elif start_temperature == "Fahrenheit" and final_temperature == "Celsius":
        temperature = (float(input_temperature) - 32) * 5/9
    elif start_temperature == "Fahrenheit" and final_temperature == "Kelvin":
        temperature = (float(input_temperature) - 32) * 5/9 + 273.15

    if start_temperature == "Kelvin" and final_temperature == "Kelvin":
        temperature = float(input_temperature)
    elif start_temperature == "Kelvin" and final_temperature == "Celsius":
        temperature = float(input_temperature) - 273.15
    elif start_temperature == "Kelvin" and final_temperature == "Fahrenheit":
        temperature = (float(input_temperature) - 273.15) * 9/5 + 32

    text_converted_temperature.insert(INSERT, input_temperature + " " + start_temperature + " = " + " "
                                      + str(temperature) + " " + final_temperature)


window_space = Tk()
window_space.geometry("890x650+500+200")
window_space.title("Temperature Convertor")
window_space.config(bg="#808080")
window_space.resizable(width=False, height=False)
window_space.iconphoto(False, tkinter.PhotoImage(file="temperature_image_icon.png"))

frame_space = Frame(window_space, width=860, height=630)
frame_space.place(x=14, y=10)
frame_space.pack_propagate(False)

label_choose_temperature = Label(frame_space, text="Select the temperature to convert from", font=("Courier", 20))
label_choose_temperature.pack()

celsius_button_from = Button(
    frame_space,
    text="Celsius",
    font=("Courier", 20),
    bg="#ADD8E6",
    width=10,
    command=from_celsius
)
celsius_button_from.place(x=6, y=50)

fahrenheit_button_from = Button(
    frame_space,
    text="Fahrenheit",
    font=("Courier", 20),
    bg="#fed8b1",
    width=10,
    command=from_fahrenheit
)
fahrenheit_button_from.place(x=338, y=50)

kelvin_button_from = Button(
    frame_space,
    text="Kelvin",
    font=("Courier", 20),
    bg="#94FF33",
    width=10,
    command=from_kelvin
)
kelvin_button_from.place(x=684, y=50)

label_final_temperature = Label(frame_space, text="Select the temperature to convert to", font=("Courier", 20))
label_final_temperature.pack(pady=100)

celsius_button_to = Button(
    frame_space,
    text="Celsius",
    font=("Courier", 20),
    bg="#ADD8E6",
    width=10,
    command=to_celsius
)
celsius_button_to.place(x=6, y=185)

fahrenheit_button_to = Button(
    frame_space,
    text="Fahrenheit",
    font=("Courier", 20),
    bg="#fed8b1",
    width=10,
    command=to_fahrenheit
)
fahrenheit_button_to.place(x=338, y=185)

kelvin_button_to = Button(
    frame_space,
    text="Kelvin",
    font=("Courier", 20),
    bg="#94FF33",
    width=10,
    command=to_kelvin
)
kelvin_button_to.place(x=684, y=185)

label_introduce_temperature = Label(frame_space, text="Introduce the temperature", font=("Courier", 20))
label_introduce_temperature.pack()

temperature_entry = Entry(
    frame_space,
    font=("Courier", 20),
    bg="#ffcccb"
)
temperature_entry.pack()

convert_button_temperature = Button(
    frame_space,
    text="Convert temperature",
    font=("Courier", 20),
    bg="#FFFFE0",
    command=label_temperature_conversion
)
convert_button_temperature.pack()

text_temperature_from = Text(frame_space, width=30, height=1, bg="#fed8b1", font=("Courier", 10))
text_temperature_from.pack(side=LEFT)

text_temperature_to = Text(frame_space, width=30, height=1, bg="#fed8b1", font=("Courier", 10))
text_temperature_to.pack(side=RIGHT)

label_converted_temperature = Label(frame_space, text="The temperature is", font=("Courier", 20))
text_converted_temperature = Text(frame_space, width=40, height=2, bg="#D3D3D3")

window_space.mainloop()

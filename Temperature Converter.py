import tkinter as tk


def convert_temperature():
    try:
        temperature = float(temperature_entry.get())
        original_unit = original_unit_var.get()

        if original_unit == "Celsius":
            fahrenheit = temperature * 9 / 5 + 32
            kelvin = temperature + 273.15
            output_label.config(text=f"{temperature:.2f}°C = {fahrenheit:.2f}°F = {kelvin:.2f}K")

        elif original_unit == "Fahrenheit":
            celsius = (temperature - 32) * 5 / 9
            kelvin = (temperature - 32) * 5 / 9 + 273.15
            output_label.config(text=f"{temperature:.2f}°F = {celsius:.2f}°C = {kelvin:.2f}K")

        elif original_unit == "Kelvin":
            celsius = temperature - 273.15
            fahrenheit = (temperature - 273.15) * 9 / 5 + 32
            output_label.config(text=f"{temperature:.2f}K = {celsius:.2f}°C = {fahrenheit:.2f}°F")

    except ValueError:
        output_label.config(text="Invalid input. Please enter a valid temperature value.")



root = tk.Tk()
root.title("Temperature Converter")


temperature_frame = tk.Frame(root)
temperature_frame.pack(pady=10)
temperature_label = tk.Label(temperature_frame, text="Enter Temperature:")
temperature_label.grid(row=0, column=0)
temperature_entry = tk.Entry(temperature_frame, width=10)
temperature_entry.grid(row=0, column=1)


original_unit_var = tk.StringVar(value="Celsius")
original_unit_label = tk.Label(temperature_frame, text="Original Unit:")
original_unit_label.grid(row=0, column=2)
original_unit_menu = tk.OptionMenu(temperature_frame, original_unit_var, "Celsius", "Fahrenheit", "Kelvin")
original_unit_menu.grid(row=0, column=3)


convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack()


output_label = tk.Label(root, text="")
output_label.pack(pady=10)

root.mainloop()

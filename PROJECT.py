import tkinter as tk
from tkinter import messagebox

def convert_units():
    try:
        value = float(entry_value.get())
        from_unit = from_var.get()
        to_unit = to_var.get()
        
        # Get the conversion method or rate
        conversion = conversion_rates.get((from_unit, to_unit))
        if callable(conversion):
            result = conversion(value)
        else:
            # Use custom rate if available or default rate
            custom_rate = float(entry_custom_rate.get())
            result = value * custom_rate
        
        label_result.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def set_units(from_unit, to_unit):
    from_var.set(from_unit)
    to_var.set(to_unit)
    conversion = conversion_rates.get((from_unit, to_unit), 1)
    
    # Set custom rate if it's not a callable (e.g., for non-temperature conversions)
    if not callable(conversion):
        entry_custom_rate.delete(0, tk.END)
        entry_custom_rate.insert(0, str(conversion))
    else:
        # For temperature conversions, disable the custom rate
        entry_custom_rate.delete(0, tk.END)
        entry_custom_rate.insert(0, "N/A")
        entry_custom_rate.config(state="disabled")
    
    # Re-enable if it's a non-temperature conversion
    if not callable(conversion):
        entry_custom_rate.config(state="normal")

# Dictionary for conversion rates, including custom large-unit conversions
conversion_rates = {
    ("Kilometers", "Miles"): 0.621371,
    ("Miles", "Kilometers"): 1.60934,
    ("Kilograms", "Pounds"): 2.20462,
    ("Pounds", "Kilograms"): 0.453592,
    ("Liters", "Gallons"): 0.264172,
    ("Gallons", "Liters"): 3.78541,
    ("Celsius", "Fahrenheit"): lambda c: (c * 9/5) + 32,
    ("Fahrenheit", "Celsius"): lambda f: (f - 32) * 5/9,
    # New custom unit conversions
    ("Kilometers", "Meters"): 1000,
    ("Meters", "Kilometers"): 0.001,
    ("Kilograms", "Grams"): 1000,
    ("Grams", "Kilograms"): 0.001,
    ("Liters", "Milliliters"): 1000,
    ("Milliliters", "Liters"): 0.001,
    ("Kilometers", "Centimeters"): 100000,
    ("Centimeters", "Kilometers"): 0.00001
}

# Create the main window
root = tk.Tk()
root.title("Custom Unit Converter")
root.configure(bg="lavender")

# Center the window
window_width = 400
window_height = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Style configuration
style = {"font": ("Arial", 14), "bg": "lavender"}
btn_style = {"font": ("Arial", 12), "bg": "#e6e6fa"}

# Widgets
tk.Label(root, text="Value:", **style).grid(row=0, column=0, pady=10)
entry_value = tk.Entry(root, font=("Arial", 14))
entry_value.grid(row=0, column=1, pady=10)

tk.Label(root, text="From:", **style).grid(row=1, column=0, pady=10)
from_var = tk.StringVar()
tk.Entry(root, textvariable=from_var, font=("Arial", 14)).grid(row=1, column=1, pady=10)

tk.Label(root, text="To:", **style).grid(row=2, column=0, pady=10)
to_var = tk.StringVar()
tk.Entry(root, textvariable=to_var, font=("Arial", 14)).grid(row=2, column=1, pady=10)

tk.Label(root, text="Custom Rate:", **style).grid(row=3, column=0, pady=10)
entry_custom_rate = tk.Entry(root, font=("Arial", 14))
entry_custom_rate.grid(row=3, column=1, pady=10)
entry_custom_rate.insert(0, "1")

tk.Button(root, text="Convert", command=convert_units, **btn_style).grid(row=4, column=0, columnspan=2, pady=20)
label_result = tk.Label(root, text="Result:", **style)
label_result.grid(row=5, column=0, columnspan=2, pady=10)

# Buttons for common conversions
tk.Button(root, text="Km to Miles", command=lambda: set_units("Kilometers", "Miles"), **btn_style).grid(row=6, column=0, pady=5)
tk.Button(root, text="Miles to Km", command=lambda: set_units("Miles", "Kilometers"), **btn_style).grid(row=6, column=1, pady=5)
tk.Button(root, text="Kg to Pounds", command=lambda: set_units("Kilograms", "Pounds"), **btn_style).grid(row=7, column=0, pady=5)
tk.Button(root, text="Pounds to Kg", command=lambda: set_units("Pounds", "Kilograms"), **btn_style).grid(row=7, column=1, pady=5)
tk.Button(root, text="Liters to Gallons", command=lambda: set_units("Liters", "Gallons"), **btn_style).grid(row=8, column=0, pady=5)
tk.Button(root, text="Gallons to Liters", command=lambda: set_units("Gallons", "Liters"), **btn_style).grid(row=8, column=1, pady=5)
tk.Button(root, text="Celsius to Fahrenheit", command=lambda: set_units("Celsius", "Fahrenheit"), **btn_style).grid(row=9, column=0, pady=5)
tk.Button(root, text="Fahrenheit to Celsius", command=lambda: set_units("Fahrenheit", "Celsius"), **btn_style).grid(row=9, column=1, pady=5)
# New buttons for large-to-small conversions
tk.Button(root, text="Km to M", command=lambda: set_units("Kilometers", "Meters"), **btn_style).grid(row=10, column=0, pady=5)
tk.Button(root, text="M to Km", command=lambda: set_units("Meters", "Kilometers"), **btn_style).grid(row=10, column=1, pady=5)
tk.Button(root, text="Kg to G", command=lambda: set_units("Kilograms", "Grams"), **btn_style).grid(row=11, column=0, pady=5)
tk.Button(root, text="G to Kg", command=lambda: set_units("Grams", "Kilograms"), **btn_style).grid(row=11, column=1, pady=5)
tk.Button(root, text="L to mL", command=lambda: set_units("Liters", "Milliliters"), **btn_style).grid(row=12, column=0, pady=5)
tk.Button(root, text="mL to L", command=lambda: set_units("Milliliters", "Liters"), **btn_style).grid(row=12, column=1, pady=5)
tk.Button(root, text="Km to Cm", command=lambda: set_units("Kilometers", "Centimeters"), **btn_style).grid(row=13, column=0, pady=5)
tk.Button(root, text="Cm to Km", command=lambda: set_units("Centimeters", "Kilometers"), **btn_style).grid(row=13, column=1, pady=5)

root.mainloop()










